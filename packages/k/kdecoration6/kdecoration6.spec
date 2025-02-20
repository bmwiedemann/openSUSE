#
# spec file for package kdecoration6
#
# Copyright (c) 2025 SUSE LLC
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


%define kf6_version 6.10.0
%define qt6_version 6.7.0

%define rname kdecoration

%global sover 6
%global private_sover 1
%bcond_without released
Name:           kdecoration6
Version:        6.3.1
Release:        0
Summary:        KDE's window decorations library
License:        GPL-2.0-or-later
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/plasma/%{version}/%{rname}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/plasma/%{version}/%{rname}-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}

%description
Plugin based library to create window decorations.

%package -n libkdecorations3-%{sover}
Summary:        KDE's window decorations library

%description -n libkdecorations3-%{sover}
Plugin based library to create window decorations.

%package -n libkdecorations3private%{private_sover}
Summary:        KDE's window decorations library
%if "%{private_sover}" == "1"
# Had wrong name once
Obsoletes:      libkdecorations3private11 <= %{version}
%endif

%description -n libkdecorations3private%{private_sover}
Plugin based library to create window decorations.

%package devel
Summary:        KDE's window decorations library (development package)
Requires:       libkdecorations3-%{sover} = %{version}
Requires:       libkdecorations3private%{private_sover} = %{version}
Requires:       cmake(Qt6Gui)

%description devel
Development files belonging to kdecoration,
plugin based library to create window decorations.

%lang_package -n libkdecorations3-%{sover}

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name} --all-name

%ldconfig_scriptlets -n libkdecorations3-%{sover}
%ldconfig_scriptlets -n libkdecorations3private%{private_sover}

%files -n libkdecorations3-%{sover}
%license LICENSES/*
%{_kf6_libdir}/libkdecorations3.so.%{sover}
%{_kf6_libdir}/libkdecorations3.so.*

%files -n libkdecorations3private%{private_sover}
%{_kf6_libdir}/libkdecorations3private.so.%{private_sover}
%{_kf6_libdir}/libkdecorations3private.so.*

%files devel
%{_includedir}/KDecoration3/
%{_kf6_cmakedir}/KDecoration3/
%{_kf6_includedir}/kdecoration3_version.h
%{_kf6_libdir}/libkdecorations3.so
%{_kf6_libdir}/libkdecorations3private.so

%files -n libkdecorations3-%{sover}-lang -f %{name}.lang

%changelog
