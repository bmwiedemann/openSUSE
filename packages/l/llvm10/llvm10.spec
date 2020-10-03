#
# spec file for package llvm10
#
# Copyright (c) 2020 SUSE LLC
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


%define _relver 10.0.1
%define _version %_relver%{?_rc:rc%_rc}
%define _tagver %_relver%{?_rc:-rc%_rc}
%define _minor  10.0
%define _sonum  10
# Integer version used by update-alternatives
%define _uaver  1001
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

# LLVM currently doesn't build with Gold on ppc
# Gold is not supported on riscv64
%ifarch ppc riscv64
%bcond_with gold
%else
%bcond_without gold
%endif

%ifarch x86_64
%bcond_without lldb
%bcond_without lldb_python
%else
%bcond_with lldb
%bcond_with lldb_python
%endif

# Disabled on ppc64le because of internal error in gold.
# /usr/bin/ld.gold: internal error in get_opd_ent, at ../../gold/powerpc.cc:198
%ifarch aarch64 %{arm} x86_64 %{ix86} s390x
%bcond_without thin_lto
%else
%bcond_with thin_lto
%endif

%bcond_with ffi
%bcond_with oprofile
%bcond_with valgrind
%bcond_without clang_scripts
%bcond_without polly
%bcond_without lld

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

Name:           llvm10
Version:        %_relver%{?_rc:~rc%_rc}
Release:        0
Summary:        Low Level Virtual Machine
License:        Apache-2.0 WITH LLVM-exception OR NCSA
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
Patch8:         clang-ignore-stack-clash-protector.patch
Patch9:         link-clang-shared.patch
Patch10:        link-clang-tools-extra-shared.patch
# PATCH-FIX-OPENSUSE lldb-cmake.patch -- Fix ncurses include path.
Patch11:        lldb-cmake.patch
# PATCH-FIX-OPENSUSE polly-pthread.patch -- Make sure -lpthread is linked after libPolly (related to GCC#55394)
Patch12:        polly-pthread.patch
Patch13:        llvm-normally-versioned-libllvm.patch
Patch14:        llvm-do-not-install-static-libraries.patch
# PATCH-FIX-UPSTREAM tablegen-test-link-static.patch -- https://reviews.llvm.org/D74588
Patch15:        tablegen-test-link-static.patch
Patch20:        llvm_build_tablegen_component_as_shared_library.patch
Patch21:        tests-use-python3.patch
Patch22:        llvm-better-detect-64bit-atomics-support.patch
Patch24:        opt-viewer-Find-style-css-in-usr-share.patch
# A patch in 10.0.0 changed the ABI vs upstream, but the upstream patch that
# landed in 10.0.1 is ABI stable, so to be ABI-compatible with our 10.0.0 we
# need to make sure we go with our 10.0.0 enum value order.
Patch25:        restore-llvm10-abi.patch
# PATCH-FIX-OPENSUSE lld-default-sha1.patch
Patch26:        lld-default-sha1.patch
# PATCH-FIX-UPSTREAM fix-atomics-test.patch -- Fix Clang test for arches without native atomics.
Patch27:        fix-atomics-test.patch
# PATCH-FIX-UPSTREAM llvm-fix-a-copy-and-paste-error-that-would-cause-a-crash.patch -- Fix dsymutil crash on ELF file.
Patch28:        llvm-fix-a-copy-and-paste-error-that-would-cause-a-crash.patch
BuildRequires:  binutils-devel >= 2.21.90
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libstdc++-devel
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  python3-base
BuildRequires:  pkgconfig(libedit)
BuildRequires:  pkgconfig(zlib)
# Avoid multiple provider errors
Requires:       libLLVM%{_sonum}
Requires(post): update-alternatives
Requires(postun): update-alternatives
Recommends:     %{name}-doc
# llvm does not work on s390
ExcludeArch:    s390
%if %{with gold}
BuildRequires:  binutils-gold
%endif
%if %{with ffi}
BuildRequires:  pkgconfig(libffi)
%endif
%if %{with valgrind}
BuildRequires:  pkgconfig(valgrind)
%endif
%if %{with oprofile}
BuildRequires:  oprofile-devel
%endif

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
Requires:       libstdc++-devel
Requires:       libtool
Requires:       llvm%{_sonum}-LTO-devel
Requires:       llvm%{_sonum}-gold
%if %{with polly}
Requires:       llvm%{_sonum}-polly-devel
%endif
Requires:       pkgconfig
Conflicts:      llvm-devel-provider < %{version}
Conflicts:      cmake(LLVM)
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
# Avoid multiple provider errors
Requires:       libLTO%{_sonum}
Requires:       libclang%{_sonum}
Requires(post): update-alternatives
Requires(postun): update-alternatives
Recommends:     clang-tools
Recommends:     clang%{_sonum}-doc
Recommends:     libstdc++-devel
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

%package -n libclang%{_sonum}
Summary:        Library files needed for clang
# Avoid multiple provider errors
Group:          System/Libraries
Requires:       libLLVM%{_sonum}

%description -n libclang%{_sonum}
This package contains the shared libraries needed for clang.

%package -n clang%{_sonum}-devel
Summary:        CLANG frontend for LLVM (devel package)
Group:          Development/Libraries/C and C++
Requires:       %{name}-devel = %{version}
Requires:       clang%{_sonum} = %{version}
Requires:       clang-tools = %{version}
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
# Avoid multiple provider errors
Group:          System/Libraries
Requires:       libLLVM%{_sonum}

%description -n libLTO%{_sonum}
This package contains the link-time optimizer for LLVM.

%package LTO-devel
Summary:        Link-time optimizer for LLVM (devel package)
# Avoid multiple provider errors
Group:          Development/Libraries/C and C++
Requires:       %{name}-devel = %{version}
Requires:       libLTO%{_sonum}
Conflicts:      libLTO.so < %{version}
Provides:       libLTO.so = %{version}

%description LTO-devel
This package contains the link-time optimizer for LLVM.
(development files)

%package gold
Summary:        Gold linker plugin for LLVM
# Avoid multiple provider errors
Group:          Development/Tools/Building
Requires:       libLLVM%{_sonum}
Conflicts:      llvm-gold-provider < %{version}
Provides:       llvm-gold-provider = %{version}
Supplements:    packageand(clang%{_sonum}:binutils-gold)

%description gold
This package contains the Gold linker plugin for LLVM.

%package -n libomp%{_sonum}-devel
Summary:        MPI plugin for LLVM
# Avoid multiple provider errors
Group:          Development/Libraries/C and C++
Requires:       libLLVM%{_sonum}
Conflicts:      libomp-devel < %{version}
Provides:       libomp-devel = %{version}

%description -n libomp%{_sonum}-devel
This package contains the OpenMP MPI plugin for LLVM.

%if %{with libcxx}
%package -n libc++%{_socxx}
Summary:        C++ standard library implementation
Group:          System/Libraries
URL:            https://libcxx.llvm.org/
Requires:       libc++abi%{_socxx} = %{version}

%description -n libc++%{_socxx}
This package contains libc++, a new implementation of the C++
standard library, targeting C++11.

%package -n libc++-devel
Summary:        C++ standard library implementation (devel package)
# Avoid multiple provider errors
Group:          Development/Libraries/C and C++
Requires:       libc++%{_socxx} = %{version}
Requires:       libc++abi-devel = %{version}
Conflicts:      libc++.so < %{version}
Provides:       libc++.so = %{version}

