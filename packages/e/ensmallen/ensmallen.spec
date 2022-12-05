#
# spec file for package ensmallen
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2020 Markus Kolb <novell+ensmallen@tower-net.de>
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


Name:           ensmallen
Version:        2.19.0
Release:        0
Summary:        Math optimization C++ library
License:        BSD-3-Clause AND MPL-2.0 AND BSL-1.0
Group:          Development/Languages/C and C++
URL:            https://ensmallen.org
Source0:        https://ensmallen.org/files/ensmallen-%{version}.tar.gz
BuildRequires:  armadillo-devel >= 9.800.6
BuildRequires:  cmake >= 3.3.2
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  make
Recommends:     armadillo-devel >= 9.800.6

%description
ensmallen provides a set of abstractions for writing an objective
function to optimize. It also provides a set of standard and
optimizers that can be used for mathematical optimization tasks.
These include full-batch gradient descent techniques, small-batch
techniques, gradient-free optimizers, and constrained optimization.

%package devel
Summary:        Math optimization C++ library
Group:          Development/Languages/C and C++

%description devel
ensmallen provides a set of abstractions for writing an objective
function to optimize. It also provides a set of standard and
optimizers that can be used for mathematical optimization tasks.
These include full-batch gradient descent techniques, small-batch
techniques, gradient-free optimizers, and constrained optimization.

%prep
%autosetup -p1

%build
%cmake -DENSMALLEN_CMAKE_DIR=%{_libdir}/cmake/ensmallen/
# Build the tests
%cmake_build

%install
%cmake_install
%fdupes %{buildroot}/%{_prefix}

%files devel
%license COPYRIGHT.txt
%license LICENSE.txt
%{_includedir}/ensmallen.hpp
%{_includedir}/ensmallen_bits
%{_libdir}/cmake/ensmallen/

%changelog
