#
# spec file for package ucommon
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2008, 2009 David Sugar, Tycho Softworks.
# This file is free software; as a special exception the author gives
# unlimited permission to copy and/or distribute it, with or without
# modifications, as long as this notice is preserved.
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


Name:           ucommon
Version:        7.0.0
Release:        0
%define lname	libucommon8
Summary:        Runtime library for portable C++ threading and sockets
License:        LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
URL:            http://www.gnu.org/software/commoncpp

#Git-Clone:	https://git.savannah.gnu.org/cgit/commoncpp.git
Source:         http://ftp.gnu.org/gnu/commoncpp/%name-%version.tar.gz
Source2:        http://ftp.gnu.org/gnu/commoncpp/%name-%version.tar.gz.sig
Source3:        %name.keyring
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  graphviz-gd
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(openssl) < 1.1
# Added for 13.1
Obsoletes:      %name-bin < %version-%release
Provides:       %name-bin = %version-%release

%description
GNU uCommon C++ is a lightweight library to facilitate using C++
design patterns even for very deeply embedded applications, such as
for systems using uClibc along with POSIX threading support.

This subpackage contains a collection of command line tools that use
various aspects of the ucommon library. Some may be needed to prepare
files or for development of applications.

%package -n %lname
Summary:        GNU uCommon Runtime library for portable C++ threading and sockets
Group:          System/Libraries

%description -n %lname
GNU uCommon C++ is a lightweight library to facilitate using C++
design patterns even for very deeply embedded applications, such as
for systems using uClibc along with POSIX threading support. For this
reason, uCommon disables language features that consume memory or
introduce runtime overhead. uCommon introduces some design patterns
from Objective-C, such as reference counted objects, memory pools,
and smart pointers. uCommon introduces some new concepts for handling
of thread locking and synchronization.

%package devel
Summary:        Headers for building ucommon applications
Group:          Development/Libraries/C and C++
Requires:       %lname = %version
Requires:       pkgconfig(libcrypto)
Requires:       pkgconfig(libssl)

%description devel
This package provides header and support files needed for building
applications that use the uCommon library and frameworks.

%package doc
Summary:        Generated class documentation for ucommon
Group:          Documentation
BuildArch:      noarch

%description doc
Generated class documentation for GNU uCommon library from header files,
html browsable.

%prep
%autosetup -p1

%build
%configure --disable-static
%make_build

%install
%make_install
rm -f "%buildroot/%_libdir"/*.la
chmod a+x "%buildroot/%_bindir"/*-config

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files
%doc AUTHORS README NEWS SUPPORT ChangeLog
%_bindir/args
%_bindir/car
%_bindir/keywait
%_bindir/scrub-files
%_bindir/mdsum
%_bindir/urlout
%_bindir/pdetach
%_bindir/sockaddr
%_bindir/zerofill
%_mandir/man1/args.*
%_mandir/man1/scrub-files.*
%_mandir/man1/mdsum.*
%_mandir/man1/urlout.*
%_mandir/man1/pdetach.1*
%_mandir/man1/zerofill.*
%_mandir/man1/sockaddr.*
%_mandir/man1/car.*
%_mandir/man1/keywait.*

%files -n %lname
%license COPYING COPYING.LESSER COPYRIGHT
%_libdir/libucommon.so.8*
%_libdir/libusecure.so.8*
%_libdir/libcommoncpp.so.8*

%files devel
%_libdir/*.so
%_includedir/ucommon/
%_includedir/commoncpp/
%_datadir/ucommon/
%_libdir/pkgconfig/*.pc
%_bindir/ucommon-config
%_bindir/commoncpp-config
%_mandir/man1/ucommon-config.*
%_mandir/man1/commoncpp-config.*

%changelog
