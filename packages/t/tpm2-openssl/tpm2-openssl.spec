#
# spec file for package tpm2-openssl
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


%define _MODULES_DIR %(pkg-config --variable=modulesdir libcrypto)

Name:           tpm2-openssl
Version:        1.3.0
Release:        0
Summary:        OpenSSL 3 Engine for TPM2 devices
License:        BSD-3-Clause
Group:          Productivity/Security
URL:            https://github.com/tpm2-software
Source0:        %{url}/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz
Source1:        %{url}/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz.asc
Source2:        tpm2-openssl.keyring
BuildRequires:  autoconf-archive
BuildRequires:  libgcrypt-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libcrypto) >= 3
BuildRequires:  pkgconfig(tss2-esys) >= 3.2.0
BuildRequires:  pkgconfig(tss2-rc) >= 3.2.0
BuildRequires:  pkgconfig(tss2-tctildr)
Conflicts:      openssl_tpm2_engine

%description
Makes the TPM 2.0 accessible via the standard OpenSSL API and command-line tools, so
one can add TPM support to (almost) any OpenSSL 3.x based application.

%prep
%autosetup

%build
autoreconf -fvi
%configure
%make_build

%install
%make_install
# Remove libtool archives
find %{buildroot} -type f -name "*.la" -delete -print

%files
%doc README.md
%license LICENSE
%{_MODULES_DIR}/tpm2.so

%changelog
