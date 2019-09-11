#
# spec file for package ck
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define sover   0
%define libname libck%{sover}
Name:           ck
Version:        0.6.0
Release:        0
Summary:        Concurrency Kit
License:        BSD-2-Clause AND Apache-2.0
Group:          Development/Libraries/C and C++
URL:            http://concurrencykit.org/
Source:         http://concurrencykit.org/releases/ck-%{version}.tar.gz
# PATCH-FIX-UPSTREAM https://github.com/concurrencykit/ck/issues/141
Patch0:         ck-fix-j1.patch
BuildRequires:  pkgconfig
ExcludeArch:    s390 s390x

%description
Concurrency primitives, safe memory reclamation mechanisms and non-blocking
data structures for the research, design and implementation of high performance
concurrent systems.

%package -n %{libname}
Summary:        Shared library for Concurrency Kit
Group:          System/Libraries

%description -n %{libname}
Concurrency primitives, safe memory reclamation mechanisms and non-blocking
data structures for the research, design and implementation of high performance
concurrent systems.

This package holds the shared library.

%package devel
Summary:        Development files for Concurrency Kit
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description devel
Concurrency primitives, safe memory reclamation mechanisms and non-blocking
data structures for the research, design and implementation of high performance
concurrent systems.

This package holds the development files.

%prep
%setup -q
%patch0 -p1

%build
# not a normal autotool configure, can't use configure macro
export CFLAGS="%{optflags}"
# not autotools configure
./configure                       \
  --includedir=%{_includedir}/ck/ \
  --libdir=%{_libdir}             \
  --mandir=%{_mandir}             \
  --prefix=%{_prefix}             \
  --cores=%jobs

# The following options will affect generated code.
#  --enable-pointer-packing Assumes address encoding is subset of pointer range
#  --enable-rtm             Enable restricted transactional memory (power, x86_64)
#  --enable-lse             Enable large system extensions (arm64)
#  --memory-model=N         Specify memory model (currently tso, pso or rmo)
#  --vma-bits=N             Specify valid number of VMA bits
#  --platform=N             Force the platform type, instead of relying on autodetection
#  --use-cc-builtins        Use the compiler atomic bultin functions, instead of the CK implementation
#  --disable-double         Don't generate any of the functions using the "double" type
# The following options affect regression testing.
#   --cores=N                Specify number of cores available on target machine

%make_build

%install
%make_install
rm -rv %{buildroot}%{_libdir}/libck.a

%check
make %{?_smp_mflags} check

%post   -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%license LICENSE
%{_libdir}/libck.so.%{sover}*

%files devel
%{_mandir}/man3/ck*
%{_mandir}/man3/CK*
%{_libdir}/libck.so
%{_includedir}/ck/
%{_libdir}/pkgconfig/ck.pc

%changelog
