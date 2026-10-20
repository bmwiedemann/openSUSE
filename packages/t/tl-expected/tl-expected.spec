#
# spec file for package tl-expected
#
# Copyright (c) 2026 SUSE LLC
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


Name:           tl-expected
Version:        1.3.1
Release:        0
Summary:        C++11/14/17 std::expected with functional-style extensions
License:        CC0-1.0
URL:            https://github.com/TartanLlama/expected
Source0:        https://github.com/TartanLlama/expected/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  cmake >= 3.14
BuildRequires:  gcc-c++
BuildArch:      noarch

%description
std::expected is proposed as the preferred way to represent objects
which will either have an expected value, or an unexpected value
giving information about why something failed. Unfortunately,
chaining together many computations which may fail can be verbose,
as error-checking code will be mixed in with the actual programming
logic. This implementation provides a number of utilities to make
coding with expected cleaner.

%package devel
Summary:        Development files for %{name}
Provides:       %{name} = %{version}

%description devel
Header-only C++11/14/17 std::expected with functional-style extensions.

%prep
%autosetup -p1 -n expected-%{version}

%build
%cmake \
    -DEXPECTED_BUILD_PACKAGE=OFF \
    -DEXPECTED_BUILD_TESTS=OFF
%cmake_build

%install
%cmake_install

%files devel
%license COPYING
%doc README.md
%{_includedir}/tl
%{_datadir}/cmake/tl-expected

%changelog
