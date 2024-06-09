#
# spec file for package hubble
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

Name:           hubble
Version:        0.13.5
Release:        0
Summary:        Network, Service & Security Observability for Kubernetes using eBPF
License:        Apache-2.0
URL:            https://github.com/cilium/hubble
Source:         hubble-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  go >= 1.22

%description
Hubble is a fully distributed networking and security observability platform
for cloud native workloads. It is built on top of Cilium and eBPF to enable
deep visibility into the communication and behavior of services as well as the
networking infrastructure in a completely transparent manner.

Hubble can answer questions such as:
  * Service dependencies & communication map:
    - What services are communicating with each other? How frequently? What
      does the service dependency graph look like?
    - What HTTP calls are being made? What Kafka topics does a service consume
      from or produce to?
  * Operational monitoring & alerting:
    - Is any network communication failing? Why is communication failing? Is it
      DNS? Is it an application or network problem? Is the communication broken
      on layer 4 (TCP) or layer 7 (HTTP)?
    - Which services have experienced a DNS resolution problems in the last 5
      minutes? Which services have experienced an interrupted TCP connection
      recently or have seen connections timing out? What is the rate of unanswered
      TCP SYN requests?
  * Application monitoring:
    - What is the rate of 5xx or 4xx HTTP response codes for a particular
      service or across all clusters?
    - What is the 95th and 99th percentile latency between HTTP requests and
      responses in my cluster? Which services are performing the worst? What is
      the latency between two services?
  * Security observability:
    - Which services had connections blocked due to network policy? What
      services have been accessed from outside the cluster? Which services have
      resolved a particular DNS name?

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
COMMIT_HASH="$(sed -n 's/commit: \(.*\)/\1/p' %_sourcedir/hubble.obsinfo)"
go build \
   -mod=vendor \
   -buildmode=pie \
   -ldflags=" \
   -X github.com/cilium/hubble/pkg.GitBranch=main \
   -X github.com/cilium/hubble/pkg.GitHash=${COMMIT_HASH:0:8} \
   -X github.com/cilium/hubble/pkg.Version=%{version}" \
   -o bin/hubble .

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
