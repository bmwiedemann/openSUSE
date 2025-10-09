#
# spec file for package kleingebaeck
#
# Copyright (c) 2024-2025, Martin Hauke <mardnh@gmx.de>
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


Name:           kleingebaeck
Version:        0.3.23
Release:        0
Summary:        Backup tool for kleinanzeigen.de
License:        GPL-3.0-or-later
URL:            https://github.com/TLINDEN/kleingebaeck
#Git-Clone:     https://github.com/TLINDEN/kleingebaeck.git
Source:         https://github.com/TLINDEN/kleingebaeck/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  go >= 1.21
BuildRequires:  golang-packaging
%{go_provides}

%description
This tool can be used to backup ads on the German ad page
https://kleinanzeigen.de

It downloads all (or only the specified ones) ads of one user into
a directory, each ad into its own subdirectory.

The backup will contain a textfile Adlisting.txt which contains
the ad contents as the title, body, price etc.

All images will be downloaded as well.

%prep
%autosetup -p 1 -a 1

%build
go build \
  -mod=vendor \
  -buildmode=pie \
  -o kleingebaeck .


%install
install -Dm 0755 kleingebaeck %{buildroot}/%{_bindir}/kleingebaeck
install -Dm 0644 kleingebaeck.1 %{buildroot}%{_mandir}/man1/kleingebaeck.1

%files
%license LICENSE
%doc README.md README-de.md
%doc example.conf
%{_bindir}/kleingebaeck
%{_mandir}/man1/kleingebaeck.1%{?ext_man}

%changelog
