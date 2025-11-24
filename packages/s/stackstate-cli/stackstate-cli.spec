#
# spec file for package stackstate-cli
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

%define _bin_name sts

Name:           stackstate-cli
Version:        3.1.4
Release:        0
Summary:        SUSE Observability sts CLI
License:        Apache-2.0
URL:            https://github.com/stackvista/stackstate-cli
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  golang(API) >= 1.22
Provides:       suse-observability-cli

%description
The SUSE Observability sts CLI provides easy access to the functionality provided by the SUSE Observability APIs. It can be used for automation using SUSE Observability data, to configure SUSE Observability and to develop StackPacks.

%prep
%autosetup -a 1

%build
export GOFLAGS="-buildmode=pie"
go build -ldflags='-s -X main.version=%{version}' -o=./%{_bin_name} main.go

%install
install -D -m 0755 sts "%{buildroot}/%{_bindir}/%{_bin_name}"

%files
%doc README.md
%license LICENSE
%{_bindir}/%{_bin_name}

%changelog
