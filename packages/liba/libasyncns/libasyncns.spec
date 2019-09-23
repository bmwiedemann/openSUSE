#
# spec file for package libasyncns
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define so_name libasyncns0
Name:           libasyncns
Version:        0.8
Release:        0
Summary:        Asynchronous Name Service Library
License:        LGPL-2.1+
Group:          Development/Libraries/C and C++
Url:            http://0pointer.de/lennart/projects/libasyncns/
Source0:        http://0pointer.de/lennart/projects/libasyncns/libasyncns-%{version}.tar.gz
BuildRequires:  pkgconfig
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
A C library for executing name service queries asynchronously.
It is an asynchronous wrapper around getaddrinfo(3), getnameinfo(3),
res_query(3) and res_search(3) from libc and libresolv.

%package -n %{so_name}
Summary:        Asynchronous Name Service Library
Group:          System/Libraries

%description -n %{so_name}
A C library for executing name service queries asynchronously. It is
an asynchronous wrapper around getaddrinfo(3), getnameinfo(3),
res_query(3) and res_search(3) from libc and libresolv.

In contrast to GNU's asynchronous name resolving API,
getaddrinfo_a(), libasyncns does not make use of UNIX signals for
reporting completion of name queries. Instead, the API exports a
standard UNIX file descriptor which may be integerated into custom
main loops.

%package devel
Summary:        Development Files for libasyncns Client Development
Group:          Development/Libraries/C and C++
Requires:       %{so_name} = %{version}-%{release}

%description devel
A C library for executing name service queries asynchronously. It is
an asynchronous wrapper around getaddrinfo(3), getnameinfo(3),
res_query(3) and res_search(3) from libc and libresolv.

This subpackage contains libraries and header files for developing
applications that want to make use of libasyncns.

%post -n %{so_name} -p /sbin/ldconfig
%postun -n %{so_name} -p /sbin/ldconfig

%prep
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags}

%install
make %{?_smp_mflags} DESTDIR=%{buildroot} install
find %{buildroot} \( -name *.a -o -name *.la \) -delete
rm -rf %{buildroot}%{_datadir}/doc/libasyncns/

%files -n %{so_name}
%defattr(-,root,root)
%doc README LICENSE
%{_libdir}/libasyncns.so.*

%files devel
%defattr(-,root,root)
%{_includedir}/asyncns.h
%{_libdir}/libasyncns.so
%{_libdir}/pkgconfig/libasyncns.pc

%changelog
