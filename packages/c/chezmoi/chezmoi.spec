#
# spec file for package chezmoi
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


Name:           chezmoi
Version:        2.49.0
Release:        0
Summary:        A multi-host manager for dotfiles
License:        MIT
Group:          Development/Tools/Version Control
URL:            https://chezmoi.io
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
Recommends:     git
BuildRequires:  golang(API) >= 1.18

%description
chezmoi is a manager for personal preference configs and state files
("dotfiles") that programs such as editors might create. chezmoi
sources dotfiles from a GitHub repository and installs them onto new,
empty machines.

%package bash-completion
Summary:        Bash completion for %{name}
Requires:       %{name} = %{version}
Supplements:    (%{name} and bash-completion)
BuildArch:      noarch

%description bash-completion
Bash command line completion support for %{name}.

%package fish-completion
Summary:        Fish completion for %{name}
Requires:       %{name} = %{version}
Supplements:    (%{name} and fish)
BuildArch:      noarch

%description fish-completion
Fish command line completion support for %{name}.

%package zsh-completion
Summary:        Zsh completion for %{name}
Requires:       %{name} = %{version}
Supplements:    (%{name} and zsh)
BuildArch:      noarch

%description zsh-completion
Zsh command line completion support for %{name}.

%prep
%autosetup -a 1

%build
go build \
        -mod=vendor \
        -buildmode=pie \
        -tags noupgrade \
        -ldflags "-X main.version=%version
                  -X main.builtBy=build.opensuse.org"

%install
install -D -m 0755 %{name} "%{buildroot}/%{_bindir}/%{name}"
install -D -m 0644 "completions/%{name}-completion.bash" "%{buildroot}/%{_datadir}/bash-completion/completions/%{name}"
install -D -m 0644 "completions/%{name}.fish" "%{buildroot}/%{_datadir}/fish/vendor_completions.d/%{name}.fish"
install -D -m 0644 "completions/%{name}.zsh" "%{buildroot}/%{_datadir}/zsh/site-functions/_%{name}"

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%files bash-completion
%{_datadir}/bash-completion/completions/%{name}

%files fish-completion
%dir %{_datadir}/fish
%dir %{_datadir}/fish/vendor_completions.d
%{_datadir}/fish/vendor_completions.d/%{name}.fish

%files zsh-completion
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_%{name}

%changelog
