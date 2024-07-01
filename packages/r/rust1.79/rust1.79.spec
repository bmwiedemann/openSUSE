#
# spec file for package rust1.79
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2019 Luke Jones, luke@ljones.dev
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


%global version_suffix 1.79
%global version_current 1.79.0
%global version_previous 1.78.0
# This has to be kept lock step to the rust version.
# -- will be 18 for 1.78
%global llvm_version 18
%if 0%{?sle_version} <= 150900 && 0%{?suse_version} < 1599
# We may need a minimum gcc version for some linker flags
# This is especially true on leap/sle
#
# ⚠️   11 or greater is required for a number of linker flags to be supported in sle.
#
%global gcc_version 13
%endif

#KEEP NOSOURCE DEBUGINFO

%define obsolete_rust_versioned() \
Obsoletes:      %{1}1.78%{?2:-%{2}} \
Obsoletes:      %{1}1.77%{?2:-%{2}} \
Obsoletes:      %{1}1.76%{?2:-%{2}} \
Obsoletes:      %{1}1.75%{?2:-%{2}} \
Obsoletes:      %{1}1.74%{?2:-%{2}} \
Obsoletes:      %{1}1.73%{?2:-%{2}} \
Obsoletes:      %{1}1.72%{?2:-%{2}} \
Obsoletes:      %{1}1.71%{?2:-%{2}} \
Obsoletes:      %{1}1.70%{?2:-%{2}} \
Obsoletes:      %{1}1.69%{?2:-%{2}} \
Obsoletes:      %{1}1.68%{?2:-%{2}} \
Obsoletes:      %{1}1.67%{?2:-%{2}} \
Obsoletes:      %{1}1.66%{?2:-%{2}} \
Obsoletes:      %{1}1.65%{?2:-%{2}} \
Obsoletes:      %{1}1.64%{?2:-%{2}} \
Obsoletes:      %{1}1.63%{?2:-%{2}} \
Obsoletes:      %{1}1.62%{?2:-%{2}}

# ⚠️  Must leave 1.62 here due to kernel requirements.

# Build the rust target triple.
# Some rust arches don't match what SUSE labels them.
%global rust_arch %{_arch}
%global abi gnu

%ifarch armv7hl
%global rust_arch armv7
%global abi gnueabihf
%endif

%ifarch armv6hl
%global rust_arch arm
%global abi gnueabihf
%endif

%ifarch ppc
%global rust_arch powerpc
%endif

%ifarch ppc64
%global rust_arch powerpc64
%endif

%ifarch ppc64le
%global rust_arch powerpc64le
%endif

%ifarch riscv64
%global rust_arch riscv64gc
%endif

# Must restrict the x86 build to i686 since i586 is currently
# unsupported
%ifarch %{ix86}
%global rust_arch i686
%endif

%global rust_triple %{rust_arch}-unknown-linux-%{abi}

# Web Assembly targets
%define rust_wasm_targets %{?with_wasm32:,wasm32-unknown-unknown%{?with_wasi:,wasm32-wasi}}

# Base Rust targets for all architectures
%define rust_base_targets %{rust_triple}%{rust_wasm_targets}

# For x86-64 add the x86_64-unknown-none target
%ifarch x86_64
%define rust_target_list %{rust_base_targets},x86_64-unknown-none
%else
%define rust_target_list %{rust_base_targets}
%endif

# All sources and bootstraps are fetched form here
%global dl_url https://static.rust-lang.org/dist

# Rust doesn't function well when put in /usr/lib64
%global common_libdir %{_prefix}/lib
%global rustlibdir %{common_libdir}/rustlib

# Detect if sccache has been requested by the build
%if "%{getenv:RUSTC_WRAPPER}" == "sccache"
%bcond_without sccache
%else
%bcond_with sccache
%endif

# === rust arch support tiers ===
# https://doc.rust-lang.org/nightly/rustc/platform-support.html
# tl;dr only aarch64, x86_64 and i686 are guaranteed to work.
#
# armv6/7, s390x, ppc[64[le]], riscv are all "guaranteed to build" only
# but may not always work.

# === broken distro llvm ===
# In some situations the llvm provided on the platform may not work.
# we add these conditions here.
#
# ⚠️   SLE/LEAP 15.3 LLVM is too old!
# ⚠️   1.59 breaks codegen with distro llvm!!!

