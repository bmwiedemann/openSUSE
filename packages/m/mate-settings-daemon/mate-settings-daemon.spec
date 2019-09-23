#
# spec file for package mate-settings-daemon
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


%define _version 1.23
Name:           mate-settings-daemon
Version:        1.23.0
Release:        0
Summary:        MATE session settings daemon
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          System/GUI/Other
URL:            https://mate-desktop.org/
Source:         https://pub.mate-desktop.org/releases/%{_version}/%{name}-%{version}.tar.xz
# PATCH-FIX-UPSTREAM drop-libXxf86-dependency.patch -- drop libXxf89 dependency, which leaves mate in broken state, fixes boo#1139857
Patch0:         drop-libXxf86-dependency.patch
BuildRequires:  hicolor-icon-theme
# set to _version when mate-common has an equal release
BuildRequires:  mate-common >= 1.22
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(dconf) >= 0.13
BuildRequires:  pkgconfig(glib-2.0) >= 2.50
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(libcanberra-gtk3)
BuildRequires:  pkgconfig(libmatekbd) >= %{_version}
BuildRequires:  pkgconfig(libmatemixer) >= %{_version}
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libpulse-mainloop-glib)
BuildRequires:  pkgconfig(libxklavier) >= 5.2
BuildRequires:  pkgconfig(mate-desktop-2.0) >= %{_version}
BuildRequires:  pkgconfig(nss)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(xi)
# The default background is required as fallback.
Requires:       mate-backgrounds
# mate-settings-daemon needs a glib scheme to work correctly.
Requires:       matekbd-common
Recommends:     %{name}-lang
%glib2_gsettings_schema_requires

%description
This package contains the daemon which is responsible for setting
the various parameters of a MATE session and the applications that
run under it.

%package devel
Summary:        MATE session settings daemon development files
Group:          Development/Libraries/Other
Requires:       %{name} = %{version}

%description devel
This package contains the daemon which is responsible for setting
the various parameters of a MATE session and the applications that
run under it.

%lang_package

%prep
%setup -q
%patch0 -p1

%build
NOCONFIGURE=1 mate-autogen
%configure \
  --libexecdir=%{_bindir}   \
  --disable-static          \
  --disable-schemas-install \
  --enable-pulse            \
  --enable-polkit
make %{?_smp_mflags} V=1

%install
%make_install
%find_lang %{name} %{?no_lang_C}
find %{buildroot} -type f -name "*.la" -delete -print

%if 0%{?suse_version} < 1500
%post
%icon_theme_cache_post
%icon_theme_cache_post mate
%glib2_gsettings_schema_post

%postun
%icon_theme_cache_postun
%icon_theme_cache_postun mate
%glib2_gsettings_schema_postun
%endif

%files
%license COPYING COPYING.LIB
%doc AUTHORS NEWS
%config %{_sysconfdir}/dbus-1/system.d/org.mate.SettingsDaemon.DateTimeMechanism.conf
%dir %{_sysconfdir}/%{name}/
%dir %{_sysconfdir}/%{name}/xrandr/
%{_sysconfdir}/xrdb/
%dir %{_datadir}/mate-control-center/
%dir %{_datadir}/mate-control-center/keybindings/
%{_sysconfdir}/xdg/autostart/mate-settings-daemon.desktop
%{_bindir}/*
%{_libdir}/mate-settings-daemon/
%{_datadir}/dbus-1/services/*.service
%{_datadir}/dbus-1/system-services/*.service
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/mate-control-center/keybindings/50-accessibility.xml
%{_datadir}/%{name}/
%{_datadir}/polkit-1/actions/org.mate.settingsdaemon.datetimemechanism.policy
%{_datadir}/glib-2.0/schemas/*.xml
%{_libexecdir}/udev/rules.d/61-%{name}-rfkill.rules
%{_mandir}/man?/%{name}.?%{?ext_man}
%{_mandir}/man?/msd-*.?%{?ext_man}

%files devel
%{_includedir}/%{name}/
%{_libdir}/pkgconfig/%{name}.pc

%files lang -f %{name}.lang

%changelog
