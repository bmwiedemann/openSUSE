#
# spec file for package libminizinc
#
# Copyright (c) 2025 SUSE LLC
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
Version:        2.8.7
Release:        0
Summary:        A high-level constraint modelling language
Group:          Productivity/Scientific/Math
License:        MPL-2.0
URL:            https://www.minizinc.org/
Source:         https://github.com/MiniZinc/libminizinc/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FEATURE-OPENSUSE - Be more verbose on thrown exceptions
Patch0:         0001-Disambiguate-UNKNOWN-EXCEPTION.patch
Patch1:         0002-Catch-std-exception-by-const-reference.patch
Patch2:         0003-Try-to-get-some-more-information-when-catching.patch
BuildRequires:  cmake >= 3.4.0
BuildRequires:  gcc-c++
BuildRequires:  gecode-devel
BuildRequires:  gecode-minizinc
BuildRequires:  pkgconfig(mpfr)

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

%check
cat > t.mzn <<EOF
var 1..5: x;
EOF
cat > t1.mzc.mzn <<EOF
output["SIMPLE CHECK"];
EOF
cat > t2.mzc.mzn <<EOF
int: data :: add_to_output = 2;
EOF
export LD_LIBRARY_PATH=./build/
./build/minizinc --solvers
./build/minizinc t1.mzc.mzn t.mzn --output-mode json --output-time --output-objective --output-output-item --statistics
./build/minizinc t2.mzc.mzn t.mzn --output-mode json --output-time --output-objective --output-output-item --statistics

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
