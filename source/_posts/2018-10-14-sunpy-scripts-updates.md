---
title: "SunPy Scripts Updates"
categories: 'Solar Physics'
tags: [python, sunpy]
date: "2018-10-14 16:07:46 +0800"
---
Update:

<p>
{% btn https://github.com/lydiazly/python-intro/raw/master/notebooks/example_hmi.zip, Jupyter Notebook, download fa-fw %} <wbr>
{% btn https://pan.baidu.com/s/1nwsIcDr?pwd=s5re, Example Data, download fa-fw %} <wbr>
{% btn https://github.com/lydiazly/python-intro/raw/master/sunpy-modules.zip, User Module, download fa-fw %}<nobr> (<a href="https://github.com/lydiazly/scripts-sunpy/tree/master/modules">source</a> / <a href="/usr_sunpy.html">doc</a>)
</p>

[ Tested ]

Ubuntu 16.04 LTS

Date|Python|Sunpy|NumPy|SciPy|Matplotlib|Astropy|Pandas
:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:
2018-10-13|3.6.6|**0.9.3**|1.15.2|1.1.0|3.0.0|3.0.4|0.23.4

- Add `aiaprep_usr()`.
- Change parameter list of `plot_map()`, `plot_vmap()`, `proj_matrix()`.
- Change return value of `_get_image_params()` from a tuple to a dict.
- Adjust positions of colorbar & title.
- Fix docs.
