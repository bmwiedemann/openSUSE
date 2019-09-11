#
# spec file for package lttng-modules
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%if 0%{?suse_version} >= 1500 && !0%{?is_opensuse}
%ifarch x86_64
%define buildrt 1
%endif
%endif
Name:           lttng-modules
Version:        2.10.9
Release:        0
Summary:        Licensing information for package lttng-modules
License:        GPL-2.0-only AND LGPL-2.1-only AND MIT
Group:          System/Kernel
Url:            https://lttng.org/
Source:         https://lttng.org/files/lttng-modules/%{name}-%{version}.tar.bz2
Source1:        https://lttng.org/files/lttng-modules/%{name}-%{version}.tar.bz2.asc
Source2:        %{name}.keyring
Source3:        %{name}-preamble
Source4:        Module.supported
# PATCH-FIX-OPENSUSE lttng-modules-fix-leap-15.0.patch -- Fix building on openSUSE Leap 15.0.
Patch0:         lttng-modules-fix-leap-15.0.patch
BuildRequires:  kernel-devel
BuildRequires:  kernel-source
BuildRequires:  kernel-syms
BuildRequires:  module-init-tools
ExclusiveArch:  %ix86 x86_64 aarch64 ppc64 ppc64le
%if 0%{?buildrt}
BuildRequires:  kernel-syms-rt
%endif

%description
This package provides licensing documentation for the lttng kmp packages.

%suse_kernel_module_package -p %{name}-preamble ec2 xen xenpae vmi um

%package KMP
Summary:        LTTng Kernel Tracing Modules
Group:          System/Kernel

%description KMP
This package contains the LTTng 2.0 Kernel Modules necessary for
instrumenting kernel subsystems.

%prep
%setup -q
%patch0 -p1

set -- *
mkdir source
mkdir obj

for i in "$@"; do
   case $i in
      LICENSE|*.txt) ;;
      *) mv $i source ;;
   esac
done

%build
export EXTRA_CFLAGS='-DVERSION=\"%{version}\"'
for flavor in %{flavors_to_build}; do
    rm -rf obj/$flavor
    cp -r source obj/$flavor
    cp %{SOURCE4} obj/$flavor
    make %{?_smp_mflags} V=1 -C %{_prefix}/src/linux-obj/%{_target_cpu}/$flavor modules \
      M=$PWD/obj/$flavor CONFIG_LTTNG=m CONFIG_LTTNG_CLOCK_PLUGIN_TEST=m
done

%install
export INSTALL_MOD_PATH=%{buildroot}
export INSTALL_MOD_DIR=updates
export BRP_PESIGN_FILES="*.ko /lib/firmware"
for flavor in %{flavors_to_build}; do
    make -C %{_prefix}/src/linux-obj/%{_target_cpu}/$flavor modules_install \
      M=$PWD/obj/$flavor CONFIG_LTTNG=m CONFIG_LTTNG_CLOCK_PLUGIN_TEST=m
done

%files
%license LICENSE lgpl-2.1.txt gpl-2.0.txt mit-license.txt

%changelog
