#
# spec file for package cilium-etcd-operator
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

%global provider        github
%global provider_tld    com
%global project         cilium
%global repo            cilium-etcd-operator
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}

Name:           cilium-etcd-operator
Version:        2.0.5
Release:        0
Summary:        Operator to manage Cilium's etcd cluster 
License:        Apache-2.0
Group:          Development/Languages/Golang
Url:            https://github.com/cilium/cilium-etcd-operator/archive/v%{version}.tar.gz
Source:         v%{version}.tar.gz
Source1:        LICENSE
BuildRequires:  golang-packaging
%{go_provides}

%description
Cilium uses etcd as one of its supported KV stores. This operator
provides etcd cluster management for cilium.

%prep
%setup -q -n %{name}-%{version}
cp %{SOURCE1} .

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
