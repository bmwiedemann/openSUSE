#
# spec file for package libzpc
#
# Copyright (c) 2026 SUSE LLC and contributors
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
Version:        2.0.1
Release:        0
Summary:        IBM Z Protected-key Crypto library
License:        MIT
Group:          Productivity/Security
URL:            https://github.com/opencryptoki/libzpc
Source0:        https://github.com/opencryptoki/libzpc/archive/refs/tags/v%{version}.tar.gz#/libzpc-%{version}.tar.gz
Source1:        libzpc-rpmlintrc

BuildRequires:  clang
BuildRequires:  cmake >= 3.10
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libjson-c-devel

BuildRequires:  pkgconfig(libcrypto) >= 3.0.7
BuildRequires:  pkgconfig(libssl) >= 3.0.7

ExclusiveArch:  s390x

%description
The IBM Z Protected-key Crypto library %{name} is an open-source project
targeting the 64-bit Linux on IBM Z (s390x) platform. It provides access
to z/Architecture's extensive performance-boosting hardware support and its
protected-key feature which ensures that key material is never present in
main memory at any time.


%ifarch s390x
%package	provider
Summary:        OpenSSL provider module for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description	provider
The %{name}-provider package contains a provider module for OpenSSL v3.0 (and
later), interfacing to the protected key feature of z/Architecture.
%endif

%package	tools
Summary:        Key management tool for %{name} keys
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description	tools
The %{name}-tools package contains a key management tool for key origins.
As the protected keys itself are volatile, the tooling can be used to manage
persistent protected key origins, from which protected keys can be (re-)derived.

%prep
%autosetup -p1
%global modulesdir %(pkg-config --variable=modulesdir libcrypto)

%build
%cmake
%make_build

%install
cd build
touch hbkzpcprovider.conf.5 hbkzpcprovider.7 zpckey.1
%make_install
install -m644 hbkzpcprovider.conf \
        -D -t %{buildroot}%{_sysconfdir}/pki/tls/openssl.d/

%fdupes %{buildroot}%{_mandir}

%check
%ctest

%files
%doc README.md CHANGES.md
%license LICENSE

%ifarch s390x
%files provider
%license LICENSE
%{modulesdir}/zpcprovider.so
%{_mandir}/man5/hbkzpcprovider.conf.5*
%{_mandir}/man7/hbkzpcprovider.7*
%dir %{_sysconfdir}/pki
%dir %{_sysconfdir}/pki/tls
%dir %{_sysconfdir}/pki/tls/openssl.d
%config(noreplace) %{_sysconfdir}/pki/tls/openssl.d/hbkzpcprovider.conf
%endif

%files tools
%license LICENSE
%{_bindir}/zpckey
%{_mandir}/man1/zpckey.1*

%changelog
