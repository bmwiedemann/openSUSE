#
# spec file for package swag
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


Name:           swag
Version:        1.16.4
Release:        0
Summary:        Automatically generate RESTful API documentation with Swagger 2.0 for Go
License:        MIT
URL:            https://github.com/swaggo/swag
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  golang(API) >= 1.22

%description
Swag converts Go annotations to Swagger Documentation 2.0. We've created a
variety of plugins for popular Go web frameworks. This allows you to quickly
integrate with an existing Go project (using Swagger UI).

%prep
%autosetup -a 1

%build
%ifnarch ppc64
export GOFLAGS="-buildmode=pie"
%endif
go build ./cmd/%{name}

%install
install -D -m 0755 %{name} "%{buildroot}/%{_bindir}/%{name}"

%files
%doc README.md
%license license
%{_bindir}/%{name}

%changelog
