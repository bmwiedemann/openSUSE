#
# spec file for package mcphost
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
%global provider github
%global provider_tld com
%global project mark3labs
%global repo mcphost
%global import_path %{provider}.%{provider_tld}/%{project}/%{repo}
%global name %{provider}-%{provider_tld}-%{project}-%{repo}
%{!?goprep: %define goprep go version #}
%{!?gobuild: %define gobuild go build -buildmode=pie -mod=vendor}
%{!?goinstall: %define goinstall install -D -m 0755 %{repo} %{buildroot}%{_bindir}/%{repo}}

Name:           %repo
Version:        0.31.1
Release:        4.mge
Summary:        A CLI host application for the Model Context Protocol (MCP)
License:        MIT and Apache-2.0 and BSD-2-Clause and BSD-3-Clause
URL:            https://github.com/mark3labs/mcphost
Source0:        https://%{import_path}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}-%{version}-vendor.tar.gz
BuildRequires:  go >= 1.24
%if 0%{?suse_version} >= 1500
BuildRequires:  golang-packaging
%endif

%description
A CLI host application that enables Large Language Models (LLMs) to interact
with external tools through the Model Context Protocol (MCP). Currently
supports both Claude 3.5 Sonnet and Ollama models.

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
# Setup the main source code
%setup -q -n %{name}-%{version}
%setup -q -D -T -a 1 -n %{name}-%{version}

sed -i -e "s/go1.24.5/go1.24/g" go.mod
%{goprep} %{import_path}

%build
%{gobuild}

%install
%{goinstall}

# Build the shell autocomplete files
%{buildroot}/%{_bindir}/%{name} completion bash > %{name}-autocomplete.bash
%{buildroot}/%{_bindir}/%{name} completion zsh > %{name}-autocomplete.zsh
%{buildroot}/%{_bindir}/%{name} completion fish > %{name}-autocomplete.fish

# Install the shell autocomplete files
install -Dm 644 %{name}-autocomplete.bash %{buildroot}%{_datadir}/bash-completion/completions/%{name}
install -Dm 644 %{name}-autocomplete.zsh %{buildroot}%{_datadir}/zsh/site-functions/_%{name}
install -Dm 644 %{name}-autocomplete.fish %{buildroot}%{_datadir}/fish/completions/_%{name}

%check
# execute the binary as a basic check
%{buildroot}/%{_bindir}/%{name} help

%files
%license LICENSE
%{_bindir}/%{name}
# completions
%files bash-completion
%{_datadir}/bash-completion

%files zsh-completion
%{_datadir}/zsh

%files fish-completion
%{_datadir}/fish

%changelog
