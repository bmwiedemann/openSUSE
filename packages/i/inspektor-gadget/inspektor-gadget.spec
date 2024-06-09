#
# spec file for package inspektor-gadget
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


%define __arch_install_post export NO_BRP_STRIP_DEBUG=true

Name:           inspektor-gadget
Version:        0.29.0
Release:        0
Summary:        A eBPF tool and systems inspection framework
License:        Apache-2.0
URL:            https://github.com/inspektor-gadget/inspektor-gadget
Source:         inspektor-gadget-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  go1.22
# /usr/bin/ig conflicts with igrep
Conflicts:      igrep

%description
The eBPF tool and systems inspection framework for Kubernetes, containers and
Linux hosts

Inspektor Gadget is a collection of tools (or gadgets) to debug and inspect
Kubernetes resources and applications. It manages the packaging, deployment and
execution of eBPF programs in a Kubernetes cluster, including many based on BCC
tools, as well as some developed specifically for use in Inspektor Gadget. It
automatically maps low-level kernel primitives to high-level Kubernetes
resources, making it easier and quicker to find the relevant information.

%package -n %{name}-bash-completion
Summary:        Bash Completion for %{name}
Group:          System/Shells
Requires:       %{name} = %{version}
Requires:       bash-completion
Supplements:    (%{name} and bash-completion)
BuildArch:      noarch

%description -n %{name}-bash-completion
Bash command line completion support for %{name}.

%package -n %{name}-fish-completion
Summary:        Fish Completion for %{name}
Group:          System/Shells
Requires:       %{name} = %{version}
Supplements:    (%{name} and fish)
BuildArch:      noarch

%description -n %{name}-fish-completion
Fish command line completion support for %{name}.

%package -n %{name}-zsh-completion
Summary:        Zsh Completion for %{name}
Group:          System/Shells
Requires:       %{name} = %{version}
Supplements:    (%{name} and zsh)
BuildArch:      noarch

%description -n %{name}-zsh-completion
zsh command line completion support for %{name}.

%prep
%autosetup -a 1 -p 1

%build
go build \
   -mod=vendor \
   -buildmode=pie \
   -ldflags=" \
   -X github.com/inspektor-gadget/inspektor-gadget/internal/version.version=%{version} \
   -X main.gadgetimage=ghcr.io/inspektor-gadget/inspektor-gadget:latest" \
   -tags withoutebpf \
   -o bin/kubectl-gadget \
   github.com/inspektor-gadget/inspektor-gadget/cmd/kubectl-gadget

go build \
   -mod=vendor \
   -buildmode=pie \
   -tags withoutebpf \
   -ldflags=" \
   -X github.com/inspektor-gadget/inspektor-gadget/internal/version.version=%{version} \
   -X main.gadgetimage=ghcr.io/inspektor-gadget/inspektor-gadget:latest" \
   -o bin/gadgetctl \
   github.com/inspektor-gadget/inspektor-gadget/cmd/gadgetctl

go build \
   -mod=vendor \
   -buildmode=pie \
   -ldflags=" \
   -X github.com/inspektor-gadget/inspektor-gadget/internal/version.version=%{version} \
   -X github.com/inspektor-gadget/inspektor-gadget/cmd/common/image.builderImage=ghcr.io/inspektor-gadget/ebpf-builder:latest" \
   -tags netgo \
   -o bin/ig \
   github.com/inspektor-gadget/inspektor-gadget/cmd/ig

%install
# Install the binary.
install -D -m 0755 bin/kubectl-gadget %{buildroot}/%{_bindir}/kubectl-gadget
install -D -m 0755 bin/gadgetctl %{buildroot}/%{_bindir}/gadgetctl
install -D -m 0755 bin/gadgetctl %{buildroot}/%{_bindir}/ig

# create the bash completion file
mkdir -p %{buildroot}%{_datarootdir}/bash-completion/completions/
%{buildroot}/%{_bindir}/gadgetctl completion bash > %{buildroot}%{_datarootdir}/bash-completion/completions/gadgetctl
%{buildroot}/%{_bindir}/kubectl-gadget completion bash > %{buildroot}%{_datarootdir}/bash-completion/completions/kubectl-gadget

# create the fish completion file
mkdir -p %{buildroot}%{_datarootdir}/fish/vendor_completions.d/
%{buildroot}/%{_bindir}/gadgetctl completion fish > %{buildroot}%{_datarootdir}/fish/vendor_completions.d/gadgetctl.fish
%{buildroot}/%{_bindir}/kubectl-gadget completion fish > %{buildroot}%{_datarootdir}/fish/vendor_completions.d/kubectl-gadget.fish

# create the zsh completion file
mkdir -p %{buildroot}%{_datarootdir}/zsh_completion.d/
%{buildroot}/%{_bindir}/gadgetctl completion zsh > %{buildroot}%{_datarootdir}/zsh_completion.d/_gadgetctl
%{buildroot}/%{_bindir}/kubectl-gadget completion zsh > %{buildroot}%{_datarootdir}/zsh_completion.d/_kubectl-gadget

%files
%doc README.md
%license LICENSE
%{_bindir}/gadgetctl
%{_bindir}/ig
%{_bindir}/kubectl-gadget

%files -n %{name}-bash-completion
%dir %{_datarootdir}/bash-completion/completions/
%{_datarootdir}/bash-completion/completions/gadgetctl
%{_datarootdir}/bash-completion/completions/kubectl-gadget

%files -n %{name}-fish-completion
%dir %{_datarootdir}/fish
%dir %{_datarootdir}/fish/vendor_completions.d
%{_datarootdir}/fish/vendor_completions.d/gadgetctl.fish
%{_datarootdir}/fish/vendor_completions.d/kubectl-gadget.fish

%files -n %{name}-zsh-completion
%defattr(-,root,root)
%dir %{_datarootdir}/zsh_completion.d/
%{_datarootdir}/zsh_completion.d/_gadgetctl
%{_datarootdir}/zsh_completion.d/_kubectl-gadget

%changelog
