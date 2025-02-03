#
# spec file for package minisign
#
# Copyright (c) 2025 SUSE LLC
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


Name:           minisign
Version:        0.12
Release:        0
License:        ISC
Summary:        A dead simple tool to sign files and verify signatures
URL:            https://jedisct1.github.io/minisign/
Group:          Productivity/Networking/Security
Source0:        https://github.com/jedisct1/minisign/archive/%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  pkgconfig(libsodium)

%description
Minisign is a dead simple tool to sign files and verify signatures.

It is portable, lightweight, and uses the highly secure Ed25519 public-key signature system.

%prep
%autosetup

%build
%cmake -DCMAKE_STRIP:BOOL=OFF
%cmake_build

%install
%cmake_install

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*

%changelog