%description -n libc++-devel
This package contains libc++, a new implementation of the C++
standard library, targeting C++11. (development files)

%package -n libc++abi%{_socxx}
Summary:        C++ standard library ABI
Group:          System/Libraries
URL:            https://libcxxabi.llvm.org/

%description -n libc++abi%{_socxx}
This package contains the ABI for libc++, a new implementation
of the C++ standard library, targeting C++11.

%package -n libc++abi-devel
Summary:        C++ standard library ABI (devel package)
Group:          Development/Libraries/C and C++
Requires:       libc++-devel
Requires:       libc++abi%{_socxx} = %{version}
Conflicts:      libc++abi.so < %{version}
Provides:       libc++abi.so = %{version}

%description -n libc++abi-devel
This package contains the ABI for libc++, a new implementation
of the C++ standard library, targeting C++11.
(development files)
%endif

%package        vim-plugins
Summary:        Vim plugins for LLVM
Group:          Productivity/Text/Editors
Supplements:    packageand(llvm%{_sonum}:vim)
Conflicts:      vim-plugin-llvm < %{version}
Provides:       vim-plugin-llvm = %{version}
BuildArch:      noarch

%description    vim-plugins
This package contains vim plugins for LLVM like syntax highlighting.

%package -n python3-clang
Summary:        Python bindings for libclang
Group:          Development/Libraries/Python
Requires:       clang%{_sonum}-devel = %{version}
Requires:       python3-base
Conflicts:      %{python3_sitearch}/clang/
Provides:       %{python3_sitearch}/clang/
BuildArch:      noarch

%description -n python3-clang
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
# Avoid multiple provider errors
Requires:       liblldb%{_sonum} = %{version}
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
# Avoid multiple provider errors
Group:          System/Libraries
Requires:       libLLVM%{_sonum}
Requires:       libclang%{_sonum}

%description -n liblldb%{_sonum}
This subpackage contains the main LLDB component.

%package -n lldb%{_sonum}-devel
Summary:        Development files for LLDB
# Avoid multiple provider errors
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
# Avoid multiple provider errors
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
Requires:       llvm%{_sonum}-polly = %{version}
Conflicts:      llvm-polly-devel-provider < %{version}
Provides:       llvm-polly-devel-provider = %{version}

%description polly-devel
This package contains the development files for Polly.
%endif

%prep
%setup -q -a 1 -a 2 -a 3 -a 4 -a 5 -a 6 -a 7 -a 8 -a 9 -b 50 -a 51 -n llvm-%{_version}.src

%patch0 -p2
%patch5 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p2
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch24 -p1
%patch25 -p1
%patch28 -p2

pushd clang-%{_version}.src
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch6 -p1
%patch8 -p1
%patch9 -p2
%patch27 -p1

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
popd

%if %{with lldb}
pushd lldb-%{_version}.src
%patch11 -p1
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

pushd polly-%{_version}.src
%patch12 -p2
popd

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
flags+=" -mfloat-abi=hard -march=armv6zk -mtune=arm1176jzf-s -mfpu=vfp"
%endif
%ifarch armv7hl
flags+=" -mfloat-abi=hard -march=armv7-a -mtune=cortex-a15 -mfpu=vfpv3-d16"
%endif

CFLAGS=$flags
CXXFLAGS=$flags

# By default build everything
TARGETS_TO_BUILD="all"
%ifarch s390 s390x
# No graphics cards on System z
TARGETS_TO_BUILD="host;BPF"
%endif
%ifarch %arm
# TODO: Document why those.
TARGETS_TO_BUILD="host;ARM;AMDGPU;BPF;NVPTX"
%endif
%ifarch ppc64 ppc64le
# TODO: Document why those.
TARGETS_TO_BUILD="host;AMDGPU;BPF;NVPTX"
%endif
%ifarch ppc
# TODO: Graphics cards turned off because of relocation overflows.
TARGETS_TO_BUILD="host;BPF"
%endif

mem_per_compile_job=900000
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
# -z,now is breaking now, it needs to be fixed
%cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DBUILD_SHARED_LIBS:BOOL=OFF \
    -DLLVM_BUILD_LLVM_DYLIB:BOOL=OFF \
    -DLLVM_LINK_LLVM_DYLIB:BOOL=OFF \
    -DLLVM_PARALLEL_COMPILE_JOBS="$max_compile_jobs" \
    -DLLVM_PARALLEL_LINK_JOBS="$max_link_jobs" \
    -DENABLE_LINKER_BUILD_ID=ON \
    -DLLVM_BINUTILS_INCDIR=%{_includedir} \
    -DLLVM_BUILD_TOOLS:BOOL=OFF \
    -DLLVM_BUILD_UTILS:BOOL=OFF \
    -DLLVM_BUILD_EXAMPLES:BOOL=OFF \
    -DLLVM_POLLY_BUILD:BOOL=OFF \
    -DLLVM_TOOL_CLANG_TOOLS_EXTRA_BUILD:BOOL=OFF \
    -DLLVM_INCLUDE_TESTS:BOOL=OFF \
    -DLLVM_ENABLE_ASSERTIONS=OFF \
    -DLLVM_TARGETS_TO_BUILD=Native \
%if %{with gold}
    -DLLVM_USE_LINKER=gold \
%endif
    -DCLANG_ENABLE_ARCMT:BOOL=OFF \
    -DCLANG_ENABLE_STATIC_ANALYZER:BOOL=OFF \
    -DCOMPILER_RT_BUILD_SANITIZERS:BOOL=OFF \
    -DCOMPILER_RT_BUILD_XRAY:BOOL=OFF \
    -DLLDB_DISABLE_PYTHON=ON \
    -DCMAKE_SKIP_RPATH:BOOL=OFF \
    -DCMAKE_EXE_LINKER_FLAGS="-Wl,--as-needed -Wl,--no-keep-memory" \
    -DCMAKE_MODULE_LINKER_FLAGS="-Wl,--as-needed -Wl,--no-keep-memory" \
    -DCMAKE_SHARED_LINKER_FLAGS="-Wl,--as-needed -Wl,--no-keep-memory" \
    -DPYTHON_EXECUTABLE:FILEPATH=%{_bindir}/python3
%if %{with thin_lto}
ninja -v %{?_smp_mflags} clang llvm-tblgen clang-tblgen llvm-ar llvm-ranlib LLVMgold
%else
ninja -v %{?_smp_mflags} clang llvm-tblgen clang-tblgen
%endif
cd ..

# Remove files that won't be needed anymore.
# This reduces the total amount of disk space used during build. (bnc#1074625)
find ./stage1 \( -name '*.o' -or -name '*.a' \) -delete

# Clang uses a bit less memory.
mem_per_compile_job=700000
%ifarch i586 ppc armv6hl armv7hl
# 32-bit arches need less memory than 64-bit arches.
mem_per_compile_job=500000
%endif

%set_jobs compile $mem_per_compile_job

