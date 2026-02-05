#
# spec file for package goose
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


Name:           goose
Version:        1.23.0
Release:        0
Summary:        A local, extensible, open source AI agent that automates engineering tasks
License:        Apache-2.0
URL:            https://github.com/block/goose
Source0:        goose-%{version}.tar.zst
Source1:        vendor.tar.zst
BuildRequires:  cargo
BuildRequires:  cargo-packaging
BuildRequires:  libxcb-devel
BuildRequires:  protobuf-devel
# wtype is required for Linux automation
# Goose shows a warning during startup in it's abscence
Recommends:     wtype

%description
Goose is an extensible open source AI agent that enhances your software development by automating coding tasks.

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
%autosetup -a1 -p0

%build
# optimize binary
export CARGO_REGISTRIES_CRATES_IO_PROTOCOL=sparse
export CARGO_PROFILE_RELEASE_LTO=true
export CARGO_PROFILE_RELEASE_CODEGEN_UNITS=1
export CARGO_PROFILE_RELEASE_OPT_LEVEL=z

%{cargo_build} --package goose-cli --features disable-update

%install
mkdir -p %{buildroot}%{_bindir}

install -m 0755 %{_builddir}/%{name}-%{version}/target/release/%{name} %{buildroot}%{_bindir}/%{name}

# Build the shell autocomplete files
%{buildroot}/%{_bindir}/%{name} completion bash > %{name}-autocomplete.bash
%{buildroot}/%{_bindir}/%{name} completion zsh > %{name}-autocomplete.zsh
%{buildroot}/%{_bindir}/%{name} completion fish > %{name}-autocomplete.fish

# Install the shell autocomplete files
install -Dm 644 %{name}-autocomplete.bash %{buildroot}%{_datadir}/bash-completion/completions/%{name}
install -Dm 644 %{name}-autocomplete.zsh %{buildroot}%{_datadir}/zsh/site-functions/_%{name}
install -Dm 644 %{name}-autocomplete.fish %{buildroot}%{_datadir}/fish/completions/_%{name}

%check
# basic check
%{buildroot}%{_bindir}/%{name} info

# check if self update subcommand is disabled
%{buildroot}%{_bindir}/%{name} update || echo "self update is disabled!"

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
