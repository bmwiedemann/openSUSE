#
# spec file for package judy
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


%define libname libJudy1
Name:           judy
Version:        1.0.5
Release:        0
Summary:        A general purpose dynamic array implemented as a C callable library
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            http://judy.sourceforge.net/
Source0:        http://sourceforge.net/projects/judy/files/judy/Judy-%{version}/Judy-%{version}.tar.gz
# PATCH-FIX-OPENSUSE Judy-test-shared.patch -- use shared library for testing
Patch0:         Judy-test-shared.patch
Patch1:         reproducible.patch
BuildRequires:  fdupes

%description
Judy is a C library that provides a state-of-the-art core technology that implements
a sparse dynamic array. Judy arrays are declared simply with a null pointer. A Judy
array consumes memory only when it is populated, yet can grow to take advantage
of all available memory if desired.

Judy's key benefits are scalability, high performance, and memory efficiency. A Judy
array is extensible and can scale up to a very large number of elements, bounded
only by machine memory. Since Judy is designed as an unbounded array, the size of
a Judy array is not pre-allocated but grows and shrinks dynamically
with the array population.

%package -n %{libname}
Summary:        Dynamic libraries for Judy
Group:          Development/Libraries/C and C++

%description -n %{libname}
Judy is a C library that provides a state-of-the-art core technology that implements
a sparse dynamic array. Judy arrays are declared simply with a null pointer. A Judy
array consumes memory only when it is populated, yet can grow to take advantage
of all available memory if desired.

Judy's key benefits are scalability, high performance, and memory efficiency. A Judy
array is extensible and can scale up to a very large number of elements, bounded
only by machine memory. Since Judy is designed as an unbounded array, the size of
a Judy array is not pre-allocated but grows and shrinks dynamically
with the array population.

%package devel
Summary:        Development files for Judy
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}
Recommends:     %{name}-doc

%description devel
This package holds the development files for Judy.

%package doc
Summary:        Development files for Judy
Group:          Documentation/Other
BuildArch:      noarch

%description doc
This package contains documentation about Judy library and examples.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%configure \
	--disable-static
# not parallel safe
%make_build -j1

%check
%make_build check

%install
%make_install

find %{buildroot} -type f -name "*.la" -delete -print

%fdupes -s %{buildroot}/%{_mandir}

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files devel
%{_includedir}/Judy.h
%{_libdir}/libJudy.so
%{_mandir}/man3/J*

%files -n %{libname}
%{_libdir}/libJudy.so.1*

%files doc
%license COPYING
%doc AUTHORS ChangeLog doc/ext/README_deliver doc/ext/*.htm* doc/int/*.htm*
%doc examples

%changelog
