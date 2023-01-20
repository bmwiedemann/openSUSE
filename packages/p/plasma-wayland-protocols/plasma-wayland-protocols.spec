#
# spec file for package plasma-wayland-protocols
#
# Copyright (c) 2023 SUSE LLC
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


%bcond_without lang
Name:           plasma-wayland-protocols
Version:        1.10
Release:        0
Summary:        Wayland protocols used by Plasma
License:        BSD-3-Clause AND LGPL-2.1-only AND LGPL-2.1-or-later AND MIT
Group:          System/GUI/KDE
URL:            https://www.kde.org
Source0:        https://download.kde.org/stable/%{name}/%{name}-%{version}.tar.xz
BuildRequires:  extra-cmake-modules
BuildRequires:  fdupes
BuildRequires:  kf5-filesystem
%if %{with lang}
Source1:        https://download.kde.org/stable/%{name}/%{name}-%{version}.tar.xz.sig
# Note: The key in there is currently only self-signed and so not actually trusted.
Source2:        plasma-wayland-protocols.keyring
%endif

%description
This package contains the non-standard Wayland protocol definitions used by
KDE Plasma.

%prep
%autosetup -p1

%build
  %cmake_kf5 -d build
  %cmake_build

%install
  %kf5_makeinstall -C build
  %fdupes %{buildroot}

%files
%license COPYING* LICENSES/*.txt
%{_kf5_sharedir}/plasma-wayland-protocols/
%{_kf5_cmakedir}/PlasmaWaylandProtocols/

%changelog
