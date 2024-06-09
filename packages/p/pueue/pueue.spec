#
# spec file for package pueue
#
# Copyright (c) 2020 SUSE LLC
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

Name:           pueue
Version:        3.4.1
Release:        0
Summary:        Command-line task management tool for sequential and parallel execution
License:        MIT
URL:            https://github.com/Nukesor/pueue
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
BuildRequires:  cargo-packaging
# Completions
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  zsh
BuildRequires:  fish

%description
Pueue is a command-line task management tool for sequential and parallel execution of long-running tasks.
It's a tool that processes a queue of shell commands.
Since Pueue is not bound to any terminal, you can control your tasks from any terminal on the same machine.
The queue will be continuously processed, even if you no longer have any active ssh sessions.

%package fish-completion
Summary:        Fish Completion for %{name}
Supplements:    (%{name} and fish)
Requires:       %{name} = %{version}
BuildArch:      noarch

%description fish-completion
The official fish completion script for %{name}.

%package bash-completion
Summary:        Fish Completion for %{name}
Supplements:    (%{name} and bash-completion)
Requires:       %{name} = %{version}
BuildArch:      noarch

%description bash-completion
The official bash completion script for %{name}.

%package zsh-completion
Summary:        Fish Completion for %{name}
Supplements:    (%{name} and zsh)
Requires:       %{name} = %{version}
BuildArch:      noarch

%description zsh-completion
The official zsh completion script for %{name}.

%prep
%autosetup -a1

%build
%{cargo_build}

# Generate completions
for shell in bash fish zsh; do
  ./target/release/pueue completions ${shell} .
done

%check
%{cargo_test}

%install
install -D -m 0755 target/release/%{name} %{buildroot}%{_bindir}/%{name}
install -D -m 0755 target/release/%{name}d %{buildroot}%{_bindir}/%{name}d

#Install shell completion
install -Dm 0644 %{name}.bash %{buildroot}/%{_datadir}/bash-completion/completions/%{name}
install -Dm 0644 %{name}.fish %{buildroot}/%{_datadir}/fish/vendor_completions.d/%{name}.fish
install -Dm 0644 _%{name} %{buildroot}/%{_datadir}/zsh/site-functions/_%{name}

# Install user service
install -Dm644 utils/%{name}d.service %{buildroot}%{_userunitdir}/%{name}d.service

%files
%license LICENSE
%doc README.md CHANGELOG.md
%{_bindir}/%{name}
%{_bindir}/%{name}d
%{_userunitdir}/%{name}d.service

%files bash-completion
%{_datadir}/bash-completion

%files fish-completion
%{_datadir}/fish

%files zsh-completion
%{_datadir}/zsh

%changelog

