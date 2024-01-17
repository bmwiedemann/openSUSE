#
# spec file for package julia
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


# We must not strip binaries in julia, since it can lead to many problems.
# For example, see:
#
# https://github.com/JuliaLang/julia/issues/17941
%undefine _build_create_debug
%define __arch_install_post export NO_BRP_STRIP_DEBUG=true

%global __provides_exclude_from ^%{_libdir}/%{name}/.*\\.so$

# List all bundled libraries.
%global _privatelibs lib(LLVM-.*|ccalltest|llvmcalltest|uv|openblas.*|sys|julia.*)\\.so.*
%global __provides_exclude ^(%{_privatelibs})$
%global __requires_exclude ^(%{_privatelibs})$

%define libjulia_sover_major 1
%define libjulia_sover_minor 9

%if "@BUILD_FLAVOR@%{nil}" == "compat"
%define compat_mode  1
%else
%define compat_mode  0
%endif

%if 0%{?compat_mode}
%define libname              libjulia-compat%{libjulia_sover_major}
%else
%define libname              libjulia%{libjulia_sover_major}
%endif

# LTO currently makes building blastrampoline and Julia itself fail
# It is not enabled upstream anyway
%global _lto_cflags %nil
Version:        1.9.4
Release:        0
URL:            http://julialang.org/
Source0:        https://github.com/JuliaLang/julia/releases/download/v%{version}/julia-%{version}-full.tar.gz
Source1:        julia-rpmlintrc
# PATCH-FIX-OPENSUSE julia-env-script-interpreter.patch ronisbr@gmail.com -- Change script interpreted to avoid errors in rpmlint.
Patch1:         julia-env-script-interpreter.patch
Patch2:         https://gitlab.archlinux.org/archlinux/packaging/packages/julia/-/raw/main/e08e1444.patch?ref_type=heads#/new-pass-manager.patch
Patch3:         https://gitlab.archlinux.org/archlinux/packaging/packages/julia/-/raw/main/959902f1.patch?ref_type=heads#/support-float16-depending-on-llvm-and-platform.patch
Patch4:         https://gitlab.archlinux.org/archlinux/packaging/packages/julia/-/raw/main/f11bfc6c.patch?ref_type=heads#/use-newpm-asan.patch
Patch5:         https://gitlab.archlinux.org/archlinux/packaging/packages/julia/-/raw/main/21d4c2f1.patch?ref_type=heads#/llvm-set-of-custom-patches.patch
Patch6:         https://gitlab.archlinux.org/archlinux/packaging/packages/julia/-/raw/main/julia-libunwind-1.6.patch?ref_type=heads#/julia-libunwind-1.9.patch
Patch8:         https://gitlab.archlinux.org/archlinux/packaging/packages/julia/-/raw/main/julia-libgit2-1.7.patch?ref_type=heads#/julia-libgit2-1.7.patch
Patch9:         https://gitlab.archlinux.org/archlinux/packaging/packages/julia/-/raw/main/julia-suitesparse-7.patch?ref_type=heads#/julia-suitesparse-7.patch
Patch10:        use-system-libuv-correctly.patch
Patch11:        openlibm.patch
Patch12:        llvm-link-shared.patch
# Adapted from https://gitlab.archlinux.org/archlinux/packaging/packages/julia/-/raw/main/julia-hardcoded-libs.patch?ref_type=heads
# We just remove the julia specific llvm sofile change
Patch13:        julia-hardcoded-libs.patch
Patch14:        mbedtls-hardcoded-libs.patch
Patch15:        libblastrampoline-hardcoded-libs.patch
BuildRequires:  arpack-ng-devel >= 3.3.0
BuildRequires:  blas-devel
BuildRequires:  ca-certificates
BuildRequires:  cmake
BuildRequires:  dSFMT-devel
BuildRequires:  dos2unix
BuildRequires:  double-conversion-devel
BuildRequires:  fdupes
BuildRequires:  fftw3-threads-devel >= 3.3.4
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
BuildRequires:  git
BuildRequires:  gmp-devel >= 6.1.2
BuildRequires:  hicolor-icon-theme
BuildRequires:  lapack-devel >= 3.5.0
BuildRequires:  libblastrampoline-devel
BuildRequires:  libcurl-devel
BuildRequires:  libgit2-devel
BuildRequires:  libnghttp2-devel
BuildRequires:  libopenblas_openmp-devel >= 0.3.5
BuildRequires:  libssh2-devel >= 1.9.0
BuildRequires:  libunwind-devel >= 1.3.1
BuildRequires:  libuv-devel
BuildRequires:  libwhich
BuildRequires:  lld14
BuildRequires:  llvm14-devel
BuildRequires:  m4
BuildRequires:  mbedtls-devel
BuildRequires:  mpfr-devel >= 4.0.2
BuildRequires:  ncurses-devel
BuildRequires:  openblas-common-devel
BuildRequires:  openlibm-devel
BuildRequires:  openspecfun-devel
BuildRequires:  openssl
BuildRequires:  p7zip >= 16
BuildRequires:  patchelf >= 0.9
BuildRequires:  pcre2-devel >= 10.31
BuildRequires:  perl
BuildRequires:  python >= 2.5
BuildRequires:  readline-devel
BuildRequires:  suitesparse-devel >= 5.4.0
BuildRequires:  update-desktop-files
BuildRequires:  utf8proc-devel
BuildRequires:  zlib-devel
Requires:       ca-certificates
Requires:       p7zip >= 16
Requires:       readline

