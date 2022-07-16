---
title: "SunPy scripts updates"
categories: 'Solar Physics'
tags: [python, sunpy]
date: "2018-10-14 16:07:46 +0800"
---
Update:

<p align=left>
{% btn [nb], Jupyter Notebook, download fa-fw %}
{% btn [eg], Example Data, download fa-fw %}<br>
{% btn [mod], User Module, download fa-fw %} ([doc][doc])
</p>

[nb]: /downloads/notebooks/example_hmi.zip
[eg]: https://pan.baidu.com/s/1nwsIcDr?pwd=s5re
[mod]: /downloads/scripts/sunpy-modules.zip
[doc]: /usr_sunpy.html

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
