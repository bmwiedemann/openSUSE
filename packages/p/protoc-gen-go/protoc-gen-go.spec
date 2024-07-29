#
# spec file for package protoc-gen-go
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


Name:           protoc-gen-go
Version:        1.34.2
Release:        0
Summary:        Go support for Google's protocol buffers
License:        BSD-3-Clause
Group:          Development/Languages/Go
URL:            https://github.com/golang/protobuf
Source:         %{name}-%{version}.tar.xz
Source1:        vendor.tar.xz
BuildRequires:  golang(API) >= 1.17

%description
protoc-gen-go implements Go bindings for protocol buffers. For information
about protocol buffers themselves, see
https://developers.google.com/protocol-buffers/

%prep
%autosetup -a 1

%build
%ifnarch ppc64
export GOFLAGS="-buildmode=pie"
%endif
go build ./cmd/%{name}

%check
# execute the binary as a basic check
./%{name} --help

%install
install -D -m0755 %{name} %{buildroot}%{_bindir}/%{name}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%changelog
