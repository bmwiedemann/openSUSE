#
# spec file for package ms-gsl
#
# Copyright (c) 2025 SUSE LLC
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


Name:           ms-gsl
Version:        4.2.1
Release:        0
Summary:        Guidelines Support Library
License:        MIT
URL:            https://github.com/Microsoft/GSL
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source100:      README.md
BuildRequires:  git-core
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(gtest)
BuildArch:      noarch

%description
The Guidelines Support Library (GSL) contains functions and types
that are suggested for use by the C++ Core Guidelines maintained by
the Standard C++ Foundation. This repo contains Microsoft's
implementation of GSL. The entire implementation is provided inline
in the headers under the gsl directory. The implementation generally
assumes a platform that implements C++14 support. While some types
have been broken out into their own headers (e.g. gsl/span), it is
simplest to just include gsl/gsl and gain access to the entire
library.

%package devel
Summary:        Development files for %{name}

%description devel
%{summary}.

%prep
%autosetup -n GSL-%{version}

%build
%cmake \
  -DGSL_TEST=ON \
  -DCMAKE_BUILD_TYPE=Release \
  -DGSL_CXX_STANDARD=17
%cmake_build

%install
%cmake_install

%check
%ctest

%files devel
%license LICENSE
%doc README.md ThirdPartyNotices.txt CONTRIBUTING.md
%{_datadir}/cmake/Microsoft.GSL/
%{_includedir}/gsl/

%changelog

