#
# spec file for package libid3tag
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


%define lver 0_16_2
Name:           libid3tag
Version:        0.16.2
Release:        0
Summary:        ID3 Tag Manipulation Library
License:        GPL-2.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://github.com/tenacityteam/libid3tag
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        baselibs.conf
BuildRequires:  c++_compiler
BuildRequires:  cmake
BuildRequires:  gperf
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(zlib)

%description
libid3tag is a library for reading and writing ID3 tags, both ID3v1 and
the various versions of ID3v2.

%package -n %{name}%{lver}
Summary:        ID3 Tag Manipulation Library
Group:          System/Libraries

%description -n %{name}%{lver}
libid3tag is a library for reading and writing ID3 tags, both ID3v1 and
the various versions of ID3v2.

%package devel
Summary:        Development package for libid3tag library
Group:          Development/Libraries/C and C++
Requires:       %{name}%{lver} = %{version}

%description devel
This package contains the header files and static libraries needed to
develop applications with libid3tag.

%prep
%setup -q

%build
%cmake
%cmake_build

%install
%cmake_install

%post -n %{name}%{lver} -p /sbin/ldconfig
%postun -n %{name}%{lver} -p /sbin/ldconfig

%files -n %{name}%{lver}
%license COPYING COPYRIGHT
%{_libdir}/libid3tag.so.*

%files devel
%doc CHANGES CREDITS README
%{_includedir}/id3tag.h
%{_libdir}/libid3tag.so
%{_libdir}/cmake/id3tag
%{_libdir}/pkgconfig/id3tag.pc

%changelog
