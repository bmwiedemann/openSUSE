#
# spec file
#
# Copyright (c) 2021 SUSE LLC
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


%global version_suffix 1.56
%global version_current 1.56.1
%global version_previous 1.55.0
# This has to be kept lock step to the rust version.
%global llvm_version 13

%define obsolete_rust_versioned() \
Obsoletes:      %{1}1.55%{?2:-%{2}} \
Obsoletes:      %{1}1.54%{?2:-%{2}} \
Obsoletes:      %{1}1.53%{?2:-%{2}} \
Obsoletes:      %{1}1.52%{?2:-%{2}}

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
#

# === broken distro llvm ===
# In some situations the llvm provided on the platform may not work.
# we add these conditions here.

%if 0%{?is_opensuse} == 1 && 0%{?suse_version} >= 1550
# Tw is fine, can proceed with pinned llvm.
%bcond_with bundled_llvm
%else
# Use bundled llvm instead.
# For details see boo#1192067
%bcond_without bundled_llvm
%endif

# Test is done in a different multibuild package (rustXXX-test).  This
# package will replace the local-rust-root and use the systems's one
# from the rustXXX package itself.  This will exercise the compiler,
# even tho, the tests will require more compilation.  If we do not
# agree on this model we can drop the _multibuild option and do the
# pct check as a part of the main spec.

%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test" && ! %with bundled_llvm
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

# Use hardening ldflags
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
%if ! %{with test}
Source99:       %{name}-rpmlintrc
%endif
Source100:      %{dl_url}/rust-%{version_current}-x86_64-unknown-linux-gnu.tar.xz
Source101:      %{dl_url}/rust-%{version_current}-i686-unknown-linux-gnu.tar.xz
Source102:      %{dl_url}/rust-%{version_current}-aarch64-unknown-linux-gnu.tar.xz
Source103:      %{dl_url}/rust-%{version_current}-armv7-unknown-linux-gnueabihf.tar.xz
Source104:      %{dl_url}/rust-%{version_current}-arm-unknown-linux-gnueabihf.tar.xz
Source105:      %{dl_url}/rust-%{version_current}-powerpc64-unknown-linux-gnu.tar.xz
Source106:      %{dl_url}/rust-%{version_current}-powerpc64le-unknown-linux-gnu.tar.xz
Source107:      %{dl_url}/rust-%{version_current}-s390x-unknown-linux-gnu.tar.xz
Source108:      %{dl_url}/rust-%{version_current}-powerpc-unknown-linux-gnu.tar.xz
Source109:      %{dl_url}/rust-%{version_current}-riscv64gc-unknown-linux-gnu.tar.xz
Source200:      %{dl_url}/rust-%{version_current}-x86_64-unknown-linux-gnu.tar.xz.asc
Source201:      %{dl_url}/rust-%{version_current}-i686-unknown-linux-gnu.tar.xz.asc
Source202:      %{dl_url}/rust-%{version_current}-aarch64-unknown-linux-gnu.tar.xz.asc
Source203:      %{dl_url}/rust-%{version_current}-armv7-unknown-linux-gnueabihf.tar.xz.asc
Source204:      %{dl_url}/rust-%{version_current}-arm-unknown-linux-gnueabihf.tar.xz.asc
Source205:      %{dl_url}/rust-%{version_current}-powerpc64-unknown-linux-gnu.tar.xz.asc
Source206:      %{dl_url}/rust-%{version_current}-powerpc64le-unknown-linux-gnu.tar.xz.asc
Source207:      %{dl_url}/rust-%{version_current}-s390x-unknown-linux-gnu.tar.xz.asc
Source208:      %{dl_url}/rust-%{version_current}-powerpc-unknown-linux-gnu.tar.xz.asc
Source209:      %{dl_url}/rust-%{version_current}-riscv64gc-unknown-linux-gnu.tar.xz.asc
# Make factory-auto stop complaining...
Source1000:     README.suse-maint
# PATCH-FIX-OPENSUSE: edit src/librustc_llvm/build.rs to ignore GCC incompatible flag
Patch0:         ignore-Wstring-conversion.patch
# PATCH-FIX-UPSTREAM [Tests] fix_bootstrap_vendor.patch
# https://github.com/rust-lang/rust/pull/90800
Patch1:         fix_bootstrap_vendor.patch
# PATCH-FIX-UPSTREAM [Tests] fix_function-names_test_for_gdb_10_1.patch
Patch2:         fix_function-names_test_for_gdb_10_1.patch
# PATCH-FIX-UPSTREAM [Tests] set_the_library_path_in_sysroot-crates-are-unstable.patch
Patch3:         set_the_library_path_in_sysroot-crates-are-unstable.patch
# PATCH-FIX-UPSTREAM [Tests] fix_alloc-optimisation_is_only_for_rust_llvm.patch
Patch4:         fix_alloc-optimisation_is_only_for_rust_llvm.patch
BuildRequires:  curl
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  procps
BuildRequires:  python3-base
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(zlib)
# Set requires appropriately
%if %with sccache
BuildRequires:  sccache
%else
BuildRequires:  ccache
%endif
BuildRequires:  cmake
BuildRequires:  gcc-c++

