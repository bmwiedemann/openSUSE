#
# spec file for package vhba-kmp
#
# Copyright (c) 2022 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           vhba-kmp
Version:        20211218
Release:        0
Summary:        Virtual SCSI Host Bus Adapter
License:        GPL-2.0-or-later
Group:          System/Kernel
URL:            https://cdemu.sourceforge.io/about/vhba/

#Git-Clone:	https://github.com/cdemu/cdemu
Source:         https://downloads.sf.net/cdemu/vhba-module-%version.tar.xz
Source2:        %name-preamble
Patch1:         vhba-no-werror.diff
Patch2:         vhba-devname.diff
BuildRequires:  %kernel_module_package_buildreqs
BuildRequires:  kernel-syms >= 2.6.20

%{?kernel_module_package:%kernel_module_package -n vhba -p %name-preamble}

%description
A Linux kernel module implementing a virtual SCSI Host Bus Adapter to
act as a low-level SCSI driver and which provides the SCSI layer with
a virtual SCSI adapter which can have multiple virtual devices. It is
part of the userspace cdemu suite, CD/DVD-ROM device emulator for
Linux.

%package KMP
Summary:        Virtual SCSI Host Bus adapter
Group:          System/Kernel

%description KMP
A Linux kernel module implementing a virtual SCSI Host Bus Adapter to
act as a low-level SCSI driver and which provides the SCSI layer with
a virtual SCSI adapter which can have multiple virtual devices. It is
part of the userspace cdemu suite, CD/DVD-ROM device emulator for
Linux.

%prep
echo %flavors_to_build
%autosetup -n vhba-module-%version -p1

%build
for flavor in %flavors_to_build; do
	cp -a . "../obj-$flavor/"
	pushd "../obj-$flavor/"
	make KDIR="/usr/src/linux-obj/%_target_cpu/$flavor" \
		%{?_smp_mflags}
	popd
done

%install
export INSTALL_MOD_PATH="%buildroot"

for flavor in %flavors_to_build; do
	pushd "../obj-$flavor/"
	make KDIR="/usr/src/linux-obj/%_target_cpu/$flavor" \
		modules_install
	popd
done

%changelog
