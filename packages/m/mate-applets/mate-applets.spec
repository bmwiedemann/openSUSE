#
# spec file for package mate-applets
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


%define _version 1.26

Name:           mate-applets
Version:        1.26.1
Release:        0
Summary:        A set of applets for the MATE Desktop
License:        GFDL-1.1-only AND GPL-2.0-or-later
URL:            https://mate-desktop.org/
Source:         https://pub.mate-desktop.org/releases/%{_version}/%{name}-%{version}.tar.xz
Group:          System/GUI/Other
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  mate-common >= %{_version}
BuildRequires:  pkgconfig
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtksourceview-3.0)
BuildRequires:  pkgconfig(gucharmap-2.90)
BuildRequires:  pkgconfig(libgtop-2.0)
BuildRequires:  pkgconfig(libmatepanelapplet-4.0)
BuildRequires:  pkgconfig(libnl-genl-3.0)
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

%package doc
Group:          Documentation/HTML
Summary:        Documentation how to use mate-applets
BuildArch:      noarch

%description doc
This package contains the documentation for mate-applets

%lang_package

%prep
%autosetup

%build
NOCONFIGURE=1 mate-autogen
%configure \
  --disable-static                    \
  --enable-stickynotes                \
  --disable-frequency-selector        \
  --libexecdir=%{_libexecdir}/%{name}
%make_build

%install
%make_install
%find_lang %{name} %{?no_lang_C}
%fdupes %{buildroot}%{_datadir}
%fdupes %{buildroot}%{python_sitelib}

%files
%license COPYING COPYING-DOCS
%doc AUTHORS NEWS README
%dir %{_sysconfdir}/sound/
%dir %{_sysconfdir}/sound/events/
%config %{_sysconfdir}/sound/events/mate-battstat_applet.soundlist
%{_libexecdir}/%{name}/
%{_datadir}/dbus-1/*/*.service
%{_datadir}/%{name}/
# %{_datadir}/mate/
%{_datadir}/mate-panel/
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/icons/hicolor/*/devices/*
%{_datadir}/icons/hicolor/*/status/*
%{_datadir}/pixmaps/mate-*
%{_mandir}/man?/mate*.?%{?ext_man}
%{_datadir}/glib-2.0/schemas/*.xml

%files doc
%doc %{_datadir}/help/*/mate*/

%files lang -f %{name}.lang

%changelog
