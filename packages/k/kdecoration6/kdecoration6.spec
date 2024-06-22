#
# spec file for package kdecoration6
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


%define kf6_version 6.2.0
%define qt6_version 6.6.0

%define rname kdecoration

%global sover 6
%global private_sover 11
%bcond_without released
Name:           kdecoration6
Version:        6.1.0
Release:        0
Summary:        KDE's window decorations library
License:        GPL-2.0-or-later
URL:            https://www.kde.org
Source:         %{rname}-%{version}.tar.xz
%if %{with released}
Source1:        %{rname}-%{version}.tar.xz.sig
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

%package -n libkdecorations2-%{sover}
Summary:        KDE's window decorations library
Obsoletes:      libkdecorations2-5-lang

%description -n libkdecorations2-%{sover}
Plugin based library to create window decorations.

%package -n libkdecorations2private%{private_sover}
Summary:        KDE's window decorations library

%description -n libkdecorations2private%{private_sover}
Plugin based library to create window decorations.

%package devel
Summary:        KDE's window decorations library (development package)
Requires:       libkdecorations2-%{sover} = %{version}
Requires:       libkdecorations2private%{private_sover} = %{version}
Requires:       cmake(Qt6Gui)
Obsoletes:      libkdecoration2-devel < %{version}

%description devel
Development files belonging to kdecoration,
plugin based library to create window decorations.

%lang_package -n libkdecorations2-%{sover}

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name} --all-name

%ldconfig_scriptlets -n libkdecorations2-%{sover}
%ldconfig_scriptlets -n libkdecorations2private%{private_sover}

%files -n libkdecorations2-%{sover}
%license LICENSES/*
%{_kf6_libdir}/libkdecorations2.so.*

%files -n libkdecorations2private%{private_sover}
%{_kf6_libdir}/libkdecorations2private.so.*

%files devel
%{_includedir}/KDecoration2/
%{_kf6_cmakedir}/KDecoration2/
%{_kf6_includedir}/kdecoration2_version.h
%{_kf6_libdir}/libkdecorations2.so
%{_kf6_libdir}/libkdecorations2private.so

%files -n libkdecorations2-%{sover}-lang -f %{name}.lang

%changelog
