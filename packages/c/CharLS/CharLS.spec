#
# spec file for package CharLS
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


%define so_ver 2

Name:           CharLS
Version:        2.0.0
Release:        0
Summary:        A JPEG-LS library
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
Url:            https://github.com/team-charls/charls/
Source0:        https://github.com/team-charls/charls/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
%if 0%{?suse_version} > 1320
BuildRequires:  gcc-c++
%else
# Leap 42.2+ / SLE12SP2Backports
BuildRequires:  gcc6-c++
#!Buildignore:  libgcc_s1
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
An optimized implementation of the JPEG-LS standard for lossless and
near-lossless image compression. JPEG-LS is a low-complexity standard that
matches JPEG 2000 compression ratios. In terms of speed, CharLS outperforms
open source and commercial JPEG LS implementations.

%package devel
Summary:        Libraries and headers for CharLS
Group:          Development/Libraries/C and C++
Requires:       libCharLS%{so_ver} = %{version}

%description devel
This package contains libraries and headers for CharLS.

%package -n libCharLS%{so_ver}
Summary:        A JPEG-LS library
Group:          System/Libraries

%description -n libCharLS%{so_ver}
An optimized implementation of the JPEG-LS standard for lossless and
near-lossless image compression. JPEG-LS is a low-complexity standard that
matches JPEG 2000 compression ratios. In terms of speed, CharLS outperforms
open source and commercial JPEG LS implementations.

%prep
%setup -q -n charls-%{version}
# Fix rpmlint warning "wrong-file-end-of-line-encoding"
sed -i 's/\r$//' License.txt

%build
test -x "$(type -p gcc-5)" && export CC=gcc-5
test -x "$(type -p g++-5)" && export CXX=g++-5
test -x "$(type -p gcc-6)" && export CC=gcc-6
test -x "$(type -p g++-6)" && export CXX=g++-6
test -x "$(type -p gcc-7)" && export CC=gcc-7
test -x "$(type -p g++-7)" && export CXX=g++-7
%cmake \
 -DBUILD_SHARED_LIBS=ON \
 -DBUILD_TESTING=ON
make %{?_smp_mflags} VERBOSE=1

%install
%cmake_install

%check
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:.
ctest .

%post -n libCharLS%{so_ver} -p /sbin/ldconfig

%postun -n libCharLS%{so_ver} -p /sbin/ldconfig

%files devel
%defattr(-,root,root,-)
%doc License.txt README.md
%{_includedir}/CharLS/
%{_libdir}/*.so

%files -n libCharLS%{so_ver}
%defattr(-,root,root,-)
%{_libdir}/libCharLS.so.%{so_ver}*

%changelog
