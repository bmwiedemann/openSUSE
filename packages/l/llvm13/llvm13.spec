#
# spec file for package llvm13
#
# Copyright (c) 2024 SUSE LLC
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


%define _relver 13.0.1
%define _version %_relver%{?_rc:rc%_rc}
%define _tagver %_relver%{?_rc:-rc%_rc}
%define _minor  13.0
%define _sonum  13
%define _itsme13 1
# Integer version used by update-alternatives
%define _uaver  1301
%define _soclang 13
%define _socxx  1

%ifarch x86_64 aarch64 %arm
%bcond_without libcxx
%else
%bcond_with libcxx
%endif

%ifarch aarch64 ppc64 ppc64le %{ix86} x86_64
%bcond_without openmp
%else
%bcond_with openmp
%endif

%ifarch s390x
%bcond_with use_lld
%else
%bcond_without use_lld
%endif

%ifarch x86_64
%bcond_without lldb
%bcond_without lldb_python
%else
%bcond_with lldb
%bcond_with lldb_python
%endif

# Disabled on ARM because it's awfully slow and often times out. (boo#1178070)
%ifarch %{ix86} ppc64le s390x x86_64
%bcond_without thin_lto
%else
%bcond_with thin_lto
%endif

%bcond_with ffi
%bcond_with oprofile
%bcond_with valgrind
%bcond_without polly
%bcond_without lld

# Figure out the host triple.
%ifarch armv6hl
# See https://build.opensuse.org/request/show/968066.
%define target_cpu armv6kz
%else
# What RPM spells ppc, GCC spells powerpc.
%define target_cpu %{lua:print((string.gsub(rpm.expand("%{_target_cpu}"), "ppc", "powerpc")))}
%endif

%ifarch %{arm}
%define target_runtime gnueabihf
%else
%define target_runtime gnu
%endif
%define host_triple %{target_cpu}-%{_target_vendor}-%{_target_os}-%{target_runtime}

%define _plv %{!?product_libs_llvm_ver:%{_sonum}}%{?product_libs_llvm_ver}

# Expands to -n if we're providing the distribution default for the given package.
%define multisource() %{expand:%%{?_itsme%{expand:%%{!?product_libs_llvm_ver_%{1}:%%{_plv}}%%{?product_libs_llvm_ver_%{1}}}:-n}}

# set_jobs type memory
# Set max_<type>_jobs so that every job of the given type has at least the
# given amount of memory.
%define set_jobs() \
    max_%{1}_jobs="%{?jobs:%{jobs}}" \
    if test -n "$max_%{1}_jobs" -a "$max_%{1}_jobs" -gt 1 ; then \
        max_jobs="$(($avail_mem / %2))" \
        test "$max_%{1}_jobs" -gt "$max_jobs" && max_%{1}_jobs="$max_jobs" && echo "Warning: Reducing number of %{1} jobs to $max_jobs because of memory limits" \
        test "$max_%{1}_jobs" -le 0 && max_%{1}_jobs=1 && echo "Warning: Not %{1}ing in parallel at all because of memory limits" \
    fi

# Compatibility with distros that don't have /usr/libexec.
%if "%{_libexecdir}" == "%{_prefix}/libexec"
%define _libexecdir_fallback %{_libexecdir}
%else
%define _libexecdir_fallback %{_bindir}
%endif

%define _dwz_low_mem_die_limit  40000000
%define _dwz_max_die_limit     200000000

Name:           llvm13
Version:        %_relver%{?_rc:~rc%_rc}
Release:        0
Summary:        Low Level Virtual Machine
License:        Apache-2.0 WITH LLVM-exception AND NCSA
Group:          Development/Languages/Other
URL:            https://www.llvm.org/
# NOTE: please see README.packaging in the llvm package for details on how to update this package
Source0:        https://github.com/llvm/llvm-project/releases/download/llvmorg-%{_tagver}/llvm-%{_version}.src.tar.xz
Source1:        https://github.com/llvm/llvm-project/releases/download/llvmorg-%{_tagver}/clang-%{_version}.src.tar.xz
Source2:        https://github.com/llvm/llvm-project/releases/download/llvmorg-%{_tagver}/clang-tools-extra-%{_version}.src.tar.xz
Source3:        https://github.com/llvm/llvm-project/releases/download/llvmorg-%{_tagver}/compiler-rt-%{_version}.src.tar.xz
Source4:        https://github.com/llvm/llvm-project/releases/download/llvmorg-%{_tagver}/libcxx-%{_version}.src.tar.xz
Source5:        https://github.com/llvm/llvm-project/releases/download/llvmorg-%{_tagver}/libcxxabi-%{_version}.src.tar.xz
Source6:        https://github.com/llvm/llvm-project/releases/download/llvmorg-%{_tagver}/openmp-%{_version}.src.tar.xz
Source7:        https://github.com/llvm/llvm-project/releases/download/llvmorg-%{_tagver}/lld-%{_version}.src.tar.xz
Source8:        https://github.com/llvm/llvm-project/releases/download/llvmorg-%{_tagver}/lldb-%{_version}.src.tar.xz
Source9:        https://github.com/llvm/llvm-project/releases/download/llvmorg-%{_tagver}/polly-%{_version}.src.tar.xz
Source10:       https://github.com/llvm/llvm-project/raw/llvmorg-%{_tagver}/libunwind/include/mach-o/compact_unwind_encoding.h
# Docs are created manually, see below
Source50:       llvm-docs-%{_version}.src.tar.xz
Source51:       clang-docs-%{_version}.src.tar.xz
Source100:      %{name}-rpmlintrc
Source101:      baselibs.conf
# PATCH-FIX-OPENSUSE lto-disable-cache.patch -- Disable ThinLTO cache
Patch0:         lto-disable-cache.patch
# PATCH-FIX-UPSTREAM https://github.com/llvm/llvm-project/commit/54b909de682bfa4e3389b680b0916ab18c99952a,
# rebased past https://github.com/llvm/llvm-project/commit/40ec1c0f16cb23f8b83fb3d28b195e83991defd9.
Patch1:         llvm-rust-mangle-for-fastcall.patch
# PATCH-FIX-OPENSUSE assume-opensuse.patch idoenmez@suse.de -- Always enable openSUSE/SUSE features
Patch2:         assume-opensuse.patch
# PATCH-FIX-OPENSUSE default-to-i586.patch -- Use i586 as default target for 32bit
Patch3:         default-to-i586.patch
Patch4:         clang-resourcedirs.patch
Patch5:         llvm-remove-clang-only-flags.patch
Patch6:         llvm-fix-find-gcc5-install.patch
Patch9:         link-clang-shared.patch
Patch10:        link-clang-tools-extra-shared.patch
# PATCH-FIX-OPENSUSE lldb-cmake.patch -- Fix ncurses include path.
Patch11:        lldb-cmake.patch
Patch13:        llvm-normally-versioned-libllvm.patch
Patch14:        llvm-do-not-install-static-libraries.patch
# Cherry pick patch from LLVM 15: https://github.com/llvm/llvm-project/issues/56421
Patch17:        llvm-glibc-2-36.patch
# PATCH-FIX-UPSTREAM llvm-gcc13 https://github.com/llvm/llvm-project/issues/55711
Patch18:        llvm-gcc13-issue55711.patch
Patch20:        llvm_build_tablegen_component_as_shared_library.patch
Patch21:        tests-use-python3.patch
Patch22:        llvm-better-detect-64bit-atomics-support.patch
Patch24:        opt-viewer-Find-style-css-in-usr-share.patch
# PATCH-FIX-OPENSUSE lld-default-sha1.patch
Patch26:        lld-default-sha1.patch
# PATCH-FIX-OPENSUSE llvm-exegesis-link-dylib.patch -- Don't waste space for llvm-exegesis.
# It's crippled anyway because of missing deps and not relevant for users. Eventually we should drop it.
Patch27:        llvm-exegesis-link-dylib.patch
# Fix lookup of targets in installed CMake files. (boo#1180748, https://reviews.llvm.org/D96670)
Patch33:        CMake-Look-up-target-subcomponents-in-LLVM_AVAILABLE_LIBS.patch
Patch35:        llvm-update-extract-section-script.patch
# Fix build with Swig 4.1.0: backport of upstream commits 81fc5f7909a4, f0a25fe0b746. (gh#llvm/llvm-project#58018)
Patch38:        lldb-swig-4.1.0-build-fix.patch
# PATCH-FIX-UPSTREAM: Use symbol versioning also for libclang-cpp.so.
Patch39:        clang-shlib-symbol-versioning.patch
BuildRequires:  binutils-devel >= 2.21.90
BuildRequires:  cmake >= 3.13.4
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libstdc++-devel
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  python3-base
BuildRequires:  pkgconfig(libedit)
BuildRequires:  pkgconfig(zlib)
Requires(post): update-alternatives
Requires(postun): update-alternatives
# llvm does not work on s390
ExcludeArch:    s390
%if %{with ffi}
BuildRequires:  pkgconfig(libffi)
%endif
%if %{with valgrind}
BuildRequires:  pkgconfig(valgrind)
%endif
%if %{with oprofile}
BuildRequires:  oprofile-devel
%endif
Suggests:       %{name}-doc

%description
LLVM is a compiler infrastructure designed for compile-time,
link-time, runtime, and idle-time optimization of programs from
arbitrary programming languages.

The compiler infrastructure includes mirror sets of programming
tools as well as libraries with equivalent functionality.

%package -n libLLVM%{_sonum}
Summary:        Libraries for LLVM
Group:          System/Libraries

%description -n libLLVM%{_sonum}
This package contains the shared libraries needed for LLVM.

%package devel
Summary:        Header Files for LLVM
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
%if %{with openmp}
# Referenced by LLVMExports.cmake
Requires:       libomp%{_sonum}-devel
%endif
Requires:       libLLVM%{_sonum} = %{version}
Requires:       libLTO%{_sonum} = %{version}
Requires:       libstdc++-devel
Requires:       libtool
Requires:       llvm%{_sonum}-gold
%if %{with polly}
# Referenced by LLVMExports.cmake
Requires:       llvm%{_sonum}-polly-devel
%endif
Requires:       pkgconfig
Conflicts:      llvm-devel-provider < %{version}
%if %{suse_version} <= 1500
# llvm{5,7} in SLE/Leap 15.x used to have the man page for FileCheck.
Conflicts:      llvm5
Conflicts:      llvm7
%endif
Conflicts:      cmake(LLVM)
# libLTO.so used to be a separate package.
Conflicts:      libLTO.so < %{version}
Provides:       libLTO.so = %{version}
Obsoletes:      llvm%{_sonum}-LTO-devel <= %{version}
Provides:       llvm%{_sonum}-LTO-devel = %{version}
Provides:       llvm-devel-provider = %{version}
%if %{with ffi}
Requires:       pkgconfig(libffi)
%endif
%if %{with valgrind}
Requires:       pkgconfig(valgrind)
%endif
%if %{with oprofile}
Requires:       oprofile-devel
%endif

%description devel
This package contains library and header files needed to develop
new native programs that use the LLVM infrastructure.

%package doc
Summary:        Documentation for LLVM
Group:          Documentation/HTML
Requires:       %{name} = %{version}
# The docs used to be contained in the devel package.
Conflicts:      llvm-devel-provider < 9.0.0
Conflicts:      llvm-doc-provider < %{version}
Provides:       llvm-doc-provider = %{version}
BuildArch:      noarch

%description doc
This package contains documentation for the LLVM infrastructure.

%package -n clang%{_sonum}
Summary:        CLANG frontend for LLVM
Group:          Development/Languages/C and C++
URL:            https://clang.llvm.org/
Requires(post): update-alternatives
Requires(postun): update-alternatives
Recommends:     clang-tools
Recommends:     gcc
Recommends:     glibc-devel
Recommends:     libstdc++-devel
Suggests:       clang%{_sonum}-doc
Suggests:       libc++-devel

%description -n clang%{_sonum}
This package contains the clang (C language) frontend for LLVM.

%package -n clang-tools
Summary:        Tools for Clang
Group:          Development/Languages/C and C++
URL:            https://clang-analyzer.llvm.org/
# Avoid multiple provider errors
Requires:       clang%{_sonum}
# Some binaries used to be in the clang package.
Conflicts:      clang5
Conflicts:      clang6
# hmaptool used to be contained in the llvm package.
Conflicts:      llvm5
Conflicts:      llvm6
%if %{suse_version} <= 1500
# llvm9 in SLE/Leap 15.x is still affected.
Conflicts:      llvm9
%endif
Conflicts:      scan-build < %{version}
Conflicts:      scan-view < %{version}
Provides:       scan-build = %{version}
Provides:       scan-view = %{version}
Conflicts:      emacs-llvm < %{version}
Provides:       emacs-llvm = %{version}
Conflicts:      vim-plugin-llvm < %{version}

%description -n clang-tools
This package contains tools and scripts for using Clang, including:
* bash completions for clang,
* the clang-doc tool,
* plugins for using clang-format, clang-rename, clang-include-fixer
  in vim and emacs.
* scripts for using clang-format: git-clang-format and clang-format-diff,
* scripts for using clang-tidy: run-clang-tidy and clang-tidy-diff,
* scripts for using the Clang static analyzer: scan-build and scan-view,
* a script for using find-all-symbols: run-find-all-symbols.

%package %{multisource libclang%{_soclang}} libclang%{_soclang}
Summary:        Clang stable C API for indexing and code completion
Group:          System/Libraries
Provides:       libclang%{_soclang} = %{version}
Conflicts:      libclang%{_soclang} < %{version}

%description %{multisource libclang%{_soclang}} libclang%{_soclang}
This library exposes a limited C API for indexing and code completion for
code written in languages of the C family.
It is designed to be stable across major versions of LLVM.

It corresponds to the header files in %{_includedir}/clang-c.

%package -n libclang-cpp%{_sonum}
Summary:        Clang full C++ API
Group:          System/Libraries

%description -n libclang-cpp%{_sonum}
This library exposes the full C++ API to Clang that is used to implement
all Clang tools. It is not stable across major LLVM versions.

It corresponds to the header files in %{_includedir}/clang.

%package -n clang%{_sonum}-devel
Summary:        CLANG frontend for LLVM (devel package)
Group:          Development/Libraries/C and C++
Requires:       %{name}-devel = %{version}
Requires:       clang%{_sonum} = %{version}
Requires:       clang-tools >= %{version}
Requires:       libclang%{_soclang} >= %{version}
Requires:       libclang-cpp%{_sonum} = %{version}
Conflicts:      cmake(Clang)

