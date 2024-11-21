#
# spec file for package sequoia-sq
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


Name:           sequoia-sq
Version:        0.39.0
Release:        0
Summary:        Command-line frontend for Sequoia
Group:          Productivity/Security
# for legal: vendor packages are not shipped the tool itself is GPL-v2-only
License:        GPL-2.0-only
URL:            https://sequoia-pgp.org/
Source0:        sequoia-sq-%{version}.tar.xz
Source1:        vendor.tar.xz
BuildRequires:  capnproto
BuildRequires:  cargo-packaging
BuildRequires:  clang-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(nettle)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(sqlite3)
ExclusiveArch:  %{rust_tier1_arches}
Conflicts:      ispell-sq

%global crate sequoia-sq

%description
Sequoia is an OpenPGP implementation. Sequoia-sq is the frontend
for the sequoia library and it is also an example of how to use various
aspects of Sequoia.

%package bash-completion
Summary:        Bash completion for %{name}
Group:          Productivity/Security
BuildArch:      noarch
Requires:       %{name}
Requires:       bash-completion
Supplements:    (%{name} and bash-completion)

%description bash-completion
Bash command line completion support for %{name}

%package        fish-completion
Summary:        Fish Completion for %{name}
Group:          Productivity/Security
Supplements:    (%{name} and fish)
Requires:       fish
BuildArch:      noarch

%description    fish-completion
Fish command-line completion support for %{name}.

%package        zsh-completion
Summary:        Zsh Completion for %{name}
Group:          Productivity/Security
Supplements:    (%{name} and zsh)
Requires:       zsh
BuildArch:      noarch

%description    zsh-completion
Zsh command-line completion support for %{name}.

%prep
%autosetup -a1 -n sequoia-sq-%{version}
mkdir -p .cargo

%build
%{cargo_build}

%install
%{cargo_install}
# install man pages
mkdir -p %{buildroot}/%{_mandir}/man1
cp -pav target/release/build/%{crate}-*/out/man-pages/sq*.1 %{buildroot}/%{_mandir}/man1/
# install shell completions
install -Dpm 0644 target/release/build/%{crate}-*/out/shell-completions/sq.bash %{buildroot}%{_datadir}/bash-completion/completions/sq.bash
install -Dpm 0644 target/release/build/%{crate}-*/out/shell-completions/sq.fish %{buildroot}%{_datadir}/fish/vendor_completions.d/sq.fish
install -Dpm 0644 target/release/build/%{crate}-*/out/shell-completions/_sq %{buildroot}%{_datadir}/zsh/site-functions/_sq

%check
%{cargo_test}

%files
%license LICENSE.txt
%doc README.md
%doc NEWS
%{_bindir}/sq
%{_mandir}/man1/sq*

%files bash-completion
%license LICENSE.txt
%{_datadir}/bash-completion/completions/sq.bash

%files fish-completion
%license LICENSE.txt
%dir %{_datadir}/fish
%dir %{_datadir}/fish/vendor_completions.d
%{_datadir}/fish/vendor_completions.d/sq.fish

%files zsh-completion
%license LICENSE.txt
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_sq

%changelog
