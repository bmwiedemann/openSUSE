#
# spec file for package rust
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

# === rust arch support tiers ===
# https://doc.rust-lang.org/nightly/rustc/platform-support.html
# tl;dr only aarch64, x86_64 and i686 are guaranteed to work.
#
# armv6/7, s390x, ppc[64[le]], riscv are all "guaranteed to build" only
# but may not always work.
#


%global version_suffix 1.53
%global version_current 1.53.0
%global version_previous 1.52.1

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

# Dev tools - these are needed for developers, vs building, so
# we don't always enable them. Some platforms have issues
# building these (IE RLS requires 64-bit atomics).
# As a result, we limit this to platforms that are likely used on
# desktop arches
%ifarch x86_64 aarch64
%bcond_without devtools
%else
%bcond_with devtools
%endif

# Platforms that SHOULD have documentation.
%ifarch x86_64 aarch64
%bcond_without mddocs
%else
# s390x especially has issues building docs.
%bcond_with mddocs
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

# Debuginfo can exhaust memory on these architecture workers
%ifarch  %{arm} %{ix86}
%define debug_info --disable-debuginfo --disable-debuginfo-only-std --disable-debuginfo-tools --disable-debuginfo-lines
%define strip_debug_flag 1
%else
%define debug_info --enable-debuginfo --disable-debuginfo-only-std --enable-debuginfo-tools --disable-debuginfo-lines
%endif

# Use hardening ldflags
%global rustflags -Clink-arg=-Wl,-z,relro,-z,now

# Exclude implicitly-scanned Provides, especially the libLLVM.so ones:
%global __provides_exclude_from ^%{rustlibdir}/.*$

# enable the --with-rust_bootstrap flag
%bcond_with rust_bootstrap

Name:           rust%{version_suffix}
Version:        %{version_current}
Release:        0
Summary:        A systems programming language
License:        Apache-2.0 OR MIT
Group:          Development/Languages/Rust
URL:            https://www.rust-lang.org
Source0:        %{dl_url}/rustc-%{version}-src.tar.xz
Source1:        rust.keyring
Source99:       %{name}-rpmlintrc
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
BuildRequires:  curl
BuildRequires:  fdupes
BuildRequires:  git
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
BuildRequires:  pkgconfig(libssh2) >= 1.6.0
BuildRequires:  pkgconfig(libgit2)
# Real LLVM minimum version should be 9.x, but rust has a fallback mode
%if !%with bundled_llvm
BuildRequires:  llvm-devel >= 10.0
%else
BuildRequires:  ninja
%endif
%if !%with rust_bootstrap
# We will now package cargo using the version number of rustc since it
# is being built from rust sources. Old cargo packages have a 0.x
# number
BuildRequires:  cargo <= %{version_current}
BuildRequires:  cargo >= %{version_previous}
BuildRequires:  rust <= %{version_current}
BuildRequires:  rust >= %{version_previous}
%endif
Recommends:     cargo

Conflicts:      rustc-bootstrap
Conflicts:      rust+rustc < %{version}
Obsoletes:      rust+rustc < %{version}
Provides:       rust+rustc = %{version}
Conflicts:      rust-std < %{version}
Obsoletes:      rust-std < %{version}
Provides:       rust-std = %{version}
Conflicts:      rust-std-static < %{version}
Obsoletes:      rust-std-static < %{version}
Provides:       rust-std-static = %{version}

# Restrict the architectures as building rust relies on being
# initially bootstrapped before we can build the n+1 release
ExclusiveArch:  x86_64 %{arm} aarch64 ppc ppc64 ppc64le s390x %{ix86} riscv64
%ifarch %{ix86}
ExclusiveArch:  i686
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

%package doc
Summary:        Rust documentation
License:        Apache-2.0 OR MIT
Group:          Development/Languages/Rust
Conflicts:      rust-doc < %{version}
Obsoletes:      rust-doc < %{version}
Provides:       rust-doc = %{version}

%description doc
Documentation for the Rust language.

