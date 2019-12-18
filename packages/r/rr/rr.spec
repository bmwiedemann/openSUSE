#
# spec file for package rr
#
# Copyright (c) 2019 SUSE LLC
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


Name:           rr
Version:        5.2.0
Release:        0
Summary:        Records nondeterministic executions and debugs them deterministically
License:        MIT
Group:          Development/Languages/C and C++
URL:            https://rr-project.org/
Source:         https://github.com/mozilla/%{name}/archive/%{version}.tar.gz
# https://github.com/mozilla/rr/issues/2391
Patch0:         rr-5.2.0-remove-ucontext.patch
# https://github.com/mozilla/rr/issues/2269
Patch1:         rr-5.2.0-cpp14.patch
# https://github.com/mozilla/rr/issues/2390
Patch2:         rr-5.2.0-python3.patch
BuildRequires:  capnproto
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gdb
BuildRequires:  libcapnp-devel
BuildRequires:  pkgconfig
BuildRequires:  python3-base
BuildRequires:  python3-pexpect
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(zlib)
ExclusiveArch:  x86_64 %{ix86}
%ifarch x86_64
BuildRequires:  gcc-c++-32bit
%endif

%description
This program aspires to be your primary debugging tool, enhancing gdb. It
also provides efficient reverse execution under gdb. Set breakpoints and
data watchpoints and quickly reverse-execute to where they were hit.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
# Fix incorrect path to bash
sed -i "s|%{_bindir}/bash|/bin/bash|g" ./scripts/signal-rr-recording.sh
CXXFLAGS=-std=c++14 %cmake \
  -DBUILD_TESTS=OFF
CXXFLAGS=-std=c++14 %make_jobs

%install
%cmake_install

%files
%license LICENSE
%doc README.md
%dir %{_prefix}/lib/rr
%dir %{_datadir}/rr
%{_bindir}/rr
%{_bindir}/rr_exec_stub*
%{_bindir}/rr_page_32
%{_bindir}/rr_page_32_replay
%{_bindir}/rr_page_64
%{_bindir}/rr_page_64_replay
%{_bindir}/signal-rr-recording.sh
%{_prefix}/lib/rr/librrpreload*.so
%{_datadir}/rr/*

%changelog
