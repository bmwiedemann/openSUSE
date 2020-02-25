#
# spec file for package bash-git-prompt
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


Name:           bash-git-prompt
Version:        2.7.1
Release:        0
Summary:        Informative git prompt for bash and fish
License:        BSD-2-Clause
Group:          Development/Tools/Version Control
URL:            https://github.com/magicmonty/bash-git-prompt
Source0:        https://github.com/magicmonty/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Requires:       git
BuildArch:      noarch

%description
A bash prompt that displays information about the current git repository. In particular the branch name, difference with remote branch, number of files staged, changed, etc.

This package will automatically enable the git prompt for bash after
install. It will disable the prompt accordingly after uninstall.

%prep
%setup -q

%build
sed -i -e 's,#!/usr/bin/env bash,#!/bin/bash,' $(find . -name \*.sh)

%install
install -dm 755 %{buildroot}%{_datadir}/%{name}
install -pm 755 *.sh %{buildroot}%{_datadir}/%{name}
#install -pm 755 *.py %{buildroot}%{_datadir}/%{name}
install -pm 755 *.fish %{buildroot}%{_datadir}/%{name}
install -pm 644 README.md %{buildroot}%{_datadir}/%{name}
install -dm 755 %{buildroot}%{_datadir}/%{name}/themes
install -pm 644 themes/*.bgptheme %{buildroot}%{_datadir}/%{name}/themes
install -pm 644 themes/*.bgptemplate %{buildroot}%{_datadir}/%{name}/themes

# enable bash-git-prompt
mkdir -p %{buildroot}%{_sysconfdir}/profile.d
cat << EOF >> %{buildroot}%{_sysconfdir}/profile.d/%{name}.sh
if [ -n "\${BASH_VERSION-}" ] && [ -f %{_datadir}/%{name}/gitprompt.sh ]; then
    # Set config variables first

    GIT_PROMPT_ONLY_IN_REPO=1
    GIT_PROMPT_THEME=Default
    source %{_datadir}/%{name}/gitprompt.sh
fi
EOF

%files
%{_datadir}/%{name}
%{_sysconfdir}/profile.d/%{name}.sh

%doc README.md

%license LICENSE.txt

%changelog
