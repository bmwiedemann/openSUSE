#
# spec file for package rust
#
# Copyright (c) 2020 SUSE LLC
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


%global version_current 1.45.2
%global version_previous 1.44.1
%global version_bootstrap 1.44.1

# some sub-packages are versioned independently
%global rustfmt_version 1.4.16
%global clippy_version 0.0.212

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

# Will build with distro LLVM by default, but the following versions
# do not have a version new enough, >= 8.0 add --without bundled_llvm
# option, i.e. enable bundled_llvm by default Leap 42 to 42.3, SLE12
# SP1 to SLE12 SP3, Leap 15.1, SLE15 SP0
%if 0%{?sle_version} >= 120000 && 0%{?sle_version} <= 150100
%bcond_without bundled_llvm
%endif

# RLS requires 64-bit atomics
%ifarch ppc
%bcond_with rls
%else
%bcond_without rls
%endif

# Do not use parallel codegen in order to 
#   a) not exhaust memory on build-machines and 
#   b) generate the fastest possible binary
# at the cost of longer build times for this package
%define codegen_units --set rust.codegen-units=1
# Debuginfo can exhaust memory on these architecture workers
%ifarch  %{arm} %{ix86}
%define debug_info --disable-debuginfo --disable-debuginfo-only-std --disable-debuginfo-tools --disable-debuginfo-lines
%else
%define debug_info --enable-debuginfo --disable-debuginfo-only-std --enable-debuginfo-tools --disable-debuginfo-lines
%endif

%if 0%{?sle_version} >= 120000 && 0%{?sle_version} <= 120500
# Use hardening ldflags, plus link path for gcc7's libstdc++
%global gcc_arch %{_arch}
%ifarch %{ix86}
# This is where gcc7 puts things in 32-bit x86.
%global gcc_arch i586
%endif
%ifarch ppc64le
# This is where gcc7 puts things in ppc64le.
%global gcc_arch powerpc64le
%endif
%global rustflags -Clink-arg=-Wl,-z,relro,-z,now -L%{_libdir}/gcc/%{gcc_arch}-suse-linux/7
%else
# Use hardening ldflags
%global rustflags -Clink-arg=-Wl,-z,relro,-z,now
%endif

# Exclude implicitly-scanned Provides, especially the libLLVM.so ones:
%global __provides_exclude_from ^%{rustlibdir}/.*$

# enable the --with-rust_bootstrap flag
%bcond_with rust_bootstrap

