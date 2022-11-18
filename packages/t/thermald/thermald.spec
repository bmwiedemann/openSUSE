#
# spec file for package thermald
#
# Copyright (c) 2022 SUSE LLC
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
Version:        2.5.1
Release:        0
Summary:        The Linux Thermal Daemon program from 01.org
License:        GPL-2.0-or-later
Group:          System/Daemons
URL:            https://01.org/linux-thermal-daemon
Source0:        https://github.com/intel/thermal_daemon/archive/v%{version}/thermal_daemon-%{version}.tar.gz
Source1:        %{name}.conf
Source2:        %{name}-group.conf
Source3:        sysconfig.%{name}
Source10:       thermal-monitor.desktop
Source11:       thermal-monitor.png
Patch0:         fix-systemd-service.patch
BuildRequires:  autoconf-archive
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  qcustomplot-devel
BuildRequires:  sysuser-shadow
BuildRequires:  sysuser-tools
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk-doc)
BuildRequires:  pkgconfig(libevdev)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(upower-glib)
Requires(post): %fillup_prereq
Suggests:       acpica
Suggests:       dptfxtract
Suggests:       thermal-monitor
ExclusiveArch:  %{ix86} x86_64
%sysusers_requires

%description
Thermald is a Linux daemon used to prevent the overheating of platforms.
This daemon monitors temperature and applies compensation using available cooling methods.

%package -n thermal-monitor
Summary:        Displays current temperature readings
License:        GPL-3.0-or-later
Group:          Hardware/Other
Requires:       %{name} >= 1.4.3
Requires:       group(power)

%description -n thermal-monitor
Thermal Monitor displays current temperature readings on a graph.
To communicate with thermald via dbus, the user has to be member of "power" group.

%prep
%autosetup -n thermal_daemon-%{version} -p1

%build
NO_CONFIGURE=1 ./autogen.sh
%configure --disable-werror
%make_build CFLAGS="%{optflags}"
%sysusers_generate_pre %{SOURCE2} power

pushd tools/thermal_monitor
%qmake5 ThermalMonitor.pro
%make_build
popd

%install
%make_install

ln -s service %{buildroot}%{_sbindir}/rcthermald
install -D -m 0755 -t %{buildroot}%{_sbindir}/ tools/thermald_set_pref.sh
install -D -m 0644 -t %{buildroot}%{_prefix}/lib/modules-load.d/ %{SOURCE1}
install -D -m 0644 %{SOURCE2} %{buildroot}%{_sysusersdir}/%{name}.conf
install -D -m 0644 -t %{buildroot}%{_fillupdir}/ %{SOURCE3}

install -D -m 0755 -t %{buildroot}%{_bindir}/ tools/thermal_monitor/ThermalMonitor
install -D -m 0644 -t %{buildroot}%{_datadir}/applications/ %{SOURCE10}
install -D -m 0644 -t %{buildroot}%{_datadir}/pixmaps/ %{SOURCE11}
%suse_update_desktop_file thermal-monitor

%pre -f power.pre
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
%dir %{_datadir}/dbus-1/system-services
%dir %{_sysconfdir}/dbus-1/system.d
%dir %{_sysconfdir}/thermald
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/org.freedesktop.thermald.conf
%config(noreplace) %{_sysconfdir}/thermald/thermal-cpu-cdev-order.xml
%{_datadir}/dbus-1/system-services/org.freedesktop.thermald.service
%{_fillupdir}/sysconfig.%{name}
%{_mandir}/man5/thermal-conf.xml.5%{?ext_man}
%{_mandir}/man8/thermald.8%{?ext_man}
%dir %{_prefix}/lib/modules-load.d
%{_prefix}/lib/modules-load.d/thermald.conf
%{_sbindir}/rcthermald
%{_sbindir}/thermald
%{_sbindir}/thermald_set_pref.sh
%{_sysusersdir}/%{name}.conf
%{_unitdir}/thermald.service

%files -n thermal-monitor
%license tools/thermal_monitor/README
%{_bindir}/ThermalMonitor
%{_datadir}/applications/thermal-monitor.desktop
%{_datadir}/pixmaps/thermal-monitor.png

%changelog
