#
# spec file for package krius
#
# Copyright (c) 2023 SUSE LLC
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

Name:           krius
Version:        0.1.1
Release:        0
Summary:        Setup Prometheus, Thanos & friends across multiple clusters
License:        Apache-2.0
URL:            https://github.com/infracloudio/krius
Source:         krius-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  go >= 1.17

%description
Krius is a cli tool to setup and manage Prometheus, Thanos & friends across multiple clusters easily for scale

%prep
%setup -q
%setup -q -T -D -a 1

%build
go build \
   -mod=vendor \
   -buildmode=pie \
   -o bin/krius ./cli/cmd/

%install
# Install the binary.
install -D -m 0755 bin/%{name} "%{buildroot}/%{_bindir}/%{name}"

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%changelog
