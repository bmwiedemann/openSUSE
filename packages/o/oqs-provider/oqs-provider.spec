#
# spec file for package oqs-provider
#
# Copyright (c) 2024 SUSE LLC
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


Name:           oqs-provider
Version:        0.6.1
Release:        0
Summary:        Quantum-safe crypto provider for OpenSSL
License:        MIT
Group:          Productivity/Security
URL:            https://github.com/open-quantum-safe/oqs-provider/
Source:         https://github.com/open-quantum-safe/oqs-provider/archive/refs/tags/%{version}.tar.gz#/%name-%version.tar.gz
# currently would need libtestutil.a from openssl-3, so basically a copy of openssl-3 to test.
Patch1:         oqs-provider-disable-test.patch
BuildRequires:  cmake
BuildRequires:  libopenssl-3-devel
BuildRequires:  pkgconfig(liboqs)

%description
This is a plugin/shared library making available quantum-safe cryptography
(QSC) to OpenSSL 3.x installations via the Provider API.

Sample call:

openssl-3 ciphers -provider oqsprovider

%prep
%autosetup

%build
mkdir build
export RPM_OPT_FLAGS="%optflags -std=gnu11"
cd build
cmake -DBUILD_SHARED_LIBS=ON ..
%cmake_build

%install
install -d %buildroot/%{_libdir}/ossl-modules/

install -m 755 -c build/lib/oqsprovider.so %buildroot/%{_libdir}/ossl-modules/

%files
%license LICENSE.txt
%dir /%{_libdir}/ossl-modules
/%{_libdir}/ossl-modules/oqsprovider.so

%changelog
