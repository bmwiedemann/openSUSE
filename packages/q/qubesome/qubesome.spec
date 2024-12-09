#
# spec file for package qubesome
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


Name:           qubesome
Version:        0.0.8
Release:        0
Summary:        Containerize Window Managers, apps and config from a declarative state in Git
License:        Apache-2.0
Group:          System/X11/Utilities
URL:            https://github.com/qubesome/cli
Source0:        %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  golang(API) >= 1.23

%description
Define your Window Manager and Workloads in Git and run them as containers. Just like dotfiles management, but better.

%prep
%autosetup -a 1

%build -n %{project}-%{version}
%ifnarch ppc64
export GOFLAGS="-buildmode=pie"
%endif
go build -o %{name} cmd/qubesome/main.go

%check
# execute the binary as a basic check
./%{name} deps

%install
install -D -m 0755 %{name} "%{buildroot}/%{_bindir}/%{name}"

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%changelog
