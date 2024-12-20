#
# spec file for package ovpn-dco
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


Name:           ovpn-dco
Version:        0.2.20241216~git0.a08b2fd
Release:        0
Summary:        OpenVPN Data Channel Offload in the Linux kernel
License:        GPL-2.0-only
URL:            https://github.com/OpenVPN/ovpn-dco
Source:         ovpn-dco-%{version}.tar.gz
Source1:        ovpn-dco-preamble
BuildRequires:  %kernel_module_package_buildreqs

# Releases prior to 15.2 don't have a new enough kernel
%if 0%{?sle_version} > 0 && 0%{?sle_version} < 150200
ExclusiveArch:  do_not_build
%endif

%{?kernel_module_package:%kernel_module_package -n ovpn-dco -p %name-preamble}

%description
This package contains a linux kernel module implementing the data channel of
the OpenVPN protocol in the linux kernel.

This kernel module allows OpenVPN to offload any data plane management to the
linux kernel, thus allowing it to exploit any Linux low level API, while
avoiding expensive and slow payload transfer between kernel space and
user space.

LIMITATIONS
* Only AEAD mode and 'none' (with no auth) supported
* Only AES-GCM and CHACHA20POLY1305 ciphers supported

%package KMP
Summary:        OpenVPN Data Channel Offload in the Linux kernel
Group:          Productivity/Networking/Security

%description KMP
This package contains a linux kernel module implementing the data channel of
the OpenVPN protocol in the linux kernel.

This kernel module allows OpenVPN to offload any data plane management to the
linux kernel, thus allowing it to exploit any Linux low level API, while
avoiding expensive and slow payload transfer between kernel space and
user space.

LIMITATIONS
* Only AEAD mode and 'none' (with no auth) supported
* Only AES-GCM and CHACHA20POLY1305 ciphers supported

%prep
echo %flavors_to_build
%autosetup -p1

%build
for flavor in %flavors_to_build; do
        mkdir obj-$flavor
        pushd obj-$flavor
        ln -s ../* .
        make KERNEL_SRC="/usr/src/linux-obj/%_target_cpu/$flavor" \
             V=1 %{?_smp_mflags}
        popd
done

%install
export INSTALL_MOD_PATH="%buildroot"

for flavor in %flavors_to_build; do
        pushd obj-$flavor/
        make KERNEL_SRC="/usr/src/linux-obj/%_target_cpu/$flavor" DEPMOD=/bin/true install
        popd
done

%check
# Would need to be able to load the module

%changelog
