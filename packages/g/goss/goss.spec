#
# spec file for package goss
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
# nodebuginfo


%define dgoss_name dgoss
%define kgoss_name kgoss
%define dcgoss_name dcgoss

Name:           goss
Version:        0.3.18
Release:        0
Summary:        Quick and Easy server testing/validation
License:        Apache-2.0
Group:          Development/Tools/Other
URL:            https://github.com/aelsabbahy/goss
Source0:        goss-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  golang-packaging
BuildRequires:  golang(API) >= 1.13

%description
Goss is a YAML based serverspec alternative tool for validating a server’s configuration. It eases the process of writing tests by allowing the user to generate tests from the current system state. Once the test suite is written they can be executed, waited-on, or served as a health endpoint.

%prep
%setup -q
tar -zxf %{SOURCE1}

%build
GO111MODULE=on CGO_ENABLED=0 go build -mod=vendor -o %{name} -buildmode=pie \
	-ldflags "-s -w -X main.version=%{version}" ./cmd/goss/goss.go

%install
install -D -m0755 %{name} %{buildroot}%{_bindir}/%{name}
install -D -m0755 extras/%{dgoss_name}/%{dgoss_name} %{buildroot}%{_bindir}/%{dgoss_name}
install -D -m0755 extras/%{kgoss_name}/%{kgoss_name} %{buildroot}%{_bindir}/%{kgoss_name}
install -D -m0755 extras/%{dcgoss_name}/%{dcgoss_name} %{buildroot}%{_bindir}/%{dcgoss_name}

%files
%license LICENSE
%{_bindir}/%{name}
%{_bindir}/%{dgoss_name}
%{_bindir}/%{kgoss_name}
%{_bindir}/%{dcgoss_name}

%changelog
