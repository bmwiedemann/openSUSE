#
# spec file for package lttng-modules
#
# Copyright (c) 2023 SUSE LLC
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


Name:           lttng-modules
Version:        2.13.8
Release:        0
Summary:        Licensing information for package lttng-modules
License:        GPL-2.0-only AND LGPL-2.1-only AND MIT
Group:          System/Kernel
URL:            https://lttng.org/
Source:         https://lttng.org/files/lttng-modules/%{name}-%{version}.tar.bz2
Source1:        https://lttng.org/files/lttng-modules/%{name}-%{version}.tar.bz2.asc
Source2:        %{name}.keyring
Source3:        %{name}-preamble
Source4:        Module.supported
BuildRequires:  %{kernel_module_package_buildreqs}
ExclusiveArch:  %ix86 x86_64 armv7l aarch64 riscv64 ppc64 ppc64le

%description
This package provides licensing documentation for the lttng kmp packages.

%kernel_module_package -p %{name}-preamble -x ec2 xen xenpae vmi um

%prep
%setup -q

set -- *
mkdir source obj

for i in "$@"; do
   case $i in
      LICENSE|LICENSES|ChangeLog) ;;
      *) mv $i source ;;
   esac
done

%build
export EXTRA_CFLAGS='-DVERSION=\"%{version}\"'
for flavor in %{flavors_to_build}; do
    rm -rf obj/$flavor
    cp -r source obj/$flavor
    cp %{SOURCE4} obj/$flavor
    %make_build -C %{kernel_source $flavor} %{?linux_make_arch} modules \
      M=$PWD/obj/$flavor CONFIG_LTTNG=m CONFIG_LTTNG_CLOCK_PLUGIN_TEST=m
done

%install
export INSTALL_MOD_PATH=%{buildroot}
export INSTALL_MOD_DIR=updates
export BRP_PESIGN_FILES="*.ko /lib/firmware"
for flavor in %{flavors_to_build}; do
    make -C %{kernel_source $flavor} %{?linux_make_arch} modules_install \
      M=$PWD/obj/$flavor CONFIG_LTTNG=m CONFIG_LTTNG_CLOCK_PLUGIN_TEST=m
done

%files
%license LICENSE LICENSES/
%doc ChangeLog

%changelog
