#
# spec file for package wireguard-tools
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2020, Martin Hauke <mardnh@gmx.de>
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


Name:           wireguard-tools
Version:        1.0.20200510
Release:        0
Summary:        WireGuard userspace tools
License:        GPL-2.0-only
Group:          Productivity/Networking/Security
URL:            https://www.wireguard.com/
Source:         https://git.zx2c4.com/wireguard-tools/snapshot/wireguard-tools-%{version}.tar.xz
Source1:        https://git.zx2c4.com/wireguard-tools/snapshot/wireguard-tools-%{version}.tar.asc
Source99:       https://www.zx2c4.com/keys/AB9942E6D4A4CFC3412620A749FC7012A5DE03AE.asc#/WireGuard.keyring
BuildRequires:  bash-completion
BuildRequires:  pkgconfig
%systemd_requires

%description
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
%setup -q -n wireguard-tools-%{version}
## HACK: Fixing wg-quick's DNS= directive with a hatchet
contrib/dns-hatchet/apply.sh

%build
export CFLAGS="%{optflags}"
make V=1 -C src %{?_smp_mflags}

%install
cd src
%{make_install} \
    WITH_BASHCOMPLETION=yes \
    WITH_WGQUICK=yes \
    WITH_SYSTEMDUNITS=yes

install -D -m0644 systemd/wg-quick.target %{buildroot}%{_unitdir}/wg-quick.target
install -d %{buildroot}/%{_sysconfdir}/wireguard/

%pre
%service_add_pre wg-quick.target wg-quick@.service

%post
%service_add_post wg-quick.target wg-quick@.service

%preun
%service_del_preun wg-quick.target wg-quick@.service

%postun
%service_del_postun wg-quick.target wg-quick@.service

%files
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
%{_unitdir}/wg-quick.target

%changelog
