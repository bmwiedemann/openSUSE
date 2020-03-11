#
# spec file for package nmap-parse-output
#
# Copyright (c) 2020 SUSE LLC
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


Name:           nmap-parse-output
Version:        1.5.1
Release:        0
Summary:        A tool for analyzing Nmap scans
License:        BSD-3-Clause
Group:          Productivity/Networking/Diagnostic
URL:            https://github.com/ernw/nmap-parse-output/
Source:         https://github.com/ernw/nmap-parse-output/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         nmap-parse-output-fix-paths.patch
Requires:       bash
Requires:       libxslt-tools
BuildArch:      noarch

%description
Converts/manipulates/extracts data from a Nmap scan output.

%package bash-completion
Summary:        Bash Completion for %{name}
Group:          Productivity/Networking/Diagnostic
Requires:       %{name} = %{version}
Requires:       bash-completion
Supplements:    (nmap-parse-output and bash-completion)

%description bash-completion
Bash completion script for %{name}.

%prep
%setup -q
%patch0 -p1

%build

%install
install -D -m0755 %{name} %{buildroot}/%{_bindir}/%{name}
install -D -m0644 -t %{buildroot}%{_datadir}/%{name}/nmap-parse-output-xslt/ nmap-parse-output-xslt/*
install -D -m0644 _nmap-parse-output %{buildroot}%{_datadir}/bash-completion/completions/%{name}

%files
%license LICENSE ThirdPartyNotices.md
%doc README.md
%{_bindir}/nmap-parse-output
%{_datadir}/%{name}/

%files bash-completion
%{_datadir}/bash-completion/completions/%{name}

%changelog
