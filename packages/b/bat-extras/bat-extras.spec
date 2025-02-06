#
# spec file for package bat-extras
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


%define testsuite_version 6b97e0a531f77d2e1f10f48ebb68d4033d69e04d

Name:           bat-extras
Version:        2024.08.24
Release:        0
Summary:        Extra scripts for bat
License:        MIT
BuildArch:      noarch
Group:          Productivity/File utilities
URL:            https://github.com/eth-p/bat-extras
Source0:        https://github.com/eth-p/bat-extras/archive/v%{version}.tar.gz
Source1:        https://github.com/eth-p/best/archive/%{testsuite_version}.tar.gz
Patch0:         recreate-snapshots-with-bat-v0.25.0.patch
Requires:       bash
Requires:       bat
BuildRequires:  bat
BuildRequires:  ripgrep
BuildRequires:  shfmt
Recommends:     delta
Recommends:     entr
Recommends:     ripgrep

%description
Bash scripts that integrate bat with various command line tools.

%prep
%setup -q -a 1
rm -r '.test-framework'
mv best-%{testsuite_version}/ '.test-framework'
%patch 0

%build

%install
./build.sh --install --manuals --no-verify --minify=lib --prefix=%{buildroot}%{_prefix}
sed -i "s@/usr/bin/env bash@/bin/bash@" %{buildroot}%{_bindir}/*
install -Dm 0644 -t %{buildroot}%{_mandir}/man1 man/*

%check
./test.sh

%files
%defattr(-, root, root)
%license LICENSE.md
%{_mandir}/man1/*
%doc README.md
%{_bindir}/*

%changelog
