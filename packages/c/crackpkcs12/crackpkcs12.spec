#
# spec file for package crackpkcs12
#
# Copyright (c) 2025 Andreas Stieger <Andreas.Stieger@gmx.de>
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


Name:           crackpkcs12
Version:        0.2.11
Release:        0
Summary:        Multithreaded program to crack PKCS#12 files (p12 and pfx extensions)
License:        GPL-3.0-or-later WITH cryptsetup-OpenSSL-exception
URL:            https://crackpkcs12.sourceforge.net/
Source:         https://sourceforge.net/projects/crackpkcs12/files/%{version}/%{name}-%{version}.tar.gz
Patch0:         crackpkcs12-0.2.11-nonvoid-return.patch
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libssl)

%description
crackpkcs12 is a tool to audit PKCS#12 files passwords (extension .p12 or
.pfx). It's written in C and uses openssl library.

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install

%check
%make_build check

%files
%license COPYING
%doc AUTHORS README
%{_bindir}/crackpkcs12

%changelog
