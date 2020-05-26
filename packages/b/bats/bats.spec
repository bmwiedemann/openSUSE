#
# spec file for package bats
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


Name:           bats
Version:        1.2.0
Release:        0
Summary:        Bash Automated Testing System
License:        MIT
Group:          Development/Tools/Other
URL:            https://github.com/bats-core/bats-core/
Source:         https://github.com/bats-core/bats-core/archive/v%{version}.tar.gz
BuildRequires:  ncurses-utils
BuildArch:      noarch

%description
Bats is a TAP-compliant (http://testanything.org/) testing framework for Bash.
It provides a simple and repeatable way to verify that the UNIX programs you
write behave as expected.

A Bats test file is a Bash script with special syntax for defining test cases.
Under the hood, each test case is just a function with a description.

Bats is most useful when testing software written in Bash, but you can use it
to test any UNIX program.

%prep
%setup -q -n %{name}-core-%{version}
mv libexec lib

sed -i 's|libexec|lib|g' install.sh ./lib/bats-core/* ./bin/bats
sed -i '1s|#!%{_bindir}/env bash|#!/bin/bash|' ./lib/bats-core/* ./bin/bats

%build

%install
./install.sh %{buildroot}%{_prefix}

%check
./bin/bats test/bats.bats
./bin/bats test/suite.bats

%files
%license LICENSE.md
%doc README.md
%{_bindir}/bats
%{_prefix}/lib/%{name}-core
%{_mandir}/man1/bats.1%{?ext_man}
%{_mandir}/man7/bats.7%{?ext_man}

%changelog
