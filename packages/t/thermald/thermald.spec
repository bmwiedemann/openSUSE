#
# spec file for package thermald
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           thermald
Version:        1.8
Release:        0
Summary:        The Linux Thermal Daemon program from 01.org
License:        GPL-2.0-or-later
Group:          System/Daemons
URL:            https://01.org/linux-thermal-daemon
Source0:        https://github.com/01org/thermal_daemon/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        thermald.conf
Patch0:         fix_long_int_i586_issue.patch
Patch1:         fix_missing_include.patch
BuildRequires:  automake
BuildRequires:  dbus-1-devel
BuildRequires:  dbus-1-glib-devel
BuildRequires:  gcc-c++
BuildRequires:  glib2-devel
BuildRequires:  libxml2-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(systemd)
ExclusiveArch:  %{ix86} x86_64

%description
Thermald is a Linux daemon used to prevent the overheating of platforms.
This daemon monitors temperature and applies compensation using available cooling methods.

%prep
%setup -q -n thermal_daemon-%{version}
%autopatch -p1

%build
autoreconf -fiv
%configure
make %{?_smp_mflags} CFLAGS="%{optflags}"

%pre
%service_add_pre thermald.service

%install
%make_install

ln -s service %{buildroot}%{_sbindir}/rcthermald
install -Dm644 "%{_sourcedir}/thermald.conf" "%{buildroot}/%{_libexecdir}/modules-load.d/thermald.conf"

%post
%service_add_post thermald.service

%preun
%service_del_preun thermald.service

%postun
%service_del_postun thermald.service

%files
%dir %{_datadir}/dbus-1/system-services
%dir %{_sysconfdir}/dbus-1/system.d
%dir %{_sysconfdir}/thermald
%config %{_sysconfdir}/dbus-1/system.d/org.freedesktop.thermald.conf
%doc data/thermal-conf.xml
%config %{_sysconfdir}/thermald/thermal-cpu-cdev-order.xml
%{_datadir}/dbus-1/system-services/org.freedesktop.thermald.service
%{_mandir}/man5/thermal-conf.xml.5%{?ext_man}
%{_mandir}/man8/thermald.8%{?ext_man}
%{_sbindir}/thermald
%dir %{_libexecdir}/modules-load.d
%{_libexecdir}/modules-load.d/thermald.conf
%{_unitdir}/thermald.service
%{_sbindir}/rcthermald

%changelog
