#
# spec file for package uefisettings
#
# Copyright (c) 2026 SUSE LLC
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


Name:           uefisettings
Version:        0.1.6
Release:        0
Summary:        Command-line tool to read-write BIOS/UEFI settings
# Legal-Review-Notice: license derived from the full vendored tree (90 crates
# linked into the root crate per offline cargo tree): no copyleft linked.
# MIT-only, Apache-2.0-only (fbthrift), ISC-only (libloading) and
# Unicode-3.0 data (unicode-ident) crates force the aggregate tag; the rest
# is MIT-or-Apache dual-licensed (Unlicense, Zlib and LLVM-exception options
# satisfied via the MIT/Apache choice).
License:        BSD-3-Clause AND Apache-2.0 AND ISC AND MIT AND Unicode-3.0
URL:            https://github.com/linuxboot/uefisettings
Source0:        %{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  cargo-packaging
ExclusiveArch:  %{rust_tier1_arches}

%description
A tool to read/get/extract and write/change/modify BIOS/UEFI settings
from the Linux command line.

It currently supports two interfaces:

* HiiDB (used in OCP and also has partial support in other platforms)
* iLO BlobStore (used in HPE servers; needs HPE's closed-source
  ilorest_chif library at runtime, which is neither shipped nor
  required here)

%prep
%autosetup -a 1

%build
%{cargo_build}

%install
%{cargo_install}

%check
# NOTE: keep the cargo macros in this spec in braced form. The bare form
# misparses the trailing test arguments, which broke the build before.
# Tests skipped by leaf name (substring match): the two mount-flags tests
# need /proc and rootfs access, Transport and IloRestChif need HPE iLO
# hardware and the closed-source ilorest_chif library (same skips as NixOS).
%{cargo_test} -- --skip test_get_current_mount_flags_for_proc --skip test_get_current_mount_flags_for_root --skip Transport --skip IloRestChif

%files
%license LICENSE
%doc README.md doc/ilorest.md
%{_bindir}/uefisettings

%changelog
