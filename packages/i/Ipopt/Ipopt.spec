#
# spec file for package Ipopt
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


%define shlib libipopt0
Name:           Ipopt
Version:        3.13.3
Release:        0
Summary:        A software package for large-scale nonlinear optimization methods
License:        EPL-2.0
Group:          Development/Libraries/C and C++
URL:            https://projects.coin-or.org/Ipopt
Source0:        https://github.com/coin-or/Ipopt/archive/releases/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  blas-devel
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
BuildRequires:  graphviz
BuildRequires:  graphviz-gd
BuildRequires:  java-devel
BuildRequires:  javapackages-tools
BuildRequires:  lapack-devel
BuildRequires:  metis-devel
BuildRequires:  mumps-devel
BuildRequires:  pkgconfig
BuildRequires:  strip-nondeterminism
BuildRequires:  texlive-bibtex-bin
BuildRequires:  texlive-dvips-bin
BuildRequires:  texlive-latex-bin

%description
Ipopt (Interior Point OPTimizer, pronounced eye-pea-Opt) is a software
package for large-scale nonlinear optimization.

%package -n %{shlib}
Summary:        A software package for large-scale nonlinear optimization methods
Group:          System/Libraries

%description -n %{shlib}
Ipopt (Interior Point OPTimizer, pronounced eye-pea-Opt) is a software
package for large-scale nonlinear optimization.

%package devel
Summary:        Development and header files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{shlib} = %{version}
Requires:       mumps-devel
Provides:       ipopt-devel = %{version}

%description devel
This package contains the development and header files for %{name}.

%package java
Summary:        Java bindings for %{name}
Group:          Development/Libraries/C and C++

%description java
This package provides the java bindings for %{name} in a jar file.

%prep
%setup -q -n %{name}-releases-%{version}

%build
%configure --docdir=%{_docdir}/%{name} \
           --with-mumps-cflags="-I%{_includedir}/mumps" \
           --with-mumps-lflags="-L%{_libdir} -ldmumps_seq"

%make_build all
# create docs in a separate step for reproducible build results (boo#1102408)
%make_build doc

%install
%make_install
strip-nondeterminism %{buildroot}%{_javadir}/org.coinor.ipopt.jar

# REMOVE FILES TO BE PACKAGED USING %%doc
for f in AUTHORS README.md LICENSE;
do
  rm %{buildroot}%{_docdir}/%{name}/${f}
done

find %{buildroot} -type f -name "*.la" -delete -print

%fdupes %{buildroot}%{_datadir}/coin/doc

%check
%make_build test

%post -n %{shlib} -p /sbin/ldconfig
%postun -n %{shlib} -p /sbin/ldconfig

%files -n %{shlib}
%{_libdir}/*.so.*

%files devel
%doc README.md AUTHORS
%doc doc/html
%license LICENSE
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/ipopt.pc

%files java
%license LICENSE
%{_javadir}/org.coinor.ipopt.jar

%changelog
