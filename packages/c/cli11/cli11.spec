#
# spec file for package cli11
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


%define         git_ver .0.5cb3efabce00
Name:           cli11
Version:        1.9.1
Release:        0
Summary:        Command line parser for C++11
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++

URL:            https://github.com/CLIUtils/CLI11
Source:         %{name}-%{version}%{git_ver}.tar.gz
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  python3-devel


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

%prep
%autosetup -p1 -n %{name}-%{version}%{git_ver}

%build
%cmake -DCLI11_BUILD_TESTS:BOOL=FALSE -DCLI11_BUILD_DOCS:BOOL=TRUE
%cmake_build all docs

%install
%cmake_install

%files devel
%license LICENSE
%doc CHANGELOG.md
%dir %{_includedir}/CLI
%{_includedir}/CLI/*.hpp
%dir %{_libdir}/cmake/CLI11/
%{_libdir}/cmake/CLI11/*.cmake

%changelog