Name:           rust
Version:        %{version_current}
Release:        0
Summary:        A systems programming language
License:        MIT OR Apache-2.0
Group:          Development/Languages/Rust
URL:            https://www.rust-lang.org
Source0:        %{dl_url}/rustc-%{version}-src.tar.xz
Source99:       %{name}-rpmlintrc
Source100:      %{dl_url}/rust-%{version_bootstrap}-x86_64-unknown-linux-gnu.tar.xz
Source101:      %{dl_url}/rust-%{version_bootstrap}-i686-unknown-linux-gnu.tar.xz
Source102:      %{dl_url}/rust-%{version_bootstrap}-aarch64-unknown-linux-gnu.tar.xz
Source103:      %{dl_url}/rust-%{version_bootstrap}-armv7-unknown-linux-gnueabihf.tar.xz
Source105:      %{dl_url}/rust-%{version_bootstrap}-powerpc64-unknown-linux-gnu.tar.xz
Source106:      %{dl_url}/rust-%{version_bootstrap}-powerpc64le-unknown-linux-gnu.tar.xz
Source107:      %{dl_url}/rust-%{version_bootstrap}-s390x-unknown-linux-gnu.tar.xz
Source108:      %{dl_url}/rust-%{version_bootstrap}-powerpc-unknown-linux-gnu.tar.xz
# Not yet available
#Source109:      %{dl_url}/rust-%{version_bootstrap}-riscv64gc-unknown-linux-gnu.tar.xz
# Make factory-auto stop complaining...
Source1000:     README.suse-maint
# PATCH-FIX-OPENSUSE: edit src/librustc_llvm/build.rs to ignore GCC incompatible flag
Patch0:         ignore-Wstring-conversion.patch
BuildRequires:  ccache
BuildRequires:  curl
BuildRequires:  fdupes
BuildRequires:  git
BuildRequires:  pkgconfig
BuildRequires:  procps
BuildRequires:  python3-base
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(zlib)
# Leap 42 to 42.3, SLE12 SP1, SP2
%if 0%{?sle_version} >= 120000 && 0%{?sle_version} <= 120200
# In these distros cmake is 2.x, so we need cmake3 for building llvm.
BuildRequires:  cmake3
%else
# cmake got upgraded to 3.5 in SLE-12 SP2
BuildRequires:  cmake
%endif
# In all of SLE12, the default gcc is 4.8.  Rust's LLVM wants 5.1 at least.
# So, we'll just use gcc7.
%if 0%{?sle_version} >= 120000 && 0%{?sle_version} <= 120500
BuildRequires:  gcc7-c++
%else
BuildRequires:  gcc-c++
%endif
# The following requires must mirror: LIBSSH2_SYS_USE_PKG_CONFIG
%if !%{with rust_bootstrap} && 0%{?sle_version} >= 150000
BuildRequires:  pkgconfig(libssh2) >= 1.6.0
%endif
# Real LLVM minimum version should be 8.x, but rust has a fallback
# mode
%if !%with bundled_llvm
BuildRequires:  llvm-devel >= 8.0
%endif
%if !%with rust_bootstrap
# We will now package cargo using the version number of rustc since it
# is being built from rust sources. Old cargo packages have a 0.x
# number
BuildRequires:  cargo <= %{version_current}
BuildRequires:  cargo >= %{version_previous}
BuildRequires:  rust <= %{version_current}
BuildRequires:  rust >= %{version_previous}
BuildRequires:  rust-std-static <= %{version_current}
BuildRequires:  rust-std-static >= %{version_previous}
%endif
# The compiler is not generally useful without the std library
# installed and the std library is exactly specific to the version of
# the compiler
Requires:       %{name}-std-static = %{version}
Recommends:     %{name}-doc
Recommends:     cargo
Conflicts:      rust
Conflicts:      rustc-bootstrap
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

%package -n rust-std-static
Summary:        Standard library for Rust
License:        MIT OR Apache-2.0
Group:          Development/Languages/Rust
Requires:       %{name} = %{version}
Conflicts:      rust-std < %{version}
Obsoletes:      rust-std < %{version}
Provides:       rust-std = %{version}

%description -n rust-std-static
This package includes the standard libraries for building applications
written in Rust.

%package -n rust-doc
Summary:        Rust documentation
License:        MIT OR Apache-2.0
Group:          Development/Languages/Rust
Requires:       %{name} = %{version}

%description -n rust-doc
Documentation for the Rust language.

%package -n rust-gdb
Summary:        Gdb integration for rust binaries
License:        MIT OR Apache-2.0
Group:          Development/Languages/Rust
Requires:       %{name} = %{version}
%if 0%{?suse_version} && 0%{?suse_version} < 1500
# Legacy SUSE-only form
Supplements:    packageand(%{name}:gdb)
%else
# Standard form
Supplements:    (%{name} and gdb)
%endif

%description -n rust-gdb
This subpackage provides pretty printers and a wrapper script for
invoking gdb on rust binaries.

%package -n rust-src
Summary:        Sources for the Rust standard library
License:        MIT OR Apache-2.0
Group:          Development/Languages/Rust
Requires:       %{name} = %{version}
BuildArch:      noarch

%description -n rust-src
This package includes source files for the Rust standard library. This
is commonly used for function detail lookups in helper programs such
as RLS or racer.

%package -n rls
Summary:        Language server for Rust lang
License:        MIT OR Apache-2.0
Group:          Development/Languages/Rust
Requires:       %{name} = %{version}
Requires:       %{name}-analysis = %{version}
Requires:       %{name}-src = %{version}

%description -n rls
The RLS provides a server that runs in the background, providing IDEs,
editors, and other tools with information about Rust programs. It
supports functionality such as 'goto definition', symbol search,
reformatting, and code completion, and enables renaming and
refactorings.  It can be used with an IDE such as Gnome-Builder.

%package -n rust-analysis
Summary:        Compiler analysis data for the Rust standard library
License:        MIT OR Apache-2.0
Group:          Development/Languages/Rust
Requires:       rust-std-static = %{version}

%description -n rust-analysis
This package contains analysis data files produced with rustc's
-Zsave-analysis feature for the Rust standard library. The RLS (Rust
Language Server) uses this data to provide information about the Rust
standard library.

