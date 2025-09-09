#
# spec file for package go-licenses
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


Name:           go-licenses
Version:        2.0.1
Release:        0
Summary:        CLI tool to report the licenses used by a Go package and its dependencies
License:        Apache-2.0
Group:          Development/Languages/Go
URL:            https://github.com/google/go-licenses
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
Patch0:         pr329-fix-detect-stdlib-modules.patch
BuildRequires:  golang(API) >= 1.19

%description
go-licenses analyzes the dependency tree of a Go package/binary. It can output a
report on the libraries used and under what license they can be used. It can
also collect all of the license documents, copyright notices and source code
into a directory in order to comply with license terms on redistribution.

%prep
%autosetup -a 1 -p 1

%build
%ifnarch ppc64
export GOFLAGS="-buildmode=pie"
%endif
go build

%check
# execute the binary as a basic check
./%{name} --help

%install
install -D -m 0755 %{name} "%{buildroot}/%{_bindir}/%{name}"

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%changelog
