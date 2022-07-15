---
title: "Python 安装和配置"
permalink: /installpy.html
categories: 'Solar Physics'
tags: [python, conda, jupyter, astropy, sunpy, install]
date: 2018-07-02 20:45:13
---
[<i class="fas fa-file-arrow-down"></i> Jupyter Notebook](/downloads/notebooks/installpy.zip)

<small><font color=gray>[Update 2022-07-12] Some outputs are updated with python 3.10.</font></small>

<!-- more -->

## 安装 python

### 安装 python 3

* 检查系统自带的版本:

```python
import sys
print(sys.version)
!{sys.executable} --version
```

    3.10.5 | packaged by conda-forge | (main, Jun 14 2022, 07:04:59) [GCC 10.3.0]
    Python 3.10.5


```bash
%%bash
python --version
python3 --version
```

    Python 3.10.5
    Python 3.10.5


### pip

#### 安装 pip

检查 pip 是否安装以及版本

```bash
%%bash
pip --version
```

    pip 22.1.2 from /home/lydia/miniconda3/lib/python3.10/site-packages/pip (python 3.10)


```bash
%%bash
python -m pip --version
```

    pip 22.1.2 from /home/lydia/miniconda3/lib/python3.10/site-packages/pip (python 3.10)


安装 (Ubuntu):

```bash
sudo apt-get install python3-pip
```

#### 用 pip 安装 python 包

```bash
pip install <package>
pip install --upgrade <package>
pip uninstall <package>
pip list
pip list --outdated
pip show <package>
```

安装到根目录 (不推荐!)

```bash
sudo -H pip install <package>
```

[选项]