%define __builddir build
export PATH=${PWD}/stage1/bin:$PATH
export CC=${PWD}/stage1/bin/clang
export CXX=${PWD}/stage1/bin/clang++
%if %{with thin_lto}
export LLVM_AR=${PWD}/stage1/bin/llvm-ar
export LLVM_RANLIB=${PWD}/stage1/bin/llvm-ranlib
%endif
export LLVM_TABLEGEN=${PWD}/stage1/bin/llvm-tblgen
export CLANG_TABLEGEN=${PWD}/stage1/bin/clang-tblgen
# -z,now is breaking now, it needs to be fixed
%cmake \
    -DBUILD_SHARED_LIBS:BOOL=OFF \
    -DLLVM_BUILD_LLVM_DYLIB:BOOL=ON \
    -DLLVM_LINK_LLVM_DYLIB:BOOL=ON \
    -DCLANG_LINK_CLANG_DYLIB:BOOL=ON \
    -DLLVM_PARALLEL_COMPILE_JOBS="$max_compile_jobs" \
    -DLLVM_PARALLEL_LINK_JOBS="$max_link_jobs" \
%if %{with thin_lto}
    -DLLVM_ENABLE_LTO=Thin \
    -DCMAKE_AR="${LLVM_AR}" \
    -DCMAKE_RANLIB="${LLVM_RANLIB}" \
%endif
%ifarch %arm ppc s390 %{ix86}
    -DCMAKE_C_FLAGS_RELWITHDEBINFO="-g1" \
    -DCMAKE_CXX_FLAGS_RELWITHDEBINFO="-g1" \
%endif
    -DENABLE_LINKER_BUILD_ID=ON \
    -DLLVM_TABLEGEN="${LLVM_TABLEGEN}" \
    -DCLANG_TABLEGEN="${CLANG_TABLEGEN}" \
    -DLLVM_ENABLE_RTTI:BOOL=ON \
    -DLLVM_ENABLE_ASSERTIONS=OFF \
    -DLLVM_ENABLE_PIC=ON \
    -DLLVM_BINUTILS_INCDIR=%{_includedir} \
    -DLLVM_TARGETS_TO_BUILD=${TARGETS_TO_BUILD} \
%if %{with libcxx}
    -DLIBCXX_ENABLE_SHARED=YES \
    -DLIBCXX_ENABLE_STATIC=NO \
    -DLIBCXX_ENABLE_EXPERIMENTAL_LIBRARY=NO \
    -DLIBCXXABI_ENABLE_SHARED=YES \
    -DLIBCXXABI_ENABLE_STATIC=NO \
%endif
%if %{with gold}
    -DLLVM_USE_LINKER=gold \
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
    -DCMAKE_SKIP_RPATH:BOOL=OFF \
    -DCMAKE_EXE_LINKER_FLAGS="-Wl,--as-needed -Wl,--build-id=sha1" \
    -DCMAKE_MODULE_LINKER_FLAGS="-Wl,--as-needed -Wl,--build-id=sha1" \
    -DCMAKE_SHARED_LINKER_FLAGS="-Wl,--as-needed -Wl,--build-id=sha1" \
    -DPYTHON_EXECUTABLE:FILEPATH=%{_bindir}/python3 \
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
%cmake_install

# Remove files that won't be needed anymore.
# This reduces the total amount of disk space used during build. (bnc#1074625)
find ./build \( -name '*.o' -or -name '*.a' \)  -delete

# Docs are prebuilt due to sphinx dependency
#
# tar xf llvm-%{_version}.src.tar.xz
# tar xf clang-%{_version}.src.tar.xz
# pushd llvm-%{_version}.src/docs
# make -f Makefile.sphinx man html
# popd
# pushd clang-%{_version}.src/docs
# make -f Makefile.sphinx man html
# popd
# tar cvJf llvm-docs-%{_version}.src.tar.xz llvm-%{_version}.src/docs/_build/{man,html}
# tar cvJf clang-docs-%{_version}.src.tar.xz clang-%{_version}.src/docs/_build/{man,html}