%if 0%{?is_opensuse} == 1 && 0%{?suse_version} >= 1699
# && "{version_suffix}" != "1.61"
# Can proceed with pinned llvm.
%bcond_with bundled_llvm
%else
# Use bundled llvm instead.
# For details see boo#1192067
%bcond_without bundled_llvm
%endif

# === Use clang/lld during build if possible ===
# i586 - unable to link libatomic
# aarch64 - fails due to an invalid linker flag
#
%bcond_with llvmtools

# Depending on our environment, we may need to configure our linker in a different manner.

# If we elect for llvm, always use clang.
%if %{with llvmtools}
%define rust_linker clang
%else
%if 0%{?gcc_version} != 0
%define rust_linker gcc-%{gcc_version}
%else
%define rust_linker cc
%endif
%endif

# === Enable wasm/wasi on t1 targets ===
%if 0%{?is_opensuse} == 1 && 0%{?suse_version} >= 1699
%ifarch x86_64 aarch64
%bcond_without wasm32
%bcond_without wasi
%else
%bcond_with wasm32
%bcond_with wasi
%endif
%else
%bcond_with wasm32
%bcond_with wasi
%endif

# Test is done in a different multibuild package (rustXXX-test).  This
# package will replace the local-rust-root and use the systems's one
# from the rustXXX package itself.  This will exercise the compiler,
# even tho, the tests will require more compilation.  If we do not
# agree on this model we can drop the _multibuild option and do the
# pct check as a part of the main spec.

%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif

# """
# Do not use parallel codegen in order to
#   a) not exhaust memory on build-machines and
#   b) generate the fastest possible binary
# at the cost of longer build times for this package
# """
#
# These claims are incorrect
# a) codegen=1, actually consumes MORE memory due to the fact that the full
# code unit is then LTO'd in a single pass. This can cause LLVM to internally OOM
# especially if the machine has less than 1G of ram, and this is documented:
#  * https://github.com/rust-lang/rust/issues/85598
# it has also been observed in OBS during builds of 1.52 and 1.53
#
# b) the performance gains from codegen=1 are minimal at best, and not worth
# us messing about with these values - especially when the rust language team
# probably know more about how to set and tune these based on data and research
#
# Debuginfo can exhaust memory on these architecture workers
%ifarch %{arm} %{ix86}
%define debug_info --debuginfo-level=0 --debuginfo-level-rustc=0 --debuginfo-level-std=0 --debuginfo-level-tools=0 --debuginfo-level-tests=0
%else
%define debug_info %{nil}
%endif

%global rustflags -Clink-arg=-Wl,-z,relro,-z,now

# Exclude implicitly-scanned Provides, especially the libLLVM.so ones:
%global __provides_exclude_from ^%{rustlibdir}/.*$

