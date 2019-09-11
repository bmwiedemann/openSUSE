#
# spec file for package meep
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define somajor 14
Name:           meep
Version:        1.9.0
Release:        0
Summary:        FDTD finite-difference time-domain solver
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Electronics
Url:            http://ab-initio.mit.edu/wiki/index.php/Meep
Source0:        https://github.com/stevengj/meep/releases/download/v%{version}/meep-%{version}.tar.gz
# PATCH-FIX-OPENSUSE disable_test_tumbleweed.patch boo#1130438 -- Disable
# failing test on Tumbleweed
Patch0:         disable_test_tumbleweed.patch
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
BuildRequires:  latex2html
BuildRequires:  libctl-devel >= 4.2.0
BuildRequires:  pkgconfig
BuildRequires:  zlib-devel

# providing ice-9/boot-9.scm
Requires:       guile

# providing /usr/share/libctl/base/include.scm
Requires:       libctl-devel >= 4.2.0

BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Meep (or MEEP) is a free finite-difference time-domain (FDTD)
simulation software package developed at MIT to model electromagnetic
systems.

%package -n     lib%{name}%{somajor}
Summary:        FDTD finite-difference time-domain solver library
# Avoid unresolvable errors from multiple providers
Group:          System/Libraries
Requires:       libhdf5

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
%if 0%{?suse_version} >= 1550
%patch0 -p1
%endif

%build
export CFLAGS="%{optflags} -fPIC"
export CXXFLAGS="%{optflags} -fPIC"
export FFLAGS="%{optflags} -fPIC"
%configure --enable-shared --disable-static --enable-portable-binary
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%check
make check

%post -n lib%{name}%{somajor} -p /sbin/ldconfig

%postun -n lib%{name}%{somajor} -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc AUTHORS COPYRIGHT NEWS.md
%{_bindir}/*
%{_datadir}/meep/

%files -n lib%{name}%{somajor}
%defattr(-,root,root)
%{_libdir}/libmeep.so.*

%files devel
%defattr(-,root,root)
%{_libdir}/libmeep.so
%{_libdir}/pkgconfig/*
%{_includedir}/*

%changelog