# Libraries used by CompilerSupportLibraries_jll, blastrampoline,
# nghttp2_jll but not detected as they are dlopen()ed but not linked to
%if 0%{?__isa_bits} == 64
Requires:       libgfortran.so.5()(64bit)
Requires:       libgomp.so.1()(64bit)
Requires:       libnghttp2.so.14()(64bit)
%else
Requires:       libgfortran.so.5
Requires:       libgomp.so.1
Requires:       libnghttp2.so.14
%endif

# Same as the previous comment. But the difference
# is that we applied julia-hardcoded-libs.patch
# so therefore it is needed
Requires:       libblastrampoline-devel
Requires:       libnghttp2-devel
Requires:       openlibm-devel
Requires:       suitesparse-devel

# Julia requires the devel package as well
# specifically libjulia.so
%if 0%{?compat_mode}
Requires:       julia-compat-devel
%else
Requires:       julia-devel
%endif

Requires(post): %{_sbindir}/update-alternatives
Requires(post): %{_sbindir}/ldconfig
Requires(postun):%{_sbindir}/update-alternatives
Requires(postun):%{_sbindir}/ldconfig
Recommends:     arpack-ng-devel
Recommends:     git
Recommends:     gmp-devel
Recommends:     mpfr-devel
Recommends:     openspecfun-devel
Recommends:     pcre2-devel
Recommends:     suitesparse-devel
%if 0%{?compat_mode} == 0
Name:           julia
%else
Name:           julia-compat
%endif
%if 0%{?compat_mode} == 0
Summary:        High-level, high-performance dynamic programming language
License:        BSD-3-Clause AND GPL-2.0-or-later AND MIT AND Zlib
Group:          Development/Languages/Other
%else
Summary:        High-level, high-performance dynamic programming language (without CPU optim.)
License:        BSD-3-Clause AND GPL-2.0-or-later AND MIT AND Zlib
Group:          Development/Languages/Other
%endif
%if 0%{?compat_mode}
Conflicts:      julia
Provides:       julia = %{version}
%endif

# Let's not be optimistic towards 32 bit support and other architectures
# openSUSE cannot guarantee to support, shall we?
ExclusiveArch:  x86_64

