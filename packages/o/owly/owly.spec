#
# spec file for package owly
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           owly
Version:        0.4.3
Release:        0
Summary:        AirDrop over AWDL for Linux Wi-Fi cards
License:        MIT AND Apache-2.0 AND BSD-3-Clause AND ISC AND Unicode-3.0
URL:            https://github.com/t4t5/owly
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
# Source-Binary-Exception: vendor.tar.zst:vendor/ring-*/pregenerated/*.o -- other-platform: pregenerated Windows COFF objects of the ring crate, never used by the Linux build
BuildRequires:  cargo-packaging
BuildRequires:  dbus-1-daemon
BuildRequires:  iproute2
BuildRequires:  pkgconfig
# %%check runs omdrop-owl's send-to-peer helper
BuildRequires:  python3-base
BuildRequires:  rust >= 1.88
BuildRequires:  pkgconfig(systemd)
Requires:       NetworkManager
Requires:       iproute2
Requires:       iputils
Requires:       polkit
Requires:       util-linux
Recommends:     hostapd
Suggests:       bluez
# Upstream supports and builds only these
ExclusiveArch:  aarch64 x86_64
%{?systemd_ordering}

%description
Owly does AirDrop between iPhones and Linux machines whose Wi-Fi card
is not Apple's Broadcom chip, by running AWDL in user space.

It contains owlyd, a D-Bus-activated system service that takes over
the Wi-Fi card, runs AWDL on it and lends the resulting awdl0
interface to the application that asked for it, and the owly
command-line tool, which checks the card (doctor, test-card) and
browses for, sends to and receives from AirDrop devices.

Only some Wi-Fi cards work; "owly doctor" reports whether this one
does.

%prep
%autosetup -a1

%build
%cargo_build -- -p owlyd -p owly-cli

%install
DESTDIR=%{buildroot} PREFIX=%{_prefix} TARGET=target \
  DOCDIR=%{_docdir}/%{name} LICENSEDIR=%{_licensedir}/%{name} \
  LIBEXECDIR=%{_libexecdir} \
  sh packaging/install.sh owly
# owlyd goes in %%{_libexecdir} (bin_t), not /usr/lib (lib_t, where
# systemd would run it as init_t without nl80211). Upstream supports
# LIBEXECDIR since 0.4.2, so no manual move is needed.

%check
# The loopback, native and rtnl tests add veth and dummy links in an
# unprivileged user namespace: a chroot build root can't create the
# namespace, and OBS's build kernel has neither driver.
targets=
if ! unshare --user --map-root-user --net sh -c \
  'ip link add owlyp0 type veth peer name owlyp1 && ip link add owlyp2 type dummy' \
  2>/dev/null; then
  echo "No veth or dummy links here: skipping the loopback, native and rtnl tests"
  targets="--lib --bins --test conformance --test discoverable --test vectors"
  targets="$targets --test driver --test node --test simulation --test hwsim"
  targets="$targets --test injection --test replay --test service"
fi
%cargo_test -- --workspace $targets

%pre
%service_add_pre owlyd.service

%post
%service_add_post owlyd.service
# NetworkManager reads conf.d only on a reload, so Owly's interfaces stay
# managed until something rereads it.
if systemctl is-active --quiet NetworkManager 2>/dev/null; then
  nmcli general reload conf >/dev/null 2>&1 || :
fi

%preun
%service_del_preun owlyd.service

%postun
%service_del_postun owlyd.service

%files
%dir %{_licensedir}/%{name}
%license %{_licensedir}/%{name}/LICENSE
%dir %{_docdir}/%{name}
%doc %{_docdir}/%{name}/README.md
%{_bindir}/owly
%dir %{_libexecdir}/owly
%{_libexecdir}/owly/owlyd
%{_unitdir}/owlyd.service
%{_datadir}/dbus-1/system.d/io.github.t4t5.Owly.conf
%{_datadir}/dbus-1/system-services/io.github.t4t5.Owly.service
%{_datadir}/polkit-1/actions/io.github.t4t5.Owly.policy
%dir %{_prefix}/lib/NetworkManager
%dir %{_prefix}/lib/NetworkManager/conf.d
%{_prefix}/lib/NetworkManager/conf.d/90-owly-unmanaged.conf
%dir %{_systemd_util_dir}/network
%{_systemd_util_dir}/network/10-owly-awdl0.link

%changelog
