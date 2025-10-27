#
# spec file for package tinygo
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
# nodebuginfo


Name:           tinygo
Version:        0.39.0
Release:        0
Summary:        Go toolchain targeting embedded devices and webassembly
License:        Apache-2.0
Group:          Development/Languages/Go
URL:            https://tinygo.org
Source:         tinygo-%{version}.tar.gz
Source1:        vendor.tar.gz
# extracted from llvm19 sources because we need .c files at runtime:
Source2:        llvm-compiler-rt-builtins.tar.gz
Source3:        tinygo.rpmlintrc
Patch0:         go-llvm-makefile-llvm-config.patch
Requires:       clang20
Requires:       go1.25
Requires:       lld20
BuildRequires:  clang20-devel
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  llvm20-devel
BuildRequires:  golang(API) >= 1.19
# for test:
BuildRequires:  lld20
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
%autosetup -p1 -a1
tar xf %{S:2}

%build
%ifnarch ppc64
export GOFLAGS="-buildmode=pie"
%endif
go build

%check
cat >hello.go <<EOF
package main
import "fmt"
func main() {
   fmt.Println("hello world")
}
EOF
export TINYGOROOT=%{buildroot}%{_datadir}/%{name}
# Native test compile on supported architectures
%ifarch %ix86 x86_64 %arm aarch64
%{buildroot}%{_bindir}/%{name} build hello.go
./hello
%else
GOARCH=amd64 %{buildroot}%{_bindir}/%{name} build hello.go
%endif
export LDFLAGS="-lLLVM -lclang"
export CGO_LDFLAGS="-lLLVM -lclang"
make test || true

%install
install -D -m 0755 %{name} "%{buildroot}%{_bindir}/%{name}"
mkdir -p %{buildroot}%{_datadir}/%{name}/lib
cp -a --parents src lib/{musl,compiler-rt-builtins,bdwgc} %{buildroot}%{_datadir}/%{name}/
cp -a targets %{buildroot}%{_datadir}/%{name}/
# make rpmlint happy:
find %{buildroot}%{_datadir}/%{name}/ -iname '.[a-z]*' -type f -delete # drop hidden files
rm -rf %{buildroot}%{_datadir}/%{name}/lib/musl/{tools,configure}
%fdupes %{buildroot}%{_datadir}/%{name}/

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/%{name}

%changelog
