#
# spec file for package vdt
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


%define shlib lib%{name}0
Name:           vdt
Version:        0.4.4
Release:        0
Summary:        A collection of fast and inline implementations of mathematical functions
License:        LGPL-3.0-or-later
URL:            https://github.com/dpiparo/vdt
Source:         %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM vdt-shared-lib-versioning.patch badshah400@gmail.com -- Implement proper so versioning
Patch0:         vdt-shared-lib-versioning.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  python3-base

%description
VDT is a collection of fast and inline implementations of mathematical
functions that can be used in autovectorised loops.

%package -n %{shlib}
Summary:        Shared library for vdt

%description -n %{shlib}
This package provides the shared library for vdt.

%package devel
Requires:       %{shlib} = %{version}
Summary:        Headers and sources for building against vdt

%description devel
This package provides the headers and sources for developing applications
against vdt.

%prep
%autosetup -p1

%build
# Note: Neon is implicitly enabled on aarch64
%cmake \
  -DDIAG:BOOL=ON \
  -DAVX:BOOL=OFF \
%ifnarch x86_64
  -DSSE:BOOL=OFF \
%else
  -DSSE:BOOL=ON \
%endif
%{nil}

%cmake_build

%install
%cmake_install

%check
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}

for x in `ls -1 bin/* | grep -v "vdt*"`
do
  ./${x} > /dev/null
done
./bin/vdtArithmBenchmark -n=test > /dev/null
# Get list of benchmark files generated from prev test
testfiles=`ls -w0 -m *test*.txt | sed -E "s/,\s/,/g"`
./bin/vdtArithmComparison -n=test -R=${testfiles} -T=${testfiles} > /dev/null
./bin/vdtPerfBenchmark -n=test > /dev/null

%post   -n %{shlib} -p /sbin/ldconfig
%postun -n %{shlib} -p /sbin/ldconfig

%files -n %{shlib}
%license Licence.txt
%{_libdir}/*.so.*

%files devel
%license Licence.txt
%doc ReadMe.md ReleaseNotes.txt
%{_libdir}/*.so
%{_includedir}/%{name}/

%changelog
