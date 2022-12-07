#
# spec file for package llvm15
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


%define _relver 15.0.6
%define _version %_relver%{?_rc:rc%_rc}
%define _tagver %_relver%{?_rc:-rc%_rc}
%define _minor  15.0
%define _sonum  15
%define _itsme15 1
# Integer version used by update-alternatives
%define _uaver  1506
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
%define host_cpu armv6kz
%else
%define host_cpu %{_host_cpu}
%endif

%ifarch %{arm}
%define host_triple %{host_cpu}-%{_host_vendor}-%{_host_os}-gnueabihf
%else
%define host_triple %{host_cpu}-%{_host_vendor}-%{_host_os}
%endif

# By default, build everything.
%global llvm_targets "all"
%global llvm_experimental_targets "M68k"
%ifarch %arm ppc64 ppc64le
# No cross-compilation, but GPU targets.
%global llvm_targets "host;AMDGPU;BPF;NVPTX;WebAssembly"
%global llvm_experimental_targets ""
%endif
%ifarch ppc s390x
# No graphics cards on System Z; turned off for ppc because of relocation overflows.
%global llvm_targets "host;BPF;WebAssembly"
%global llvm_experimental_targets ""
%endif

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

# Recursion utils.
%global _stop0 1
%define _lapply_rec(p:f:) %{expand:%{%{-p*} %{-f*}} %%{?!_stop%#:%%{_lapply_rec -p %{-p*} -f %*}}}

# Usage:
#   %%global pattern foo_%%1
#   %%{lapply -p pattern a b c}
# produces foo_a foo_b foo_c.
%define lapply(p:) %{_lapply_rec -p %{-p*} -f %{shrink:%*}}

%define comment() %{nil}

# Due to RPMs recursion limit, we have to split the lists into portions of ≤ 20.
%global llvm_ua_anchor llvm-ar
%global llvm_tools \
%{comment Optimizer, compiler, interpreter, linker} \
    llc \
    lli \
    llvm-jitlink \
    llvm-link \
    llvm-lto \
    llvm-lto2 \
    llvm-rtdyld \
    opt \
%{comment LLVM IR tools} \
    llvm-as \
    llvm-bcanalyzer \
    llvm-bitcode-strip \
    llvm-cat \
    llvm-diff \
    llvm-dis \
    llvm-extract \
    llvm-modextract \
    llvm-sim \
    llvm-split
%global llvm_elf_dwarf_tools \
%{comment ELF tools} \
    llvm-cfi-verify \
    llvm-nm \
    llvm-objcopy \
    llvm-objdump \
    llvm-ranlib \
    llvm-readelf \
    llvm-readobj \
    llvm-size \
    llvm-strip \
%{comment Debug info tools} \
    dsymutil \
    llvm-addr2line \
    llvm-debuginfod \
    llvm-debuginfod-find \
    llvm-dwarfdump \
    llvm-dwarfutil \
    llvm-dwp \
    llvm-gsymutil
%global llvm_abi_coff_macho_tools \
%{comment ABI tools} \
    llvm-cxxdump \
    llvm-cxxfilt \
    llvm-cxxmap \
    llvm-ifs \
%{comment Windows/COFF} \
    llvm-cvtres \
    llvm-dlltool \
    llvm-lib \
    llvm-ml \
    llvm-mt \
    llvm-pdbutil \
    llvm-rc \
    llvm-undname \
    llvm-windres \
%{comment Apple/Mach-O} \
    llvm-install-name-tool \
    llvm-libtool-darwin \
    llvm-lipo \
    llvm-otool \
    llvm-tapi-diff
%global llvm_instr_devel_tools \
%{comment Instrumentation and introspection} \
    llvm-cov \
    llvm-opt-report \
    llvm-profdata \
    llvm-profgen \
    llvm-symbolizer \
    llvm-xray \
    sancov \
    sanstats \
%{comment Development utilities} \
    bugpoint \
    llvm-c-test \
    llvm-mc \
    llvm-mca \
    llvm-reduce \
    llvm-remark-size-diff \
    llvm-stress \
    llvm-strings \
    llvm-tblgen \
    llvm-tli-checker \
    split-file \
    verify-uselistorder

%global clang_ua_anchor clang
%global clang_binfiles \
    c-index-test \
    clang++ \
    clang-check \
    clang-cl \
    clang-extdef-mapping \
    clang-format \
    clang-linker-wrapper \
    clang-nvlink-wrapper \
    clang-offload-bundler \
    clang-offload-packager \
    clang-offload-wrapper \
    clang-refactor \
    clang-rename \
    clang-repl \
    clang-scan-deps \
    diagtool
%global clang_tools_extra_binfiles \
    clang-apply-replacements \
    clang-change-namespace \
    clang-include-fixer \
    clang-move \
    clang-pseudo \
    clang-query \
    clang-reorder-fields \
    clang-tidy \
    clangd \
    find-all-symbols \
    modularize \
    pp-trace
%if %{with lld}
%global lld_ua_anchor lld
%global lld_binfiles \
    ld.lld \
    lld-link \
    ld64.lld \
    wasm-ld
%endif
%if %{with lldb}
%global lldb_ua_anchor lldb
%global lldb_binfiles \
    lldb-argdumper \
    lldb-instr \
    lldb-server \
    lldb-vscode
%endif
%global binfiles \
    %{llvm_ua_anchor} %{llvm_tools} %{llvm_elf_dwarf_tools} \
    %{llvm_abi_coff_macho_tools} %{llvm_instr_devel_tools} \
    %{clang_ua_anchor} %{clang_binfiles} %{clang_tools_extra_binfiles} \
    %{?lld_ua_anchor} %{?lld_binfiles} %{?lldb_ua_anchor} %{?lldb_binfiles}

%global llvm_man \
%{comment Optimizer, compiler, interpreter, linker} \
    llc \
    lli \
    llvm-link \
    opt \
%{comment LLVM IR tools} \
    llvm-as \
    llvm-bcanalyzer \
    llvm-dis \
    llvm-extract \
%{comment Instrumentation and introspection} \
    llvm-cov \
    llvm-profdata \
    llvm-profgen \
    llvm-symbolizer
%global llvm_bin_utils_man \
%{comment ELF tools} \
    llvm-ar \
    llvm-nm \
    llvm-objcopy \
    llvm-objdump \
    llvm-ranlib \
    llvm-readelf \
    llvm-readobj \
    llvm-size \
    llvm-strip \
%{comment Debug info tools} \
    dsymutil \
    llvm-addr2line \
    llvm-dwarfdump \
    llvm-dwarfutil \
%{comment Windows/COFF} \
    llvm-lib \
    llvm-pdbutil \
%{comment Apple/Mach-O} \
    llvm-install-name-tool \
    llvm-libtool-darwin \
    llvm-lipo \
    llvm-otool
%global llvm_devel_utils_man \
%{comment ABI tools} \
    llvm-cxxfilt \
    llvm-cxxmap \
    llvm-ifs \
%{comment Development utilities} \
    bugpoint \
    llvm-diff \
    llvm-mca \
    llvm-remark-size-diff \
    llvm-stress \
    llvm-strings \
    llvm-tblgen \
    llvm-tli-checker

%global clang_manfiles clang diagtool
%global manfiles %{llvm_man} %{llvm_bin_utils_man} %{llvm_devel_utils_man} %{clang_manfiles}

%define _dwz_low_mem_die_limit  40000000
%define _dwz_max_die_limit     200000000

Name:           llvm15
Version:        %_relver%{?_rc:~rc%_rc}
Release:        0
Summary:        Low Level Virtual Machine
License:        Apache-2.0 WITH LLVM-exception AND NCSA
Group:          Development/Languages/Other
URL:            https://www.llvm.org/
# NOTE: please see README.packaging in the llvm package for details on how to update this package
Source0:        https://github.com/llvm/llvm-project/releases/download/llvmorg-%{_tagver}/llvm-%{_version}.src.tar.xz
Source1:        https://github.com/llvm/llvm-project/releases/download/llvmorg-%{_tagver}/cmake-%{_version}.src.tar.xz
Source2:        https://github.com/llvm/llvm-project/releases/download/llvmorg-%{_tagver}/clang-%{_version}.src.tar.xz
Source3:        https://github.com/llvm/llvm-project/releases/download/llvmorg-%{_tagver}/clang-tools-extra-%{_version}.src.tar.xz
Source4:        https://github.com/llvm/llvm-project/releases/download/llvmorg-%{_tagver}/compiler-rt-%{_version}.src.tar.xz
Source5:        https://github.com/llvm/llvm-project/releases/download/llvmorg-%{_tagver}/libcxx-%{_version}.src.tar.xz
Source6:        https://github.com/llvm/llvm-project/releases/download/llvmorg-%{_tagver}/libcxxabi-%{_version}.src.tar.xz
Source7:        https://github.com/llvm/llvm-project/releases/download/llvmorg-%{_tagver}/openmp-%{_version}.src.tar.xz
Source8:        https://github.com/llvm/llvm-project/releases/download/llvmorg-%{_tagver}/lld-%{_version}.src.tar.xz
Source9:        https://github.com/llvm/llvm-project/releases/download/llvmorg-%{_tagver}/lldb-%{_version}.src.tar.xz
Source10:       https://github.com/llvm/llvm-project/releases/download/llvmorg-%{_tagver}/polly-%{_version}.src.tar.xz
Source11:       https://github.com/llvm/llvm-project/raw/llvmorg-%{_tagver}/libunwind/include/mach-o/compact_unwind_encoding.h
# Docs are created manually, see below
Source50:       llvm-docs-%{_version}.src.tar.xz
Source51:       clang-docs-%{_version}.src.tar.xz
Source100:      %{name}-rpmlintrc
Source101:      baselibs.conf
# PATCH-FIX-OPENSUSE lto-disable-cache.patch -- Disable ThinLTO cache
Patch0:         lto-disable-cache.patch
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
# PATCH-FIX-OPENSUSE (or -UPSTREAM?): we disable RPATHs, but the test driver drops LD_LIBRARY_PATH.
Patch15:        libcxx-test-library-path.patch
Patch20:        llvm_build_tablegen_component_as_shared_library.patch
Patch21:        tests-use-python3.patch
Patch22:        llvm-better-detect-64bit-atomics-support.patch
Patch24:        opt-viewer-Find-style-css-in-usr-share.patch
# PATCH-FIX-OPENSUSE check-no-llvm-exegesis.patch -- Don't let tests depend on llvm-exegesis.
# We don't build this because it's not useful without libpfm and can't link with libLLVM.so.
Patch25:        check-no-llvm-exegesis.patch
# PATCH-FIX-OPENSUSE lld-default-sha1.patch
Patch26:        lld-default-sha1.patch
# Fix lookup of targets in installed CMake files. (boo#1180748, https://reviews.llvm.org/D96670)
Patch33:        CMake-Look-up-target-subcomponents-in-LLVM_AVAILABLE_LIBS.patch
# Make sure we link libatomic into libLLVM if necessary. Fixes build on ppc. (https://reviews.llvm.org/D132799)
Patch34:        llvm-link-atomic.patch
# _Unwind_Exception is sometimes just an alias, not a struct. Fixes test on armv7l. (https://reviews.llvm.org/D132873)
Patch35:        libcxxabi-fix-armv7-test.patch
# Let test match for linux instead of -linux-.
Patch36:        clang-test-xfail-gnuless-triple.patch
# Fix lowering of "icmp uge <4 x i32> zeroinitializer, ..." on armv7. (https://reviews.llvm.org/D136447?id=469567, boo#1204267, gh#llvm/llvm-project#58514)
Patch37:        llvm-armv7-fix-vector-compare-with-zero-lowering.patch
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
Requires(postun):update-alternatives
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
Requires(postun):update-alternatives
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
Conflicts:      %{python3_sitearch}/clang/
Provides:       %{python3_sitearch}/clang/

%description -n python3-clang%{_sonum}
This package contains the Python bindings to clang (C language)
frontend for LLVM.

%package -n lld%{_sonum}
Summary:        Linker for Clang/LLVM
Group:          Development/Tools/Building
URL:            https://lld.llvm.org/
Requires(post): update-alternatives
Requires(postun):update-alternatives

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
Requires(postun):update-alternatives
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
%setup -q -a 1 -a 2 -a 3 -a 4 -a 5 -a 6 -a 7 -a 8 -a 9 -a 10 -b 50 -b 51 -n llvm-%{_version}.src
%patch0 -p2
%patch5 -p1
%patch13 -p1
%patch14 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch24 -p1
%patch25 -p2
%patch33 -p2
%patch34 -p2
%patch37 -p1

pushd clang-%{_version}.src
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch6 -p1
%patch9 -p2
%patch36 -p2

# We hardcode openSUSE
rm unittests/Driver/DistroTest.cpp

# We hardcode i586
rm test/Driver/x86_features.c
rm test/Driver/nacl-direct.c
popd

pushd clang-tools-extra-%{_version}.src
%patch10 -p2
popd

pushd lld-%{_version}.src
%patch26 -p1
# lld got a compile-time dependency on libunwind that we don't want. (https://reviews.llvm.org/D86805)
mkdir include/mach-o
cp %{SOURCE11} include/mach-o
popd

%if %{with lldb}
pushd lldb-%{_version}.src
%patch11 -p1
popd
%endif

%if %{with libcxx}
pushd libcxxabi-%{_version}.src
%patch35 -p2
popd

pushd libcxx-%{_version}.src
%patch15 -p2
rm test/libcxx/thread/thread.threads/thread.thread.this/sleep_for.pass.cpp
rm test/std/localization/locale.categories/category.time/locale.time.get.byname/get_monthname.pass.cpp
rm test/std/localization/locale.categories/category.time/locale.time.get.byname/get_monthname_wide.pass.cpp

# These tests often verify timing and can randomly fail if the system is under heavy load. It happens sometimes on our build machines.
rm -rf test/std/thread/
popd
%endif

# Move into right place
mv cmake-%{_version}.src ../cmake
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
%global sourcedir %{_builddir}/%{buildsubdir}

%define _lto_cflags %{nil}

# Use optflags, but:
# 1) Remove the -D_FORTIFY_SOURCE=2 because llvm does not build correctly with
#    hardening. The problem is in sanitizers from compiler-rt.
# 2) Remove the -g. We don't want it in stage1 and it will be added by cmake in
#    the following stage.
%global cleaned_flags %(echo %{optflags} | sed 's/-D_FORTIFY_SOURCE=./-D_FORTIFY_SOURCE=0/;s/\\B-g\\b//g')

%global flags %{cleaned_flags}
%ifarch armv6hl
%global flags %{cleaned_flags} -mfloat-abi=hard -mcpu=arm1176jzf-s -mfpu=vfpv2
%endif
%ifarch armv7hl
%global flags %{cleaned_flags} -mfloat-abi=hard -march=armv7-a -mtune=cortex-a17 -mfpu=vfpv3-d16
%endif

CFLAGS="%flags"
CXXFLAGS="%flags"

mem_per_compile_job=1200000
%ifarch i586 ppc armv6hl armv7hl
# 32-bit arches need less memory than 64-bit arches.
mem_per_compile_job=700000
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
    -DLLVM_BUILD_TOOLS:BOOL=OFF \
    -DLLVM_BUILD_UTILS:BOOL=OFF \
    -DLLVM_BUILD_EXAMPLES:BOOL=OFF \
    -DLLVM_BUILD_RUNTIME:BOOL=OFF \
    -DLLVM_TOOL_CLANG_TOOLS_EXTRA_BUILD:BOOL=OFF \
    -DLLVM_INCLUDE_BENCHMARKS:BOOL=OFF \
    -DLLVM_INCLUDE_TESTS:BOOL=OFF \
    -DLLVM_TARGETS_TO_BUILD=Native \
    -DCLANG_ENABLE_ARCMT:BOOL=OFF \
    -DCLANG_ENABLE_STATIC_ANALYZER:BOOL=OFF
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
if ! ./stage1/bin/clang -c -xc -Werror -fstack-clash-protection -o /dev/null /dev/null;
then
    flags=$(echo %flags | sed 's/-fstack-clash-protection//');
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
# The build occasionally uses tools linking against previously built
# libraries (mostly libLLVM.so), but we don't want to set RUNPATHs.
export LD_LIBRARY_PATH=%{sourcedir}/build/%{_lib}
%cmake \
    -DCMAKE_C_COMPILER="%{sourcedir}/stage1/bin/clang" \
    -DCMAKE_CXX_COMPILER="%{sourcedir}/stage1/bin/clang++" \
    -DBUILD_SHARED_LIBS:BOOL=OFF \
    -DLLVM_HOST_TRIPLE=%{host_triple} \
    -DLLVM_BUILD_LLVM_DYLIB:BOOL=ON \
    -DLLVM_LINK_LLVM_DYLIB:BOOL=ON \
    -DCLANG_LINK_CLANG_DYLIB:BOOL=ON \
    -DLLVM_PARALLEL_COMPILE_JOBS="$max_compile_jobs" \
    -DLLVM_PARALLEL_LINK_JOBS="$max_link_jobs" \
%if %{with thin_lto}
    -DLLVM_ENABLE_LTO=Thin \
    -DCMAKE_AR="%{sourcedir}/stage1/bin/llvm-ar" \
    -DCMAKE_RANLIB="%{sourcedir}/stage1/bin/llvm-ranlib" \
%if %{with use_lld}
    -DCMAKE_LINKER="%{sourcedir}/stage1/bin/ld.lld" \
    -DLLVM_USE_LINKER="%{sourcedir}/stage1/bin/ld.lld" \
%endif
%endif
%ifarch %arm ppc s390 %{ix86}
    -DCMAKE_C_FLAGS_RELWITHDEBINFO="-O2 -g1 -DNDEBUG" \
    -DCMAKE_CXX_FLAGS_RELWITHDEBINFO="-O2 -g1 -DNDEBUG" \
%endif
    -DENABLE_LINKER_BUILD_ID=ON \
    -DLLVM_TABLEGEN="%{sourcedir}/stage1/bin/llvm-tblgen" \
    -DCLANG_TABLEGEN="%{sourcedir}/stage1/bin/clang-tblgen" \
    -DLLVM_ENABLE_RTTI:BOOL=ON \
    -DLLVM_ENABLE_PIC=ON \
    -DLLVM_BINUTILS_INCDIR=%{_includedir} \
    -DLLVM_TARGETS_TO_BUILD=%{llvm_targets} \
    -DLLVM_EXPERIMENTAL_TARGETS_TO_BUILD=%{llvm_experimental_targets} \
    -DLLVM_TOOL_LLVM_EXEGESIS_BUILD:BOOL=OFF \
    -DLLVM_ENABLE_PER_TARGET_RUNTIME_DIR:BOOL=OFF \
    -DLLVM_INCLUDE_BENCHMARKS:BOOL=OFF \
    -DCLANG_FORCE_MATCHING_LIBCLANG_SOVERSION:BOOL=OFF \
    -DCOMPILER_RT_USE_LIBCXX:BOOL=OFF \
    -DLIBCXX_INCLUDE_BENCHMARKS:BOOL=OFF \
%if %{with libcxx}
    -DLIBCXX_ENABLE_SHARED=YES \
    -DLIBCXX_ENABLE_STATIC=NO \
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
%else
    -DLLDB_USE_SYSTEM_SIX:BOOL=ON \
%endif
    -DCMAKE_SKIP_RPATH:BOOL=ON \
    -DLLVM_POLLY_LINK_INTO_TOOLS=OFF \
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
export LD_LIBRARY_PATH=%{sourcedir}/build/%{_lib}
%cmake_install

# Install FileCheck needed for testing Rust boo#1192629
install -m 0755 build/bin/FileCheck %{buildroot}%{_bindir}/FileCheck

# Remove files that won't be needed anymore.
# This reduces the total amount of disk space used during build. (bnc#1074625)
find ./build \( -name '*.o' -or -name '*.a' \)  -delete

# Docs are prebuilt due to sphinx dependency
#
# tar xf cmake-%{_version}.src.tar.xz
# mv cmake-%{_version}.src cmake
# tar xf llvm-%{_version}.src.tar.xz
# pushd llvm-%{_version}.src/tools
# tar xf ../../clang-%{_version}.src.tar.xz
# mv clang-%{_version}.src clang
# cd ..
# ln -s ../../../build/tools/clang/docs/{Attribute,Diagnostics}Reference.rst tools/clang/docs
# mkdir build; cd build
# cmake -G Ninja -DCMAKE_BUILD_TYPE=Release -DLLVM_ENABLE_SPHINX:BOOL=ON -DLLVM_BUILD_DOCS:BOOL=ON \
#     -DSPHINX_WARNINGS_AS_ERRORS:BOOL=OFF -DLLVM_INCLUDE_BENCHMARKS:BOOL=OFF ..
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
mv %{buildroot}%{_datadir}/clang/clang-format-diff.py %{buildroot}%{_bindir}/clang-format-diff
mv %{buildroot}%{_datadir}/clang/clang-tidy-diff.py %{buildroot}%{_bindir}/clang-tidy-diff
mv %{buildroot}%{_datadir}/clang/run-find-all-symbols.py %{buildroot}%{_bindir}/run-find-all-symbols

# Fix paths to internal binaries.
sed -i "s|COMPILER_WRAPPER_\([A-Z]*\) = 'intercept-\([^']*\)'|COMPILER_WRAPPER_\1 = '%{_libexecdir}/intercept-\2'|" \
    %{buildroot}%{_prefix}/lib/libscanbuild/intercept.py
%if "%{_libexecdir}" != "%{_prefix}/libexec"
LIBEXEC=%{_libexecdir}
RELATIVE_LIBEXEC=${LIBEXEC#%{_prefix}/}
sed -i "s|\$AbsRealBin/../libexec/\([^-]*\)-analyzer|\$AbsRealBin/../$RELATIVE_LIBEXEC/\1-analyzer|" \
    %{buildroot}%{_bindir}/scan-build
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
rm %{buildroot}%{_libexecdir}/{c++,ccc}-analyzer
rm %{buildroot}%{_libexecdir}/{analyze,intercept}-{cc,c++}
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
rm %{buildroot}%{_mandir}/man1/llvm-{exegesis,locstats}.1

%if %{with lldb_python}
# Python: fix binary libraries location.
rm %{buildroot}%{python3_sitearch}/lldb/_lldb.%{cpython3_soabi}.so
liblldb=$(basename $(readlink -e %{buildroot}%{_libdir}/liblldb.so))
ln -vsf "../../../${liblldb}" %{buildroot}%{python3_sitearch}/lldb/_lldb.%{cpython3_soabi}.so
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

# Fix the clang -> clang-X.Y symlink to work with update-alternatives
mv %{buildroot}%{_bindir}/clang-%{_sonum} %{buildroot}%{_bindir}/clang
ln -s %{_bindir}/clang-%{_relver} %{buildroot}%{_bindir}/clang-%{_sonum}
ln -s %{_bindir}/clang-%{_relver} %{buildroot}%{_bindir}/clang-%{_minor}

# Add clang++-X.Y symbolic link as well - it seems to be expected by some
# software. https://bugzilla.opensuse.org/show_bug.cgi?id=1012260
ln -s %{_bindir}/clang++-%{_relver} %{buildroot}%{_bindir}/clang++-%{_sonum}
ln -s %{_bindir}/clang++-%{_relver} %{buildroot}%{_bindir}/clang++-%{_minor}

# Rewrite symlinks to point to new location
for p in %{shrink:%binfiles} ; do
    if [ -h "%{buildroot}%{_bindir}/$p" ] ; then
        ln -f -s %{_bindir}/$(readlink %{buildroot}%{_bindir}/$p)-%{_relver} %{buildroot}%{_bindir}/$p
    fi
done
for p in %{shrink:%binfiles} ; do
    mv %{buildroot}%{_bindir}/$p %{buildroot}%{_bindir}/$p-%{_relver}
    ln -s -f %{_sysconfdir}/alternatives/$p %{buildroot}%{_bindir}/$p
done
for p in %{shrink:%manfiles} ; do
    mv %{buildroot}%{_mandir}/man1/$p.1 %{buildroot}%{_mandir}/man1/$p-%{_relver}.1
    ln -s -f %{_sysconfdir}/alternatives/$p.1%{ext_man} %{buildroot}%{_mandir}/man1/$p.1%{ext_man}
done

# Also rewrite the CMake files referring to the binaries.
sed -i "$(
    for p in %{shrink:%binfiles}; do
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
%_libclang_sonum %{_soclang}
%_libcxx_sonum %{_socxx}

# Build information
%_llvm_with_libcxx %{with libcxx}
%_llvm_with_openmp %{with openmp}
%_llvm_with_ffi %{with ffi}
%_llvm_with_oprofile %{with oprofile}
%_llvm_with_valgrind %{with valgrind}
%_llvm_with_lldb %{with lldb}
EOF

# Don't use env in shebangs, and prefer python3. (https://www.python.org/dev/peps/pep-0394/#for-python-runtime-distributors)
for script in %{buildroot}%{_bindir}/opt-{diff,stats,viewer} \
%if %{_plv} == %{_sonum}
        %{buildroot}%{_bindir}/{{analyze,intercept}-build,clang-{format,tidy}-diff,git-clang-format,hmaptool,run-{clang-tidy,find-all-symbols},scan-{build,build-py,view}} \
        %{buildroot}%{_libexecdir}/{{analyze,intercept}-{c++,cc},{c++,ccc}-analyzer} \
%endif
%ifarch aarch64 x86_64
        %{buildroot}%{_libdir}/clang/%{_relver}/bin/hwasan_symbolize \
%endif
        %{buildroot}%{python3_sitelib}/optrecord.py; do
    sed -i '1s|/usr/bin/env *|%{_bindir}/|;1s|/usr/bin/python$|%{_bindir}/python3|' $script
done

# Remove executable bit where not needed.
chmod -x \
  %{buildroot}%{python3_sitelib}/optpmap.py \
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
sed -i '1i; UNSUPPORTED: armv6' ../test/{CodeGen/Generic/PBQP.ll,ExecutionEngine/Orc/global-ctor-with-cast.ll}
sed -i '1i; UNSUPPORTED: armv6\n; XFAIL: powerpc-' \
  ../test/ExecutionEngine/{mov64zext32,test-interp-vec-{arithm_{float,int},logical,setcond-{fp,int}}}.ll
%ifarch ppc64le
# Sporadic failures, possibly races?
rm ../test/tools/llvm-cov/{multithreaded-report,sources-specified}.test
%endif
python3 bin/llvm-lit -sv test/

# On ppc, these tests fails with "fatal error: error in backend: Relocation type not implemented yet!"
sed -i '1i// XFAIL: powerpc-' ../tools/clang/test/Interpreter/{code-undo,execute,execute-weak}.cpp
# Tests hang on armv6l.
sed -i '1i// UNSUPPORTED: armv6' \
  ../tools/clang/test/{Interpreter/{code-undo,execute,execute-weak}.cpp,Modules/{preprocess-{build-diamond.m,decluse.cpp,module.cpp},string_names.cpp}}
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
python3 bin/llvm-lit -sv --param enable_experimental=False projects/libcxx/test/
%endif

# There are undefined references to __cxa_* functions and "typeinfo for int".
sed -i '1i@ XFAIL: arm' ../projects/libcxxabi/test/native/arm-linux-eabi/ttype-encoding-{0,9}0.pass.sh.s
# Compiler error: typedef '_Unwind_Exception' cannot be referenced with a struct specifier
sed -i '1i// XFAIL: armv6, armv7' ../projects/libcxxabi/test/forced_unwind{1,2}.pass.cpp
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

%global ua_install() %{_sbindir}/update-alternatives \\\
    --install %{_bindir}/%1 %1 %{_bindir}/%1-%{_relver} %{_uaver}
%global ua_bin_slave() \\\
    --slave %{_bindir}/%1 %1 %{_bindir}/%1-%{_relver}
%global ua_man_slave() \\\
    --slave %{_mandir}/man1/%1.1%{ext_man} %1.1%{ext_man} %{_mandir}/man1/%1-%{_relver}.1%{ext_man}
%global ua_remove() \
if [ ! -f %{_bindir}/%1-%{_relver} ] ; then \
    %{_sbindir}/update-alternatives --remove %1 %{_bindir}/%1-%{_relver} \
fi

%post
%{ua_install %llvm_ua_anchor} \
    %{lapply -p ua_bin_slave %llvm_tools} \
    %{lapply -p ua_bin_slave %llvm_elf_dwarf_tools} \
    %{lapply -p ua_bin_slave %llvm_abi_coff_macho_tools} \
    %{lapply -p ua_bin_slave %llvm_instr_devel_tools} \
    %{lapply -p ua_man_slave %llvm_man} \
    %{lapply -p ua_man_slave %llvm_bin_utils_man} \
    %{lapply -p ua_man_slave %llvm_devel_utils_man}

%postun
%{ua_remove %llvm_ua_anchor}

%post -n clang%{_sonum}
%{ua_install %clang_ua_anchor} \
    %{lapply -p ua_bin_slave %clang_binfiles} \
    %{lapply -p ua_bin_slave %clang_tools_extra_binfiles} \
    %{lapply -p ua_man_slave %clang_manfiles}

%postun -n clang%{_sonum}
%{ua_remove %clang_ua_anchor}

%if %{with lld}
%post -n lld%{_sonum}
%{ua_install %lld_ua_anchor} \
    %{lapply -p ua_bin_slave %lld_binfiles}
%{_sbindir}/update-alternatives --install %{_bindir}/ld ld %{_bindir}/ld.lld 1

%postun -n lld%{_sonum}
%{ua_remove %lld_ua_anchor}
if [ ! -f %{_bindir}/lld ] ; then
    %{_sbindir}/update-alternatives --remove ld %{_bindir}/ld.lld
fi
%endif

%if %{with lldb}
%post -n lldb%{_sonum}
%{ua_install %lldb_ua_anchor} \
    %{lapply -p ua_bin_slave %lldb_binfiles}

%postun -n lldb%{_sonum}
%{ua_remove %lldb_ua_anchor}
%endif

%global bin_path() \
%{_bindir}/%1
%global bin_relver_path() \
%{_bindir}/%1-%{_relver}
%global ghost_ua_bin_link() \
%ghost %{_sysconfdir}/alternatives/%1
%global man_path() \
%{_mandir}/man1/%1.1%{ext_man}
%global man_relver_path() \
%{_mandir}/man1/%1-%{_relver}.1%{ext_man}
%global ghost_ua_man_link() \
%ghost %{_sysconfdir}/alternatives/%1.1%{ext_man}

%files
%license CREDITS.TXT LICENSE.TXT
%{lapply -p bin_path %llvm_ua_anchor %llvm_tools}
%{lapply -p bin_path %llvm_elf_dwarf_tools}
%{lapply -p bin_path %llvm_abi_coff_macho_tools}
%{lapply -p bin_path %llvm_instr_devel_tools}
%{lapply -p bin_relver_path %llvm_ua_anchor %llvm_tools}
%{lapply -p bin_relver_path %llvm_elf_dwarf_tools}
%{lapply -p bin_relver_path %llvm_abi_coff_macho_tools}
%{lapply -p bin_relver_path %llvm_instr_devel_tools}
%{lapply -p ghost_ua_bin_link %llvm_ua_anchor %llvm_tools}
%{lapply -p ghost_ua_bin_link %llvm_elf_dwarf_tools}
%{lapply -p ghost_ua_bin_link %llvm_abi_coff_macho_tools}
%{lapply -p ghost_ua_bin_link %llvm_instr_devel_tools}

%{lapply -p man_path %llvm_man}
%{lapply -p man_path %llvm_bin_utils_man}
%{lapply -p man_path %llvm_devel_utils_man}
%{lapply -p man_relver_path %llvm_man}
%{lapply -p man_relver_path %llvm_bin_utils_man}
%{lapply -p man_relver_path %llvm_devel_utils_man}
%{lapply -p ghost_ua_man_link %llvm_man}
%{lapply -p ghost_ua_man_link %llvm_bin_utils_man}
%{lapply -p ghost_ua_man_link %llvm_devel_utils_man}

%files -n clang%{_sonum}
%license CREDITS.TXT LICENSE.TXT
%{_bindir}/clang-%{_minor}
%{_bindir}/clang-%{_sonum}
%{_bindir}/clang++-%{_minor}
%{_bindir}/clang++-%{_sonum}
%{_bindir}/clang-cpp
%{lapply -p bin_path %clang_ua_anchor %clang_binfiles}
%{lapply -p bin_path %clang_tools_extra_binfiles}
%{lapply -p bin_relver_path %clang_ua_anchor %clang_binfiles}
%{lapply -p bin_relver_path %clang_tools_extra_binfiles}
%{lapply -p ghost_ua_bin_link %clang_ua_anchor %clang_binfiles}
%{lapply -p ghost_ua_bin_link %clang_tools_extra_binfiles}

%{lapply -p man_path %clang_manfiles}
%{lapply -p man_relver_path %clang_manfiles}
%{lapply -p ghost_ua_man_link %clang_manfiles}

%dir %{_libdir}/clang/
%dir %{_libdir}/clang/%{_relver}/
%ifarch aarch64 x86_64
%{_libdir}/clang/%{_relver}/bin
%endif
%{_libdir}/clang/%{_relver}/lib
# The sanitizer runtime is not available for ppc.
%ifnarch ppc
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
%{_libexecdir}/analyze-c++
%{_libexecdir}/analyze-cc
%{_libexecdir}/c++-analyzer
%{_libexecdir}/ccc-analyzer
%{_libexecdir}/intercept-c++
%{_libexecdir}/intercept-cc
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
%{_libdir}/libompd.so
%{_libdir}/libomptarget.so
# TODO: intentional? We don't have it for libomp.so.
%{_libdir}/libomptarget.so.%{_sonum}
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
%{_libdir}/libc++experimental.a
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
%{lapply -p bin_path %lld_ua_anchor %lld_binfiles}
%{lapply -p bin_relver_path %lld_ua_anchor %lld_binfiles}
%{lapply -p ghost_ua_bin_link %lld_ua_anchor %lld_binfiles}
%endif

%if %{with lldb}
%files -n lldb%{_sonum}
%license CREDITS.TXT LICENSE.TXT
%{lapply -p bin_path %lldb_ua_anchor %lldb_binfiles}
%{lapply -p bin_relver_path %lldb_ua_anchor %lldb_binfiles}
%{lapply -p ghost_ua_bin_link %lldb_ua_anchor %lldb_binfiles}

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
