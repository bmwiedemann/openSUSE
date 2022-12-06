#
# spec file for package cli11
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


%define upstream_name CLI11

Name:           cli11
Version:        2.3.0
Release:        0
Summary:        Command line parser for C++11
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++

URL:            https://github.com/CLIUtils/CLI11
Source:         %{upstream_name}-%{version}.tar.gz
BuildRequires:  Catch2-2-devel
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  python3-devel
BuildArch:      noarch

%description
CLI11 is a command line parser for C++11 and beyond that provides a
rich feature set.

%package devel
Summary:        Development files for CLI11

%description devel
CLI11 is a command line parser for C++11 and beyond that provides a
rich feature set. It is header only, and has a number of design
limits by choice:

 * No completion of partial options (like --ve for --version,
   if it were unambiguous)
 * No wide strings/Unicode

%package      doc
Summary:        Documentation for CLI11
Group:          Documentation/Other

%description  doc
This package contains documentation for CLI11

CLI11 is a command line parser for C++11 and beyond that provides a
rich feature set. It is header only, and has a number of design
limits by choice:

 * No completion of partial options (like --ve for --version,
   if it were unambiguous)
 * No wide strings/Unicode

%prep
%autosetup -p1 -n %{upstream_name}-%{version}

%build
%cmake \
%if 0%{?sle_version} <= 150300 && 0%{?suse_version} <= 1500
  -DCLI11_BUILD_TESTS:BOOL=FALSE \
%else
  -DCLI11_BUILD_TESTS:BOOL=TRUE \
%endif
  -DCLI11_BUILD_DOCS:BOOL=TRUE \
  -DCLI11_BUILD_EXAMPLES:BOOL=FALSE
%cmake_build all docs

%install
%cmake_install

%if 0%{?sle_version} <= 150300 && 0%{?suse_version} <= 1500
%else

%check
%ctest
%endif

%files devel
%license LICENSE
%doc CHANGELOG.md
%dir %{_includedir}/CLI
%dir %{_includedir}/CLI/impl
%{_includedir}/CLI/*.hpp
%{_includedir}/CLI/impl/*.hpp
%dir %{_datadir}/cmake/CLI11/
%{_datadir}/cmake/CLI11/*.cmake
%{_datadir}/pkgconfig/CLI11.pc

%files doc
%doc build/docs/html/

%changelog
