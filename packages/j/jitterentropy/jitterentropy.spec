#
# spec file for package jitterentropy
#
# Copyright (c) 2023 SUSE LLC
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


Name:           jitterentropy
Summary:        A userspace library for jitter entropy generation
License:        BSD-3-Clause OR GPL-2.0-or-later
Group:          Development/Tools/Other
Version:        3.4.1
Release:        0
URL:            https://github.com/smuellerDD/jitterentropy-library
Source0:        https://github.com/smuellerDD/jitterentropy-library/archive/refs/tags/v%{version}.tar.gz
Source1:        baselibs.conf
#PATCH-FIX-UPSTREAM github.com/smuellerDD/jitterentropy-library/commit/7bf9f85
Patch0:         jitterentropy-fix-a-stack-corruption-on-s390x.patch

%description
The Jitter RNG provides a noise source using the CPU execution
timing jitter. It depends on a high-resolution time stamp.

The design of this RNG is given in the documentation found at
http://www.chronox.de/jent.html . This documentation also covers the full
assessment of the SP800-90B compliance as well as all required test code.

%package -n libjitterentropy3
Summary:        Jitter entropy generator shared library
Group:          System/Libraries

%description -n libjitterentropy3
The Jitter RNG provides a noise source using the CPU execution
timing jitter. It depends on a high-resolution time stamp.

This package contains the shared library.

%package devel
Summary:        Jitter entropy generator development header and library
Group:          Development/Tools/Other
Requires:       libjitterentropy3 = %{version}

%description devel
The Jitter RNG provides a noise source using the CPU execution
timing jitter. It depends on a high-resolution time stamp.

This package contains the development header and library.

%package devel-static
Summary:        Jitter entropy generator static library
Group:          Development/Tools/Other

%description devel-static
The Jitter RNG provides a noise source using the CPU execution
timing jitter. It depends on a high-resolution time stamp.

This package contains the static library.

%prep
%autosetup -n jitterentropy-library-%version

%build
%make_build PREFIX="%_prefix" LIBDIR="%_lib"

%install
%make_install PREFIX="%_prefix" LIBDIR="%_lib" all install-static

%post -n libjitterentropy3 -p /sbin/ldconfig
%postun -n libjitterentropy3 -p /sbin/ldconfig

%files devel
%license LICENSE.gplv2 LICENSE LICENSE.bsd
%_includedir/jitterentropy-base-user.h
%_includedir/jitterentropy.h
%_libdir/libjitterentropy.so
%_mandir/man3/jitterentropy.3*

%files devel-static
%license LICENSE.gplv2 LICENSE LICENSE.bsd
%_libdir/libjitterentropy.a

%files -n libjitterentropy3
%license LICENSE.gplv2 LICENSE LICENSE.bsd
%_libdir/libjitterentropy.so.3
%_libdir/libjitterentropy.so.%version

%changelog
