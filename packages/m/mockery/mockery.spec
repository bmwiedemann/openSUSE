#
# spec file for package mockery
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


Name:           mockery
Version:        2.36.0
Release:        0
Summary:        A mock code autogenerator for Go
License:        BSD-3-Clause
URL:            https://github.com/vektra/mockery
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  golang(API) >= 1.22

%description
mockery provides the ability to easily generate mocks for Golang interfaces
using the stretchr/testify/mock package. It removes the boilerplate coding
required to use mocks.

%prep
%autosetup -a 1

%build
%ifnarch ppc64
export GOFLAGS="-buildmode=pie"
%endif
go build \
   -ldflags="-X github.com/vektra/mockery/v2/pkg/logging.SemVer=v%{version}"

%install
install -D -m 0755 %{name} "%{buildroot}/%{_bindir}/%{name}"

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%changelog
