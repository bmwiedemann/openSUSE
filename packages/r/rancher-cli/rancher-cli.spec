#
# spec file for package rancher-cli
#
# Copyright (c) 2025 SUSE LLC and contributors
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           rancher-cli
Version:        2.12.0
Release:        0
Summary:        Rancher CLI
License:        Apache-2.0
URL:            https://github.com/rancher/cli
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  golang(API) >= 1.23

%description
The Rancher Command Line Interface (CLI) is a unified tool for interacting with
your Rancher Server.
For usage information see: https://rancher.com/docs/rancher/v2.x/en/cli/

%prep
%autosetup -p 1 -a 1

%build
go build \
   -mod=vendor \
   -buildmode=pie \
   -ldflags="-X main.VERSION=%{version}"

%install
# Install the binary.
install -D -m 0755 cli %{buildroot}/%{_bindir}/%{name}

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%changelog