%package -n rustfmt
Summary:        Code formatting tool for Rust lang
License:        MIT OR Apache-2.0
Group:          Development/Languages/Rust
Requires:       %{name} = %{version}
Requires:       cargo = %{version}
Provides:       cargo-fmt = %{rustfmt_version}
Provides:       rustfmt = %{rustfmt_version}
%if 0%{?suse_version} && 0%{?suse_version} < 1500
# Legacy SUSE-only form
Supplements:    packageand(%{name}:cargo)
%else
# Standard form
Supplements:    (%{name} and cargo)
%endif

%description -n rustfmt
A tool for formatting Rust code according to style guidelines.

%package -n clippy
Summary:        Lints to catch common mistakes and improve Rust code
# /usr/bin/clippy-driver is dynamically linked against internal rustc libs
License:        MPL-2.0
Group:          Development/Languages/Rust
Requires:       %{name} = %{version}
Requires:       cargo = %{version}
Provides:       clippy = %{clippy_version}

%description -n clippy
A collection of lints to catch common mistakes and improve Rust code.

%package -n cargo
Summary:        The Rust package manager
License:        MIT OR Apache-2.0
Group:          Development/Languages/Rust
Requires:       %{name} = %{version}
Conflicts:      cargo < %{version}
Obsoletes:      cargo < %{version}
Conflicts:      cargo-vendor < %{version}
Obsoletes:      cargo-vendor < %{version}
Provides:       rustc:%{_bindir}/cargo = %{version}

%description -n cargo
Cargo downloads dependencies of Rust projects and compiles it.

%package -n cargo-doc
Summary:        Documentation for Cargo
# Cargo no longer builds its own documentation
# https://github.com/rust-lang/cargo/pull/4904
License:        MIT OR Apache-2.0
Group:          Development/Languages/Rust
Requires:       rust-doc = %{version}
BuildArch:      noarch

%description -n cargo-doc
This package includes HTML documentation for Cargo.

%prep
%if %{with rust_bootstrap}
%ifarch x86_64
%setup -q -T -b 100 -n rust-%{version_bootstrap}-%{rust_triple}
%endif
%ifarch %{ix86}
%setup -q -T -b 101 -n rust-%{version_bootstrap}-%{rust_triple}
%endif
%ifarch aarch64
%setup -q -T -b 102 -n rust-%{version_bootstrap}-%{rust_triple}
%endif
%ifarch armv7hl
%setup -q -T -b 103 -n rust-%{version_bootstrap}-%{rust_triple}
%endif
%ifarch armv6hl
%setup -q -T -b 104 -n rust-%{version_bootstrap}-%{rust_triple}
%endif
%ifarch ppc64
%setup -q -T -b 105 -n rust-%{version_bootstrap}-%{rust_triple}
%endif
%ifarch ppc64le
%setup -q -T -b 106 -n rust-%{version_bootstrap}-%{rust_triple}
%endif
%ifarch s390x
%setup -q -T -b 107 -n rust-%{version_bootstrap}-%{rust_triple}
%endif
%ifarch ppc
%setup -q -T -b 108 -n rust-%{version_bootstrap}-%{rust_triple}
%endif
%ifarch riscv64
# Not yet available
#%%setup -q -T -b 109 -n rust-%{version_bootstrap}-%{rust_triple}
%endif
./install.sh --components=cargo,rustc,rust-std-%{rust_triple} --prefix=.%{_prefix} --disable-ldconfig
%endif

%if %{with rust_bootstrap}
    %global rust_root %{_builddir}/rust-%{version_bootstrap}-%{rust_triple}%{_prefix}
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

# Remove hidden files from source
find src/ -type f -name '.appveyor.yml' -exec rm -v '{}' '+'
find src/ -type f -name '.travis.yml' -exec rm -v '{}' '+'
find src/ -type f -name '.cirrus.yml' -exec rm -v '{}' '+'

%if !%with bundled_llvm
rm -rf src/llvm/
%endif

# The configure macro will modify some autoconf-related files, which upsets
# cargo when it tries to verify checksums in those files.  If we just truncate
# that file list, cargo won't have anything to complain about.
find vendor -name .cargo-checksum.json \
  -exec sed -i.uncheck -e 's/"files":{[^}]*}/"files":{ }/' '{}' '+'

