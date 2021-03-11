#
# spec file for package rtl8812au
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


Name:           rtl8812au
Version:        5.9.3.2+git20210302.d1bf6df
Release:        0
Summary:        Kernel driver for Realtek 802.11ac 8812au wifi cards
License:        GPL-2.0-only
Group:          System/Kernel
URL:            https://github.com/gordboy/rtl8812au-5.9.3.2
Source0:        %{name}-%{version}.tar.xz
Source1:        %{name}-preamble
Source2:        LICENSE
# PATCH-FIX-OPENSUSE fix-backported-ndo_select_queue.patch
Patch0:         fix-backported-ndo_select_queue.patch
BuildRequires:  %{kernel_module_package_buildreqs}
BuildRequires:  bc
BuildRequires:  binutils
BuildRequires:  fdupes
BuildRequires:  kernel-devel
BuildRequires:  kernel-source
BuildRequires:  module-init-tools
%kernel_module_package -p %{name}-preamble

%description
Kernel driver for Realtek 802.11ac 8812au wifi cards

The sources were obtained from https://github.com/gordboy/rtl8812au, which adaptes the official driver
released by Realtek to build on recent kernels.

The previous sources were obtained from https://github.com/diederikdehaas/rtl8812AU and 
https://github.com/maurossi/rtl8812au/ .

%package KMP
Summary:        Kernel driver for Realtek 802.11ac rtl8812au wifi cards
Group:          System/Kernel

%description KMP
Kernel driver for Realtek 802.11ac 8812au wifi cards

The sources were obtained from https://github.com/gordboy/rtl8812au, which adaptes the official driver
released by Realtek to build on recent kernels.

The previous sources were obtained from https://github.com/diederikdehaas/rtl8812AU and 
https://github.com/maurossi/rtl8812au/ .

%prep
%setup -q
%if 0%{?sle_version} == 150100
%patch0 -p1
%endif

set -- *
mkdir source
mv "$@" source/
cp "%{S:2}" source/
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
for flavor in %{flavors_to_build} ; do
	cp -a source obj/$flavor
        pushd obj/$flavor
        sed -i -e "s,^KSRC := /lib/modules/\$(KVER)/build$,KSRC := %{_prefix}/src/linux-obj/%{_target_cpu}/$flavor," Makefile
        make %{?_smp_mflags}
        popd
done

%install
export INSTALL_MOD_PATH=%{buildroot}
export INSTALL_MOD_DIR=%{kernel_module_package_moddir}
kernel_version=`uname -r | sed -e "s/-[^-]*$//"`

echo ${kernel_version}
for flavor in %{flavors_to_build} ; do
        pushd obj/$flavor
        install -d %{buildroot}/lib/modules/${kernel_version}-${flavor}/${INSTALL_MOD_DIR}/
        install -p -m 644 8812au.ko %{buildroot}/lib/modules/${kernel_version}-${flavor}/${INSTALL_MOD_DIR}/
        popd
done

%files
%license source/LICENSE

%changelog
