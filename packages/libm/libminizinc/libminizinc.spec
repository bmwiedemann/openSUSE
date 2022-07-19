#
# spec file for package libminizinc
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


Name:           libminizinc
Version:        2.6.4
Release:        0
Summary:        A high-level constraint modelling language
Group:          Productivity/Scientific/Math
License:        MPL-2.0
URL:            https://www.minizinc.org/
Source:         https://github.com/MiniZinc/libminizinc/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake >= 3.4.0
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(mpfr)
BuildRequires:  gecode-devel

%description
MiniZinc is a free and open-source constraint modeling language.

%package -n minizinc
Summary:        A high-level constraint modelling language
Recommends:     gecode-minizinc

%description -n minizinc
You can use MiniZinc to model constraint satisfaction and optimisation
problems in a high-level, solver-independent way, taking advantage of
a large library of pre-defined constraints. Your model is then
compiled into FlatZinc, a solver input language that is understood
by a wide range of solvers.

%package devel
Summary:        A high-level constraint modelling language
Group:          Development/Libraries/C and C++
Requires:       minizinc = %{version}

%description devel
MiniZinc is a free and open-source constraint modeling language.

%prep
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%post -n minizinc -p /sbin/ldconfig
%postun -n minizinc -p /sbin/ldconfig

%files -n minizinc
%license LICENSE.txt
%doc changes.rst README.md
%{_bindir}/*
%{_datadir}/minizinc
%{_libdir}/libmzn*

%files devel
%{_includedir}/minizinc
%{_libdir}/cmake/libminizinc

%changelog
