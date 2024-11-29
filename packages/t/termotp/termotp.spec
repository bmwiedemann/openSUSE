#
# spec file for package termotp
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


Name:           termotp
Version:        0.0.11
Release:        0
Summary:        A TOTP code generator for your terminal
License:        Apache-2.0
Group:          Productivity/Security
URL:            https://github.com/marcopaganini/termotp
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  golang-packaging

%description
termotp reads an encrypted vault export from your TOTP Android App (currently, only Aegis Authenticator is supported) and displays issuers, providers and a TOTP for each of them. The program uses no database and reads directly from the App export. Since backups are encrypted, your credentials never stay on the disk unencrypted. It's basically a pure terminal based way to generate TOTP tokens while keeping your credentials encrypted.

%prep
%setup -q -a 1

%build
go build \
   -mod=vendor \
   -buildmode=pie

%install
install -D -m0755 %{name} %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}
%doc README.md

%changelog
