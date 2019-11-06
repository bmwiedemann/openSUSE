#
# spec file for package afl
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


Name:           afl
Version:        2.52c
Release:        0
Summary:        American fuzzy lop is a security-oriented fuzzer
License:        Apache-2.0
Url:            http://lcamtuf.coredump.cx/afl/
Source:         https://github.com/vanhauser-thc/AFLplusplus/archive/%{version}.tar.gz
Source1:        afl-rpmlintrc
Patch1:         afl-1.58b-fix-paths.patch
BuildRequires:  gcc-c++

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
sed -i 's|#!/usr/bin/env bash|#!/bin/bash|g' afl-cmin

%build
export CFLAGS="$CFLAGS %{optflags}"
%ifnarch %{ix86} x86_64
export AFL_NO_X86=1
%endif
make %{?_smp_mflags} PREFIX=%{_prefix} LIBEXEC_DIR=%{_libexecdir} DOC_DIR=%{_docdir}

%install
%ifnarch %{ix86} x86_64
export AFL_NO_X86=1
%endif
make %{?_smp_mflags} PREFIX=%{_prefix} LIBEXEC_DIR=%{_libexecdir} DOC_DIR=%{_docdir} DESTDIR=%{buildroot} install

%files
%doc docs/ChangeLog docs/COPYING docs/README docs/*.txt
%{_bindir}/%{name}-*
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/%{name}-as
%{_libexecdir}/%{name}/as
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/testcases
%{_datadir}/%{name}/testcases/*
%dir %{_datadir}/afl/dictionaries/
%{_datadir}/afl/dictionaries/*

%changelog