Name:           rust%{version_suffix}%{psuffix}
Version:        %{version_current}
Release:        0
Summary:        A systems programming language
License:        Apache-2.0 OR MIT
Group:          Development/Languages/Rust
URL:            https://www.rust-lang.org
Source0:        %{dl_url}/rustc-%{version}-src.tar.xz
Source1:        rust.keyring
%if %{without test}
Source99:       %{name}-rpmlintrc
%endif
Source100:      %{dl_url}/rust-%{version_current}-x86_64-unknown-linux-gnu.tar.xz
NoSource:       100
Source101:      %{dl_url}/rust-%{version_current}-i686-unknown-linux-gnu.tar.xz
NoSource:       101
Source102:      %{dl_url}/rust-%{version_current}-aarch64-unknown-linux-gnu.tar.xz
NoSource:       102
Source103:      %{dl_url}/rust-%{version_current}-armv7-unknown-linux-gnueabihf.tar.xz
NoSource:       103
Source104:      %{dl_url}/rust-%{version_current}-arm-unknown-linux-gnueabihf.tar.xz
NoSource:       104
Source105:      %{dl_url}/rust-%{version_current}-powerpc64-unknown-linux-gnu.tar.xz
NoSource:       105
Source106:      %{dl_url}/rust-%{version_current}-powerpc64le-unknown-linux-gnu.tar.xz
NoSource:       106
Source107:      %{dl_url}/rust-%{version_current}-s390x-unknown-linux-gnu.tar.xz
NoSource:       107
Source108:      %{dl_url}/rust-%{version_current}-powerpc-unknown-linux-gnu.tar.xz
NoSource:       108
Source109:      %{dl_url}/rust-%{version_current}-riscv64gc-unknown-linux-gnu.tar.xz
NoSource:       109
Source200:      %{dl_url}/rust-%{version_current}-x86_64-unknown-linux-gnu.tar.xz.asc
NoSource:       200
Source201:      %{dl_url}/rust-%{version_current}-i686-unknown-linux-gnu.tar.xz.asc
NoSource:       201
Source202:      %{dl_url}/rust-%{version_current}-aarch64-unknown-linux-gnu.tar.xz.asc
NoSource:       202
Source203:      %{dl_url}/rust-%{version_current}-armv7-unknown-linux-gnueabihf.tar.xz.asc
NoSource:       203
Source204:      %{dl_url}/rust-%{version_current}-arm-unknown-linux-gnueabihf.tar.xz.asc
NoSource:       204
Source205:      %{dl_url}/rust-%{version_current}-powerpc64-unknown-linux-gnu.tar.xz.asc
NoSource:       205
Source206:      %{dl_url}/rust-%{version_current}-powerpc64le-unknown-linux-gnu.tar.xz.asc
NoSource:       206
Source207:      %{dl_url}/rust-%{version_current}-s390x-unknown-linux-gnu.tar.xz.asc
NoSource:       207
Source208:      %{dl_url}/rust-%{version_current}-powerpc-unknown-linux-gnu.tar.xz.asc
NoSource:       208
Source209:      %{dl_url}/rust-%{version_current}-riscv64gc-unknown-linux-gnu.tar.xz.asc
NoSource:       209
# Make factory-auto stop complaining...
Source1000:     README.suse-maint
# PATCH-FIX-OPENSUSE: edit src/librustc_llvm/build.rs to ignore GCC incompatible flag
Patch0:         ignore-Wstring-conversion.patch
# IMPORTANT - To generate patches for submodules in git so they apply relatively you can use
#  git format-patch --text --dst-prefix=b/src/tools/cargo/  HEAD~2

BuildRequires:  chrpath
BuildRequires:  curl
# BUG - fdupes on leap/sle causes issues with debug info
%if 0%{?is_opensuse} == 1 && 0%{?suse_version} >= 1699
BuildRequires:  fdupes
%endif
BuildRequires:  pkgconfig
BuildRequires:  procps
BuildRequires:  python3-base
BuildRequires:  util-linux
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(zlib)
# Set requires appropriately
%if %with sccache
BuildRequires:  sccache
%else
BuildRequires:  ccache
%endif

# For linking to platform
Requires:       glibc-devel
# Rustc doesn't really do much without Cargo, but you know, if you wanna yolo that ...
Recommends:     cargo
# For static linking
Recommends:     glibc-devel-static

%if %{with wasi}
BuildRequires:  wasi-libc
%endif

%if %{with llvmtools}
BuildRequires:  clang
BuildRequires:  libstdc++-devel
BuildRequires:  lld
Requires:       clang
Requires:       lld
%else
%if 0%{?gcc_version} != 0
BuildRequires:  gcc%{gcc_version}-c++
Requires:       gcc%{gcc_version}
%else
BuildRequires:  gcc-c++
Requires:       gcc
%endif
%endif

# CMake and Ninja required to drive the bundled llvm build.
# Cmake is also needed in tests.
%if 0%{?sle_version} >= 120000 && 0%{?sle_version} <= 150200
# In these distros cmake is 2.x, or 3.X < 3.13, so we need cmake3 for building llvm.
BuildRequires:  cmake3 > 3.13.4
%else
BuildRequires:  cmake > 3.13.4
%endif

# To build rust-lld
BuildRequires:  ninja

%if %{without bundled_llvm}
# Use distro provided LLVM on Tumbleweed, but pin it to the matching LLVM!
# For details see boo#1192067
BuildRequires:  llvm%{llvm_version}-devel
BuildRequires:  clang%{llvm_version}
Requires:       lld%{llvm_version}
%endif

%if %{with test}
BuildRequires:  cargo%{version_suffix} = %{version}
BuildRequires:  rust%{version_suffix} = %{version}
# Static linking tests need this.
BuildRequires:  glibc-devel-static
BuildRequires:  git

%if %{without bundled_llvm}
# For FileCheck
BuildRequires:  llvm%{llvm_version}-devel
%endif

%if %{with wasm32}
BuildRequires:  nodejs-default
%endif

# End with test
%endif

