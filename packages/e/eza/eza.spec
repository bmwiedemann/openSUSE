#
# spec file for package eza
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


Name:           eza
Version:        0.18.17+0
Release:        0
Summary:        Replacement for ls written in Rust
License:        MIT
Group:          System/Base
URL:            https://github.com/eza-community/eza
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
# PATCH-FIX-OPENSUSE smolsheep@opensuse.org -- Fix test in container env gh/eza-community/eza#902
Patch0:         eza-fix-test.patch
BuildRequires:  bash-completion
BuildRequires:  cargo-packaging
BuildRequires:  fish
BuildRequires:  zsh
%ifnarch %ix86 %arm ppc
BuildRequires:  pandoc
%endif
Provides:       exa = 0.10.1
Obsoletes:      exa <= 0.10.1

%description
eza is a modern, maintained replacement for ls, built on exa.

%package bash-completion
Summary:        Bash Completion for %{name}
Group:          System/Shells
Requires:       %{name} = %{version}
Supplements:    (%{name} and bash-completion)
BuildArch:      noarch

%description bash-completion
Bash command line completion support for %{name}.

%package zsh-completion
Summary:        Zsh Completion for %{name}
Group:          System/Shells
Requires:       %{name} = %{version}
Supplements:    (%{name} and zsh)
BuildArch:      noarch

%description zsh-completion
Zsh command line completion support for %{name}.

%package fish-completion
Summary:        Fish completion for %{name}
Group:          System/Shells
Requires:       %{name} = %{version}
Supplements:    (%{name} and fish)
BuildArch:      noarch

%description fish-completion
Fish command line completion support for %{name}.

%prep
%autosetup -a1 -p1

%build
%{cargo_build}

%install
%{cargo_install}

# Manpage
# pandoc isnt available everywhere
%ifnarch %ix86 %arm ppc
install -d -m 0755 %{buildroot}%{_mandir}/man1/
pandoc --standalone -f markdown -t man man/eza.1.md > %{buildroot}%{_mandir}/man1/eza.1

install -d -m 0755 %{buildroot}%{_mandir}/man5/
pandoc --standalone -f markdown -t man man/eza_colors.5.md > %{buildroot}%{_mandir}/man5/eza_colors.5
pandoc --standalone -f markdown -t man man/eza_colors-explanation.5.md > %{buildroot}%{_mandir}/man5/eza_colors-explanation.5
%endif

# Completion files
install -Dm0644 completions/bash/eza "%{buildroot}%{_datadir}/bash-completion/completions/%{name}"
install -Dm0644 completions/zsh/_eza "%{buildroot}%{_datadir}/zsh/site-functions/_%{name}"
install -Dm0644 completions/fish/eza.fish "%{buildroot}/%{_datadir}/fish/vendor_completions.d/%{name}.fish"

%check
%{cargo_test}

%files
%license LICENCE
%doc README.md
%{_bindir}/eza
%ifnarch %ix86 %arm ppc
%{_mandir}/man1/eza.1%{?ext_man}
%{_mandir}/man5/eza_colors.5%{?ext_man}
%{_mandir}/man5/eza_colors-explanation.5%{?ext_man}
%endif

%files bash-completion
%{_datadir}/bash-completion/completions/%{name}

%files zsh-completion
%{_datadir}/zsh/site-functions/_%{name}

%files fish-completion
%{_datadir}/fish/vendor_completions.d/%{name}.fish

%changelog
