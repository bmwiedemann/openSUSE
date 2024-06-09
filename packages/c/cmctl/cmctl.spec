#
# spec file for package cmctl
#
# Copyright (c) 2024 SUSE LLC
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


%define __arch_install_post export NO_BRP_STRIP_DEBUG=true

%define archive_name cert-manager

Name:           cmctl
Version:        1.14.6
Release:        0
Summary:        CLI tool that can help you to manage cert-manager resources inside your cluster
License:        Apache-2.0
URL:            https://github.com/cert-manager/cert-manager
Source:         %{archive_name}-%{version}.tar.gz
Source1:        vendor.tar.gz
Source2:        README.md
BuildRequires:  go >= 1.20

%description
cmctl is a CLI tool that can help you to manage cert-manager resources inside your cluster.
While also available as a kubectl plugin, it is recommended to use as a stand alone binary as this allows the use of command auto-completion.

%prep
%autosetup -p1 -a 1 -n cert-manager-%{version}
cp %{S:2} .

%build
go build \
   -mod=vendor \
   -buildmode=pie \
   -ldflags="-w -s -X github.com/cert-manager/cert-manager/cmd/ctl/pkg/build.name=cmctl \
   -X github.com/cert-manager/cert-manager/cmd/ctl/pkg/build/commands.registerCompletion=true \
   -X github.com/cert-manager/cert-manager/pkg/util.AppVersion=%{version} \
   -X github.com/cert-manager/cert-manager/pkg/util.AppGitCommit=v%{version}" \
   -o bin/cmctl ./

%install
# Install the binary.
install -D -m 0755 bin/%{name} "%{buildroot}/%{_bindir}/%{name}"
cd %{buildroot}/%{_bindir}/
ln -s %{name} kubectl-cert_manager

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_bindir}/kubectl-cert_manager

%changelog
