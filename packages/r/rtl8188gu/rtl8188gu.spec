#
# spec file for package rtl8188gu
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

%define   commit          c2b79fc1c085d9fc4a70ac0f5bc730ec929c562b
%define   shortcommit     c2b79fc

Name:           rtl8188gu
Version:        0.0.0+git20230112.%{shortcommit}
Release:        0
Summary:        Driver for Linux RTL8188GU
License:        GPL-2.0+
Group:          Hardware/Other
Url:            https://github.com/McMCCRU/rtl8188gu
Source0:        https://github.com/McMCCRU/rtl8188gu/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
Source1:        LICENSE
# PATCH-FIX-UPSTREAM fix-build-on-kernel-6_4.patch hillwood@opensuse.org - Support Kernel 6.5+
Patch0:         fix-build-on-kernel-6_4.patch
# PATCH-FIX-UPSTREAM fix-build-on-kernel-6_5.patch hillwood@opensuse.org - Support Kernel 6.5+
Patch1:         fix-build-on-kernel-6_5.patch
# PATCH-FIX-UPSTREAM fix-build-on-kernel-6_5.patch hillwood@opensuse.org - Support Kernel 6.8+
Patch2:         fix-build-on-kernel-6_8.patch
BuildRequires:  bc
BuildRequires:  binutils
BuildRequires:  fdupes
BuildRequires:  kernel-default-devel
BuildRequires:  kernel-devel
BuildRequires:  module-init-tools
%if %{defined kernel_module_package_buildreqs}
BuildRequires:  %{kernel_module_package_buildreqs}
%endif
Requires:       %{name}-kmp
Provides:       %{name}-kmod-common = %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if %{defined kernel_module_package}
%kernel_module_package
%endif

%description
Driver for Linux RTL8188GU (RTL8710B) (VID:PID = 0x0BDA:0xB711)

%package KMP
Summary:        RTL8188GU Module for deepin-anything
Group:          System/Kernel

%description KMP
These packages contain Anything Module for RTL8188GU.

%prep
%autosetup -p1 -n %{name}-%{commit}
cp %{SOURCE1} .
set -- *
mkdir source
cp -r "$@" source/
mkdir obj

%build
%ifarch %arm
export ARCH=arm
%endif
%ifarch aarch64
export ARCH=arm64
%endif
%ifarch %ppc ppc64 ppc64le
export ARCH=powerpc
%endif
%ifarch riscv64
export ARCH=riscv
%endif
%ifarch i586
export ARCH=i386
%endif
for flavor in %{flavors_to_build} ; do
    cp -a source obj/$flavor
        pushd obj/$flavor
        sed -i -e "s,^KSRC := /lib/modules/\$(KVER)/build$,KSRC := %{_prefix}/src/linux-obj/%{_target_cpu}/$flavor," Makefile
        make -O V=1 %{?_smp_mflags}
        popd
done

%install
export INSTALL_MOD_PATH=%{buildroot}
export INSTALL_MOD_DIR=updates
for flavor in %{flavors_to_build}; do
    make -C %{_prefix}/src/linux-obj/%{_target_cpu}/$flavor modules_install \
        M=$PWD/obj/$flavor
done

%files
%doc README.md
%license LICENSE

%changelog

