#
# spec file for package gops
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


%global provider        github
%global provider_tld    com
%global project         google
%global repo            gops
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider_prefix}

Name:           gops
Version:        0.3.4
Release:        0
Summary:        A tool to list and diagnose Go processes currently running on your system
License:        BSD-3-Clause-Clear
Group:          System/Monitoring
Url:            https://%{provider_prefix}
Source0:        https://%{provider_prefix}/archive/v%{version}.tar.gz#/%{repo}-%{version}.tar.gz
BuildRequires:  golang-packaging
%{go_provides}

%description
gops is a command to list and diagnose Go processes currently running on your
system. For processes that starts the diagnostics agent, gops can report
additional information such as the current stack trace, Go version, memory stats,
etc. It is possible to use gops tool both in local and remote mode.

%prep
%setup -q -n %{repo}-%{version}

%build
%goprep %{provider_prefix}
%gobuild .

%install
%goinstall

%files
%{_bindir}/%{name}

%changelog

