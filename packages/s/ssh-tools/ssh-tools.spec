#
# spec file for package ssh-tools
#
# Copyright (c) 2021 SUSE LLC
# Copyright (c) 2020, Martin Hauke <mardnh@gmx.de>
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


Name:           ssh-tools
Version:        1.7
Release:        0
Summary:        A collection of various tools using ssh
License:        GPL-3.0-or-later
Group:          Productivity/Networking/SSH
URL:            https://github.com/vaporup/ssh-tools/
Source:         https://github.com/vaporup/ssh-tools/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  bash
## SECTION test requirements
#BuildRequires:  ShellCheck
#BuildRequires:  openssh
#BuildRequires:  sshpass
## /SECTION
Requires:       bash
Requires:       openssh
Recommends:     colordiff
Recommends:     jo
BuildArch:      noarch

%description
A collection of various tools using ssh
The following tools are included
  * ssh-ping: check if host is reachable using ssh_config
  * ssh-version: shows version of the SSH server you are connecting to
  * ssh-diff: diff a file over SSH
  * ssh-facts: get some facts about the remote system
  * ssh-hostkeys: prints server host keys in several formats
  * ssh-keyinfo: prints keys in several formats
  * ssh-certinfo: shows validity and information of SSH certificates

%prep
%setup -q
sed -i 's|#!%{_bindir}/env bash|#!/bin/bash|g' ssh-*

%build

%install
install -D -m0755 -t %{buildroot}/%{_bindir}/ ssh-*

#%%check
# test disabled since it requires a network connection to an external system
#./test.sh

%files
%license LICENSE
%doc CHANGELOG.md
%{_bindir}/ssh-*

%changelog
