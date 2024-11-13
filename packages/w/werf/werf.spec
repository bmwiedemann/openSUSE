#
# spec file for package werf
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


Name:           werf
Version:        2.12.1
Release:        0
Summary:        CLI for the Werf CI/CD system
License:        Apache-2.0
URL:            https://github.com/werf/werf
Source:         werf-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  bash-completion
BuildRequires:  fish
BuildRequires:  go >= 1.22.7
BuildRequires:  zsh
#
BuildRequires:  device-mapper-devel
BuildRequires:  libbtrfs-devel
BuildRequires:  libcontainers-common
BuildRequires:  libgpgme-devel

%description
werf is a CNCF Sandbox CLI tool to implement full-cycle CI/CD to Kubernetes easily. werf integrates into your CI system and leverages familiar and reliable technologies, such as Git, Dockerfile, Helm, and Buildah.

What makes werf special:
* Complete application lifecycle management: build and publish container images, test, deploy an application to Kubernetes, distribute release artifacts and clean up the container registry.
* Ease of use: use Dockerfiles and Helm chart for configuration and let werf handle all the rest.
* Advanced features: automatic build caching and content-based tagging, enhanced resource tracking and extra capabilities in Helm, a unique container registry cleanup approach, and more.
* Gluing common technologies: Git, Buildah, Helm, Kubernetes, and your CI system of choice.
* Production-ready: werf has been used in production since 2017; thousands of projects rely on it to build & deploy various apps.

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
go build \
   -mod=vendor \
   -buildmode=pie \
   -ldflags="-X github.com/werf/werf/v2/pkg/werf.Version=%{version}" \
   -tags="dfrunsecurity dfrunnetwork dfrunmount dfssh containers_image_openpgp osusergo exclude_graphdriver_devicemapper netgo no_devmapper static_build" \
   -o bin/werf ./cmd/werf

%install
# Install the binary.
install -D -m 0755 bin/%{name} %{buildroot}/%{_bindir}/%{name}

# create the bash completion file
mkdir -p %{buildroot}%{_datarootdir}/bash-completion/completions/
%{buildroot}/%{_bindir}/%{name} completion bash > %{buildroot}%{_datarootdir}/bash-completion/completions/%{name}

# create the fish completion file
mkdir -p %{buildroot}%{_datarootdir}/fish/vendor_completions.d/
%{buildroot}/%{_bindir}/%{name} completion fish > %{buildroot}%{_datarootdir}/fish/vendor_completions.d/%{name}.fish

# create the zsh completion file
mkdir -p %{buildroot}%{_datarootdir}/zsh/site-functions/
%{buildroot}/%{_bindir}/%{name} completion zsh > %{buildroot}%{_datarootdir}/zsh/site-functions/_%{name}

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%files -n %{name}-bash-completion
%{_datarootdir}/bash-completion/completions/%{name}

%files -n %{name}-fish-completion
%{_datarootdir}/fish/vendor_completions.d/%{name}.fish

%files -n %{name}-zsh-completion
%{_datarootdir}/zsh/site-functions/_%{name}

%changelog
