#
# spec file for package hdjmod
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2021 Matthias Bach <marix@marix.org>
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


Name:           hdjmod
Version:        1.34
Release:        0
Summary:        Support for Hercules DJ Devices
License:        GPL-2.0-or-later
Group:          System/Kernel
URL:            https://codeberg.org/Marix/hdjmod
Source0:        https://codeberg.org/Marix/hdjmod/archive/%{version}.tar.gz#/hdjmod-%{version}.tar.gz
Source1:        preamble
BuildRequires:  %{kernel_module_package_buildreqs}
BuildRequires:  libelf-devel
%suse_kernel_module_package -p%{_sourcedir}/preamble

%description
This is the Hercules DJ Series Kernel Module, which supports Hercules DJ Devices.

%prep
echo %{flavors_to_build}

%setup -q -n %{name}

set -- *
mkdir source
mv "$@" source/
mkdir obj

%build
for flavor in %{flavors_to_build}; do
        rm -rf obj/$flavor
        cp -r source obj/$flavor
        %make_build -C %{kernel_source $flavor} %{?linux_make_arch} modules M=$PWD/obj/$flavor
done

%install
export INSTALL_MOD_PATH=%{buildroot}
export INSTALL_MOD_DIR=updates
for flavor in %{flavors_to_build}; do
        make -C %{kernel_source $flavor} %{?linux_make_arch} modules_install M=$PWD/obj/$flavor
done

%changelog
