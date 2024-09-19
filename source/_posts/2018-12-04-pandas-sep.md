---
title: "Pandas sep='\\s+' 的问题"
categories: 'Python Tips'
tags: [python, pandas]
date: 2018-12-04 17:00:03
---

Pandas 的 `read_table` ([官方文档](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_table.html))
和 `read_csv` ([官方文档](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_csv.html)) (指定分隔符的情况下两者无区别),
有关键字 `sep=` (`read_table` 默认为 `sep='\t'`, `read_csv` 默认为 `sep=','`).

但当需要指定多个空格的情况下, 指定 `sep='\s+'` 可能无法被正确识别.
<!-- more -->

请使用 **`' +'`** 代替.

官方文档中关于 `sep` 关键字的说明有如下描述:

> In addition, separators longer than 1 character and
> **different from ``'\s+'``** will be interpreted as regular expressions and
> will also force the use of the Python parsing engine.

指定 `sep='\s+'` 可能无法被正确识别, 

暂时的办法是:<br>
加上参数 `engine='python'`, 或使用 **`' +'`** 代替 (此时 `engine='python'`).<br>
如果设为 `engine='c'`, 速度较快, 但不便识别正则表达, 追求效率的话可以配合使用:<br>
`quoting=3` (即使用 `csv.QUOTE_NONE`)

---

Pandas 的读取方法简单介绍参见:
[用 pandas 读 csv](/advance.html#用-pandas-读-csv)