%description -n clang%{_sonum}-devel
This package contains the clang (C language) frontend for LLVM.
(development files)

%package -n clang%{_sonum}-doc
Summary:        Documentation for Clang
Group:          Documentation/HTML
Conflicts:      clang-doc-provider < %{version}
# The docs used to be contained in the devel package.
Conflicts:      clang5-devel
Conflicts:      clang6-devel
Conflicts:      clang7-devel
Conflicts:      clang8-devel
Provides:       clang-doc-provider = %{version}
BuildArch:      noarch

%description -n clang%{_sonum}-doc
This package contains documentation for the Clang compiler.

%package -n libLTO%{_sonum}
Summary:        Link-time optimizer for LLVM
Group:          System/Libraries

%description -n libLTO%{_sonum}
This package contains the link-time optimizer for LLVM.

%package gold
Summary:        LLVM LTO plugin for ld.bfd and ld.gold
Group:          Development/Tools/Building
Conflicts:      llvm-gold-provider < %{version}
Provides:       llvm-gold-provider = %{version}
Supplements:    packageand(clang%{_sonum}:binutils)
Supplements:    packageand(clang%{_sonum}:binutils-gold)

%description gold
This package contains a plugin for link-time optimization in binutils linkers.

Despite the name, it can also be used with ld.bfd. It is required for using
Clang with -flto=full or -flto=thin when linking with one of those linkers.

%package -n libomp%{_sonum}-devel
Summary:        MPI plugin for LLVM
Group:          Development/Libraries/C and C++
Conflicts:      libomp-devel < %{version}
Provides:       libomp-devel = %{version}

%description -n libomp%{_sonum}-devel
This package contains the OpenMP MPI plugin for LLVM.

%package %{multisource libcxx%{_socxx}} libc++%{_socxx}
Summary:        C++ standard library implementation
Group:          System/Libraries
URL:            https://libcxx.llvm.org/
Requires:       libc++abi%{_socxx} = %{version}
Conflicts:      libc++%{_socxx} < %{version}
Provides:       libc++%{_socxx} = %{version}

%description %{multisource libcxx%{_socxx}} libc++%{_socxx}
This package contains libc++, a new implementation of the C++
standard library, targeting C++11.

%package %{multisource libcxx_devel} libc++-devel
Summary:        C++ standard library implementation (devel package)
Group:          Development/Libraries/C and C++
Requires:       libc++%{_socxx} >= %{version}
Requires:       libc++abi.so >= %{version}
Conflicts:      libc++.so < %{version}
Provides:       libc++.so = %{version}

%description %{multisource libcxx_devel} libc++-devel
This package contains libc++, a new implementation of the C++
standard library, targeting C++11. (development files)

%package %{multisource libcxxabi%{_socxx}} libc++abi%{_socxx}
Summary:        C++ standard library ABI
Group:          System/Libraries
URL:            https://libcxxabi.llvm.org/
Conflicts:      libc++abi%{_socxx} < %{version}
Provides:       libc++abi%{_socxx} = %{version}

%description %{multisource libcxxabi%{_socxx}} libc++abi%{_socxx}
This package contains the ABI for libc++, a new implementation
of the C++ standard library, targeting C++11.

%package %{multisource libcxx_devel} libc++abi-devel
Summary:        C++ standard library ABI (devel package)
Group:          Development/Libraries/C and C++
Requires:       libc++abi%{_socxx} >= %{version}
Conflicts:      libc++abi.so < %{version}
Provides:       libc++abi.so = %{version}

%description %{multisource libcxx_devel} libc++abi-devel
This package contains the ABI for libc++, a new implementation
of the C++ standard library, targeting C++11.
(development files)

%package        vim-plugins
Summary:        Vim plugins for LLVM
Group:          Productivity/Text/Editors
Supplements:    packageand(llvm%{_sonum}:vim)
Conflicts:      vim-plugin-llvm < %{version}
Provides:       vim-plugin-llvm = %{version}
BuildArch:      noarch

%description    vim-plugins
This package contains vim plugins for LLVM like syntax highlighting.

%package -n python3-clang%{_sonum}
Summary:        Python bindings for libclang
Group:          Development/Libraries/Python
Requires:       libclang%{_soclang} >= %{version}
Requires:       python3-base
%if %{suse_version} > 1500
Conflicts:      %{python3_sitelib}/clang/
Provides:       %{python3_sitelib}/clang/
%else
Conflicts:      %{python3_sitearch}/clang/
Provides:       %{python3_sitearch}/clang/
%endif
BuildArch:      noarch

%description -n python3-clang%{_sonum}
This package contains the Python bindings to clang (C language)
frontend for LLVM.

%package -n lld%{_sonum}
Summary:        Linker for Clang/LLVM
Group:          Development/Tools/Building
URL:            https://lld.llvm.org/
Requires(post): update-alternatives
Requires(postun): update-alternatives

%description -n lld%{_sonum}
LLD is a linker from the LLVM project. That is a drop-in replacement for system linkers and runs much faster than them. It also provides features that are useful for toolchain developers.

%package opt-viewer
Summary:        Tools for visualising the LLVM optimization records
Group:          Development/Languages/Other
BuildRequires:  python3-base
Requires:       python3-PyYAML
Requires:       python3-Pygments
Conflicts:      opt-viewer < %{version}
Provides:       opt-viewer = %{version}
BuildArch:      noarch

%description opt-viewer
Set of tools for visualising the LLVM optimization records generated with -fsave-optimization-record. Used for compiler-assisted performance analysis.

%if %{with lldb}
%package -n lldb%{_sonum}
Summary:        Software debugger built using LLVM libraries
Group:          Development/Tools/Debuggers
URL:            https://lldb.llvm.org/
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libedit)
BuildRequires:  pkgconfig(libffi)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(panel)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(zlib)
Requires(post): update-alternatives
Requires(postun): update-alternatives
Recommends:     python3-lldb%{_sonum}
ExclusiveArch:  x86_64

%description -n lldb%{_sonum}
LLDB is a next generation, high-performance debugger. It is built as a set
of reusable components which highly leverage existing libraries in the
larger LLVM Project, such as the Clang expression parser and LLVM
disassembler.

%package -n liblldb%{_sonum}
Summary:        LLDB software debugger runtime library
Group:          System/Libraries

%description -n liblldb%{_sonum}
This subpackage contains the main LLDB component.

%package -n lldb%{_sonum}-devel
Summary:        Development files for LLDB
Group:          Development/Libraries/C and C++
Requires:       clang%{_sonum}-devel = %{version}
Requires:       liblldb%{_sonum} = %{version}
Requires:       llvm%{_sonum}-devel = %{version}
Requires:       pkgconfig(libedit)
Requires:       pkgconfig(libxml-2.0)
Conflicts:      lldb-devel-provider < %{version}
Provides:       lldb-devel-provider = %{version}

%description -n lldb%{_sonum}-devel
This package contains the development files for LLDB.

%if %{with lldb_python}
%package -n python3-lldb%{_sonum}
Summary:        Python bindings for liblldb
Group:          Development/Libraries/Python
BuildRequires:  swig >= 3.0.11
Requires:       liblldb%{_sonum} = %{version}
Requires:       python3-base
Requires:       python3-six
Conflicts:      %{python3_sitearch}/lldb/
Provides:       %{python3_sitearch}/lldb/

%description -n python3-lldb%{_sonum}
This package contains the Python bindings for LLDB. It also contains
pretty printers for the C++ standard library.
%endif

%endif

%if %{with polly}
%package polly
Summary:        LLVM Framework for High-Level Loop and Data-Locality Optimizations
Group:          Development/Languages/Other
URL:            https://polly.llvm.org/
Conflicts:      llvm-polly-provider < %{version}
Provides:       llvm-polly-provider = %{version}

%description polly
Polly is a high-level loop and data-locality optimizer and optimization
infrastructure for LLVM. It uses an abstract mathematical representation based
on integer polyhedra to analyze and optimize the memory access pattern of a
program. Polly can currently perform classical loop transformations, especially
tiling and loop fusion to improve data-locality. It can also exploit OpenMP
level parallelism and expose SIMDization opportunities.

%package polly-devel
Summary:        Development files for Polly
Group:          Development/Libraries/C and C++
Requires:       llvm%{_sonum}-devel = %{version}
Requires:       llvm%{_sonum}-polly = %{version}
Conflicts:      llvm-polly-devel-provider < %{version}
Provides:       llvm-polly-devel-provider = %{version}

%description polly-devel
This package contains the development files for Polly.
%endif

%prep
%setup -q -a 1 -a 2 -a 3 -a 4 -a 5 -a 6 -a 7 -a 8 -a 9 -b 50 -b 51 -n llvm-%{_version}.src
%patch -P 0 -p2
%patch -P 1 -p2
%patch -P 5 -p1
%patch -P 13 -p1
%patch -P 14 -p1
%patch -P 18 -p2
%patch -P 20 -p1
%patch -P 21 -p1
%patch -P 22 -p1
%patch -P 24 -p1
%patch -P 27 -p2
%patch -P 33 -p2
%patch -P 35 -p2

pushd clang-%{_version}.src
%patch -P 2 -p1
%patch -P 3 -p1
%patch -P 4 -p1
%patch -P 6 -p1
%patch -P 9 -p2
%patch -P 39 -p2

# We hardcode openSUSE
rm unittests/Driver/DistroTest.cpp

# We hardcode i586
rm test/Driver/x86_features.c
rm test/Driver/nacl-direct.c
popd

pushd clang-tools-extra-%{_version}.src
%patch -P 10 -p2
popd

pushd compiler-rt-%{_version}.src
%patch -P 17 -p2
popd

pushd lld-%{_version}.src
%patch -P 26 -p1
# lld got a compile-time dependency on libunwind that we don't want. (https://reviews.llvm.org/D86805)
mkdir include/mach-o
cp %{SOURCE10} include/mach-o
popd

%if %{with lldb}
pushd lldb-%{_version}.src
%patch -P 11 -p1
%patch -P 38 -p2
popd
%endif

%if %{with libcxx}
pushd libcxx-%{_version}.src
rm test/libcxx/thread/thread.threads/thread.thread.this/sleep_for.pass.cpp
rm test/std/localization/locale.categories/category.time/locale.time.get.byname/get_monthname.pass.cpp
rm test/std/localization/locale.categories/category.time/locale.time.get.byname/get_monthname_wide.pass.cpp

# These tests often verify timing and can randomly fail if the system is under heavy load. It happens sometimes on our build machines.
rm -rf test/std/thread/
popd
%endif

# Move into right place
mv clang-%{_version}.src tools/clang
mv compiler-rt-%{_version}.src projects/compiler-rt
mv clang-tools-extra-%{_version}.src tools/clang/tools/extra
%if %{with lld}
mv lld-%{_version}.src tools/lld
%endif
%if %{with polly}
mv polly-%{_version}.src tools/polly
%endif

%if %{with lldb}
mv lldb-%{_version}.src tools/lldb
%endif

%if %{with openmp}
mv openmp-%{_version}.src  projects/openmp
%endif

%if %{with libcxx}
mv libcxx-%{_version}.src projects/libcxx
mv libcxxabi-%{_version}.src projects/libcxxabi
%endif

%build
%define _lto_cflags %{nil}

# Use optflags, but:
# 1) Remove the -D_FORTIFY_SOURCE=2 because llvm does not build correctly with
#    hardening. The problem is in sanitizers from compiler-rt.
# 2) Remove the -g. We don't want it in stage1 and it will be added by cmake in
#    the following stage.
flags=$(echo %{optflags} | sed 's/-D_FORTIFY_SOURCE=./-D_FORTIFY_SOURCE=0/;s/\B-g\b//g')

%ifarch armv6hl
flags+=" -mfloat-abi=hard -mcpu=arm1176jzf-s -mfpu=vfpv2"
%endif
%ifarch armv7hl
flags+=" -mfloat-abi=hard -march=armv7-a -mtune=cortex-a17 -mfpu=vfpv3-d16"
%endif

CFLAGS=$flags
CXXFLAGS=$flags

# By default build everything
TARGETS_TO_BUILD="all"
EXPERIMENTAL_TARGETS_TO_BUILD="M68k"
%ifarch s390 s390x
# No graphics cards on System z
TARGETS_TO_BUILD="host;BPF"
EXPERIMENTAL_TARGETS_TO_BUILD=
%endif
%ifarch %arm
# TODO: Document why those.
TARGETS_TO_BUILD="host;ARM;AMDGPU;BPF;NVPTX"
EXPERIMENTAL_TARGETS_TO_BUILD=
%endif
%ifarch ppc64 ppc64le
# TODO: Document why those.
TARGETS_TO_BUILD="host;AMDGPU;BPF;NVPTX"
EXPERIMENTAL_TARGETS_TO_BUILD=
%endif
%ifarch ppc
# TODO: Graphics cards turned off because of relocation overflows.
TARGETS_TO_BUILD="host;BPF"
EXPERIMENTAL_TARGETS_TO_BUILD=
%endif

mem_per_compile_job=1000000
%ifarch i586 ppc armv6hl armv7hl
# 32-bit arches need less memory than 64-bit arches.
mem_per_compile_job=600000
%endif

mem_per_link_job=3000000
%ifarch riscv64
# Give RISCV link jobs more memory.
mem_per_link_job=4000000
%endif

echo "Available memory:"
cat /proc/meminfo
echo "System limits:"
ulimit -a
avail_mem=$(awk '/MemAvailable/ { print $2 }' /proc/meminfo)
%set_jobs link $mem_per_link_job
%set_jobs compile $mem_per_compile_job

%define __builder ninja
%define __builddir stage1
%define build_ldflags -Wl,--no-keep-memory
%cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DBUILD_SHARED_LIBS:BOOL=OFF \
    -DLLVM_HOST_TRIPLE=%{host_triple} \
    -DLLVM_BUILD_LLVM_DYLIB:BOOL=OFF \
    -DLLVM_LINK_LLVM_DYLIB:BOOL=OFF \
    -DLLVM_PARALLEL_COMPILE_JOBS="$max_compile_jobs" \
    -DLLVM_PARALLEL_LINK_JOBS="$max_link_jobs" \
    -DENABLE_LINKER_BUILD_ID=ON \
    -DLLVM_BINUTILS_INCDIR=%{_includedir} \
    -DPython3_EXECUTABLE=%{_bindir}/python3 \
    -DLLVM_BUILD_TOOLS:BOOL=OFF \
    -DLLVM_BUILD_UTILS:BOOL=OFF \
    -DLLVM_BUILD_EXAMPLES:BOOL=OFF \
    -DLLVM_POLLY_BUILD:BOOL=OFF \
    -DLLVM_TOOL_CLANG_TOOLS_EXTRA_BUILD:BOOL=OFF \
    -DLLVM_INCLUDE_TESTS:BOOL=OFF \
    -DLLVM_TARGETS_TO_BUILD=Native \
    -DCLANG_ENABLE_ARCMT:BOOL=OFF \
    -DCLANG_ENABLE_STATIC_ANALYZER:BOOL=OFF \
    -DCOMPILER_RT_BUILD_SANITIZERS:BOOL=OFF \
    -DCOMPILER_RT_BUILD_XRAY:BOOL=OFF \
    -DLLDB_DISABLE_PYTHON=ON
