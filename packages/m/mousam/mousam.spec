#
# spec file for package mousam
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           mousam
Version:        1.4.2
Release:        0
Summary:        A lightweight weather app
License:        GPL-3.0-or-later
URL:            https://github.com/amit9838/mousam
Source:         %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  desktop-file-utils
BuildRequires:  gobject-introspection
BuildRequires:  hicolor-icon-theme
BuildRequires:  meson
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  python3-base >= 3.8
BuildRequires:  python3-requests
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
Requires:       python3-gobject-Gdk
BuildArch:      noarch

%lang_package

%description
Mousam is a lightweight weather app. It has the following features:
*	Real-time temperature, humidity, wind speed, UV index, pressure and more
*	Provide hourly forecasts for the next 24 hours
*	Also shows tomorrow and 7-day forcasts
*	Supports metric or imperial systems

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name} %{?no_lang_C}

%check
%meson_test

%files
%license COPYING
%doc README.md
%{_bindir}/mousam
%{_datadir}/%{name}/
%{_datadir}/appdata/*appdata.xml
%{_datadir}/applications/*.desktop
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/icons/hicolor/scalable/mousam_icons/
%{_datadir}/icons/hicolor/*/apps/*.svg

%files lang -f %{name}.lang

%changelog
