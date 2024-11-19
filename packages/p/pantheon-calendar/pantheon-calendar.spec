#
# spec file for package pantheon-calendar
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


%define         sover 0
%define         appid io.elementary.calendar
Name:           pantheon-calendar
Version:        8.0.0
Release:        0
Summary:        Maya Calendar for the Pantheon Desktop
License:        GPL-3.0-or-later
URL:            https://github.com/elementary/calendar
Source:         %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(champlain-0.12)
BuildRequires:  pkgconfig(champlain-gtk-0.12)
BuildRequires:  pkgconfig(clutter-1.0)
BuildRequires:  pkgconfig(folks)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(geocode-glib-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(granite) >= 6.2.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.11.6
BuildRequires:  pkgconfig(libedataserver-1.2)
BuildRequires:  pkgconfig(libgeoclue-2.0)
BuildRequires:  pkgconfig(libhandy-1) >= 0.90.0
BuildRequires:  pkgconfig(libical)
BuildRequires:  pkgconfig(libportal)
BuildRequires:  pkgconfig(libportal-gtk3)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(vapigen) >= 0.40.4
Provides:       elementary-calendar = %{version}
Obsoletes:      elementary-calendar < %{version}

%description
A slim, lightweight Granite calendar app written in Vala, designed for
the Pantheon Desktop where it is known simply as Calendar.

Also looks and works great on other GTK desktops.

%package -n     libelementary-calendar%{sover}
Summary:        The calendar for the Pantheon Desktop

%description -n libelementary-calendar%{sover}
A slim, lightweight Granite calendar app written in Vala, designed for
Elementary OS where it is known simply as Calendar.

%package        plugins
Summary:        A collection of plugins for %{name}
Requires:       %{name} = %{version}

%description    plugins
Calendar for the Pantheon Desktop.

This package contains a collection of plugins: CalDAV, Google and etc.

%package        devel
Summary:        Development files for lib%{name}
Requires:       libelementary-calendar%{sover} = %{version}

%description    devel
This subpackage contains libraries and header files for developing
applications

%lang_package

%prep
%autosetup -n calendar-%{version}

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{appid}
%fdupes %{buildroot}/%{_datadir}

%ldconfig_scriptlets -n libelementary-calendar%{sover}

%files
%license COPYING
%doc README.md
%{_bindir}/%{appid}
%{_datadir}/applications/%{appid}.desktop
%{_datadir}/metainfo/%{appid}.metainfo.xml
%{_datadir}/vala/vapi/elementary-calendar.{deps,vapi}
%{_datadir}/icons/hicolor/*/apps/%{appid}.svg
%{_datadir}/glib-2.0/schemas/%{appid}.gschema.xml
%dir %{_datadir}/icons/hicolor/{128x128@2,128x128@2/apps,16x16@2,16x16@2/apps,24x24@2,24x24@2/apps,32x32@2,32x32@2/apps,48x48@2,48x48@2/apps,64x64@2,64x64@2/apps}

%files -n libelementary-calendar%{sover}
%{_libdir}/libelementary-calendar.so.*

%files plugins
%dir %{_libdir}/{%{appid},%{appid}/plugins}
%{_libdir}/%{appid}/plugins/*

%files devel
%{_includedir}/elementary-calendar
%{_libdir}/libelementary-calendar.so
%{_libdir}/pkgconfig/elementary-calendar.pc

%files lang -f %{appid}.lang

%changelog
