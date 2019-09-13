#
# spec file for package liboop
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define lname   liboop4
Name:           liboop
Version:        1.0.1
Release:        0
Summary:        Low-Level Event Loop Management Library
License:        LGPL-2.1+
Group:          Development/Libraries/C and C++
Url:            https://www.lysator.liu.se/liboop
Source:         https://ftp.lysator.liu.se/pub/liboop/liboop-%version.tar.gz
Source1:        https://ftp.lysator.liu.se/pub/liboop/liboop-%version.tar.gz.sig
BuildRequires:  pkgconfig

%description
Liboop is a low-level event loop management library for POSIX-based
operating systems. It supports the development of modular, multiplexed
applications that may respond to events from several sources. It
replaces the "select() loop" and allows the registration of event
handlers for file and network I/O, timers, and signals. Because
processes use these mechanisms for almost all external communication,
liboop can be used as the basis for almost any application.

%package -n %lname
Summary:        Low-Level Event Loop Management Library
Group:          System/Libraries

%description -n %lname
Liboop is a low-level event loop management library for POSIX-based
operating systems. It supports the development of modular, multiplexed
applications that may respond to events from several sources. It
replaces the "select() loop" and allows the registration of event
handlers for file and network I/O, timers, and signals. Because
processes use these mechanisms for almost all external communication,
liboop can be used as the basis for almost any application.

%package devel
Summary:        Development Libraries and Header Files for liboop
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
This package contains the static libraries and header files needed to
develop programs which make use of the liboop programming interface.

%prep
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags}

%check
make check %{?_smp_mflags}

%install
%make_install
find "%buildroot" -type f -name "*.la" -delete

%post -n %lname -p /sbin/ldconfig

%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%defattr(-,root,root)
%_libdir/liboop.so.4*
%doc COPYING

%files devel
%defattr(-,root,root)
%_includedir/oop*
%_libdir/liboop.so
%_libdir/pkgconfig/liboop*

%changelog
