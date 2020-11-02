#
# spec file for package abseil-cpp
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


%define src_install_dir %{_prefix}/src/%{name}
Name:           abseil-cpp
Version:        20200225.2
Release:        0
Summary:        C++11 libraries which augment the C++ stdlib
License:        Apache-2.0
URL:            https://abseil.io/
Source0:        https://github.com/abseil/abseil-cpp/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}-rpmlintrc
BuildRequires:  c++_compiler
BuildRequires:  cmake
BuildRequires:  fdupes

%description
Abseil is a collection of C++11 libraries which augment the C++
standard library. It also provides features incorporated into C++14
and C++17 standards.

%package devel
Summary:        Header files for Abseil
Requires:       %{name} = %{version}

%description devel
Abseil is a collection of C++11 libraries which augment the C++
standard library.
This package contains headers and build system files for it.

%package source
Summary:        Source code of Abseil

%description source
Source code of Abseil, a collection of C++11 libraries
which augment the C++ standard library. It also provides
features incorporated into C++14 and C++17 standards.

%prep
%autosetup -p1

%build
# let rpm/OBS have some versioning to work with when it comes to upgrades and rebuilds
cat >"%_builddir/abslx.sym" <<-EOF
	ABSL_%version { global: *; };
EOF
%define build_ldflags -Wl,--version-script=%_builddir/abslx.sym
%cmake -DBUILD_SHARED_LIBS:BOOL=ON

%install
%cmake_install
mkdir -p %{buildroot}%{src_install_dir}
cp -r * %{buildroot}%{src_install_dir}
%fdupes %{buildroot}/%{_prefix}

%files
%{_libdir}/libabsl_*.so

%files devel
%{_includedir}/absl/
%{_libdir}/cmake/

%files source
%license LICENSE
%doc README.md
%{src_install_dir}

%changelog
