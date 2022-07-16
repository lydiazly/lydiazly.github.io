---
title: Limit the memory usage in Windows 10 WSL2
date: 2022-07-16 14:56:11
categories: 'Other'
tags: [wsl2, powershell]
---
## Limit the memory usage

It's very annoying that WSL2 was always eating up my poor RAM.
There is a solution. It's working, except that the memory usage can't be exactly 'limited' but 'fixed'.

My distribution is:

```powershell
> wsl -l -v
  NAME            STATE           VERSION
* Ubuntu-18.04    Running         2
```

Create a configure file named `.wslconfig` in your user directory in Windows.

Open PowerShell as Administrator, shutdown your WSL2 and edit the file:

```powershell
> wsl --shutdown
> notepad "$env:USERPROFILE\.wslconfig"
```
For me the content is:

    [wsl2]
    memory=2GB
    swap=0

<!-- more -->

After that, the memory usage of my WSL2 never bothered me again.

## Compact the virtual disk

You may notice that this file occupies a huge amount of space: `%USERPROFILE%\AppData\Local\Packages\CanonicalGroupLimited.Ubuntu18.04onWindows_*\LocalState\ext4.vhdx`. It's said that WSL2 won't actually release the space after files are deleted. So I compacted the virtual disk to reduce the size as follows.

Open PowerShell as Administrator:

```powershell
> wsl --shutdown
> diskpart

# Raplace <user> and <pkg> by yours. It has to be a full path.
DISKPART> select vdisk file="C:\Users\<user>\AppData\Local\Packages\CanonicalGroupLimited.<pkg>\LocalState\ext4.vhdx"
  DiskPart successfully selected the virtual disk file.

# Compact and wait for minutes
DISKPART> compact vdisk
  100 percent completed
  DiskPart successfully compacted the virtual disk file.

DISKPART> detach vdisk
```

Press `Ctrl+C` to exit `DISKPART`.

I've no idea who is the original author for this. Thanks a lot.

<br>
This is not working for me (`optimize-vhd` is not found):

```powershell
> optimize-vhd -Path .\ext4.vhdx -Mode full
```

<br>
I'm not using Docker, btw.