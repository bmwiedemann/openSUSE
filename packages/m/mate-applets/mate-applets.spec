#
# spec file for package mate-applets
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
Name:           mate-applets
Version:        1.23.0
Release:        0
Summary:        A set of applets for the MATE Desktop
License:        GFDL-1.1-only AND GPL-2.0-or-later
Group:          System/GUI/Other
URL:            https://mate-desktop.org/
Source:         https://pub.mate-desktop.org/releases/%{_version}/%{name}-%{version}.tar.xz
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  libxml2-python
# set to _version when mate-common has an equal release
BuildRequires:  mate-common >= 1.22
BuildRequires:  pkgconfig
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(NetworkManager)
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(gio-2.0) >= 2.50
BuildRequires:  pkgconfig(glib-2.0) >= 2.50
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22
BuildRequires:  pkgconfig(gtksourceview-3.0)
BuildRequires:  pkgconfig(gucharmap-2.90)
BuildRequires:  pkgconfig(libgtop-2.0)
BuildRequires:  pkgconfig(libmatepanelapplet-4.0)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libwnck-3.0)
BuildRequires:  pkgconfig(mate-settings-daemon) >= %{_version}
BuildRequires:  pkgconfig(mateweather) >= 1.9.0
BuildRequires:  pkgconfig(polkit-gobject-1) >= 0.97
BuildRequires:  pkgconfig(popt)
BuildRequires:  pkgconfig(pygobject-3.0)
BuildRequires:  pkgconfig(upower-glib)
Recommends:     %{name}-lang
# mate-applet-netspeed was last used in openSUSE Leap 42.1.
Provides:       mate-applet-netspeed = %{version}
Obsoletes:      mate-applet-netspeed < %{version}
Obsoletes:      mate-applet-netspeed-lang < %{version}
Provides:       mate-netspeed = %{version}
Obsoletes:      mate-netspeed < %{version}
Obsoletes:      mate-netspeed-lang < %{version}
%glib2_gsettings_schema_requires

%description
This package provides a set of applets to use with the MATE panel.

%lang_package

%prep
%setup -q

%build
NOCONFIGURE=1 mate-autogen
%configure \
  --disable-static                    \
  --enable-stickynotes                \
  --disable-frequency-selector        \
  --libexecdir=%{_libexecdir}/%{name}
make %{?_smp_mflags} V=1

%install
%make_install
%find_lang %{name}
%fdupes %{buildroot}%{_datadir}
%fdupes %{buildroot}%{python_sitelib}

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
%license COPYING COPYING-DOCS
%doc AUTHORS NEWS README
%doc %{_datadir}/help/C/mate*/
%dir %{_sysconfdir}/sound/
%dir %{_sysconfdir}/sound/events/
%config %{_sysconfdir}/sound/events/mate-battstat_applet.soundlist
%{_libexecdir}/%{name}/
%{_datadir}/dbus-1/*/*.service
%{_datadir}/%{name}/
%{_datadir}/mate/
%{_datadir}/mate-panel/
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/icons/hicolor/*/devices/*
%{_datadir}/icons/hicolor/*/status/*
%{_datadir}/pixmaps/mate-*
%{_mandir}/man?/mate*.?%{?ext_man}
%{_datadir}/glib-2.0/schemas/*.xml

%files lang -f %{name}.lang
%{_datadir}/help/
%exclude %{_datadir}/help/C/

%changelog
