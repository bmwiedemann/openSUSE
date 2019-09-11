#
# spec file for package belcard
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define soname  libbelcard
%define sover   1
Name:           belcard
Version:        1.0.2
Release:        0
Summary:        C++ library to manipulate vCard standard format files
License:        GPL-3.0+
Group:          Development/Libraries/C and C++
Url:            https://linphone.org/
Source:         https://linphone.org/releases/sources/%{name}/%{name}-%{version}.tar.gz
Source1:        baselibs.conf
# PATCH-FIX-OPENSUSE belcard-fix-pkgconfig.patch sor.alexei@meowr.ru -- Install belcard.pc.
Patch0:         belcard-fix-pkgconfig.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(bctoolbox) >= 0.6.0
BuildRequires:  pkgconfig(belr)

%description
Belcard is a C++ library to manipulate the vCard standard format files.

%package -n %{soname}%{sover}
Summary:        C++ library to manipulate vCard standard format files
Group:          System/Libraries

%description -n %{soname}%{sover}
Belcard is a C++ library to manipulate the vCard standard format files.

%package devel
Summary:        Headers and libraries for the belcard library
Group:          Development/Libraries/C and C++
Requires:       %{soname}%{sover} = %{version}

%description devel
Belcard is a C++ library to manipulate the vCard standard format files.

This package contains header files and development libraries needed
to develop applications using the belcard library.

%prep
%setup -q -n %{name}-%{version}-0
%patch0 -p1

%build
%cmake \
  -DENABLE_STRICT=OFF \
  -DENABLE_STATIC=OFF
make %{?_smp_mflags} V=1

%install
%cmake_install

%post -n %{soname}%{sover} -p /sbin/ldconfig

%postun -n %{soname}%{sover} -p /sbin/ldconfig

%files -n %{soname}%{sover}
%doc COPYING
%{_libdir}/%{soname}.so.%{sover}*

%files devel
%doc COPYING NEWS README.md
%{_bindir}/%{name}*
%{_includedir}/%{name}/
%{_libdir}/%{soname}.so
%{_datadir}/belcard_tester/
%{_datadir}/Belcard/
%{_libdir}/pkgconfig/%{name}.pc

%changelog
