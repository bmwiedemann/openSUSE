#
# spec file for package caasp-cli
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


# Project name when using go tooling.
%define go_version 1.11

Name:           caasp-cli
Version:        3.0.0+20180515.git_r38_8943b1e
Release:        0
Summary:        CLI for interacting with SUSE CaaS Platform Clusters
License:        Apache-2.0
Group:          System/Management
Url:            https://github.com/kubic-project/caasp-cli
Source:         master.tar.gz
BuildRequires:  go >= %{go_version}
BuildRequires:  golang-packaging
BuildRequires:  golang(API) = %{go_version}
Requires(post): %fillup_prereq
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{go_nostrip}
%{go_provides}

%description
SUSE CaaS Platform CLI provides command-line tooling for managing a SUSE CaaS Platform cluster

%prep
%setup -q -n caasp-cli-master

%build
%{goprep} github.com/kubic-project/caasp-cli
%{gobuild}

%install
%{goinstall}

%files
%defattr(-,root,root)
%doc README.md LICENSE
%{_bindir}/caasp-cli

%changelog
