#
# spec file for package chmlib
#
# Copyright (c) 2023 SUSE LLC
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


%define lname	libchm0
Name:           chmlib
Version:        0.40
Release:        0
Summary:        A library for dealing with ITSS/CHM files
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            http://www.jedrea.com/chmlib/
Source0:        http://www.jedrea.com/chmlib/%{name}-%{version}.tar.bz2
Source2:        baselibs.conf
# backported from upstream
Patch1:         chmlib-0001-Patch-to-fix-integer-types-problem-by-Goswin-von-Bre.patch
# backported from upstream
Patch2:         chmlib-0002-Fix-for-extract_chmLib-confusing-empty-files-with-di.patch
# PATCH-FIX-UPSTREAM: https://github.com/jedwing/CHMLib/pull/10
Patch3:         chm_http-port-shortopt.patch
# PATCH-FIX-UPSTREAM: https://github.com/jedwing/CHMLib/pull/11
Patch4:         chm_http-bind-localhost.patch
# PATCH-FIX-UPSTREAM: https://github.com/jedwing/CHMLib/pull/12
Patch5:         chm_http-output-server-address.patch
# PATCH-FIX-UPSTREAM: https://github.com/jedwing/CHMLib/pull/17
Patch6:         chmlib-c99.patch
BuildRequires:  gcc-c++

%description
CHMLIB is a library for dealing with Microsoft ITSS/CHM format files.

%package -n %{lname}
Summary:        A library for dealing with ITSS/CHM files
Group:          System/Libraries
Obsoletes:      chmlib < %{version}-%{release}
Provides:       chmlib = %{version}-%{release}

%description -n %{lname}
CHMLIB is a library for dealing with Microsoft ITSS/CHM format files.

%package      devel
Summary:        Documentation and Headers for chmlib
Group:          System/Libraries
Requires:       %{lname} = %{version}

%description	devel
This package contains the headers and documentation for the chmlib API
that programmers will need to develop applications which use chmlib,
the software library for dealing with Microsoft ITSS/CHM format files.

%package        examples
Summary:        Example applications for chmlib
Group:          System/Libraries
Requires:       %{lname} = %{version}

%description	examples
This package contains examples built on chmlib which may be useful
to convert chm files from command line.

%prep
%autosetup -p1

%build
export CFLAGS="%{optflags} -fstack-protector"
export CXXFLAGS="$CFLAGS"
export CXXCPP="g++ -E"
%configure \
	--disable-static \
	--disable-pread \
	--enable-examples
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}
%license COPYING
%doc AUTHORS NEWS README
%{_libdir}/*.so.*

%files devel
%{_includedir}/chm_lib.h
%{_includedir}/lzx.h
%{_libdir}/*.so

%files examples
%{_bindir}/*

%changelog