%if !%with bundled_llvm
# Use distro provided LLVM on Tumbleweed, but pin it to the matching LLVM!
# For details see boo#1192067
BuildRequires:  llvm%{llvm_version}-devel
%else
# Ninja required to drive the bundled llvm build.
BuildRequires:  ninja
%endif
Recommends:     cargo

%if %{with test}
BuildRequires:  cargo%{version_suffix} = %{version}
BuildRequires:  rust%{version_suffix} = %{version}
# Required because FileCheck
BuildRequires:  llvm%{llvm_version}-devel
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

%if ! %{with test}
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

%prep
%if ! %{with test}
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
%endif

%autosetup -p1 -n rustc-%{version}-src

# We never enable emscripten.
rm -rf src/llvm-emscripten/
# We never enable other LLVM tools.
rm -rf src/tools/clang
rm -rf src/tools/lld
rm -rf src/tools/lldb
# CI tooling won't be used
rm -rf src/ci

%if !%with bundled_llvm
rm -rf src/llvm/
%endif

# Fix rpmlint error "This script uses 'env' as an interpreter"
sed -i '1s|#!%{_bindir}/env python|#!%{_bindir}/python3|' library/core/src/unicode/printable.py
chmod +x library/core/src/unicode/printable.py

%build
# The configure macro will modify some autoconf-related files, which upsets
# cargo when it tries to verify checksums in those files. So we don't use
# the macro, as it provides no tangible benefit to our build process.
# FUTURE: See if we can build sanitizers without the full llvm bundling.
# {?with_tier1: --enable-sanitizers} \
./configure \
  --build=%{rust_triple} --host=%{rust_triple} --target=%{rust_triple} \
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
  %{?with_bundled_llvm: --disable-llvm-link-shared --set llvm.link-jobs=4} \
  --enable-optimize \
  %{?with_sccache: --enable-sccache} \
%ifnarch armv6l armv6hl
  %{!?with_sccache: --enable-ccache} \
%endif
  --disable-docs \
  --disable-compiler-docs \
  --enable-verbose-tests \
  %{debug_info} \
  --enable-vendor \
  --enable-extended \
  --tools="cargo" \
  --release-channel="stable"

# Sometimes we may be rebuilding with the same compiler,
# setting local-rebuild will skip stage0 build, reducing build time
# -- we no longer need to set this manually as local-rust implies this if
# the rustc version matches our target build version.

# Create exports file
# Keep all the "export VARIABLE" together here, so they can be
# reread in the %%install section below.
# If the environments between build and install and different,
# everything will be rebuilt during installation!
cat > .env.sh <<\EOF
export RUSTFLAGS="%{rustflags}"
export DESTDIR=%{buildroot}
export CARGO_FEATURE_VENDORED=1
unset FFLAGS
# END EXPORTS
EOF

%if ! %{with test}
. ./.env.sh
python3 ./x.py build
%endif

%install
# Reread exports file
%if ! %{with test}
. ./.env.sh

python3 ./x.py install

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

# Install rust-llvm-dwp in _bindir
mv %{buildroot}%{rustlibdir}/*-unknown-linux-gnu*/bin/rust-llvm-dwp  %{buildroot}%{_bindir}
rm -rf %{buildroot}%{rustlibdir}/*-unknown-linux-gnu*/bin

# Create the path for crate-devel packages
mkdir -p %{buildroot}%{_datadir}/cargo/registry

# Remove completions
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

# Remove llvm installation
rm -rf %{buildroot}/home
%endif

%if %{with test}
%check
. ./.env.sh

# There are some crates forked in github.  Use the vendored version to
# stop trying `cargo` to access internet.
#
# https://github.com/rust-lang/rust/issues/90764

mkdir .cargo
cat > .cargo/config <<EOF
[source.crates-io]
replace-with = 'vendored-sources'
registry = 'https://example.com'

[source.vendored-sources]
directory = '$(pwd)/vendor'

[source."https://github.com/bjorn3/rust-ar.git"]
git = "https://github.com/bjorn3/rust-ar.git"
branch = "do_not_remove_cg_clif_ranlib"
replace-with = "vendored-sources"

[source."https://github.com/bytecodealliance/wasmtime.git"]
git = "https://github.com/bytecodealliance/wasmtime.git"
replace-with = "vendored-sources"
EOF

python3 ./x.py test
%endif

%if ! %{with test}
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
%{_bindir}/rust-llvm-dwp
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
%dir %{rustlibdir}/%{rust_triple}/lib
%{rustlibdir}/%{rust_triple}/lib/*.so
%{rustlibdir}/%{rust_triple}/lib/*.rlib
%{_libexecdir}/cargo-credential-1password

%files -n cargo%{version_suffix}
%license src/tools/cargo/LICENSE-{APACHE,MIT,THIRD-PARTY}
%license src/tools/rustfmt/LICENSE-{APACHE,MIT}
%license src/tools/clippy/LICENSE-{APACHE,MIT}
%{_bindir}/cargo
%{_mandir}/man1/cargo*.1%{?ext_man}
%dir %{_datadir}/cargo
%dir %{_datadir}/cargo/registry
%endif

%changelog
