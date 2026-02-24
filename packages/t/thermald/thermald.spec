#
# spec file for package thermald
#
# Copyright (c) 2026 SUSE LLC
# Copyright (c) 2025 SUSE LLC and contributors
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


#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir %{_localstatedir}/adm/fillup-templates
%endif

Name:           thermald
Version:        2.5.11.9.git+49457fb
Release:        0
Summary:        The Linux Thermal Daemon program from 01.org
License:        GPL-2.0-or-later
Group:          System/Daemons
URL:            https://github.com/intel/thermal_daemon.git
Source0:        thermal_daemon-%{version}.tar.xz
Source1:        %{name}.conf
Source3:        sysconfig.%{name}
Patch0:         fix-systemd-service.patch
Patch1:         power_user_cleanups.patch
BuildRequires:  autoconf-archive
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  sysuser-shadow
BuildRequires:  sysuser-tools
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk-doc)
BuildRequires:  pkgconfig(libevdev)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(upower-glib)
Requires(post): %fillup_prereq
Suggests:       acpica
Suggests:       dptfxtract
ExclusiveArch:  %{ix86} x86_64
%sysusers_requires

%description
Thermald is a Linux daemon used to prevent the overheating of platforms.
This daemon monitors temperature and applies compensation using available cooling methods.

%prep
%autosetup -n thermal_daemon-%{version} -p1

%build
NO_CONFIGURE=1 ./autogen.sh
%configure --disable-werror
%make_build CFLAGS="%{optflags}"

%install
%make_install

ln -s service %{buildroot}%{_sbindir}/rcthermald
install -D -m 0755 -t %{buildroot}%{_sbindir}/ tools/thermald_set_pref.sh
install -D -m 0644 -t %{buildroot}%{_prefix}/lib/modules-load.d/ %{SOURCE1}
install -D -m 0644 -t %{buildroot}%{_fillupdir}/ %{SOURCE3}

%pre
%service_add_pre thermald.service

%post
%fillup_only
%service_add_post thermald.service

%preun
%service_del_preun thermald.service

%postun
%service_del_postun thermald.service

%files
%license COPYING
%doc README.txt data/thermal-conf.xml
%doc test/thermald_optimization_with_dptfxtract
%dir %{_datadir}/dbus-1/system.d
%{_datadir}/dbus-1/system.d/org.freedesktop.thermald.conf
%dir %{_sysconfdir}/thermald
%config(noreplace) %{_sysconfdir}/thermald/thermal-cpu-cdev-order.xml
%dir %{_datadir}/dbus-1/system-services
%{_datadir}/dbus-1/system-services/org.freedesktop.thermald.service
%{_fillupdir}/sysconfig.%{name}
%{_mandir}/man5/thermal-conf.xml.5%{?ext_man}
%{_mandir}/man8/thermald.8%{?ext_man}
%dir %{_prefix}/lib/modules-load.d
%{_prefix}/lib/modules-load.d/thermald.conf
%{_sbindir}/rcthermald
%{_sbindir}/thermald
%{_sbindir}/thermald_set_pref.sh
%{_unitdir}/thermald.service

%changelog
