#
# spec file for package ineffassign
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           ineffassign
Version:        0.2.0
Release:        0
Summary:        Tool to detect ineffectual assignments in Go code
License:        MIT
URL:            https://github.com/gordonklaus/ineffassign
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
Source99:       %{name}-rpmlintrc
BuildRequires:  golang(API) >= 1.23

%description
This tool misses some cases because does not consider any type information in
its analysis. (For example, assignments to struct fields are never marked as
ineffectual.) It should, however, never give any false positives.

%prep
%autosetup -a 1

%build
%ifnarch ppc64
export GOFLAGS="-buildmode=pie"
%endif
go build

%install
# Install the binary.
install -D -m 0755 %{name} "%{buildroot}/%{_bindir}/%{name}"

%check
# execute the binary as a basic check
./%{name} --help

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%changelog