%description
Julia is a high-level, high-performance dynamic programming language for
technical computing, with syntax that is familiar to users of other technical
computing environments. It provides a sophisticated compiler, distributed
parallel execution, numerical accuracy, and an extensive mathematical function
library. The library, largely written in Julia itself, also integrates mature,
best-of-breed C and Fortran libraries for linear algebra, random number
generation, signal processing, and string processing.

This package is experimental and by no means supported by upstream. If you want
to use julia, please install juliaup instead.

%package        devel
Summary:        Julia development, debugging and testing files
Group:          Development/Languages/Other
Requires:       %{libname} = %{version}
%if 0%{?compat_mode}
Conflicts:      julia-devel
Provides:       julia-devel
%endif

%description    devel
Contains library symbolic links and header files for developing applications
linking to the Julia library, in particular embedding it, as well as tests and a
debugging version of Julia. This package is normally not needed when programming
in the Julia language, but rather for embedding Julia into external programs or
debugging Julia itself.

%package -n     %{libname}
Summary:        Julia shared object libraries
Group:          System/Libraries
%if 0%{?compat_mode}
Conflicts:      libjulia%{libjulia_sover_major}
Provides:       libjulia%{libjulia_sover_major}
%endif

%description -n %{libname}
Contains library files for interacting with Julia through C interfaces.

%prep
%setup -q -n julia-%{version}
patch -p1 -i %{PATCH1}
# patch -p1 -i %%{PATCH2}
# patch -p1 -i %%{PATCH3}
# patch -p1 -i %%{PATCH4}
# patch -p1 -i %%{PATCH5}
# libunwind 1.6 compatibility
patch -p1 -i %{PATCH6}
# Fix tests with libgit2 1.7
patch -p1 -i %{PATCH8}
# Make.inc puts it in the wrong libpath
# patch -p1 -i %%{PATCH10}
patch -p1 -i %{PATCH11}
patch -p1 -i %{PATCH12}
patch -p1 -i %{PATCH13}
patch -p1 -i %{PATCH14}
patch -p1 -i %{PATCH15}

%ifarch aarch64 %{arm}
# https://github.com/JuliaLang/julia/issues/41613#issuecomment-976535193
sed -i 's#$(eval $(call symlink_system_library,CSL,libquadmath,0))##' base/Makefile
%endif

pushd stdlib/srccache
  tar -xzf SparseArrays-37e6e58706a54c5a1b96a17cda7d3e8be8bcb190.tar.gz
  patch -d JuliaSparse-SparseArrays.jl-37e6e58 -p1 -i %{PATCH9}
  rm SparseArrays-37e6e58706a54c5a1b96a17cda7d3e8be8bcb190.tar.gz
  tar -czf SparseArrays-37e6e58706a54c5a1b96a17cda7d3e8be8bcb190.tar.gz JuliaSparse-SparseArrays.jl-37e6e58
  md5sum SparseArrays-37e6e58706a54c5a1b96a17cda7d3e8be8bcb190.tar.gz | cut -d ' ' -f 1 > ../../deps/checksums/SparseArrays-37e6e58706a54c5a1b96a17cda7d3e8be8bcb190.tar.gz/md5
  sha512sum SparseArrays-37e6e58706a54c5a1b96a17cda7d3e8be8bcb190.tar.gz | cut -d ' ' -f 1 > ../../deps/checksums/SparseArrays-37e6e58706a54c5a1b96a17cda7d3e8be8bcb190.tar.gz/sha512

popd

# Work around bug that prompts zlib to be downloaded even when not used
# https://github.com/JuliaLang/julia/pull/42524/files#r734972945
sed "s/ \$(build_prefix)\\/manifest\\/zlib//" -i deps/llvm.mk

%build

%if 0%{?compat_mode} == 0
    %ifarch x86_64
        %define julia_march core2
    %endif

    %ifarch %{ix86}
        %define julia_march pentium4
    %endif

    %ifarch aarch64
        %define julia_march armv8-a
    %endif

    %ifarch armv7l armv7hl
       %define julia_march armv7-a
    %endif

    %ifarch armv6l armv6hl
        %define julia_march armv6
    %endif

    %ifarch ppc64le
        %define julia_march ppc64le
    %endif
