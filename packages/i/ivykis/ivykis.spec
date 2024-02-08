#
# spec file for package ivykis
#
# Copyright (c) 2024 SUSE LLC
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


%define lname   libivykis0
Name:           ivykis
Version:        0.43
Release:        0
Summary:        An event dispatching library
License:        LGPL-2.1-only
Group:          Development/Libraries/C and C++
URL:            https://sourceforge.net/projects/libivykis/
Source:         https://downloads.sf.net/libivykis/%name-%version.tar.gz
BuildRequires:  c_compiler
BuildRequires:  pkg-config

%description
libivykis is a wrapper over various OS'es implementation of I/O
readiness notification facilities (such as poll(2), kqueue(2)) and
can be used for writing portable network servers.

%package -n %lname
Summary:        An event dispatching library
Group:          System/Libraries

%description -n %lname
libivykis is a wrapper over various OS'es implementation of I/O
readiness notification facilities (such as poll(2), kqueue(2)) and
can be used for writing portable network servers.

%package devel
Summary:        Development files for libivykis, an event dispatching library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
libivykis is a wrapper over various OS'es implementation of I/O
readiness notification facilities (such as poll(2), kqueue(2)) and
can be used for writing portable network servers.

This package contains the header files and development symlinks.

%prep
%autosetup -p1

%build
# includedir intentional, cf. bugzilla.opensuse.org/795968
%configure --disable-static --includedir="%_includedir/%name"
%make_build

%install
%make_install
find %buildroot -type f -name "*.la" -delete -print

%check
%make_build check

%post -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%_libdir/libivykis.so.0*

%files devel
%_includedir/%name/
%_libdir/libivykis.so
%_libdir/pkgconfig/ivykis.pc
%_mandir/man3/iv*.3*
%_mandir/man3/IV*.3*

%changelog
