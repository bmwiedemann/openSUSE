#
# spec file for package ai-bwrap
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           ai-bwrap
Version:        0.1.1~git20260918.4bdb112
Release:        0
Summary:        Run AI coding agents inside a bubblewrap sandbox
License:        MIT
URL:            https://github.com/didvc/ai-bwrap
Source0:        ai-bwrap-%{version}.tar.gz
Source1:        config.sh
BuildArch:      noarch
%if 0%{?suse_version} >= 1699
BuildRequires:  shellcheck
%endif
Requires:       bubblewrap

%description
ai-bwrap runs AI coding agents or a plain shell inside a bubblewrap sandbox.
Each agent gets read-write access only to the current working directory or a
transparent overlay while the rest of $HOME stays hidden; only the config,
cache, and state directories an agent actually needs are passed through. Agents
are declared as small shell functions, so the registry is extensible without
modifying the wrapper.

%prep
%autosetup -n ai-bwrap-%{version} -p1

%build
# embrace suse standards
sed -i 's@#!/usr/bin/env bash@#!/usr/bin/bash@' ai-bwrap

%install
install -Dm0755 ai-bwrap %{buildroot}%{_bindir}/%{name}
install -Dm644 %{S:1} %{buildroot}%{_sysconfdir}/ai-bwrap/%{S:1}

%if 0%{?suse_version} >= 1699
%check
shellcheck ai-bwrap
%endif

%files
%license LICENSE
%doc README.md
%doc CITATION.cff
%{_bindir}/%{name}
%config %{_sysconfdir}/ai-bwrap

%changelog
