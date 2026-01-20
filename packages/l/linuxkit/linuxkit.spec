#
# spec file for package linuxkit
#
# Copyright (c) 2026 SUSE LLC and contributors
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

Name:           linuxkit
Version:        1.8.2
Release:        0
Summary:        Toolkit for building secure, portable and lean operating systems for containers
License:        Apache-2.0
URL:            https://github.com/linuxkit/linuxkit
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  go >= 1.21

%description
LinuxKit, a toolkit for building custom minimal, immutable Linux distributions.

* Secure defaults without compromising usability
* Everything is replaceable and customisable
* Immutable infrastructure applied to building Linux distributions
* Completely stateless, but persistent storage can be attached
* Easy tooling, with easy iteration
* Built with containers, for running containers
* Designed to create reproducible builds [WIP]
* Designed for building and running clustered applications, including but not
  limited to container orchestration such as Docker or Kubernetes
* Designed from the experience of building Docker Editions, but redesigned as a
  general-purpose toolkit
* Designed to be managed by external tooling, such as Infrakit (renamed to
  deploykit which has been archived in 2019) or similar tools
* Includes a set of longer-term collaborative projects in various stages of
  development to innovate on kernel and userspace changes, particularly around
  security

LinuxKit currently supports the x86_64, arm64, and s390x architectures on a
variety of platforms, both as virtual machines and baremetal (see below for
details).

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
rm -rf src/cmd/linuxkit/vendor/
mv vendor/ src/cmd/linuxkit/

%build
COMMIT_HASH="$(sed -n 's/commit: \(.*\)/\1/p' %_sourcedir/%{name}.obsinfo)"

cd src/cmd/linuxkit/

go build \
   -mod=vendor \
   -buildmode=pie \
   -ldflags=" \
   -X github.com/linuxkit/linuxkit/src/cmd/linuxkit/version.GitCommit=${COMMIT_HASH} \
   -X github.com/linuxkit/linuxkit/src/cmd/linuxkit/version.Version=v%{version}" \
   -o bin/%{name}

%install
cd src/cmd/linuxkit/

# Install the binary.
install -D -m 0755 bin/%{name} %{buildroot}/%{_bindir}/%{name}

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
%dir %{_datarootdir}/zsh_completion.d/
%{_datarootdir}/zsh_completion.d/_%{name}

%changelog
