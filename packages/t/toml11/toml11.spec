#
# spec file for package toml11
#
# Copyright (c) 2023 Neal Gompa
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


# Disable debuginfo package, since it's useless and can cause local build failures
%global debug_package %{nil}

# Common description
%global _description %{expand:
toml11 is a C++ header-only toml parser/encoder depending only on
C++ standard library.

  * It is compatible to the latest version of TOML v1.0.0.
  * It is one of the most TOML standard compliant libraries, tested with the
    language agnostic test suite for TOML parsers by BurntSushi.
  * It shows highly informative error messages.
  * It has configurable container. You can use any random-access containers
    and key-value maps as backend containers.
  * It optionally preserves comments without any overhead.
  * It has configurable serializer that supports comments, inline tables,
    literal strings and multiline strings.
  * It supports user-defined type conversion from/into toml values.
  * It correctly handles UTF-8 sequences, with or without BOM.}


Name:           toml11
Version:        3.7.1
Release:        0
Summary:        TOML for Modern C++

License:        MIT
URL:            https://github.com/ToruNiina/toml11
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  make

%description %{_description}

%package devel
Summary:        Development files for %{name}

%description devel %{_description}

Development files for %{name}.


%prep
%autosetup -p1


%build
%cmake
%cmake_build


%install
%cmake_install


%files devel
%license LICENSE
%doc README.md
%{_includedir}/*.hpp
%{_includedir}/toml/
%{_libdir}/cmake/%{name}/


%changelog
