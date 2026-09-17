#
# spec file for package protoc-gen-go-grpc
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


Name:           protoc-gen-go-grpc
Version:        1.78.0
Release:        0
Summary:        The Go language implementation of gRPC
License:        Apache-2.0
URL:            https://github.com/grpc/grpc-go
Source0:        %{name}-%{version}.tar.xz
Source1:        vendor.tar.xz
BuildRequires:  golang(API) >= 1.24

%description
The Go implementation of gRPC: A high performance, open source,
general RPC framework that puts mobile and HTTP/2 first.

%prep
%autosetup -a1 -p1

%build
# Upstream source has unusual layout where cmd/ has its own go.mod
mv vendor cmd/%{name}
pushd cmd/%{name}
%ifnarch ppc64
export GOFLAGS="-buildmode=pie"
%endif
%ifnarch s390x armv6l armv7l
export CGO_ENABLED=0
%endif
go build -ldflags="-X main.version=%{version}"
popd

%install
install -D -m 0755 -t %{buildroot}%{_bindir} cmd/%{name}/%{name}

%files
%doc README.md
%license LICENSE
%doc cmd/protoc-gen-go-grpc/README.md
%{_bindir}/%{name}

%changelog
