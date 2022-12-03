#
# spec file for package openssl_tpm2_engine
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2017 James.Bottomley@HansenPartnership.com
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


Name:           openssl_tpm2_engine
Version:        3.1.2
Release:        0
Summary:        OpenSSL TPM 2.0 interface engine plugin
License:        LGPL-2.1-only
Group:          Productivity/Security
URL:            https://git.kernel.org/pub/scm/linux/kernel/git/jejb/openssl_tpm2_engine.git/
Source0:        https://git.kernel.org/pub/scm/linux/kernel/git/jejb/openssl_tpm2_engine.git/snapshot/%{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  fakeroot
BuildRequires:  help2man
BuildRequires:  ibmswtpm2
BuildRequires:  ibmtss-devel
BuildRequires:  libtool
BuildRequires:  openssl-devel

%description
This package contains a plugin a for OpenSSL which connects it with the
Trusted Platform Module version 2.0 found on newer machines and a
create_tpm2_key helper binary to create and extract a TPM key.

%prep
%setup -q

%build
autoreconf -fiv
%configure --libdir=/%{_lib}
%make_build

%check
make check || { cat tests/test-suite.log; exit 1; }

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
%define EXTRA_FILES ExtraFiles.list
CWD=`pwd`
cd %{buildroot}
touch $CWD/%{EXTRA_FILES}
find * -name \*.so -printf "/%p\n" > $CWD/%{EXTRA_FILES}

%files -f %{EXTRA_FILES}
%license LICENSE
%doc README openssl.cnf.sample
%{_bindir}/*
%{_mandir}/man1/*

%changelog
