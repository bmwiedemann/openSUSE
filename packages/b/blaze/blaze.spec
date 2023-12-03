#
# spec file for package blaze
#
# Copyright (c) 2023 SUSE LLC
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


Name:           blaze
Version:        3.8.2
Release:        0
Summary:        A high performance C++ math library
License:        BSD-3-Clause
URL:            https://bitbucket.org/blaze-lib/blaze
Source:         %{url}/downloads/%{name}-%{version}.tar.gz
BuildRequires:  blas-devel
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  lapack-devel

%description
Blaze is an open-source, high-performance C++ math library for dense and sparse
arithmetic.

%package devel
Summary:        Headers and cmake files for blaze - a c++ math library
BuildArch:      noarch

%description devel
Blaze is an open-source, high-performance C++ math library for dense and sparse
arithmetic.

This package provides the headers and cmake files needed to build applications
against blaze.

%package devel-doc
Summary:        API documentation for blaze - a c++ math library
BuildArch:      noarch

%description devel-doc
This package provides the API documentation for blaze in HTML format.

%prep
%autosetup

%build
%cmake -DBLAZE_BLAS_MODE:BOOL=ON
%cmake_build
doxygen ../Doxyfile

%install
%cmake_install

%check
sh ./blazetest/run

%files devel
%license LICENSE
%{_includedir}/%{name}/
%{_datadir}/%{name}/

%files devel-doc
%license LICENSE
%doc doc

%changelog
