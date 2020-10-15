#
# spec file for package julia
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


# We must not strip binaries in julia, since it can lead to many problems.
# For example, see:
#
# https://github.com/JuliaLang/julia/issues/17941
%undefine _build_create_debug
%define __arch_install_post export NO_BRP_STRIP_DEBUG=true

%define julia_ver            1.4.2
%define libjulia_sover_major 1
%define libjulia_sover_minor 4
%if "@BUILD_FLAVOR@%{nil}" == "compat"
%define compat_mode  1
%else
%define compat_mode  0
%endif
Version:        1.4.2
Release:        0
URL:            http://julialang.org/
Source0:        https://github.com/JuliaLang/julia/releases/download/v1.4.2/julia-%{julia_ver}-full.tar.gz
Source99:       juliabuildopts
# PATCH-FIX-OPENSUSE julia-env-script-interpreter.patch ronisbr@gmail.com -- Change script interpreted to avoid errors in rpmlint.
Patch0:         julia-env-script-interpreter.patch
# PATCH-FIX-UPSTREAM llvm-8.0.1-gcc-10.patch ronisbr@gmail.com -- Fix LLVM 8.0.1 build using GCC 10 - https://reviews.llvm.org/D64937.
Patch1:         llvm-8.0.1-gcc-10.patch
# PATCH-FIX-UPSTREAM - https://github.com/JuliaLang/julia/commit/15dee645cdddda022de8960c91141109c41a66b4
Patch2:         julia-fix-aarch64.patch
BuildRequires:  arpack-ng-devel >= 3.3.0
BuildRequires:  blas-devel
BuildRequires:  cmake
BuildRequires:  double-conversion-devel
BuildRequires:  fdupes
BuildRequires:  fftw3-threads-devel >= 3.3.4
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
BuildRequires:  gmp-devel >= 6.1.2
BuildRequires:  hicolor-icon-theme
BuildRequires:  lapack-devel >= 3.5.0
BuildRequires:  libcurl-devel
BuildRequires:  libopenblas_openmp-devel >= 0.3.5
BuildRequires:  libssh2-devel >= 1.9.0
BuildRequires:  libunwind-devel >= 1.3.1
BuildRequires:  m4
BuildRequires:  mbedtls-devel >= 2.16.0
BuildRequires:  mpfr-devel >= 4.0.2
BuildRequires:  ncurses-devel
BuildRequires:  openspecfun-devel
BuildRequires:  openssl
BuildRequires:  patchelf >= 0.9
BuildRequires:  pcre2-devel >= 10.31
BuildRequires:  perl
BuildRequires:  python >= 2.5
BuildRequires:  readline-devel
BuildRequires:  suitesparse-devel >= 5.4.0
BuildRequires:  update-desktop-files
BuildRequires:  zlib-devel >= 1.2.11
Requires:       libamd2
Requires:       libarpack2
Requires:       libcamd2
Requires:       libccolamd2
Requires:       libcholmod3
Requires:       libcolamd2
Requires:       libfftw3_threads3
Requires:       libgmp10
Requires:       libmpfr6
Requires:       libopenblas_openmp0 >= 0.3.5
Requires:       libpcre2-8-0
Requires:       libspqr2
Requires:       libsuitesparseconfig5
Requires:       libumfpack5
Requires:       ncurses
Requires:       p7zip >= 16
Requires:       readline
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
License:        MIT AND GPL-2.0-or-later AND BSD-3-Clause AND Zlib
Group:          Development/Languages/Other
%else
Summary:        High-level, high-performance dynamic programming language (without CPU optim.)
License:        MIT AND GPL-2.0-or-later AND BSD-3-Clause AND Zlib
Group:          Development/Languages/Other
%endif
%if 0%{?compat_mode}
Conflicts:      julia
Provides:       julia = %{version}
%endif
# Since the 32-bit julia package is already being built using MARCH=pentium4,
# which is the most generic flag supported, then the julia-compat mode only
# makes sense for 64-bit architectures.
%if 0%{?compat_mode}
ExclusiveArch:  x86_64
%else
ExclusiveArch:  %{ix86} x86_64 %{arm} aarch64 ppc64le
%endif

%description
Julia is a high-level, high-performance dynamic programming language for
technical computing, with syntax that is familiar to users of other technical
computing environments. It provides a sophisticated compiler, distributed
parallel execution, numerical accuracy, and an extensive mathematical function
library. The library, largely written in Julia itself, also integrates mature,
best-of-breed C and Fortran libraries for linear algebra, random number
generation, signal processing, and string processing.

%package        devel
Summary:        Julia development, debugging and testing files
Group:          Development/Languages/Other
Requires:       %{name} = %{version}
%if 0%{?compat_mode}
Conflicts:      julia-devel
%endif

%description    devel
Contains library symbolic links and header files for developing applications
linking to the Julia library, in particular embedding it, as well as tests and a
debugging version of Julia. This package is normally not needed when programming
in the Julia language, but rather for embedding Julia into external programs or
debugging Julia itself.

%package        debug
Summary:        Julia debugging
Group:          Development/Languages/Other
Requires:       %{name} = %{version}
%if 0%{?compat_mode}
Conflicts:      julia-debug
%endif

%description    debug
Contains a debugging version of Julia system image and Julia library.

%if 0%{?compat_mode} == 0
%package        doc
Summary:        Julia documentation and code examples
Group:          Documentation/Other
BuildArch:      noarch

