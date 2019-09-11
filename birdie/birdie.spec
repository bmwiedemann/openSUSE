#
# spec file for package birdie
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           birdie
Version:        1.1
Release:        0
Summary:        A native Twitter client
License:        GPL-3.0
Group:          Productivity/Networking/Other
Url:            https://birdieapp.github.io/
Source:         https://github.com/needle-and-thread/birdie/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM birdie-1.1-vala-0.34.patch gh#needle-and-thread/birdie#191 -- Fix a warning where "static" is superfluous.
Patch0:         birdie-1.1-vala-0.34.patch
# PATCH-FIX-UPSTREAM birdie-webkit2gtk4-port.patch sor.alexei@meowr.ru -- Port to WebKit2Gtk-4.0.
Patch1:         birdie-webkit2gtk4-port.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  vala
BuildRequires:  pkgconfig(dbusmenu-gtk3-0.4)
BuildRequires:  pkgconfig(gee-1.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtksourceview-3.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(purple)
BuildRequires:  pkgconfig(rest-0.7)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(webkit2gtk-4.0)
BuildRequires:  pkgconfig(xtst)
Recommends:     %{name}-lang
%glib2_gsettings_schema_requires

%description
Birdie is a beautiful and fast Twitter client designed for Elementary OS.

%lang_package

%prep
%setup -q
%patch0 -p1
%patch1 -p1
chmod a-x AUTHORS COPYING README.md

%build
%cmake
make %{?_smp_mflags} V=1

%install
%cmake_install
%find_lang %{name}

%post
%desktop_database_post
%icon_theme_cache_post
%glib2_gsettings_schema_post

%postun
%desktop_database_postun
%icon_theme_cache_postun
%glib2_gsettings_schema_postun

%files
%doc AUTHORS COPYING README.md
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/glib-2.0/schemas/*%{name}.gschema.xml
%dir %{_datadir}/appdata/
%{_datadir}/appdata/*%{name}.appdata.xml
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/icons/hicolor/*/*/*.*
%dir %{_datadir}/indicators/
%dir %{_datadir}/indicators/messages/
%dir %{_datadir}/indicators/messages/applications/
%{_datadir}/indicators/messages/applications/birdie

%files lang -f %{name}.lang

%changelog
