#
# spec file for package tpm2.0-tools
#
# Copyright (c) 2021 SUSE LLC
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


Name:           tpm2.0-tools
Version:        5.1.1
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
Patch2:         0001-tpm2_checkquote-fix-uninitialized-variable.patch
Patch3:         0001-tpm2_eventlog-read-eventlog-file-in-chunks.patch
Patch4:         0001-tpm2_eventlog-fix-buffer-offset-when-reading-the-eve.patch
BuildRequires:  gcc-c++
BuildRequires:  libcurl-devel
BuildRequires:  libopenssl-devel
BuildRequires:  libtool
BuildRequires:  libuuid-devel
BuildRequires:  pkgconfig(efivar)
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
BuildRequires:  pkgconfig
BuildRequires:  tpm2-0-tss-devel
BuildRequires:  tpm2.0-abrmd-devel
# requirements for unit test suite (configure --enable-unit)
BuildRequires:  expect
BuildRequires:  ibmswtpm2
BuildRequires:  libcmocka-devel
BuildRequires:  python38-pyaml
BuildRequires:  tpm2.0-abrmd
# for xxd, which is also required by the tests
BuildRequires:  vim
Recommends:     tpm2.0-abrmd

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
%configure --disable-static --enable-unit
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
find %{buildroot} -type f -name "*.la" -delete -print

%files
%defattr(-,root,root)
%doc README.md doc/CHANGELOG.md
%license doc/LICENSE
/usr/bin/tpm2*
/usr/bin/tss2*
%{_mandir}/man1/tpm2*
%{_mandir}/man1/tss2*
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/*

# the test suite does not currently work, because it conflicts with our LTO
# linking (see bsc#1188085).
#%%check
#make check

%changelog