%obsolete_rust_versioned rust
Conflicts:      rust+rustc < %{version}
Conflicts:      rustc-bootstrap
Provides:       rust+rustc = %{version}
Conflicts:      rust-std < %{version}
Obsoletes:      rust-std < %{version}
Provides:       rust-std = %{version}
Conflicts:      rust-std-static < %{version}
Obsoletes:      rust-std-static < %{version}
Provides:       rust-std-static = %{version}
Conflicts:      rust-gdb < %{version}
Obsoletes:      rust-gdb < %{version}
Provides:       rust-gdb = %{version}

%if %{without test}
# Restrict the architectures as building rust relies on being
# initially bootstrapped before we can build the n+1 release
ExclusiveArch:  x86_64 %{arm} aarch64 ppc ppc64 ppc64le s390x %{ix86} riscv64
%ifarch %{ix86}
ExclusiveArch:  i686
%endif
%else
# Restrict for Tier 1 targets (but we should report bugs in Tier 2)
# https://doc.rust-lang.org/nightly/rustc/platform-support.html#tier-1-with-host-tools
ExclusiveArch:  x86_64 i686 aarch64
%endif

%description
Rust is a systems programming language focused on three goals: safety,
speed, and concurrency. It maintains these goals without having a
garbage collector, making it a useful language for a number of use
cases other languages are not good at: embedding in other languages,
programs with specific space and time requirements, and writing
low-level code, like device drivers and operating systems. It improves
on current languages targeting this space by having a number of
compile-time safety checks that produce no runtime overhead, while
eliminating all data races. Rust also aims to achieve "zero-cost
abstractions", even though some of these abstractions feel like those
of a high-level language. Even then, Rust still allows precise control
like a low-level language would.

%package -n cargo%{version_suffix}
Summary:        The Rust package manager
License:        Apache-2.0 OR MIT
Group:          Development/Languages/Rust
Requires:       rust-std = %{version}
Obsoletes:      cargo-vendor < %{version}
Provides:       cargo-vendor = %{version}
Provides:       rust+cargo = %{version}
%obsolete_rust_versioned cargo

%description -n cargo%{version_suffix}
Cargo downloads dependencies of Rust projects and compiles it.

%package src
Summary:        The Rust Standard Library Source
License:        Apache-2.0 OR MIT
Group:          Development/Languages/Rust
Requires:       rust-std = %{version}
BuildArch:      noarch

%description src
Rust Stanard Library Sources are required for building some types of projects

%prep
# Previously the stage0 compiler was skipped in test builds, but there are now
# tests in rust's source tree that require it.
%ifarch x86_64
%setup -q -T -b 100 -n rust-%{version_current}-%{rust_triple}
%endif
%ifarch %{ix86}
%setup -q -T -b 101 -n rust-%{version_current}-%{rust_triple}
%endif
%ifarch aarch64
%setup -q -T -b 102 -n rust-%{version_current}-%{rust_triple}
%endif
%ifarch armv7hl
%setup -q -T -b 103 -n rust-%{version_current}-%{rust_triple}
%endif
%ifarch armv6hl
%setup -q -T -b 104 -n rust-%{version_current}-%{rust_triple}
%endif
%ifarch ppc64
%setup -q -T -b 105 -n rust-%{version_current}-%{rust_triple}
%endif
%ifarch ppc64le
%setup -q -T -b 106 -n rust-%{version_current}-%{rust_triple}
%endif
%ifarch s390x
%setup -q -T -b 107 -n rust-%{version_current}-%{rust_triple}
%endif
%ifarch ppc
%setup -q -T -b 108 -n rust-%{version_current}-%{rust_triple}
%endif
%ifarch riscv64
%setup -q -T -b 109 -n rust-%{version_current}-%{rust_triple}
%endif
./install.sh --components=cargo,rustc,rust-std-%{rust_triple} --prefix=.%{_prefix} --disable-ldconfig

%global rust_root %{_builddir}/rust-%{version_current}-%{rust_triple}%{_prefix}

%autosetup -p1 -n rustc-%{version}-src

# We never enable emscripten.
rm -rf src/llvm-emscripten/
# We never enable other LLVM tools.
rm -rf src/tools/clang
rm -rf src/tools/lldb

# Fix rpmlint error "This script uses 'env' as an interpreter"
sed -i '1s|#!%{_bindir}/env python|#!%{_bindir}/python3|' library/core/src/unicode/printable.py
chmod +x library/core/src/unicode/printable.py

