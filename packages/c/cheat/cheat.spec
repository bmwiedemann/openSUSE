#
# spec file for package cheat
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


Name:           cheat
Version:        4.4.0
Release:        0
Summary:        Allows you to create and view interactive cheatsheets on the command-line
License:        MIT
Group:          Productivity/Other
URL:            https://github.com/cheat/cheat
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  golang-packaging

%description
cheat allows you to create and view interactive cheatsheets on the command-line. It was designed to help remind *nix system administrators of options for commands that they use frequently, but not frequently enough to remember.

%prep
%setup -q -a 1

%build
go build -mod=vendor -buildmode=pie -o cheat ./cmd/cheat

%install
install -D -m0755 %{name} %{buildroot}%{_bindir}/%{name}
install -Dm644 "doc/%{name}.1" -t "%{buildroot}%{_mandir}/man1/"

%files
%{_bindir}/%{name}
%{_mandir}/man1/cheat.1%{?ext_man}

%changelog
