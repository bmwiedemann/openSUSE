#
# spec file for package ssh-audit
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


Name:           ssh-audit
Version:        2.9.0
Release:        0
Summary:        SSH server auditing
License:        MIT
Group:          Productivity/Security
URL:            https://github.com/jtesta/ssh-audit
Source:         https://github.com/jtesta/ssh-audit/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1:        https://github.com/jtesta/ssh-audit/releases/download/v%{version}/%{name}-%{version}.tar.gz.sig
Source2:        %{name}.keyring
BuildRequires:  fdupes
BuildRequires:  python3-pytest
BuildRequires:  python3-rpm-macros
BuildRequires:  python3-setuptools
Requires:       python3
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

%prep
%setup -q
sed -i -e '/^#!\//, 1d' src/ssh_audit/ssh_audit.py

%build
%python3_build

%install
%python3_install
%fdupes %{buildroot}%{python3_sitelib}
install -D -p -m0644 ssh-audit.1 %{buildroot}%{_mandir}/man1/ssh-audit.1

%files
%license LICENSE
%doc README.md
%{_bindir}/ssh-audit
%{_mandir}/man1/ssh-audit.1%{?ext_man}
%{python3_sitelib}/ssh_audit*

%changelog