ninja -v %{?_smp_mflags} clang llvm-tblgen clang-tblgen \
%if %{with thin_lto}
    llvm-ar llvm-ranlib \
%if %{with use_lld}
    lld
%else
    LLVMgold
%endif
%endif

cd ..

# Remove files that won't be needed anymore.
# This reduces the total amount of disk space used during build. (bnc#1074625)
find ./stage1 \( -name '*.o' -or -name '*.a' \) -delete

# 3) Remove -fstack-clash-protection on architectures where it isn't supported.
#    Using it just prints a warning, but that warning prevents the configuration
#    step, which uses -Werror, from recognizing the availability of other flags.
if ! ${PWD}/stage1/bin/clang -c -xc -Werror -fstack-clash-protection -o /dev/null /dev/null;
then
    flags=$(echo $flags | sed 's/-fstack-clash-protection//');
fi
CFLAGS=$flags
CXXFLAGS=$flags

# Clang uses a bit less memory.
mem_per_compile_job=700000
%ifarch i586 ppc armv6hl armv7hl
# 32-bit arches need less memory than 64-bit arches.
mem_per_compile_job=500000
%endif

%set_jobs compile $mem_per_compile_job
%if %{with thin_lto}
# A single ThinLTO job is fully parallel already.
max_link_jobs=1
%endif

%define __builddir build
%define build_ldflags -Wl,--build-id=sha1
export PATH=${PWD}/stage1/bin:$PATH
export CC=${PWD}/stage1/bin/clang
export CXX=${PWD}/stage1/bin/clang++
%if %{with thin_lto}
export LLVM_AR=${PWD}/stage1/bin/llvm-ar
export LLVM_RANLIB=${PWD}/stage1/bin/llvm-ranlib
export LLD=${PWD}/stage1/bin/ld.lld
%endif
export LLVM_TABLEGEN=${PWD}/stage1/bin/llvm-tblgen
export CLANG_TABLEGEN=${PWD}/stage1/bin/clang-tblgen
# Build is using absolute paths assuming the monorepo layout, so we need this.
export CLANG_TOOLS_EXTRA_DIR=${PWD}/tools/clang/tools/extra
# The build occasionally uses tools linking against previously built
# libraries (mostly libLLVM.so), but we don't want to set RUNPATHs.
export LD_LIBRARY_PATH=${PWD}/build/%{_lib}
%cmake \
    -DBUILD_SHARED_LIBS:BOOL=OFF \
    -DLLVM_HOST_TRIPLE=%{host_triple} \
    -DLLVM_BUILD_LLVM_DYLIB:BOOL=ON \
    -DLLVM_LINK_LLVM_DYLIB:BOOL=ON \
    -DCLANG_LINK_CLANG_DYLIB:BOOL=ON \
    -DLLVM_PARALLEL_COMPILE_JOBS="$max_compile_jobs" \
    -DLLVM_PARALLEL_LINK_JOBS="$max_link_jobs" \
%if %{with thin_lto}
    -DLLVM_ENABLE_LTO=Thin \
    -DCMAKE_AR="${LLVM_AR}" \
    -DCMAKE_RANLIB="${LLVM_RANLIB}" \
%if %{with use_lld}
    -DCMAKE_LINKER=${LLD} \
    -DLLVM_USE_LINKER=${LLD} \
%endif
%endif
%ifarch %arm ppc s390 %{ix86}
    -DCMAKE_C_FLAGS_RELWITHDEBINFO="-O2 -g1 -DNDEBUG" \
    -DCMAKE_CXX_FLAGS_RELWITHDEBINFO="-O2 -g1 -DNDEBUG" \
%endif
    -DENABLE_LINKER_BUILD_ID=ON \
    -DLLVM_TABLEGEN="${LLVM_TABLEGEN}" \
    -DCLANG_TABLEGEN="${CLANG_TABLEGEN}" \
    -DLLVM_ENABLE_RTTI:BOOL=ON \
    -DLLVM_ENABLE_PIC=ON \
    -DLLVM_BINUTILS_INCDIR=%{_includedir} \
    -DPython3_EXECUTABLE=%{_bindir}/python3 \
    -DLLVM_TARGETS_TO_BUILD=${TARGETS_TO_BUILD} \
    -DLLVM_EXPERIMENTAL_TARGETS_TO_BUILD=${EXPERIMENTAL_TARGETS_TO_BUILD} \
%if %{with libcxx}
    -DLIBCXX_ENABLE_SHARED=YES \
    -DLIBCXX_ENABLE_STATIC=NO \
    -DLIBCXX_ENABLE_EXPERIMENTAL_LIBRARY=NO \
    -DLIBCXXABI_ENABLE_SHARED=YES \
    -DLIBCXXABI_ENABLE_STATIC=NO \
%endif
%if "%{_lib}" == "lib64"
    -DLLVM_LIBDIR_SUFFIX=64 \
%endif
%if %{with ffi}
    -DLLVM_ENABLE_FFI=ON \
%endif
%if %{with oprofile}
    -DLLVM_USE_OPROFILE=ON \
%endif
%if %{without lldb_python}
    -DLLDB_DISABLE_PYTHON=ON \
%endif
    -DCMAKE_SKIP_RPATH:BOOL=ON \
    -DLLVM_POLLY_LINK_INTO_TOOLS=OFF \
    -DLLVM_EXTERNAL_CLANG_TOOLS_EXTRA_SOURCE_DIR=${CLANG_TOOLS_EXTRA_DIR} \
    -DPOLLY_BUNDLED_ISL:BOOL=ON

# ThinLTO uses multiple threads from the linker process for optimizations, which
# causes an extremely high lock contention on allocations due to MALLOC_CHECK_,
# so we deactivate it for compilation. The tests will have it activated again.
%if %{with thin_lto}
MALLOC_CHECK_BACK=$MALLOC_CHECK_
unset MALLOC_CHECK_
%endif

ninja -v %{?_smp_mflags}

%if %{with thin_lto}
MALLOC_CHECK_=$MALLOC_CHECK_BACK
%endif

cd ..

%install
# Installation seems to build some files not contained in "all".
export LD_LIBRARY_PATH=${PWD}/build/%{_lib}
%cmake_install

# Install FileCheck needed for testing Rust boo#1192629
install -m 0755 build/bin/FileCheck %{buildroot}%{_bindir}/FileCheck

# Remove files that won't be needed anymore.
# This reduces the total amount of disk space used during build. (bnc#1074625)
find ./build \( -name '*.o' -or -name '*.a' \)  -delete

# Docs are prebuilt due to sphinx dependency
#
# tar xf llvm-%{_version}.src.tar.xz
# pushd llvm-%{_version}.src/tools
# tar xf ../../clang-%{_version}.src.tar.xz
# mv clang-%{_version}.src clang
# cd ..
# ln -s ../../../build/tools/clang/docs/{Attribute,Diagnostics}Reference.rst tools/clang/docs
# mkdir build; cd build
# cmake -G Ninja -DLLVM_ENABLE_SPHINX:BOOL=ON -DLLVM_BUILD_DOCS:BOOL=ON \
#     -DSPHINX_WARNINGS_AS_ERRORS:BOOL=OFF ..
# ninja gen-{Attribute,Diagnostics}Reference.rst
# ninja -j1 docs-{llvm,clang}-{html,man}
# popd
# tar --sort=name --owner=0 --group=0 --mtime="@${SOURCE_DATE_EPOCH}" \
#     --pax-option=exthdr.name=%d/PaxHeaders/%f,delete=atime,delete=ctime \
#     -cJf llvm-docs-%{_version}.src.tar.xz llvm-%{_version}.src/build/docs/{man,html}
# tar --sort=name --owner=0 --group=0 --mtime="@${SOURCE_DATE_EPOCH}" \
#     --pax-option=exthdr.name=%d/PaxHeaders/%f,delete=atime,delete=ctime \
#     -cJf clang-docs-%{_version}.src.tar.xz llvm-%{_version}.src/build/tools/clang/docs/{man,html}

