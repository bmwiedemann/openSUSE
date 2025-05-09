#
# spec file for package spice-up
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


%define         appid com.github.philip_scott.spice-up
Name:           spice-up
Version:        1.9.1
Release:        0
Summary:        Desktop presentation application
License:        GPL-3.0-only
URL:            https://github.com/Philip-Scott/Spice-up
Source:         %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  shared-mime-info
BuildRequires:  vala > 0.48.0
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(granite) >= 0.5
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22.0
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libevdev)
BuildRequires:  pkgconfig(libsoup-2.4)

%description
Spice-up is a desktop presentation application
based upon SpiceOfDesign's presentation concept.

%lang_package

%prep
%autosetup -n Spice-up-%{version}

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{appid}
%fdupes %{buildroot}

%files
%license COPYING
%doc README.md
%{_bindir}/%{appid}
%{_datadir}/applications/%{appid}.desktop
%{_datadir}/glib-2.0/schemas/%{appid}.gschema.xml
%{_datadir}/icons/hicolor/*/apps/%{appid}.svg
%{_datadir}/metainfo/%{appid}.appdata.xml
%{_datadir}/mime/packages/%{appid}.mime.xml
%dir %{_datadir}/icons/hicolor/{128x128@2,128x128@2/apps,16x16@2,16x16@2/apps,24x24@2,24x24@2/apps,32x32@2,32x32@2/apps,48x48@2,48x48@2/apps,64x64@2,64x64@2/apps}

%files lang -f %{appid}.lang

%changelog
