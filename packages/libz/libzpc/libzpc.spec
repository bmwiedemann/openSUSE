#
# spec file for package libzpc
#
# Copyright (c) 2021 SUSE LLC
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


Name:           libzpc
Version:        1.0.0
Release:        0
Summary:        IBM Z Protected-key Crypto library
License:        Apache-2.0
Group:          Productivity/Security
URL:            https://github.com/opencryptoki/libzpc
Source:         libzpc-1.0.0.tar.gz
Source1:        %{name}-rpmlintrc
BuildRequires:  cmake >= 3.10
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  libjson-c-devel
ExclusiveArch:  s390x

%description
The IBM Z Protected-key Crypto library libzpc is an open-source
library targeting the 64-bit Linux on IBM Z (s390x) platform. It
provides interfaces for cryptographic primitives. The underlying
implementations make use of z/Architecture's extensive
performance-boosting hardware support and its protected-key feature
which ensures that key material is never present in main memory at any
time.

%package -n libzpc1
Summary:        Library
Group:          System/Libraries

%description -n libzpc1
This package contains the shared library to work with the
IBM protected-key cryptography hardware

%package devel
Summary:        Deep Learning Library development files
Requires:       libzpc0 = %{version}-%{release}

%description devel
This package provides the sole include file and symbolic link to the
shared library for the libzpc RPM.

%prep
%setup -q

%build
mkdir build && cd build
cmake .. -DCMAKE_INSTALL_PREFIX=/usr -DBUILD_SHARED_LIBS=ON -DBUILD_DOC=ON
%make_build

%install
cd build
%make_install

%post -n libzpc1 -p /sbin/ldconfig

%postun -n libzpc1 -p /sbin/ldconfig

%files -n libzpc1
%doc README.md
%license LICENSE
%{_libdir}/libzpc.so.1
%{_libdir}/libzpc.so.1.0.0

%files devel
%dir %{_includedir}/zpc
%{_includedir}/zpc/*.h
%{_libdir}/libzpc.so
%{_datadir}/pkgconfig/libzpc.pc

%changelog