%package gdb
Summary:        Gdb integration for rust binaries
License:        Apache-2.0 OR MIT
Group:          Development/Languages/Rust
Requires:       rust%{version_suffix} = %{version}
Conflicts:      rust+gdb < %{version}
Obsoletes:      rust+gdb < %{version}
Provides:       rust+gdb = %{version}

%description gdb
This subpackage provides pretty printers and a wrapper script for
invoking gdb on rust binaries.

%package src
Summary:        Sources for the Rust standard library
License:        Apache-2.0 OR MIT
Group:          Development/Languages/Rust
BuildArch:      noarch
Requires:       rust%{version_suffix} = %{version}
Conflicts:      rust-src < %{version}
Obsoletes:      rust-src < %{version}
Provides:       rust-src = %{version}

%description src
This package includes source files for the Rust standard library. This
is commonly used for function detail lookups in helper programs such
as RLS or racer.

%package -n rls%{version_suffix}
Summary:        Language server for Rust lang
License:        Apache-2.0 OR MIT
Group:          Development/Languages/Rust
Requires:       rust%{version_suffix} = %{version}
Requires:       rust%{version_suffix}-analysis = %{version}
Requires:       rust%{version_suffix}-src = %{version}
Conflicts:      rust+rls < %{version}
Obsoletes:      rust+rls < %{version}
Provides:       rust+rls = %{version}

%description -n rls%{version_suffix}
The RLS provides a server that runs in the background, providing IDEs,
editors, and other tools with information about Rust programs. It
supports functionality such as 'goto definition', symbol search,
reformatting, and code completion, and enables renaming and
refactorings.  It can be used with an IDE such as Gnome-Builder.

%package analysis
Summary:        Compiler analysis data for the Rust standard library
License:        Apache-2.0 OR MIT
Group:          Development/Languages/Rust
Requires:       rust%{version_suffix} = %{version}
Conflicts:      rust-analysis < %{version}
Obsoletes:      rust-analysis < %{version}
Provides:       rust-analysis = %{version}

%description analysis
This package contains analysis data files produced with rustc's
-Zsave-analysis feature for the Rust standard library. The RLS (Rust
Language Server) uses this data to provide information about the Rust
standard library.

%package -n cargo%{version_suffix}
Summary:        The Rust package manager
License:        Apache-2.0 OR MIT
Group:          Development/Languages/Rust
Requires:       rust%{version_suffix} = %{version}
Conflicts:      cargo-vendor < %{version}
Obsoletes:      cargo-vendor < %{version}
Provides:       cargo-vendor = %{version}
Conflicts:      rust+cargo < %{version}
Obsoletes:      rust+cargo < %{version}
Provides:       rust+cargo = %{version}
Conflicts:      rustfmt < %{version}
Obsoletes:      rustfmt < %{version}
Provides:       rustfmt = %{version}
Conflicts:      cargo-fmt < %{version}
Obsoletes:      cargo-fmt < %{version}
Provides:       cargo-fmt = %{version}
Conflicts:      clippy < %{version}
Obsoletes:      clippy < %{version}
Provides:       clippy = %{version}

%description -n cargo%{version_suffix}
Cargo downloads dependencies of Rust projects and compiles it.

%package -n cargo%{version_suffix}-doc
Summary:        Documentation for Cargo
# Cargo no longer builds its own documentation
# https://github.com/rust-lang/cargo/pull/4904
License:        Apache-2.0 OR MIT
Group:          Development/Languages/Rust
Requires:       rust%{version_suffix}-doc = %{version}
Conflicts:      cargo-doc < %{version}
Obsoletes:      cargo-doc < %{version}
Provides:       cargo-doc = %{version}
BuildArch:      noarch

%description -n cargo%{version_suffix}-doc
This package includes HTML documentation for Cargo.

%prep
%if %{with rust_bootstrap}
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
%endif

%if %{with rust_bootstrap}
    %global rust_root %{_builddir}/rust-%{version_current}-%{rust_triple}%{_prefix}
%else
    %global rust_root %{_prefix}
%endif

%setup -q -n rustc-%{version}-src

%patch0 -p1