| | |
|:---|:---|
| -U, --upgrade  | 升级, 配合 install 使用 |
| --force-reinstall  | 强制重新安装依赖 |
| -I, --ignore-installed | 强制安装 (无论是否已安装) |
| --no-cache-dir | 不生成cache |
| -i <font color=blue>*url*</font> | 使用指定源 (更改配置见 [pip 镜像源](#pip-镜像源)) |
| <font color=blue>*package*</font>==x.x.x | 指定版本, 错误版本号 (或为空) 将返回可用版本号 |
| "<font color=blue>*package*</font><x.x.x" | 指定小于某版本的最新版本, 必须有引号 |


检查包 (尝试导入, 查看包版本):

```bash
python -c "import <package>"
python -c "import <package>; print(<package>.__version__)"  # 版本号
python -c "import <package>; print(<package>.version)"  # 安装位置
```

#### 使 pip 安装 python 包到用户路径

```bash
%%bash
python -m site | grep 'USER_SITE'
```

    USER_SITE: '/home/lydia/.local/lib/python3.10/site-packages' (doesn't exist)
    ENABLE_USER_SITE: True


* 确认已创建用户包安装路径.<br>
* 在 `~/.bashrc` 中设置 `PATH` 变量:

```bash
export PATH=$HOME/.local/bin:$PATH
```

* 使用 `install` 或 `list` 时加上选项 <font color=red>--user</font> (注意: `uninstall` 不用)

> <font color=#b32425>*使用 Anaconda 路径下的 pip 时不需要这个选项*</font>

```bash
pip install --user <pkg_name>
pip list --user
pip list --outdated --user
```

### Anaconda

#### 安装 Anaconda 或 Miniconda (推荐)

* 安装 miniconda 64位 (默认安装到 <font color=blue>~/miniconda3/</font>)

  下载 <https://conda.io/miniconda.html>

```bash
bash Miniconda3-latest-Linux-x86_64.sh
```

* 在 `~/.bashrc` 加入如下语句:

```bash
export PATH=$HOME/miniconda3/bin:$PATH
. $HOME/miniconda3/etc/profile.d/conda.sh
```

&ensp;完成后执行:

```bash
source ~/.bashrc
```

* 安装好后先更新 conda 和 pip:

```bash
conda update conda pip
```

* 帮助

```bash
conda [cmd] --help
```

miniconda 下载 <https://conda.io/miniconda.html><br>
安装参考 <https://conda.io/docs/user-guide/install/index.html>

#### environment

默认环境为 base<br>
`-n, --name <env_name>` 指定环境

```bash
conda create --name <env_name> [<packages>] python=3.6
conda create --name <env_name> --clone base

# e.g.
conda create --name intel intelpython3_core python=3
```

```bash
# 删除环境
conda-env remove --name <env_name>
*
# 列出信息
conda info -e/--envs
conda-env list

# 进入环境
source activate <env_name>
conda activate <env_name>

# 离开环境
source deactivate
conda deactivate

# 在某环境中执行操作
conda <commands> --name <env_name>
```

#### 使用 conda 命令

```bash
conda info
conda list [<packages>]
conda search <package>
conda search <package> --info
conda install <packages>
conda update/upgrade <packages>
conda remove/uninstall <packages>
conda clean --all
```
见 `conda --help` 或 `conda cmd --help`, `conda search` 语法见 <https://github.com/conda/conda/blob/master/conda/models/match_spec.py>

配置:
```bash
# 安装确认时显示源的 url, 默认已开启
conda config --set show_channel_urls True

# 禁止每次更新自动检查 conda 的更新, 默认True
conda config --set auto_update_conda False

# 禁止源优先而使用版本优先, 默认True
conda config --set channel_priority False

# 增加设置, 例如增加源 (可使用 url 或别名)
conda config --add channels <channel>

# 删除某项设置的所有值, 例如删除所有自定义源
conda config --remove-key channels

# 删除某项设置的某个值, 例如删除某个源
conda config --remove channels <channel>
```

用户配置文件 `~/.condarc` (见 [conda 镜像源](#conda-镜像源))<br>
参考链接 <https://conda.io/docs/user-guide/configuration/use-condarc.html>

也可以在不同的环境用不同的配置文件: `~/miniconda3/envs/<env_name>/.condarc`

### 镜像源

#### pip 镜像源

用户配置文件:

```bash
%%bash
cat ~/.pip/pip.conf
```

    [global]
    index-url = <https://pypi.douban.com/simple>
    trusted-host = pypi.doubanio.com

#### conda 镜像源

```bash
conda config --add/--prepend channels <new_channel>
conda config --append channels <new_channel>
```

清华源:<br>
<https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/><br>
<https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/><br>
<https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/><br>

channels 的默认的优先级为: 前排优先<br>
镜像源中 `pkgs/main` 通常比 `pkgs/free` 新, 因此将其放在最前.<br>
或使用 `channel_priority: false`, 见上一节 [conda 设置](#使用-conda-命令).

e.g.

```bash
conda config --add channels <https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/>
```

此时 `~/.condarc` 的内容:

> channels:<br>
&emsp;- <https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/><br>
&emsp;- defaults

### Troubleshooting

#### conda 安装时指定源且禁用其他源

```bash
conda install <packages> -c <channel> --override-channels
```

#### Astropy 新版不再支持旧版 Python

```bash
pip install "astropy<3.0" # for python < 3.5
```

## 安装常用包

### numpy, scipy, matplotlib

```bash
conda install numpy
conda install scipy
conda install matplotlib
```
&ensp;Or
```bash
pip install numpy
pip install scipy
pip install matplotlib
```

配置启动文件 (Ubuntu), 在 `~/.bashrc` 中添加:
```bash
export PYTHONSTARTUP=$HOME/.pythonrc
```

```python
cat ~/.pythonrc
```

    # Python startup file
    # ~/.pythonrc
    import matplotlib.pyplot as plt
    from matplotlib import cm
    import numpy as np
    import os
    
    print(">>> import matplotlib.pyplot as plt")
    print(">>> from matplotlib import cm")
    print(">>> import numpy as np")
    print(">>> import os")
    
    try:
        from pprint import pprint
    except ImportError:
        pass
    else:
        print(">>> from pprint import pprint")
    
    # Tab completion & history
    try:
        import atexit, readline, rlcompleter
    except ImportError:
        pass
    else:
        readline.parse_and_bind('tab: complete') # Tab completion
        readline.parse_and_bind('''control-l:"    "''') # Indent, since TAB is occupied
        histfile = os.path.join(os.environ['HOME'], '.pyhistory') # History file
        try:
            readline.read_history_file(histfile)
        except IOError:
            pass
        atexit.register(readline.write_history_file, histfile)
        del histfile, readline, rlcompleter
        print("--- Tab completion: [ON] ---")
        print("--- History: [ON] ---")
        print("--- [Tab] -> [Ctrl+L] ---")


### Astropy, SunPy

```bash
conda install astropy
conda install sunpy -c conda-forge
```
&ensp;Or
```bash
pip install astropy
pip install sunpy[all] pytest
```

测试:

```python
>>> import astropy
>>> astropy.test()
```

```python
>>> import sunpy
>>> sunpy.self_test(online=False)
```

如果出错: '$USER'权限问题, 见下面修改 `~/.sunpy/sunpyrc` 说明.

查看包信息:

```bash
%%bash
conda search "conda-forge::sunpy>=4.0"
```

    Loading channels: ...working... done
    # Name                       Version           Build  Channel             
    sunpy                          4.0.0 py310hde88566_0  conda-forge         
    sunpy                          4.0.0  py38h71d37f0_0  conda-forge         
    sunpy                          4.0.0  py39hd257fcd_0  conda-forge         
    sunpy                          4.0.1 py310hde88566_0  conda-forge         
    sunpy                          4.0.1  py38h71d37f0_0  conda-forge         
    sunpy                          4.0.1  py39hd257fcd_0  conda-forge         
    sunpy                          4.0.2 py310hde88566_0  conda-forge         
    sunpy                          4.0.2  py38h71d37f0_0  conda-forge         
    sunpy                          4.0.2  py39hd257fcd_0  conda-forge         
    sunpy                          4.0.3 py310hde88566_0  conda-forge         
    sunpy                          4.0.3  py38h71d37f0_0  conda-forge         
    sunpy                          4.0.3  py39hd257fcd_0  conda-forge         


```bash
%%bash
conda search "sunpy 4.0.3 py310hde88566_0" --info
```

    Loading channels: ...working... done
    sunpy 4.0.3 py310hde88566_0
    ---------------------------
    file name   : sunpy-4.0.3-py310hde88566_0.tar.bz2
    name        : sunpy
    version     : 4.0.3
    build       : py310hde88566_0
    build number: 0
    size        : 5.7 MB
    license     : BSD-2-Clause
    subdir      : linux-64
    url         : <https://conda.anaconda.org/conda-forge/linux-64/sunpy-4.0.3-py310hde88566_0.tar.bz2>
    md5         : 5831b8fde0edd2aa0ff9f42b237b7ba2
    timestamp   : 2022-07-08 16:21:32 UTC
    dependencies: 
      - asdf >=2.8.0
      - asdf-astropy >=0.1.1
      - astropy >=4.1.0
      - beautifulsoup4 >=4.8.0
      - cdflib >=0.3.19,!=0.4.0
      - drms >=0.6.1
      - glymur >=0.8.18,!=0.9.0,!=0.9.5
      - h5netcdf >=0.8.1
      - h5py >=3.1.0
      - libgcc-ng >=12
      - matplotlib-base >=3.2.0
      - mpl_animators >=1.0.0
      - numpy >=1.21.6,<2.0a0
      - pandas >=1.0.0
      - parfive >=1.2.0
      - python >=3.10,<3.11.0a0
      - python-dateutil >=2.8.0
      - python_abi 3.10.* *_cp310
      - reproject
      - scikit-image >=0.16.0
      - scipy >=1.3.0
      - setuptools
      - sqlalchemy >=1.3.4
      - tqdm >=4.32.1
      - zeep >=3.4.0
    
    


用户文件位置: `~/.sunpy/sunpyrc`

```python
cat ~/.sunpy/sunpyrc
```

    [general]
    time_format = %Y-%m-%d %H:%M:%S
    working_dir = /home/lydia/sunpy-downloads
    
    [downloads]
    download_dir = /home/lydia/sunpy-downloads/data
    sample_dir = /home/lydia/sunpy-downloads/data/sample_data
    
    [database]
    url = sqlite:////home/lydia/sunpy-downloads/sunpydb.sqlite

```python
import sunpy
sunpy.util.system_info()
```

    ==============================
    sunpy Installation Information
    ==============================
    
    General
    #######
    OS: Ubuntu (18.04, Linux 4.19.128-microsoft-standard)
    Arch: 64bit, (x86_64)
    sunpy: 4.0.3
    Installation path: /home/lydia/miniconda3/lib/python3.10/site-packages/sunpy-4.0.3.dist-info
    
    Required Dependencies
    #####################
    astropy: 5.1
    numpy: 1.23.1
    packaging: 21.3
    parfive: 1.5.1
    
    Optional Dependencies
    #####################
    asdf: 2.12.0
    asdf-astropy: 0.2.1
    beautifulsoup4: 4.11.1
    cdflib: 0.4.4
    dask: 2022.7.0
    drms: 0.6.2
    glymur: 0.10.1
    h5netcdf: 0.0.0
    h5py: 3.7.0
    matplotlib: 3.5.2
    mpl-animators: 1.0.1
    pandas: 1.4.1
    python-dateutil: 2.8.2
    reproject: 0.8
    scikit-image: 0.19.3
    scipy: 1.8.1
    sqlalchemy: 1.4.39
    tqdm: 4.64.0
    zeep: 4.1.0


设置下载位置:<br>
(参考 <http://docs.sunpy.org/en/stable/guide/customization.html?=sunpy.config.set)>

e.g.
> [downloads]<br>
&emsp;download_dir = ...

```python
>>> import sunpy
>>> sunpy.config.set('downloads', 'download_dir',
                 '/home/<user>/<your_path>/sunpy-downloads/data')
```

退出后再进入 python 如果发现没有修改成功, 则需要手动修改 ~/.sunpy/sunpyrc 文件.<br>
不能用 '$USER' 代替具体的用户名 '<user\>'

### Jupyter

```bash
conda install jupyter -c conda-forge
```
&ensp;Or
```bash
pip install jupyter
```

```bash
%%bash
jupyter --path
```

    config:
        /home/lydia/.jupyter
        /home/lydia/.local/etc/jupyter
        /home/lydia/miniconda3/etc/jupyter
        /usr/local/etc/jupyter
        /etc/jupyter
    data:
        /home/lydia/.local/share/jupyter
        /home/lydia/miniconda3/share/jupyter
        /usr/local/share/jupyter
        /usr/share/jupyter
    runtime:
        /home/lydia/.local/share/jupyter/runtime


* 设置双击打开 \*.ipynb 文件


```bash
pip install nbopen
```

再执行:

Linux/BSD: <br>
```bash
python3 -m nbopen.install_xdg<br>
 ```   

Windows: <br>
```bash
python3 -m nbopen.install_win<br>
```

Mac: <br>
&ensp;Clone the repository (https://github.com/takluyver/nbopen.git)<br>
&ensp;and run `./osx-install.sh`<br><br>
之后即可在文件浏览器中选择文件的打开方式为 `Jupyter Notebook`.

> 注意可能会更改 bash 脚本的默认打开方式.

* Jupyter 插件集合<br>(https://github.com/ipython-contrib/jupyter_contrib_nbextensions)


```bash
conda install jupyter_contrib_nbextensions -c conda-forge
```
&ensp;Or
```bash
pip install jupyter_contrib_nbextensions
```
> This also automatically installs the Javascript and CSS files:<br>
`jupyter contrib nbextension install --sys-prefix`

安装好后将同时启用 `Nbextensions` 选项卡, 手动选择需要的插件, 
或者在命令行启用和禁用:

```bash
jupyter nbextension list # 查看
jupyter nbextension enable <path> # <path> 为上述 list 中的 <extension>/main
jupyter nbextension disable <path>
```

注意用如果 jupyter 安装在 conda 路径, 手动安装插件 (`jupyter nbextension install`) 时需要指定 <font color=red>--sys-prefix</font>

* notebook 主题 (https://github.com/dunovank/jupyter-themes)


```bash
pip install jupyterthemes
```

* 演示代码过程的插件 (https://github.com/lgpage/nbtutor)


```bash
conda install nbtutor -c conda-forge
```
&ensp;Or
```bash
pip install nbtutor
jupyter nbextension install --overwrite --py nbtutor
jupyter nbextension enable --py nbtutor
```

载入:

```python
# ipython/jupyter
%load_ext nbtutor
```
使用:<br>
CodeCell 中首行加入下面语句, 然后执行 Cell (numpy 等需要在 Cell 内导入)
```python
# ipython/jupyter
%%nbtutor -r -f
# 或
%%nbtutor -r -f -i  # 缩减显示
```

### 其他

* PeakUtils (http://peakutils.readthedocs.io/en/latest/)


```bash
git clone <https://bitbucket.org/lucashnegri/peakutils.git>
cd peakutils
python setup.py install
```

```python
>>> import peakutils
```

* LMfit-py (https://github.com/lmfit/lmfit-py)


```bash
conda install lmfit -c conda-forge
# 或
pip install lmfit
```

```python
>>> import lmfit
```

* HDF5包 (http://docs.h5py.org/en/latest/index.html)<br>


**pandas**
```bash
conda install pytables pandas
```
&ensp;Or
```bash
pip install tables pandas
```
<br><br>
**h5py** (http://docs.h5py.org/en/latest/index.html)
```bash
conda install h5py  # 推荐. 将同时安装 hdf5, 并得到 h5dump 等命令
```
&ensp;Or
```bash
pip install h5py  # 需要 sudo apt-get install libhdf5-dev
```

* CDF包<br>

安装 spacepy (https://pythonhosted.org/SpacePy)

或

```bash
pip install cdflib # <https://github.com/MAVENSDC/cdflib>
```

* EVTK (https://bitbucket.org/pauloh/pyevtk)


```bash
sudo apt-get install mercurial  # 得到 hg 命令

hg clone <https://bitbucket.org/pauloh/pyevtk>
cd pyevtk
python setup.py build --debug install
```

```bash
hg pull && hg update default # 更新
```

```python
>>> from evtk.hl import gridToVTK
```

* Mayavi (http://docs.enthought.com/mayavi/mayavi)

&emsp;需要先安装 cython (conda 或 pip)

```bash
pip install mayavi  # 将同时安装 vtk. (pip 是目前 mayavi 最保险的安装方式)
```
```bash
# shell
mayavi2
```
