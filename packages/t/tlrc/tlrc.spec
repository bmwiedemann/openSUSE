#
# spec file for package tlrc
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


Name:           tlrc
Version:        1.12.0
Release:        0
Summary:        A tldr-pages client written in Rust
License:        MIT
URL:            https://tldr.sh/
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
BuildRequires:  cargo-packaging
# Seems there is already another tldr-pages client
# Well but tlrc is the official one :)
Conflicts:      tealdeer

%description
The tldr-pages project is a collection of community-maintained help pages for command-line tools, that aims to be a simpler, more approachable complement to traditional man pages.

%package        bash-completion
Summary:        Bash Completion for %{name}
Group:          System/Shells
Supplements:    (%{name} and bash-completion)
Requires:       %{name} = %{version}
Requires:       bash-completion
BuildArch:      noarch

%description    bash-completion
Bash command-line completion support for %{name}.

%package        fish-completion
Summary:        Fish Completion for %{name}
Group:          System/Shells
Supplements:    (%{name} and fish)
Requires:       %{name} = %{version}
Requires:       fish
BuildArch:      noarch

%description    fish-completion
Fish command-line completion support for %{name}.

%package        zsh-completion
Summary:        Zsh Completion for %{name}
Group:          System/Shells
Supplements:    (%{name} and zsh)
Requires:       %{name} = %{version}
Requires:       zsh
BuildArch:      noarch

%description    zsh-completion
Zsh command-line completion support for %{name}.

%prep
%autosetup -p1 -a1

%build
%{cargo_build}

%install
%{cargo_install}

install -Dm644 completions/tldr.bash %{buildroot}%{_datadir}/bash-completion/completions/tldr
install -Dm644 completions/tldr.fish -t %{buildroot}%{_datadir}/fish/vendor_completions.d
install -Dm644 completions/_tldr -t %{buildroot}%{_datadir}/zsh/site-functions

%check
%{cargo_test}

%files
%{_bindir}/tldr

%files bash-completion
%{_datadir}/bash-completion/*

%files fish-completion
%dir %{_datadir}/fish
%{_datadir}/fish/*

%files zsh-completion
%dir %{_datadir}/zsh
%{_datadir}/zsh/*

%changelog
