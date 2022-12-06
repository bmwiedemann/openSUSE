#
# spec file for package belcard
#
# Copyright (c) 2022 SUSE LLC
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


%define soname  libbelcard
%define sover   1
Name:           belcard
Version:        5.1.72
Release:        0
Summary:        C++ library to manipulate vCard standard format files
License:        GPL-3.0-or-later
Group:          Development/Languages/C and C++
URL:            https://linphone.org/
Source:         https://gitlab.linphone.org/BC/public/belcard/-/archive/%{version}/%{name}-%{version}.tar.bz2
Source1:        baselibs.conf
# PATCH-FIX-OPENSUSE belcard-fix-pkgconfig.patch sor.alexei@meowr.ru -- Install belcard.pc.
Patch0:         belcard-fix-pkgconfig.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libudev-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(bctoolbox) >= 5.0.0
BuildRequires:  pkgconfig(belr) >= 5.0.0

%description
Belcard is a C++ library to manipulate the vCard standard format files.

%package -n %{soname}%{sover}
Summary:        C++ library to manipulate vCard standard format files
Group:          Development/Languages/C and C++
Requires:       %{name}-data >= %{version}

%description -n %{soname}%{sover}
Belcard is a C++ library to manipulate the vCard standard format files.

%package data
Summary:        Belcard data files
Group:          Development/Languages/C and C++
Requires:       %{soname}%{sover} = %{version}
BuildArch:      noarch

%description data
Belcard is a C++ library to manipulate the vCard standard format files.

This package contains data files such as belr grammar.

%package devel
Summary:        Headers and libraries for the belcard library
Group:          Development/Languages/C and C++
Requires:       %{soname}%{sover} = %{version}

%description devel
Belcard is a C++ library to manipulate the vCard standard format files.

This package contains header files and development libraries needed
to develop applications using the belcard library.

%prep
%autosetup -p1

%build
%cmake \
  -DENABLE_STRICT=OFF \
  -DENABLE_STATIC=OFF
%cmake_build

%install
%cmake_install

%post -n %{soname}%{sover} -p /sbin/ldconfig
%postun -n %{soname}%{sover} -p /sbin/ldconfig

%files -n %{soname}%{sover}
%license LICENSE.txt
%{_libdir}/%{soname}.so.%{sover}*

%files data
%dir %{_datadir}/belr/
%{_datadir}/belr/grammars/

%files devel
%license LICENSE.txt
%doc CHANGELOG.md README.md
%{_bindir}/%{name}*
%{_includedir}/%{name}/
%{_libdir}/%{soname}.so
%{_datadir}/%{name}/
%{_datadir}/%{name}_tester/
%{_libdir}/pkgconfig/%{name}.pc

%changelog
