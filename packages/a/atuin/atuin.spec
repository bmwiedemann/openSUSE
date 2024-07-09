#
# spec file for package atuin
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


Name:           atuin
Version:        18.3.0
Release:        0
Summary:        Magical shell history
License:        MIT
Group:          System/Console
URL:            https://github.com/ellie/atuin
Source0:        https://github.com/ellie/atuin/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  c++_compiler
BuildRequires:  c_compiler
BuildRequires:  cargo >= 1.77
BuildRequires:  cargo-packaging
BuildRequires:  protobuf-devel
BuildRequires:  zstd

%description
Atuin replaces your existing shell history with a SQLite database, and records additional context for your commands.
Additionally, it provides optional and fully encrypted synchronisation of your history between machines, via an Atuin server.

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
%autosetup -a1 -p1

%build
# Omit feature "check-update" and disable defaults
%{cargo_build} --locked --no-default-features -F "client,sync,server,clipboard"

for shell in "zsh" "bash" "fish"
do
  ./target/release/%{name} gen-completions --shell "$shell" > target/%{name}."$shell"
done

%install
install -D -m 0755 "%{_builddir}/%{name}-%{version}/target/release/atuin" "%{buildroot}%{_bindir}/atuin"
install -D -m 0644 "target/%{name}.bash" "%{buildroot}/%{_datadir}/bash-completion/completions/%{name}"
install -D -m 0644 "target/%{name}.fish" "%{buildroot}/%{_datadir}/fish/vendor_completions.d/%{name}.fish"
install -D -m 0644 "target/%{name}.zsh" "%{buildroot}/%{_datadir}/zsh/site-functions/_%{name}"

%files
%license LICENSE
%doc README.md CHANGELOG.md docs/* crates/atuin/src/shell
%{_bindir}/atuin

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
