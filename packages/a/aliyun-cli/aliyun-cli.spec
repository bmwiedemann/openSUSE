#
# spec file for package aliyun-cli
#
# Copyright (c) 2025 SUSE LLC
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
%global project         aliyun
%global repo            aliyun-cli
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider_prefix}

Name:           aliyun-cli
Version:        3.1.0
Release:        0
License:        Apache-2.0
Summary:        Alibaba Cloud CLI
URL:            https://github.com/aliyun/aliyun-cli
Source0:        %{name}-v%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  golang-packaging
BuildRequires:  go >= 1.23
# Building with -buildmode=pie is currently unsupported on armv7l, i586, riscv64 and s390x
ExclusiveArch:  aarch64 ppc64le x86_64

%{go_nostrip}
%{go_provides}

%description
The Alibaba Cloud CLI is a tool to manage and use Alibaba Cloud resources
through a command line interface. It is written in Go and built on the top
of Alibaba Cloud OpenAPI.

%prep
%setup -n %{repo}-v%{version} -a1

%build
%goprep %{import_path}
CGO_ENABLED=0 go build -v -x -buildmode=pie -ldflags="-X 'github.com/aliyun/aliyun-cli/cli.Version=${VERSION}'" -mod=vendor -o aliyun main/main.go

%install
install -d %{buildroot}%{_bindir}
install -p -m 0755 aliyun %{buildroot}%{_bindir}/aliyun

%files
%license LICENSE
%doc CHANGELOG.md README.md SECURITY.md
%{_bindir}/aliyun

%changelog
