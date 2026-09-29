#
# spec file for package binaryen
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


Name:           binaryen
Version:        133
Release:        0
Summary:        Compiler infrastructure and toolchain library for WebAssembly
# Legal-Review-Notice: code compiled in besides upstream's Apache-2.0:
# - third_party/llvm-project (DWARF support, BUILD_LLVM_DWARF is ON by
#   default) and src/support/suffix_tree*.cpp (always built) are
#   Apache-2.0 WITH LLVM-exception; llvm-project's MD5.cpp is
#   bcrypt-Solar-Designer and its ConvertUTF.cpp carries the
#   Unicode-DFS-2015 notice. The bundled include/llvm/LICENSE.TXT keeps
#   the legacy University of Illinois/NCSA licence for pre-relicensing
#   LLVM code, and the compiled Support sources fall under it: NCSA.
# - The header-only third_party/FP16 is MIT.
# - The other third_party trees are empty submodules or unused by the
#   build (wabt/wasm2c only serves the fuzzer scripts), and
#   BUILD_MIMALLOC defaults to OFF.
License:        Apache-2.0 AND Apache-2.0 WITH LLVM-exception AND MIT AND NCSA AND Unicode-DFS-2015 AND bcrypt-Solar-Designer
URL:            https://github.com/WebAssembly/binaryen
Source:         https://github.com/WebAssembly/binaryen/archive/version_%{version}.tar.gz#/%{name}-version_%{version}.tar.gz
BuildRequires:  cmake >= 3.16.3
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
Requires:       lib%{name} = %{version}

%description
Binaryen is a compiler and toolchain infrastructure library for WebAssembly,
written in C++, for compiling WebAssembly.

* Binaryen has a single header C API. It accepts input in WebAssembly-like form,
  but also accepts a general control flow graph for compilers that prefer that.
* Binaryen's internal IR uses compact data structures and is designed for
  completely parallel codegen and optimization, using all available CPU cores.
* Binaryen IR compiles down to WebAssembly easily and quickly because it is
  a subset of WebAssembly.
* Effective: Binaryen's optimizer has many passes that can improve code (e.g.
  local coloring to coalesce local variables, dead code elimination; precomputing
  expressions when possible at compile time; etc.).
* WASM minification

Compilers built using Binaryen include:

* s2wasm which compiles the LLVM WebAssembly's backend .s output format
* mir2wasm which compiles Rust MIR

Those compilers generate Binaryen IR, which can then be optimized and
emitted as WebAssembly (the first two use the internal C++ API, the
last the C API).

Binaryen provides a toolchain that can:

* Parse and emit WebAssembly. Users can load WebAssembly, optimize it
  using Binaryen, and re-emit it, thus implementing a wasm-to-wasm optimizer.
* Interpret WebAssembly as well as run the WebAssembly spec tests.
* Integrate with Emscripten in order to provide a complete compiler
  toolchain from C and C++ to WebAssembly.
* Polyfill WebAssembly by running it in the interpreter compiled to JavaScript,
  if the browser does not yet have native support (useful for testing).

%package -n lib%{name}
Summary:        Library for %{name}

%description -n lib%{name}
Library for %{name}.

%package -n lib%{name}-devel
Summary:        Development files for lib%{name}
Requires:       lib%{name} = %{version}

%description -n lib%{name}-devel
Development files for lib%{name}.

%prep
%autosetup -n %{name}-version_%{version}

%build
%cmake \
    -DBUILD_TESTS=OFF \
    -DENABLE_WERROR=OFF
%cmake_build

%install
%cmake_install

%post -n lib%{name} -p /sbin/ldconfig
%postun -n lib%{name} -p /sbin/ldconfig

%files
%license LICENSE
%doc README.md Contributing.md
%{_bindir}/wasm2js
%{_bindir}/wasm-as
%{_bindir}/wasm-ctor-eval
%{_bindir}/wasm-dis
%{_bindir}/wasm-emscripten-finalize
%{_bindir}/wasm-fuzz-lattices
%{_bindir}/wasm-fuzz-types
%{_bindir}/wasm-merge
%{_bindir}/wasm-metadce
%{_bindir}/wasm-opt
%{_bindir}/wasm-reduce
%{_bindir}/wasm-shell
%{_bindir}/wasm-split

%files -n lib%{name}
%{_libdir}/lib%{name}.so

%files -n lib%{name}-devel
%{_includedir}/%{name}-c.h
%{_includedir}/wasm-delegations.def

%changelog
