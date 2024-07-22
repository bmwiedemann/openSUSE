#
# spec file for package go-passbolt-cli
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


Name:           go-passbolt-cli
Version:        0.3.1
Release:        0
Summary:        A CLI tool to interact with Passbolt
License:        MIT
Group:          Productivity/Security
URL:            https://github.com/passbolt/go-passbolt-cli
Source0:        %{name}-%{version}.tar.xz
Source1:        vendor.tar.gz
BuildRequires:  golang(API) >= 1.21

%define bin_name passbolt

%description
This package provides a CLI tool to interact with Passbolt, An Open Source Password Manager for Teams

Passbolt Website: https://www.passbolt.com/

This project is community driven and not associated with Passbolt SA

%package bash-completion
Summary:        Bash Completion for %{name}
Group:          System/Shells
Requires:       bash-completion
BuildArch:      noarch
Requires:       %{name}
Supplements:    (%{name} and bash-completion)

%description bash-completion
The official bash completion script for %{name}, generated during the build.

%package zsh-completion
Summary:        ZSH Completion for %{name}
Group:          System/Shells
BuildArch:      noarch
Requires:       %{name}
Supplements:    (%{name} and zsh)

%description zsh-completion
The official zsh completion script for %{name}, generated during the build.

%package fish-completion
Summary:        Fish Completion for %{name}
Group:          System/Shells
BuildArch:      noarch
Requires:       %{name}
Supplements:    (%{name} and fish)

%description fish-completion
The official fish completion script for %{name}, generated during the build.

%prep
%autosetup -a1

%build
# Renaming the binary, As upsteam prefers to use it in examples
# See: https://github.com/passbolt/go-passbolt-cli?tab=readme-ov-file#getting-started
go build \
   -buildmode=pie \
   -ldflags "-s -w" \
   -o %{bin_name}

# Build the shell autocomplete files
./%{bin_name} completion bash > %{name}-autocomplete.bash
./%{bin_name} completion zsh > %{name}-autocomplete.zsh
./%{bin_name} completion fish > %{name}-autocomplete.fish

# generate man pages
mkdir man && ./%{bin_name} gendoc --type man

%install

# install the binary
install -D -m 0755 %{bin_name} "%{buildroot}%{_bindir}/%{bin_name}"

# Install the shell autocomplete files
install -Dm 644 %{name}-autocomplete.bash %{buildroot}%{_datadir}/bash-completion/completions/%{name}
install -Dm 644 %{name}-autocomplete.zsh %{buildroot}%{_datadir}/zsh/site-functions/_%{name}
install -Dm 644 %{name}-autocomplete.fish %{buildroot}%{_datadir}/fish/completions/_%{name}

# Install the man pages.
mkdir -p "%{buildroot}%{_mandir}/man1"
install -D -m 0644 man/*.1 "%{buildroot}%{_mandir}/man1"

%check
./%{bin_name} -v

%files
%license LICENSE
%doc README.md

%{_bindir}/%{bin_name}
%{_mandir}/man1/%{bin_name}*.1.gz

%files bash-completion
%{_datadir}/bash-completion

%files zsh-completion
%{_datadir}/zsh

%files fish-completion
%{_datadir}/fish

%changelog
