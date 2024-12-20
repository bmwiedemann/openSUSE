#
# spec file for package delve
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


%define shortname dlv

Name:           delve
Version:        1.24.0
Release:        0
Summary:        Debugger for the Go Programming Language
License:        MIT
Group:          Development/Languages/Go
URL:            https://github.com/go-delve/delve
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  golang(API) >= 1.17
# your_linux_architecture_is_not_supported_by_delve (support_sentinel_linux.go)
ExcludeArch:    s390x ppc64 ppc64le %arm riscv64

%description
Delve is a debugger for the Go programming language. The goal of
the project is to provide a simple, full featured debugging tool
for Go. Delve should be easy to invoke and easy to use. Chances are
if you're using a debugger, things aren't going your way. With that
in mind, Delve should stay out of your way as much as possible.

%prep
%autosetup -a 1

%build
%ifnarch ppc64
export GOFLAGS="-buildmode=pie"
%endif
go build \
   ./cmd/%{shortname}

%check
# execute the binary as a basic check
./%{shortname} --help

%install
install -D -m 0755 %{shortname} "%{buildroot}/%{_bindir}/%{shortname}"

%files
%doc README.md
%doc Documentation
%license LICENSE
%{_bindir}/%{shortname}

%changelog
