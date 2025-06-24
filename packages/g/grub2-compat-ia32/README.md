# grub2-compat-ia32

Enable 32-bit x86 support in the kernel on modern openSUSE/SLE installations that do not include it by default.

## Purpose

Starting with openSUSE Leap 16.0 and SUSE Linux Enterprise (SLE) 16.0, support for 32-bit x86 execution is disabled by default.  
This change was made to ensure that the system is [Y2038-safe](https://en.wikipedia.org/wiki/Year_2038_problem).

## What This Package Does

This package adds the following kernel parameter:

`ia32_emulation=1`

This is done via:

/usr/sbin/update-bootloader --add-option "ia32_emulation=1"

Enabling this option restores compatibility with 32-bit x86 user-space binaries.

## Without This Package

Applications like Steam, Wine, or VirtualBox that rely on 32-bit compatibility may fail with errors such as:

Error: Missing libc.so.6

or directly:

```
/usr/bin/ldd: line 159: /lib/ld-linux.so.2: cannot execute binary file: Exec format error
not a dynamic executable
```

## Installation

Install the package using Zypper:

```bash
sudo zypper in grub2-compat-ia32
```

After installation, make sure to reboot:
```bash
sudo reboot
```

## Further Reading
See https://en.opensuse.org/GRUB#Enabling_32bit_x86_support_in_Kernel
