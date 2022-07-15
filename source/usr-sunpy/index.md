---
layout: page
title: "SunPy module documentation"
permalink: /usr_sunpy.html
author: "Lydia Zhang"
categories: 'Solar Physics'
tags: [python, sunpy]
date: 2018-10-14 16:37:05
---
<h1 id="usr_sunpy">usr_sunpy</h1>


User functions.
- SunPy Version: 0.9.3

------------------------------------------------------------------------

<h1 id="usr_sunpy.basic">usr_sunpy.basic</h1>


- SunPy Version: 0.9.3
- Reference <http://docs.sunpy.org/en/stable/code_ref/map.html>
- Change log:
  - 2018-10-11
    - Add `aiaprep_usr()`.

------------------------------------------------------------------------

<h2 id="usr_sunpy.basic.read_sdo">read_sdo</h2>

```python
read_sdo(filename)
```

Example of reading from a FITS file. Print the filename and dimensions.

[Returns] a sunpy `GenericMap` or subclass(e.g. `HMIMap`) object
- data - a 2D numpy `ndarray`
  data[i, j]: i from the bottom(y), j from te left(x).
- meta - a `dict` of the original image headr tags.

[See also]
- help(sunpy.map.GenericMap)
- [http://docs.sunpy.org/en/stable/code_ref/map.html#using-map-objects](http://docs.sunpy.org/en/stable/code_ref/map.html#using-map-objects)

--------------------------------------------------------------------

<h2 id="usr_sunpy.basic.tai">tai</h2>

```python
tai(*timestr)
```

Warp time strings as TAI time.

[Parameters]
- timestr: time strings
  e.g. '2010-01-01T00:00:00', '2010.01.01_00:00:00_TAI'

[Returns]
- len(timestr) == 1: a TAI `Time` object
- len(timestr) > 1: a list of TAI `Time` objects

[See also]
- [http://docs.astropy.org/en/stable/time/](http://docs.astropy.org/en/stable/time/)
- [http://docs.sunpy.org/en/stable/guide/time.html](http://docs.sunpy.org/en/stable/guide/time.html)

--------------------------------------------------------------------

<h2 id="usr_sunpy.basic.aiaprep_usr">aiaprep_usr</h2>

```python
aiaprep_usr(aiamap, order=3)
```

**Modified [`sunpy.instr.aia.aiaprep()`](https://docs.sunpy.org/en/latest/api/sunpy.instr.aia.aiaprep.html)**

Processes a level 1 `~sunpy.map.sources.sdo.AIAMap` into a level 1.5
`~sunpy.map.sources.sdo.AIAMap`. Rotates, scales and
translates the image so that solar North is aligned with the y axis, each
pixel is 0.6 arcsec across, and the center of the sun is at the center of
the image. The actual transformation is done by Map's
:meth:`~sunpy.map.mapbase.GenericMap.rotate` method.

This function is similar in functionality to aia_prep() in SSWIDL, but
it does not use the same transformation to rotate the image and it handles
the meta data differently. It should therefore not be expected to produce
the same results.

Parameters
----------
aiamap : `~sunpy.map.sources.sdo.AIAMap` instance
    A `sunpy.map.Map` from AIA

Returns
-------
newmap : A level 1.5 copy of `~sunpy.map.sources.sdo.AIAMap`

Notes
-----
This routine makes use of Map's :meth:`~sunpy.map.mapbase.GenericMap.rotate`
method, which modifies the header information to the standard PCi_j WCS
formalism.
The FITS header resulting in saving a file after this procedure will
therefore differ from the original file.

--------------------------------------------------------------------

<h1 id="usr_sunpy.plot">usr_sunpy.plot</h1>


- SunPy Version: 0.9.3
- Reference [http://docs.sunpy.org/en/stable/code_ref/map.html](http://docs.sunpy.org/en/stable/code_ref/map.html)
- Change log:
  - 2018-10-11
    - Change parameter list of `plot_map()`, `plot_vmap()`, `proj_matrix()`.
    - Change return value of `_get_image_params()` from a tuple to a dict.
    - Adjust positions of colorbar & title.
    - Fix docs.

------------------------------------------------------------------------

<h2 id="usr_sunpy.plot.plot_map">plot_map</h2>

```python
plot_map(smap, ax=None, coords=None, annotate=True, title=True, colorbar=True, grid=True, grid_color='yellow', grid_ls=':', grid_lw=0.8, grid_alpha=0.5, **kwargs)
```

Plot image.

[Plot Function]
- plot_map(smap, **kwargs) -> use smap.plot(), `imshow` from matplotlib
- plot_map(smap, coords=(X, Y), **kwargs) -> `pcolormesh` from matplotlib

[Parameters]
- smap: a sunpy `GenericMap`
- ax: a matplotlib `Axes` object
- coords: tuple or list of `ndarray`s: (X, Y)
- grid: bool or `~astropy.units.Quantity`(spacing), zorder = 90
- grid_color: grid color
- grid_ls: grid line stlye
- grid_lw: grid line width
- grid_alpha: grid alpha
- cmap: name of color map
- kwargs: dict, matplotlib kwargs
  If coords is None(default), use kwargs of `imshow`,
  else of `pcolormesh`.

[Returns] a matplotlib image object

[See also]
[http://docs.sunpy.org/en/stable/code_ref/map.html#sunpy.map.mapbase.GenericMap.plot](http://docs.sunpy.org/en/stable/code_ref/map.html#sunpy.map.mapbase.GenericMap.plot)

--------------------------------------------------------------------

<h2 id="usr_sunpy.plot.plot_vmap">plot_vmap</h2>

```python
plot_vmap(mapu, mapv, mapc, ax=None, coords=None, cmap='binary', iskip='auto', jskip='auto', cmin=0.0, cmax=None, vmin=None, vmax=1000.0, scale_units='xy', scale=20.0, minlength=0.05, width=0.003, headlength=6.5, headwidth=5, headaxislength=3.5, **kwargs)
```

Quiver plot of (U, V).

[Plot Function] `quiver` from matplotlib, zorder(default) = 100

[Parameters]
- mapu: a sunpy `GenericMap` of U
- mapv: a sunpy `GenericMap` of V
- mapc: a sunpy `GenericMap` to set color values
- ax: matplotlib axes object
- coords: tuple or list of 2D `ndarray`s: (X, Y)
- iskip, jskip: 'auto' or number of skipped points
- cmin: where mapc.data < cmin => set U, V to zero
- cmax: where mapc.data > cmax => set U, V to zero
- vmin: clip norm(U, V) to vmin
- vmax: clip norm(U, V) to vmax
- cmap: name of a color map
- scale_units, ..., **kwargs: kwargs of `quiver`

[Returns] a matplotlib `artist`(image object)

[See also]
[https://matplotlib.org/devdocs/api/_as_gen/matplotlib.axes.Axes.quiver.html#matplotlib-axes-axes-quiver](https://matplotlib.org/devdocs/api/_as_gen/matplotlib.axes.Axes.quiver.html#matplotlib-axes-axes-quiver)

--------------------------------------------------------------------

<h2 id="usr_sunpy.plot.image_to_helio">image_to_helio</h2>

```python
image_to_helio(*smap)
```

Transform maps from image-coordinate to helio-coordinate.
- Helo-coordinate: Helioprojective(Cartesian) system
- Matrix: A22 or A33 get from `usr_sunpy.proj_matrix`
- Unit: arcsec

[Parameters]
- smap: `GenericMap`, one or three elements.
  - For scalar: `image_to_helio(smap)`
  - For vectors: `image_to_helio(smapx, smapy, smapz)`

[Returns]
- For scalar: x_h, y_h (type: `ndarray`)
- For vectors: smapx_h, smapy_h, smapz_h (type: `GenericMap`)

[See also]
[http://docs.sunpy.org/en/stable/code_ref/coordinates.html#sunpy-coordinates](http://docs.sunpy.org/en/stable/code_ref/coordinates.html#sunpy-coordinates)

--------------------------------------------------------------------

<h2 id="usr_sunpy.plot.proj_matrix">proj_matrix</h2>

```python
proj_matrix(P, L0, B0, Lc, Bc, *dim)
```

- For coords: (x, y)_helio = A22.T.I * (x, y)_image
- For vectors: (U, V, W)_helio = A33 * (U, V, W)_image

 A33 = [[a11, a12, a13],
        [a21, a22, a23],
        [a31, a32, a33]]

[Parameters]
-  P: the angle of the northern extremity, CCW from the north point of the disk.
- L0: the longitude of the center of the disk.
- B0: the latitude of the center of the disk.
- Lc: the longitude of the the referenced point.
- Bc: the latitude of the referenced point.

[Returns] elements of a 2D array
        (use values instead of arrays just for easy reading & comparison)
- default: a11, a12, a13, a21, a22, a23, a31, a32, a33
-   dim=2: a11, a12, a21, a22

[Reference]
[http://link.springer.com/10.1007/BF00158295](http://link.springer.com/10.1007/BF00158295)

--------------------------------------------------------------------