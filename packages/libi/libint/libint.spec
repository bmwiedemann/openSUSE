#
# spec file for package libint
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

Name:           libint
Version:        2.7.2
Release:        0
%define         sover 2
Summary:        High-performance library for computing Gaussian integrals in quantum mechanics
License:        GPL-3.0-or-later AND LGPL-3.0-or-later
Group:          Productivity/Scientific/Chemistry
URL:            https://evaleev.github.io/libint/
Source0:        https://github.com/evaleev/libint/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  eigen3-devel
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
BuildRequires:  libboost_headers-devel
# Exclude 32-bits - https://github.com/evaleev/libint/issues/196
ExcludeArch:    %{ix86} %arm
# not enough memory for lto
%global _lto_cflags %nil

%description
LIBINT computes the Coulomb and exchange integrals, which in electronic
structure theory are called electron repulsion integrals (ERIs). This is by
far the most common type of integrals in molecular structure theory.

LIBINT uses recursive schemes that originate in seminal Obara-Saika method and
Head-Gordon and Pople’s variation thereof. The idea of LIBINT is to optimize
computer implementation of such methods by implementing an optimizing compiler
to generate automatically highly-specialized code that runs well on
super-scalar architectures.

%package -n libint2-%sover
Summary:        Main libint library v2
Group:          System/Libraries

%description -n libint2-%sover
LIBINT computes the Coulomb and exchange integrals, which in electronic
structure theory are called electron repulsion integrals (ERIs). This is by
far the most common type of integrals in molecular structure theory.

LIBINT uses recursive schemes that originate in seminal Obara-Saika method and
Head-Gordon and Pople’s variation thereof. The idea of LIBINT is to optimize
computer implementation of such methods by implementing an optimizing compiler
to generate automatically highly-specialized code that runs well on
super-scalar architectures.

This package contains the library of the libint package.

%package devel
Summary:        Development headers and libraries for libint
Group:          Development/Libraries/C and C++
Requires:       eigen3-devel
Requires:       libint2-%sover = %{version}

%description devel
LIBINT computes the Coulomb and exchange integrals, which in electronic
structure theory are called electron repulsion integrals (ERIs). This is by
far the most common type of integrals in molecular structure theory.

LIBINT uses recursive schemes that originate in seminal Obara-Saika method and
Head-Gordon and Pople’s variation thereof. The idea of LIBINT is to optimize
computer implementation of such methods by implementing an optimizing compiler
to generate automatically highly-specialized code that runs well on
super-scalar architectures.

This package contains development headers and libraries for libint.

%prep
%setup -q
./autogen.sh

%build
%{configure} --enable-shared --disable-static \
  --enable-eri=2 --enable-eri3=2 --enable-eri2=2 \
  --with-eri-max-am=7,5,4 --with-eri-opt-am=3 \
  --with-eri3-max-am=7 --with-eri2-max-am=7 \
  --with-g12-max-am=5 --with-g12-opt-am=3 \
  --with-g12dkh-max-am=5 --with-g12dkh-opt-am=3 \
  --disable-unrolling --enable-generic-code --enable-contracted-ints \
  --with-incdirs="-I%{_includedir}/eigen3" \
  --with-cxx-optflags="%optflags"
%make_build

%install
%make_install
find %{buildroot} -name *.la -delete
# Make sure libraries are executable (otherwise they are not stripped)
find %{buildroot} -name *.so.*.* -exec chmod 755 {} \;
# Get rid of the basis set files that ship with libint
find %{buildroot}%{_datadir}/libint -name \*.g94 -delete

%post -n libint2-%sover -p /sbin/ldconfig
%postun -n libint2-%sover -p /sbin/ldconfig

%files -n libint2-%sover
%doc README.md CHANGES
%license LICENSE COPYING COPYING.LESSER
%{_libdir}/libint2.so.%{sover}*

%files devel
%{_includedir}/libint2/
%{_includedir}/libint2.h
%{_includedir}/libint2.hpp
%{_libdir}/libint2.so
%{_libdir}/pkgconfig/libint2.pc

%changelog
