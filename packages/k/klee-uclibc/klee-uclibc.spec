#
# spec file for package klee-uclibc
#
# Copyright (c) 2025 SUSE LLC
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


%define llvm_version 14

Name:           klee-uclibc
Summary:        Libc library for Klee
License:        LGPL-2.1-or-later
Group:          Development/Languages/Other
Version:        1.4+git.20240531
Release:        0
URL:            https://github.com/klee/klee-uclibc
Source0:        %{name}-%{version}.tar.xz
Source1:        %{name}-rpmlintrc
Patch1:         proper-compiler-flags-check.patch
Patch2:         0001-strtod-fix-__strtofpmax.patch
BuildRequires:  clang%{llvm_version}
BuildRequires:  llvm%{llvm_version}-devel
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  python3-base
ExclusiveArch:  x86_64

%description
This is a port of uClibc to LLVM to serve Klee. Hence, this package
provides a "static" library, but it is not composed of ELF objects, but is
LLVM bytecode packed by `ar`. Klee uses this to emulate the POSIX runtime
development symbolically.

%package devel-static
Summary:        Libc library for Klee
Group:          Development/Languages/Other
Provides:       %{name}-devel-static(llvm%{llvm_version})

%description devel-static
This is a port of uClibc to LLVM to serve Klee. Hence, this package
provides a "static" library, but it is not composed of ELF objects, but is
LLVM bytecode packed by `ar`. Klee uses this to emulate the POSIX runtime
development symbolically.

%prep
%autosetup -p1

%build
./configure \
	--make-llvm-lib
# README.md says: "Warning things might break if you do this." about this:
	#--enable-release
%make_build KLEE_CFLAGS=-g lib/libc.a

%install
install -d %{buildroot}%{_libdir}/%{name}/lib/
install -m 0644 lib/libc.a %{buildroot}%{_libdir}/%{name}/lib/

%files devel-static
%doc README README.md TODO
%license COPYING.LIB
%dir %{_libdir}/%{name}/
%dir %{_libdir}/%{name}/lib/
%{_libdir}/%{name}/lib/libc.a

%changelog
