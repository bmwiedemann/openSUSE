#
# spec file for package range-v3
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


%define __builder ninja
Name:           range-v3
Version:        0.12.0
Release:        0
Summary:        Range library for C++14/17/20, basis for C++20's std::ranges
License:        BSL-1.0
URL:            https://github.com/ericniebler/range-v3
Source:         %{url}/archive/%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja

%description
Range library for C++14/17/20. This code was the basis of a formal proposal to add range support to the C++ standard library.
That proposal evolved through a Technical Specification, and finally into P0896R4 "The One Ranges Proposal"
which was merged into the C++20 working drafts in November 2018.

%package devel
Summary:        Development files for %{name}
Provides:       %{name}-static = %{version}

%description devel
%{summary}.

%prep
%autosetup -p1

%build
%cmake \
  -DCMAKE_BUILD_TYPE=Release \
  -DRANGE_V3_TESTS=OFF \
  -DRANGE_V3_DOCS=OFF \
  -DRANGE_V3_EXAMPLES=OFF \
  -DRANGES_MODULES=OFF

%cmake_build

%install
%cmake_install
rm -f %{buildroot}%{_includedir}/module.modulemap

%files devel
%doc README.md CREDITS.md TODO.md
%license LICENSE.txt
%{_includedir}/{meta,range,concepts,std}
%{_libdir}/cmake/%{name}

%changelog
