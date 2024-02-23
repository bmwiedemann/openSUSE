#
# spec file for package kColorPicker
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


%global qtver 0
%if "@BUILD_FLAVOR@" == ""
ExclusiveArch:  do_not_build
%endif
%if "@BUILD_FLAVOR@" == "qt5"
%global qtver 5
%endif
%if "@BUILD_FLAVOR@" == "qt6"
%global qtver 6
%endif

%define sover   0
%define libname libkColorPicker-Qt%{qtver}-%{sover}
%if %{qtver} == 0
Name:           kColorPicker
%else
Name:           kColorPicker-Qt%{qtver}
%endif
Version:        0.3.0
Release:        0
Summary:        Qt based Color Picker with popup menu
License:        GPL-2.0-or-later
Group:          Development/Tools/Other
URL:            https://github.com/DamirPorobic/kColorPicker
Source:         https://github.com/DamirPorobic/kColorPicker/archive/v%{version}.tar.gz#/kColorPicker-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  cmake(Qt%{qtver}Test)
BuildRequires:  cmake(Qt%{qtver}Widgets)

%description
QToolButton with color popup menu with lets you select a color. The popup
featues a color dialog button which can be used to add custom colors to the
popup menu.

%package -n %{libname}
Summary:        Qt based Color Picker with popup menu
Group:          System/Libraries

%description -n %{libname}
QToolButton with color popup menu with lets you select a color. The popup
featues a color dialog button which can be used to add custom colors to the
popup menu.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}
%if %{qtver} == 5
Obsoletes:      kColorPicker-devel < %{version}
%endif

%description devel
Development files for %{name} including headers and libraries

%prep
%autosetup -p1 -n kColorPicker-%{version}

%build
%define opts -DBUILD_TESTS=TRUE -DBUILD_EXAMPLE=FALSE
%if %{qtver} == 6
    %cmake_qt6 -DBUILD_WITH_QT6=TRUE -DBUILD_SHARED_LIBS=TRUE %{opts}
    %qt6_build
%else
    %cmake %{opts}
    %cmake_build
%endif

%install
%if %{qtver} == 6
    %qt6_install
%else
    %cmake_install
%endif

%check
export QT_QPA_PLATFORM=offscreen
%ctest

%ldconfig_scriptlets -n %{libname}

%files -n %{libname}
%license LICENSE
%{_libdir}/lib%{name}.so.%{sover}
%{_libdir}/lib%{name}.so.%{sover}.*

%files devel
%doc README.md
%{_libdir}/lib%{name}.so
%{_libdir}/cmake/%{name}
%{_includedir}/%{name}

%changelog
