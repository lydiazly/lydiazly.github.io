---
title: Limit the memory usage in Windows 10 WSL2
date: 2022-07-16 14:56:11
categories: 'Miscellaneous'
tags: [wsl2, powershell]
---

## Limit the memory usage

It was annoying that WSL2 was always eating up my poor RAM.
The following solution worked. [[Reference](https://www.aleksandrhovhannisyan.com/blog/limiting-memory-usage-in-wsl-2/)]

My distribution is:

```powershell
> wsl -l -v
  NAME            STATE           VERSION
* Ubuntu-18.04    Running         2
```

Create a configure file named `.wslconfig` in your user directory in Windows.

Open PowerShell as administrator, shutdown WSL2 and edit the file:

```powershell
> wsl --shutdown
> notepad "$env:USERPROFILE\.wslconfig"
```

For me the content is:

```text
[wsl2]
memory=2GB
swap=0
```

<!-- more -->

After these steps, the memory usage of my WSL2 never bothered me again.

## Compact the virtual disk

This file always occupies a huge amount of space: `%USERPROFILE%\AppData\Local\Packages\CanonicalGroupLimited.Ubuntu18.04onWindows_*\LocalState\ext4.vhdx`. It's because WSL2 won't actually release the space after files are deleted. The solution is to compact the virtual disk to reduce its size as follows. [[Reference](https://github.com/microsoft/WSL/issues/4699)]

Open PowerShell as Administrator:

```powershell
> wsl --shutdown
> diskpart

# Replace <user> and <pkg> by yours. Must be a full path.
DISKPART> select vdisk file="C:\Users\<user>\AppData\Local\Packages\CanonicalGroupLimited.<pkg>\LocalState\ext4.vhdx"
  DiskPart successfully selected the virtual disk file.

# Compact and wait for several minutes
DISKPART> compact vdisk
  100 percent completed
  DiskPart successfully compacted the virtual disk file.

DISKPART> detach vdisk
```

Press `Ctrl+C` to exit `DISKPART`.
<br>

P.S. This didn't work for me (`optimize-vhd` is not found):

```powershell
> optimize-vhd -Path .\ext4.vhdx -Mode full
```
