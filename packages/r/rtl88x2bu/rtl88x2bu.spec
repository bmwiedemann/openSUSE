#
# spec file for package rtl88x2bu
#
# Copyright (c) 2025 SUSE LLC
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


Name:           rtl88x2bu
Version:        5.8.7.1+git20250126.efe396c
Release:        0
Summary:        Kernel driver for Realtek 88x2bu wifi cards
License:        GPL-2.0-only
Group:          System/Kernel
URL:            https://github.com/cilynx/rtl88x2bu
ExcludeArch:    s390x
Source0:        %{name}-%{version}.tar
Source1:        %{name}-preamble
# PATCH-FIX-OPENSUSE rtl88x2bu_nodate_time.patch
Patch0:         rtl88x2bu_nodate_time.patch
# PATCH-FIX-OPENSUSE fix-backported-update_mgmt_frame_registrations.patch
Patch1:         fix-backported-update_mgmt_frame_registrations.patch
BuildRequires:  %{kernel_module_package_buildreqs}
BuildRequires:  bc
BuildRequires:  kernel-macros
BuildRequires:  module-init-tools

%{!?kernel_module_directory:%define kernel_module_directory /lib/modules}

%description
Kernel driver for Realtek 88x2bu wifi cards

The sources were obtained from https://github.com/cilynx/rtl88x2bu, which adapts the official driver
released by Realtek to build on recent kernels.

%package KMP
Summary:        Kernel driver for Realtek rtl88x2bu wifi cards
Group:          System/Kernel

%description KMP
Kernel driver for Realtek 88x2bu wifi cards

The sources were obtained from https://github.com/cilynx/rtl88x2bu, which adapts the official driver
released by Realtek to build on recent kernels.

%kernel_module_package -p %{name}-preamble

%prep
%setup -q
sed -i '/EXTRA_CFLAGS += -O2/d' Makefile
sed -i '/EXTRA_LDFLAGS += --strip-debug/d' Makefile
%patch -P 0 -p0
%if 0%{?sle_version} == 150300
%patch -P 1 -p0
%endif

set -- *
mkdir source
mv "$@" source/
mkdir obj

%build
%ifarch %{arm}
export ARCH=arm
%endif
%ifarch aarch64
export ARCH=arm64
%endif
%ifarch %{ppc} ppc64 ppc64le
export ARCH=powerpc
%endif
%ifarch riscv64
export ARCH=riscv
%endif

for flavor in %{flavors_to_build} ; do
    rm -rf obj/$flavor
    cp -a source obj/$flavor
    pushd obj/$flavor
    sed -i -e "s,^KSRC := /lib/modules/\$(KVER)/build$,KSRC := %{_prefix}/src/linux-obj/%{_target_cpu}/$flavor," Makefile
    %make_build
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
    mkdir -p %{buildroot}%{kernel_module_directory}/${kernel_version}-${flavor}/${INSTALL_MOD_DIR}/
    install -p -m 644 88x2bu.ko %{buildroot}%{kernel_module_directory}/${kernel_version}-${flavor}/${INSTALL_MOD_DIR}/
    popd
done

%files
%license source/LICENSE

%changelog
