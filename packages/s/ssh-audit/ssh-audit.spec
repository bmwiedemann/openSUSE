#
# spec file for package ssh-audit
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           ssh-audit
Version:        2.1.1
Release:        0
Summary:        SSH server auditing
License:        MIT
Group:          Productivity/Security
Url:            https://github.com/jtesta/ssh-audit
Source:         https://github.com/jtesta/ssh-audit/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1:        https://github.com/jtesta/ssh-audit/releases/download/v%{version}/%{name}-%{version}.tar.gz.sig
Source2:        %{name}.keyring
BuildRequires:  python3-pytest
Requires:       python >= 3
BuildArch:      noarch

%description
ssh-audit is a tool for ssh server auditing.

Features:
 * SSH1 and SSH2 protocol server support;
 * grab banner, recognize device or software and operating system, detect compression;
 * gather key-exchange, host-key, encryption and message authentication code algorithms;
 * output algorithm information (available since, removed/disabled, unsafe/weak/legacy, etc);
 * output algorithm recommendations (append or remove based on recognized software version);
 * output security information (related issues, assigned CVE list, etc);
 * analyze SSH version compatibility based on algorithm information;
 * historical information from OpenSSH, Dropbear SSH and libssh;
 * no dependencies, compatible with Python 2.6+, Python 3.x and PyPy;

%prep
%setup -q
sed -i "s|#!/usr/bin/env python3|#!%{_bindir}/python3|g" ssh-audit.py

%build
#

%install
install -Dm0755 ssh-audit.py %{buildroot}%{_bindir}/ssh-audit

%check
# Skip tests that need a network environment
python3 -m pytest -vv -k 'not (TestResolve or test_socket or test_add_constraint_with_platform or TestSSH2)'

%files
%license LICENSE
%doc README.md
%{_bindir}/ssh-audit

%changelog

