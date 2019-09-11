#
# spec file for package crossguid
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

%define sover 0

Name:           crossguid
Version:        0.2.2.20190128T092719.8fee233
Release:        0
Summary:        Cross platform C++ GUID/UUID library 
License:        MIT
Group:          Development/Libraries/C and C++
Url:            https://github.com/graeme-hill/crossguid
Source0:        %{name}-%{version}.tar.xz
Patch0:         crossguid.patch
BuildRequires:  cmake >= 3.8
%if %{suse_version} < 1500
BuildRequires:  gcc8-c++
%else
BuildRequires:  gcc-c++
%endif
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(uuid)

%description
Lightweight cross platform C++ GUID/UUID library

%package devel
Summary:        Development files for lib%{name}
Group:          Development/Libraries/C and C++
Requires:       lib%{name}%{sover} = %{version}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use lib%{name}.

%package     -n lib%{name}%{sover}
Summary:        C++ GUID/UUID library
Group:          System/Libraries

%description -n lib%{name}%{sover}
Lightweight cross platform C++ GUID/UUID library

%prep
%autosetup -p1

%build
test -x "$(type -p g++)"   && export CXX="$_"
test -x "$(type -p g++-7)" && export CXX="$_"
test -x "$(type -p g++-8)" && export CXX="$_"
test -x "$(type -p g++-9)" && export CXX="$_"
%cmake
%make_jobs

%install
%cmake_install

%post   -n lib%{name}%{sover} -p /sbin/ldconfig
%postun -n lib%{name}%{sover} -p /sbin/ldconfig

%files -n lib%{name}%{sover}
%license LICENSE
%{_libdir}/lib%{name}.so.%{sover}*

%files devel
%{_includedir}/*
%{_datadir}/*
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/*.pc

%changelog
