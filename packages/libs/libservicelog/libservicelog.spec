#
# spec file for package libservicelog
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


Name:           libservicelog
%define lname	libservicelog-1_1-1
Version:        1.1.18
Release:        0
Summary:        Servicelog Database and Library
License:        LGPL-2.0+
Group:          System/Libraries
Url:            http://linux-diag.sourceforge.net/servicelog/

#Git-Clone:	git://git.code.sf.net/p/linux-diag/libservicelog
#Git-Web:	http://sourceforge.net/p/linux-diag/libservicelog/
Source0:        http://downloads.sourceforge.net/linux-diag/%{name}-%{version}.tar.gz
Source1:        baselibs.conf
Source2:        libservicelog-rpmlintrc
PreReq:         %{_sbindir}/groupadd
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  librtas-devel
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  sqlite3-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
ExclusiveArch:  ppc ppc64 ppc64le

%description
The libservicelog package contains a library to create and maintain a
database for storing events related to system service. This database
allows for the logging of serviceable and informational events, and for
the logging of service procedures that have been performed upon the
system.

%package -n %lname
Summary:        Servicelog Database and Library
Group:          System/Libraries
Requires:       %name

%description -n %lname
The libservicelog package contains a library to create and maintain a
database for storing events related to system service. This database
allows for the logging of serviceable and informational events, and for
the logging of service procedures that have been performed upon the
system.

%package        devel
Summary:        Development files for libservicelog
Group:          Development/Libraries/Other
Requires:       %lname = %version
Requires:       glibc-devel
Requires:       sqlite3-devel

%description    devel
Contains header files for building with libservicelog.

%prep
%setup -q

%build
autoreconf -fiv
%configure --with-pic --disable-static
make %{?_smp_mflags}

%install
%make_install
%__rm -f %{buildroot}%{_libdir}/*.la

%pre
/usr/sbin/groupadd -r service || echo groupadd service failed

%post    -n %lname -p /sbin/ldconfig
%postun  -n %lname -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc COPYING AUTHORS
%attr( 754, root, service ) %dir /var/lib/servicelog
%attr( 644, root, service ) /var/lib/servicelog/servicelog.db

%files -n %lname
%defattr(-,root,root,-)
%{_libdir}/lib*.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/servicelog-1
%{_libdir}/pkgconfig/servicelog-1.pc
%{_libdir}/*.so

%changelog