# Build man/html pages
pushd build/docs
rm -rf %{buildroot}%{_prefix}/docs
mkdir -p %{buildroot}%{_docdir}/llvm
mkdir -p %{buildroot}%{_mandir}/man1
cp -r man/* %{buildroot}%{_mandir}/man1
cp -r html/* %{buildroot}%{_docdir}/llvm
rm -r %{buildroot}%{_docdir}/llvm/_sources
popd

pushd build/tools/clang/docs
mkdir -p %{buildroot}%{_docdir}/llvm-clang
cp -r man/* %{buildroot}%{_mandir}/man1
cp -r html/* %{buildroot}%{_docdir}/llvm-clang
rm -r %{buildroot}%{_docdir}/llvm-clang/_sources
popd

# install python bindings
install -d %{buildroot}%{python3_sitelib}/clang
pushd tools/clang/bindings/python
cp clang/*.py %{buildroot}%{python3_sitelib}/clang
# Make the bindings use the current so number, so that we don't need an unversioned libclang.so.
sed -i "s/file = 'libclang\.so'/file = 'libclang.so.%{_soclang}'/" %{buildroot}%{python3_sitelib}/clang/cindex.py
install -d %{buildroot}%{_docdir}/python-clang/examples/cindex
cp -r examples %{buildroot}%{_docdir}/python-clang
install -d %{buildroot}%{_docdir}/python-clang/tests/cindex/INPUTS
cp -r tests %{buildroot}%{_docdir}/python-clang
popd

# Scripts for clang use unversioned executables, so it doesn't make sense to
# have multiple versions of them. We package them only for the default version.
%if %{_plv} == %{_sonum}
%if "%{_libexecdir}" != "%{_prefix}/libexec"
mv %{buildroot}%{_prefix}/libexec/{c++,ccc}-analyzer %{buildroot}%{_bindir}
mv %{buildroot}%{_prefix}/libexec/{analyze,intercept}-{cc,c++} %{buildroot}%{_bindir}
%endif

mv %{buildroot}%{_datadir}/clang/clang-format-diff.py %{buildroot}%{_bindir}/clang-format-diff
mv %{buildroot}%{_datadir}/clang/clang-tidy-diff.py %{buildroot}%{_bindir}/clang-tidy-diff
mv %{buildroot}%{_datadir}/clang/run-find-all-symbols.py %{buildroot}%{_bindir}/run-find-all-symbols

# Fix paths to internal binaries.
sed -i "s|COMPILER_WRAPPER_\([A-Z]*\) = 'intercept-\([^']*\)'|COMPILER_WRAPPER_\1 = '%{_libexecdir_fallback}/intercept-\2'|" \
    %{buildroot}%{_prefix}/lib/libscanbuild/intercept.py
%if "%{_libexecdir}" != "%{_prefix}/libexec"
LIBEXEC=%{_libexecdir_fallback}
RELATIVE_LIBEXEC=${LIBEXEC#%{_prefix}/}
RELATIVE_LIBEXEC_COMMA=${RELATIVE_LIBEXEC//\//\', \'}
sed -i "s|os.path.join(scanbuild_dir, '..', 'libexec', 'analyze-\([^']*\)')|os.path.join(scanbuild_dir, '..', '$RELATIVE_LIBEXEC_COMMA', 'analyze-\1')|" \
    %{buildroot}%{_prefix}/lib/libscanbuild/analyze.py
%endif

mkdir -p %{buildroot}%{_datadir}/bash-completion/completions
mv %{buildroot}%{_datadir}/clang/bash-autocomplete.sh %{buildroot}%{_datadir}/bash-completion/completions/clang

# We don't care about applescript or sublime text
rm %{buildroot}%{_datadir}/clang/*.applescript
rm %{buildroot}%{_datadir}/clang/clang-format-sublime.py
%else
rm %{buildroot}%{_bindir}/{analyze,intercept}-build
rm %{buildroot}%{_bindir}/clang-doc
rm %{buildroot}%{_bindir}/git-clang-format
rm %{buildroot}%{_bindir}/hmaptool
rm %{buildroot}%{_bindir}/run-clang-tidy
rm %{buildroot}%{_bindir}/scan-{build,build-py,view}
rm -r %{buildroot}%{_prefix}/lib/lib{ear,scanbuild}
rm %{buildroot}%{_prefix}/libexec/{c++,ccc}-analyzer
rm %{buildroot}%{_prefix}/libexec/{analyze,intercept}-{cc,c++}
rm -r %{buildroot}%{_datadir}/{clang,scan-build,scan-view}/
rm %{buildroot}%{_mandir}/man1/scan-build.1
%endif

# Note that bfd-plugins is in /usr/lib/bfd-plugins before binutils 2.33.1
mkdir -p %{buildroot}%{_libdir}/bfd-plugins
ln -s %{_libdir}/LLVMgold.so %{buildroot}%{_libdir}/bfd-plugins/

install -m 755 -d %{buildroot}%{_datadir}/vim/site/
for i in ftdetect ftplugin indent syntax; do
    cp -r utils/vim/$i %{buildroot}%{_datadir}/vim/site/
done
mv utils/vim/README utils/vim/README.vim

install -d %{buildroot}%{python3_sitelib}
mv %{buildroot}%{_datadir}/opt-viewer/opt-diff.py %{buildroot}%{_bindir}/opt-diff
mv %{buildroot}%{_datadir}/opt-viewer/opt-stats.py %{buildroot}%{_bindir}/opt-stats
mv %{buildroot}%{_datadir}/opt-viewer/opt-viewer.py %{buildroot}%{_bindir}/opt-viewer
mv %{buildroot}%{_datadir}/opt-viewer/optpmap.py %{buildroot}%{python3_sitelib}/optpmap.py
mv %{buildroot}%{_datadir}/opt-viewer/optrecord.py %{buildroot}%{python3_sitelib}/optrecord.py

rm %{buildroot}%{_mandir}/man1/{,clang-,lldb-,mlir-}tblgen.1
rm %{buildroot}%{_mandir}/man1/llvm-locstats.1

%if %{with lldb_python}
# Python: fix binary libraries location.
rm %{buildroot}%{python3_sitearch}/lldb/_lldb.so
liblldb=$(basename $(readlink -e %{buildroot}%{_libdir}/liblldb.so))
ln -vsf "../../../${liblldb}" %{buildroot}%{python3_sitearch}/lldb/_lldb.so

# Remove bundled six.py.
rm -f %{buildroot}%{python3_sitearch}/six.*
%endif

# Stuff we don't want to include
rm %{buildroot}%{_includedir}/mach-o/compact_unwind_encoding.h
rm %{buildroot}%{_mandir}/man1/lit.1

# These are only available as static libraries, which we don't ship.
rm -rf %{buildroot}%{_includedir}/{clang-tidy,lld}
rm -rf %{buildroot}%{_libdir}/cmake/lld/

%if %{with openmp}
rm %{buildroot}%{_libdir}/libgomp.so
rm %{buildroot}%{_libdir}/libiomp*.so
rm %{buildroot}%{_libdir}/libarcher_static.a
%endif

# Prepare for update-alternatives usage
mkdir -p %{buildroot}%{_sysconfdir}/alternatives
binfiles=( bugpoint dsymutil llc lli \
           llvm-addr2line llvm-ar llvm-as llvm-bcanalyzer llvm-bitcode-strip llvm-c-test llvm-cat llvm-cfi-verify
           llvm-cov llvm-cxxdump llvm-cxxfilt llvm-cxxmap llvm-cvtres llvm-diff llvm-dis \
           llvm-dlltool llvm-dwarfdump llvm-dwp llvm-exegesis llvm-extract llvm-gsymutil llvm-ifs \
           llvm-install-name-tool llvm-jitlink llvm-lib llvm-libtool-darwin \
           llvm-link llvm-lipo llvm-lto llvm-lto2 llvm-mc llvm-mca \
           llvm-ml llvm-mt llvm-modextract llvm-nm llvm-objcopy llvm-objdump llvm-opt-report llvm-otool \
           llvm-pdbutil llvm-profdata llvm-profgen llvm-ranlib llvm-rc llvm-readelf llvm-readobj llvm-reduce \
           llvm-rtdyld llvm-sim llvm-size llvm-split llvm-stress llvm-strings llvm-strip \
           llvm-symbolizer llvm-tapi-diff llvm-tblgen llvm-undname llvm-windres \
           llvm-xray opt sancov sanstats split-file verify-uselistorder \
           c-index-test clang clangd clang++ clang-apply-replacements \
           clang-change-namespace clang-check clang-cl clang-cpp clang-extdef-mapping clang-format \
           clang-include-fixer clang-move clang-offload-bundler \
           clang-offload-wrapper clang-query clang-refactor clang-repl clang-scan-deps clang-rename \
           clang-reorder-fields clang-tidy diagtool find-all-symbols modularize pp-trace \
%if %{with lldb}
           lldb lldb-argdumper lldb-instr lldb-server lldb-vscode \
%endif
%if %{with lld}
           ld.lld lld lld-link ld64.lld ld64.lld.darwinnew ld64.lld.darwinold wasm-ld \
%endif
	   )
manfiles=( bugpoint dsymutil llc lli \
           llvm-addr2line llvm-ar llvm-as llvm-bcanalyzer llvm-cov llvm-cxxfilt llvm-cxxmap llvm-diff \
           llvm-dis llvm-dwarfdump llvm-exegesis llvm-extract llvm-install-name-tool \
           llvm-lib llvm-libtool-darwin llvm-link llvm-lipo llvm-mca \
           llvm-nm llvm-objcopy llvm-objdump llvm-otool llvm-pdbutil \
           llvm-profdata llvm-profgen llvm-ranlib llvm-readelf llvm-readobj \
           llvm-size llvm-stress llvm-strings llvm-strip llvm-symbolizer llvm-tblgen opt \
           clang diagtool )

# Fix the clang -> clang-X.Y symlink to work with update-alternatives
mv %{buildroot}%{_bindir}/clang-%{_sonum} %{buildroot}%{_bindir}/clang
ln -s %{_bindir}/clang-%{_relver} %{buildroot}%{_bindir}/clang-%{_sonum}
ln -s %{_bindir}/clang-%{_relver} %{buildroot}%{_bindir}/clang-%{_minor}

# Add clang++-X.Y symbolic link as well - it seems to be expected by some
# software. https://bugzilla.opensuse.org/show_bug.cgi?id=1012260
ln -s %{_bindir}/clang++-%{_relver} %{buildroot}%{_bindir}/clang++-%{_sonum}
ln -s %{_bindir}/clang++-%{_relver} %{buildroot}%{_bindir}/clang++-%{_minor}

# Rewrite symlinks to point to new location
for p in "${binfiles[@]}" ; do
    if [ -h "%{buildroot}%{_bindir}/$p" ] ; then
        ln -f -s %{_bindir}/$(readlink %{buildroot}%{_bindir}/$p)-%{_relver} %{buildroot}%{_bindir}/$p
    fi
done
for p in "${binfiles[@]}" ; do
    mv %{buildroot}%{_bindir}/$p %{buildroot}%{_bindir}/$p-%{_relver}
    ln -s -f %{_sysconfdir}/alternatives/$p %{buildroot}%{_bindir}/$p
done
for p in "${manfiles[@]}" ; do
    mv %{buildroot}%{_mandir}/man1/$p.1 %{buildroot}%{_mandir}/man1/$p-%{_relver}.1
    ln -s -f %{_sysconfdir}/alternatives/$p.1%{ext_man} %{buildroot}%{_mandir}/man1/$p.1%{ext_man}
done

# Also rewrite the CMake files referring to the binaries.
sed -i "$(
    for p in "${binfiles[@]}"; do
        echo "s|\"\${_IMPORT_PREFIX}/bin/$p\"|\"\${_IMPORT_PREFIX}/bin/$p-%{_relver}\"|g"
    done
)" %{buildroot}%{_libdir}/cmake/{llvm/LLVMExports,clang/ClangTargets}-relwithdebinfo.cmake

# For libclang, have the CMake export list refer to the library via soname.
# The original library might not be available. (We might have a newer version.)
sed -i "s|\"\${_IMPORT_PREFIX}/%{_lib}/libclang.so.%{_relver}\"|\"\${_IMPORT_PREFIX}/%{_lib}/libclang.so.%{_soclang}\"|g" \
    %{buildroot}%{_libdir}/cmake/clang/ClangTargets-relwithdebinfo.cmake

# rpm macro for version checking
mkdir -p %{buildroot}%{_rpmconfigdir}/macros.d/
cat > %{buildroot}%{_rpmconfigdir}/macros.d/macros.llvm <<EOF
#
# RPM macros for LLVM/Clang packaging
#

# Version information
%_llvm_version %{version}
%_llvm_relver %{_relver}
%_llvm_minorver %{_minor}
%_llvm_sonum  %{_sonum}
%_libcxx_sonum %{_socxx}

# Build information
%_llvm_with_libcxx %{with libcxx}
%_llvm_with_openmp %{with openmp}
%_llvm_with_ffi %{with ffi}
%_llvm_with_oprofile %{with oprofile}
%_llvm_with_valgrind %{with valgrind}
%_llvm_with_lldb %{with lldb}
EOF

# Don't use env in shebangs, and prefer python3.X. (https://www.python.org/dev/peps/pep-0394/#for-python-runtime-distributors)
sed -i -E "1s|/usr/bin/env *|/usr/bin/|; 1s|/usr/bin/python3?\$|$(realpath /usr/bin/python3)|" \
%if %{_plv} == %{_sonum}
        %{buildroot}%{_bindir}/{{analyze,intercept}-build,clang-{format,tidy}-diff,git-clang-format,hmaptool,run-{clang-tidy,find-all-symbols},scan-{build,build-py,view}} \
        %{buildroot}%{_libexecdir_fallback}/{{analyze,intercept}-{c++,cc},{c++,ccc}-analyzer} \
%endif
%ifarch aarch64 x86_64
        %{buildroot}%{_libdir}/clang/%{_relver}/bin/hwasan_symbolize \
%endif
        %{buildroot}%{_bindir}/opt-{diff,stats,viewer}

# Remove shebangs where not needed.
sed -i '1{ /^#!/d }' \
%if %{_plv} == %{_sonum}
    %{buildroot}%{_datadir}/scan-view/{Reporter,startfile}.py \
%endif
%if %{with lldb_python}
    %{buildroot}%{python3_sitearch}/lldb/utils/{in_call_stack,symbolication}.py \
%endif
    %{buildroot}%{python3_sitelib}/optrecord.py

# Remove executable bit where not needed.
chmod -x \
  %{buildroot}%{python3_sitelib}/opt{pmap,record}.py \
  %{buildroot}%{_datadir}/opt-viewer/style.css \
%if %{_plv} == %{_sonum}
  %{buildroot}%{_datadir}/bash-completion/completions/clang \
  %{buildroot}%{_datadir}/clang/clang-{format,include-fixer,rename}.{el,py} \
  %{buildroot}%{_mandir}/man1/scan-build.1
find %{buildroot}%{_prefix}/lib/{libear,libscanbuild} -type f -executable -exec chmod -x {} +
%endif

%fdupes -s %{buildroot}%{_docdir}/llvm
%fdupes -s %{buildroot}%{_docdir}/llvm-clang
%fdupes %{_includedir}/%{name}/Host/

%check
# We don't want to set RUNPATHs, and running tests against installed libraries
# should be more representative of the actual behavior of the installed packages.
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
# LLVM test suite is written in python and has troubles with encoding if
# python 3 is used because it is written with assumption that python will
# default to UTF-8 encoding. However, it only does if the current locale is
# UTF-8.
export LANG=C.UTF-8

# NOTE: We're not running the tests via ninja, because we've removed object
# files and static libraries already.
pushd build
%if !0%{?qemu_user_space_build:1}
# we just do not have enough memory with qemu emulation

# On armv6l, fpext frem(12.0f, 5.0f) to double = inf for some reason. On ppc relocation errors.
sed -i '1i; XFAIL: armv6, powerpc-' ../test/ExecutionEngine/frem.ll
# Disable tests that seem to hang (armv6) or fail with relocation errors (ppc).
sed -i '1i; UNSUPPORTED: armv6' ../test/CodeGen/Generic/PBQP.ll
sed -i '1i; UNSUPPORTED: armv6\n; XFAIL: powerpc-' \
  ../test/ExecutionEngine/{mov64zext32,test-interp-vec-{arithm_{float,int},logical,setcond-{fp,int}}}.ll
# Missing DW_TAG_formal_parameter. Test has been moved to X86 in the meantime (https://reviews.llvm.org/D109806).
sed -i '1i; XFAIL: powerpc64le-' ../test/DebugInfo/Generic/missing-abstract-variable.ll
%ifarch ppc64le
# Sporadic failures, possibly races?
rm ../test/tools/llvm-cov/{multithreaded-report,sources-specified}.test
%endif
python3 bin/llvm-lit -sv test/

# On s390x, this test complains that a required pass couldn't be found and then crashes. (FIXME)
sed -i '/XFAIL/i// XFAIL: s390x' ../tools/clang/test/CodeGen/sanitize-coverage-old-pm.c
# On ppc, this test fails with "fatal error: error in backend: Relocation type not implemented yet!"
sed -i '/UNSUPPORTED/i// XFAIL: powerpc-' ../tools/clang/test/Interpreter/execute.cpp
# Tests hang on armv6l.
sed -i '1i// UNSUPPORTED: armv6' \
  ../tools/clang/test/{Interpreter/execute.cpp,Modules/{preprocess-{build-diamond.m,decluse.cpp,module.cpp},string_names.cpp}}
%ifarch ppc64le
# Sporadic failures, possibly races?
rm -r ../tools/clang/test/ClangScanDeps
%endif
python3 bin/llvm-lit -sv --param clang_site_config=tools/clang/test/lit.site.cfg \
	--param USE_Z3_SOLVER=0 tools/clang/test/

%if %{with libcxx}
# libcxx tests run too long for what they're worth to us.
# So let's just run them for new versions only.
%if 0
# FIXME: investigate those
sed -i '1i# XFAIL: *' ../projects/libcxx/test/libcxx/selftest/dsl/dsl.sh.py
# Several tests seem to hang on armv6l.
sed -i '1i// UNSUPPORTED: armv6' \
  ../projects/libcxx/test/libcxx/utilities/memory/util.smartptr/race_condition.pass.cpp \
  ../projects/libcxx/test/std/utilities/memory/util.smartptr/util.smartptr.{enab/enable_shared_from_this,shared/util.smartptr.shared.const/{deduction,weak_ptr},weak/util.smartptr.weak.{const/shared_ptr_deduction,mod/swap,obs/lock,spec/swap}}.pass.cpp
python3 bin/llvm-lit -sv projects/libcxx/test/
%endif

# There are undefined references to __cxa_* functions and "typeinfo for int".
sed -i '1i@ XFAIL: arm' ../projects/libcxxabi/test/native/arm-linux-eabi/ttype-encoding-{0,9}0.pass.sh.s
python3 bin/llvm-lit -sv projects/libcxxabi/test/
%endif
%endif
popd

# Remove files that won't be needed anymore.
# This reduces the total amount of disk space used during build. (bnc#1074625)
# This is meant to happen after build, install and check, but before
# creating the final RPMs.
rm -rf ./stage1 ./build

%post -n libLLVM%{_sonum} -p /sbin/ldconfig
%postun -n libLLVM%{_sonum} -p /sbin/ldconfig
%post %{multisource libclang%{_soclang}} libclang%{_soclang} -p /sbin/ldconfig
%postun %{multisource libclang%{_soclang}} libclang%{_soclang} -p /sbin/ldconfig
%post -n libclang-cpp%{_sonum} -p /sbin/ldconfig
%postun -n libclang-cpp%{_sonum} -p /sbin/ldconfig
%post -n libLTO%{_sonum} -p /sbin/ldconfig
%postun -n libLTO%{_sonum} -p /sbin/ldconfig
%post -n clang%{_sonum}-devel -p /sbin/ldconfig
%postun -n clang%{_sonum}-devel -p /sbin/ldconfig

%if %{with lldb}
%post -n liblldb%{_sonum} -p /sbin/ldconfig
%postun -n liblldb%{_sonum} -p /sbin/ldconfig
%endif

%post gold -p /sbin/ldconfig
%postun gold -p /sbin/ldconfig
%post devel -p /sbin/ldconfig
%postun devel -p /sbin/ldconfig

%if %{with openmp}
%post -n libomp%{_sonum}-devel -p /sbin/ldconfig
%postun -n libomp%{_sonum}-devel -p /sbin/ldconfig
%endif

%if %{with libcxx}
%post %{multisource libcxx%{_socxx}} libc++%{_socxx} -p /sbin/ldconfig
%postun %{multisource libcxx%{_socxx}} libc++%{_socxx} -p /sbin/ldconfig
%post %{multisource libcxxabi%{_socxx}} libc++abi%{_socxx} -p /sbin/ldconfig
%postun %{multisource libcxxabi%{_socxx}} libc++abi%{_socxx} -p /sbin/ldconfig
%post %{multisource libcxx_devel} libc++-devel -p /sbin/ldconfig
%postun %{multisource libcxx_devel} libc++-devel -p /sbin/ldconfig
%post %{multisource libcxx_devel} libc++abi-devel -p /sbin/ldconfig
%postun %{multisource libcxx_devel} libc++abi-devel -p /sbin/ldconfig
%endif

%if %{with polly}
%post polly -p /sbin/ldconfig
%postun polly -p /sbin/ldconfig
%post polly-devel -p /sbin/ldconfig
%postun polly-devel -p /sbin/ldconfig
%endif

%post
%{_sbindir}/update-alternatives \
   --install %{_bindir}/llvm-ar llvm-ar %{_bindir}/llvm-ar-%{_relver} %{_uaver} \
   --slave %{_bindir}/bugpoint bugpoint %{_bindir}/bugpoint-%{_relver} \
   --slave %{_bindir}/dsymutil dsymutil %{_bindir}/dsymutil-%{_relver} \
   --slave %{_bindir}/llc llc %{_bindir}/llc-%{_relver} \
   --slave %{_bindir}/lli lli %{_bindir}/lli-%{_relver} \
   --slave %{_bindir}/llvm-addr2line llvm-addr2line %{_bindir}/llvm-addr2line-%{_relver} \
   --slave %{_bindir}/llvm-as llvm-as %{_bindir}/llvm-as-%{_relver} \
   --slave %{_bindir}/llvm-bcanalyzer llvm-bcanalyzer %{_bindir}/llvm-bcanalyzer-%{_relver} \
   --slave %{_bindir}/llvm-bitcode-strip llvm-bitcode-strip %{_bindir}/llvm-bitcode-strip-%{_relver} \
   --slave %{_bindir}/llvm-c-test llvm-c-test %{_bindir}/llvm-c-test-%{_relver} \
   --slave %{_bindir}/llvm-cat llvm-cat %{_bindir}/llvm-cat-%{_relver} \
   --slave %{_bindir}/llvm-cfi-verify llvm-cfi-verify %{_bindir}/llvm-cfi-verify-%{_relver} \
   --slave %{_bindir}/llvm-cov llvm-cov %{_bindir}/llvm-cov-%{_relver} \
   --slave %{_bindir}/llvm-cvtres llvm-cvtres %{_bindir}/llvm-cvtres-%{_relver} \
   --slave %{_bindir}/llvm-cxxdump llvm-cxxdump %{_bindir}/llvm-cxxdump-%{_relver} \
   --slave %{_bindir}/llvm-cxxfilt llvm-cxxfilt %{_bindir}/llvm-cxxfilt-%{_relver} \
   --slave %{_bindir}/llvm-cxxmap llvm-cxxmap %{_bindir}/llvm-cxxmap-%{_relver} \
   --slave %{_bindir}/llvm-diff llvm-diff %{_bindir}/llvm-diff-%{_relver} \
   --slave %{_bindir}/llvm-dis llvm-dis %{_bindir}/llvm-dis-%{_relver} \
   --slave %{_bindir}/llvm-dlltool llvm-dlltool %{_bindir}/llvm-dlltool-%{_relver} \
   --slave %{_bindir}/llvm-dwarfdump llvm-dwarfdump %{_bindir}/llvm-dwarfdump-%{_relver} \
   --slave %{_bindir}/llvm-dwp llvm-dwp %{_bindir}/llvm-dwp-%{_relver} \
   --slave %{_bindir}/llvm-exegesis llvm-exegesis %{_bindir}/llvm-exegesis-%{_relver} \
   --slave %{_bindir}/llvm-extract llvm-extract %{_bindir}/llvm-extract-%{_relver} \
   --slave %{_bindir}/llvm-gsymutil llvm-gsymutil %{_bindir}/llvm-gsymutil-%{_relver} \
   --slave %{_bindir}/llvm-ifs llvm-ifs %{_bindir}/llvm-ifs-%{_relver} \
   --slave %{_bindir}/llvm-install-name-tool llvm-install-name-tool %{_bindir}/llvm-install-name-tool-%{_relver} \
   --slave %{_bindir}/llvm-jitlink llvm-jitlink %{_bindir}/llvm-jitlink-%{_relver} \
   --slave %{_bindir}/llvm-lib llvm-lib %{_bindir}/llvm-lib-%{_relver} \
   --slave %{_bindir}/llvm-libtool-darwin llvm-libtool-darwin %{_bindir}/llvm-libtool-darwin-%{_relver} \
   --slave %{_bindir}/llvm-link llvm-link %{_bindir}/llvm-link-%{_relver} \
   --slave %{_bindir}/llvm-lipo llvm-lipo %{_bindir}/llvm-lipo-%{_relver} \
   --slave %{_bindir}/llvm-lto llvm-lto %{_bindir}/llvm-lto-%{_relver} \
   --slave %{_bindir}/llvm-lto2 llvm-lto2 %{_bindir}/llvm-lto2-%{_relver} \
   --slave %{_bindir}/llvm-mc llvm-mc %{_bindir}/llvm-mc-%{_relver} \
   --slave %{_bindir}/llvm-mca llvm-mca %{_bindir}/llvm-mca-%{_relver} \
   --slave %{_bindir}/llvm-ml llvm-ml %{_bindir}/llvm-ml-%{_relver} \
   --slave %{_bindir}/llvm-mt llvm-mt %{_bindir}/llvm-mt-%{_relver} \
   --slave %{_bindir}/llvm-modextract llvm-modextract %{_bindir}/llvm-modextract-%{_relver} \
   --slave %{_bindir}/llvm-nm llvm-nm %{_bindir}/llvm-nm-%{_relver} \
   --slave %{_bindir}/llvm-objcopy llvm-objcopy %{_bindir}/llvm-objcopy-%{_relver} \
   --slave %{_bindir}/llvm-objdump llvm-objdump %{_bindir}/llvm-objdump-%{_relver} \
   --slave %{_bindir}/llvm-opt-report llvm-opt-report %{_bindir}/llvm-opt-report-%{_relver} \
   --slave %{_bindir}/llvm-otool llvm-otool %{_bindir}/llvm-otool-%{_relver} \
   --slave %{_bindir}/llvm-pdbutil llvm-pdbutil %{_bindir}/llvm-pdbutil-%{_relver} \
   --slave %{_bindir}/llvm-profdata llvm-profdata %{_bindir}/llvm-profdata-%{_relver} \
   --slave %{_bindir}/llvm-profgen llvm-profgen %{_bindir}/llvm-profgen-%{_relver} \
   --slave %{_bindir}/llvm-ranlib llvm-ranlib %{_bindir}/llvm-ranlib-%{_relver} \
   --slave %{_bindir}/llvm-rc llvm-rc %{_bindir}/llvm-rc-%{_relver} \
   --slave %{_bindir}/llvm-readelf llvm-readelf %{_bindir}/llvm-readelf-%{_relver} \
   --slave %{_bindir}/llvm-readobj llvm-readobj %{_bindir}/llvm-readobj-%{_relver} \
   --slave %{_bindir}/llvm-reduce llvm-reduce %{_bindir}/llvm-reduce-%{_relver} \
   --slave %{_bindir}/llvm-rtdyld llvm-rtdyld %{_bindir}/llvm-rtdyld-%{_relver} \
   --slave %{_bindir}/llvm-sim llvm-sim %{_bindir}/llvm-sim-%{_relver} \
   --slave %{_bindir}/llvm-size llvm-size %{_bindir}/llvm-size-%{_relver} \
   --slave %{_bindir}/llvm-split llvm-split %{_bindir}/llvm-split-%{_relver} \
   --slave %{_bindir}/llvm-stress llvm-stress %{_bindir}/llvm-stress-%{_relver} \
   --slave %{_bindir}/llvm-strings llvm-strings %{_bindir}/llvm-strings-%{_relver} \
   --slave %{_bindir}/llvm-strip llvm-strip %{_bindir}/llvm-strip-%{_relver} \
   --slave %{_bindir}/llvm-symbolizer llvm-symbolizer %{_bindir}/llvm-symbolizer-%{_relver} \
   --slave %{_bindir}/llvm-tapi-diff llvm-tapi-diff %{_bindir}/llvm-tapi-diff-%{_relver} \
   --slave %{_bindir}/llvm-tblgen llvm-tblgen %{_bindir}/llvm-tblgen-%{_relver} \
   --slave %{_bindir}/llvm-undname llvm-undname %{_bindir}/llvm-undname-%{_relver} \
   --slave %{_bindir}/llvm-windres llvm-windres %{_bindir}/llvm-windres-%{_relver} \
   --slave %{_bindir}/llvm-xray llvm-xray %{_bindir}/llvm-xray-%{_relver} \
   --slave %{_bindir}/opt opt %{_bindir}/opt-%{_relver} \
   --slave %{_bindir}/sancov sancov %{_bindir}/sancov-%{_relver} \
   --slave %{_bindir}/sanstats sanstats %{_bindir}/sanstats-%{_relver} \
   --slave %{_bindir}/split-file split-file %{_bindir}/split-file-%{_relver} \
   --slave %{_bindir}/verify-uselistorder verify-uselistorder %{_bindir}/verify-uselistorder-%{_relver} \
   --slave %{_mandir}/man1/bugpoint.1%{ext_man} bugpoint.1%{ext_man} %{_mandir}/man1/bugpoint-%{_relver}.1%{ext_man} \
   --slave %{_mandir}/man1/dsymutil.1%{ext_man} dsymutil.1%{ext_man} %{_mandir}/man1/dsymutil-%{_relver}.1%{ext_man} \
   --slave %{_mandir}/man1/llc.1%{ext_man} llc.1%{ext_man} %{_mandir}/man1/llc-%{_relver}.1%{ext_man} \
   --slave %{_mandir}/man1/lli.1%{ext_man} lli.1%{ext_man} %{_mandir}/man1/lli-%{_relver}.1%{ext_man} \
   --slave %{_mandir}/man1/llvm-addr2line.1%{ext_man} llvm-addr2line.1%{ext_man} %{_mandir}/man1/llvm-addr2line-%{_relver}.1%{ext_man} \
   --slave %{_mandir}/man1/llvm-ar.1%{ext_man} llvm-ar.1%{ext_man} %{_mandir}/man1/llvm-ar-%{_relver}.1%{ext_man} \
   --slave %{_mandir}/man1/llvm-as.1%{ext_man} llvm-as.1%{ext_man} %{_mandir}/man1/llvm-as-%{_relver}.1%{ext_man} \
   --slave %{_mandir}/man1/llvm-bcanalyzer.1%{ext_man} llvm-bcanalyzer.1%{ext_man} %{_mandir}/man1/llvm-bcanalyzer-%{_relver}.1%{ext_man} \
   --slave %{_mandir}/man1/llvm-cov.1%{ext_man} llvm-cov.1%{ext_man} %{_mandir}/man1/llvm-cov-%{_relver}.1%{ext_man} \
   --slave %{_mandir}/man1/llvm-cxxfilt.1%{ext_man} llvm-cxxfilt.1%{ext_man} %{_mandir}/man1/llvm-cxxfilt-%{_relver}.1%{ext_man} \
   --slave %{_mandir}/man1/llvm-cxxmap.1%{ext_man} llvm-cxxmap.1%{ext_man} %{_mandir}/man1/llvm-cxxmap-%{_relver}.1%{ext_man} \
   --slave %{_mandir}/man1/llvm-diff.1%{ext_man} llvm-diff.1%{ext_man} %{_mandir}/man1/llvm-diff-%{_relver}.1%{ext_man} \
   --slave %{_mandir}/man1/llvm-dis.1%{ext_man} llvm-dis.1%{ext_man} %{_mandir}/man1/llvm-dis-%{_relver}.1%{ext_man} \
   --slave %{_mandir}/man1/llvm-dwarfdump.1%{ext_man} llvm-dwarfdump.1%{ext_man} %{_mandir}/man1/llvm-dwarfdump-%{_relver}.1%{ext_man} \
   --slave %{_mandir}/man1/llvm-exegesis.1%{ext_man} llvm-exegesis.1%{ext_man} %{_mandir}/man1/llvm-exegesis-%{_relver}.1%{ext_man} \
   --slave %{_mandir}/man1/llvm-extract.1%{ext_man} llvm-extract.1%{ext_man} %{_mandir}/man1/llvm-extract-%{_relver}.1%{ext_man} \
   --slave %{_mandir}/man1/llvm-install-name-tool.1%{ext_man} llvm-install-name-tool.1%{ext_man} %{_mandir}/man1/llvm-install-name-tool-%{_relver}.1%{ext_man} \
   --slave %{_mandir}/man1/llvm-lib.1%{ext_man} llvm-lib.1%{ext_man} %{_mandir}/man1/llvm-lib-%{_relver}.1%{ext_man} \
   --slave %{_mandir}/man1/llvm-libtool-darwin.1%{ext_man} llvm-libtool-darwin.1%{ext_man} %{_mandir}/man1/llvm-libtool-darwin-%{_relver}.1%{ext_man} \
   --slave %{_mandir}/man1/llvm-link.1%{ext_man} llvm-link.1%{ext_man} %{_mandir}/man1/llvm-link-%{_relver}.1%{ext_man} \
   --slave %{_mandir}/man1/llvm-lipo.1%{ext_man} llvm-lipo.1%{ext_man} %{_mandir}/man1/llvm-lipo-%{_relver}.1%{ext_man} \
   --slave %{_mandir}/man1/llvm-mca.1%{ext_man} llvm-mca.1%{ext_man} %{_mandir}/man1/llvm-mca-%{_relver}.1%{ext_man} \
   --slave %{_mandir}/man1/llvm-nm.1%{ext_man} llvm-nm.1%{ext_man} %{_mandir}/man1/llvm-nm-%{_relver}.1%{ext_man} \
   --slave %{_mandir}/man1/llvm-objcopy.1%{ext_man} llvm-objcopy.1%{ext_man} %{_mandir}/man1/llvm-objcopy-%{_relver}.1%{ext_man} \
   --slave %{_mandir}/man1/llvm-objdump.1%{ext_man} llvm-objdump.1%{ext_man} %{_mandir}/man1/llvm-objdump-%{_relver}.1%{ext_man} \
   --slave %{_mandir}/man1/llvm-otool.1%{ext_man} llvm-otool.1%{ext_man} %{_mandir}/man1/llvm-otool-%{_relver}.1%{ext_man} \
   --slave %{_mandir}/man1/llvm-pdbutil.1%{ext_man} llvm-pdbutil.1%{ext_man} %{_mandir}/man1/llvm-pdbutil-%{_relver}.1%{ext_man} \
   --slave %{_mandir}/man1/llvm-profdata.1%{ext_man} llvm-profdata.1%{ext_man} %{_mandir}/man1/llvm-profdata-%{_relver}.1%{ext_man} \
   --slave %{_mandir}/man1/llvm-profgen.1%{ext_man} llvm-profgen.1%{ext_man} %{_mandir}/man1/llvm-profgen-%{_relver}.1%{ext_man} \
   --slave %{_mandir}/man1/llvm-ranlib.1%{ext_man} llvm-ranlib.1%{ext_man} %{_mandir}/man1/llvm-ranlib-%{_relver}.1%{ext_man} \
   --slave %{_mandir}/man1/llvm-readelf.1%{ext_man} llvm-readelf.1%{ext_man} %{_mandir}/man1/llvm-readelf-%{_relver}.1%{ext_man} \
   --slave %{_mandir}/man1/llvm-readobj.1%{ext_man} llvm-readobj.1%{ext_man} %{_mandir}/man1/llvm-readobj-%{_relver}.1%{ext_man} \
   --slave %{_mandir}/man1/llvm-size.1%{ext_man} llvm-size.1%{ext_man} %{_mandir}/man1/llvm-size-%{_relver}.1%{ext_man} \
   --slave %{_mandir}/man1/llvm-stress.1%{ext_man} llvm-stress.1%{ext_man} %{_mandir}/man1/llvm-stress-%{_relver}.1%{ext_man} \
   --slave %{_mandir}/man1/llvm-strings.1%{ext_man} llvm-strings.1%{ext_man} %{_mandir}/man1/llvm-strings-%{_relver}.1%{ext_man} \
   --slave %{_mandir}/man1/llvm-strip.1%{ext_man} llvm-strip.1%{ext_man} %{_mandir}/man1/llvm-strip-%{_relver}.1%{ext_man} \
   --slave %{_mandir}/man1/llvm-symbolizer.1%{ext_man} llvm-symbolizer.1%{ext_man} %{_mandir}/man1/llvm-symbolizer-%{_relver}.1%{ext_man} \
   --slave %{_mandir}/man1/llvm-tblgen.1%{ext_man} llvm-tblgen.1%{ext_man} %{_mandir}/man1/llvm-tblgen-%{_relver}.1%{ext_man} \
   --slave %{_mandir}/man1/opt.1%{ext_man} opt.1%{ext_man} %{_mandir}/man1/opt-%{_relver}.1%{ext_man}

%postun
if [ ! -f %{_bindir}/llvm-ar-%{_relver} ] ; then
    %{_sbindir}/update-alternatives --remove llvm-ar %{_bindir}/llvm-ar-%{_relver}
fi

%post -n clang%{_sonum}
%{_sbindir}/update-alternatives \
   --install %{_bindir}/clang clang %{_bindir}/clang-%{_relver} %{_uaver} \
   --slave %{_bindir}/clangd clangd %{_bindir}/clangd-%{_relver} \
   --slave %{_bindir}/c-index-test c-index-test %{_bindir}/c-index-test-%{_relver} \
   --slave %{_bindir}/clang++ clang++ %{_bindir}/clang++-%{_relver} \
   --slave %{_bindir}/clang-apply-replacements clang-apply-replacements %{_bindir}/clang-apply-replacements-%{_relver} \
   --slave %{_bindir}/clang-change-namespace clang-change-namespace %{_bindir}/clang-change-namespace-%{_relver} \
   --slave %{_bindir}/clang-check clang-check %{_bindir}/clang-check-%{_relver} \
   --slave %{_bindir}/clang-cl clang-cl %{_bindir}/clang-cl-%{_relver} \
   --slave %{_bindir}/clang-cpp clang-cpp %{_bindir}/clang-cpp-%{_relver} \
   --slave %{_bindir}/clang-extdef-mapping clang-extdef-mapping %{_bindir}/clang-extdef-mapping-%{_relver} \
   --slave %{_bindir}/clang-format clang-format %{_bindir}/clang-format-%{_relver} \
   --slave %{_bindir}/clang-include-fixer clang-include-fixer %{_bindir}/clang-include-fixer-%{_relver} \
   --slave %{_bindir}/clang-move clang-move %{_bindir}/clang-move-%{_relver} \
   --slave %{_bindir}/clang-offload-bundler clang-offload-bundler %{_bindir}/clang-offload-bundler-%{_relver} \
   --slave %{_bindir}/clang-offload-wrapper clang-offload-wrapper %{_bindir}/clang-offload-wrapper-%{_relver} \
   --slave %{_bindir}/clang-query clang-query %{_bindir}/clang-query-%{_relver} \
   --slave %{_bindir}/clang-refactor clang-refactor %{_bindir}/clang-refactor-%{_relver} \
   --slave %{_bindir}/clang-repl clang-repl %{_bindir}/clang-repl-%{_relver} \
   --slave %{_bindir}/clang-rename clang-rename %{_bindir}/clang-rename-%{_relver} \
   --slave %{_bindir}/clang-reorder-fields clang-reorder-fields %{_bindir}/clang-reorder-fields-%{_relver} \
   --slave %{_bindir}/clang-scan-deps clang-scan-deps %{_bindir}/clang-scan-deps-%{_relver} \
   --slave %{_bindir}/clang-tidy clang-tidy %{_bindir}/clang-tidy-%{_relver} \
   --slave %{_bindir}/diagtool diagtool %{_bindir}/diagtool-%{_relver} \
   --slave %{_bindir}/find-all-symbols find-all-symbols %{_bindir}/find-all-symbols-%{_relver} \
   --slave %{_bindir}/modularize modularize %{_bindir}/modularize-%{_relver} \
   --slave %{_bindir}/pp-trace pp-trace %{_bindir}/pp-trace-%{_relver} \
   --slave %{_mandir}/man1/clang.1%{ext_man} clang.1%{ext_man} %{_mandir}/man1/clang-%{_relver}.1%{ext_man} \
   --slave %{_mandir}/man1/diagtool.1%{ext_man} diagtool.1%{ext_man} %{_mandir}/man1/diagtool-%{_relver}.1%{ext_man}

%postun -n clang%{_sonum}
if [ ! -f %{_bindir}/clang-%{_relver} ] ; then
    %{_sbindir}/update-alternatives --remove clang %{_bindir}/clang-%{_relver}
fi

%if %{with lld}
%post -n lld%{_sonum}
%{_sbindir}/update-alternatives \
   --install %{_bindir}/lld lld %{_bindir}/lld-%{_relver} %{_uaver} \
   --slave %{_bindir}/ld.lld ld.lld %{_bindir}/ld.lld-%{_relver} \
   --slave %{_bindir}/ld64.lld ld64.lld %{_bindir}/ld64.lld-%{_relver} \
   --slave %{_bindir}/ld64.lld.darwinnew ld64.lld.darwinnew %{_bindir}/ld64.lld.darwinnew-%{_relver} \
   --slave %{_bindir}/ld64.lld.darwinold ld64.lld.darwinold %{_bindir}/ld64.lld.darwinold-%{_relver} \
   --slave %{_bindir}/lld-link lld-link %{_bindir}/lld-link-%{_relver} \
   --slave %{_bindir}/wasm-ld wasm-ld %{_bindir}/wasm-ld-%{_relver}
%{_sbindir}/update-alternatives --install %{_bindir}/ld ld %{_bindir}/ld.lld 1

%postun -n lld%{_sonum}
if [ ! -f %{_bindir}/lld-%{_relver} ] ; then
    %{_sbindir}/update-alternatives --remove lld %{_bindir}/lld-%{_relver}
fi
if [ ! -f %{_bindir}/lld ] ; then
    %{_sbindir}/update-alternatives --remove ld %{_bindir}/ld.lld
fi
%endif

%if %{with lldb}
%post -n lldb%{_sonum}
%_sbindir/update-alternatives \
   --install %{_bindir}/lldb lldb %{_bindir}/lldb-%{_relver} %{_uaver} \
   --slave %{_bindir}/lldb-argdumper lldb-argdumper %{_bindir}/lldb-argdumper-%{_relver} \
   --slave %{_bindir}/lldb-instr lldb-instr %{_bindir}/lldb-instr-%{_relver} \
   --slave %{_bindir}/lldb-server lldb-server %{_bindir}/lldb-server-%{_relver} \
   --slave %{_bindir}/lldb-vscode lldb-vscode %{_bindir}/lldb-vscode-%{_relver}

%postun -n lldb%{_sonum}
if [ $1 -eq 0 ] ; then
    %_sbindir/update-alternatives --remove lldb %{_bindir}/lldb-%{_relver}
fi
%endif

%files
%license CREDITS.TXT LICENSE.TXT

%{_bindir}/bugpoint
%{_bindir}/dsymutil
%{_bindir}/llc
%{_bindir}/lli
%{_bindir}/llvm-addr2line
%{_bindir}/llvm-ar
%{_bindir}/llvm-as
%{_bindir}/llvm-bcanalyzer
%{_bindir}/llvm-bitcode-strip
%{_bindir}/llvm-c-test
%{_bindir}/llvm-cat
%{_bindir}/llvm-cfi-verify
%{_bindir}/llvm-cov
%{_bindir}/llvm-cvtres
%{_bindir}/llvm-cxxdump
%{_bindir}/llvm-cxxfilt
%{_bindir}/llvm-cxxmap
%{_bindir}/llvm-diff
%{_bindir}/llvm-dis
%{_bindir}/llvm-dlltool
%{_bindir}/llvm-dwarfdump
%{_bindir}/llvm-dwp
%{_bindir}/llvm-exegesis
%{_bindir}/llvm-extract
%{_bindir}/llvm-gsymutil
%{_bindir}/llvm-ifs
%{_bindir}/llvm-install-name-tool
%{_bindir}/llvm-jitlink
%{_bindir}/llvm-lib
%{_bindir}/llvm-libtool-darwin
%{_bindir}/llvm-link
%{_bindir}/llvm-lipo
%{_bindir}/llvm-lto
%{_bindir}/llvm-lto2
%{_bindir}/llvm-mc
%{_bindir}/llvm-mca
%{_bindir}/llvm-ml
%{_bindir}/llvm-mt
%{_bindir}/llvm-modextract
%{_bindir}/llvm-nm
%{_bindir}/llvm-objcopy
%{_bindir}/llvm-objdump
%{_bindir}/llvm-opt-report
%{_bindir}/llvm-otool
%{_bindir}/llvm-pdbutil
%{_bindir}/llvm-profdata
%{_bindir}/llvm-profgen
%{_bindir}/llvm-ranlib
%{_bindir}/llvm-rc
%{_bindir}/llvm-readelf
%{_bindir}/llvm-readobj
%{_bindir}/llvm-reduce
%{_bindir}/llvm-rtdyld
%{_bindir}/llvm-sim
%{_bindir}/llvm-size
%{_bindir}/llvm-split
%{_bindir}/llvm-stress
%{_bindir}/llvm-strings
%{_bindir}/llvm-strip
%{_bindir}/llvm-symbolizer
%{_bindir}/llvm-tapi-diff
%{_bindir}/llvm-tblgen
%{_bindir}/llvm-undname
%{_bindir}/llvm-windres
%{_bindir}/llvm-xray
%{_bindir}/opt
%{_bindir}/sancov
%{_bindir}/sanstats
%{_bindir}/split-file
%{_bindir}/verify-uselistorder

%{_bindir}/bugpoint-%{_relver}
%{_bindir}/dsymutil-%{_relver}
%{_bindir}/llc-%{_relver}
%{_bindir}/lli-%{_relver}
%{_bindir}/llvm-addr2line-%{_relver}
%{_bindir}/llvm-ar-%{_relver}
%{_bindir}/llvm-as-%{_relver}
%{_bindir}/llvm-bcanalyzer-%{_relver}
%{_bindir}/llvm-bitcode-strip-%{_relver}
%{_bindir}/llvm-c-test-%{_relver}
%{_bindir}/llvm-cat-%{_relver}
%{_bindir}/llvm-cfi-verify-%{_relver}
%{_bindir}/llvm-cov-%{_relver}
%{_bindir}/llvm-cvtres-%{_relver}
%{_bindir}/llvm-cxxdump-%{_relver}
%{_bindir}/llvm-cxxfilt-%{_relver}
%{_bindir}/llvm-cxxmap-%{_relver}
%{_bindir}/llvm-diff-%{_relver}
%{_bindir}/llvm-dis-%{_relver}
%{_bindir}/llvm-dlltool-%{_relver}
%{_bindir}/llvm-dwarfdump-%{_relver}
%{_bindir}/llvm-dwp-%{_relver}
%{_bindir}/llvm-exegesis-%{_relver}
%{_bindir}/llvm-extract-%{_relver}
%{_bindir}/llvm-gsymutil-%{_relver}
%{_bindir}/llvm-ifs-%{_relver}
%{_bindir}/llvm-install-name-tool-%{_relver}
%{_bindir}/llvm-jitlink-%{_relver}
%{_bindir}/llvm-lib-%{_relver}
%{_bindir}/llvm-libtool-darwin-%{_relver}
%{_bindir}/llvm-link-%{_relver}
%{_bindir}/llvm-lipo-%{_relver}
%{_bindir}/llvm-lto-%{_relver}
%{_bindir}/llvm-lto2-%{_relver}
%{_bindir}/llvm-mc-%{_relver}
%{_bindir}/llvm-mca-%{_relver}
%{_bindir}/llvm-ml-%{_relver}
%{_bindir}/llvm-mt-%{_relver}
%{_bindir}/llvm-modextract-%{_relver}
%{_bindir}/llvm-nm-%{_relver}
%{_bindir}/llvm-objcopy-%{_relver}
%{_bindir}/llvm-objdump-%{_relver}
%{_bindir}/llvm-opt-report-%{_relver}
%{_bindir}/llvm-otool-%{_relver}
%{_bindir}/llvm-pdbutil-%{_relver}
%{_bindir}/llvm-profdata-%{_relver}
%{_bindir}/llvm-profgen-%{_relver}
%{_bindir}/llvm-ranlib-%{_relver}
%{_bindir}/llvm-rc-%{_relver}
%{_bindir}/llvm-readelf-%{_relver}
%{_bindir}/llvm-readobj-%{_relver}
%{_bindir}/llvm-reduce-%{_relver}
%{_bindir}/llvm-rtdyld-%{_relver}
%{_bindir}/llvm-sim-%{_relver}
%{_bindir}/llvm-size-%{_relver}
%{_bindir}/llvm-split-%{_relver}
%{_bindir}/llvm-stress-%{_relver}
%{_bindir}/llvm-strings-%{_relver}
%{_bindir}/llvm-strip-%{_relver}
%{_bindir}/llvm-symbolizer-%{_relver}
%{_bindir}/llvm-tapi-diff-%{_relver}
%{_bindir}/llvm-tblgen-%{_relver}
%{_bindir}/llvm-undname-%{_relver}
%{_bindir}/llvm-windres-%{_relver}
%{_bindir}/llvm-xray-%{_relver}
%{_bindir}/opt-%{_relver}
%{_bindir}/sancov-%{_relver}
%{_bindir}/sanstats-%{_relver}
%{_bindir}/split-file-%{_relver}
%{_bindir}/verify-uselistorder-%{_relver}

%ghost %{_sysconfdir}/alternatives/bugpoint
%ghost %{_sysconfdir}/alternatives/dsymutil
%ghost %{_sysconfdir}/alternatives/llc
%ghost %{_sysconfdir}/alternatives/lli
%ghost %{_sysconfdir}/alternatives/llvm-addr2line
%ghost %{_sysconfdir}/alternatives/llvm-ar
%ghost %{_sysconfdir}/alternatives/llvm-as
%ghost %{_sysconfdir}/alternatives/llvm-bcanalyzer
%ghost %{_sysconfdir}/alternatives/llvm-bitcode-strip
%ghost %{_sysconfdir}/alternatives/llvm-c-test
%ghost %{_sysconfdir}/alternatives/llvm-cat
%ghost %{_sysconfdir}/alternatives/llvm-cfi-verify
%ghost %{_sysconfdir}/alternatives/llvm-cxxfilt
%ghost %{_sysconfdir}/alternatives/llvm-cxxmap
%ghost %{_sysconfdir}/alternatives/llvm-cov
%ghost %{_sysconfdir}/alternatives/llvm-cvtres
%ghost %{_sysconfdir}/alternatives/llvm-cxxdump
%ghost %{_sysconfdir}/alternatives/llvm-diff
%ghost %{_sysconfdir}/alternatives/llvm-dis
%ghost %{_sysconfdir}/alternatives/llvm-dlltool
%ghost %{_sysconfdir}/alternatives/llvm-dwarfdump
%ghost %{_sysconfdir}/alternatives/llvm-dwp
%ghost %{_sysconfdir}/alternatives/llvm-exegesis
%ghost %{_sysconfdir}/alternatives/llvm-extract
%ghost %{_sysconfdir}/alternatives/llvm-gsymutil
%ghost %{_sysconfdir}/alternatives/llvm-ifs
%ghost %{_sysconfdir}/alternatives/llvm-install-name-tool
%ghost %{_sysconfdir}/alternatives/llvm-jitlink
%ghost %{_sysconfdir}/alternatives/llvm-lib
%ghost %{_sysconfdir}/alternatives/llvm-libtool-darwin
%ghost %{_sysconfdir}/alternatives/llvm-link
%ghost %{_sysconfdir}/alternatives/llvm-lipo
%ghost %{_sysconfdir}/alternatives/llvm-lto
%ghost %{_sysconfdir}/alternatives/llvm-lto2
%ghost %{_sysconfdir}/alternatives/llvm-mc
%ghost %{_sysconfdir}/alternatives/llvm-mca
%ghost %{_sysconfdir}/alternatives/llvm-ml
%ghost %{_sysconfdir}/alternatives/llvm-mt
%ghost %{_sysconfdir}/alternatives/llvm-modextract
%ghost %{_sysconfdir}/alternatives/llvm-nm
%ghost %{_sysconfdir}/alternatives/llvm-objcopy
%ghost %{_sysconfdir}/alternatives/llvm-objdump
%ghost %{_sysconfdir}/alternatives/llvm-opt-report
%ghost %{_sysconfdir}/alternatives/llvm-otool
%ghost %{_sysconfdir}/alternatives/llvm-pdbutil
%ghost %{_sysconfdir}/alternatives/llvm-profdata
%ghost %{_sysconfdir}/alternatives/llvm-profgen
%ghost %{_sysconfdir}/alternatives/llvm-ranlib
%ghost %{_sysconfdir}/alternatives/llvm-rc
%ghost %{_sysconfdir}/alternatives/llvm-readelf
%ghost %{_sysconfdir}/alternatives/llvm-readobj
%ghost %{_sysconfdir}/alternatives/llvm-reduce
%ghost %{_sysconfdir}/alternatives/llvm-rtdyld
%ghost %{_sysconfdir}/alternatives/llvm-sim
%ghost %{_sysconfdir}/alternatives/llvm-size
%ghost %{_sysconfdir}/alternatives/llvm-split
%ghost %{_sysconfdir}/alternatives/llvm-stress
%ghost %{_sysconfdir}/alternatives/llvm-strings
%ghost %{_sysconfdir}/alternatives/llvm-strip
%ghost %{_sysconfdir}/alternatives/llvm-symbolizer
%ghost %{_sysconfdir}/alternatives/llvm-tapi-diff
%ghost %{_sysconfdir}/alternatives/llvm-tblgen
%ghost %{_sysconfdir}/alternatives/llvm-undname
%ghost %{_sysconfdir}/alternatives/llvm-windres
%ghost %{_sysconfdir}/alternatives/llvm-xray
%ghost %{_sysconfdir}/alternatives/opt
%ghost %{_sysconfdir}/alternatives/sancov
%ghost %{_sysconfdir}/alternatives/sanstats
%ghost %{_sysconfdir}/alternatives/split-file
%ghost %{_sysconfdir}/alternatives/verify-uselistorder

%{_mandir}/man1/bugpoint.1%{ext_man}
%{_mandir}/man1/dsymutil.1%{ext_man}
%{_mandir}/man1/llc.1%{ext_man}
%{_mandir}/man1/lli.1%{ext_man}
%{_mandir}/man1/llvm-addr2line.1%{ext_man}
%{_mandir}/man1/llvm-ar.1%{ext_man}
%{_mandir}/man1/llvm-as.1%{ext_man}
%{_mandir}/man1/llvm-bcanalyzer.1%{ext_man}
%{_mandir}/man1/llvm-cov.1%{ext_man}
%{_mandir}/man1/llvm-cxxfilt.1%{ext_man}
%{_mandir}/man1/llvm-cxxmap.1%{ext_man}
%{_mandir}/man1/llvm-diff.1%{ext_man}
%{_mandir}/man1/llvm-dis.1%{ext_man}
%{_mandir}/man1/llvm-dwarfdump.1%{ext_man}
%{_mandir}/man1/llvm-exegesis.1%{ext_man}
%{_mandir}/man1/llvm-extract.1%{ext_man}
%{_mandir}/man1/llvm-install-name-tool.1%{ext_man}
%{_mandir}/man1/llvm-lib.1%{ext_man}
%{_mandir}/man1/llvm-libtool-darwin.1%{ext_man}
%{_mandir}/man1/llvm-link.1%{ext_man}
%{_mandir}/man1/llvm-lipo.1%{ext_man}
%{_mandir}/man1/llvm-mca.1%{ext_man}
%{_mandir}/man1/llvm-nm.1%{ext_man}
%{_mandir}/man1/llvm-objcopy.1%{ext_man}
%{_mandir}/man1/llvm-objdump.1%{ext_man}
%{_mandir}/man1/llvm-otool.1%{ext_man}
%{_mandir}/man1/llvm-pdbutil.1%{ext_man}
%{_mandir}/man1/llvm-profdata.1%{ext_man}
%{_mandir}/man1/llvm-profgen.1%{ext_man}
%{_mandir}/man1/llvm-ranlib.1%{ext_man}
%{_mandir}/man1/llvm-readelf.1%{ext_man}
%{_mandir}/man1/llvm-readobj.1%{ext_man}
%{_mandir}/man1/llvm-size.1%{ext_man}
%{_mandir}/man1/llvm-stress.1%{ext_man}
%{_mandir}/man1/llvm-strings.1%{ext_man}
%{_mandir}/man1/llvm-strip.1%{ext_man}
%{_mandir}/man1/llvm-symbolizer.1%{ext_man}
%{_mandir}/man1/llvm-tblgen.1%{ext_man}
%{_mandir}/man1/opt.1%{ext_man}
%{_mandir}/man1/bugpoint-%{_relver}.1%{ext_man}
%{_mandir}/man1/dsymutil-%{_relver}.1%{ext_man}
%{_mandir}/man1/llc-%{_relver}.1%{ext_man}
%{_mandir}/man1/lli-%{_relver}.1%{ext_man}
%{_mandir}/man1/llvm-addr2line-%{_relver}.1%{ext_man}
%{_mandir}/man1/llvm-ar-%{_relver}.1%{ext_man}
%{_mandir}/man1/llvm-as-%{_relver}.1%{ext_man}
%{_mandir}/man1/llvm-bcanalyzer-%{_relver}.1%{ext_man}
%{_mandir}/man1/llvm-cov-%{_relver}.1%{ext_man}
%{_mandir}/man1/llvm-cxxfilt-%{_relver}.1%{ext_man}
%{_mandir}/man1/llvm-cxxmap-%{_relver}.1%{ext_man}
%{_mandir}/man1/llvm-diff-%{_relver}.1%{ext_man}
%{_mandir}/man1/llvm-dis-%{_relver}.1%{ext_man}
%{_mandir}/man1/llvm-dwarfdump-%{_relver}.1%{ext_man}
%{_mandir}/man1/llvm-exegesis-%{_relver}.1%{ext_man}
%{_mandir}/man1/llvm-extract-%{_relver}.1%{ext_man}
%{_mandir}/man1/llvm-install-name-tool-%{_relver}.1%{ext_man}
%{_mandir}/man1/llvm-lib-%{_relver}.1%{ext_man}
%{_mandir}/man1/llvm-libtool-darwin-%{_relver}.1%{ext_man}
%{_mandir}/man1/llvm-link-%{_relver}.1%{ext_man}
%{_mandir}/man1/llvm-lipo-%{_relver}.1%{ext_man}
%{_mandir}/man1/llvm-mca-%{_relver}.1%{ext_man}
%{_mandir}/man1/llvm-nm-%{_relver}.1%{ext_man}
%{_mandir}/man1/llvm-objcopy-%{_relver}.1%{ext_man}
%{_mandir}/man1/llvm-objdump-%{_relver}.1%{ext_man}
%{_mandir}/man1/llvm-otool-%{_relver}.1%{ext_man}
%{_mandir}/man1/llvm-pdbutil-%{_relver}.1%{ext_man}
%{_mandir}/man1/llvm-profdata-%{_relver}.1%{ext_man}
%{_mandir}/man1/llvm-profgen-%{_relver}.1%{ext_man}
%{_mandir}/man1/llvm-ranlib-%{_relver}.1%{ext_man}
%{_mandir}/man1/llvm-readelf-%{_relver}.1%{ext_man}
%{_mandir}/man1/llvm-readobj-%{_relver}.1%{ext_man}
%{_mandir}/man1/llvm-size-%{_relver}.1%{ext_man}
%{_mandir}/man1/llvm-stress-%{_relver}.1%{ext_man}
%{_mandir}/man1/llvm-strings-%{_relver}.1%{ext_man}
%{_mandir}/man1/llvm-strip-%{_relver}.1%{ext_man}
%{_mandir}/man1/llvm-symbolizer-%{_relver}.1%{ext_man}
%{_mandir}/man1/llvm-tblgen-%{_relver}.1%{ext_man}
%{_mandir}/man1/opt-%{_relver}.1%{ext_man}
%ghost %{_sysconfdir}/alternatives/bugpoint.1%{ext_man}
%ghost %{_sysconfdir}/alternatives/dsymutil.1%{ext_man}
%ghost %{_sysconfdir}/alternatives/llc.1%{ext_man}
%ghost %{_sysconfdir}/alternatives/lli.1%{ext_man}
%ghost %{_sysconfdir}/alternatives/llvm-addr2line.1%{ext_man}
%ghost %{_sysconfdir}/alternatives/llvm-ar.1%{ext_man}
%ghost %{_sysconfdir}/alternatives/llvm-as.1%{ext_man}
%ghost %{_sysconfdir}/alternatives/llvm-bcanalyzer.1%{ext_man}
%ghost %{_sysconfdir}/alternatives/llvm-cov.1%{ext_man}
%ghost %{_sysconfdir}/alternatives/llvm-cxxfilt.1%{ext_man}
%ghost %{_sysconfdir}/alternatives/llvm-cxxmap.1%{ext_man}
%ghost %{_sysconfdir}/alternatives/llvm-diff.1%{ext_man}
%ghost %{_sysconfdir}/alternatives/llvm-dis.1%{ext_man}
%ghost %{_sysconfdir}/alternatives/llvm-dwarfdump.1%{ext_man}
%ghost %{_sysconfdir}/alternatives/llvm-exegesis.1%{ext_man}
%ghost %{_sysconfdir}/alternatives/llvm-extract.1%{ext_man}
%ghost %{_sysconfdir}/alternatives/llvm-install-name-tool.1%{ext_man}
%ghost %{_sysconfdir}/alternatives/llvm-lib.1%{ext_man}
%ghost %{_sysconfdir}/alternatives/llvm-libtool-darwin.1%{ext_man}
%ghost %{_sysconfdir}/alternatives/llvm-link.1%{ext_man}
%ghost %{_sysconfdir}/alternatives/llvm-lipo.1%{ext_man}
%ghost %{_sysconfdir}/alternatives/llvm-mca.1%{ext_man}
%ghost %{_sysconfdir}/alternatives/llvm-nm.1%{ext_man}
%ghost %{_sysconfdir}/alternatives/llvm-objcopy.1%{ext_man}
%ghost %{_sysconfdir}/alternatives/llvm-objdump.1%{ext_man}
%ghost %{_sysconfdir}/alternatives/llvm-otool.1%{ext_man}
%ghost %{_sysconfdir}/alternatives/llvm-pdbutil.1%{ext_man}
%ghost %{_sysconfdir}/alternatives/llvm-profdata.1%{ext_man}
%ghost %{_sysconfdir}/alternatives/llvm-profgen.1%{ext_man}
%ghost %{_sysconfdir}/alternatives/llvm-ranlib.1%{ext_man}
%ghost %{_sysconfdir}/alternatives/llvm-readelf.1%{ext_man}
%ghost %{_sysconfdir}/alternatives/llvm-readobj.1%{ext_man}
%ghost %{_sysconfdir}/alternatives/llvm-size.1%{ext_man}
%ghost %{_sysconfdir}/alternatives/llvm-stress.1%{ext_man}
%ghost %{_sysconfdir}/alternatives/llvm-strings.1%{ext_man}
%ghost %{_sysconfdir}/alternatives/llvm-strip.1%{ext_man}
%ghost %{_sysconfdir}/alternatives/llvm-symbolizer.1%{ext_man}
%ghost %{_sysconfdir}/alternatives/llvm-tblgen.1%{ext_man}
%ghost %{_sysconfdir}/alternatives/opt.1%{ext_man}

%files -n clang%{_sonum}
%license CREDITS.TXT LICENSE.TXT
%{_bindir}/clang-%{_minor}
%{_bindir}/clang-%{_sonum}
%{_bindir}/clang++-%{_minor}
%{_bindir}/clang++-%{_sonum}
%{_bindir}/c-index-test
%{_bindir}/clang
%{_bindir}/clangd
%{_bindir}/clang++
%{_bindir}/clang-apply-replacements
%{_bindir}/clang-change-namespace
%{_bindir}/clang-check
%{_bindir}/clang-cl
%{_bindir}/clang-cpp
%{_bindir}/clang-extdef-mapping
%{_bindir}/clang-format
%{_bindir}/clang-include-fixer
%{_bindir}/clang-move
%{_bindir}/clang-offload-bundler
%{_bindir}/clang-offload-wrapper
%{_bindir}/clang-query
%{_bindir}/clang-refactor
%{_bindir}/clang-repl
%{_bindir}/clang-rename
%{_bindir}/clang-reorder-fields
%{_bindir}/clang-scan-deps
%{_bindir}/clang-tidy
%{_bindir}/diagtool
%{_bindir}/find-all-symbols
%{_bindir}/modularize
%{_bindir}/pp-trace
%{_bindir}/c-index-test-%{_relver}
%{_bindir}/clang-%{_relver}
%{_bindir}/clangd-%{_relver}
%{_bindir}/clang++-%{_relver}
%{_bindir}/clang-apply-replacements-%{_relver}
%{_bindir}/clang-change-namespace-%{_relver}
%{_bindir}/clang-check-%{_relver}
%{_bindir}/clang-cl-%{_relver}
%{_bindir}/clang-cpp-%{_relver}
%{_bindir}/clang-extdef-mapping-%{_relver}
%{_bindir}/clang-format-%{_relver}
%{_bindir}/clang-include-fixer-%{_relver}
%{_bindir}/clang-move-%{_relver}
%{_bindir}/clang-offload-bundler-%{_relver}
%{_bindir}/clang-offload-wrapper-%{_relver}
%{_bindir}/clang-query-%{_relver}
%{_bindir}/clang-refactor-%{_relver}
%{_bindir}/clang-repl-%{_relver}
%{_bindir}/clang-rename-%{_relver}
%{_bindir}/clang-reorder-fields-%{_relver}
%{_bindir}/clang-scan-deps-%{_relver}
%{_bindir}/clang-tidy-%{_relver}
%{_bindir}/diagtool-%{_relver}
%{_bindir}/find-all-symbols-%{_relver}
%{_bindir}/modularize-%{_relver}
%{_bindir}/pp-trace-%{_relver}
%ghost %{_sysconfdir}/alternatives/c-index-test
%ghost %{_sysconfdir}/alternatives/clang
%ghost %{_sysconfdir}/alternatives/clangd
%ghost %{_sysconfdir}/alternatives/clang++
%ghost %{_sysconfdir}/alternatives/clang-apply-replacements
%ghost %{_sysconfdir}/alternatives/clang-change-namespace
%ghost %{_sysconfdir}/alternatives/clang-check
%ghost %{_sysconfdir}/alternatives/clang-cl
%ghost %{_sysconfdir}/alternatives/clang-cpp
%ghost %{_sysconfdir}/alternatives/clang-extdef-mapping
%ghost %{_sysconfdir}/alternatives/clang-format
%ghost %{_sysconfdir}/alternatives/clang-include-fixer
%ghost %{_sysconfdir}/alternatives/clang-move
%ghost %{_sysconfdir}/alternatives/clang-offload-bundler
%ghost %{_sysconfdir}/alternatives/clang-offload-wrapper
%ghost %{_sysconfdir}/alternatives/clang-query
%ghost %{_sysconfdir}/alternatives/clang-refactor
%ghost %{_sysconfdir}/alternatives/clang-repl
%ghost %{_sysconfdir}/alternatives/clang-rename
%ghost %{_sysconfdir}/alternatives/clang-reorder-fields
%ghost %{_sysconfdir}/alternatives/clang-scan-deps
%ghost %{_sysconfdir}/alternatives/clang-tidy
%ghost %{_sysconfdir}/alternatives/diagtool
%ghost %{_sysconfdir}/alternatives/find-all-symbols
%ghost %{_sysconfdir}/alternatives/modularize
%ghost %{_sysconfdir}/alternatives/pp-trace
%{_mandir}/man1/clang.1%{ext_man}
%{_mandir}/man1/diagtool.1%{ext_man}
%{_mandir}/man1/clang-%{_relver}.1%{ext_man}
%{_mandir}/man1/diagtool-%{_relver}.1%{ext_man}
%ghost %{_sysconfdir}/alternatives/clang.1%{ext_man}
%ghost %{_sysconfdir}/alternatives/diagtool.1%{ext_man}
%dir %{_libdir}/clang/
%dir %{_libdir}/clang/%{_relver}/
%ifarch aarch64 x86_64
%{_libdir}/clang/%{_relver}/bin
%endif
# The sanitizer runtime is not available for ppc.
%ifnarch ppc
%{_libdir}/clang/%{_relver}/lib
%{_libdir}/clang/%{_relver}/share
%endif

%if %{_plv} == %{_sonum}
%files -n clang-tools
%license CREDITS.TXT LICENSE.TXT
%{_bindir}/analyze-build
%{_bindir}/clang-doc
%{_bindir}/clang-format-diff
%{_bindir}/clang-tidy-diff
%{_bindir}/git-clang-format
%{_bindir}/hmaptool
%{_bindir}/intercept-build
%{_bindir}/run-clang-tidy
%{_bindir}/run-find-all-symbols
%{_bindir}/scan-build
%{_bindir}/scan-build-py
%{_bindir}/scan-view
%{_libexecdir_fallback}/analyze-c++
%{_libexecdir_fallback}/analyze-cc
%{_libexecdir_fallback}/c++-analyzer
%{_libexecdir_fallback}/ccc-analyzer
%{_libexecdir_fallback}/intercept-c++
%{_libexecdir_fallback}/intercept-cc
%{_prefix}/lib/libear
%{_prefix}/lib/libscanbuild
%{_datadir}/bash-completion/completions/clang
%{_datadir}/clang/
%{_datadir}/scan-build/
%{_datadir}/scan-view/
%{_mandir}/man1/scan-build.1%{ext_man}
%endif

%files opt-viewer
%license CREDITS.TXT LICENSE.TXT
%{_bindir}/opt-diff
%{_bindir}/opt-stats
%{_bindir}/opt-viewer
%{python3_sitelib}/optpmap.py
%{python3_sitelib}/optrecord.py
%{_datadir}/opt-viewer/

%files -n libLLVM%{_sonum}
%license CREDITS.TXT LICENSE.TXT
%{_libdir}/libLLVM*.so.*
%{_libdir}/libRemarks.so.*

%files %{multisource libclang%{_soclang}} libclang%{_soclang}
%license CREDITS.TXT LICENSE.TXT
%{_libdir}/libclang.so.%{_soclang}
%{_libdir}/libclang.so.%{_relver}

%files -n libclang-cpp%{_sonum}
%license CREDITS.TXT LICENSE.TXT
%{_libdir}/libclang-cpp.so.%{_sonum}
%dir %{_libdir}/clang/
%dir %{_libdir}/clang/%{_relver}/
%{_libdir}/clang/%{_relver}/include

%files -n libLTO%{_sonum}
%license CREDITS.TXT LICENSE.TXT
%{_libdir}/libLTO.so.*

%files gold
%license CREDITS.TXT LICENSE.TXT
%{_libdir}/LLVMgold.so
# Note that bfd-plugins is in /usr/lib/bfd-plugins before binutils 2.33.1
%dir %{_libdir}/bfd-plugins/
%{_libdir}/bfd-plugins/LLVMgold.so

%if %{with openmp}
%files -n libomp%{_sonum}-devel
%license CREDITS.TXT LICENSE.TXT
%{_bindir}/llvm-omp-device-info
%{_includedir}/ompt-multiplex.h
%{_libdir}/libarcher.so
%{_libdir}/libomp.so
%{_libdir}/libomptarget.so
# TODO: Figure out why these architectures.
%ifarch aarch64 ppc64le x86_64
%{_libdir}/libomptarget-amdgcn-gfx*.bc
%endif
%{_libdir}/cmake/openmp
%endif

%if %{with libcxx}
%files %{multisource libcxx%{_socxx}} libc++%{_socxx}
%license CREDITS.TXT LICENSE.TXT
%{_libdir}/libc++.so.*

%files %{multisource libcxxabi%{_socxx}} libc++abi%{_socxx}
%license CREDITS.TXT LICENSE.TXT
%{_libdir}/libc++abi.so.*

%files %{multisource libcxx_devel} libc++-devel
%license CREDITS.TXT LICENSE.TXT
%{_libdir}/libc++.so
%dir %{_includedir}/c++/
%{_includedir}/c++/v%{_socxx}

%files %{multisource libcxx_devel} libc++abi-devel
%license CREDITS.TXT LICENSE.TXT
%{_libdir}/libc++abi.so
%endif

%files devel
%license CREDITS.TXT LICENSE.TXT
%{_bindir}/FileCheck
%{_bindir}/llvm-config
%{_libdir}/libLLVM.so
%{_libdir}/libLLVMTableGen.so
%{_libdir}/libLTO.so
%{_libdir}/libRemarks.so
%{_includedir}/llvm/
%{_includedir}/llvm-c/
%{_libdir}/cmake/llvm
%{_mandir}/man1/FileCheck.1%{ext_man}
%{_mandir}/man1/llvm-config.1%{ext_man}
%{_rpmconfigdir}/macros.d/macros.llvm

%files doc
%{_docdir}/llvm/

%files -n clang%{_sonum}-devel
%license CREDITS.TXT LICENSE.TXT
%{_libdir}/libclang*.so
%{_includedir}/clang/
%{_includedir}/clang-c/
%{_libdir}/cmake/clang

%files -n clang%{_sonum}-doc
%{_docdir}/llvm-clang/

%files vim-plugins
%license CREDITS.TXT LICENSE.TXT
%doc utils/vim/README.vim
%{_datadir}/vim/

%files -n python3-clang%{_sonum}
%license CREDITS.TXT LICENSE.TXT
%{python3_sitelib}/clang/
%{_docdir}/python-clang/

%if %{with lld}
%files -n lld%{_sonum}
%license CREDITS.TXT LICENSE.TXT
%{_bindir}/ld.lld
%{_bindir}/ld64.lld
%{_bindir}/ld64.lld.darwinnew
%{_bindir}/ld64.lld.darwinold
%{_bindir}/lld
%{_bindir}/lld-link
%{_bindir}/wasm-ld
%{_bindir}/ld.lld-%{_relver}
%{_bindir}/ld64.lld-%{_relver}
%{_bindir}/ld64.lld.darwinnew-%{_relver}
%{_bindir}/ld64.lld.darwinold-%{_relver}
%{_bindir}/lld-%{_relver}
%{_bindir}/lld-link-%{_relver}
%{_bindir}/wasm-ld-%{_relver}
%ghost %{_sysconfdir}/alternatives/ld.lld
%ghost %{_sysconfdir}/alternatives/ld64.lld
%ghost %{_sysconfdir}/alternatives/ld64.lld.darwinnew
%ghost %{_sysconfdir}/alternatives/ld64.lld.darwinold
%ghost %{_sysconfdir}/alternatives/lld
%ghost %{_sysconfdir}/alternatives/lld-link
%ghost %{_sysconfdir}/alternatives/wasm-ld
%endif

%if %{with lldb}
%files -n lldb%{_sonum}
%license CREDITS.TXT LICENSE.TXT
%{_bindir}/lldb
%{_bindir}/lldb-argdumper
%{_bindir}/lldb-instr
%{_bindir}/lldb-server
%{_bindir}/lldb-vscode
%{_bindir}/lldb-%{_relver}
%{_bindir}/lldb-argdumper-%{_relver}
%{_bindir}/lldb-instr-%{_relver}
%{_bindir}/lldb-server-%{_relver}
%{_bindir}/lldb-vscode-%{_relver}
%ghost %{_sysconfdir}/alternatives/lldb
%ghost %{_sysconfdir}/alternatives/lldb-argdumper
%ghost %{_sysconfdir}/alternatives/lldb-instr
%ghost %{_sysconfdir}/alternatives/lldb-server
%ghost %{_sysconfdir}/alternatives/lldb-vscode

%if %{with lldb_python}
%files -n python3-lldb%{_sonum}
%license CREDITS.TXT LICENSE.TXT
%{python3_sitearch}/lldb/
%endif

%files -n liblldb%{_sonum}
%license CREDITS.TXT LICENSE.TXT
%{_libdir}/liblldb.so.*
%{_libdir}/liblldbIntelFeatures.so.*

%files -n lldb%{_sonum}-devel
%license CREDITS.TXT LICENSE.TXT
%{_includedir}/lldb/
%{_libdir}/liblldb.so
%{_libdir}/liblldbIntelFeatures.so
%endif

%if %{with polly}
%files polly
%license CREDITS.TXT LICENSE.TXT
%{_libdir}/LLVMPolly.so

%files polly-devel
%license CREDITS.TXT LICENSE.TXT
%{_includedir}/polly
%{_libdir}/cmake/polly
%endif

%changelog
