#
# spec file for package libkcapi
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           liboqs
Version:        0.7.1
Release:        0
Summary:        C library for quantum-resistant cryptographic algorithms
License:        MIT
Group:          Productivity/Security
Url:            https://github.com/open-quantum-safe/liboqs/
Source:		https://github.com/open-quantum-safe/liboqs/archive/refs/tags/%{version}.tar.gz
Source1:	baselibs.conf
Patch0:		liboqs-fix-build.patch
BuildRequires:	cmake
BuildRequires:	libopenssl-devel
BuildRequires:	doxygen

%description
liboqs is an open source C library for quantum-resistant cryptographic
algorithms. Details about liboqs can be found in README.md. See in
particular limitations on intended use.

%package -n liboqs0
Summary:        C library for quantum-resistant cryptographic algorithms
Group:          System/Libraries

%description -n liboqs0
liboqs is a C library for quantum-resistant cryptographic 
algorithms. Details about liboqs can be found in README.md. See in
particular limitations on intended use.

%package devel
Summary:        Open source C library for quantum-resistant cryptographic algorithms
Group:          Development/Languages/C and C++
Requires:	liboqs0 = %version

%description devel
liboqs is an open source C library for quantum-resistant cryptographic 
algorithms. Details about liboqs can be found in README.md. See in
particular limitations on intended use.

%prep
%autosetup -p1

%build
mkdir build
export RPM_OPT_FLAGS="%optflags -std=gnu11"
cd build
cmake -DBUILD_SHARED_LIBS=ON -DOQS_DIST_BUILD=ON ..
%cmake_build 

%install
%cmake_install
# need to find out what cmake option is needed
mv %buildroot/usr/local/* %buildroot/usr
if [ "%_lib" != "lib" ]; then
	mv %buildroot/usr/lib %buildroot/usr/%_lib
fi
rmdir %buildroot/usr/local/

%post -n liboqs0 -p /sbin/ldconfig
%postun -n liboqs0 -p /sbin/ldconfig

%files -n liboqs0
%license LICENSE.txt 
/%{_libdir}/liboqs.so.0*

%files devel
%license LICENSE.txt 
%dir %{_includedir}/oqs
%{_includedir}/oqs/*
/%_libdir/liboqs.so
%dir /%_libdir/cmake/
%dir /%_libdir/cmake/liboqs/
/%_libdir/cmake/liboqs/liboqsConfig-noconfig.cmake
/%_libdir/cmake/liboqs/liboqsConfig.cmake

%changelog
