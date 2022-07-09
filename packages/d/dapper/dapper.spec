#
# spec file for package dapper
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

Name:           dapper
Version:        0.6.0
Release:        0
Summary:        Docker build wrapper
License:        Apache-2.0
URL:            https://github.com/rancher/dapper
Source:         dapper-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  go >= 1.16

%description
Dapper is a tool to wrap any existing build tool in an consistent environment. This allows people to build your software from source or modify it without worrying about setting up a build environment. The approach is very simple and taken from a common pattern that has adopted by many open source projects. Create a file called Dockerfile.dapper in the root of your repository. Dapper will build that Dockerfile and then execute a container based off of the resulting image. Dapper will also copy in source files and copy out resulting artifacts or will use bind mounting if you choose.

%prep
%setup -q
%setup -q -T -D -a 1

%build
go build \
   -mod=vendor \
   -buildmode=pie \
   -ldflags="-X main.Version=%{version}"

%install
# Install the binary.
install -D -m 0755 %{name} "%{buildroot}/%{_bindir}/%{name}"

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%changelog
