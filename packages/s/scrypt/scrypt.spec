#
# spec file for package scrypt
#
# Copyright (c) 2020 SUSE LLC
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


Name:           scrypt
Version:        1.3.1
Release:        0
Summary:        Password-based encryption utility using the scrypt key derivation function
License:        BSD-3-Clause
Group:          Productivity/Networking/Security
URL:            https://www.tarsnap.com/scrypt.html
Source0:        https://www.tarsnap.com/scrypt/scrypt-%{version}.tgz
Source1:        https://www.tarsnap.com/scrypt/scrypt-sigs-%{version}.asc#/scrypt-%{version}.tgz.asc
Source3:        %name.keyring
BuildRequires:  openssl-devel

%description
The scrypt key derivation function was originally developed for use in the
Tarsnap online backup system and is designed to be far more secure against
hardware brute-force attacks than alternative functions such as PBKDF2 or
bcrypt.

%prep
%setup -q

%build
%configure
%make_build

%install
%make_install

%check
make %{?_smp_mflags} test

%files
%license COPYRIGHT
%doc FORMAT
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}

%changelog
