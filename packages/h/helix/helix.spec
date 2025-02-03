#
# spec file for package helix
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


%global         _helix_runtimedir %{_libdir}/%{name}/runtime
Name:           helix
Version:        25.01.1
Release:        0
Summary:        A post-modern modal text editor written in Rust
License:        (Apache-2.0 OR MIT) AND BSD-3-Clause AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 OR MIT OR Zlib) AND (MIT OR Unlicense) AND (Apache-2.0 OR Zlib OR MIT) AND Apache-2.0 AND BSL-1.0 AND ISC AND MIT AND MPL-2.0 AND Zlib AND MPL-2.0
URL:            https://github.com/helix-editor/helix
# This tarball includes fetched grammars
Source0:        %{url}/releases/download/%{version}/%{name}-%{version}-source.tar.xz#/%{name}-%{version}.tar.xz
Source1:        vendor.tar.zst
BuildRequires:  bash-completion
BuildRequires:  c++_compiler
BuildRequires:  c_compiler
BuildRequires:  cargo >= 1.74.0
BuildRequires:  cargo-packaging
BuildRequires:  fdupes
BuildRequires:  fish
BuildRequires:  git-core
BuildRequires:  hicolor-icon-theme
BuildRequires:  update-desktop-files
BuildRequires:  zsh
Recommends:     %{name}-runtime = %{version}
ExclusiveArch:  %{rust_arches}

%description
A kakoune/neovim inspired modal text editor with built-in LSP and
has treesitter support for syntax highlighting and improved navigation

%package        bash-completion
Summary:        Bash Completion for %{name}
Supplements:    (%{name} and bash-completion)
Requires:       %{name} = %{version}
BuildArch:      noarch

%description    bash-completion
Bash command-line completion support for %{name}.

%package        fish-completion
Summary:        Fish Completion for %{name}
Supplements:    (%{name} and fish)
Requires:       %{name} = %{version}
BuildArch:      noarch

%description    fish-completion
Fish command-line completion support for %{name}.

%package        zsh-completion
Summary:        Zsh Completion for %{name}
Supplements:    (%{name} and zsh)
Requires:       %{name} = %{version}
BuildArch:      noarch

%description    zsh-completion
Zsh command-line completion support for %{name}.

%package        runtime
Summary:        Runtime files for %{name}
Requires:       %{name}

%description runtime
Helix runtime files. Separated due to how huge the runtime files are.
The runtime contains tree-sitter and grammars that makes run helix normally
if there is no runtime present in the users config directory specifically
`XDG_CONFIG_HOME/helix`.

%prep
%autosetup -a1 -c

# Remove shell definitions
sed -e '/^\#\!\/usr\/bin\/env .*/d' -i contrib/completion/hx.*

%build
#be explicit where the default runtime lives
export HELIX_DEFAULT_RUNTIME=%{_libdir}/%{name}/runtime
%{cargo_build}
cargo run --release --offline -- --grammar build

%install
install -d -m 0755 %{buildroot}%{_helix_runtimedir}

install -Dm0755 ./target/release/hx %{buildroot}%{_bindir}/hx
ln -sfv "%{_bindir}/hx" "%{buildroot}%{_bindir}/%{name}"

cp -av "runtime/queries" %{buildroot}%{_helix_runtimedir}
cp -av "runtime/themes" %{buildroot}%{_helix_runtimedir}
find "%{_builddir}/%{name}-%{version}/runtime/grammars" -type f -name '*.so' -exec \
    install --verbose -Dm 755 {} -t "%{buildroot}%{_helix_runtimedir}/grammars" \;
install -Dm644 runtime/tutor -t %{buildroot}%{_helix_runtimedir}

# Not needed during runtime
rm -rfv %{buildroot}%{_helix_runtimedir}/grammars/sources

# Desktop application file
install -Dm644 -T %{_builddir}/%{name}-%{version}/contrib/Helix.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop
%suse_update_desktop_file %{name}
install -Dm644 -T %{_builddir}/%{name}-%{version}/contrib/Helix.appdata.xml %{buildroot}%{_datadir}/metainfo/%{name}.appdata.xml

# Icon
install -Dm644 -T %{_builddir}/%{name}-%{version}/logo.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

# Shell completions
install -Dm644 -T %{_builddir}/%{name}-%{version}/contrib/completion/hx.bash %{buildroot}%{_datadir}/bash-completion/completions/hx
install -Dm644 -T %{_builddir}/%{name}-%{version}/contrib/completion/hx.fish %{buildroot}%{_datadir}/fish/vendor_completions.d/hx.fish
install -Dm644 -T %{_builddir}/%{name}-%{version}/contrib/completion/hx.zsh %{buildroot}%{_datadir}/zsh/site-functions/_hx

%fdupes %{buildroot}

%files
%license LICENSE
%doc README.md CHANGELOG.md languages.toml docs/CONTRIBUTING.md docs/architecture.md docs/vision.md
%{_bindir}/hx
%{_bindir}/%{name}

# Desktop application file
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/applications/%{name}.desktop
%{_datadir}/metainfo/%{name}.appdata.xml

%dir %{_libdir}/%{name}

# Tutor
%dir %{_helix_runtimedir}
%{_helix_runtimedir}/tutor

%files runtime
# Runtimes and runtime files
# Grammars
%dir %{_helix_runtimedir}/grammars
%{_helix_runtimedir}/grammars/*
# Queries
%dir %{_helix_runtimedir}/queries
%{_helix_runtimedir}/queries/*
# Themes
%dir %{_helix_runtimedir}/themes
%{_helix_runtimedir}/themes/*

%files bash-completion
%{_datadir}/bash-completion/completions/hx

%files fish-completion
%{_datadir}/fish/vendor_completions.d/hx.fish

%files zsh-completion
%{_datadir}/zsh/site-functions/_hx

%changelog
