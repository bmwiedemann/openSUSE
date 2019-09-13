#
# spec file for package scrypt
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           scrypt
Version:        1.2.1
Release:        0
Summary:        Password-based encryption utility using the scrypt key derivation function
License:        BSD-3-Clause
Group:          Productivity/Networking/Security
Url:            http://www.tarsnap.com/scrypt.html
Source0:        http://www.tarsnap.com/scrypt/scrypt-%{version}.tgz
BuildRequires:  openssl-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The scrypt key derivation function was originally developed for use in the
Tarsnap online backup system and is designed to be far more secure against
hardware brute-force attacks than alternative functions such as PBKDF2 or
bcrypt.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
%make_install

%check
make test

%files
%defattr(-,root,root)
%doc COPYRIGHT FORMAT
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{ext_man}

%changelog
