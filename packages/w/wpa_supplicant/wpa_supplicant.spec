#
# spec file for package wpa_supplicant
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


Name:           wpa_supplicant
Version:        2.6
Release:        0
Summary:        WPA supplicant implementation
License:        BSD-3-Clause AND GPL-2.0-or-later
Group:          Productivity/Networking/Other
URL:            https://w1.fi/wpa_supplicant
Source0:        https://w1.fi/releases/%{name}-%{version}.tar.gz
Source1:        config
Source2:        %{name}.conf
Source3:        fi.epitest.hostap.WPASupplicant.service
Source4:        logrotate.wpa_supplicant
Source5:        fi.w1.wpa_supplicant1.service
Source6:        wpa_supplicant.service
Source7:        wpa_supplicant@.service
# wpa_supplicant-flush-debug-output.patch won't go upstream as it might
# change timings
Patch1:         wpa_supplicant-flush-debug-output.patch
# wpa_supplicant-sigusr1-changes-debuglevel.patch won't go upstream as it
# is not portable
Patch2:         wpa_supplicant-sigusr1-changes-debuglevel.patch
Patch3:         wpa_supplicant-alloc_size.patch
Patch4:         wpa_supplicant-getrandom.patch
Patch5:         wpa_supplicant-dump-certificate-as-PEM-in-debug-mode.diff
Patch10:        rebased-v2.6-0001-hostapd-Avoid-key-reinstallation-in-FT-handshake.patch
Patch11:        rebased-v2.6-0002-Prevent-reinstallation-of-an-already-in-use-group-ke.patch
Patch12:        rebased-v2.6-0003-Extend-protection-of-GTK-IGTK-reinstallation-of-WNM-.patch
Patch13:        rebased-v2.6-0004-Prevent-installation-of-an-all-zero-TK.patch
Patch14:        rebased-v2.6-0005-Fix-PTK-rekeying-to-generate-a-new-ANonce.patch
Patch15:        rebased-v2.6-0006-TDLS-Reject-TPK-TK-reconfiguration.patch
Patch16:        rebased-v2.6-0007-WNM-Ignore-WNM-Sleep-Mode-Response-without-pending-r.patch
Patch17:        rebased-v2.6-0008-FT-Do-not-allow-multiple-Reassociation-Response-fram.patch
Patch18:        wpa_supplicant-bnc-1099835-fix-private-key-password.patch
Patch19:        wpa_supplicant-bnc-1099835-clear-default_passwd_cb.patch
Patch20:        rebased-v2.6-0009-WPA-Ignore-unauthenticated-encrypted-EAPOL-Key-data.patch
Patch21:        wpa_supplicant-log-file-permission.patch
Patch22:        wpa_supplicant-log-file-cloexec.patch
Patch23:        wpa_supplicant-git-fa67debf4c6ddbc881a212b175faa6d5d0d90c8c.patch
Patch24:        wpa_supplicant-git-f5b74b966c942feb95a8ddbb7d130540b15b796d.patch
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  readline-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(libnl-3.0)
Requires:       logrotate

%description
wpa_supplicant is an implementation of the WPA Supplicant component,
i.e., the part that runs in the client stations. It implements key
negotiation with a WPA Authenticator and it controls the roaming and
IEEE 802.11 authentication/association of the wlan driver.

%package gui
Summary:        WPA supplicant graphical front-end
Group:          System/Monitoring
Requires:       wpa_supplicant

%description gui
This package contains a graphical front-end to wpa_supplicant, an
implementation of the WPA Supplicant component.

%prep
%setup -q -n wpa_supplicant-%{version}
cp %{SOURCE1} wpa_supplicant/.config
%autopatch -p1

%build
cd wpa_supplicant
CFLAGS="%{optflags}" make V=1 %{?_smp_mflags}
CFLAGS="%{optflags}" make V=1 %{?_smp_mflags} eapol_test
cd wpa_gui-qt4
%qmake5
%make_build

