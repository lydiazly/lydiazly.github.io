---
title: "Python 的脚本与交互式环境"
categories: python
tags: python
date: 2018-10-15 22:46:01
---

目的是从交互环境调用脚本产生的变量, 可用于调试脚本和测试数据等等.
<!-- more -->

比如当前目录下有一个包含如下内容的脚本:

``` python
#!/usr/bin/env python
a=1
print('a =', a)
```

### 方法 1. shell -> interactive mode (推荐)

使用 `-i` 选项:

```bash
# shell
$ python -i test.py
```

执行结束随即进入 python 交互环境, 并且保留了脚本中定义的变量:

```python
# python
a = 1
>>> a
1
```

### 方法 2. In ipython / jupyter (第二推荐)

```python
# ipython
In [1]: %run test.py
a = 1

In [2]: a
Out[2]: 1

In [3]: %who
a

In [4]: %whos
Variable   Type    Data/Info
----------------------------
a          int     1
```

### 方法 3. In interactive mode

> **NOTE**: Python 3 取消了 `execfile()` 这个函数! 如今使用 `exec()`.

```python
# python
>>> exec(open('test.py').read())
a = 1
>>> a
1
>>> 'a' in dir()
True
>>> globals()['a']  # same as vars()['a']
1
```

但这之后文件并没有关闭, 虽然多数时候没有影响, 但如果实在要关闭, 建议使用 `with` :

```python
# python
with open('test.py') as f:
    exec(f.read())  # ctrl+D to exit the block
```

总之十分不方便, 因此不推荐.
<br><br>
对于没有使用 `if __name__ == "__main__"` 的脚本, 当脚本处在当前目录或 `$PYTHONPATH` 中时, 也可以有比较方便的办法<br>(
注意这里因为是调用 module 的形式, 所以不要加 '.py' ):

```python
# python
>>> import test
a = 1
```

<br>
补充说明在 python 交互环境中查看当前环境中的变量的方法 (ipython / jupyter 使用 `%who`, `%whos` 即可):

```python
dir()  # without an argument, return the names in the current scope
globals()  # a dictionary containing the current scope's global variables
locals()  # a dictionary containing the current scope's local variables
vars()  # without arguments, equivalent to locals();
        # with an argument, equivalent to object.__dict__.
```
