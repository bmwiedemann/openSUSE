#
# spec file for package rr
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


Name:           rr
Version:        5.6.0
Release:        0
Summary:        Records nondeterministic executions and debugs them deterministically
License:        MIT
Group:          Development/Languages/C and C++
URL:            https://rr-project.org/
Source:         https://github.com/mozilla/%{name}/archive/%{version}.tar.gz
Patch0:         https://github.com/rr-debugger/rr/commit/2979c60e.patch
BuildRequires:  capnproto
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gdb
BuildRequires:  libcapnp-devel
BuildRequires:  patchelf
BuildRequires:  pkgconfig
BuildRequires:  python3-base
BuildRequires:  python3-pexpect
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(zlib)
ExclusiveArch:  x86_64 aarch64
%ifarch x86_64
BuildRequires:  gcc-c++-32bit
%endif

%description
This program aspires to be your primary debugging tool, enhancing gdb. It
also provides efficient reverse execution under gdb. Set breakpoints and
data watchpoints and quickly reverse-execute to where they were hit.

%prep
%autosetup -p1

%build
# Fix incorrect path to bash
sed -i "s|%{_bindir}/bash|/bin/bash|g" ./scripts/signal-rr-recording.sh
sed -i "s|#!.*%{_bindir}/env.*|#!%{_bindir}/python3|" scripts/rr-collect-symbols.py
%cmake \
  -DBUILD_TESTS=OFF \
%ifarch aarch64
  -Ddisable32bit=true \
%endif
  -DCMAKE_BUILD_TYPE=Release \
  -DCMAKE_CXX_STANDARD=14
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc README.md
%dir %{_datadir}/rr
%dir %{_libdir}/rr
%{_bindir}/rr
%{_bindir}/rr_exec_stub*
%{_bindir}/signal-rr-recording.sh
%{_bindir}/rr-collect-symbols.py
%{_libdir}/rr/librrpreload*.so
%ifarch x86_64
%{_libdir}/rr/librraudit_32.so
%{_libdir}/rr/librrpage_32.so
%endif
%{_libdir}/rr/librraudit.so
%{_libdir}/rr/librrpage.so
%{_datadir}/rr/*
%{_datadir}/bash-completion/completions/rr

%changelog
