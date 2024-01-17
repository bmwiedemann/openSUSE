#
# spec file for package mmtf-cpp
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


Name:           mmtf-cpp
Version:        1.1.0
Release:        0
Summary:        The pure C++ implementation of the MMTF API, decoder and encoder
License:        MIT
Group:          Productivity/Scientific/Chemistry
URL:            https://github.com/rcsb/mmtf-cpp
Source0:        %{name}-%{version}.tar
# PATCH-FIX-OPENSUSE fix_catch2_not_found.patch gh#rcsb/mmtf-cpp#39 andythe_great@pm.me -- Fix issue catch.hpp not found.
Patch0:         fix_catch2_not_found.patch
BuildRequires:  cmake >= 3.5
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  msgpack-cxx-devel
BuildRequires:  pkgconfig(catch2) < 3
BuildArch:      noarch

%description
Macromolecular transmission format documentation, including README, license and HTML docs.

%package  devel
Summary:        Development files of %{name}
Group:          Development/Libraries/C and C++
Requires:       msgpack-cxx-devel

%description devel
This package contains libraries and header files for developing
applications that use %{name}.

%prep
%autosetup -p1

%build
%cmake -DBUILD_TESTS:BOOL=ON \
       -Dmmtf_build_local:BOOL=ON

%cmake_build
cd ../docs
doxygen

%install
%cmake_install
# Install doc files manually so we can run fdupes on them
mkdir -p %{buildroot}%{_docdir}/%{name}
cp -pr ./docs/html %{buildroot}%{_docdir}/%{name}/
%fdupes %{buildroot}%{_docdir}/%{name}/html/

%check
%ctest

%files devel
%license LICENSE
%doc README.md
%doc %{_docdir}/%{name}/
%{_includedir}/mmtf/
%{_includedir}/*.hpp

%changelog
