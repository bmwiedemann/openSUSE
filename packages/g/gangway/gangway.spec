#
# spec file for package gangway
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#

%global provider        github
%global provider_tld    com
%global project         heptiolabs
%global repo            gangway
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}

Name:           gangway
Version:        3.1.0
Release:        0
Summary:        Enables authentication flows via OIDC in kubernetes
License:        Apache-2.0
Group:          System/Management
URL:            https://github.com/heptiolabs/gangway
Source0:        %{name}-v%{version}.tar.gz
Source1:        vendor.tar.gz
# Patch to fix securecookie the value is too long
Patch0:         fix-securecookie-value-too-long.patch
BuildRequires:  golang(API) >= 1.11
BuildRequires:  golang-packaging
BuildRequires:  esc >= 0.2.0
%{go_nostrip}
%{go_provides}

%description
An application that can be used to easily enable authentication flows via OIDC for a kubernetes cluster.

%prep
%setup -q -n %{name}-v%{version}

tar -zxf %{SOURCE1}
%patch0 -p1

%build
esc -o cmd/gangway/bindata.go templates/
%goprep %{provider_prefix}
%gobuild ./...

%install
%goinstall ./cmd/gangway/main.go

%files
# Binaries
%{_bindir}/gangway
# Docs
%doc README.md docs/*
# License
%license LICENSE

%changelog
