#
# spec file for package cage
#
# Copyright (c) 2021 SUSE LLC
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


Name:           cage
Version:        0.1.4+39.a81ab70
Release:        0
Summary:        Wayland Kiosk
License:        MIT
Group:          System/GUI/Other
URL:            https://www.hjdskes.nl/projects/cage/
Source:         %{name}-%{version}.tar.gz
Patch0:         https://patch-diff.githubusercontent.com/raw/Hjdskes/cage/pull/244.patch#/cage-wlroots-016-compat.patch
BuildRequires:  meson >= 0.43.0
BuildRequires:  pkgconfig
BuildRequires:  scdoc
BuildRequires:  wlroots-devel >= 0.16.0
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.14
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(xkbcommon)

%description
A Wayland Kiosk.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1

%build
%meson
%meson_build

%install
%meson_install

%files
%license LICENSE
%doc README.md
%{_bindir}/cage
%{_mandir}/man1/cage.1%{?ext_man}

%changelog
