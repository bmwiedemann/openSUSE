#
# spec file for package ctranslate2
#
# Copyright (c) 2024 SUSE LLC
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


Name:           ctranslate2
Version:        4.5.0
%define lname libctranslate2-4
Release:        0
Summary:        Library for efficient inference with Transformer models
License:        MIT
URL:            https://github.com/OpenNMT/CTranslate2
Source:         CTranslate2-%version.tar.xz
BuildRequires:  c++_compiler
BuildRequires:  cmake
BuildRequires:  openblas-devel
#BuildRequires:  libgmock-devel
BuildRequires:  nlohmann_json-devel
BuildRequires:  cpuinfo-devel
BuildRequires:  gmock
BuildRequires:  gtest
ExcludeArch:    %ix86 %arm

%description
CTranslate2 is a C++ and Python library for efficient inference with Transformer models.

NOTE: hardware accelaration is currently disabled in this package for license reasons

%package devel
Summary:        Development files for libctranslate2
Requires:       %lname

%description devel
Development files for libctranslate2 like cmake and header files.

%package -n %lname
Summary:        The ctranslate2 library

%description -n %lname
The ctranslate2 library

%prep
%autosetup -p1 -n CTranslate2-%version
rm -rf include/nlohmann/

%build
%cmake \
  -DBUILD_TESTS=ON \
  -DOPENBLAS_INCLUDE_DIR=/usr/include/openblas \
  -DOPENMP_RUNTIME=COMP \
  -DWITH_OPENBLAS=ON \
  -DWITH_MKL=OFF \
  -DWITH_RUY=ON

%cmake_build

%install
%cmake_install

%check
cd build
./tests/ctranslate2_test ../tests/data

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files
%license LICENSE
%doc CHANGELOG.md README.md
%doc docs examples
%_bindir/ct2-translator

%files devel
%_includedir/ctranslate2
%_includedir/half_float
%_libdir/cmake/ctranslate2
%_libdir/libctranslate2.so

%files -n %lname
%_libdir/libctranslate2.so.*

%changelog
