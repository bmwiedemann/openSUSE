#
# spec file for package cri-tools
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

%define executable_name crictl

Name:           cri-tools
Version:        1.34.0
Release:        0
Summary:        CLI and validation tools for Kubelet Container Runtime Interface
License:        Apache-2.0
Group:          System/Management
Url:            https://github.com/kubernetes-sigs/cri-tools
Source0:        %{name}-%{version}.tar.xz
Source1:        vendor.tar.gz
Source2:        rpmlintrc
Source11:       crictl.yaml
BuildRequires:  go-go-md2man
BuildRequires:  golang(API) >= 1.24
BuildRequires:  bash-completion
BuildRequires:  fish
BuildRequires:  zsh

%description
cri-tools provides a series of debugging and validation tools for
Kubelet CRI, which includes:

- crictl: CLI for kubelet CRI
- critest: validation test suites for kubelet CRI

%prep
%autosetup -a 1

%build
%ifnarch ppc64
export GOFLAGS="-buildmode=pie"
%endif
go build -o bin/%{executable_name} ./cmd/%{executable_name}
go test -o bin/critest -c ./cmd/critest

# compile the manpage
go-md2man -in docs/%{executable_name}.md -out docs/%{executable_name}.1

%install
install -D -m 0755 bin/%{executable_name} %{buildroot}/%{_bindir}/%{executable_name}
install -D -m 0755 bin/critest %{buildroot}/%{_bindir}/critest

# create the bash completion file
mkdir -p %{buildroot}%{_datarootdir}/bash-completion/completions/
%{buildroot}/%{_bindir}/%{executable_name} completion bash > %{buildroot}%{_datarootdir}/bash-completion/completions/%{executable_name}

# create the fish completion file
mkdir -p %{buildroot}%{_datarootdir}/fish/vendor_completions.d/
%{buildroot}/%{_bindir}/%{executable_name} completion fish > %{buildroot}%{_datarootdir}/fish/vendor_completions.d/%{executable_name}.fish

# create the zsh completion file
mkdir -p %{buildroot}%{_datarootdir}/zsh/site-functions/
%{buildroot}/%{_bindir}/%{executable_name} completion zsh > %{buildroot}%{_datarootdir}/zsh/site-functions/_%{executable_name}

install -d %{buildroot}/%{_mandir}/man1
install -D -m 0644 docs/%{executable_name}.1 %{buildroot}/%{_mandir}/man1/
install -D -m 0644 %{SOURCE11} %{buildroot}/%{_sysconfdir}/crictl.yaml

%files
%doc README.md
%license LICENSE
%{_bindir}/%{executable_name}
%{_bindir}/critest
%config(noreplace) %{_sysconfdir}/crictl.yaml

%{_mandir}/man1/*

%{_datarootdir}/bash-completion/completions/%{executable_name}
%{_datarootdir}/fish/vendor_completions.d/%{executable_name}.fish
%{_datarootdir}/zsh/site-functions/_%{executable_name}

%changelog
