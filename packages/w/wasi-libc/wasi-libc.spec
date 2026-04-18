#
# spec file for package wasi-libc
#
# Copyright (c) 2026 SUSE LLC and contributors
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
Version:        31
Release:        0
Summary:        WASI libc implementation for WebAssembly
# FIXME: Select a correct license from https://github.com/openSUSE/spec-cleaner#spdx-licenses
License:        MIT
URL:            https://github.com/WebAssembly/wasi-libc
Source:         https://github.com/WebAssembly/wasi-libc/archive/refs/tags/wasi-sdk-%{version}.tar.gz#/%{name}-%{version}.tar.gz
# FIXME: This should come from LLVM.
Source1:        https://github.com/WebAssembly/wasi-sdk/releases/download/wasi-sdk-25/libclang_rt.builtins-wasm32-wasi-25.0.tar.gz
Source100:      wasi-libc-rpmlintrc
# Build uses LLVM option -wasm-enable-sjlj, which was introduced in LLVM 14.
# (https://github.com/llvm/llvm-project/commit/77b921b870aacfd531ff449166937e0de6a377bc)
BuildRequires:  clang >= 14
BuildRequires:  cmake >= 3.26
BuildRequires:  lld
BuildRequires:  llvm >= 14
BuildArch:      noarch

%description
WASI libc allows cross platform binaries to be created and executed on a variety of platforms

%prep
%autosetup -p1 -n wasi-libc-wasi-sdk-%{version} -a1

%build
# Building libsetjmp.so fails with LTO:
# wasm-ld: error: symbol type mismatch: __c_longjmp
# >>> defined as WASM_SYMBOL_TYPE_FUNCTION in CMakeFiles/setjmp.dir/musl/src/setjmp/wasm32/rt.c.obj
# >>> defined as WASM_SYMBOL_TYPE_TAG in CMakeFiles/setjmp.dir/musl/src/setjmp/wasm32/libsetjmp.so.lto.rt.c.o
%global _lto_cflags %{nil}

# Removing all default compiler and linker flags and turning off linker dependency
# generation is necessary because they don't generally make sense for WebAssembly.
# Most of them don't work or are ignored, the remainder is added by CMake (-O2 -g).
%cmake \
    -DCMAKE_C_COMPILER=clang \
    -DCMAKE_C_FLAGS="" \
    -DCMAKE_SHARED_LINKER_FLAGS="" \
    -DCMAKE_LINK_DEPENDS_USE_LINKER:BOOL=OFF \
    -DCMAKE_INSTALL_PREFIX:PATH=%{_datadir}/wasi-sysroot \
    -DBUILTINS_LIB=%{_builddir}/%{buildsubdir}/libclang_rt.builtins-wasm32-wasi-25.0/libclang_rt.builtins-wasm32.a
%cmake_build

%install
%cmake_install
# brp-15-strip-debug and -ar call system-strip and ar, which are not wasm-aware, so they will break wasm-files
export NO_BRP_AR=true
export NO_BRP_STRIP_DEBUG=true

%files
%license LICENSE
%{_datadir}/wasi-sysroot/

%changelog
