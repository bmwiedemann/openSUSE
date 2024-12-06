#
# spec file for package hourglass
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


%define         appid com.github.sgpthomas.hourglass
Name:           hourglass
Version:        3.1.0
Release:        0
Summary:        Clock gadget for the Pantheon DE
License:        GPL-3.0-only
URL:            https://github.com/sgpthomas/hourglass
Source:         %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  meson >= 0.57.0
BuildRequires:  pkgconfig
BuildRequires:  vala >= 0.28
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(granite-7) >= 7.1.0
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libportal-gtk4)

%description
A clock application that is designed to fit perfectly into
Pantheon's design scheme.

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

#fix upstream
chmod -x %{buildroot}%{_datadir}/icons/hicolor/*/apps/%{appid}.svg
chmod -x %{buildroot}%{_datadir}/pixmaps/%{appid}.svg

%files
%license COPYING
%doc AUTHORS README.md
%{_bindir}/%{appid}
%{_datadir}/applications/%{appid}.desktop
%{_datadir}/glib-2.0/schemas/%{appid}.gschema.xml
%{_datadir}/icons/hicolor/*/apps/%{appid}.svg
%{_datadir}/metainfo/%{appid}.metainfo.xml
%{_datadir}/pixmaps/%{appid}.svg

%files lang -f %{appid}.lang

%changelog
