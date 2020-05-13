#
# spec file for package Vc
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2018 Asterios Dramis <asterios.dramis@gmail.com>.
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


Name:           Vc
Version:        1.4.1
Release:        0
Summary:        Collection of SIMD Vector Classes
License:        BSD-3-Clause
Group:          System/Libraries
URL:            https://github.com/VcDevel/Vc/
Source0:        https://github.com/VcDevel/Vc/releases/download/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++

%description
Vc is a free software library to ease explicit vectorization of C++ code. It
has an intuitive API and provides portability between different compilers and
compiler versions as well as portability between different vector instruction
sets.

%package devel
Summary:        Development Files for Vc
Group:          Development/Libraries/C and C++

%description devel
Vc is a free software library to ease explicit vectorization of C++ code. It
has an intuitive API and provides portability between different compilers and
compiler versions as well as portability between different vector instruction
sets.

This package provides development headers needed to build software using Vc.

%package devel-doc
Summary:        API documentation for Vc
Group:          Development/Libraries/C and C++
BuildArch:      noarch

%description devel-doc
Vc is a free software library to ease explicit vectorization of C++ code. It
has an intuitive API and provides portability between different compilers and
compiler versions as well as portability between different vector instruction
sets.

This package provides the API documentation

%package devel-static
Summary:        Vc Static Library
Group:          Development/Libraries/C and C++
Requires:       %{name}-devel = %{version}

%description devel-static
Vc is a free software library to ease explicit vectorization of C++ code. It
has an intuitive API and provides portability between different compilers and
compiler versions as well as portability between different vector instruction
sets.

This package provides the Vc static library.

%prep
%setup -q

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
%cmake \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DBUILD_TESTING=OFF
%cmake_build

cd ../doc
doxygen
cd ..

%install
%cmake_install

# Install devel docs
mkdir -p %{buildroot}%{_docdir}/%{name}-devel-doc/
cp -a doc/html %{buildroot}%{_docdir}/%{name}-devel-doc/

%files devel-doc
%doc README.md
%{_docdir}/%{name}-devel-doc/

%files devel
%license LICENSE
%{_includedir}/Vc/
%dir %{_libdir}/cmake
%{_libdir}/cmake/Vc/

%files devel-static
%{_libdir}/libVc.a

%changelog
