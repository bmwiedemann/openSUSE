#
# spec file for package openssl-ibmca
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


%global modulesdir %(pkg-config --variable=modulesdir libcrypto)

Name:           openssl-ibmca
Version:        2.5.0
Release:        0
Summary:        OpenSSL engine and provider for libica
License:        Apache-2.0
Group:          Hardware/Other
URL:            https://github.com/opencryptoki/openssl-ibmca
Source:         https://github.com/opencryptoki/openssl-ibmca/archive/v%{version}.tar.gz#/openssl-ibmca-%{version}.tar.gz
###
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
###
BuildRequires:  libica-devel >= 4.0.0
BuildRequires:  libica-tools >= 4.0.0
BuildRequires:  libopenssl-3-devel
BuildRequires:  libopenssl3
Requires:       libica4 >= 4.0.0
Requires:       libopenssl3
###
ExclusiveArch:  s390x
###

%description
OpenSSL engine and provider that uses the libica library under s390x to accelerate cryptographic operations

%prep
%autosetup -p1 -n openssl-ibmca-%{version}
 ./bootstrap.sh

%build
export CFLAGS="%{optflags}"
export CPPFLAGS="%{optflags}"

%configure \
  --disable-engine \
  --libdir=%{modulesdir}

%make_build

%install

%make_install

%post

%postun

%files
%license LICENSE
%doc ChangeLog
%doc README.md
%doc src/provider/ibmca-provider-opensslconfig
%{modulesdir}/ibmca-provider.*
%{_mandir}/man5/ibmca-provider.5%{?ext_man}

%changelog
