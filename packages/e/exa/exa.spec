#
# spec file for package exa
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


Name:           exa
Version:        0.10.1
Release:        0
Summary:        Replacement for ls written in Rust
License:        MIT
Group:          System/Base
URL:            https://the.exa.website/
Source0:        https://github.com/ogham/exa/archive/v%{version}.tar.gz
Source1:        vendor.tar.xz
BuildRequires:  bash-completion
BuildRequires:  cargo
BuildRequires:  cmake
BuildRequires:  fish
BuildRequires:  git
BuildRequires:  pandoc
BuildRequires:  pkgconfig
BuildRequires:  rust
BuildRequires:  rust-std
BuildRequires:  zsh
BuildRequires:  pkgconfig(zlib)
ExcludeArch:    %{ix86} ppc

%description
exa is a replacement for ls written in Rust.
With similar but not identical options.

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
%setup -q
%setup -q -D -T -a 1
mkdir .cargo
cat >.cargo/config <<EOF
[source.crates-io]
registry = 'https://github.com/rust-lang/crates.io-index'
replace-with = 'vendored-sources'
[source.vendored-sources]
directory = './vendor'
EOF

%build
cargo build --release %{?_smp_mflags}

%install
mkdir build
cargo install --path . --root=build
install -d -m 0755 %{buildroot}%{_bindir}
install -m 0755 build/bin/exa %{buildroot}%{_bindir}/exa

# Manpage
install -d -m 0755 %{buildroot}%{_mandir}/man1/
pandoc --standalone -f markdown -t man man/exa.1.md > %{buildroot}%{_mandir}/man1/exa.1

install -d -m 0755 %{buildroot}%{_mandir}/man5/
pandoc --standalone -f markdown -t man man/exa_colors.5.md > %{buildroot}%{_mandir}/man5/exa_colors.5

# Completion files
install -Dm0644 completions/completions.bash "%{buildroot}%{_datadir}/bash-completion/completions/%{name}"
install -Dm0644 completions/completions.zsh "%{buildroot}%{_datadir}/zsh/site-functions/_%{name}"
install -Dm0644 completions/completions.fish "%{buildroot}/%{_datadir}/fish/vendor_completions.d/%{name}.fish"

%files
%license LICENCE
%doc README.md
%{_bindir}/exa
%{_mandir}/man1/exa.1%{ext_man}
%{_mandir}/man5/exa_colors.5%{ext_man}

%files bash-completion
%{_datadir}/bash-completion/completions/%{name}

%files zsh-completion
%{_datadir}/zsh/site-functions/_%{name}

%files fish-completion
%{_datadir}/fish/vendor_completions.d/%{name}.fish

%changelog