# use python3
sed -i -e "1s|#!.*|#!%{_bindir}/python3|" x.py
sed -i.try-py3 -e '/try python2.7/i try python3 "$@"' ./configure

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
./configure \
  --host=%{_host} \
  --build=%{_build} \
  --prefix=%{_prefix} \
  --bindir=%{_bindir} \
  --sysconfdir=%{_sysconfdir} \
  --datadir=%{_datadir} \
  --localstatedir=%{_localstatedir} \
  --mandir=%{_mandir} \
  --infodir=%{_infodir} \
  --set rust.deny-warnings=false \
  --disable-option-checking \
  --build=%{rust_triple} --host=%{rust_triple} --target=%{rust_triple} \
  --enable-local-rust \
  --local-rust-root=%{rust_root} \
  --libdir=%{common_libdir} \
  --docdir=%{_docdir}/rust \
  %{!?with_bundled_llvm: --llvm-root=%{_prefix} --enable-llvm-link-shared} \
  %{?with_bundled_llvm: --disable-llvm-link-shared --set llvm.link-jobs=4} \
  --disable-codegen-tests \
  --enable-optimize \
  %{?with_sccache: --enable-sccache} \
  %{!?with_sccache: --enable-ccache} \
  %{?with_mddocs: --enable-docs} \
  %{!?with_mddocs: --disable-docs} \
  --enable-verbose-tests \
  --disable-jemalloc \
  --disable-rpath \
  %{codegen_units} \
  %{debug_info} \
  --enable-vendor \
  --enable-extended \
%if %{with devtools}
  --tools="cargo","rls","clippy","rustfmt","analysis","src" \
%else
  --tools="cargo","src" \
%endif
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
export LIBSSH2_SYS_USE_PKG_CONFIG=1
# END EXPORTS
EOF

. ./.env.sh

%if 0%{?strip_debug_flag}
export CFLAGS="$(echo $RPM_OPT_FLAGS | sed -e 's/ -g$//')"
%endif
export CXXFLAGS="$CFLAGS"
unset FFLAGS

./x.py build -v
%if %{with mddocs}
./x.py doc -v --stage 1
%endif

%install
# Reread exports file
. ./.env.sh

./x.py install
./x.py install src

# Remove executable permission from HTML documentation
# to prevent RPMLINT errors.
%if %{with mddocs}
chmod -R -x+X %{buildroot}%{_docdir}/rust/html

# Remove lockfile to avoid errors.
rm %{buildroot}%{_docdir}/rust/html/.lock

# Sanitize the HTML documentation
find %{buildroot}%{_docdir}/rust/html -empty -delete
find %{buildroot}%{_docdir}/rust/html -type f -exec chmod -x '{}' '+'
find %{buildroot}%{_docdir}/rust/html -type f -name '.nojekyll' -exec rm -v '{}' '+'

# The html docs for x86 and x86_64 are the same in most places
%fdupes -s %{buildroot}%{_docdir}/%{name}/html
%fdupes -s %{buildroot}/%{_mandir}
%fdupes %{buildroot}/%{_prefix}

# Cargo no longer builds its own documentation
# https://github.com/rust-lang/cargo/pull/4904
mkdir -p %{buildroot}%{_docdir}/cargo
ln -sT ../rust/html/cargo/ %{buildroot}%{_docdir}/cargo/html
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

# Remove exec bits from scripts in the src pkg
find %{buildroot}%{rustlibdir}/src/ -type f -exec chmod -x '{}' '+'

# The shared libraries should be executable to allow fdupes find duplicates.
find %{buildroot}%{common_libdir} -maxdepth 1 -type f -name '*.so' -exec chmod -v +x '{}' '+'

# The shared libraries should be executable for debuginfo extraction.
find %{buildroot}%{rustlibdir} -maxdepth 1 -type f -name '*.so' -exec chmod -v +x '{}' '+'

# Install rust-llvm-dwp in _bindir
mv %{buildroot}%{rustlibdir}/*-unknown-linux-gnu*/bin/rust-llvm-dwp  %{buildroot}%{_bindir}
rm -rf %{buildroot}%{rustlibdir}/*-unknown-linux-gnu*/bin

