#
# spec file for package harminv
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           harminv
Version:        1.4.1
Release:        0
%define somajor 3
Summary:        Solver for the problem of harmonic inversion
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Electronics
Url:            https://github.com/stevengj/harminv
Source0:        https://github.com/stevengj/harminv/releases/download/v%{version}/harminv-%{version}.tar.gz
BuildRequires:  blas-devel
BuildRequires:  gcc-fortran
BuildRequires:  lapack-devel
BuildRequires:  pkgconfig
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%define FORTRAN_COMPILER gfortran

%description
Harminv is a program to solve the problem of harmonic inversion — given
a discrete-time, finite-length signal that consists of a sum of
finitely-many sinusoids (possibly exponentially decaying) in a given
bandwidth, it determines the frequencies, decay constants, amplitudes,
and phases of those sinusoids.

%package -n     libharminv%{somajor}
Summary:        Library for solving the problem of harmonic inversion
Group:          System/Libraries

%description -n libharminv%{somajor}
Harminv is library to solve the problem of harmonic inversion — given
a discrete-time, finite-length signal that consists of a sum of
finitely-many sinusoids (possibly exponentially decaying) in a given
bandwidth, it determines the frequencies, decay constants, amplitudes,
and phases of those sinusoids.

%package        devel
Summary:        Libraries and header files for the harminv library
Group:          Development/Libraries/C and C++
Requires:       libharminv%{somajor} = %{version}

%description    devel
Harminv is library to solve the problem of harmonic inversion — given
a discrete-time, finite-length signal that consists of a sum of
finitely-many sinusoids (possibly exponentially decaying) in a given
bandwidth, it determines the frequencies, decay constants, amplitudes,
and phases of those sinusoids.

This package contains libraries and header files for developing
applications that use harminv.

%prep
%setup -q

sed -i 's/@LIBS@//g' harminv.pc.in

%build
export CFLAGS="%{optflags} -fPIC"
export CXXFLAGS="%{optflags} -fPIC"
export FFLAGS="%{optflags} -fPIC"
%configure --enable-shared --disable-static
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n libharminv%{somajor} -p /sbin/ldconfig

%postun -n libharminv%{somajor} -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc COPYING NEWS.md README.md
%{_bindir}/*
%{_mandir}/man1/*

%files -n libharminv%{somajor}
%defattr(-,root,root)
%{_libdir}/libharminv.so.*

%files devel
%defattr(-,root,root)
%{_libdir}/libharminv.so
%{_libdir}/pkgconfig/*
%{_includedir}/*

%changelog
