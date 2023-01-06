#
# spec file for package afl
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


%define afl_rt compiler-rt,llvm-rt,llvm-rt-lto

%ifarch %{arm} %ix86 s390x x86_64
%define afl_32 1
%endif
%ifarch ppc64le
%if %{pkg_vcmp clang < 12}
%define afl_32 1
%endif
%endif

%ifarch aarch64 ppc64 ppc64le riscv64 s390x x86_64
%define afl_64 1
%endif

Name:           afl
Version:        4.05c
Release:        0
Summary:        American fuzzy lop is a security-oriented fuzzer
#URL:            https://lcamtuf.coredump.cx/afl/
License:        Apache-2.0
URL:            https://github.com/AFLplusplus/AFLplusplus
Source:         https://github.com/AFLplusplus/AFLplusplus/archive/%{version}.tar.gz
Source1:        afl-rpmlintrc
Patch1:         afl-3.0c-fix-paths.patch
BuildRequires:  clang
BuildRequires:  gcc-c++
%ifarch x86_64
BuildRequires:  gcc-32bit
%endif
%if %?suse_version >= 1550
BuildRequires:  gcc-devel
%endif
BuildRequires:  lld
BuildRequires:  llvm-devel >= 11.0.0
BuildRequires:  python3-devel
Requires:       lld

%description
American fuzzy lop is a security-oriented fuzzer that employs a novel type
of compile-time instrumentation and genetic algorithms to automatically
discover clean, interesting test cases that trigger new internal states in
the targeted binary. This substantially improves the functional coverage
for the fuzzed code. The compact synthesized corpora produced by the tool
are also useful for seeding other, more labor- or resource-intensive
testing regimes down the road.

Compared to other instrumented fuzzers, afl-fuzz is designed to be
practical: it has modest performance overhead, uses a variety of highly
effective fuzzing strategies and effort minimization tricks, requires
essentially no configuration, and seamlessly handles complex, real-world
use cases - say, common image parsing or file compression libraries.

%prep
%setup -q -n AFLplusplus-%version
%patch1 -p1
sed -i 's|#!/usr/bin/env sh|#!/bin/sh|g' afl-cmin
sed -i 's|#!/usr/bin/env bash|#!/bin/bash|g' afl-cmin.bash

%build
export CFLAGS="$CFLAGS %{optflags} -fno-lto"
%ifnarch %{ix86} x86_64
export AFL_NO_X86=1
%endif
make %{?_smp_mflags} PREFIX=%{_prefix} LIBEXEC_DIR=%{_libexecdir} DOC_DIR=%{_docdir}
# make radamsa

%install
%ifnarch %{ix86} x86_64
export AFL_NO_X86=1
%endif
make %{?_smp_mflags} PREFIX=%{_prefix} LIBEXEC_DIR=%{_libexecdir} DOC_DIR=%{_docdir} MAN_PATH=%{_mandir}/man8 DESTDIR=%{buildroot} install
chmod -x %{buildroot}/%{_libexecdir}/%{name}/*.o

%files
%license docs/COPYING LICENSE
%doc /usr/share/doc/packages/%name/
%{_bindir}/%{name}-*
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/%{name}-as
%{_libexecdir}/%{name}/as
%if 0%{?afl_64}
%{_libexecdir}/%{name}/afl-{%{afl_rt}}-64.o
%endif
%if 0%{?afl_32}
%{_libexecdir}/%{name}/afl-{%{afl_rt}}-32.o
%endif
%ifarch aarch64
%{_libexecdir}/%{name}/afl-llvm-rt-lto-32.o
%endif
%{_libexecdir}/%{name}/afl-{%{afl_rt}}.o
%{_libexecdir}/%{name}/dynamic_list.txt
%{_libexecdir}/%{name}/*.so
%{_libexecdir}/%{name}/*.a
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/testcases
%{_datadir}/%{name}/testcases/*
%dir %{_datadir}/afl/dictionaries/
%{_datadir}/afl/dictionaries/*
%{_mandir}/man8/afl*.8*

%changelog