%else
    # compat_mode is only defined for 64-bit architecture.

    %define julia_march x86-64
%endif

%ifarch armv6l armv6hl
export LDFLAGS="$LDFLAGS -latomic"
%endif

export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags}"
export LD_LIBRARY_PATH=%{_builddir}/%{buildsubdir}/build/usr/lib:%{_builddir}/%{buildsubdir}/build%{_libdir}:%{_builddir}/%{buildsubdir}/usr/lib

pushd deps
    export BUILDDIR="%{_builddir}/%{buildsubdir}/build"
    export USE_BLAS64=1
    export USE_BINARYBUILDER_OPENBLAS=0
    export OPENBLAS_LIBNAMESUFFIX="%{?__isa_bits}_"
    export OPENBLAS_SYMBOLSUFFIX="%{?__isa_bits}_"
    export OPENBLAS_CFLAGS="%{optflags}"
    make prefix=%{prefix} libdir=%{_libdir} bindir=%{_bindir} install-openblas
popd

make %{?_smp_mflags} \
                     MARCH=%{julia_march} \
%ifarch aarch64
                     JULIA_CPU_TARGET="generic;cortex-a57;thunderx2t99;armv8.2-a,crypto,fullfp16,lse,rdm" \
%endif
%ifarch x86_64
                     JULIA_CPU_TARGET="generic;sandybridge,-xsaveopt,clone_all;haswell,-rdrnd,base(1)" \
%endif
                     build_prefix=%{_builddir}/%{buildsubdir}/build%{_prefix} \
                     build_libdir=%{_builddir}/%{buildsubdir}/build%{_libdir} \
                     prefix=%{_prefix} \
                     bindir=%{_bindir} \
                     libdir=%{_libdir} \
                     libexecdir=%{_libexecdir} \
                     datarootdir=%{_datarootdir} \
                     includedir=%{_includedir} \
                     sysconfdir=%{_sysconfdir} \
                     USE_BINARYBUILDER=0 \
                     USE_SYSTEM_CSL=1 \
                     USE_SYSTEM_LLVM=0 \
                     USE_SYSTEM_LLD=1 \
                     USE_SYSTEM_LIBUNWIND=1 \
                     USE_SYSTEM_PCRE=1 \
                     USE_SYSTEM_BLAS=0 \
                     USE_SYSTEM_LAPACK=0 \
                     USE_SYSTEM_LIBBLASTRAMPOLINE=1 \
                     USE_SYSTEM_GMP=1 \
                     USE_SYSTEM_MPFR=1 \
                     USE_SYSTEM_LIBSUITESPARSE=1 \
                     USE_SYSTEM_SUITESPARSE=1 \
                     USE_INTEL_JITEVENTS=0 \
                     USE_SYSTEM_LIBWHICH=1 \
                     USE_SYSTEM_DSFMT=1 \
                     USE_SYSTEM_LIBUV=0 \
                     USE_SYSTEM_UTF8PROC=1 \
                     USE_SYSTEM_LIBGIT2=1 \
                     USE_SYSTEM_LIBSSH2=1 \
                     USE_SYSTEM_MBEDTLS=1 \
                     USE_SYSTEM_CURL=1 \
                     USE_SYSTEM_PATCHELF=1 \
                     USE_SYSTEM_ZLIB=1 \
                     USE_SYSTEM_P7ZIP=1 \
                     USE_SYSTEM_OPENLIBM=1 \
                     USE_BLAS64=1 \
                     JLDFLAGS="$LDFLAGS" \
                     VERBOSE=1 \
                     TAGGED_RELEASE_BANNER="openSUSE %{suse_version} experimental build (unofficial)" \
                     release debug

