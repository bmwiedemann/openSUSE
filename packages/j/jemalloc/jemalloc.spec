#
# spec file for package jemalloc
#
# Copyright (c) 2022 SUSE LLC
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


%define lname	libjemalloc2
Name:           jemalloc
Version:        5.3.0
Release:        0
Summary:        General-purpose scalable concurrent malloc implementation
License:        BSD-2-Clause
Group:          Development/Libraries/C and C++
URL:            http://jemalloc.net/
Source:         https://github.com/jemalloc/jemalloc/releases/download/%version/jemalloc-%version.tar.bz2
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  libxslt
BuildRequires:  pkgconfig
Requires:       %lname = %version

%description
jemalloc is a general-purpose scalable concurrent malloc(3) implementation.
This package provides a shell wrapper script to run programs using jemalloc.

%package -n %lname
Summary:        General-purpose scalable concurrent malloc implementation
Group:          System/Libraries

%description -n %lname
General-purpose scalable concurrent malloc(3) implementation.
This distribution is the stand-alone "portable" version of jemalloc.

%package devel
Summary:        Development files for jemalloc
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
Headers for jemalloc, general-purpose scalable concurrent malloc(3)
implementation.

%prep
%autosetup -p1

%build
export EXTRA_CFLAGS="%optflags -std=gnu99"
# AArch64: Set lg-page to 2^16 to be compatible with 64k kernels - https://github.com/jemalloc/jemalloc/pull/769
%configure --disable-static --enable-prof \
%ifarch aarch64
  --with-lg-page=16 \
%endif
%ifarch %arm
  --disable-thp
%endif

%make_build

%install
b=%buildroot
%make_install
if [ "%_docdir" != "%_datadir/doc" ]; then
	# Makefile apparently ignored the --docdir in %%configure
	mkdir -p "$b/%_docdir"
	mv "$b/%_datadir/doc/jemalloc" "$b/%_docdir/%name"
fi

%check
export LD_LIBRARY_PATH="$PWD/lib:$LD_LIBRARY_PATH"
%make_build check

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files
%_bindir/jemalloc.sh
%_bindir/jemalloc-config
%_bindir/jeprof
%_mandir/man*/*
%_docdir/%name

%files -n %lname
%license COPYING
%doc ChangeLog README
%_libdir/libjemalloc.so.2*

%files devel
%_includedir/jemalloc
%_libdir/libjemalloc.so
%_libdir/pkgconfig/jemalloc.pc

%changelog
