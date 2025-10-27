#
# spec file for package gotestsum
#
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


Name:           gotestsum
Version:        1.13.0
Release:        0
Summary:        CLI Go test runner with output optimized for human readability
License:        Apache-2.0
Group:          Development/Languages/Go
URL:            https://github.com/gotestyourself/gotestsum
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  golang(API) >= 1.24

%description
Go test runner with output optimized for humans, JUnit XML for CI integration,
and a summary of the test results.

%prep
%autosetup -a 1

%build
%ifnarch ppc64
export GOFLAGS="-buildmode=pie"
go build
%endif

%check
# execute the binary as a basic check
./%{name} --help

%install
install -D -m 0755 %{name} "%{buildroot}/%{_bindir}/%{name}"

%files
%doc README.md
%license LICENSE NOTICE
%{_bindir}/%{name}

%changelog
