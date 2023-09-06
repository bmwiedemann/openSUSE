#
# spec file for package libexmdbpp
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


%define lname libexmdbpp0
Name:           libexmdbpp
Version:        1.11.0.58baa16
Release:        0
Summary:        A C++ implementation of the exmdb wire protocol
License:        AGPL-3.0-or-later
Group:          Productivity/Networking/Email/Servers
URL:            https://grommunio.com/
Source:         %name-%version.tar.xz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  python3
BuildRequires:  python3-pybind11-devel
BuildRequires:  pkgconfig(python3)

%description
The library provides a C++ API and implementation for constructing
exmdb protocol requests and responses and conversing with a server.

%package -n %lname
Summary:        A C++ implementation of the exmdb wire protocol
Group:          System/Libraries

%description -n %lname
The library provides a C++ API and implementation for constructing
exmdb protocol requests and responses and conversing with a server.

%package devel
Summary:        Development files for libexmdbpp
Group:          System/Libraries
Requires:       %lname = %version-%release

%description devel
The library provides a C++ API and implementation for constructing
exmdb protocol requests and responses and conversing with a server.

This subpackage contains the header files for the library.

%package -n python3-pyexmdb
Summary:        Python bindings for libexmdbpp
Group:          Development/Languages/Python
Requires:       %lname = %version-%release

%description -n python3-pyexmdb
The library provides a C++ API and implementation for constructing
exmdb protocol requests and responses and conversing with a server.

This subpackage contains bindings for Python.

%prep
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install
# Stop check-rpaths from complaining about standard runpaths (fedora).
export QA_RPATHS=0x0001

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%_libdir/libexmdbpp.so.0
%license LICENSE.txt

%files devel
%_includedir/exmdbpp/
%_libdir/libexmdbpp.so
%_datadir/exmdbpp/

%files -n python3-pyexmdb
%python3_sitearch/pyexm*

%changelog
