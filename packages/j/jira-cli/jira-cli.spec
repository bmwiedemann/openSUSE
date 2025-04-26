#
# spec file for package jira-cli
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
# nodebuginfo


%define __arch_install_post export NO_BRP_STRIP_DEBUG=true
%define shortname jira
Name:           jira-cli
Version:        1.6.0
Release:        0
Summary:        CLI tool for Atlassian JIRA inspired by the Github CLI tool
License:        MIT
Group:          Development/Tools/Other
URL:            https://github.com/ankitpokhrel/jira-cli
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  golang(API) >= 1.19
# For completions packages
BuildRequires:  fish
BuildRequires:  zsh
# For SLE_15_SP4
BuildRequires:  zstd

%description
JiraCLI is an interactive command line tool for Atlassian Jira that will help
you avoid Jira UI to some extent. This tool is not yet considered complete but
has all the essential features required to improve your workflow with Jira. The
tool started with the idea of making issue search and navigation as
straightforward as possible. The tool now includes all necessary features like
issue creation, cloning, linking, ticket transition, and much more. The TUI is
heavily inspired by the GitHub CLI.

%package bash-completion
Summary:        Bash Completion for %{name}
Requires:       %{name}
Requires:       bash-completion
Supplements:    (%{name} and bash-completion)
BuildArch:      noarch

%description bash-completion
Bash command line completion support for %{name}.

%package fish-completion
Summary:        Fish Completion for %{name}
Requires:       %{name}
Requires:       fish
Supplements:    (%{name} and fish)
BuildArch:      noarch

%description fish-completion
Fish command line completion support for %{name}.

%package zsh-completion
Summary:        Zsh Completion for %{name}
Requires:       %{name}
Requires:       zsh
Supplements:    (%{name} and zsh)
BuildArch:      noarch

%description zsh-completion
Zsh command line completion support for %{name}.

%prep
%autosetup -a 1

%build
# Build the binary.
go build \
   -mod=vendor \
   -tags extended \
   -buildmode=pie \
   ./cmd/%{shortname}

# generated via CLI--there are a number of manpages all suffixed as .7
./%{shortname} man --generate --output .
gzip %{shortname}*.7

for sh in bash zsh fish
do
   ./%{shortname} completion $sh > %{shortname}.${sh}
done

%install
# Install the binary.
install -D -m 0755 %{shortname} "%{buildroot}/%{_bindir}/%{shortname}"
install -D -m 0644 -t "%{buildroot}/%{_mandir}/man7/" %{shortname}*.7.gz
install -Dm644 %{shortname}.bash %{buildroot}%{_datadir}/bash-completion/completions/%{shortname}
install -Dm644 %{shortname}.zsh  %{buildroot}%{_datadir}/zsh/site-functions/_%{shortname}
install -Dm644 %{shortname}.fish %{buildroot}%{_datadir}/fish/vendor_completions.d/%{shortname}.fish

%files
%doc README.md
%license LICENSE
%{_bindir}/%{shortname}
%{_mandir}/man7/%{shortname}*.7.gz

%files bash-completion
%{_datadir}/bash-completion/completions/%{shortname}

%files fish-completion
%{_datadir}/fish/vendor_completions.d/%{shortname}.fish

%files zsh-completion
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_%{shortname}

%changelog
