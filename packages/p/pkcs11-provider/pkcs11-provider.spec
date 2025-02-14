#
# spec file for package pkcs11-provider
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2023 Luca Boccassi <bluca@debian.org>
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


%define _MODULES_DIR %(pkg-config --variable=modulesdir libcrypto)

Name:           pkcs11-provider
Version:        1.0
Release:        0
Summary:        A PKCS#11 provider for OpenSSL 3.0+
License:        Apache-2.0
Group:          Productivity/Security
URL:            https://github.com/latchset
Source0:        %{url}/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.xz
Source1:        %{url}/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.xz.asc
Source2:        %{name}.keyring
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libcrypto) >= 3.0.7
BuildRequires:  pkgconfig(p11-kit-1)
# Required for testing
BuildRequires:  expect
BuildRequires:  gnutls
BuildRequires:  opensc
BuildRequires:  p11-kit-devel
BuildRequires:  p11-kit-server
BuildRequires:  softhsm-devel
BuildRequires:  pkgconfig(nss)

%description
This is an Openssl 3.x provider to access Hardware or Software Tokens using
the PKCS#11 Cryptographic Token Interface.
This code targets version 3.0 of the cryptoki interface but should be backwards
compatible to previous versions as well.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%ifnarch s390x
%check
# do not run them in parrallel with %{?_smp_mflags}
%meson_test --num-processes 1
%endif

%files
%license COPYING
%doc README.md
%{_mandir}/man7/provider-pkcs11.*
%{_MODULES_DIR}/pkcs11.so

%changelog
