#
# spec file for package vendor-reset
#
# Copyright (c) 2021 SUSE LLC
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


Name:           vendor-reset
Version:        0.1.0+225a49a
Release:        0
Summary:        Kernel module for resetting devices used by VFIO
License:        Apache-2.0
Group:          System/Management
URL:            https://github.com/gnif/vendor-reset
Source:         %{name}-%{version}.tar.xz
ExclusiveArch:  %{ix86} x86_64

%description
A kernel module that is capable of resetting hardware devices into a state
where they can be re-initialized or passed through into a virtual machine
(VFIO). While it would be great to have these in the kernel as PCI quirks,
some of the reset procedures are very complex and would never be accepted
as a quirk (ie AMD Vega 10).

%package kmp
Summary:        Kernel module for resetting devices used by VFIO
Group:          System/Kernel
BuildRequires:  %{kernel_module_package_buildreqs}
Conflicts:      vendor-reset-any-kmp
%kernel_module_package

%description kmp
A kernel module that is capable of resetting hardware devices into a state
where they can be re-initialized or passed through into a virtual machine
(VFIO). While it would be great to have these in the kernel as PCI quirks,
some of the reset procedures are very complex and would never be accepted
as a quirk (ie AMD Vega 10).

%prep
%autosetup -p1

%build
for flavor in %{flavors_to_build}; do
    make %{?_smp_mflags} -C %{kernel_source $flavor} %{?linux_make_arch} modules M=$PWD
done

%install
export INSTALL_MOD_PATH=%{buildroot}
export INSTALL_MOD_DIR=updates
for flavor in %{flavors_to_build}; do
    make -C %{kernel_source $flavor} %{?linux_make_arch} modules_install M=$PWD
done
install -dm755 %{buildroot}%{_prefix}/lib/modules-load.d
echo "vendor-reset" >> %{buildroot}%{_prefix}/lib/modules-load.d/vendor-reset.conf

%files kmp
%license LICENSE
%doc README.md
%dir %{_prefix}/lib/modules-load.d
%{_prefix}/lib/modules-load.d/vendor-reset.conf

%changelog
