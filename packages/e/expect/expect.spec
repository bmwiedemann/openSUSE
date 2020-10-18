#
# spec file for package expect
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


Name:           expect
Version:        5.45.4
Release:        0
Summary:        A Tool for Automating Interactive Programs
License:        SUSE-Public-Domain
Group:          Development/Languages/Tcl
URL:            http://expect.nist.gov
Source:         https://downloads.sourceforge.net/expect/expect%version.tar.gz
Source1:        expect-rpmlintrc
Patch1:         expect.patch
Patch2:         expect-fixes.patch
Patch3:         expect-log.patch
Patch4:         config-guess-sub-update.patch
BuildRequires:  autoconf
BuildRequires:  tcl-devel

%description
Expect is a tool primarily for automating interactive applications,
such as telnet, ftp, passwd, fsck, rlogin, tip, and more.  Expect
really makes this stuff trivial.  Expect is also useful for testing
these applications.  It is described in many books, articles, papers,
and FAQs.  There is an entire book on it available from O'Reilly.

%package devel
Summary:        Header Files and C API Documentation for expect
Group:          Development/Libraries/Tcl

%description devel
This package contains header files and documentation needed for linking
to expect from programs written in compiled languages like C, C++, etc.

This package is not needed for developing scripts that run under the
/usr/bin/expect interpreter, or any other Tcl interpreter with the
expect package loaded.

%prep
%setup -q -n %name%version
%patch1
%patch2
%patch3
%patch4

%build
autoreconf
%configure \
	--with-tcl=%_libdir \
	--with-tk=no_tk \
	--with-tclinclude=%_includedir \
	--enable-shared
make %{?_smp_mflags} all pkglibdir=%_libdir/tcl/%name%version

%check
make %{?_smp_mflags} test

%install
# set the right path to the expect binary...
sed -i \
    -e '1s,^#![^ ]*expectk,#!%_bindir/wish\npackage require Expect,' \
    -e '1s,^#![^ ]*expect,#!%_bindir/expect,' \
    example/*
%make_install pkglibdir=%_libdir/tcl/%name%version
# Remove some executables and manpages we don't want to ship
rm %buildroot%_bindir/*passwd
rm %buildroot%_bindir/weather
rm %buildroot%_mandir/*/*passwd*
# Simplify linking for apps that use Expect without Tcl
ln -s libexpect%version.so %buildroot%_libdir/libexpect.so

%files
%_bindir/*
%_libdir/tcl/*
%_libdir/lib*.so
%_mandir/man1/*
%doc ChangeLog HISTORY INSTALL FAQ NEWS README

%files devel
%_libdir/libexpect.so
%_includedir/*
%_mandir/man3/*

%changelog
