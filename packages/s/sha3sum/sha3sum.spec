#
# spec file for package sha3sum
#
# Copyright (c) 2024 SUSE LLC
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


Name:           sha3sum
Version:        1.2.3.1
Release:        0
Summary:        SHA-3 and Keccak checksum utility
License:        ISC
Group:          Productivity/Security
URL:            https://codeberg.org/maandree/sha3sum
Source:         https://codeberg.org/maandree/sha3sum/archive/%version.tar.gz
Patch1:         0001-build-repair-wrong-order-of-link-arguments.patch
BuildRequires:  c_compiler
BuildRequires:  libkeccak-devel >= 1.2
Conflicts:      perl-Digest-SHA3

%description
sha3sum contains command line utilities for the Keccak, SHA-3, SHAKE, and
RawSHAKE checksum utilities

A subset of Keccak was specified by NIST as SHA-3 (Secure Hash Algorithm 3).

%prep
%autosetup -p1 -n %name

%build
%make_build -r CC="%__cc" CFLAGS="%optflags"

%install
%make_install PREFIX="%_prefix"
# packaged via macro
rm -rvf %buildroot/%_datadir/licenses/%name

%check
%make_build check

%files
%license LICENSE
%doc README
%_bindir/*
%_mandir/man1/*.1*

%changelog
