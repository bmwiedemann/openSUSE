#
# spec file for package scitokens-cpp
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


Name:           scitokens-cpp
Version:        0.6.3
Release:        0
Summary:        C++ Implementation of the SciTokens Library
License:        Apache-2.0
Group:          Development/Libraries/C and C++
URL:            https://github.com/scitokens/scitokens-cpp
Source0:        https://github.com/scitokens/scitokens-cpp/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libcurl-devel
BuildRequires:  libuuid-devel
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  sqlite-devel

%description
SciTokens provide a token format for distributed authorization. The tokens are
self-describing, can be verified in a distributed fashion (no need to contact
the issuer to determine if the token is valid). This is convenient for a
federated environment where several otherwise-independent storage endpoints
want to delegate trust for an issuer for managing a storage allocation.

%package -n libSciTokens0
Summary:        C++ Implementation of the SciTokens Library

%description -n libSciTokens0
SciTokens provide a token format for distributed authorization. The tokens are
self-describing, can be verified in a distributed fashion (no need to contact
the issuer to determine if the token is valid). This is convenient for a
federated environment where several otherwise-independent storage endpoints
want to delegate trust for an issuer for managing a storage allocation.

%package devel
Summary:        Header files for the libscitokens public interfaces
Requires:       libSciTokens0 = %{version}

%description devel
SciTokens provide a token format for distributed authorization. The tokens are
self-describing, can be verified in a distributed fashion (no need to contact
the issuer to determine if the token is valid). This is convenient for a
federated environment where several otherwise-independent storage endpoints
want to delegate trust for an issuer for managing a storage allocation.

%prep
%autosetup -n scitokens-cpp-%{version}

%build
export CFLAGS="%optflags -Wno-error=deprecated-declarations"
%{cmake}
%{cmake_build}

%install
%{cmake_install}

%post -n libSciTokens0 -p /sbin/ldconfig
%postun -n libSciTokens0 -p /sbin/ldconfig

%files -n libSciTokens0
%license LICENSE
%{_libdir}/libSciTokens.so.0*

%files devel
%doc README.md
%license LICENSE
%{_libdir}/libSciTokens.so
%{_includedir}/scitokens/scitokens.h
%dir %{_includedir}/scitokens

%changelog
