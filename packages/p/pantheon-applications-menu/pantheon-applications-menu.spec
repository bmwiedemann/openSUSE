#
# spec file for package pantheon-applications-menu
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


%define         appid io.elementary.desktop.wingpanel.applications-menu
Name:           pantheon-applications-menu
Version:        8.0.1
Release:        0
Summary:        Pantheon Application Launcher
License:        GPL-3.0-or-later
URL:            https://github.com/elementary/applications-menu
Source0:        %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  vala
BuildRequires:  pkgconfig(appstream)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libgnome-menu-3.0)
BuildRequires:  pkgconfig(libhandy-1)
BuildRequires:  pkgconfig(switchboard-3)
BuildRequires:  pkgconfig(wingpanel)
BuildRequires:  pkgconfig(zeitgeist-2.0)
Provides:       slingshot-launcher = %{version}
Obsoletes:      slingshot-launcher < %{version}

%description
The application launcher for the Pantheon Desktop.

%lang_package

%prep
%autosetup -n applications-menu-%{version}

%build
%meson \
  -Dwith-zeitgeist=true
%meson_build

%install
%meson_install
%find_lang slingshot
%fdupes %{buildroot}

%files
%license COPYING
%doc README.md
%dir %{_libdir}/wingpanel
%{_libdir}/wingpanel/libslingshot.so
%{_datadir}/glib-2.0/schemas/%{appid}.gschema.xml
%{_datadir}/metainfo/io.elementary.wingpanel.applications-menu.metainfo.xml
%{_libdir}/io.elementary.wingpanel.applications-menu

%files lang -f slingshot.lang

%changelog
