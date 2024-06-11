#
# spec file for package mesheryctl
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

Name:           mesheryctl
Version:        0.7.72
Release:        0
Summary:        CLI for the meshery cloud native management plane
License:        Apache-2.0
URL:            https://github.com/meshery/meshery
Source:         meshery-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  go >= 1.19

%description
Meshery manages the provisioning, configuration and operation of your Kubernetes clusters, workloads, and service meshes. While supporting hundreds of different types of cloud native infrastructure integrations.

Meshery also offers a catalog of curated design templates filled with configuration best practices.

Using a GitOps-centric approach, visually and collaboratively design and manage your infrastructure and microservices. Use Meshery to interoperate your various cloud native systems. With both REST and GraphQL APIs, integrating with Meshery as an extensible platform is facilitated through NATS, CloudEvents, gRPC, Service Mesh Interface (SMI), and Service Mesh Performance (SMP).

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
%autosetup -p1 -a 1 -n meshery-%{version}

%build
go build \
   -mod=vendor \
   -buildmode=pie \
   -ldflags="-X github.com/layer5io/meshery/mesheryctl/internal/cli/root/constants.version=v%{version} \
   -X github.com/layer5io/meshery/mesheryctl/internal/cli/root/constants.commitsha=v%{version} \
   -X github.com/layer5io/meshery/mesheryctl/internal/cli/root/constants.releasechannel=stable" \
   -o bin/mesheryctl ./mesheryctl/cmd/mesheryctl/main.go

%install
# Install the binary.
install -D -m 0755 bin/%{name} "%{buildroot}/%{_bindir}/%{name}"

# create the bash completion file
mkdir -p %{buildroot}%{_datarootdir}/bash-completion/completions/
%{buildroot}/%{_bindir}/%{name} completion bash > %{buildroot}%{_datarootdir}/bash-completion/completions/%{name}

# create the fish completion file
mkdir -p %{buildroot}%{_datarootdir}/fish/vendor_completions.d/
%{buildroot}/%{_bindir}/%{name} completion fish > %{buildroot}%{_datarootdir}/fish/vendor_completions.d/%{name}.fish

# create the zsh completion file
mkdir -p %{buildroot}%{_datarootdir}/zsh_completion.d/
%{buildroot}/%{_bindir}/%{name} completion zsh > %{buildroot}%{_datarootdir}/zsh_completion.d/_%{name}

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%files -n %{name}-bash-completion
%dir %{_datarootdir}/bash-completion/completions/
%{_datarootdir}/bash-completion/completions/%{name}

%files -n %{name}-fish-completion
%dir %{_datarootdir}/fish
%dir %{_datarootdir}/fish/vendor_completions.d
%{_datarootdir}/fish/vendor_completions.d/%{name}.fish

%files -n %{name}-zsh-completion
%defattr(-,root,root)
%dir %{_datarootdir}/zsh_completion.d/
%{_datarootdir}/zsh_completion.d/_%{name}

%changelog
