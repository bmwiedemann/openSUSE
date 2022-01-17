# spec file for package k0sctl
#
# Copyright (c) 2021-2022 Orville Q. Song <orville@anislet.dev>
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

%global environment     production
%global git_hash        ab868a9

%global provider        github
%global provider_tld    com
%global project         k0sproject
%global repo            k0sctl
%global provider_prefix %{provider}.%{provider_tld}/%{project}
%global import_path     %{provider_prefix}/%{repo}

Name:           k0sctl
Version:        0.12.2
Release:        0
Summary:        A bootstrapping and management tool for k0s clusters
License:        Apache-2.0
Group:          System/Management
URL:            https://github.com/k0sproject/k0sctl
Source0:        %{name}-%{version}.tar.xz
Source1:        %{name}-vendor.tar.xz
BuildRequires:  golang-packaging
BuildRequires:  golang(API) >= 1.16

%description
k0sctl is a bootstrapping and management tool for k0s clusters.

%{go_nostrip}
%{go_provides}

%prep
%setup -q -n %{name}-%{version}
%setup -a1 %{SOURCE1}

%build
%goprep .
mkdir -p vendor/%{provider_prefix}
ln -s . vendor/%{import_path}
%gobuild -ldflags "-s -w -X github.com/k0sproject/k0sctl/version.Environment=%{environment} -X github.com/k0sproject/k0sctl/version.GitCommit=%{git_hash} -X github.com/k0sproject/k0sctl/version.Version=v%{version}" .

%install
%goinstall

%files
%defattr(-,root,root)
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%changelog
