#
# spec file for package lxpanel
#
# Copyright (c) 2024 SUSE LLC
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


Name:           lxpanel
Version:        0.10.1
Release:        0
Summary:        Lightweight X11 desktop panel based on fbpanel
License:        GPL-2.0-only
Group:          System/GUI/LXDE
URL:            http://www.lxde.org/
Source0:        https://sourceforge.net/projects/lxde/files/LXPanel%20%28desktop%20panel%29/LXPanel%200.10.x/%{name}-%{version}.tar.xz
Patch0:         lxpanel-0.9.3-default_config.patch
Patch1:         lxpanel-0.9.3-panel_config.patch
BuildRequires:  autoconf
BuildRequires:  fdupes
BuildRequires:  intltool
BuildRequires:  libfm-gtk-devel
BuildRequires:  libiw-devel
BuildRequires:  libxml2-devel
BuildRequires:  pkgconfig
BuildRequires:  wireless-tools
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(keybinder)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libmenu-cache)
BuildRequires:  pkgconfig(libwnck-1.0)
Requires:       lxmenu-data
Requires:       menu-cache
Provides:       %{name}-plugins >= %{version}
Obsoletes:      %{name}-plugins < %{version}
%lang_package

%description
LXPanel is a lightweight X11 desktop panel containing:
1. User-friendly application menu automatically generated from *.desktop files on the system
2. Launcher bar (Small icons clicked to launch apps)
3. Task bar supporting urgency hint (Can flash when gaim gets new incoming messages)
4. Notification area (System tray)
5. Digital clock
6. Run dialog (A dialog lets you type a command and run it, can be called in external programs)
7. Net status icon plug-in (optional, ported from gnome-netstatus-applet)
8. Volume control plug-in (optional, written by jserv)
9. lxpanelctl, an external controller lets you control lxpanel in other programs.
For example, "lxpanelctl run" will show the Run dialog in lxpanel, and "lxpanelctl menu"
will show the application menu. This is useful in key bindings provided by window managers.

%package -n liblxpanel0
Summary:        LXDE panel libraries
Group:          System/Libraries

%description -n liblxpanel0
Library for interpolability and access to the lxpanel API by plugins.

%package devel
Summary:        Devel files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       glib2-devel
Requires:       liblxpanel0 = %{version}
Requires:       menu-cache-devel
Requires:       pkgconfig

%description devel
Headers and development files for lxpanel.

%prep
%autosetup -p1

%build
export CFLAGS="%{optflags} -Wno-incompatible-pointer-types"
# autoconf
%configure --with-plugins=all
%make_build

%install
%make_install %{?_smp_mflags}
find %{buildroot} -type f -name "*.la" -delete -print
%find_lang %{name}
%fdupes -s %{buildroot}

%post -n liblxpanel0 -p /sbin/ldconfig
%postun -n liblxpanel0 -p /sbin/ldconfig

%files
%defattr(-,root,root,0755)
%license COPYING
%doc ChangeLog README
%{_bindir}/%{name}
%{_bindir}/lxpanelctl
%{_sysconfdir}/xdg/%{name}
%dir %{_libdir}/%{name}/
%dir %{_libdir}/%{name}/plugins
%dir %{_datadir}/%{name}/
%dir %{_datadir}/%{name}/ui
%dir %{_datadir}/%{name}/images
%dir %{_datadir}/%{name}/images/xkb-flags/
%dir %{_datadir}/%{name}/xkeyboardconfig
%{_datadir}/%{name}/images/xkb-flags/*.png
%{_datadir}/%{name}/images/*.png
%{_datadir}/%{name}/xkeyboardconfig/layouts.cfg
%{_datadir}/%{name}/xkeyboardconfig/models.cfg
%{_datadir}/%{name}/xkeyboardconfig/toggle.cfg
%{_datadir}/%{name}/ui/*.ui
%{_mandir}/man1/*.1%{?ext_man}
%{_libdir}/%{name}/plugins/batt.so
%{_libdir}/%{name}/plugins/cpu.so
%{_libdir}/%{name}/plugins/deskno.so
%{_libdir}/%{name}/plugins/kbled.so
%{_libdir}/%{name}/plugins/netstatus.so
%{_libdir}/%{name}/plugins/thermal.so
%{_libdir}/%{name}/plugins/xkb.so
%{_libdir}/%{name}/plugins/volume.so
%{_libdir}/%{name}/plugins/cpufreq.so
%{_libdir}/%{name}/plugins/monitors.so
%{_libdir}/%{name}/plugins/netstat.so
%{_libdir}/%{name}/plugins/weather.so
%config(noreplace) %{_sysconfdir}/xdg/%{name}/*

%files devel
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*.h
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/lxpanel/liblxpanel.so

%files -n liblxpanel0
%dir %{_libdir}/lxpanel
%{_libdir}/lxpanel/liblxpanel.so.0
%{_libdir}/lxpanel/liblxpanel.so.0.0.0

%files lang -f %{name}.lang

%changelog
