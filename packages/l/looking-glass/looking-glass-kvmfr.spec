#
# spec file for package looking-glass-kmp
#
# Copyright (c) 2026 SUSE LLC
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

Name:           looking-glass-kvmfr
Version:        0~B7
Release:        0
Summary:        Kernel module for Looking Glass (IVSHMEM framebuffer sharing)
License:        GPL-2.0-only
URL:            https://looking-glass.io/
Source0:        looking-glass-B7.tar.xz
Source1:        looking-glass-kvmfr-kmp-preamble
Source2:        looking-glass-kvmfr.rpmlintrc
BuildRequires:  %kernel_module_package_buildreqs
Supplements:    (kernel-default and looking-glass)

%{?kernel_module_package:%kernel_module_package -p %name-kmp-preamble}

%description
This package provides the kvmfr kernel module used by Looking Glass for IVSHMEM frame sharing.

%prep
%setup -q -n looking-glass-B7
mv module kvmfr

%build
for flavor in %flavors_to_build; do
    cp -a kvmfr "obj-$flavor"
    make -C /usr/src/linux-obj/%_target_cpu/$flavor \
         M=$PWD/obj-$flavor \
         %{?_smp_mflags}
done

%install
export INSTALL_MOD_PATH="%buildroot"

for flavor in %flavors_to_build; do
    make -C /usr/src/linux-obj/%_target_cpu/$flavor \
         M=$PWD/obj-$flavor \
         modules_install
done

%changelog
