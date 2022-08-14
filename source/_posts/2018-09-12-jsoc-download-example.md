---
title: "JSOC download example"
permalink: /jsoc-download-example.html
categories: 'Solar Physics'
tags: [python, jupyter, sunpy]
date: 2018-09-12 20:16:36
---
<p>
{% btn https://github.com/lydiazly/python-intro/raw/master/notebooks/fido.zip, Jupyter Notebook, download fa-fw %}
</p>


```python
import astropy.units as u
from sunpy.net import attrs, jsoc

# Suppress some warnings
import warnings
from astropy.utils.exceptions import AstropyDeprecationWarning
warnings.simplefilter("ignore", category=FutureWarning)
warnings.simplefilter("ignore", category=AstropyDeprecationWarning)
```

```python
# JSOC string: "aia.lev1_euv_12s[2014-10-26T10:00:00Z-2014-10-26T11:00:00Z@1m][193,304]{image}"
client = jsoc.JSOCClient()
response = client.search(
    attrs.jsoc.Time('2014-10-26T10:00:00', '2014-10-26T10:30:00'),
    attrs.jsoc.Notify('xxx@xxx'),  # email
    attrs.jsoc.Series('aia.lev1_euv_12s'),
    attrs.jsoc.Segment('image'),
    attrs.Sample(10. * u.min),  # interval
    attrs.jsoc.Wavelength(193 * u.AA) | attrs.jsoc.Wavelength(304 * u.AA)
)

response
```
<!-- more -->




<i>Table length=8</i>
<table id="table23026665135352" class="table-striped table-bordered table-condensed">
<thead><tr><th>T_REC</th><th>TELESCOP</th><th>INSTRUME</th><th>WAVELNTH</th><th>CAR_ROT</th></tr></thead>
<thead><tr><th>str20</th><th>str7</th><th>str5</th><th>int64</th><th>int64</th></tr></thead>
<tr><td>2014-10-26T10:00:01Z</td><td>SDO/AIA</td><td>AIA_2</td><td>193</td><td>2156</td></tr>
<tr><td>2014-10-26T10:10:01Z</td><td>SDO/AIA</td><td>AIA_2</td><td>193</td><td>2156</td></tr>
<tr><td>2014-10-26T10:20:01Z</td><td>SDO/AIA</td><td>AIA_2</td><td>193</td><td>2156</td></tr>
<tr><td>2014-10-26T10:30:01Z</td><td>SDO/AIA</td><td>AIA_2</td><td>193</td><td>2156</td></tr>
<tr><td>2014-10-26T10:00:01Z</td><td>SDO/AIA</td><td>AIA_4</td><td>304</td><td>2156</td></tr>
<tr><td>2014-10-26T10:10:01Z</td><td>SDO/AIA</td><td>AIA_4</td><td>304</td><td>2156</td></tr>
<tr><td>2014-10-26T10:20:01Z</td><td>SDO/AIA</td><td>AIA_4</td><td>304</td><td>2156</td></tr>
<tr><td>2014-10-26T10:30:01Z</td><td>SDO/AIA</td><td>AIA_4</td><td>304</td><td>2156</td></tr>
</table>



```python
requests = client.request_data(response)
```

```python
requests[0].id
```

```python
requests[0].status
```

如官网所述, 只有为'1'时才可以下载, 但有时还是'2'时也可以下 (可能是状态有延迟?).

总之如果发现下面的语句不能执行, 请再等一会再试.

```python
res = client.get_request(requests, path='./data', overwrite=True)
```

`overwrite` 默认为 False, 即跳过已存在的文件(即使该文件数据不全, 因此建议设为 True)

```python
res.wait() 
```

`.wait()` 将显示进度条, 结束后显示已下载的文件名. 如中途显示网络出错或中断这个语句, 再次执行该语句即可 (下载过程不受影响).

如果发现该 `.wait()` 卡死不动, 可以先结束该语句.<br>
(Jupyter 中的操作: 按 `Esc` 或点击页面空白处保证该 Cell 为命令模式而非编辑模式, 即左侧的竖条为蓝色, 然后按两次 `I` 即中断该 Cell).<br>
随后执行下面语句, 然后再回去执行 `.wait()` 看是否恢复.

```python
res.poke()
```
