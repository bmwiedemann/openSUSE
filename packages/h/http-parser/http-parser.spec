#
# spec file for package http-parser
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


%define soname 2_7_1
%define libname libhttp_parser%{soname}
Name:           http-parser
Version:        2.7.1
Release:        0
Summary:        HTTP request/response parser for C
License:        MIT
Group:          Development/Libraries/C and C++
Url:            https://github.com/nodejs/http-parser
Source0:        https://github.com/nodejs/http-parser/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        baselibs.conf
Patch0:         makefile.patch
BuildRequires:  gcc-c++

%description
This is a parser for HTTP messages written in C. It parses both
requests and responses. The parser is designed to be used in
performance HTTP applications. It does not make any syscalls nor
allocations, it does not buffer data, it can be interrupted at
anytime. Depending on your architecture, it only requires about 40
bytes of data per message stream (in a web server that is per
connection).

%package        -n %{libname}
Summary:        HTTP request/response parser for C
Group:          System/Libraries
Provides:       libhttp-parser-suse0 = %{version}
Obsoletes:      libhttp-parser-suse0 <= %{version}

%description    -n %{libname}
This is a parser for HTTP messages written in C. It parses both
requests and responses. The parser is designed to be used in
performance HTTP applications. It does not make any syscalls nor
allocations, it does not buffer data, it can be interrupted at
anytime. Depending on your architecture, it only requires about 40
bytes of data per message stream (in a web server that is per
connection).

%package devel
Summary:        Development headers and libraries for http-parser
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description devel
This is a parser for HTTP messages written in C. It parses both
requests and responses. The parser is designed to be used in
performance HTTP applications. It does not make any syscalls nor
allocations, it does not buffer data, it can be interrupted at
anytime. Depending on your architecture, it only requires about 40
bytes of data per message stream (in a web server that is per
connection).

Development headers and libraries for http-parser.

%prep
%setup -q
%patch0 -p1

%build
make %{?_smp_mflags} PREFIX=%{_prefix} library

%install
make PREFIX=%{_prefix} DESTDIR=%{buildroot} LIBDIR=%{_libdir}  install
chmod a-x  %{buildroot}/%{_includedir}/*.h

%check
make %{?_smp_mflags} test

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%doc AUTHORS LICENSE-MIT README.md
%{_libdir}/libhttp_parser.so.*

%files devel
%{_includedir}/*
%{_libdir}/libhttp_parser.so

%changelog
