#
# spec file for package wireguard
#
# Copyright (c) 2020 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2017-2020, Martin Hauke <mardnh@gmx.de>
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


Name:           wireguard
Version:        0.0.20200105
Release:        0
Summary:        Fast, modern, secure kernel VPN tunnel
License:        GPL-2.0-only
Group:          Productivity/Networking/Security
URL:            https://www.wireguard.com/
Source:         https://git.zx2c4.com/wireguard-linux-compat/snapshot/wireguard-linux-compat-%{version}.tar.xz
Source1:        https://git.zx2c4.com/wireguard-linux-compat/snapshot/wireguard-linux-compat-%{version}.tar.asc
Source2:        wireguard-kmp-preamble
Source99:       https://www.zx2c4.com/keys/AB9942E6D4A4CFC3412620A749FC7012A5DE03AE.asc#/WireGuard.keyring
Patch2:         wireguard-fix-leap151.patch
BuildRequires:  %{kernel_module_package_buildreqs}
# disable flavors xen,desktop,pae,pv
%kernel_module_package -p wireguard-kmp-preamble

%description
WireGuard is a novel VPN that runs inside the Linux Kernel and uses
state-of-the-art cryptography (the "Noise" protocol). It aims to be
faster, simpler, leaner, and more useful than IPSec, while avoiding
the massive headache. It intends to be considerably more performant
than OpenVPN. WireGuard is designed as a general purpose VPN for
running on embedded interfaces and super computers alike, fit for
many different circumstances. It runs over UDP.

%prep
%setup -q -n wireguard-linux-compat-%{version}
%if 0%{?sle_version} == 150100
%patch2 -p1
%endif

cd src
set -- *
mkdir source
mv "$@" source/
mkdir obj

%build
cd src
for flavor in %{flavors_to_build}; do
    cp -r source obj/$flavor
    make V=1 -C %{kernel_source $flavor} modules M=$PWD/obj/$flavor %{?_smp_mflags}
done

%install
cd src
export INSTALL_MOD_PATH=%{buildroot}
for flavor in %{flavors_to_build}; do
    make V=1 -C %{kernel_source $flavor} modules_install M=$PWD/obj/$flavor
done

%files
%license COPYING
%doc README.md

%changelog
