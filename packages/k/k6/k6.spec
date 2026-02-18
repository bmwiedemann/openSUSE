#
# spec file for package k6
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


Name:           k6
Version:        1.6.1
Release:        0
Summary:        Modern load testing tool, using Go and JavaScript
License:        AGPL-3.0
URL:            https://github.com/grafana/k6
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  bash-completion
BuildRequires:  fish
BuildRequires:  golang(API) >= 1.24
BuildRequires:  zsh

# # github.com/grafana/xk6-output-prometheus-remote/pkg/remote
# vendor/github.com/grafana/xk6-output-prometheus-remote/pkg/remote/client.go:131:35: cannot use math.MaxUint32 (untyped int constant 4294967295) as int value in argument to fmt.Errorf (overflows)
# # github.com/grafana/xk6-dashboard/dashboard
# vendor/github.com/grafana/xk6-dashboard/dashboard/sse.go:69:31: cannot use maxSafeInteger (untyped int constant 9007199254740991) as int value in argument to strconv.Itoa (overflows)
# # go.k6.io/k6/output/cloud/expv2
# output/cloud/expv2/metrics_client.go:89:35: cannot use 0xffffffff (untyped int constant 4294967295) as int value in argument to fmt.Errorf (overflows)
ExcludeArch:    %{ix86}

%description
k6 is a modern load-testing tool, built on our years of experience in the
performance and testing industries. It's built to be powerful, extensible, and
full-featured. The key design goal is to provide the best developer experience.

Its core features are:

- Configurable load generation. Even lower-end machines can simulate lots of
  traffic.
- Tests as code. Reuse scripts, modularize logic, version control, and
  integrate tests with your CI.
- A full-featured API. The scripting API is packed with features that help you
  simulate real application traffic.
- An embedded JavaScript engine. The performance of Go, the scripting
  familiarity of JavaScript.
- Multiple Protocol support. HTTP, WebSockets, gRPC, Browser, and more.
- Large extension ecosystem. You can extend k6 to support your needs. And many
  people have already shared their extensions with the community!
- Flexible metrics storage and visualization. Summary statistics or granular
  metrics, exported to the service of your choice.
- Native integration with Grafana cloud. SaaS solution for test execution,
  metrics correlation, data analysis, and more.

This is what load testing looks like in the 21st century.

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
   -o bin/%{name}

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
%doc README.md examples
%license LICENSE.md
%{_bindir}/%{name}

%files -n %{name}-bash-completion
%{_datarootdir}/bash-completion/completions/%{name}

%files -n %{name}-fish-completion
%{_datarootdir}/fish/vendor_completions.d/%{name}.fish

%files -n %{name}-zsh-completion
%{_datarootdir}/zsh/site-functions/_%{name}

%changelog
