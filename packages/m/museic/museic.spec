#
# spec file for package museic
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


%define         appid com.github.bcedu.museic
Name:           museic
Version:        2.1.3
Release:        0
Summary:        Audio player with remote control
License:        GPL-3.0-only
URL:            https://github.com/bcedu/MuseIC
Source0:        %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  vala
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(granite) >= 0.5
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)

%description
MuseIC is a fast and simple music player with remote control from any
device through internet browser.

%prep
%autosetup -n MuseIC-%{version}

%build
%cmake \
    -DGSETTINGS_COMPILE=ON
%make_build

%install
%cmake_install
#fix upstream
rm %{buildroot}%{_datadir}/icons/hicolor/%{appid}.svg
%fdupes %{buildroot}

%files
%license LICENSE
%doc AUTHORS README.md
%{_bindir}/%{appid}
%{_datadir}/applications/%{appid}.desktop
%{_datadir}/%{appid}
%{_datadir}/glib-2.0/schemas/%{appid}.gschema.xml
%{_datadir}/icons/hicolor/*/apps/%{appid}.svg
%{_datadir}/metainfo/%{appid}.appdata.xml

%changelog
