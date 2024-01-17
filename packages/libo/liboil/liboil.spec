#
# spec file for package liboil
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


Name:           liboil
Version:        0.3.17
Release:        0
Summary:        Library of Optimized Inner Loops
License:        BSD-2-Clause
Group:          Development/Libraries/C and C++
URL:            http://liboil.freedesktop.org/wiki/
Source0:        http://liboil.freedesktop.org/download/%{name}-%{version}.tar.gz
Source1:        baselibs.conf
Patch0:         ppc-asm.patch
#PATCH-FIX-OPENSUSE bmwiedemann -- make build reproducible
Patch1:         reproducible.patch
Patch2:         s390-asm.patch
BuildRequires:  glib2-devel
BuildRequires:  gtk-doc

%description
Liboil is a library of functions that are optimized for various
CPUs. These functions are generally loops implementing
algorithms, such as converting an array of N integers to floating-point
numbers or multiplying and summing an array of N numbers. Such
functions are candidates for significant optimization using various
techniques, especially by using extended instructions provided by
modern CPUs (Altivec, MMX, SSE, etc.).

%package -n liboil-0_3-0
Summary:        Library of Optimized Inner Loops
Group:          System/Libraries
Obsoletes:      liboil < %{version}-%{release}

%description -n liboil-0_3-0
Liboil is a library of functions that are optimized for various
CPUs. These functions are generally loops implementing
algorithms, such as converting an array of N integers to floating-point
numbers or multiplying and summing an array of N numbers. Such
functions are candidates for significant optimization using various
techniques, especially by using extended instructions provided by
modern CPUs (Altivec, MMX, SSE, etc.).

%package devel
Summary:        Headers for the library of Optimized Inner Loops
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       liboil-0_3-0 = %{version}-%{release}

%description devel
Liboil is a library of functions that are optimized for various
CPUs.

%package doc
Summary:        Documentation for the library of Optimized Inner Loops
Group:          Documentation/HTML
BuildArch:      noarch

%description doc
This package provides documentation for liboil, a library of
functions that are optimized for various CPUs.

%prep
%autosetup -p1

%build
%define _lto_cflags %{nil}
%configure --disable-static
%make_build
# Do NOT! disable running the testsuite or make failures
# non-fatal for the build!

%check
# Several tests are failing only under Power KVM
# Test passed during the local build. The test for ppc64 will be
# reenabled once we'll have solution for it.
%ifnarch %{power64}
%make_build check
%endif

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post   -n liboil-0_3-0 -p /sbin/ldconfig
%postun -n liboil-0_3-0 -p /sbin/ldconfig

%files -n liboil-0_3-0
%doc AUTHORS NEWS README
%{_libdir}/*.so.*

%files devel
%{_bindir}/oil-bugreport
%{_includedir}/liboil-*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%files doc
%{_datadir}/gtk-doc/html/liboil

%changelog
