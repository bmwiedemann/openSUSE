#
# spec file for package wireguard
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2017, Martin Hauke <mardnh@gmx.de>
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


Name:           wireguard
Version:        0.0.20191012
Release:        0
Summary:        Fast, modern, secure kernel VPN tunnel
License:        GPL-2.0-only
Group:          Productivity/Networking/Security
URL:            https://www.wireguard.com/
Source:         https://git.zx2c4.com/WireGuard/snapshot/WireGuard-%{version}.tar.xz
Source98:       https://git.zx2c4.com/WireGuard/snapshot/WireGuard-%{version}.tar.asc
Source99:       https://www.zx2c4.com/keys/AB9942E6D4A4CFC3412620A749FC7012A5DE03AE.asc#/WireGuard.keyring
Source1:        wireguard.target
Source2:        wireguard-kmp-preamble
Patch0:         wireguard-remove-depmod.diff
Patch1:         wireguard-fix-systemd-service.patch
Patch2:         wireguard-fix-leap151.patch
BuildRequires:  %{kernel_module_package_buildreqs}
BuildRequires:  bash-completion
BuildRequires:  libmnl-devel
BuildRequires:  pkgconfig
# disable flavors xen,desktop,pae,pv
%kernel_module_package -p wireguard-kmp-preamble
%systemd_requires
%if 0%{?suse_version} >= 1330
BuildRequires:  libelf-devel
%endif

%description
WireGuard is a novel VPN that runs inside the Linux Kernel and uses
state-of-the-art cryptography (the "Noise" protocol). It aims to be
faster, simpler, leaner, and more useful than IPSec, while avoiding
the massive headache. It intends to be considerably more performant
than OpenVPN. WireGuard is designed as a general purpose VPN for
running on embedded interfaces and super computers alike, fit for
many different circumstances. It runs over UDP.

%package tools
Summary:        Fast, modern, secure kernel VPN tunnel
Group:          Productivity/Networking/Security

%description tools
WireGuard is a novel VPN that runs inside the Linux Kernel and uses
state-of-the-art cryptography (the "Noise" protocol). It aims to be
faster, simpler, leaner, and more useful than IPSec, while avoiding
the massive headache. It intends to be considerably more performant
than OpenVPN. WireGuard is designed as a general purpose VPN for
running on embedded interfaces and super computers alike, fit for
many different circumstances. It runs over UDP.

This package contains command-line tools to interact with the
WireGuard kernel module.  Currently, it provides only a single tool:

wg: set and retrieve configuration of WireGuard interfaces

%prep
%setup -q -n WireGuard-%{version}
%patch0 -p1
%patch1 -p1
%if 0%{?sle_version} == 150100
%patch2 -p1
%endif
## HACK: Fixing wg-quick's DNS= directive with a hatchet
contrib/examples/dns-hatchet/apply.sh
##
cd src
set -- *
mkdir source
mv "$@" source/
mkdir obj

%build
cd src
# tools
cp -r source obj/tools
make V=1 -C obj/tools/tools %{?_smp_mflags}
# kernel modules
for flavor in %{flavors_to_build}; do
    cp -r source obj/$flavor
    make V=1 -C %{kernel_source $flavor} modules M=$PWD/obj/$flavor %{?_smp_mflags}
done

%install
cd src
# tools
%{make_install} -C obj/tools/tools \
    WITH_BASHCOMPLETION=yes \
    WITH_WGQUICK=yes \
    WITH_SYSTEMDUNITS=yes
# kernel modules
export INSTALL_MOD_PATH=%{buildroot}
for flavor in %{flavors_to_build}; do
    make V=1 -C %{kernel_source $flavor} modules_install M=$PWD/obj/$flavor
done

install -Dm 0644 %{S:1} %{buildroot}%{_unitdir}/%{name}.target

install -d %{buildroot}/%{_sysconfdir}/wireguard/

%pre tools
%service_add_pre wireguard.target wg-quick@.service

%post tools
%service_add_post wireguard.target wg-quick@.service

%preun tools
%service_del_preun wireguard.target wg-quick@.service

%postun tools
%service_del_postun wireguard.target wg-quick@.service

%files tools
%license COPYING
%doc README.md
%{_sysconfdir}/wireguard/
%{_bindir}/wg
%{_bindir}/wg-quick
%{_mandir}/man8/wg.8%{?ext_man}
%{_mandir}/man8/wg-quick.8%{?ext_man}
%{_datadir}/bash-completion/completions/wg
%{_datadir}/bash-completion/completions/wg-quick
%{_unitdir}/wg-quick@.service
%{_unitdir}/%{name}.target

%changelog
