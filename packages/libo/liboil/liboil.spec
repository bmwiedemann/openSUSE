#
# spec file for package liboil
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           liboil
Version:        0.3.17
Release:        0
Summary:        Library of Optimized Inner Loops
License:        BSD-2-Clause
Group:          System/Libraries
Url:            http://liboil.freedesktop.org/wiki/
Source0:        http://liboil.freedesktop.org/download/%{name}-%{version}.tar.gz
Source1:        baselibs.conf
Patch0:         ppc-asm.patch
#PATCH-FIX-OPENSUSE bmwiedemann -- make build reproducible
Patch1:         reproducible.patch
Patch2:         s390-asm.patch
BuildRequires:  glib2-devel
BuildRequires:  gtk-doc
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Liboil is a library of simple functions that are optimized for various
CPUs. These functions are generally loops implementing simple
algorithms, such as converting an array of N integers to floating-point
numbers or multiplying and summing an array of N numbers. Such
functions are candidates for significant optimization using various
techniques, especially by using extended instructions provided by
modern CPUs (Altivec, MMX, SSE, etc.).

Many multimedia applications and libraries already do similar things
internally. The goal of this project is to consolidate some of the code
used by various multimedia projects and also make optimizations easier
to use by a broader range of applications.

%package devel
Summary:        Library of Optimized Inner Loops
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       glibc-devel

%description devel
Liboil is a library of simple functions that are optimized for various
CPUs. These functions are generally loops implementing simple
algorithms, such as converting an array of N integers to floating-point
numbers or multiplying and summing an array of N numbers. Such
functions are candidates for significant optimization using various
techniques, especially by using extended instructions provided by
modern CPUs (Altivec, MMX, SSE, etc.).

Many multimedia applications and libraries already do similar things
internally. The goal of this project is to consolidate some of the code
used by various multimedia projects, and also make optimizations easier
to use by a broader range of applications.

%package doc
Summary:        Library of optimized inner loops
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

%description doc
This package provides documentation for liboil, a library of simple
functions that are optimized for various CPUs. These functions are
generally loops implementing simple algorithms, such as converting an
array of N integers to floating-point numbers or multiplying and
summing an array of N numbers. Such functions are candidates for
significant optimization using various techniques, especially by using
extended instructions provided by modern CPUs (Altivec, MMX, SSE,
etc.).

Many multimedia applications and libraries already do similar things
internally. The goal of this project is to consolidate some of the code
used by various multimedia projects, and also make optimizations easier
to use by a broader range of applications.

%prep
%setup -q
%patch0
%patch1 -p1
%patch2 -p1

%build
%define _lto_cflags %{nil}
%configure --disable-static --with-pic
make %{?_smp_mflags}
# Do NOT! disable running the testsuite or make failures
# non-fatal for the build!

%check
# Several tests are failing only under Power KVM
# Test passed during the local build. The test for ppc64 will be
# reenabled once we'll have solution for it.
%ifnarch %{power64}
make %{?_smp_mflags} check
%endif

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
find %{buildroot} -type f -name "*.la" -delete -print

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr (-, root, root)
%doc AUTHORS NEWS README
%{_libdir}/*.so.*

%files devel
%defattr (-, root, root)
%{_bindir}/oil-bugreport
%{_includedir}/liboil-*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%files doc
%defattr (-, root, root)
%{_datadir}/gtk-doc/html/liboil

%changelog
