#
# spec file for package tinygo
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
# nodebuginfo


%define __arch_install_post export NO_BRP_STRIP_DEBUG=true

Name:           tinygo
Version:        0.33.0
Release:        0
Summary:        Go toolchain targeting embedded devices and webassembly
License:        Apache-2.0
Group:          Development/Languages/Go
URL:            https://tinygo.org
Source:         tinygo-%{version}.tar.gz
Source1:        vendor.tar.gz
Patch0:         go-llvm-makefile-llvm-config.patch
BuildRequires:  clang18-devel
BuildRequires:  gcc-c++
BuildRequires:  llvm18-devel
BuildRequires:  golang(API) >= 1.18
# for test:
BuildRequires:  nodejs >= 20

%description
TinyGo brings the Go programming language to embedded systems and to the modern
web by creating a new compiler based on LLVM.

You can compile and run TinyGo programs on over 85 different microcontroller
boards such as the BBC micro:bit and the Arduino Uno.

TinyGo can also produce WebAssembly (WASM) code which is very compact in size.
You can compile programs for web browsers, as well as for server and edge
computing environments that support the WebAssembly System Interface (WASI)
family of interfaces.

https://tinygo.org

%prep
%setup -q -a 1
%patch 0 -p1

%build
go build \
   -mod=vendor \
   -buildmode=pie

%check

export LDFLAGS="-lLLVM -lclang"
export CGO_LDFLAGS="-lLLVM -lclang"
make test || true

%install
install -D -m 0755 %{name} "%{buildroot}/%{_bindir}/%{name}"

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%changelog
