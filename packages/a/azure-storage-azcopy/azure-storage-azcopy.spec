#
# spec file for package azure-storage-azcopy
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
%global project         Azure
%global repo            azure-storage-azcopy
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider_prefix}

Name:           azure-storage-azcopy
Version:	10.30.0
Release:        0
License:        MIT
Summary:        Microsoft Azure Storage data transfer utility
URL:            https://github.com/Azure/azure-storage-azcopy
Source0:        %{name}-v%{version}.tar.gz
Source1:        vendor.tar.gz
# PATCH-FIX-UPSTREAM - Add support for s390x architecture - gh/wastore/keyctl#2
Patch0:         keyctl-add-s390x-support.patch
BuildRequires:  golang-packaging
BuildRequires:  go >= 1.24
# Building with -buildmode=pie is currently unsupported on armv7l, i586, riscv64 and s390x
ExclusiveArch:  aarch64 ppc64le x86_64

%{go_nostrip}
%{go_provides}

%description
AzCopy v10 is a command-line utility that you can use to copy data to and from
containers and file shares in Azure Storage accounts. AzCopy V10 presents
easy-to-use commands that are optimized for high performance and throughput.

%prep
%setup -n %{repo}-v%{version} -a1
pushd vendor/github.com/wastore/keyctl
%patch -P0 -p1
popd

%build
%goprep %{import_path}
CGO_ENABLED=0 go build -v -x -buildmode=pie -ldflags="-s -w -X main.version=%{version}" -mod=vendor

%install
install -d %{buildroot}%{_bindir}
install -p -m 0755 azure-storage-azcopy %{buildroot}%{_bindir}/azcopy

%files
%license LICENSE
%doc ChangeLog.md README.md SECURITY.md
%{_bindir}/azcopy

%changelog
