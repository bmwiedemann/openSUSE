#
# spec file for package afl
#
# Copyright (c) 2021 SUSE LLC
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


Name:           afl
Version:        3.12c
Release:        0
Summary:        American fuzzy lop is a security-oriented fuzzer
License:        Apache-2.0
URL:            http://lcamtuf.coredump.cx/afl/
Source:         https://github.com/AFLplusplus/AFLplusplus/archive/%{version}.tar.gz
Source1:        afl-rpmlintrc
Patch1:         afl-3.0c-fix-paths.patch
BuildRequires:  clang
BuildRequires:  gcc-c++
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
%ifarch x86_64 aarch64 ppc64 ppc64le s390x
%{_libexecdir}/%{name}/afl-compiler-rt-64.o
%{_libexecdir}/%{name}/afl-llvm-rt-64.o
%{_libexecdir}/%{name}/afl-llvm-rt-lto-64.o
%endif
%ifarch %ix86 %{arm}
%{_libexecdir}/%{name}/afl-compiler-rt-32.o
%{_libexecdir}/%{name}/afl-llvm-rt-32.o
%endif
%ifarch %ix86 aarch64
%{_libexecdir}/%{name}/afl-llvm-rt-lto-32.o
%endif
%{_libexecdir}/%{name}/afl-compiler-rt.o
%{_libexecdir}/%{name}/afl-llvm-rt.o
%ifnarch %{arm}
%{_libexecdir}/%{name}/afl-llvm-rt-lto.o
%endif
%{_libexecdir}/%{name}/dynamic_list.txt
%{_libexecdir}/%{name}/*.so
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/testcases
%{_datadir}/%{name}/testcases/*
%dir %{_datadir}/afl/dictionaries/
%{_datadir}/afl/dictionaries/*
%{_mandir}/man8/afl*.8*

%changelog
