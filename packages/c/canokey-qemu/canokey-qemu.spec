#
# spec file for package canokey-qemu
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


Name:           canokey-qemu
Version:        0.0+git20260324.41044ec
Release:        0
Summary:        Library for CanoKey support in QEMU
License:        Apache-2.0
URL:            https://github.com/canokeys/canokey-qemu
Source:         %{name}-%{version}.tar
Source1:        README.SUSE
Source2:        canokey-qemu.apparmor
Source3:        canokey-qemu.tmpfiles
Patch0:         canokey-git.diff
Patch1:         canokey-core-static.diff
# PATCH-FIX-UPSTREAM part of canokey-core c50b625d and e4a756d6
Patch2:         canokey-core-fm-return-type.patch
BuildRequires:  cmake
BuildRequires:  glibc-devel-static
BuildRequires:  python3
BuildRequires:  python3-Jinja2
BuildRequires:  python3-jsonschema
BuildRequires:  systemd-rpm-macros

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

%package libvirt
Summary:        Use a virtual CanoKey in libvirt-managed QEMU guests
Requires:       %{name} = %{version}
Supplements:    (%{name} and libvirt-daemon-driver-qemu)
Requires:       system-user-qemu
BuildArch:      noarch

%description libvirt
State directory, and an AppArmor rule for it, that let QEMU guests started by
libvirt (virt-manager) use a virtual CanoKey, attached with libvirt's QEMU
command-line passthrough. See README.SUSE for the domain XML.

%prep
%autosetup -p1
cp canokey-core/virt-card/git-rev.h.in canokey-core/virt-card/git-rev.h
echo "%version" >> canokey-core/virt-card/git-rev.h

%build
# Ignore missing symbols from qemu, libcanokey-qemu directly calls back
# into qemu (remove "-Wl,--no-undefined")
%cmake \
  -UBUILD_SHARED_LIBS -UBUILD_STATIC_LIBS \
  -DCMAKE_SHARED_LINKER_FLAGS="%{?build_ldflags} -Wl,--as-needed -Wl,-z,now"

%cmake_build

%install
%cmake_install
install -D -m 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/apparmor.d/abstractions/libvirt-qemu.d/canokey-qemu
install -D -m 0644 %{SOURCE3} %{buildroot}%{_tmpfilesdir}/canokey-qemu.conf
cp %{SOURCE1} .

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post libvirt
%tmpfiles_create %{_tmpfilesdir}/canokey-qemu.conf

%files devel
%{_libdir}/libcanokey-qemu.so
%{_includedir}/canokey-qemu.h
%{_libdir}/pkgconfig/canokey-qemu.pc

%files
%license LICENSE
%doc README.md
%{_libdir}/libcanokey-qemu.so.1

%files libvirt
%doc README.SUSE
%dir %{_sysconfdir}/apparmor.d
%dir %{_sysconfdir}/apparmor.d/abstractions
%dir %{_sysconfdir}/apparmor.d/abstractions/libvirt-qemu.d
%config(noreplace) %{_sysconfdir}/apparmor.d/abstractions/libvirt-qemu.d/canokey-qemu
%{_tmpfilesdir}/canokey-qemu.conf

%changelog
