#
# spec file for package canokey-qemu
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


Name:           canokey-qemu
Version:        0.0+git20230606.151568c
Release:        0
Summary:        Library for CanoKey support in QEMU
License:        Apache-2.0
URL:            https://github.com/canokeys/canokey-qemu
Source:         %{name}-%{version}.tar
Patch0:         canokey-git.diff
BuildRequires:  cmake

%description
CanoKey is an open-source secure key with supports of U2F / FIDO2 with Ed25519
and HMAC-secret, OpenPGP Card V3.4 with RSA4096, Ed25519 and more 2,
PIV (NIST SP 800-73-4), HOTP / TOTP, NDEF.


%package devel
Summary:        Development files for CanoKey support in QEMU
Requires:       %{name}

%description devel
Development files for CanoKey support in QEMU.

CanoKey is an open-source secure key with supports of U2F / FIDO2 with Ed25519
and HMAC-secret, OpenPGP Card V3.4 with RSA4096, Ed25519 and more 2,
PIV (NIST SP 800-73-4), HOTP / TOTP, NDEF.


%prep
%autosetup -p1
cp canokey-core/virt-card/git-rev.h.in canokey-core/virt-card/git-rev.h
echo "%version" >> canokey-core/virt-card/git-rev.h

%build
# undo command line override for those. needed to include libcanokey-core
%cmake -UBUILD_SHARED_LIBS -UBUILD_STATIC_LIBS
%cmake_build

%install
%cmake_install

%files devel
%{_includedir}/canokey-qemu.h
%{_libdir}/pkgconfig/canokey-qemu.pc

%files
%license LICENSE
%doc README.md
%{_libdir}/libcanokey-qemu.so.0
%{_libdir}/libcanokey-qemu.so

%changelog

