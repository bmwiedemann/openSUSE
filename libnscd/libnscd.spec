#
# spec file for package libnscd
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


Name:           libnscd
%define lname	libnscd1
Version:        2.0.2
Release:        0
Summary:        Library to Allow Applications to Communicate with nscd
License:        LGPL-2.1
Group:          Development/Libraries/C and C++

Source:         http://ftp.suse.com/pub/people/kukuk/libnscd/libnscd-%version.tar.bz2
Source2:        baselibs.conf
Patch:          decls.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
# bug437293
%ifarch ppc64
Obsoletes:      libnscd-64bit
%endif

%description
This library provides an interface for applications to NSCD (Name
Service Cache Daemon) and allows those applications, to flush the cache
for special services, if they have the necessary permissions.

%package -n %lname
Summary:        Library to Allow Applications to Communicate with nscd
# O/P added for 13.1
License:        LGPL-2.1
Group:          System/Libraries
Obsoletes:      libnscd < %version-%release
Provides:       libnscd = %version-%release

%description -n %lname
This library provides an interface for applications to NSCD (Name
Service Cache Daemon) and allows those applications, to flush the
cache for special services, if they have the necessary permissions.

%package devel
Summary:        Development files for libnscd
License:        LGPL-2.1+
Group:          Development/Libraries/C and C++
Requires:       %lname = %version
# bug437293
%ifarch ppc64
Obsoletes:      libnscd-devel-64bit
%endif
#

%description devel
This package contains all necessary include files and libraries needed
to develop applications that needs to communicate with a running nscd.



%prep
%setup -q
%patch -p1

%build
%configure --disable-static
make %{?_smp_mflags}

%check
make check

%install
%make_install
rm -fv %{buildroot}%{_libdir}/*.la

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%defattr(-,root,root)
%doc COPYING.LIB README NEWS
%{_libdir}/libnscd.so.*

%files devel
%defattr(-,root,root)
%{_includedir}/*.h
%{_libdir}/libnscd.so
%{_mandir}/man3/nscd_flush_cache.3*

%changelog
