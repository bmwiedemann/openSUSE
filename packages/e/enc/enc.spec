#
# spec file for package enc
#
# Copyright (c) 2023 SUSE LLC
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


Name:           enc
Version:        1.1.1
Release:        0
Summary:        Modern and friendly alternative to GnuPG
License:        MIT
Group:          Productivity/Networking/Security
URL:            https://github.com/life4/enc
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  golang-packaging

%description
Enc is a CLI tool for encryption, a modern and friendly alternative to GnuPG. It is easy to use, secure by default and can encrypt and decrypt files using password or encryption keys, manage and download keys, and sign data. Our goal was to make encryption available to all engineers without the need to learn a lot of new words, concepts, and commands.

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
