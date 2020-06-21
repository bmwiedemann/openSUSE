#
# spec file for package kColorPicker
#
# Copyright (c) 2020 SUSE LLC
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


%define sover   0_1_4
%define libname libkColorPicker%{sover}
Name:           kColorPicker
Version:        0.1.4
Release:        0
Summary:        Qt based Color Picker with popup menu
License:        GPL-2.0-or-later
Group:          Development/Tools/Other
URL:            https://github.com/DamirPorobic/kColorPicker
Source:         https://github.com/DamirPorobic/kColorPicker/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5Widgets)

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

%description devel
Development files for %{name} including headers and libraries

%prep
%setup -q

%build
%cmake
%make_jobs

%install
%cmake_install

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%license LICENSE
%{_libdir}/lib%{name}.so.*

%files devel
%doc README.md
%{_libdir}/lib%{name}.so
%{_libdir}/cmake/%{name}
%{_includedir}/%{name}

%changelog
