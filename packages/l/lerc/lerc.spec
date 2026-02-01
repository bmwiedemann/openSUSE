#
# spec file for package lerc
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define  sover  4
%define  lname  libLerc
Name:           lerc
Version:        4.0.0
Release:        0
Summary:        Limited Error Raster Compression
License:        Apache-2.0
Group:          Development/Libraries/C and C++
URL:            https://github.com/Esri/lerc
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source99:       baselibs.conf
BuildRequires:  c++_compiler
BuildRequires:  cmake
BuildRequires:  dos2unix

%description
LERC is an open-source image or raster format which supports rapid encoding
and decoding for any pixel type (not just RGB or Byte). Users set the
maximum compression error per pixel while encoding, so the precision of the
original input image is preserved (within user defined error bounds).

%package -n %{lname}%{sover}
Summary:        Shared library for %{name}

%description -n %{lname}%{sover}
LERC is an open-source image or raster format which supports rapid encoding
and decoding for any pixel type (not just RGB or Byte). Users set the
maximum compression error per pixel while encoding, so the precision of the
original input image is preserved (within user defined error bounds).
This package contains shared libraries of %{name}

%package        devel
Summary:        Development files for %{name}
Requires:       %{lname}%{sover} = %{version}-%{release}

%description    devel
The package contains libraries and header files for %{name}

%prep
%autosetup -p1
dos2unix -v -o NOTICE
dos2unix -v -o README.md
dos2unix -v -o doc/MORE.md

%build
%cmake
%cmake_build

%install
%cmake_install

%check
cd build
c++ %{optflags} --std=c++17 ../src/LercTest/main.cpp -L. -lLerc -o testLerc
LD_LIBRARY_PATH=. ./testLerc

%ldconfig_scriptlets -n %{lname}%{sover}

%files -n %{lname}%{sover}
%doc README.md CHANGELOG.md NOTICE
%{_libdir}/libLerc.so.%{sover}
%license LICENSE

%files devel
%doc README.md CHANGELOG.md NOTICE doc/
%{_includedir}/Lerc_c_api.h
%{_includedir}/Lerc_types.h
%{_libdir}/libLerc.so
%{_libdir}/pkgconfig/Lerc.pc

%changelog
