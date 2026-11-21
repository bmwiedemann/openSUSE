#
# spec file for package tpm2.0-tools
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


%define _lto_cflags %{nil}
# Tests are disabled for now.  On big-endian architectures (ppc ppc64
# s390x) some code (tpm2_command_header_from_bytes) depends on the
# endianness of the architecture:
#   gh#tpm2-software/tpm2-tools#3055
#   gh#tpm2-software/tpm2-tools#3060
#   gh#tpm2-software/tpm2-tools#3061
%bcond_with     test
Name:           tpm2.0-tools
Version:        5.8
Release:        0
Summary:        Trusted Platform Module (TPM) 2.0 administration tools
License:        BSD-3-Clause
Group:          Productivity/Security
URL:            https://github.com/tpm2-software/tpm2-tools
Source0:        https://github.com/tpm2-software/tpm2-tools/releases/download/%{version}/tpm2-tools-%{version}.tar.gz
Source1:        https://github.com/tpm2-software/tpm2-tools/releases/download/%{version}/tpm2-tools-%{version}.tar.gz.asc
# Release signing key of Andreas Fuchs (D533275B0123D0A679F51FF48F4F9A45D7FFEE74)
# The key can be accessed by "curl https://github.com/UNAME.gpg"
Source2:        tpm2-tools.keyring
BuildRequires:  libcurl-devel
BuildRequires:  libopenssl-devel
BuildRequires:  pkgconfig
BuildRequires:  tpm2-0-tss-devel
BuildRequires:  pkgconfig(efivar)
Suggests:       tpm2.0-abrmd
%if %{with test}
# requirements for unit test suite (configure --enable-unit)
BuildRequires:  dbus-1-daemon
BuildRequires:  expect
BuildRequires:  ibmswtpm2
BuildRequires:  iproute2
BuildRequires:  libcmocka-devel
BuildRequires:  python3-PyYAML
BuildRequires:  tpm2.0-abrmd
# for xxd, which is also required by the tests
BuildRequires:  vim
%endif

%description
Trusted Computing is a set of specifications published by the Trusted
Computing Group (TCG). The Trusted Platform Module (TPM) is the
hardware component for Trusted Computing. The tpm2.0-tools package
provides tools for enablement and configuration of the TPM 2.0 and
associated interfaces.

%prep
%autosetup -p1 -n tpm2-tools-%{version}

%build
# help configure find required executables for testing
export PATH=$PATH:/usr/sbin:/usr/libexec/ibmtss
%configure --disable-static \
	   %{?with_test: --enable-unit}
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%if %{with test}
%check
# Do the tests sequentially to kill all tpm_server instances
# https://github.com/tpm2-software/tpm2-tools/issues/3042
make check
%endif

%files
%doc docs/README.md docs/CHANGELOG.md
%license docs/LICENSE
%{_bindir}/tpm2*
%{_bindir}/tss2*
%{_mandir}/man1/tpm2*
%{_mandir}/man1/tss2*
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/*

%changelog