# Fix rpmlint error "This script uses 'env' as an interpreter"
sed -i '1s|#!%{_bindir}/env python|#!%{_bindir}/python3|' src/libcore/unicode/printable.py
chmod +x src/libcore/unicode/printable.py

%build
%define _lto_cflags %{nil}
%configure \
  --set rust.deny-warnings=false \
  --disable-option-checking \
  --build=%{rust_triple} --host=%{rust_triple} --target=%{rust_triple} \
  --enable-local-rust \
  --local-rust-root=%{rust_root} \
  --libdir=%{common_libdir} \
  --docdir=%{_docdir}/%{name} \
  %{!?with_bundled_llvm: --llvm-root=%{_prefix} --enable-llvm-link-shared} \
  %{?with_bundled_llvm: --disable-llvm-link-shared --set llvm.link-jobs=4} \
  --disable-codegen-tests \
  --enable-optimize \
  --enable-ccache \
  --enable-docs \
  --enable-verbose-tests \
  --disable-jemalloc \
  --disable-rpath \
  %{debug_info} \
  %{codegen_units} \
  --enable-vendor \
  --enable-extended \
%if %{with rls}
  --tools="cargo","rls","clippy","rustfmt","analysis","src" \
%else
  --tools="cargo","clippy","rustfmt","analysis","src" \
%endif
  --release-channel="stable"

# Sometimes we may be rebuilding with the same compiler,
# setting local-rebuild will skip stage0 build, reducing build time
if [ $(%{rust_root}/bin/rustc --version | sed -En 's/rustc ([0-9].[0-9][0-9].[0-9]).*/\1/p') = '%{version}' ]; then
sed -i -e "s|#local-rebuild = false|local-rebuild = true|" config.toml;
fi

# Create exports file
# Keep all the "export VARIABLE" together here, so they can be
# reread in the %%install section below.
# If the environments between build and install and different,
# everything will be rebuilt during installation!
cat > .env.sh <<\EOF
export RUSTFLAGS="%{rustflags}"
%if 0%{?sle_version} >= 120000 && 0%{?sle_version} <= 120500
export CC=gcc-7
export CXX=g++-7
%endif
# Make cargo use system libs if not bootstrapping
%if !%{with rust_bootstrap} && 0%{?sle_version} >= 150000
export LIBSSH2_SYS_USE_PKG_CONFIG=1
%endif
# eliminate complaint from RPMlint
export CPPFLAGS="%{optflags}"
export DESTDIR=%{buildroot}
# END EXPORTS
EOF
. ./.env.sh

./x.py build -v
./x.py doc -v

%install
# Reread exports file
. ./.env.sh

./x.py install
./x.py install src

# Remove executable permission from HTML documentation
# to prevent RPMLINT errors.
chmod -R -x+X %{buildroot}%{_docdir}/%{name}/html

# Remove lockfile to avoid errors.
rm %{buildroot}%{_docdir}/%{name}/html/.lock

# Sanitize the HTML documentation
find %{buildroot}%{_docdir}/%{name}/html -empty -delete
find %{buildroot}%{_docdir}/%{name}/html -type f -exec chmod -x '{}' '+'
find %{buildroot}%{_docdir}/%{name}/html -type f -name '.nojekyll' -exec rm -v '{}' '+'

