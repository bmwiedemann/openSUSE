#
# spec file for package openssl-pkcs11-sign-provider
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

%global modulesdir %(pkg-config --variable=modulesdir libcrypto)

Name:           openssl-pkcs11-sign-provider
Version:        1.0.0
Release:        0
Summary:        OpenSSL Provider for asymmetric operations with private PKCS#11 keys
License:        Apache-2.0
URL:            https://github.com/opencryptoki/openssl-pkcs11-sign-provider
Source0:        %{url}/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{url}/releases/download/v%{version}/%{name}-%{version}.tar.gz.asc

Requires:      openssl >= 3.0.0

BuildRequires: openssl-devel >= 3.0.0
BuildRequires: openCryptoki-devel >= 3.17.0
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: autoconf-archive
BuildRequires: automake
BuildRequires: libtool

# test dependencies
# BuildRequires: openssl >= 3.0.0
# BuildRequires: gnutls
# BuildRequires: sed
# BuildRequires: openCryptoki >= 3.17.0

%description
This package contains a provider module for OpenSSL 3.0, interfacing to
PKCS#11 for operations with private keys in PKCS#11 tokens.

%prep
%autosetup

%build
%configure --libdir=%{modulesdir}
%make_build
for file in openssl-*.cnf.sample; do mv $file $file.%{_arch}; done

%check
# Uncomment the following line to enable checks during package build.
# Note: for test-module ock, a working opencryptoki and p11-kit setup
# is required for testing.
# make check

%install
%make_install

%post
%postun

%files
%license COPYING
%doc README
%{modulesdir}/pkcs11sign.{so,la}
%{_mandir}/man5/pkcs11sign.cnf.5*
%{_mandir}/man7/pkcs11sign.7*
%changelog

