#
# spec file for package libzdnn
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


Name:           libzdnn
Version:        0.3.1
Release:        0
Summary:        IBM Z Deep Learning Library
License:        Apache-2.0
Group:          Development/Libraries/Other
URL:            https://github.com/IBM/zDNN
Source:         zDNN-0.3.1.tar.gz
Patch1:         sles15sp4-libzdnn-Limit-symbol-check-to-global-symbols-3.patch
Patch2:         sles15sp4-libzdnn-Fix-initialization-of-CFLAGS_INIT-2.patch
BuildRequires:  autoconf
BuildRequires:  gcc-c++
ExclusiveArch:  s390x

%description
IBM Z Deep Neural Network Library (zDNN) provides an interface for
applications making use of Neural Network Processing Assist
Facility (NNPA).

This IBM-provided C library provides a set of functions that handle
the data transformation requirements of the AIU and provide wrapper
functions for the NNPA instruction primitives.

%package -n libzdnn0
Summary:        Library interface for the IBM Cryptographic Accelerator
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
Requires:       libzdnn0 = %{version}-%{release}

%description devel
This package provides the sole include file and symbolic link to the
shared library for the libzdnn (zDNN) RPM.

%prep
%autosetup -p1 -n zDNN-%{version}

%build
autoconf
%configure
%make_build build

%install
%make_install

# We don't want/need the static library at this time. That could change.
rm -vf %{buildroot}/%{_libdir}/libzdnn.a

%post -n libzdnn0
/sbin/ldconfig

%postun -n libzdnn0
/sbin/ldconfig

%files -n libzdnn0
%doc README.md
%license LICENSE
%{_libdir}/libzdnn.so.0

%files devel
%{_includedir}/zdnn.h
%{_libdir}/libzdnn.so

%changelog
