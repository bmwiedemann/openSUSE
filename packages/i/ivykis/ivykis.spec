#
# spec file for package ivykis
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


Name:           ivykis
%define lname   libivykis0
Version:        0.42.1
Release:        0
Summary:        An event dispatching library
License:        LGPL-2.1
Group:          Development/Libraries/C and C++
Url:            http://sf.net/projects/libivykis/

#Freshcode-URL:	http://freshcode.club/projects/ivykis
#Git-Clone:	git://github.com/buytenh/ivykis
Source:         http://downloads.sf.net/libivykis/%name-%version.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  pkgconfig
%if 0%{?suse_version} || 0%{?sles_version}
BuildRequires:  fdupes
%endif

%description
libivykis is a thin wrapper over various OS'es implementation of I/O
readiness notification facilities (such as poll(2), kqueue(2)) and is
mainly intended for writing portable high-performance network
servers.

%package -n %lname
Summary:        An event dispatching library
Group:          System/Libraries

%description -n %lname
libivykis is a thin wrapper over various OS'es implementation of I/O
readiness notification facilities (such as poll(2), kqueue(2)) and is
mainly intended for writing portable high-performance network
servers.

%package devel
Summary:        Development files for libivykis, an event dispatching library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
libivykis is a thin wrapper over various OS'es implementation of I/O
readiness notification facilities (such as poll(2), kqueue(2)) and is
mainly intended for writing portable high-performance network
servers.

This package contains the header files and development symlinks.

%prep
%if 0%{?__xz:1}
%setup -q
%else
tar -xf "%{S:0}" --use=xz;
%setup -DTq
%endif

%build
%configure --disable-static --includedir=%_includedir/%name-%version
make %{?_smp_mflags}

%install
b="%buildroot";
make install DESTDIR="$b";
rm -f "$b/%_libdir"/*.la;
%if 0%{?fdupes:1}
%fdupes %buildroot/%_prefix
%endif

%check
make %{?_smp_mflags} check;

%post -n %lname -p /sbin/ldconfig

%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%defattr(-,root,root)
%_libdir/libivykis.so.0*

%files devel
%defattr(-,root,root)
%_includedir/%name-%version
%_libdir/libivykis.so
%_libdir/pkgconfig/ivykis.pc
%_mandir/man3/iv*.3*
%_mandir/man3/IV*.3*

%changelog
