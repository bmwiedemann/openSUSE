#
# spec file for package meep
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


%define somajor 30
Name:           meep
Version:        1.25.0
Release:        0
Summary:        FDTD finite-difference time-domain solver
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Electronics
URL:            https://meep.readthedocs.io/en/latest/
Source0:        https://github.com/NanoComp/meep/releases/download/v%{version}/meep-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  binutils
BuildRequires:  blas-devel
BuildRequires:  fftw3-devel
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
BuildRequires:  gmp-devel
BuildRequires:  gsl-devel
BuildRequires:  guile-devel
BuildRequires:  harminv-devel
BuildRequires:  hdf5-devel
BuildRequires:  lapack-devel
BuildRequires:  libctl-devel >= 4.2.0
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  zlib-devel

# providing ice-9/boot-9.scm
Requires:       guile

# providing /usr/share/libctl/base/include.scm
Requires:       libctl-devel >= 4.2.0

%description
Meep (or MEEP) is a free finite-difference time-domain (FDTD)
simulation software package developed at MIT to model electromagnetic
systems.

%package -n     lib%{name}%{somajor}
Summary:        FDTD finite-difference time-domain solver library
# Avoid unresolvable errors from multiple providers
Group:          System/Libraries

%description -n lib%{name}%{somajor}
Meep (or MEEP) is a free finite-difference time-domain (FDTD)
simulation software package developed at MIT to model electromagnetic
systems.

%package        devel
Summary:        Libraries and header files for meep library
Group:          Development/Libraries/Other
Requires:       lib%{name}%{somajor} = %{version}

%description    devel
Meep (or MEEP) is a free finite-difference time-domain (FDTD)
simulation software package developed at MIT to model electromagnetic
systems.

This package contains libraries and header files for developing
applications that use meep.

%prep
%setup -q
# Checking for CPU architecture is totally broken, get rid of it
sed -i -e 's/AX_CXX_MAXOPT//' configure.ac

%build
# Missing version.sh from tarball, required for autoreconf
echo "echo -n '%{version}'" > ./version.sh ; chmod +x ./version.sh
autoreconf
# On i586, we need SSE (implicit on x86_64). Yes, we need a Pentium3 at least ...
%ifarch %{ix86}
%global optflags %{optflags} -msse -Wno-error=return-type
%else
%global optflags %{optflags} -Wno-error=return-type
%endif
# Specify fortran libraries manually, autoconf (fortran.m4) mechanism is
# totally broken and messes up pkgconfig file later
%configure \
  FLIBS="-lgfortran" \
  --enable-shared \
  --disable-static \
  --with-openmp \
  --enable-portable-binary
%make_build
# Build tests without running any
%make_build check TESTS=

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%check
grep -E "flags|model name"  /proc/cpuinfo | head -n2
# https://github.com/NanoComp/meep/issues/727
make check TESTS=2D_convergence || export xfail=2D_convergence
%make_build check XFAIL_TESTS=${xfail}
cat tests/test-suite.log

%post -n lib%{name}%{somajor} -p /sbin/ldconfig

%postun -n lib%{name}%{somajor} -p /sbin/ldconfig

%files
%doc AUTHORS NEWS.md
%license COPYRIGHT
%{_bindir}/meep
%{_datadir}/meep/

%files -n lib%{name}%{somajor}
%{_libdir}/libmeep.so.*

%files devel
%{_libdir}/libmeep.so
%{_libdir}/pkgconfig/*
%{_includedir}/*

%changelog
