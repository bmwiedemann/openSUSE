#
# spec file for package pantheon-calculator
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


%define         appid io.elementary.calculator
Name:           pantheon-calculator
Version:        8.0.0
Release:        0
Summary:        A simple calculator for the Pantheon Desktop
License:        GPL-3.0-only
URL:            https://github.com/elementary/calculator
Source:         %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  meson >= 0.58.0
BuildRequires:  pkgconfig
BuildRequires:  vala >= 0.28.0
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite-7)
BuildRequires:  pkgconfig(gtk4)
Provides:       elementary-calculator = %{version}
Obsoletes:      elementary-calculator < %{version}

%description
A tiny, simple calculator written in GTK+ and Vala.

%lang_package

%prep
%autosetup -n calculator-%{version}

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{appid}
%fdupes %{buildroot}%{_datadir}

%files
%license COPYING
%doc README.md
%{_bindir}/%{appid}
%{_datadir}/applications/%{appid}.desktop
%{_datadir}/glib-2.0/schemas/%{appid}.gschema.xml
%{_datadir}/metainfo/%{appid}.metainfo.xml
%{_datadir}/icons/hicolor/*/apps/%{appid}.svg
%dir %{_datadir}/icons/hicolor/{128x128@2,128x128@2/apps,16x16@2,16x16@2/apps,24x24@2,24x24@2/apps,32x32@2,32x32@2/apps,64x64@2,64x64@2/apps}

%files lang -f %{appid}.lang

%changelog
