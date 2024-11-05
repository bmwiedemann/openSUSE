#
# spec file for package svgpp
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


Name:           svgpp
Version:        1.3.1
Release:        0
Summary:        C++ SVG library 
Group:          Development/Library/C and C++
License:        BSL-1.0
URL:            https://svgpp.org/
Source:         https://github.com/svgpp/svgpp/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libboost_headers-devel
BuildRequires:  libboost_system-devel
BuildRequires:  libboost_timer-devel
BuildRequires:  memory-constraints

%description
SVG++ library can be thought of as a framework, containing parsers for
various SVG syntaxes, adapters that simplify handling of parsed data
and a lot of other utilities and helpers for the most common tasks.

%package devel
Summary:        C++ SVG header-only library 
Group:          Development/Library/C and C++
Requires:       libboost_headers-devel
BuildArch:      noarch

%description devel
SVG++ library can be thought of as a framework, containing parsers for
various SVG syntaxes, adapters that simplify handling of parsed data
and a lot of other utilities and helpers for the most common tasks.

%prep
%setup -q

%build
%limit_build -m 1800
# Build tests
cd src/test
%cmake
%cmake_build

%install
mkdir -p %{buildroot}/%{_includedir}
cp -R include/svgpp %{buildroot}/%{_includedir}
cp -R include/exboost %{buildroot}/%{_includedir}
find %{buildroot}/%{_includedir} -type f -exec chmod 0644 '{}' \;

%check
cd src/test/%{__builddir}
./ParserGTest

%files devel
%license LICENSE_1_0.txt
%{_includedir}/svgpp
%{_includedir}/exboost

%changelog

