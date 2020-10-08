#
# spec file for package popt
#
# Copyright (c) 2020 SUSE LLC
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


Name:           popt
Version:        1.18
Release:        0
#!BuildIgnore:  rpmlint-Factory
Summary:        A C library for parsing command line parameters
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://github.com/rpm-software-management/popt

Source:         http://ftp.rpm.org/popt/releases/popt-1.x/popt-%{version}.tar.gz
Source2:        baselibs.conf
Patch:          popt-libc-updates.patch
BuildRequires:  libtool
BuildRequires:  pkgconfig

%description
Popt is a C library for parsing command line parameters.  Popt was
heavily influenced by the getopt() and getopt_long() functions. It
improves on them by allowing more powerful argument expansion. Popt can
parse arbitrary argv[] style arrays and automatically set variables
based on command line arguments.  Popt allows command line arguments to
be aliased via configuration files and includes utility functions for
parsing arbitrary strings into argv[] arrays using shell-like rules.

%package -n libpopt0
Summary:        A C library for parsing command line parameters
Group:          System/Libraries
Provides:       popt = %{version}
Obsoletes:      popt < %{version}

%description -n libpopt0
Popt is a C library for parsing command line parameters.  Popt was
heavily influenced by the getopt() and getopt_long() functions. It
improves on them by allowing more powerful argument expansion. Popt can
parse arbitrary argv[] style arrays and automatically set variables
based on command line arguments.  Popt allows command line arguments to
be aliased via configuration files and includes utility functions for
parsing arbitrary strings into argv[] arrays using shell-like rules.

%package devel
Summary:        Development files for the popt library
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       libpopt0 = %{version}

%description devel
The popt-devel package includes header files and libraries necessary
for developing programs which use the popt C library. It contains the
API documentation of the popt library, too.

%prep
%autosetup -p1

%build
autoreconf -fiv
%configure --disable-static
%make_build

%install
%make_install
rm %{buildroot}%{_libdir}/libpopt.la

%find_lang %{name}

%post -n libpopt0 -p /sbin/ldconfig

%postun -n libpopt0 -p /sbin/ldconfig

%files -n libpopt0 -f %{name}.lang
%license COPYING
%doc CHANGES
%{_libdir}/libpopt.so.*

%files devel
%doc README
%{_libdir}/libpopt.so
%{_includedir}/popt.h
%{_mandir}/man3/popt.3*
%{_libdir}/pkgconfig/popt.pc

%changelog
