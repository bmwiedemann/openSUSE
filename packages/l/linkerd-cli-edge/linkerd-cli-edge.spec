#
# spec file for package linkerd-cli-edge
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


%define linkerd_executable_name linkerd

Name:           linkerd-cli-edge
Version:        24.11.3
Release:        0
Summary:        CLI for the linkerd service mesh for Kubernetes
License:        Apache-2.0
URL:            https://github.com/linkerd/linkerd2
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  bash-completion
BuildRequires:  fish
BuildRequires:  go >= 1.22
BuildRequires:  zsh

# cannot be installed in parallel to the stable version
Conflicts:      linkerd-cli

%description
The Linkerd CLI is the primary way to interact with Linkerd. It can install the
control plane to your cluster, add the proxy to your service and provide
detailed metrics for how your service is performing.

Linkerd is an ultralight, security-first service mesh for Kubernetes. Linkerd
adds critical security, observability, and reliability features to your
Kubernetes stack with no code change required.

Linkerd is a Cloud Native Computing Foundation (CNCF) project.

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
%autosetup -p 1 -a 1

%build
GO111MODULE=on go generate -mod=readonly ./pkg/charts/static
GO111MODULE=on go generate -mod=readonly ./jaeger/static
GO111MODULE=on go generate -mod=readonly ./multicluster/static
GO111MODULE=on go generate -mod=readonly ./viz/static
go build \
   -mod=vendor \
   -tags prod \
   -buildmode=pie \
   -ldflags="-X github.com/linkerd/linkerd2/pkg/version.Version=stable-%{version}" \
   -o bin/%{linkerd_executable_name} ./cli/

%install
# Install the binary.
install -D -m 0755 bin/%{linkerd_executable_name} %{buildroot}/%{_bindir}/%{linkerd_executable_name}

# create the bash completion file
mkdir -p %{buildroot}%{_datarootdir}/bash-completion/completions/
%{buildroot}/%{_bindir}/%{linkerd_executable_name} completion bash > %{buildroot}%{_datarootdir}/bash-completion/completions/%{name}

# create the fish completion file
mkdir -p %{buildroot}%{_datarootdir}/fish/vendor_completions.d/
%{buildroot}/%{_bindir}/%{linkerd_executable_name} completion fish > %{buildroot}%{_datarootdir}/fish/vendor_completions.d/%{name}.fish

# create the zsh completion file
mkdir -p %{buildroot}%{_datarootdir}/zsh/site-functions/
%{buildroot}/%{_bindir}/%{linkerd_executable_name} completion zsh > %{buildroot}%{_datarootdir}/zsh/site-functions/_%{name}

%files
%doc README.md
%license LICENSE
%{_bindir}/%{linkerd_executable_name}

%files -n %{name}-bash-completion
%{_datarootdir}/bash-completion/completions/%{name}

%files -n %{name}-fish-completion
%{_datarootdir}/fish/vendor_completions.d/%{name}.fish

%files -n %{name}-zsh-completion
%{_datarootdir}/zsh/site-functions/_%{name}

%changelog
