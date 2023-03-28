#
# spec file for package wasi-libc
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


Name:           wasi-libc
Version:        19
Release:        0
Summary:        WASI libc implementation for WebAssembly
# FIXME: Select a correct license from https://github.com/openSUSE/spec-cleaner#spdx-licenses
License:        MIT
URL:            https://github.com/WebAssembly/wasi-libc
Source:         https://github.com/WebAssembly/wasi-libc/archive/refs/tags/wasi-sdk-%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        wasi-libc-rpmlintrc
Patch1:         workaround-broken-makefile.patch
Patch2:         undefine-gcc-macros.patch
BuildRequires:  clang > 10
BuildRequires:  llvm > 10
BuildArch:      noarch

%description
WASI libc allows cross platform binaries to be created and executed on a variety of platforms

%prep
%setup -q -n wasi-libc-wasi-sdk-%{version}
%patch1 -p1
%patch2 -p1

%build
export CC=clang
export AR=llvm-ar
export NM=llvm-nm
%make_build

%install
export CC=clang
export AR=llvm-ar
export NM=llvm-nm
# The makefile is stupid and compiles everything again if we do `make install`, so we
# do it only once
%make_install INSTALL_DIR="%{buildroot}/%{_datadir}/wasi-sysroot"
# brp-15-strip-debug and -ar call system-strip and ar, which are not wasm-aware, so they will break wasm-files
export NO_BRP_AR=true
export NO_BRP_STRIP_DEBUG=true

%files
%license LICENSE
%{_datadir}/wasi-sysroot/

%changelog
