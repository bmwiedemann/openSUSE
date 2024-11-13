#
# spec file for package switchboard-plug-wacom
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


%define         appid io.elementary.settings.wacom
Name:           switchboard-plug-wacom
Version:        8.0.0
Release:        0
Summary:        Manage drawing tablets and Wacom devices
License:        GPL-3.0-or-later
URL:            https://github.com/elementary/switchboard-plug-wacom
Source0:        %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  vala
BuildRequires:  pkgconfig(granite-7)
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libwacom)
BuildRequires:  pkgconfig(switchboard-3)
BuildRequires:  pkgconfig(xi)
Requires:       switchboard

%description
%{summary}.

%lang_package

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{appid}

%files
%license COPYING
%doc README.md
%dir %{_libdir}/{switchboard-3,switchboard-3/hardware}
%{_libdir}/switchboard-3/hardware/libwacom.so
%{_datadir}/metainfo/%{appid}.metainfo.xml

%files lang -f %{appid}.lang

%changelog
