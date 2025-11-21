#
# spec file for package gowitness
#
# Copyright (c) 2025 SUSE LLC and contributors
# Copyright (c) 2021-2025, Martin Hauke <mardnh@gmx.de>
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


Name:           gowitness
Version:        3.1.0
Release:        0
Summary:        A commandline web screenshot and information gathering tool
License:        GPL-3.0-or-later
Group:          Productivity/Networking/Diagnostic
URL:            https://github.com/sensepost/gowitness
#Git-Clone:     https://github.com/sensepost/gowitness.git
Source:         https://github.com/sensepost/gowitness/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  go1.25
BuildRequires:  golang-packaging
%{go_provides}

%description
A commandline web screenshot and information gathering tool.

%prep
%autosetup -a 1

%build
go build \
  -mod=vendor \
  -buildmode=pie \
  -o gowitness .

%install
install -D -m0755 gowitness %{buildroot}%{_bindir}/gowitness

%files
%license LICENSE
%doc README.md
%{_bindir}/gowitness

%changelog
