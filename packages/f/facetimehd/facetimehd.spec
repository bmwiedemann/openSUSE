#
# spec file for package facetimehd
#
# Copyright (c) 2024 SUSE LLC
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


Name:           facetimehd
Version:        0.6.8.2
Release:        0
Summary:        Kernel driver for the Apple FacetimeHD webcams
License:        GPL-2.0-only
Group:          System/Kernel
URL:            https://github.com/patjak/facetimehd
Source0:        https://github.com/patjak/facetimehd/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        preamble
Patch0:         Remove-use-of-linux-pci-aspm.h-since-it-s-not-in-the.patch
BuildRequires:  %{kernel_module_package_buildreqs}
ExcludeArch:    s390x
%kernel_module_package -p %{_sourcedir}/preamble

%description
Reverse engineered Linux driver for the FacetimeHD PCIe webcam

%prep
%setup -q
%if 0%{?sle_version} == 150300
%patch -P 0 -p1
%endif

set -- *
mkdir source
mv "$@" source/
mkdir obj

%build
for flavor in %{flavors_to_build}; do
        rm -rf obj/$flavor
        cp -r source obj/$flavor
        %make_build -C %{kernel_source $flavor} modules M=$PWD/obj/$flavor
done

%install
export INSTALL_MOD_PATH=%{buildroot}
export INSTALL_MOD_DIR=updates
for flavor in %{flavors_to_build}; do
        make -C %{kernel_source $flavor} modules_install M=$PWD/obj/$flavor
done

%changelog
