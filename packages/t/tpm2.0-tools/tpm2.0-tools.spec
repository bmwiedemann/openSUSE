#
# spec file for package tpm2.0-tools
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


%define _lto_cflags %{nil}
%ifarch %{ix86} x86_64 aarch64 %{arm} ppc64le
%bcond_without  test
%else
# ppc ppc64 s390x: some code (tpm2_command_header_from_bytes) depend
# on the endianness of the architecture:
#   gh#tpm2-software/tpm2-tools#3055
#   gh#tpm2-software/tpm2-tools#3060
#   gh#tpm2-software/tpm2-tools#3061
%bcond_with     test
%endif
Name:           tpm2.0-tools
Version:        5.4
Release:        0
Summary:        Trusted Platform Module (TPM) 2.0 administration tools
License:        BSD-3-Clause
Group:          Productivity/Security
URL:            https://github.com/tpm2-software/tpm2-tools/releases
Source0:        https://github.com/tpm2-software/tpm2-tools/releases/download/%{version}/tpm2-tools-%{version}.tar.gz
Source1:        https://github.com/tpm2-software/tpm2-tools/releases/download/%{version}/tpm2-tools-%{version}.tar.gz.asc
# git show william-roberts-pub javier-martinez-pub joshua-lock-pub idesai-pub > tpm2-tools.keyring
Source2:        tpm2-tools.keyring
Patch0:         fix_bogus_warning.patch
# PATCH-FIX-UPSTREAM add_missing_shut_down_call_on_cleanup.patch -- based on PR#3176
Patch1:         echo_tcti_call_python3_binary.patch
BuildRequires:  gcc-c++
BuildRequires:  libcurl-devel
BuildRequires:  libopenssl-devel
BuildRequires:  libtool
BuildRequires:  libuuid-devel
BuildRequires:  pkgconfig
BuildRequires:  tpm2-0-tss-devel
BuildRequires:  tpm2.0-abrmd-devel
BuildRequires:  pkgconfig(efivar)
Recommends:     tpm2.0-abrmd
# Pandoc is used for generating the man pages, but since 3.0.4 prebuilt man
# pages are shipped with the distribution tarball and we don't need to generate
# them any more. Pandoc is only available on openSUSE (not 32-bit x86) and not
# in Ring 1 (no haskell), so can't be used as build dependency here.
%if 0
%if 0%{?is_opensuse}
%ifnarch %{ix86}
BuildRequires:  pandoc
%endif
%endif
%endif
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

%if %{with test}
%check
# Do the tests sequentially to kill all tpm_server instances
# https://github.com/tpm2-software/tpm2-tools/issues/3042
%make_build check
%endif

%changelog
