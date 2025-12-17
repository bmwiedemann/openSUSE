#
# spec file for package nelm
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           nelm
Version:        1.18.0
Release:        0
Summary:        Helm 3 alternative
License:        Apache-2.0
URL:            https://github.com/werf/nelm
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  bash-completion
BuildRequires:  fish
BuildRequires:  zsh
BuildRequires:  golang(API) >= 1.23

%description
Nelm is a Helm 3 alternative. It is a Kubernetes deployment tool that manages
Helm Charts and deploys them to Kubernetes and also is the deployment engine of
werf. It can do (almost) everything that Helm does, but better, and even quite
some on top of it. Nelm is based on improved and partially rewritten Helm 3
codebase, to introduce:

* terraform plan-like capabilities;
* replacement of 3-Way Merge with Server-Side Apply;
* secrets management;
* advanced resource ordering capabilities;
* improved resource state/error tracking;
* continuous printing of logs, events, resource statuses and errors during
  deploy;
* lots of fixes for Helm 3 bugs, e.g. "no matches for kind Deployment in
  version apps/v1beta1";
* ... and more.

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
Requires:       fish
Supplements:    (%{name} and fish)
BuildArch:      noarch

%description -n %{name}-fish-completion
Fish command line completion support for %{name}.

%package -n %{name}-zsh-completion
Summary:        Zsh Completion for %{name}
Group:          System/Shells
Requires:       %{name} = %{version}
Requires:       zsh
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
   -ldflags=" \
   -X github.com/werf/nelm/internal/common.Brand=Nelm \
   -X github.com/werf/nelm/internal/common.Version=%{version}" \
   -o bin/%{name} ./cmd/%{name}

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
