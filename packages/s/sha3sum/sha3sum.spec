#
# spec file for package sha3sum
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Version:        1.1.5
Release:        0
Summary:        SHA-3 and Keccak checksum utility
License:        ISC
Group:          Productivity/Security
URL:            https://github.com/maandree/sha3sum
Source:         https://github.com/maandree/sha3sum/archive/%version.tar.gz
BuildRequires:  libkeccak-devel >= 1.2
Conflicts:      perl-Digest-SHA3

%description
sha3sum contains command line utilities for the Keccak, SHA-3, SHAKE, and
RawSHAKE checksum utilities

A subset of Keccak was specified by NIST as SHA-3 (Secure Hash Algorithm 3).

%prep
%setup -q

%build
make %{?_smp_mflags} CFLAGS="%{optflags}"

%install
%make_install PREFIX=%{_prefix}
# packaged via macro
rm -rvf %{buildroot}%{_datadir}/licenses/%{name}

%check
make %{?_smp_mflags} check

%files
%license LICENSE
%doc README
%{_bindir}/*
%{_mandir}/man1/*.1%{?ext_man}

%changelog
