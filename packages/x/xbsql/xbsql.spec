#
# spec file for package xbsql
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define lib_name lib%{name}0
Name:           xbsql
Version:        0.11
Release:        0
Summary:        SQL Wrapper for the XBase Library
License:        LGPL-2.1+
Group:          Development/Libraries/C and C++
Url:            http://www.quaking.demon.co.uk/xbsql.html
Source0:        %{name}-%{version}.tar.bz2
Patch0:         %{name}.diff
Patch1:         xbsql-0.11-bufferoverflowstrncat.patch
# PATCH-FIX-OPENSUSE xbase64.patch -- fix build with latest xbase(64) 3.1.2 in Factory
Patch2:         xbase64.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  ncurses-devel
BuildRequires:  readline-devel
BuildRequires:  xbase-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
XBase DBMS is a C++ library that supports access to XBase type data
files and indexes (.dbf and related files, for example). It provides
record level access to these files.

%package -n %{lib_name}
Summary:        Shared libraries for %{name}
Group:          Development/Libraries/C and C++

%description -n %{lib_name}
XBase DBMS is a C++ library that supports access to XBase type data
files and indexes (.dbf and related files, for example). It provides
record level access to these files.

This package contains shared libraries

%package devel
Summary:        Files for developing with %{name}
Group:          Development/Libraries/C and C++
Requires:       %{lib_name} = %{version}

%description devel
XBase DBMS is a C++ library that supports access to XBase type data
files and indexes (.dbf and related files, for example). It provides
record level access to these files.

This package contains development files

%prep
%setup -q
%patch0
%patch1
%patch2 -p1

%build
autoreconf -fi
%configure \
	--disable-static \
	--with-pic
rm xbsql/lex.yy.c
make %{?_smp_mflags} -C xbsql lex.yy.c
make %{?_smp_mflags}

%check
cd test
make %{?_smp_mflags}
./runtests

%install
make DESTDIR="$RPM_BUILD_ROOT" install
#
# solve file conflict with perl-XML-XQL
#
mv %{buildroot}%{_bindir}/xql %{buildroot}%{_bindir}/XQL
find %{buildroot} -type f -name "*.la" -delete -print

%post -n %{lib_name} -p /sbin/ldconfig

%postun -n %{lib_name} -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc AUTHORS TODO COPYING README doc
%{_bindir}/*

%files -n %{lib_name}
%defattr(-,root,root)
%{_libdir}/libxbsql.so.*

%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/libxbsql.so

%changelog