# This may fix other issues where libLLVM-14jl.so is not properly copied?
if [ "x%{_lib}" != xlib ] ; then
  cp -a %{_builddir}/%{buildsubdir}/build/usr/lib/* %{_builddir}/%{buildsubdir}/build/%{_libdir}
  rm -rf %{_builddir}/%{buildsubdir}/build/usr/lib/
fi

%check
# The tests will only pass if openblas is being used.
# make %{?_smp_mflags} test

%install

%ifarch armv6l armv6hl
export LDFLAGS="$LDFLAGS -latomic"
%endif

export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags}"
export LD_LIBRARY_PATH=%{_builddir}/%{buildsubdir}/build/usr/lib:%{_builddir}/%{buildsubdir}/build%{_libdir}:%{_builddir}/%{buildsubdir}/usr/lib

make install DESTDIR=%{buildroot} \
             MARCH=%{julia_march} \
%ifarch aarch64
                     JULIA_CPU_TARGET="generic;cortex-a57;thunderx2t99;armv8.2-a,crypto,fullfp16,lse,rdm" \
%endif
%ifarch x86_64
                     JULIA_CPU_TARGET="generic;sandybridge,-xsaveopt,clone_all;haswell,-rdrnd,base(1)" \
%endif
             build_prefix=%{_builddir}/%{buildsubdir}/build%{_prefix} \
             build_libdir=%{_builddir}/%{buildsubdir}/build%{_libdir} \
             prefix=%{_prefix} \
             bindir=%{_bindir} \
             libdir=%{_libdir} \
             libexecdir=%{_libexecdir} \
             datarootdir=%{_datarootdir} \
             includedir=%{_includedir} \
             sysconfdir=%{_sysconfdir} \
             USE_BINARYBUILDER=0 \
             USE_SYSTEM_CSL=1 \
             USE_SYSTEM_LLVM=0 \
             USE_SYSTEM_LLD=1 \
             USE_SYSTEM_LIBUNWIND=1 \
             USE_SYSTEM_PCRE=1 \
             USE_SYSTEM_BLAS=0 \
             USE_SYSTEM_LAPACK=0 \
             USE_SYSTEM_LIBBLASTRAMPOLINE=1 \
             USE_SYSTEM_GMP=1 \
             USE_SYSTEM_MPFR=1 \
             USE_SYSTEM_LIBSUITESPARSE=1 \
             USE_SYSTEM_SUITESPARSE=1 \
             USE_INTEL_JITEVENTS=0 \
             USE_SYSTEM_LIBWHICH=1 \
             USE_SYSTEM_DSFMT=1 \
             USE_SYSTEM_LIBUV=0 \
             USE_SYSTEM_UTF8PROC=1 \
             USE_SYSTEM_LIBGIT2=1 \
             USE_SYSTEM_LIBSSH2=1 \
             USE_SYSTEM_MBEDTLS=1 \
             USE_SYSTEM_CURL=1 \
             USE_SYSTEM_PATCHELF=1 \
             USE_SYSTEM_ZLIB=1 \
             USE_SYSTEM_P7ZIP=1 \
             USE_SYSTEM_OPENLIBM=1 \
             USE_BLAS64=1 \
             JLDFLAGS="$LDFLAGS" \
             VERBOSE=1 \
             TAGGED_RELEASE_BANNER="openSUSE %{suse_version} experimental build (unofficial)"

# GZip man page.
gzip %{buildroot}/%{_mandir}/man1/julia.1

# Copy the man page for every executable.
cd %{buildroot}/%{_mandir}/man1/

rm -f %{buildroot}%{_libdir}/julia/libuv.a
rm -f %{buildroot}%{_datadir}/julia/base/build.h
rm -f %{buildroot}%{_datadir}/julia/base/Makefile

# Fix documentation directories.
mkdir -p %{buildroot}%{_docdir}/julia
mv -f %{buildroot}%{_datadir}/doc/julia/* %{buildroot}%{_docdir}/julia/
rm -r %{buildroot}%{_datadir}/doc/julia

ln -sfv /var/lib/ca-certificates/ca-bundle.pem %{buildroot}%{_datadir}/julia/cert.pem   # Needed by some julia packages

# Remove execution permission on documentation files.
chmod -x+X -R %{buildroot}%{_docdir}/julia/*

# Remove hidden files and zero-length files and directories from stdlib.
pushd %{buildroot}
find . -name ".codecov.yml" -prune -execdir rm -rf {} \;
find . -name ".git*" -prune -execdir rm -rf {} \;
find . -name ".ci" -prune -execdir rm -rf {} \;
find . -name ".devcontainer" -prune -execdir rm -rf {} \;
find . -name ".travis.yml" -prune -execdir rm -rf {} \;
find . -empty -type d -prune -execdir rm -rf {} \;
find . -empty -type f -prune -execdir rm -rf {} \;
find . -name "*.orig" -prune -execdir rm -rf {} \;
popd

%if 0%{?compat_mode}
rm -rf %{buildroot}%{_docdir}/julia/

# The 'application' object must be only provided by one package
# Alternatively, we could rename the .appdata and .desktop file to have
# both applications show up in a valid way, but that would require the
# -compat appdata to be modified to make the difference clear
rm %{buildroot}%{_datadir}/appdata/julia.appdata.xml
%endif

%suse_update_desktop_file -r julia Science Math

mv %{buildroot}%{_bindir}/julia %{buildroot}%{_bindir}/julia-base
mkdir -p %{buildroot}%{_sysconfdir}/alternatives

if [ "x%{_lib}" != xlib ] ; then
    mkdir -p %{buildroot}%{_prefix}/lib
    ln -sf %{_libdir}/julia %{buildroot}%{_prefix}/lib/julia
fi

ln -sf %{_sysconfdir}/alternatives/julia %{buildroot}%{_bindir}/julia

# Convert all eol encodings to Unix
find %{buildroot} -type f -execdir dos2unix -k {} \;

# make it executable
chmod +x %{buildroot}%{_datadir}/julia/stdlib/v1.9/SparseArrays/gen/generator.jl

# Remove duplicated files.
%fdupes %{buildroot}%{_datadir}/julia

%post
%{_sbindir}/update-alternatives --install %{_bindir}/julia \
    julia %{_bindir}/julia-base 5
%{_sbindir}/ldconfig

%postun
if [ ! -f %{_bindir}/julia-base ] ; then
    %{_sbindir}/update-alternatives --remove julia %{_bindir}/julia-base
fi
%{_sbindir}/ldconfig

%post   devel -p %{_sbindir}/ldconfig
%postun devel -p %{_sbindir}/ldconfig
%post   -n %{libname} -p %{_sbindir}/ldconfig
%postun -n %{libname} -p %{_sbindir}/ldconfig

%files
%doc CONTRIBUTING.md NEWS.md README.md
%license LICENSE.md
%ghost %{_bindir}/julia
%ghost %{_sysconfdir}/alternatives/julia
%{_bindir}/julia-base
%dir %{_datadir}/julia
%{_datadir}/julia/base
%{_datadir}/julia/base.cache
%{_datadir}/julia/stdlib
%{_datadir}/julia/compiled*
%{_datadir}/julia/cert.pem
%dir %{_libexecdir}/julia
%{_libexecdir}/julia/*

%if !%{?compat_mode}
%dir %{_datadir}/appdata/
%{_datadir}/appdata/julia.appdata.xml
%dir %{_docdir}/julia
%{_docdir}/julia/*
%endif
%{_datadir}/applications/julia.desktop
%{_prefix}/lib/julia
%{_libdir}/julia/
%{_mandir}/man1/julia.1%{?ext_man}
%dir %{_sysconfdir}/julia/
%config(noreplace) %{_sysconfdir}/julia/startup.jl

%files devel
%{_datadir}/julia/test/
%{_datadir}/julia/julia-config.jl
%{_includedir}/julia/
%{_libdir}/libjulia.so

%files -n %{libname}
%{_libdir}/libjulia.so.*

%changelog
