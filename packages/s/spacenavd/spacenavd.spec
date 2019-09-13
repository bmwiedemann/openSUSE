#
# spec file for package spacenavd
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%if 0%{?suse_version} > 1140
%define has_systemd 1
BuildRequires:  systemd-rpm-macros
%{?systemd_requires}
%endif
Name:           spacenavd
Version:        0.6
Release:        0
Summary:        Daemon for 3Dconnexion devices
License:        GPL-3.0-or-later
Group:          Hardware/Other
URL:            http://spacenav.sourceforge.net
Source:         https://github.com/FreeSpacenav/%{name}/archive/%{name}-%{version}.tar.gz
Source1:        spacenavd.8.gz
Source2:        spnavrc
Source3:        xinitrc-%{name}
Source4:        %{name}.service
Patch1:         spacenavd-0.6+git3066072.patch
# PATCH-FIX-UPSTREAM spacenavd-add-blacklist-and-device-ids.patch #4
Patch2:         spacenavd-add-blacklist-and-device-ids.patch
# PATCH-FIX-UPSTREAM spacenavd-add-missing-usbid.patch #12
Patch3:         spacenavd-add-missing-usbid.patch
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(x11)
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
Supplements:    modalias(usb:v256Fp*d*dc*dsc*dp*ic*isc*ip*)

%description
Spacenavd is a free software replacement user-space driver (daemon)
for 3Dconnexion's 6-degree-of-freedoms input devices. It is
compatible with the original 3dxsrv daemon, and works perfectly with
any program that was written for the 3Dconnexion driver.

%prep
%setup -q -n %{name}-%{name}-%{version}
%patch1 -p1
%patch2 -p1
%patch3 -p1

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
%if 0%{?has_systemd}
install -D -m 644 %{SOURCE4} %{buildroot}%{_unitdir}/%{name}.service
%endif

%post
%fillup_only -n %{name}
%if 0%{?has_systemd}
%service_add_post %{name}.service
%endif

%postun
%if 0%{?has_systemd}
%service_del_postun %{name}.service
%else
%restart_on_update %{name}
%insserv_cleanup
%endif

%pre
%if 0%{?has_systemd}
%service_add_pre %{name}.service
%endif

%preun
%if 0%{?has_systemd}
%service_del_preun %{name}.service
%else
%stop_on_removal %{name}
%endif

%files
%license COPYING
%doc README.md
%{_sbindir}/%{name}
%{_sbindir}/rc%{name}
%{_bindir}/spnavd_ctl
%config(noreplace) %{_sysconfdir}/spnavrc
%if 0%{?has_systemd}
%{_unitdir}/%{name}.service
%endif
%{_mandir}/man8/spacenavd.8%{?ext_man}
%{_mandir}/man8/spnavd_ctl.8%{?ext_man}
%{_sysconfdir}/X11/xinit/

%changelog