%install
install -d %{buildroot}/%{_sbindir}
install -m 0755 wpa_supplicant/wpa_cli %{buildroot}%{_sbindir}
install -m 0755 wpa_supplicant/wpa_passphrase %{buildroot}%{_sbindir}
install -m 0755 wpa_supplicant/wpa_supplicant %{buildroot}%{_sbindir}
install -m 0755 wpa_supplicant/eapol_test %{buildroot}%{_sbindir}
install -d %{buildroot}%{_sysconfdir}/dbus-1/system.d
install -m 0644 wpa_supplicant/dbus/dbus-wpa_supplicant.conf %{buildroot}%{_sysconfdir}/dbus-1/system.d/wpa_supplicant.conf
install -d %{buildroot}/%{_sysconfdir}/%{name}
install -m 0600 %{SOURCE2} %{buildroot}/%{_sysconfdir}/%{name}
install -d %{buildroot}/%{_datadir}/dbus-1/system-services
install -m 0644 %{SOURCE3} %{buildroot}/%{_datadir}/dbus-1/system-services
install -m 0644 %{SOURCE5} %{buildroot}/%{_datadir}/dbus-1/system-services
install -d %{buildroot}/%{_sysconfdir}/logrotate.d/
install -m 644 %{SOURCE4} %{buildroot}/%{_sysconfdir}/logrotate.d/wpa_supplicant
install -d %{buildroot}/%{_rundir}/%{name}
install -d %{buildroot}%{_mandir}/man{5,8}
install -m 0644 wpa_supplicant/doc/docbook/*.8 %{buildroot}%{_mandir}/man8
#  wpa_supplicant is built without CONFIG_PRIVSEP
rm %{buildroot}%{_mandir}/man8/wpa_priv.*
install -m 0644 wpa_supplicant/doc/docbook/*.5 %{buildroot}%{_mandir}/man5
install -m 755 wpa_supplicant/wpa_gui-qt4/wpa_gui %{buildroot}%{_sbindir}
install -d %{buildroot}%{_unitdir}
install -m 0644 %{SOURCE6} %{buildroot}%{_unitdir}
install -m 0644 %{SOURCE7} %{buildroot}%{_unitdir}
ln -s service %{buildroot}/%{_sbindir}/rcwpa_supplicant
# avoid spurious dependency on /usr/bin/python
chmod -x wpa_supplicant/examples/*.py
# dbus auto activation boo#966535
ln -s wpa_supplicant.service %{buildroot}%{_unitdir}/dbus-fi.epitest.hostap.WPASupplicant.service
ln -s wpa_supplicant.service %{buildroot}%{_unitdir}/dbus-fi.w1.wpa_supplicant1.service

%pre
%service_add_pre wpa_supplicant.service

%post
%service_add_post wpa_supplicant.service

%preun
%service_del_preun wpa_supplicant.service

%postun
%service_del_postun wpa_supplicant.service

%files
%license COPYING
%doc wpa_supplicant/ChangeLog README wpa_supplicant/todo.txt wpa_supplicant/examples wpa_supplicant/wpa_supplicant.conf
%{_sbindir}/eapol_test
%{_sbindir}/rcwpa_supplicant
%{_sbindir}/wpa_cli
%{_sbindir}/wpa_passphrase
%{_sbindir}/wpa_supplicant
%config %{_sysconfdir}/dbus-1/system.d/%{name}.conf
%{_datadir}/dbus-1/system-services
%config %{_sysconfdir}/%{name}/%{name}.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/wpa_supplicant
%dir %{_rundir}/%{name}
%ghost %{_rundir}/%{name}
%{_unitdir}/wpa_supplicant.service
%{_unitdir}/wpa_supplicant@.service
%{_unitdir}/dbus-fi.epitest.hostap.WPASupplicant.service
%{_unitdir}/dbus-fi.w1.wpa_supplicant1.service
%dir %{_sysconfdir}/%{name}
%{_mandir}/man8/*
%exclude %{_mandir}/man8/wpa_gui.*
%{_mandir}/man5/*

%files gui
%{_sbindir}/wpa_gui
%{_mandir}/man8/wpa_gui*

%changelog
