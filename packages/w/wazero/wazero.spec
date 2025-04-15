#
# spec file for package wazero
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


Name:           wazero
Version:        1.9.0
Release:        0
Summary:        CLI tool and library to compile and run WebAssembly
License:        Apache-2.0
Group:          Development/Languages/Go
URL:            https://github.com/tetratelabs/wazero
Source:         %{name}-%{version}.tar.gz
BuildRequires:  golang(API) >= 1.22

%description
wazero is a WebAssembly Core Specification 1.0 and 2.0 compliant runtime written
in Go. It has zero dependencies, and doesn't rely on CGO. This means you can run
applications in other languages and still keep cross compilation.

%prep
%autosetup

%build
%ifnarch ppc64
export GOFLAGS="-buildmode=pie"
%endif
go build ./cmd/%{name}

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