# Debugging for if anything goes south.
lscpu
free -h
df -h

%build

# Create exports file
# Keep all the "export VARIABLE" together here, so they can be
# reread in the %%install section below.
# If the environments between build and install and different,
# everything will be rebuilt during installation!

%if %{with llvmtools}
cat > .env.sh <<EOF
export CC="/usr/bin/clang"
export CXX="/usr/bin/clang++"
EOF
%else

%if 0%{?gcc_version} != 0
cat > .env.sh <<EOF
export CC="/usr/bin/gcc-%{gcc_version}"
export CXX="/usr/bin/g++-%{gcc_version}"
EOF
%else
cat > .env.sh <<EOF
export CC="gcc"
export CXX="g++"
EOF
%endif

%endif

# -Clink-arg=-B{_prefix}/lib/rustlib/{rust_triple}/bin/gcc-ld/"
# -Clink-arg=-B{rust_root}/lib/rustlib/{rust_triple}/bin/gcc-ld/"

%if %{with sccache}
export CC="/usr/bin/sccache ${CC}"
export CXX="/usr/bin/sccache ${CXX}"
%endif

cat >> .env.sh <<EOF
export CXXFLAGS="-I/home/abuild/rpmbuild/BUILD/rustc-%{version}-src/src/llvm-project/libunwind/include/"
export PATH="%{_prefix}/lib/rustlib/%{rust_triple}/bin/:${PATH}"
export RUSTFLAGS="%{rustflags} -Clinker=%{rust_linker}"
export LD_LIBRARY_PATH="%{rust_root}/lib"
export SCCACHE_IDLE_TIMEOUT="3000"
export DESTDIR=%{buildroot}
export CARGO_FEATURE_VENDORED=1
unset FFLAGS
unset MALLOC_CHECK_
unset MALLOC_PERTURB_
# END EXPORTS
EOF
. ./.env.sh

# Sometimes to debug sccache we need to know the state of the env.
env

# Check our rustroot works as we expect
%if %{without test}
cat >> main.rs <<EOF
fn main() {}
EOF
RUSTC_LOG=rustc_codegen_ssa::back::link=info %{rust_root}/bin/rustc -C link-args=-Wl,-v ${RUSTFLAGS} main.rs
%endif

# Find compiler-rt
%if %{without bundled_llvm}
PATH_TO_LLVM_PROFILER=`echo %{_libdir}/clang/??/lib/linux/libclang_rt.profile-*.a`
%endif

# The configure macro will modify some autoconf-related files, which upsets
# cargo when it tries to verify checksums in those files. So we don't use
# the macro, as it provides no tangible benefit to our build process.
# FUTURE: See if we can build sanitizers without the full llvm bundling.
# {?with_tier1: --enable-sanitizers} \

./configure \
  --build=%{rust_triple} --host=%{rust_triple} \
  --target %{rust_target_list} \
  %{?with_wasi: --set target.wasm32-wasi.wasi-root=%{_datadir}/wasi-sysroot/ } \
  --prefix=%{_prefix} \
  --bindir=%{_bindir} \
  --sysconfdir=%{_sysconfdir} \
  --datadir=%{_datadir} \
  --localstatedir=%{_localstatedir} \
  --mandir=%{_mandir} \
  --infodir=%{_infodir} \
  --libdir=%{common_libdir} \
  --docdir=%{_docdir}/rust \
  --enable-local-rust \
  %{!?with_test: --local-rust-root=%{rust_root} --disable-rpath} \
  %{!?with_bundled_llvm: --llvm-root=%{_prefix} --enable-llvm-link-shared} \
  %{?with_bundled_llvm: --disable-llvm-link-shared --set llvm.link-jobs=0} \
  %{?with_llvmtools: --set rust.use-lld=true --set llvm.use-linker=lld} \
  --set rust.lld=true \
  --default-linker=%{rust_linker} \
  %{?with_sccache: --enable-sccache} \
  %{!?with_sccache: --enable-ccache} \
  --disable-docs \
  --disable-compiler-docs \
  --enable-verbose-tests \
  %{debug_info} \
  --enable-vendor \
  --enable-extended \
  --tools="cargo,clippy,rustdoc,rustfmt,src" \
  --release-channel="stable" \
  --set rust.deny-warnings=false \
  %{!?with_bundled_llvm: --set target.%{rust_triple}.profiler=${PATH_TO_LLVM_PROFILER}} \
  %{?with_bundled_llvm: --set target.%{rust_triple}.profiler=true} \
  %{nil}

