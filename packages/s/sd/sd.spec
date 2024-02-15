#
# spec file for package sd
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


Name:           sd
Version:        1.0.0+g0
Release:        0
Summary:        Intuitive find & replace CLI
URL:            https://github.com/chmln/sd
License:        (Apache-2.0 OR MIT) AND (MIT OR Unlicense) AND BSD-3-Clause AND MIT AND (MIT OR Unlicense)
Group:          System/Base
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
BuildRequires:  cargo-packaging
BuildRequires:  zstd

%description
sd uses regex syntax that you already know from JavaScript and Python.
Forget about dealing with quirks of sed or awk - get productive immediately.

%package        fish-completion
Summary:        Fish Completion for %{name}
Group:          System/Shells
Supplements:    (%{name} and fish)
Requires:       fish
BuildArch:      noarch

%description    fish-completion
Fish command-line completion support for %{name}.

%package        zsh-completion
Summary:        Zsh Completion for %{name}
Group:          System/Shells
Supplements:    (%{name} and zsh)
Requires:       zsh
BuildArch:      noarch

%description    zsh-completion
Zsh command-line completion support for %{name}.

%package        bash-completion
Summary:        Bash Completion for %{name}
Group:          System/Shells
Supplements:    (%{name} and bash-completion)
Requires:       bash-completion
BuildArch:      noarch

%description    bash-completion
Bash command-line completion support for %{name}.

%prep
%autosetup -a1

%build
%{cargo_build}

%install
%{cargo_install}

# Zsh completion
install -Dpm644 -T gen/completions/_sd %{buildroot}%{_datadir}/zsh/site-functions/_sd

# Fish completion
install -Dpm644 -T gen/completions/sd.fish %{buildroot}%{_datadir}/fish/vendor_completions.d/sd.fish

# Bash completion
install -Dpm644 -T gen/completions/sd.bash %{buildroot}%{_datadir}/bash-completion/completions/sd

%files
%license LICENSE
%doc README.md CHANGELOG.md
%{_bindir}/sd

%files bash-completion
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
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