# Remove the license files from _docdir: make install put duplicates there
rm %{buildroot}%{_docdir}/%{name}/{README.md,COPYRIGHT,LICENSE*}
rm %{buildroot}%{_docdir}/%{name}/*.old

# Remove installer artifacts (manifests, uninstall scripts, etc.)
find %{buildroot}%{rustlibdir} -maxdepth 1 -type f -exec rm -v '{}' '+'

# The shared libraries should be executable for debuginfo extraction.
find %{buildroot}%{rustlibdir} -maxdepth 1 -type f -name '*.so' -exec chmod -v +x '{}' '+'

# The html docs for x86 and x86_64 are the same in most places
%fdupes -s %{buildroot}%{_docdir}/%{name}/html
%fdupes -s %{buildroot}/%{_mandir}
%fdupes %{buildroot}/%{_prefix}

# Create the path for crate-devel packages
mkdir -p %{buildroot}%{_datadir}/cargo/registry

# Cargo no longer builds its own documentation
# https://github.com/rust-lang/cargo/pull/4904
mkdir -p %{buildroot}%{_docdir}/cargo
ln -sT ../rust/html/cargo/ %{buildroot}%{_docdir}/cargo/html

# Move the bash-completition to correct directory for openSUSE
install -D %{buildroot}%{_sysconfdir}/bash_completion.d/cargo %{buildroot}%{_datadir}/bash-completion/completions/cargo
# There should be nothing here at all
rm -rf %{buildroot}%{_sysconfdir}

# Remove llvm installation
rm -rf %{buildroot}/home

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%if 0%{?suse_version} == 1315
%doc COPYRIGHT LICENSE-APACHE LICENSE-MIT
%else
%license COPYRIGHT LICENSE-APACHE LICENSE-MIT
%endif
%doc CONTRIBUTING.md README.md RELEASES.md
%{_bindir}/rustc
%{_bindir}/rustdoc
%{_bindir}/rust-lldb
%{_mandir}/man1/rustc.1%{?ext_man}
%{_mandir}/man1/rustdoc.1%{?ext_man}
%{_prefix}/lib/lib*.so
%dir %{rustlibdir}
%dir %{rustlibdir}/%{rust_triple}
%dir %{rustlibdir}/%{rust_triple}/lib
%{rustlibdir}/%{rust_triple}/lib/*.so
%exclude %{_docdir}/%{name}/html
%exclude %{rustlibdir}/src

%files -n rust-std-static
%dir %{rustlibdir}
%dir %{rustlibdir}/%{rust_triple}
%dir %{rustlibdir}/%{rust_triple}/lib
%{rustlibdir}/%{rust_triple}/lib/*.rlib

%files -n rust-gdb
%{_bindir}/rust-gdb
%{_bindir}/rust-gdbgui
%dir %{rustlibdir}
%dir %{rustlibdir}%{_sysconfdir}
%{rustlibdir}%{_sysconfdir}/debugger_pretty_printers_common.py
%{rustlibdir}%{_sysconfdir}/gdb_load_rust_pretty_printers.py
%{rustlibdir}%{_sysconfdir}/gdb_rust_pretty_printing.py
%{rustlibdir}%{_sysconfdir}/lldb_rust_formatters.py

%files -n rust-doc
%dir %{_docdir}/%{name}
%dir %{_docdir}/%{name}/html
%doc %{_docdir}/%{name}/html/*

%files -n rust-src
%dir %{rustlibdir}
%{rustlibdir}/src

%if %{with rls}
%files -n rls
%if 0%{?suse_version} == 1315 && !0%{?is_opensuse}
%doc src/tools/rls/LICENSE-{APACHE,MIT}
%else
%license src/tools/rls/LICENSE-{APACHE,MIT}
%endif
%doc src/tools/rls/{README.md,COPYRIGHT,debugging.md}
%{_bindir}/rls
%endif

%files analysis
%{rustlibdir}/%{rust_triple}/analysis/

%files -n rustfmt
%if 0%{?suse_version} == 1315 && !0%{?is_opensuse}
%doc src/tools/rustfmt/LICENSE-{APACHE,MIT}
%else
%license src/tools/rustfmt/LICENSE-{APACHE,MIT}
%endif
%doc src/tools/rustfmt/{README,CHANGELOG,Configurations}.md
%{_bindir}/cargo-fmt
%{_bindir}/rustfmt

%files -n clippy
%if 0%{?suse_version} == 1315 && !0%{?is_opensuse}
%doc src/tools/clippy/LICENSE-{APACHE,MIT}
%else
%license src/tools/clippy/LICENSE-{APACHE,MIT}
%endif
%doc src/tools/clippy/{README.md,CHANGELOG.md}
%{_bindir}/cargo-clippy
%{_bindir}/clippy-driver

%files -n cargo
%if 0%{?suse_version} == 1315 && !0%{?is_opensuse}
%doc src/tools/cargo/LICENSE-{APACHE,MIT,THIRD-PARTY}
%else
%license src/tools/cargo/LICENSE-{APACHE,MIT,THIRD-PARTY}
%endif
%{_bindir}/cargo
%{_mandir}/man1/cargo*.1%{?ext_man}
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/cargo
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_cargo
%dir %{_datadir}/cargo
%dir %{_datadir}/cargo/registry

%files -n cargo-doc
%dir %{_docdir}/cargo
%{_docdir}/cargo/html

%changelog
