#
# spec file for package libheinz
#
# Copyright (c) 2025 Andreas Stieger <Andreas.Stieger@gmx.de>
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


Name:           libheinz
Version:        3.0.0
Release:        0
Summary:        C++ base library of Heinz Maier-Leibnitz Zentrum
License:        BSD-3-Clause
URL:            https://jugit.fz-juelich.de/mlz/libheinz
Source:         https://jugit.fz-juelich.de/mlz/libheinz/-/archive/v%{version}/%{name}-v%{version}.tar.gz
BuildRequires:  c++_compiler
BuildRequires:  cmake
BuildArch:      noarch
%if 0%{?suse_version} < 1600
BuildRequires:  gcc12-c++
%endif

%description
Header-only C++ base library of Heinz Maier-Leibnitz Zentrum.

%package devel
Summary:        C++ base library of Heinz Maier-Leibnitz Zentrum

%description devel
Header-only C++ base library of Heinz Maier-Leibnitz Zentrum.

%prep
%autosetup -p1 -n %{name}-v%{version}

%build
%if 0%{?suse_version} < 1600
export CXX=g++-12
%endif
%cmake
%cmake_build

%install
%cmake_install

%files devel
%license LICENSE
%doc CHANGELOG README.md
%{_includedir}/heinz
%dir %{_prefix}/lib/cmake
%{_prefix}/lib/cmake/LibHeinz

%changelog
