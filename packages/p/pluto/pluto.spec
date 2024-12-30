#
# spec file for package pluto
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


Name:           pluto
Version:        5.21.0
Release:        0
Summary:        A cli tool to help discover deprecated apiVersions in Kubernetes
License:        Apache-2.0
URL:            https://github.com/FairwindsOps/pluto
Source:         pluto-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  bash-completion
BuildRequires:  fish
BuildRequires:  go >= 1.22
BuildRequires:  zsh

%description
Pluto is a utility to help users find deprecated Kubernetes apiVersions in
their code repositories and their helm releases.

%package bash-completion
Summary:        Bash Completion for %{name}
Requires:       %{name} = %{version}
Supplements:    (%{name} and bash-completion)
BuildArch:      noarch

%description bash-completion
Bash command line completion support for %{name}.

%package zsh-completion
Summary:        Zsh Completion for %{name}
Requires:       %{name} = %{version}
Supplements:    (%{name} and zsh)
BuildArch:      noarch

%description zsh-completion
Zsh command line completion support for %{name}.

%package fish-completion
Summary:        Fish Completion for %{name}
Requires:       %{name} = %{version}
Supplements:    (%{name} and fish)
BuildArch:      noarch

%description fish-completion
Fish command line completion support for %{name}.

%prep
%autosetup -p 1 -a 1

%build
COMMIT_HASH="$(sed -n 's/commit: \(.*\)/\1/p' %_sourcedir/%{name}.obsinfo)"

go build \
   -mod=vendor \
   -buildmode=pie \
   -ldflags=" \
   -X main.version=%{version} \
   -X main.commit=${COMMIT_HASH}" \
   -o bin/pluto ./cmd/pluto/

%install
# Install the binary.
install -D -m 0755 ./bin/%{name} %{buildroot}/%{_bindir}/%{name}
mkdir -p %{buildroot}%{_datarootdir}/bash-completion/completions
%{buildroot}/%{_bindir}/%{name} completion bash > %{buildroot}%{_datarootdir}/bash-completion/completions/%{name}
mkdir -p %{buildroot}%{_datarootdir}/zsh/site-functions
%{buildroot}/%{_bindir}/%{name} completion zsh > %{buildroot}%{_datarootdir}/zsh/site-functions/_%{name}
mkdir -p %{buildroot}%{_datadir}/fish/vendor_completions.d
%{buildroot}/%{_bindir}/%{name} completion fish > %{buildroot}%{_datarootdir}/fish/vendor_completions.d/%{name}.fish

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%files bash-completion
%{_datarootdir}/bash-completion/completions/%{name}

%files zsh-completion
%{_datarootdir}/zsh/site-functions/_%{name}

%files fish-completion
%{_datarootdir}/fish/vendor_completions.d/%{name}.fish

%changelog
