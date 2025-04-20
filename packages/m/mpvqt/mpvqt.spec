#
# spec file for package mpvqt
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


%define kf6_version 6.0.0
%define qt6_version 6.5.0

%bcond_without released
Name:           mpvqt
Version:        1.1.1
Release:        0
Summary:        Libmpv wrapper for QtQuick2 and QML
License:        LGPL-2.1-or-later
URL:            https://invent.kde.org/libraries/mpvqt
Source:         https://download.kde.org/stable/mpvqt/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/mpvqt/%{name}-%{version}.tar.xz.sig
Source2:        mpvqt.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  pkgconfig
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  pkgconfig(mpv)

%description
MpvQt is a libmpv wrapper for QtQuick2 and QML.

%package -n libMpvQt2
Summary:        Libmpv wrapper for QtQuick2 and QML
# Marked as runtime deps in the build system, but looks unneeded
# Recommends:     (yt-dlp or youtube-dl)

%description -n libMpvQt2
MpvQt is a libmpv wrapper for QtQuick2 and QML.

%package devel
Summary:        Development files for mpvqt
Requires:       libMpvQt2 = %{version}
Requires:       cmake(Qt6Quick) >= %{qt6_version}
Requires:       pkgconfig(mpv)

%description devel
This package provides development files needed to use mpvqt in your applications.

%prep
%autosetup -p1

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%ldconfig_scriptlets -n libMpvQt2

%files -n libMpvQt2
%license LICENSES/*
%{_kf6_libdir}/libMpvQt.so.*

%files devel
%doc README.md
%{_includedir}/MpvQt/
%{_kf6_cmakedir}/MpvQt/
%{_kf6_libdir}/libMpvQt.so

%changelog
