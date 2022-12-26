#
# spec file for package spacenavd
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2009,2011,2013 Herbert Graeber
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


Name:           spacenavd
Version:        1.2
Release:        0
Summary:        Daemon for 3Dconnexion devices
License:        GPL-3.0-or-later
Group:          Hardware/Other
URL:            http://spacenav.sourceforge.net
Source:         https://github.com/FreeSpacenav/spacenavd/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1:        spacenavd.8.gz
Source2:        spnavrc
Source3:        xinitrc-%{name}
Patch1:         spacenavd-fix-pidfile.patch
Patch2:         harden_spacenavd.service.patch
BuildRequires:  pkgconfig
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(x11)
%{?systemd_requires}
Requires:       xdpyinfo
Supplements:    modalias(usb:v046DpC603d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v046DpC605d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v046DpC606d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v046DpC621d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v046DpC623d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v046DpC625d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v046DpC626d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v046DpC627d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v046DpC628d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v046DpC629d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v046DpC62bd*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v046DpC640d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v256FpC62Fd*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v256FpC631d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v256FpC632d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v256FpC633d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v256FpC634d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v256FpC635d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v256FpC636d*dc*dsc*dp*ic*isc*ip*)

%description
Spacenavd is a free software replacement user-space driver (daemon)
for 3Dconnexion's 6-degree-of-freedoms input devices. It is
compatible with the original 3dxsrv daemon, and works perfectly with
any program that was written for the 3Dconnexion driver.

%prep
%setup -q
%patch1 -p1
%patch2 -p1

%build
%configure
make %{?_smp_mflags} opt="%{optflags}"

%install
install -D -m 755 %{name} %{buildroot}%{_sbindir}/%{name}
install -D -m 755 spnavd_ctl %{buildroot}%{_bindir}/spnavd_ctl
install -D -m 644 %{SOURCE1} %{buildroot}%{_mandir}/man8/spacenavd.8.gz
ln -sf spacenavd.8.gz %{buildroot}%{_mandir}/man8/spnavd_ctl.8.gz
install -D -m 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/spnavrc
install -D -m 755 %{SOURCE3} %{buildroot}%{_sysconfdir}/X11/xinit/xinitrc.d/%{name}
ln -sf service %{buildroot}%{_sbindir}/rc%{name}
install -D -m 644 contrib/systemd/%{name}.service %{buildroot}%{_unitdir}/%{name}.service

%post
%fillup_only -n %{name}
%service_add_post %{name}.service

%postun
%service_del_postun %{name}.service

%pre
%service_add_pre %{name}.service

%preun
%service_del_preun %{name}.service

%files
%license COPYING
%doc README.md
%doc doc/example-spnavrc
%doc doc/spnavrc_smouse_ent
%doc doc/spnavrc_spilot
%{_sbindir}/%{name}
%{_sbindir}/rc%{name}
%{_bindir}/spnavd_ctl
%config(noreplace) %{_sysconfdir}/spnavrc
%{_unitdir}/%{name}.service
%{_mandir}/man8/spacenavd.8%{?ext_man}
%{_mandir}/man8/spnavd_ctl.8%{?ext_man}
%{_sysconfdir}/X11/xinit/

%changelog
