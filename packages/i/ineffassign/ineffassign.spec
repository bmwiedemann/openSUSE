#
# spec file for package ineffassign
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
%global project         gordonklaus
%global repo            ineffassign
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider_prefix}

%define commit      7bae11eba15a3285c75e388f77eb6357a2d73ee2

Name:           ineffassign
Version:        0.0.0+git20180909.1003c8b
Release:        0
Summary:        Tool to detect ineffectual assignments in Go code
License:        MIT
Group:          Development/Languages/Golang
Url:            https://%{provider_prefix}
Source:         ineffassign-%{version}.tar.xz
BuildRequires:  golang-packaging
%{go_provides}

%description
This tool misses some cases because does not consider any type information in
its analysis. (For example, assignments to struct fields are never marked as
ineffectual.) It should, however, never give any false positives.

%prep
%setup -q -n %{repo}-%{version}

%build
%goprep %{provider_prefix}
%gobuild ...

%install
%goinstall

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%changelog
