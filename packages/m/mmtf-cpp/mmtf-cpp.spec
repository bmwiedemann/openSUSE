 
#
# spec file for package mmtf-cpp
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

%define __builder ninja

Name:           mmtf-cpp
Version:        1.0.0
Release:        0
Summary:        The pure C++ implementation of the MMTF API, decoder and encoder
License:        MIT
Group:          Productivity/Scientific/Chemistry
URL:            https://github.com/rcsb/%{name}
Source0:        https://github.com/rcsb/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  ninja
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  msgpack-devel
BuildArch:      noarch


%description
Macromolecular transmission format documentation, including README, license and HTML docs.

%package  devel
Summary:   Development files of %{name}
Group:     Development/Libraries/C and C++
BuildArch: noarch

%description devel
This package contains libraries and header files for developing
applications that use %{name}.

%prep
%autosetup -n %{name}-%{version}

%build
%cmake -DBUILD_TESTS=OFF \
       -Dmmtf_build_local:BOOL=OFF \
       -Dmmtf_build_examples:BOOL=ON

%cmake_build

pushd ../docs
doxygen
popd

%install
%cmake_install

%fdupes -s %{buildroot}%{_prefix}

%files devel
%license LICENSE
%doc README.md
%doc docs/html
%{_includedir}/mmtf/
%{_includedir}/*.hpp

%changelog
