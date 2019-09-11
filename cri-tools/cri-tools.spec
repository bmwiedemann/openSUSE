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


%define project         github.com/kubernetes-sigs/cri-tools
%define name_source1    crictl.yaml

Name:           cri-tools
Version:        1.15.0
Release:        0
Summary:        CLI and validation tools for Kubelet Container Runtime Interface
License:        Apache-2.0
Group:          System/Management
Url:            https://github.com/kubernetes-sigs/cri-tools
Source0:        %{name}-%{version}.tar.xz
Source1:        %{name_source1}
Source2:        rpmlintrc
BuildRequires:  go-go-md2man
BuildRequires:  golang-packaging
BuildRequires:  golang(API) >= 1.12
# disable stripping of binaries
%{go_nostrip}

%description
cri-tools provides a series of debugging and validation tools for
Kubelet CRI, which includes:
- crictl: CLI for kubelet CRI
- critest: validation test suites for kubelet CRI

%prep
%setup -q

%build
export GOPATH=$HOME/go
mkdir -pv $HOME/go/src/%{project}
rm -rf $HOME/go/src/%{project}/*
cp -avr * $HOME/go/src/%{project}
cd $HOME/go/src/%{project}

export BUILDMODE_ARGS="-buildmode=pie"
# the buildmode pie is currently not supported for ppc64
if [ %{_arch} = "ppc64" ]; then
    unset BUILDMODE_ARGS
fi

go build $BUILDMODE_ARGS \
         -o bin/crictl \
         -ldflags '-X %{project}/pkg/version.Version=%{version}' \
         %{project}/cmd/crictl

go test $BUILDMODE_ARGS \
        -o bin/critest \
        -ldflags '-X %{project}/pkg/version.Version=%{version}' \
        -c %{project}/cmd/critest


# compile the manpages
for md in docs/*.md
do
	go-md2man -in $md -out $md
done
rename '.md' '.1' docs/*

# generate auto-completions
./bin/crictl completion bash > crictl-completion-bash
./bin/crictl completion zsh > crictl-completion-zsh

%install
cd $HOME/go/src/%{project}
install -D -m 0755 bin/crictl %{buildroot}/%{_bindir}/crictl
install -D -m 0755 bin/critest %{buildroot}/%{_bindir}/critest
install -d %{buildroot}/%{_mandir}/man1
install -D -m 0644 docs/crictl.1 %{buildroot}/%{_mandir}/man1/crictl.1
install -D -m 0644 docs/benchmark.1 %{buildroot}/%{_mandir}/man1/critest-benchmark.1
install -D -m 0644 docs/validation.1 %{buildroot}/%{_mandir}/man1/critest-validation.1
install -D -m 0644 crictl-completion-bash %{buildroot}/%{_datadir}/bash-completion/completions/crictl
install -D -m 0644 crictl-completion-zsh %{buildroot}/%{_datadir}/zsh/site-functions/_crictl
install -D -m 0644 %{SOURCE1} %{buildroot}/%{_sysconfdir}/%{name_source1}

%files
%{_bindir}/crictl
%{_bindir}/critest
%{_mandir}/man1/*
%{_datadir}/bash-completion/completions/crictl
%{_datadir}/zsh
%config(noreplace) %{_sysconfdir}/%{name_source1}
%license LICENSE

%changelog
