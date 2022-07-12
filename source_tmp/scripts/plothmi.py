#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Read FITS data & Plot
[Import] numpy, matplotlib, astropy, sunpy, usr_sunpy
[Example Data] https://pan.baidu.com/s/1nwsIcDr (pswd: s5re)
'''
# 2017-12-11 written by Lydia
# 2018-10-13 modified by Lydia

from __future__ import division, print_function

# import matplotlib
# matplotlib.use('Qt5Agg')  # 'Qt5Agg', 'TkAgg', 'Agg', ...

import matplotlib.pyplot as plt
import numpy as np

from astropy.coordinates import SkyCoord
import astropy.units as u
import sunpy.map

from copy import deepcopy
import os, time
import warnings

# [usr_sunpy] Funcions: read_sdo, plot_map, plot_vmap, image_to_helio, ...
import sys
sys.path.append('../modules')
from usr_sunpy import read_sdo, plot_map, plot_vmap, image_to_helio
from usr_sunpy import aiaprep_usr as aiaprep

#======================================================================|
# Global Parameters

# Data
fnames = ('data/hmi.B_720s.20150827_052400_TAI.field.fits',
          'data/hmi.B_720s.20150827_052400_TAI.inclination.fits',
          'data/hmi.B_720s.20150827_052400_TAI.azimuth.fits',
          'data/hmi.B_720s.20150827_052400_TAI.disambig.fits')

# Range of submap (arcsec)
xrange = (300., 800.) * u.arcsec
yrange = (-500., -100.) * u.arcsec

#======================================================================|
# Read data

print('[Path] %s' % os.getcwd())
print('Reading data...')
mapb, mapi, mapa, mapd = list(map(read_sdo, fnames))
# Disambiguate
# mapa.data[np.isfinite(mapd.data) & (mapd.data > 3)] += 180.
mapa.data[mapd.data > 3] += 180.

t0 = time.time()
mapbx = deepcopy(mapb)
mapby = deepcopy(mapb)
mapbz = deepcopy(mapb)
mapbx.data[:] = mapb.data * np.sin(np.deg2rad(mapi.data)) * np.cos(np.deg2rad(mapa.data + 270.))
mapby.data[:] = mapb.data * np.sin(np.deg2rad(mapi.data)) * np.sin(np.deg2rad(mapa.data + 270.))
mapbz.data[:] = mapb.data * np.cos(np.deg2rad(mapi.data))
print('(Time of getting Bvec: %f sec)' % (time.time() - t0))
# Suppress metadata warnings
for i in {mapbx, mapby, mapbz}:
    i.meta['hgln_obs'] = 0.

# rotate(CCW) & recenter & rescale
print('level 1 -> level 1.5 ...')
t0 = time.time()
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    mapbx = aiaprep(mapbx)
    mapby = aiaprep(mapby)
    mapbz = aiaprep(mapbz)
print('(Time of rotation: %f sec)' % (time.time() - t0))

# Check the center ('crpix1', 'crpix2')
# pixel number start from 1
pcenter = ((mapbz.meta['crpix1'] - 1) * u.pix, (mapbz.meta['crpix2'] - 1) * u.pix)
center = mapbz.pixel_to_world(*pcenter)
print('[Image_center]\n  (%.3f, %.3f) pixel = (%7.4f, %7.4f) arcsec\n  (lon, lat) = (%8.5f, %8.5f) deg' %
      ((mapbz.dimensions.x.value-1.)/2., (mapbz.dimensions.y.value-1.)/2.,
        mapbz.center.Tx.value, mapbz.center.Ty.value,
        mapbz.center.heliographic_stonyhurst.lon.value,
        mapbz.center.heliographic_stonyhurst.lat.value))
print('[Disk_center]\n  (%.3f, %.3f) pixel = (%7.4f, %7.4f) arcsec\n  (lon, lat) = (%8.5f, %8.5f) deg' %
      (pcenter[0].value, pcenter[1].value,
       center.Tx.value, center.Ty.value,
       center.heliographic_stonyhurst.lon.value,
       center.heliographic_stonyhurst.lat.value))
print('[Observation]\n  (lon, lat, radius) = (%g deg, %g deg, %g m)' %
      (mapbz.heliographic_longitude.value,
       mapbz.heliographic_latitude.value,
       mapbz.observer_coordinate.radius.value))

# Submap
subcoord = SkyCoord(xrange, yrange, frame=mapbz.coordinate_frame)
smapbx = mapbx.submap(subcoord)
smapby = mapby.submap(subcoord)
smapbz = mapbz.submap(subcoord)
print('Submap: (%s, %s) arcsec  (%d x %d)'
      % (xrange.value, yrange.value, *smapbz.data.shape[::-1]))

#======================================================================|
# Plot

fig1 = plt.figure(figsize=(8, 6), dpi=100)
ax1 = fig1.add_subplot(111, projection=mapbz)
plot_map(mapbz, ax=ax1, vmin=-2000., vmax=2000., grid_color='w')

# mapbz.draw_limb(axes=ax1, color='b', linewidth=1.5)
mapbz.draw_rectangle(subcoord[0], xrange[1]-xrange[0], yrange[1]-yrange[0],
                     axes=ax1, color='yellow', linewidth=1.5)

# Specify xlim, ylim by pixels
# lim_arcsec = ((-1000.1, 1000.1) * u.arcsec, (-1000.1, 1000.1) * u.arcsec)
# lim_pix = mapbz.world_to_pixel(SkyCoord(*lim_arcsec, frame=mapbz.coordinate_frame))  # pix
# ax1.set_xlim(lim_pix[0].value)  # pix
# ax1.set_ylim(lim_pix[1].value)  # pix

# Clip NaNs
valid_index = np.where(np.isfinite(mapbz.data))
ax1.set_xlim((valid_index[0].min()-100, valid_index[0].max()+100))  # pix
ax1.set_ylim((valid_index[1].min()-100, valid_index[1].max()+100))  # pix
fig1.savefig('plothmi_disk.png', dpi=200)

#----------------------------------------------------------------------|
fig2 = plt.figure(figsize=(9, 6), dpi=100)
ax2 = fig2.add_subplot(111, projection=smapbz)
im2 = plot_map(smapbz, ax=ax2, vmin=-2000., vmax=2000., grid=10*u.deg, title=mapbz.latex_name+' (submap)')
plot_vmap(smapbx, smapby, smapbz, ax2, cmin=20., vmax=500., cmap='binary',
          scale_units='xy', scale=1/0.05, minlength=0.02);
fig2.savefig('plothmi_sub.png', dpi=200)
#----------------------------------------------------------------------|
plt.show()
