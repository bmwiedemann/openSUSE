#
# spec file for package pkcs11-provider
#
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
Version:        0.2
Release:        0
Summary:        OpenSSL 3 Engine for PKCS11
License:        Apache-2.0
Group:          Productivity/Security
URL:            https://github.com/latchset
Source0:        %{url}/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.xz
Source1:        %{url}/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.xz.asc
BuildRequires:  autoconf-archive
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libcrypto) >= 3.0.7
BuildRequires:  pkgconfig(p11-kit-1)

%description
With this provider for OpenSSL you can use the OpenSSL library (version 3) and
command line tools with any PKCS11 implementation as backend for the crypto
operations.

%prep
%setup -q

%build
autoreconf -fvi
%configure
make V=1 %{?_smp_mflags}

%install
%make_install
rm -f %{buildroot}%{_MODULES_DIR}/pkcs11.la

%files
%license COPYING
%{_datadir}/doc/pkcs11-provider/README.md
%{_mandir}/man7/provider-pkcs11.*
%{_MODULES_DIR}/pkcs11.so

%dir
%{_datadir}/doc/pkcs11-provider

%changelog