%description    doc
Contains the Julia manual, the reference documentation of the standard library.

%endif

%{expand:%global juliabuildopts %(cat %{SOURCE99})}

%prep
%setup -q -n julia-%{version}
%patch0 -p1
%patch2 -p1

# Extract LLVM sources to apply the patch.
make CFLAGS="%optflags" CXXFLAGS="%optflags" %{juliabuildopts} -C deps extract-llvm
pushd deps/srccache/llvm-8.0.1
    patch -p2 < %PATCH1
popd

# remove .gitignore
find . -name ".git*" -exec rm {} \;

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

%define julia_builddir %{_builddir}/%{name}/
make %{?_smp_mflags} \
                     MARCH=%{julia_march} \
%ifarch aarch64
                     JULIA_CPU_TARGET="generic" \
%endif
                     prefix=%{_prefix} \
                     bindir=%{_bindir} \
                     libdir=%{_libdir} \
                     libexecdir=%{_libexecdir} \
                     datarootdir=%{_datarootdir} \
                     includedir=%{_includedir} \
                     sysconfdir=%{_sysconfdir} \
                     %{juliabuildopts} \
                     release debug

%check
# The tests will only pass if openblas is being used.
# make %{?_smp_mflags} test

%install
make install DESTDIR=%{buildroot} \
             MARCH=%{julia_march} \
%ifarch aarch64
             JULIA_CPU_TARGET="generic" \
%endif
             prefix=%{_prefix} \
             bindir=%{_bindir} \
             libdir=%{_libdir} \
             libexecdir=%{_libexecdir} \
             datarootdir=%{_datarootdir} \
             includedir=%{_includedir} \
             sysconfdir=%{_sysconfdir} \
             %{juliabuildopts}

# GZip man page.
gzip %{buildroot}/%{_mandir}/man1/julia.1

# Copy the man page for every executable.
cd %{buildroot}/%{_mandir}/man1/
ln -sf julia.1.gz julia-debug.1.gz

rm -f %{buildroot}%{_libdir}/julia/libuv.a
rm -f %{buildroot}%{_datadir}/julia/base/build.h
rm -f %{buildroot}%{_datadir}/julia/base/Makefile

# Fix documentation directories.
mkdir -p %{buildroot}%{_docdir}/julia
mv -f %{buildroot}%{_datadir}/doc/julia/* %{buildroot}%{_docdir}/julia/
rm -r %{buildroot}%{_datadir}/doc/julia

# Remove execution permission on documentation files.
chmod -x+X -R %{buildroot}%{_docdir}/julia/*

%if 0%{?compat_mode}
rm -rf %{buildroot}%{_docdir}/julia/

# The 'application' object must be only provided by one package
# Alternatively, we could rename the .appdata and .desktop file to have
# both applications show up in a valid way, but that would require the
# -compat appdata to be modified to make the difference clear
rm %{buildroot}%{_datadir}/appdata/julia.appdata.xml
%endif

# Remove duplicated files.
%fdupes %{buildroot}%{_datadir}/

%suse_update_desktop_file -r julia Science Math

%post         -p /sbin/ldconfig
%postun       -p /sbin/ldconfig
%post   devel -p /sbin/ldconfig
%postun devel -p /sbin/ldconfig
%post   debug -p /sbin/ldconfig
%postun debug -p /sbin/ldconfig

%files
%doc CONTRIBUTING.md NEWS.md README.md
%license LICENSE.md
%{_bindir}/julia
%dir %{_datadir}/julia
%{_datadir}/julia/base
%{_datadir}/julia/base.cache
%{_datadir}/julia/stdlib
%{_datadir}/julia/cert.pem
%if !%{?compat_mode}
%dir %{_datadir}/appdata/
%{_datadir}/appdata/julia.appdata.xml
%endif
%{_datadir}/applications/julia.desktop
%{_datadir}/icons/hicolor/scalable/apps/julia.svg
%{_libdir}/julia/
%{_libdir}/libjulia.so.%{libjulia_sover_major}.%{libjulia_sover_minor}
%{_mandir}/man1/julia.1%{?ext_man}
%dir %{_sysconfdir}/julia/
%config(noreplace) %{_sysconfdir}/julia/startup.jl
# Exclude debugging files.
%exclude %{_libdir}/julia/libccalltest.so.debug
%exclude %{_libdir}/julia/sys-debug.so
# Exclude documentation.
%exclude %{_docdir}/julia/html

%files devel
%{_datadir}/julia/test/
%{_datadir}/julia/julia-config.jl
%{_includedir}/julia/
%{_libdir}/libjulia.so.%{libjulia_sover_major}
%{_libdir}/libjulia.so

%files debug
%{_bindir}/julia-debug
%{_libdir}/libjulia-debug.so.%{libjulia_sover_major}.%{libjulia_sover_minor}
%{_libdir}/libjulia-debug.so.%{libjulia_sover_major}
%{_libdir}/libjulia-debug.so
%{_libdir}/julia/libccalltest.so.debug
%{_libdir}/julia/sys-debug.so
%{_mandir}/man1/julia-debug.1%{?ext_man}

%if 0%{?compat_mode} == 0
%files doc
%{_docdir}/julia
%exclude %{_docdir}/julia/CONTRIBUTING.md
%exclude %{_docdir}/julia/NEWS.md
%exclude %{_docdir}/julia/README.md
%endif

%changelog
