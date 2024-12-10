#
# spec file for package reco
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


%define         appid com.github.ryonakano.reco
Name:           reco
Version:        3.2.1
Release:        0
Summary:        Audio Recording App
License:        GPL-3.0-or-later
URL:            https://github.com/ryonakano/reco
Source:         %{url}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  libxml2-tools
BuildRequires:  meson >= 0.49.0
BuildRequires:  pkgconfig
BuildRequires:  vala
BuildRequires:  pkgconfig(granite) >= 5.2.3
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libhandy-1)
BuildRequires:  pkgconfig(libpulse)

%description
An audio recording app designed for the Pantheon Desktop.

%lang_package

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{appid}
%fdupes %{buildroot}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{appid}
%{_datadir}/applications/%{appid}.desktop
%{_datadir}/glib-2.0/schemas/%{appid}.gschema.xml
%{_datadir}/icons/hicolor/*/apps/%{appid}.svg
%{_datadir}/icons/hicolor/symbolic/apps/record-completed-symbolic.svg
%{_datadir}/metainfo/%{appid}.appdata.xml

%files lang -f %{appid}.lang

%changelog
