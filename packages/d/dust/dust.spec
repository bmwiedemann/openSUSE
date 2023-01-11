#
# spec file for package dust
#
# Copyright (c) 2022 SUSE LLC
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


Name:           dust
Version:        0.8.3
Release:        0
Summary:        A more intuitive version of du
License:        Apache-2.0
URL:            https://github.com/bootandy/dust
Source0:        %{name}-%{version}.tar
Source1:        vendor.tar.xz
Source2:        cargo_config
BuildRequires:  cargo-packaging

%description
Dust is meant to give you an instant overview of which directories are using
disk space without requiring sort or head. Dust will print a maximum of one
'Did not have permissions message'.

%package bash-completion
Summary:        Bash completion for %{name}
Requires:       bash-completion
Supplements:    (%{name} and bash-completion)
BuildArch:      noarch

%description bash-completion
Bash command line completion support for %{name}.

%package fish-completion
Summary:        Fish completion for %{name}
Requires:       fish
Supplements:    (%{name} and fish)
BuildArch:      noarch

%description fish-completion
Fish command line completion support for %{name}.

%package zsh-completion
Summary:        ZSH completion for %{name}
Requires:       zsh
Supplements:    (%{name} and zsh)
BuildArch:      noarch

%description zsh-completion
ZSH completion script for %{name}.

%prep
%setup -qa1
mkdir .cargo
cp %{SOURCE2} .cargo/config

%build
%{cargo_build}

%install
%{cargo_install}
install -Dm0644 completions/_dust %{buildroot}/%{_datadir}/zsh/site-functions/_%{name}
install -Dm0644 completions/dust.bash %{buildroot}/%{_datadir}/bash-completion/completions/%{name}
install -Dm0644 completions/dust.fish %{buildroot}/%{_datadir}/fish/completions/%{name}.fish

%check
%{cargo_test}

%files
%{_bindir}/%{name}
%license LICENSE
%doc README.md

%files bash-completion
%{_datadir}/bash-completion

%files fish-completion
%{_datadir}/fish

%files zsh-completion
%{_datadir}/zsh

%changelog
