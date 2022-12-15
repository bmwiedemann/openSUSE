#
# spec file for package tp_smapi
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

Name:           tp_smapi
Summary:        IBM ThinkPad hardware functions driver
Version:        0.43
Release:        1
License:        GPL-2.0-or-later
Group:          System/Kernel
Url:            https://github.com/linux-thinkpad/tp_smapi
Source:         tp_smapi-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  %kernel_module_package_buildreqs
BuildRequires:  kernel-source
BuildRequires:  kernel-syms
BuildRequires:  module-init-tools
ExclusiveArch:  %ix86 x86_64
Requires:	kernel-desktop

%suse_kernel_module_package -p -n tp_smapi kdump um

%description
The tp_smapi kernel module exposes some features of the ThinkPad hardware/firmware via a sysfs interface.
Currently, the main implemented functionality is control of battery charging and extended battery status.
It also includes an improved version of the HDAPS driver. The underlying hardware interfaces are SMAPI
and direct access to the embedded controller.

%prep
%setup -n tp_smapi-%{version}
set -- *
mkdir source
mv "$@" source/
mkdir obj

%build
for flavor in %flavors_to_build; do
    rm -rf obj/$flavor
    cp -r source obj/$flavor
    krel=$(make -s -C /usr/src/linux-obj/%_target_cpu/$flavor kernelrelease)
    cd obj/$flavor
    make KVER=${krel} KSRC=/usr/src/linux KBUILD=/usr/src/linux-obj/%_target_cpu/$flavor M=$PWD/obj/$flavor HDAPS=1
    cd -
done

%install
export INSTALL_MOD_PATH=$RPM_BUILD_ROOT
export INSTALL_MOD_DIR=updates
for flavor in %flavors_to_build; do
    make -C /usr/src/linux-obj/%_target_cpu/$flavor modules_install M=$PWD/obj/$flavor
done
cd source

%changelog
