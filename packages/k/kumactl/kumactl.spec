#
# spec file for package kumactl
#
# Copyright (c) 2025 SUSE LLC
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


Name:           kumactl
Version:        2.9.3
Release:        0
Summary:        CLI for the Kuma service mesh
License:        Apache-2.0
URL:            https://github.com/kumahq/kuma
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  bash-completion
BuildRequires:  fish
BuildRequires:  go >= 1.23.5
BuildRequires:  zsh

%description
Kuma is a modern Envoy-based service mesh that can run on every cloud, in a
single or multi-zone capacity, across both Kubernetes and VMs. Thanks to its
broad universal workload support, combined with native support for Envoy as its
data plane proxy technology (but with no Envoy expertise required), Kuma
provides modern L4-L7 service connectivity, discovery, security, observability,
routing and more across any service on any platform, databases included.

Easy to use, with built-in service mesh policies for security, traffic control,
discovery, observability and more, Kuma ships with an advanced multi-zone and
multi-mesh support that automatically enables cross-zone communication across
different clusters and clouds, and automatically propagates service mesh
policies across the infrastructure. Kuma is currently being adopted by
enterprise organizations around the world to support distributed service meshes
across the application teams, on both Kubernetes and VMs.

Originally created and donated by Kong, Kuma is today CNCF (Cloud Native
Computing Foundation) Sandbox project and therefore available with the same
openness and neutrality as every other CNCF project. Kuma has been engineered
to be both powerful yet simple to use, reducing the complexity of running a
service mesh across every organization with very unique capabilities like
multi-zone support, multi-mesh support, and a gradual and intuitive learning
curve.

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
COMMIT_HASH="$(sed -n 's/commit: \(.*\)/\1/p' %_sourcedir/%{name}.obsinfo)"

DATE_FMT="+%%Y-%%m-%%dT%%H:%%M:%%SZ"
BUILD_DATE=$(date -u -d "@${SOURCE_DATE_EPOCH}" "${DATE_FMT}" 2>/dev/null || date -u -r "${SOURCE_DATE_EPOCH}" "${DATE_FMT}" 2>/dev/null || date -u "${DATE_FMT}")

ENVOY_VERSION="$(awk -F '= ' '/^ENVOY_VERSION/ {print $2}' mk/dev.mk)"

go build \
   -mod=vendor \
   -buildmode=pie \
   -ldflags=" \
   -X github.com/kumahq/kuma/pkg/version.version=v%{version} \
   -X github.com/kumahq/kuma/pkg/version.gitTag=%{version} \
   -X github.com/kumahq/kuma/pkg/version.gitCommit=${COMMIT_HASH} \
   -X github.com/kumahq/kuma/pkg/version.buildDate=${BUILD_DATE} \
   -X github.com/kumahq/kuma/pkg/version.Envoy=${ENVOY_VERSION}" \
   -o bin/%{name} ./app/%{name}

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

%check
bin/%{name} version | grep "Client: Kuma v%{version}"

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