# We set deny warnings to false due to a problem where rust upstream didn't test building with
# the same version (they did previous ver)

%if %{without test}
python3 ./x.py build
# Debug for post build
free -h
df -h
%endif

%install
# Reread exports file
%if %{without test}
. ./.env.sh

python3 ./x.py install

# bsc#1199126 - rust-lld contains an rpath, which is invalid.
chrpath -d %{buildroot}%{rustlibdir}/%{rust_triple}/bin/rust-lld

%if %{with bundled_llvm}
# To facilitate tests when we aren't using system LLVM, we need filecheck available.
install -m 0755 %{_builddir}/rustc-%{version}-src/build/%{rust_triple}/llvm/bin/FileCheck %{buildroot}%{rustlibdir}/%{rust_triple}/bin/FileCheck
%endif

# Remove the license files from _docdir: make install put duplicates there
rm %{buildroot}%{_docdir}/rust/{README.md,COPYRIGHT,LICENSE*}
rm %{buildroot}%{_docdir}/rust/*.old

# Remove installer artifacts (manifests, uninstall scripts, etc.)
find %{buildroot}%{rustlibdir} -maxdepth 1 -type f -exec rm -v '{}' '+'

# Remove hidden files from source
find %{buildroot}%{rustlibdir} -type f -name '.appveyor.yml' -exec rm -v '{}' '+'
find %{buildroot}%{rustlibdir} -type f -name '.travis.yml' -exec rm -v '{}' '+'
find %{buildroot}%{rustlibdir} -type f -name '.cirrus.yml' -exec rm -v '{}' '+'
find %{buildroot}%{rustlibdir} -type f -name '.clang-format' -exec rm -v '{}' '+'
find %{buildroot}%{rustlibdir} -type d -name '.github' -exec rm -r -v '{}' '+'

# The shared libraries should be executable to allow fdupes find duplicates.
find %{buildroot}%{common_libdir} -maxdepth 1 -type f -name '*.so' -exec chmod -v +x '{}' '+'

# The shared libraries should be executable for debuginfo extraction.
find %{buildroot}%{rustlibdir} -maxdepth 1 -type f -name '*.so' -exec chmod -v +x '{}' '+'

# Create the path for crate-devel packages
mkdir -p %{buildroot}%{_datadir}/cargo/registry

# Remove completions
rm -rf %{buildroot}%{_prefix}/src/etc/bash_completion.d
# rmdir %{buildroot}%{_prefix}/src/etc
rm -rf %{buildroot}%{_sysconfdir}/bash_completion.d
rm -rf %{buildroot}%{_datadir}/zsh

# There should be nothing here at all
rm -rf %{buildroot}%{_sysconfdir}
# cargo does not respect our _libexec setting on Leap:
if [ ! -f %{buildroot}%{_libexecdir}/cargo-credential-1password ] &&
   [ -f %{buildroot}%{_exec_prefix}/libexec/cargo-credential-1password ]; then
    mv %{buildroot}%{_exec_prefix}/libexec/cargo-credential-1password \
    %{buildroot}%{_libexecdir}/cargo-credential-1password
fi

# Silence any duplicate library warnings.
%if 0%{?is_opensuse} == 1 && 0%{?suse_version} >= 1699
%fdupes %{buildroot}/%{common_libdir}
%endif

# Ugly hack to get brp-15-strip-debug call llvm-strip, which is wasm-aware, as system-strip will break wasm-files (same for ar/ranlib)
export CROSS_COMPILE=llvm-

# End without test
%endif

%if %{with test}
%check
. ./.env.sh

# Tests require stage0 in place, so we need to symlink that in for compiler access.
# Generally in a non-local rust build, this process assumes you downloaded and unpacked
# the compiler toolchain into stage0, which is why we have to feed that in manually.
mkdir -p %{_builddir}/rustc-%{version}-src/build/%{rust_triple}
ln -s %{rust_root} %{_builddir}/rustc-%{version}-src/build/%{rust_triple}/stage0

# Need to exclude issue-71519 as when we enable lld for wasm, this test incorrectly assumes
# we can use it with -Z gcc-ld=lld (which is sadly trapped in nightly). We can't exclude
# a single test so sadly we have to exclude that whole suite.
%ifarch aarch64
python3 ./x.py test --target=%{rust_triple} \
    --exclude tests/run-make/issue-71519 \
    --exclude tests/run-make/pgo-branch-weights \
    --exclude src/tools/tidy \
    --exclude src/tools/expand-yaml-anchors \
    --exclude tests/ui/methods \
    --exclude tests/ui/typeck \
    --exclude tests/ui/issues/issue-21763 \
    --exclude tests/ui/mismatched_types \
    --exclude tests/run-make/short-ice \
    --exclude tests/run-make/rust-lld \
    --exclude src/bootstrap
%else
python3 ./x.py test --target=%{rust_triple} \
    --exclude tests/run-make/issue-71519 \
    --exclude tests/run-make/pgo-branch-weights \
    --exclude src/tools/tidy \
    --exclude src/tools/expand-yaml-anchors \
    --exclude tests/ui/methods \
    --exclude tests/ui/typeck \
    --exclude tests/ui/issues/issue-21763 \
    --exclude tests/ui/mismatched_types \
    --exclude tests/run-make/short-ice \
    --exclude tests/run-make/rust-lld \
    --exclude src/bootstrap
%endif

# End with test
%endif

%if %{without test}
%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license COPYRIGHT LICENSE-APACHE LICENSE-MIT
%doc CONTRIBUTING.md README.md RELEASES.md
%{_bindir}/rustc
%{_bindir}/rustdoc
%{_bindir}/rust-gdb
%{_bindir}/rust-gdbgui
%{_bindir}/rust-lldb
%{_bindir}/cargo-clippy
%{_bindir}/cargo-fmt
%{_bindir}/clippy-driver
%{_bindir}/rustfmt
%{_mandir}/man1/rustc.1%{?ext_man}
%{_mandir}/man1/rustdoc.1%{?ext_man}
%{_prefix}/lib/lib*.so
%dir %{rustlibdir}
%dir %{rustlibdir}%{_sysconfdir}
%{rustlibdir}%{_sysconfdir}/gdb_load_rust_pretty_printers.py
%{rustlibdir}%{_sysconfdir}/gdb_lookup.py
%{rustlibdir}%{_sysconfdir}/gdb_providers.py
%{rustlibdir}%{_sysconfdir}/lldb_commands
%{rustlibdir}%{_sysconfdir}/lldb_lookup.py
%{rustlibdir}%{_sysconfdir}/lldb_providers.py
%{rustlibdir}%{_sysconfdir}/rust_types.py
%dir %{rustlibdir}/%{rust_triple}
%{rustlibdir}/%{rust_triple}/bin
%dir %{rustlibdir}/%{rust_triple}/lib
%{rustlibdir}/%{rust_triple}/lib/*.so
%{rustlibdir}/%{rust_triple}/lib/*.rlib
%if %{with wasm32}
%dir %{rustlibdir}/wasm32-unknown-unknown
%dir %{rustlibdir}/wasm32-unknown-unknown/lib
%{rustlibdir}/wasm32-unknown-unknown/lib/*.rlib
%if %{with wasi}
%dir %{rustlibdir}/wasm32-wasi
%dir %{rustlibdir}/wasm32-wasi/lib
%dir %{rustlibdir}/wasm32-wasi/lib/self-contained
%{rustlibdir}/wasm32-wasi/lib/*.rlib
%{rustlibdir}/wasm32-wasi/lib/self-contained/*.o
%{rustlibdir}/wasm32-wasi/lib/self-contained/*.a
%endif
%endif
%ifarch x86_64
%dir %{rustlibdir}/x86_64-unknown-none
%dir %{rustlibdir}/x86_64-unknown-none/lib
%{rustlibdir}/x86_64-unknown-none/lib/*.rlib
%endif

# Seems to have been removed in 1.73
# pct {_libexecdir}/cargo-credential-1password

%files -n cargo%{version_suffix}
%license src/tools/cargo/LICENSE-{APACHE,MIT,THIRD-PARTY}
%license src/tools/rustfmt/LICENSE-{APACHE,MIT}
%license src/tools/clippy/LICENSE-{APACHE,MIT}
%{_bindir}/cargo
%{_mandir}/man1/cargo*.1%{?ext_man}
%dir %{_datadir}/cargo
%dir %{_datadir}/cargo/registry

%files src
%{rustlibdir}/src

# End not with test
%endif

%changelog
