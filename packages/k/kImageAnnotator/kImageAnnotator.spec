#
# spec file for package kImageAnnotator
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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

%define sover   0_1_0
%define libname libkImageAnnotator%{sover}
Name:           kImageAnnotator
Version:        0.1.0
Release:        0
Summary:        Tool for annotating images
License:        GPL-2.0-or-later
Group:          Development/Tools/Other
URL:            https://github.com/DamirPorobic/kImageAnnotator
Source:         https://github.com/DamirPorobic/kImageAnnotator/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/DamirPorobic/kImageAnnotator/master/LICENSE
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(x11)
BuildRequires:  kColorPicker-devel

%description
kImageAnnotator is a tool for annotating images.

%package -n %{libname}
Summary:        Tool for annotating images
Group:          System/Libraries

%description -n %{libname}
kImageAnnotator is a tool for annotating images.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description devel
Development files for %{name} including headers and libraries

%prep
%setup -q
cp %{SOURCE1} .

%build
%cmake \
    -DBUILD_EXAMPLE=ON
make %{?_smp_mflags}

%install
%cmake_install

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%license LICENSE
%{_libdir}/lib%{name}.so.*

%files devel
%doc CHANGELOG.md README.md
%{_libdir}/lib%{name}.so
%{_libdir}/cmake/%{name}
%{_includedir}/%{name}

%changelog