# Build man/html pages
pushd docs
rm -rf %{buildroot}%{_prefix}/docs
mkdir -p %{buildroot}%{_docdir}/llvm/html
mkdir -p %{buildroot}%{_mandir}/man1
cp -r _build/man/* %{buildroot}%{_mandir}/man1
cp -r _build/html/* %{buildroot}%{_docdir}/llvm/html
popd

pushd tools/clang/docs
mkdir -p %{buildroot}%{_docdir}/llvm-clang/html
cp -r _build/man/* %{buildroot}%{_mandir}/man1
cp -r _build/html/* %{buildroot}%{_docdir}/llvm-clang/html
popd

# install python bindings
# The python bindings use the unversioned libclang.so,
# so it doesn't make sense to have multiple versions of it
%if %{with clang_scripts}
install -d %{buildroot}%{python3_sitelib}/clang
pushd tools/clang/bindings/python
cp clang/*.py %{buildroot}%{python3_sitelib}/clang
install -d %{buildroot}%{_docdir}/python-clang/examples/cindex
cp -r examples %{buildroot}%{_docdir}/python-clang
install -d %{buildroot}%{_docdir}/python-clang/tests/cindex/INPUTS
cp -r tests %{buildroot}%{_docdir}/python-clang
popd
%endif

# Note that bfd-plugins is always in /usr/lib/bfd-plugins, no matter what _libdir is.
mkdir -p %{buildroot}%{_prefix}/lib/bfd-plugins
ln -s %{_libdir}/LLVMgold.so %{buildroot}%{_prefix}/lib/bfd-plugins/

install -m 755 -d %{buildroot}%{_datadir}/vim/site/
for i in ftdetect ftplugin indent syntax; do
    cp -r utils/vim/$i %{buildroot}%{_datadir}/vim/site/
done
mv utils/vim/README utils/vim/README.vim

mv %{buildroot}%{_prefix}/libexec/{c++,ccc}-analyzer %{buildroot}%{_bindir}
mv %{buildroot}%{_datadir}/clang/clang-format-diff.py %{buildroot}%{_bindir}/clang-format-diff
mv %{buildroot}%{_datadir}/clang/clang-tidy-diff.py %{buildroot}%{_bindir}/clang-tidy-diff
mv %{buildroot}%{_datadir}/clang/run-clang-tidy.py %{buildroot}%{_bindir}/run-clang-tidy
mv %{buildroot}%{_datadir}/clang/run-find-all-symbols.py %{buildroot}%{_bindir}/run-find-all-symbols

install -d %{buildroot}%{python3_sitelib}
mv %{buildroot}%{_datadir}/opt-viewer/opt-diff.py %{buildroot}%{_bindir}/opt-diff
mv %{buildroot}%{_datadir}/opt-viewer/opt-stats.py %{buildroot}%{_bindir}/opt-stats
mv %{buildroot}%{_datadir}/opt-viewer/opt-viewer.py %{buildroot}%{_bindir}/opt-viewer
mv %{buildroot}%{_datadir}/opt-viewer/optpmap.py %{buildroot}%{python3_sitelib}/optpmap.py
mv %{buildroot}%{_datadir}/opt-viewer/optrecord.py %{buildroot}%{python3_sitelib}/optrecord.py

mkdir -p %{buildroot}%{_datadir}/bash-completion/completions
mv %{buildroot}%{_datadir}/clang/bash-autocomplete.sh %{buildroot}%{_datadir}/bash-completion/completions/clang

mv %{buildroot}%{_mandir}/man1/{,llvm-}tblgen.1
rm %{buildroot}%{_mandir}/man1/{FileCheck,llvm-locstats}.1
chmod -x %{buildroot}%{_mandir}/man1/scan-build.1

%if %{with lldb_python}
# Python: fix binary libraries location.
rm %{buildroot}%{python3_sitearch}/lldb/_lldb.so
liblldb=$(basename $(readlink -e %{buildroot}%{_libdir}/liblldb.so))
ln -vsf "../../../${liblldb}" %{buildroot}%{python3_sitearch}/lldb/_lldb.so

# Remove bundled six.py.
rm -f %{buildroot}%{python3_sitearch}/six.*
%endif

# Stuff we don't want to include
rm %{buildroot}%{_mandir}/man1/lit.1

rm -rf %{buildroot}%{_includedir}/lld

%if %{with openmp}
rm %{buildroot}%{_libdir}/libgomp.so
rm %{buildroot}%{_libdir}/libiomp*.so
rm %{buildroot}%{_libdir}/libarcher_static.a
%endif

# We don't care about applescript or sublime text
rm %{buildroot}%{_datadir}/clang/*.applescript
rm %{buildroot}%{_datadir}/clang/clang-format-sublime.py

# Prepare for update-alternatives usage
mkdir -p %{buildroot}%{_sysconfdir}/alternatives
binfiles=( bugpoint dsymutil llc lli \
           llvm-addr2line llvm-ar llvm-as llvm-bcanalyzer llvm-c-test llvm-cat llvm-cfi-verify
           llvm-cov llvm-cxxdump llvm-cxxfilt llvm-cxxmap llvm-cvtres llvm-diff llvm-dis \
           llvm-dlltool llvm-dwarfdump llvm-dwp llvm-elfabi llvm-exegesis llvm-extract llvm-ifs \
           llvm-install-name-tool llvm-jitlink llvm-lib llvm-link llvm-lipo llvm-lto llvm-lto2 llvm-mc llvm-mca \
           llvm-mt llvm-modextract llvm-nm llvm-objcopy llvm-objdump llvm-opt-report \
           llvm-pdbutil llvm-profdata llvm-ranlib llvm-rc llvm-readelf llvm-readobj llvm-reduce \
           llvm-rtdyld llvm-size llvm-split llvm-stress llvm-strings llvm-strip \
           llvm-symbolizer llvm-tblgen llvm-undname llvm-xray obj2yaml opt sancov \
           sanstats verify-uselistorder yaml2obj \
           c-index-test clang clangd clang++ clang-apply-replacements \
           clang-change-namespace clang-check clang-cl clang-extdef-mapping clang-format \
           clang-import-test clang-include-fixer clang-move clang-offload-bundler \
           clang-offload-wrapper clang-query clang-refactor clang-scan-deps clang-rename \
           clang-reorder-fields clang-tidy diagtool find-all-symbols modularize pp-trace \
%if %{with lldb}
           lldb lldb-argdumper lldb-instr lldb-server lldb-vscode \
%endif
%if %{with lld}
           ld.lld lld lld-link ld64.lld wasm-ld \
%endif
	   )
manfiles=( bugpoint dsymutil llc lli \
           llvm-addr2line llvm-ar llvm-as llvm-bcanalyzer llvm-build llvm-cov llvm-cxxfilt llvm-cxxmap llvm-diff \
           llvm-dis llvm-dwarfdump llvm-exegesis llvm-extract llvm-lib llvm-link llvm-lipo llvm-mca \
           llvm-nm llvm-objcopy llvm-objdump llvm-pdbutil llvm-profdata llvm-ranlib llvm-readelf llvm-readobj \
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
%_llvm_with_clang_scripts %{with clang_scripts}
%_llvm_with_lldb %{with lldb}
EOF

# Don't use env in shebangs, and prefer python3. (https://www.python.org/dev/peps/pep-0394/#for-python-runtime-distributors)
for script in %{buildroot}%{_bindir}/{clang-{format,tidy}-diff,git-clang-format,\
hmaptool,run-{clang-tidy,find-all-symbols},scan-{build,view},opt-{diff,stats,viewer}} \
%ifarch aarch64 x86_64
        %{buildroot}%{_libdir}/clang/%{_relver}/bin/hwasan_symbolize \
%endif
        %{buildroot}%{python3_sitelib}/optrecord.py; do
    sed -i '1s|/usr/bin/env *|%{_bindir}/|;1s|/usr/bin/python$|%{_bindir}/python3|' $script
done

# Remove executable bit where not needed.
chmod -x \
  %{buildroot}%{python3_sitelib}/optpmap.py \
  %{buildroot}%{_datadir}/bash-completion/completions/clang \
  %{buildroot}%{_datadir}/clang/clang-{format,include-fixer,rename}.{el,py} \
  %{buildroot}%{_datadir}/opt-viewer/style.css

%if !%{with clang_scripts}
rm %{buildroot}%{_bindir}/{c++,ccc}-analyzer
rm %{buildroot}%{_bindir}/clang-{doc,format-diff,tidy-diff}
rm %{buildroot}%{_bindir}/git-clang-format
rm %{buildroot}%{_bindir}/hmaptool
rm %{buildroot}%{_bindir}/run-{clang-tidy,find-all-symbols}
rm %{buildroot}%{_bindir}/scan-{build,view}
rm %{buildroot}%{_datadir}/bash-completion/completions/clang
rm -r %{buildroot}%{_datadir}/{clang,scan-build,scan-view}/
rm %{buildroot}%{_mandir}/man1/scan-build.1
%endif

# Remove documentation sources.
rm -r %{buildroot}%{_docdir}/llvm{,-clang}/html/_sources

%fdupes -s %{buildroot}%{_docdir}/llvm
%fdupes -s %{buildroot}%{_docdir}/llvm-clang
%fdupes %{_includedir}/%{name}/Host/

%check
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

# On armv6l, fpext frem(12.0f, 5.0f) to double = inf for some reason.
sed -i '1i; XFAIL: armv6' ../test/ExecutionEngine/frem.ll
# Tests are disabled on ppc because of sporadic hangs. Also some tests fail.
%ifnarch ppc
python3 bin/llvm-lit -sv test/
%endif
python3 bin/llvm-lit -sv --param clang_site_config=tools/clang/test/lit.site.cfg \
	--param USE_Z3_SOLVER=0 tools/clang/test/

%if %{with libcxx}
# libcxx tests take too long on ARM.
%ifnarch %{arm}
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
%post -n libclang%{_sonum} -p /sbin/ldconfig
%postun -n libclang%{_sonum} -p /sbin/ldconfig
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
%post LTO-devel -p /sbin/ldconfig
%postun LTO-devel -p /sbin/ldconfig

%if %{with openmp}
%post -n libomp%{_sonum}-devel -p /sbin/ldconfig
%postun -n libomp%{_sonum}-devel -p /sbin/ldconfig
%endif

%if %{with libcxx}
%post -n libc++%{_socxx} -p /sbin/ldconfig
%postun -n libc++%{_socxx} -p /sbin/ldconfig
%post -n libc++abi%{_socxx} -p /sbin/ldconfig
%postun -n libc++abi%{_socxx} -p /sbin/ldconfig
%post -n libc++-devel -p /sbin/ldconfig
%postun -n libc++-devel -p /sbin/ldconfig
%post -n libc++abi-devel -p /sbin/ldconfig
%postun -n libc++abi-devel -p /sbin/ldconfig
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
   --slave %{_bindir}/llvm-elfabi llvm-elfabi %{_bindir}/llvm-elfabi-%{_relver} \
   --slave %{_bindir}/llvm-exegesis llvm-exegesis %{_bindir}/llvm-exegesis-%{_relver} \
   --slave %{_bindir}/llvm-extract llvm-extract %{_bindir}/llvm-extract-%{_relver} \
   --slave %{_bindir}/llvm-ifs llvm-ifs %{_bindir}/llvm-ifs-%{_relver} \
   --slave %{_bindir}/llvm-install-name-tool llvm-install-name-tool %{_bindir}/llvm-install-name-tool-%{_relver} \
   --slave %{_bindir}/llvm-jitlink llvm-jitlink %{_bindir}/llvm-jitlink-%{_relver} \
   --slave %{_bindir}/llvm-lib llvm-lib %{_bindir}/llvm-lib-%{_relver} \
   --slave %{_bindir}/llvm-link llvm-link %{_bindir}/llvm-link-%{_relver} \
   --slave %{_bindir}/llvm-lipo llvm-lipo %{_bindir}/llvm-lipo-%{_relver} \
   --slave %{_bindir}/llvm-lto llvm-lto %{_bindir}/llvm-lto-%{_relver} \
   --slave %{_bindir}/llvm-lto2 llvm-lto2 %{_bindir}/llvm-lto2-%{_relver} \
   --slave %{_bindir}/llvm-mc llvm-mc %{_bindir}/llvm-mc-%{_relver} \
   --slave %{_bindir}/llvm-mca llvm-mca %{_bindir}/llvm-mca-%{_relver} \
   --slave %{_bindir}/llvm-mt llvm-mt %{_bindir}/llvm-mt-%{_relver} \
   --slave %{_bindir}/llvm-modextract llvm-modextract %{_bindir}/llvm-modextract-%{_relver} \
   --slave %{_bindir}/llvm-nm llvm-nm %{_bindir}/llvm-nm-%{_relver} \
   --slave %{_bindir}/llvm-objcopy llvm-objcopy %{_bindir}/llvm-objcopy-%{_relver} \
   --slave %{_bindir}/llvm-objdump llvm-objdump %{_bindir}/llvm-objdump-%{_relver} \
   --slave %{_bindir}/llvm-opt-report llvm-opt-report %{_bindir}/llvm-opt-report-%{_relver} \
   --slave %{_bindir}/llvm-pdbutil llvm-pdbutil %{_bindir}/llvm-pdbutil-%{_relver} \
   --slave %{_bindir}/llvm-profdata llvm-profdata %{_bindir}/llvm-profdata-%{_relver} \
   --slave %{_bindir}/llvm-ranlib llvm-ranlib %{_bindir}/llvm-ranlib-%{_relver} \
   --slave %{_bindir}/llvm-rc llvm-rc %{_bindir}/llvm-rc-%{_relver} \
   --slave %{_bindir}/llvm-readelf llvm-readelf %{_bindir}/llvm-readelf-%{_relver} \
   --slave %{_bindir}/llvm-readobj llvm-readobj %{_bindir}/llvm-readobj-%{_relver} \
   --slave %{_bindir}/llvm-reduce llvm-reduce %{_bindir}/llvm-reduce-%{_relver} \
   --slave %{_bindir}/llvm-rtdyld llvm-rtdyld %{_bindir}/llvm-rtdyld-%{_relver} \
   --slave %{_bindir}/llvm-size llvm-size %{_bindir}/llvm-size-%{_relver} \
   --slave %{_bindir}/llvm-split llvm-split %{_bindir}/llvm-split-%{_relver} \
   --slave %{_bindir}/llvm-stress llvm-stress %{_bindir}/llvm-stress-%{_relver} \
   --slave %{_bindir}/llvm-strings llvm-strings %{_bindir}/llvm-strings-%{_relver} \
   --slave %{_bindir}/llvm-strip llvm-strip %{_bindir}/llvm-strip-%{_relver} \
   --slave %{_bindir}/llvm-symbolizer llvm-symbolizer %{_bindir}/llvm-symbolizer-%{_relver} \
   --slave %{_bindir}/llvm-tblgen llvm-tblgen %{_bindir}/llvm-tblgen-%{_relver} \
   --slave %{_bindir}/llvm-undname llvm-undname %{_bindir}/llvm-undname-%{_relver} \
   --slave %{_bindir}/llvm-xray llvm-xray %{_bindir}/llvm-xray-%{_relver} \
   --slave %{_bindir}/obj2yaml obj2yaml %{_bindir}/obj2yaml-%{_relver} \
   --slave %{_bindir}/opt opt %{_bindir}/opt-%{_relver} \
   --slave %{_bindir}/sancov sancov %{_bindir}/sancov-%{_relver} \
   --slave %{_bindir}/sanstats sanstats %{_bindir}/sanstats-%{_relver} \
   --slave %{_bindir}/verify-uselistorder verify-uselistorder %{_bindir}/verify-uselistorder-%{_relver} \
   --slave %{_bindir}/yaml2obj yaml2obj %{_bindir}/yaml2obj-%{_relver} \
   --slave %{_mandir}/man1/bugpoint.1%{ext_man} bugpoint.1%{ext_man} %{_mandir}/man1/bugpoint-%{_relver}.1%{ext_man} \
   --slave %{_mandir}/man1/dsymutil.1%{ext_man} dsymutil.1%{ext_man} %{_mandir}/man1/dsymutil-%{_relver}.1%{ext_man} \
   --slave %{_mandir}/man1/llc.1%{ext_man} llc.1%{ext_man} %{_mandir}/man1/llc-%{_relver}.1%{ext_man} \
   --slave %{_mandir}/man1/lli.1%{ext_man} lli.1%{ext_man} %{_mandir}/man1/lli-%{_relver}.1%{ext_man} \
   --slave %{_mandir}/man1/llvm-addr2line.1%{ext_man} llvm-addr2line.1%{ext_man} %{_mandir}/man1/llvm-addr2line-%{_relver}.1%{ext_man} \
   --slave %{_mandir}/man1/llvm-ar.1%{ext_man} llvm-ar.1%{ext_man} %{_mandir}/man1/llvm-ar-%{_relver}.1%{ext_man} \
   --slave %{_mandir}/man1/llvm-as.1%{ext_man} llvm-as.1%{ext_man} %{_mandir}/man1/llvm-as-%{_relver}.1%{ext_man} \
   --slave %{_mandir}/man1/llvm-bcanalyzer.1%{ext_man} llvm-bcanalyzer.1%{ext_man} %{_mandir}/man1/llvm-bcanalyzer-%{_relver}.1%{ext_man} \
   --slave %{_mandir}/man1/llvm-build.1%{ext_man} llvm-build.1%{ext_man} %{_mandir}/man1/llvm-build-%{_relver}.1%{ext_man} \
   --slave %{_mandir}/man1/llvm-cov.1%{ext_man} llvm-cov.1%{ext_man} %{_mandir}/man1/llvm-cov-%{_relver}.1%{ext_man} \
   --slave %{_mandir}/man1/llvm-cxxfilt.1%{ext_man} llvm-cxxfilt.1%{ext_man} %{_mandir}/man1/llvm-cxxfilt-%{_relver}.1%{ext_man} \
   --slave %{_mandir}/man1/llvm-cxxmap.1%{ext_man} llvm-cxxmap.1%{ext_man} %{_mandir}/man1/llvm-cxxmap-%{_relver}.1%{ext_man} \
   --slave %{_mandir}/man1/llvm-diff.1%{ext_man} llvm-diff.1%{ext_man} %{_mandir}/man1/llvm-diff-%{_relver}.1%{ext_man} \
   --slave %{_mandir}/man1/llvm-dis.1%{ext_man} llvm-dis.1%{ext_man} %{_mandir}/man1/llvm-dis-%{_relver}.1%{ext_man} \
   --slave %{_mandir}/man1/llvm-dwarfdump.1%{ext_man} llvm-dwarfdump.1%{ext_man} %{_mandir}/man1/llvm-dwarfdump-%{_relver}.1%{ext_man} \
   --slave %{_mandir}/man1/llvm-exegesis.1%{ext_man} llvm-exegesis.1%{ext_man} %{_mandir}/man1/llvm-exegesis-%{_relver}.1%{ext_man} \
   --slave %{_mandir}/man1/llvm-extract.1%{ext_man} llvm-extract.1%{ext_man} %{_mandir}/man1/llvm-extract-%{_relver}.1%{ext_man} \
   --slave %{_mandir}/man1/llvm-lib.1%{ext_man} llvm-lib.1%{ext_man} %{_mandir}/man1/llvm-lib-%{_relver}.1%{ext_man} \
   --slave %{_mandir}/man1/llvm-link.1%{ext_man} llvm-link.1%{ext_man} %{_mandir}/man1/llvm-link-%{_relver}.1%{ext_man} \
   --slave %{_mandir}/man1/llvm-lipo.1%{ext_man} llvm-lipo.1%{ext_man} %{_mandir}/man1/llvm-lipo-%{_relver}.1%{ext_man} \
   --slave %{_mandir}/man1/llvm-mca.1%{ext_man} llvm-mca.1%{ext_man} %{_mandir}/man1/llvm-mca-%{_relver}.1%{ext_man} \
   --slave %{_mandir}/man1/llvm-nm.1%{ext_man} llvm-nm.1%{ext_man} %{_mandir}/man1/llvm-nm-%{_relver}.1%{ext_man} \
   --slave %{_mandir}/man1/llvm-objcopy.1%{ext_man} llvm-objcopy.1%{ext_man} %{_mandir}/man1/llvm-objcopy-%{_relver}.1%{ext_man} \
   --slave %{_mandir}/man1/llvm-objdump.1%{ext_man} llvm-objdump.1%{ext_man} %{_mandir}/man1/llvm-objdump-%{_relver}.1%{ext_man} \
   --slave %{_mandir}/man1/llvm-pdbutil.1%{ext_man} llvm-pdbutil.1%{ext_man} %{_mandir}/man1/llvm-pdbutil-%{_relver}.1%{ext_man} \
   --slave %{_mandir}/man1/llvm-profdata.1%{ext_man} llvm-profdata.1%{ext_man} %{_mandir}/man1/llvm-profdata-%{_relver}.1%{ext_man} \
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
   --slave %{_bindir}/clang-extdef-mapping clang-extdef-mapping %{_bindir}/clang-extdef-mapping-%{_relver} \
   --slave %{_bindir}/clang-format clang-format %{_bindir}/clang-format-%{_relver} \
   --slave %{_bindir}/clang-import-test clang-import-test %{_bindir}/clang-import-test-%{_relver} \
   --slave %{_bindir}/clang-include-fixer clang-include-fixer %{_bindir}/clang-include-fixer-%{_relver} \
   --slave %{_bindir}/clang-move clang-move %{_bindir}/clang-move-%{_relver} \
   --slave %{_bindir}/clang-offload-bundler clang-offload-bundler %{_bindir}/clang-offload-bundler-%{_relver} \
   --slave %{_bindir}/clang-offload-wrapper clang-offload-wrapper %{_bindir}/clang-offload-wrapper-%{_relver} \
   --slave %{_bindir}/clang-query clang-query %{_bindir}/clang-query-%{_relver} \
   --slave %{_bindir}/clang-refactor clang-refactor %{_bindir}/clang-refactor-%{_relver} \
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
%{_bindir}/llvm-elfabi
%{_bindir}/llvm-exegesis
%{_bindir}/llvm-extract
%{_bindir}/llvm-ifs
%{_bindir}/llvm-install-name-tool
%{_bindir}/llvm-jitlink
%{_bindir}/llvm-lib
%{_bindir}/llvm-link
%{_bindir}/llvm-lipo
%{_bindir}/llvm-lto
%{_bindir}/llvm-lto2
%{_bindir}/llvm-mc
%{_bindir}/llvm-mca
%{_bindir}/llvm-mt
%{_bindir}/llvm-modextract
%{_bindir}/llvm-nm
%{_bindir}/llvm-objcopy
%{_bindir}/llvm-objdump
%{_bindir}/llvm-opt-report
%{_bindir}/llvm-pdbutil
%{_bindir}/llvm-profdata
%{_bindir}/llvm-ranlib
%{_bindir}/llvm-rc
%{_bindir}/llvm-readelf
%{_bindir}/llvm-readobj
%{_bindir}/llvm-reduce
%{_bindir}/llvm-rtdyld
%{_bindir}/llvm-size
%{_bindir}/llvm-split
%{_bindir}/llvm-stress
%{_bindir}/llvm-strings
%{_bindir}/llvm-strip
%{_bindir}/llvm-symbolizer
%{_bindir}/llvm-tblgen
%{_bindir}/llvm-undname
%{_bindir}/llvm-xray
%{_bindir}/obj2yaml
%{_bindir}/opt
%{_bindir}/sancov
%{_bindir}/sanstats
%{_bindir}/verify-uselistorder
%{_bindir}/yaml2obj

%{_bindir}/bugpoint-%{_relver}
%{_bindir}/dsymutil-%{_relver}
%{_bindir}/llc-%{_relver}
%{_bindir}/lli-%{_relver}
%{_bindir}/llvm-addr2line-%{_relver}
%{_bindir}/llvm-ar-%{_relver}
%{_bindir}/llvm-as-%{_relver}
%{_bindir}/llvm-bcanalyzer-%{_relver}
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
%{_bindir}/llvm-elfabi-%{_relver}
%{_bindir}/llvm-exegesis-%{_relver}
%{_bindir}/llvm-ifs-%{_relver}
%{_bindir}/llvm-install-name-tool-%{_relver}
%{_bindir}/llvm-extract-%{_relver}
%{_bindir}/llvm-jitlink-%{_relver}
%{_bindir}/llvm-lib-%{_relver}
%{_bindir}/llvm-link-%{_relver}
%{_bindir}/llvm-lipo-%{_relver}
%{_bindir}/llvm-lto-%{_relver}
%{_bindir}/llvm-lto2-%{_relver}
%{_bindir}/llvm-mc-%{_relver}
%{_bindir}/llvm-mca-%{_relver}
%{_bindir}/llvm-mt-%{_relver}
%{_bindir}/llvm-modextract-%{_relver}
%{_bindir}/llvm-nm-%{_relver}
%{_bindir}/llvm-objcopy-%{_relver}
%{_bindir}/llvm-objdump-%{_relver}
%{_bindir}/llvm-opt-report-%{_relver}
%{_bindir}/llvm-pdbutil-%{_relver}
%{_bindir}/llvm-profdata-%{_relver}
%{_bindir}/llvm-ranlib-%{_relver}
%{_bindir}/llvm-rc-%{_relver}
%{_bindir}/llvm-readelf-%{_relver}
%{_bindir}/llvm-readobj-%{_relver}
%{_bindir}/llvm-reduce-%{_relver}
%{_bindir}/llvm-rtdyld-%{_relver}
%{_bindir}/llvm-size-%{_relver}
%{_bindir}/llvm-split-%{_relver}
%{_bindir}/llvm-stress-%{_relver}
%{_bindir}/llvm-strings-%{_relver}
%{_bindir}/llvm-strip-%{_relver}
%{_bindir}/llvm-symbolizer-%{_relver}
%{_bindir}/llvm-tblgen-%{_relver}
%{_bindir}/llvm-undname-%{_relver}
%{_bindir}/llvm-xray-%{_relver}
%{_bindir}/obj2yaml-%{_relver}
%{_bindir}/opt-%{_relver}
%{_bindir}/sancov-%{_relver}
%{_bindir}/sanstats-%{_relver}
%{_bindir}/verify-uselistorder-%{_relver}
%{_bindir}/yaml2obj-%{_relver}

%ghost %{_sysconfdir}/alternatives/bugpoint
%ghost %{_sysconfdir}/alternatives/dsymutil
%ghost %{_sysconfdir}/alternatives/llc
%ghost %{_sysconfdir}/alternatives/lli
%ghost %{_sysconfdir}/alternatives/llvm-addr2line
%ghost %{_sysconfdir}/alternatives/llvm-ar
%ghost %{_sysconfdir}/alternatives/llvm-as
%ghost %{_sysconfdir}/alternatives/llvm-bcanalyzer
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
%ghost %{_sysconfdir}/alternatives/llvm-elfabi
%ghost %{_sysconfdir}/alternatives/llvm-exegesis
%ghost %{_sysconfdir}/alternatives/llvm-extract
%ghost %{_sysconfdir}/alternatives/llvm-ifs
%ghost %{_sysconfdir}/alternatives/llvm-install-name-tool
%ghost %{_sysconfdir}/alternatives/llvm-jitlink
%ghost %{_sysconfdir}/alternatives/llvm-lib
%ghost %{_sysconfdir}/alternatives/llvm-link
%ghost %{_sysconfdir}/alternatives/llvm-lipo
%ghost %{_sysconfdir}/alternatives/llvm-lto
%ghost %{_sysconfdir}/alternatives/llvm-lto2
%ghost %{_sysconfdir}/alternatives/llvm-mc
%ghost %{_sysconfdir}/alternatives/llvm-mca
%ghost %{_sysconfdir}/alternatives/llvm-mt
%ghost %{_sysconfdir}/alternatives/llvm-modextract
%ghost %{_sysconfdir}/alternatives/llvm-nm
%ghost %{_sysconfdir}/alternatives/llvm-objcopy
%ghost %{_sysconfdir}/alternatives/llvm-objdump
%ghost %{_sysconfdir}/alternatives/llvm-opt-report
%ghost %{_sysconfdir}/alternatives/llvm-pdbutil
%ghost %{_sysconfdir}/alternatives/llvm-profdata
%ghost %{_sysconfdir}/alternatives/llvm-ranlib
%ghost %{_sysconfdir}/alternatives/llvm-rc
%ghost %{_sysconfdir}/alternatives/llvm-readelf
%ghost %{_sysconfdir}/alternatives/llvm-readobj
%ghost %{_sysconfdir}/alternatives/llvm-reduce
%ghost %{_sysconfdir}/alternatives/llvm-rtdyld
%ghost %{_sysconfdir}/alternatives/llvm-size
%ghost %{_sysconfdir}/alternatives/llvm-split
%ghost %{_sysconfdir}/alternatives/llvm-stress
%ghost %{_sysconfdir}/alternatives/llvm-strings
%ghost %{_sysconfdir}/alternatives/llvm-strip
%ghost %{_sysconfdir}/alternatives/llvm-symbolizer
%ghost %{_sysconfdir}/alternatives/llvm-tblgen
%ghost %{_sysconfdir}/alternatives/llvm-undname
%ghost %{_sysconfdir}/alternatives/llvm-xray
%ghost %{_sysconfdir}/alternatives/obj2yaml
%ghost %{_sysconfdir}/alternatives/opt
%ghost %{_sysconfdir}/alternatives/sancov
%ghost %{_sysconfdir}/alternatives/sanstats
%ghost %{_sysconfdir}/alternatives/verify-uselistorder
%ghost %{_sysconfdir}/alternatives/yaml2obj

%{_mandir}/man1/bugpoint.1%{ext_man}
%{_mandir}/man1/dsymutil.1%{ext_man}
%{_mandir}/man1/llc.1%{ext_man}
%{_mandir}/man1/lli.1%{ext_man}
%{_mandir}/man1/llvm-addr2line.1%{ext_man}
%{_mandir}/man1/llvm-ar.1%{ext_man}
%{_mandir}/man1/llvm-as.1%{ext_man}
%{_mandir}/man1/llvm-bcanalyzer.1%{ext_man}
%{_mandir}/man1/llvm-build.1%{ext_man}
%{_mandir}/man1/llvm-cov.1%{ext_man}
%{_mandir}/man1/llvm-cxxfilt.1%{ext_man}
%{_mandir}/man1/llvm-cxxmap.1%{ext_man}
%{_mandir}/man1/llvm-diff.1%{ext_man}
%{_mandir}/man1/llvm-dis.1%{ext_man}
%{_mandir}/man1/llvm-dwarfdump.1%{ext_man}
%{_mandir}/man1/llvm-exegesis.1%{ext_man}
%{_mandir}/man1/llvm-extract.1%{ext_man}
%{_mandir}/man1/llvm-lib.1%{ext_man}
%{_mandir}/man1/llvm-link.1%{ext_man}
%{_mandir}/man1/llvm-lipo.1%{ext_man}
%{_mandir}/man1/llvm-mca.1%{ext_man}
%{_mandir}/man1/llvm-nm.1%{ext_man}
%{_mandir}/man1/llvm-objcopy.1%{ext_man}
%{_mandir}/man1/llvm-objdump.1%{ext_man}
%{_mandir}/man1/llvm-pdbutil.1%{ext_man}
%{_mandir}/man1/llvm-profdata.1%{ext_man}
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
%{_mandir}/man1/llvm-build-%{_relver}.1%{ext_man}
%{_mandir}/man1/llvm-cov-%{_relver}.1%{ext_man}
%{_mandir}/man1/llvm-cxxfilt-%{_relver}.1%{ext_man}
%{_mandir}/man1/llvm-cxxmap-%{_relver}.1%{ext_man}
%{_mandir}/man1/llvm-diff-%{_relver}.1%{ext_man}
%{_mandir}/man1/llvm-dis-%{_relver}.1%{ext_man}
%{_mandir}/man1/llvm-dwarfdump-%{_relver}.1%{ext_man}
%{_mandir}/man1/llvm-exegesis-%{_relver}.1%{ext_man}
%{_mandir}/man1/llvm-extract-%{_relver}.1%{ext_man}
%{_mandir}/man1/llvm-lib-%{_relver}.1%{ext_man}
%{_mandir}/man1/llvm-link-%{_relver}.1%{ext_man}
%{_mandir}/man1/llvm-lipo-%{_relver}.1%{ext_man}
%{_mandir}/man1/llvm-mca-%{_relver}.1%{ext_man}
%{_mandir}/man1/llvm-nm-%{_relver}.1%{ext_man}
%{_mandir}/man1/llvm-objcopy-%{_relver}.1%{ext_man}
%{_mandir}/man1/llvm-objdump-%{_relver}.1%{ext_man}
%{_mandir}/man1/llvm-pdbutil-%{_relver}.1%{ext_man}
%{_mandir}/man1/llvm-profdata-%{_relver}.1%{ext_man}
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
%ghost %{_sysconfdir}/alternatives/llvm-build.1%{ext_man}
%ghost %{_sysconfdir}/alternatives/llvm-cov.1%{ext_man}
%ghost %{_sysconfdir}/alternatives/llvm-cxxfilt.1%{ext_man}
%ghost %{_sysconfdir}/alternatives/llvm-cxxmap.1%{ext_man}
%ghost %{_sysconfdir}/alternatives/llvm-diff.1%{ext_man}
%ghost %{_sysconfdir}/alternatives/llvm-dis.1%{ext_man}
%ghost %{_sysconfdir}/alternatives/llvm-dwarfdump.1%{ext_man}
%ghost %{_sysconfdir}/alternatives/llvm-exegesis.1%{ext_man}
%ghost %{_sysconfdir}/alternatives/llvm-extract.1%{ext_man}
%ghost %{_sysconfdir}/alternatives/llvm-lib.1%{ext_man}
%ghost %{_sysconfdir}/alternatives/llvm-link.1%{ext_man}
%ghost %{_sysconfdir}/alternatives/llvm-lipo.1%{ext_man}
%ghost %{_sysconfdir}/alternatives/llvm-mca.1%{ext_man}
%ghost %{_sysconfdir}/alternatives/llvm-nm.1%{ext_man}
%ghost %{_sysconfdir}/alternatives/llvm-objcopy.1%{ext_man}
%ghost %{_sysconfdir}/alternatives/llvm-objdump.1%{ext_man}
%ghost %{_sysconfdir}/alternatives/llvm-pdbutil.1%{ext_man}
%ghost %{_sysconfdir}/alternatives/llvm-profdata.1%{ext_man}
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
%{_bindir}/clang-import-test
%{_bindir}/clang-include-fixer
%{_bindir}/clang-move
%{_bindir}/clang-offload-bundler
%{_bindir}/clang-offload-wrapper
%{_bindir}/clang-query
%{_bindir}/clang-refactor
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
%{_bindir}/clang-extdef-mapping-%{_relver}
%{_bindir}/clang-format-%{_relver}
%{_bindir}/clang-import-test-%{_relver}
%{_bindir}/clang-include-fixer-%{_relver}
%{_bindir}/clang-move-%{_relver}
%{_bindir}/clang-offload-bundler-%{_relver}
%{_bindir}/clang-offload-wrapper-%{_relver}
%{_bindir}/clang-query-%{_relver}
%{_bindir}/clang-refactor-%{_relver}
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
%ghost %{_sysconfdir}/alternatives/clang-extdef-mapping
%ghost %{_sysconfdir}/alternatives/clang-format
%ghost %{_sysconfdir}/alternatives/clang-import-test
%ghost %{_sysconfdir}/alternatives/clang-include-fixer
%ghost %{_sysconfdir}/alternatives/clang-move
%ghost %{_sysconfdir}/alternatives/clang-offload-bundler
%ghost %{_sysconfdir}/alternatives/clang-offload-wrapper
%ghost %{_sysconfdir}/alternatives/clang-query
%ghost %{_sysconfdir}/alternatives/clang-refactor
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
%ifnarch riscv64
%{_libdir}/clang/%{_relver}/share
%endif
%endif

%if %{with clang_scripts}
%files -n clang-tools
%license CREDITS.TXT LICENSE.TXT
%{_bindir}/c++-analyzer
%{_bindir}/ccc-analyzer
%{_bindir}/clang-doc
%{_bindir}/clang-format-diff
%{_bindir}/clang-tidy-diff
%{_bindir}/git-clang-format
%{_bindir}/hmaptool
%{_bindir}/run-clang-tidy
%{_bindir}/run-find-all-symbols
%{_bindir}/scan-build
%{_bindir}/scan-view
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

%files -n libclang%{_sonum}
%license CREDITS.TXT LICENSE.TXT
%{_libdir}/libclang*.so.*
%dir %{_libdir}/clang/
%dir %{_libdir}/clang/%{_relver}/
%{_libdir}/clang/%{_relver}/include

%files -n libLTO%{_sonum}
%license CREDITS.TXT LICENSE.TXT
%{_libdir}/libLTO.so.*

%files gold
%license CREDITS.TXT LICENSE.TXT
%{_libdir}/LLVMgold.so
# Note that bfd-plugins is always in /usr/lib/bfd-plugins, no matter what _libdir is.
%dir %{_prefix}/lib/bfd-plugins/
%{_prefix}/lib/bfd-plugins/LLVMgold.so

%if %{with openmp}
%files -n libomp%{_sonum}-devel
%license CREDITS.TXT LICENSE.TXT
%{_libdir}/libarcher.so
%{_libdir}/libomp.so
%{_libdir}/libomptarget.so
%endif

%if %{with libcxx}
%files -n libc++%{_socxx}
%license CREDITS.TXT LICENSE.TXT
%{_libdir}/libc++.so.*

%files -n libc++abi%{_socxx}
%license CREDITS.TXT LICENSE.TXT
%{_libdir}/libc++abi.so.*

%files -n libc++-devel
%license CREDITS.TXT LICENSE.TXT
%{_libdir}/libc++.so
%dir %{_includedir}/c++/
%{_includedir}/c++/v%{_socxx}

%files -n libc++abi-devel
%license CREDITS.TXT LICENSE.TXT
%{_libdir}/libc++abi.so
%endif

%files devel
%license CREDITS.TXT LICENSE.TXT
%{_bindir}/llvm-config
%{_libdir}/libLLVM.so
%{_libdir}/libLLVMTableGen.so
%{_libdir}/libRemarks.so
%{_includedir}/llvm/
%{_includedir}/llvm-c/
%{_libdir}/cmake/llvm
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

%files LTO-devel
%license CREDITS.TXT LICENSE.TXT
%{_libdir}/libLTO.so

%files vim-plugins
%license CREDITS.TXT LICENSE.TXT
%doc utils/vim/README.vim
%{_datadir}/vim/

%if %{with clang_scripts}
%files -n python3-clang
%license CREDITS.TXT LICENSE.TXT
%{python3_sitelib}/clang/
%{_docdir}/python-clang/
%endif

%if %{with lld}
%files -n lld%{_sonum}
%license CREDITS.TXT LICENSE.TXT
%{_bindir}/ld.lld
%{_bindir}/ld64.lld
%{_bindir}/lld
%{_bindir}/lld-link
%{_bindir}/wasm-ld
%{_bindir}/ld.lld-%{_relver}
%{_bindir}/ld64.lld-%{_relver}
%{_bindir}/lld-%{_relver}
%{_bindir}/lld-link-%{_relver}
%{_bindir}/wasm-ld-%{_relver}
%ghost %{_sysconfdir}/alternatives/ld.lld
%ghost %{_sysconfdir}/alternatives/ld64.lld
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
