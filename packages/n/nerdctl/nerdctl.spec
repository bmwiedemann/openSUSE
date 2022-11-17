#
# spec file for package nerdctl
#
# Copyright (c) 2022 SUSE LLC
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
%global project         containerd
%global repo            nerdctl
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider_prefix}

Name:           nerdctl
Version:        1.0.0
Release:        0
Summary:        Docker-compatible CLI for containerd
License:        Apache-2.0
URL:            https://github.com/containerd/nerdctl
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.xz
BuildRequires:  golang(API) >= 1.18
Requires:       buildkit
Requires:       cni-plugins
Requires:       containerd
Requires:       rootlesskit >= 1.0.0
Requires:       slirp4netns >= 0.4.0
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
nerdctl is a Docker-compatible CLI for containerd.

%prep
%setup -qa1

%build
CGO_ENABLED=0
go build -mod=vendor -buildmode=pie -o _output/nerdctl %{provider_prefix}/cmd/nerdctl

%install
mkdir -p %{buildroot}%{_bindir}/
install -m 0755 _output/nerdctl %{buildroot}%{_bindir}/nerdctl
install -m 0755 extras/rootless/containerd-rootless-setuptool.sh %{buildroot}%{_bindir}/containerd-rootless-setuptool.sh
install -m 0755 extras/rootless/containerd-rootless.sh %{buildroot}%{_bindir}/containerd-rootless.sh

%files
%license LICENSE
%doc docs/*.md
%{_bindir}/nerdctl
%{_bindir}/containerd-rootless-setuptool.sh
%{_bindir}/containerd-rootless.sh

%changelog
