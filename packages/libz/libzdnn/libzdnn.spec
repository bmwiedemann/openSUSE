#
# spec file for package libzdnn
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


Name:           libzdnn
Version:        1.1.1
Release:        0
Summary:        IBM Z Deep Learning Library
License:        Apache-2.0
Group:          Development/Libraries/Other
URL:            https://github.com/IBM/zDNN
Source:         zDNN-1.1.1.tar.gz
BuildRequires:  autoconf
BuildRequires:  gcc-c++
%if %{gcc_version} < 14
BuildRequires:  gcc14-c++
%else
BuildRequires:  gcc%{gcc_version}-c++
%endif

ExclusiveArch:  s390x

%description
IBM Z Deep Neural Network Library (zDNN) provides an interface for
applications making use of Neural Network Processing Assist
Facility (NNPA).

This IBM-provided C library provides a set of functions that handle
the data transformation requirements of the AIU and provide wrapper
functions for the NNPA instruction primitives.

%package -n libzdnn0
Summary:        Library interface for the IBM AI Accelerator
Group:          Development/Libraries/Other

%description -n libzdnn0
IBM Z Deep Neural Network Library (zDNN) provides an interface for
applications making use of Neural Network Processing Assist
Facility (NNPA).

This IBM-provided C library provides a set of functions that handle
the data transformation requirements of the AIU and provide wrapper
functions for the NNPA instruction primitives.

%package devel
Summary:        Deep Learning Library development files
Group:          Development/Libraries/Other
Requires:       libzdnn0 = %{version}-%{release}

%description devel
This package provides the sole include file and symbolic link to the
shared library for the libzdnn (zDNN) RPM.

%prep
%autosetup -p1 -n zDNN-%{version}

%build

export CC=gcc-%{gcc_version}
export CXX=g++-%{gcc_version}

%if %{gcc_version} < 14
export CC=gcc-14
export CXX=g++-14
%endif

autoconf
%configure
%make_build build

%install
%make_install

# We don't want/need the static library at this time. That could change.
rm -vf %{buildroot}/%{_libdir}/libzdnn.a

%post -n libzdnn0 -p /sbin/ldconfig

%postun -n libzdnn0 -p /sbin/ldconfig

%files -n libzdnn0
%doc README.md
%license LICENSE
%{_libdir}/libzdnn.so.0

%files devel
%{_includedir}/zdnn.h
%{_libdir}/libzdnn.so

%changelog
