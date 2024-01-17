#
# spec file for package arprec
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define libname libarprec0

Name:           arprec
Version:        2.2.17
Release:        0
Summary:        ARbitrary PRECision Computation Package
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
Url:            http://crd-legacy.lbl.gov/~dhbailey/mpdist/
Source0:        http://crd.lbl.gov/~dhbailey/mpdist/arprec-%{version}.tar.gz
Source1:        http://crd.lbl.gov/~dhbailey/mpdist/BSD-LBNL-License.doc
# PATCH-FIX-UPSTREAM -- Fix build with GCC6
Patch1:         arprec-gcc6.patch
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
ARPREC is a software package for performing arbitrary precision
arithmetic. It consists of a revision and extension of Bailey's
earlier MPFUN package, enhanced with special IEEE numerical
techniques.

This package supports a flexible, arbitrarily high level of numeric
precision -- the equivalent of hundreds or even thousands of decimal
digits (up to approximately ten million digits if needed). Special
routines are provided for extra-high precision (above 1000 digits).
The entire library is written in C++. High-precision real, integer
and complex datatypes are supported.

%package -n %libname
Summary:        A library for ARbitrary PRECision Computation
Group:          System/Libraries
# Earlier faulty name of libarprec0
Obsoletes:      libarpec0 < %version-%release
Provides:       libarpec0 = %version-%release

%description -n %libname
ARPREC is a software package for performing arbitrary precision
arithmetic. It consists of a revision and extension of Bailey's
earlier MPFUN package, enhanced with special IEEE numerical
techniques.

This package supports a flexible, arbitrarily high level of numeric
precision -- the equivalent of hundreds or even thousands of decimal
digits (up to approximately ten million digits if needed). Special
routines are provided for extra-high precision (above 1000 digits).
The entire library is written in C++. High-precision real, integer
and complex datatypes are supported.

%package        devel
Summary:        Development files for the ARbitrary PRECision Computation library
Group:          Development/Libraries/C and C++
Requires:       %libname = %{version}

%description    devel
ARPREC is a software package for performing arbitrary precision
arithmetic. It consists of a revision and extension of Bailey's
earlier MPFUN package, enhanced with special IEEE numerical
techniques.

The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q
%patch1 -p1

%build
cp %{SOURCE1} .
%configure --enable-shared --disable-static
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -name '*.la' -delete

rm -rf %{buildroot}%{_datadir}/doc/arprec

%post -n %libname -p /sbin/ldconfig

%postun -n %libname -p /sbin/ldconfig

%files -n %libname
%defattr(-,root,root,-)
%doc COPYING
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING BSD-LBNL-License.doc doc/arprec.pdf NEWS README
%{_bindir}/%{name}-config
%{_includedir}/*
%{_libdir}/*.so

%changelog
