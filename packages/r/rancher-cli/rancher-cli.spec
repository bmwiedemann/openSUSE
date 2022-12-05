#
# spec file for package rancher-cli
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


%define __arch_install_post export NO_BRP_STRIP_DEBUG=true
Name:           rancher-cli
Version:        2.7.0
Release:        0
Summary:        Rancher CLI
License:        Apache-2.0
URL:            https://github.com/rancher/cli
Source:         https://github.com/rancher/cli/archive/refs/tags/v%{version}.tar.gz#/cli-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  golang(API) = 1.16

%description
The Rancher Command Line Interface (CLI) is a unified tool for interacting with your Rancher Server.
For usage information see: https://rancher.com/docs/rancher/v2.x/en/cli/

%prep
%setup -q -n cli-%{version}
%setup -q -T -D -a 1 -n cli-%{version}

%build -n cli-%{version}
go build \
   -mod=vendor \
   -ldflags="-X main.Version=%{version}"

%install
# Install the binary.
install -D -m 0755 cli "%{buildroot}/%{_bindir}/%{name}"

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%changelog
