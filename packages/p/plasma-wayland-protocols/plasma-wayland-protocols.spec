#
# spec file for package plasma-wayland-protocols
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


%bcond_without released
Name:           plasma-wayland-protocols
Version:        1.15.0
Release:        0
Summary:        Wayland protocols used by Plasma
License:        BSD-3-Clause AND LGPL-2.1-only AND LGPL-2.1-or-later AND MIT
Group:          System/GUI/KDE
URL:            https://www.kde.org
Source0:        https://download.kde.org/stable/plasma-wayland-protocols/plasma-wayland-protocols-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/plasma-wayland-protocols/plasma-wayland-protocols-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
BuildRequires:  fdupes
BuildRequires:  kf6-extra-cmake-modules

%description
This package contains the non-standard Wayland protocol definitions used by
KDE Plasma.

%prep
%autosetup -p1

%build
%cmake_kf6
%kf6_build

%install
%kf6_install
%fdupes %{buildroot}

%files
%license COPYING* LICENSES/*.txt
%{_kf6_sharedir}/plasma-wayland-protocols/
%{_kf6_cmakedir}/PlasmaWaylandProtocols/

%changelog
