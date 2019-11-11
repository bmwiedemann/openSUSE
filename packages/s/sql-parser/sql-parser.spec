#
# spec file for package sql-parser
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


%define sover 1
%define libname libsqlparser%{sover}

Name:           sql-parser
Version:        1.5+git20181206
Release:        0
Summary:        SQL Parser for C++
License:        MIT
Url:            https://github.com/envoyproxy/%{name}
Source:         %{name}-%{version}.tar.xz
BuildRequires:  gcc-c++
BuildRequires:  patchelf

%description
A SQL Parser for C++. It parses the given SQL query into C++ objects. It has
been developed for integration in Hyrise, but can be used perfectly well in
other environments as well.

%package -n %{libname}
Summary:        Shared library for sql-parser

%description -n %{libname}
A SQL Parser for C++. It parses the given SQL query into C++ objects. It has
been developed for integration in Hyrise, but can be used perfectly well in
other environments as well.

This package contains shared library for sql-parser.

%package devel
Summary:        Development files for sql-parser
Requires:       %{libname} = %{version}

%description devel
A SQL Parser for C++. It parses the given SQL query into C++ objects. It has
been developed for integration in Hyrise, but can be used perfectly well in
other environments as well.

This package contains development files for sql-parser.

%prep
%setup -q
sed -i \
    -e "s|\$(INSTALL)/lib|%{buildroot}%{_libdir}|" \
    Makefile

%build
%make_build
patchelf --set-soname libsqlparser.so.%{sover} libsqlparser.so

%install
mkdir -p %{buildroot}%{_includedir}/sqlparser
mkdir -p %{buildroot}%{_libdir}
%make_install INSTALL=%{buildroot}%{_prefix}
mv %{buildroot}%{_libdir}/libsqlparser.so %{buildroot}%{_libdir}/libsqlparser.so.%{sover}
ln -sf libsqlparser.so.%{sover} %{buildroot}%{_libdir}/libsqlparser.so
cp -r include/sqlparser/* %{buildroot}%{_includedir}/sqlparser

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%license LICENSE
%doc README.md
%{_libdir}/libsqlparser.so.%{sover}

%files devel
%{_includedir}/hsql
%{_includedir}/sqlparser
%{_libdir}/libsqlparser.so

%changelog