# Create the path for crate-devel packages
mkdir -p %{buildroot}%{_datadir}/cargo/registry

# Move the bash-completion to correct directory for openSUSE
install -D %{buildroot}%{_sysconfdir}/bash_completion.d/cargo %{buildroot}%{_datadir}/bash-completion/completions/cargo
# There should be nothing here at all
rm -rf %{buildroot}%{_sysconfdir}
# cargo does not respect our _libexec setting on Leap:
if [ ! -f %{buildroot}%{_libexecdir}/cargo-credential-1password ] &&
   [ -f %{buildroot}%{_exec_prefix}/libexec/cargo-credential-1password ]; then
	mv %{buildroot}%{_exec_prefix}/libexec/cargo-credential-1password	\
	   %{buildroot}%{_libexecdir}/cargo-credential-1password
fi

# Remove llvm installation
rm -rf %{buildroot}/home

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license COPYRIGHT LICENSE-APACHE LICENSE-MIT
%doc CONTRIBUTING.md README.md RELEASES.md
%{_bindir}/rustc
%{_bindir}/rustdoc
%{_bindir}/rust-lldb
%{_bindir}/rust-llvm-dwp
%{_mandir}/man1/rustc.1%{?ext_man}
%{_mandir}/man1/rustdoc.1%{?ext_man}
%{_prefix}/lib/lib*.so
%dir %{rustlibdir}
%dir %{rustlibdir}/%{rust_triple}
%dir %{rustlibdir}/%{rust_triple}/lib
%{rustlibdir}/%{rust_triple}/lib/*.so
%{rustlibdir}/%{rust_triple}/lib/*.rlib
%{_libexecdir}/cargo-credential-1password
%exclude %{_docdir}/rust/html
%exclude %{rustlibdir}/src

%files gdb
%{_bindir}/rust-gdb
%{_bindir}/rust-gdbgui
%dir %{rustlibdir}
%dir %{rustlibdir}%{_sysconfdir}
%{rustlibdir}%{_sysconfdir}/gdb_load_rust_pretty_printers.py
%{rustlibdir}%{_sysconfdir}/gdb_lookup.py
%{rustlibdir}%{_sysconfdir}/gdb_providers.py
%{rustlibdir}%{_sysconfdir}/lldb_commands
%{rustlibdir}%{_sysconfdir}/lldb_lookup.py
%{rustlibdir}%{_sysconfdir}/lldb_providers.py
%{rustlibdir}%{_sysconfdir}/rust_types.py

%if %{with mddocs}
%files doc
%dir %{_docdir}/rust
%dir %{_docdir}/rust/html
%doc %{_docdir}/rust/html/*
%endif

%files src
%dir %{rustlibdir}
%{rustlibdir}/src

%if %{with devtools}
%files -n rls%{version_suffix}
%license src/tools/rls/LICENSE-{APACHE,MIT}
%doc src/tools/rls/{README.md,COPYRIGHT,debugging.md}
%{_bindir}/rls
%endif

%if %{with devtools}
%files analysis
%{rustlibdir}/%{rust_triple}/analysis/
%endif

%files -n cargo%{version_suffix}
%license src/tools/cargo/LICENSE-{APACHE,MIT,THIRD-PARTY}
%license src/tools/rustfmt/LICENSE-{APACHE,MIT}
%license src/tools/clippy/LICENSE-{APACHE,MIT}
%{_bindir}/cargo
%if %{with devtools}
%{_bindir}/cargo-fmt
%{_bindir}/rustfmt
%{_bindir}/cargo-clippy
%{_bindir}/clippy-driver
%doc src/tools/rustfmt/{README,CHANGELOG,Configurations}.md
%doc src/tools/clippy/{README.md,CHANGELOG.md}
%endif
%{_mandir}/man1/cargo*.1%{?ext_man}
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/cargo
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_cargo
%dir %{_datadir}/cargo
%dir %{_datadir}/cargo/registry

%if %{with mddocs}
%files -n cargo%{version_suffix}-doc
%dir %{_docdir}/cargo
%{_docdir}/cargo/html
%endif

%changelog
