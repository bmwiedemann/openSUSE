#
# spec file for package helix
#
# Copyright (c) 2023 SUSE LLC
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

# Workaround for quilt to work
%if "x%{?rust_arches}" == "x"
%global rust_arches x86_64
%endif

%global _helix_runtimedir %{_libdir}/%{name}/runtime

Name:           helix
Version:        22.12
Release:        0
Summary:        A post-modern modal text editor written in Rust
License:        (Apache-2.0 OR MIT) AND BSD-3-Clause AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND (MIT OR Apache-2.0 OR Zlib) AND (MIT or Unlicense) AND (Zlib OR Apache-2.0 OR MIT) AND Apache-2.0 AND BSL-1.0 AND ISC AND MIT AND MPL-2.0+ AND Zlib AND MPL-2.0
URL:            https://github.com/helix-editor/helix
# This tarball includes fetched grammars
Source0:        %{url}/releases/download/%{version}/%{name}-%{version}-source.tar.xz#/%{name}-%{version}.tar.xz
Source1:        vendor.tar.xz
Source2:        cargo_config
Source3:        README-suse-maint.md
Source4:        helix-rpmlintrc
Patch0:         helix-runtime-path.patch
BuildRequires:  c++_compiler
BuildRequires:  c_compiler
BuildRequires:  cargo-packaging
BuildRequires:  hicolor-icon-theme
BuildRequires:  update-desktop-files
Recommends:     %{name}-runtime
ExclusiveArch:  %{rust_arches}

%description
A kakoune/neovim inspired modal text editor with built-in LSP and
has treesitter support for syntax highlighting and improved navigation

%package        bash-completion
Summary:        Bash Completion for %{name}
Group:          System/Shells
Supplements:    (%{name} and bash-completion)
BuildArch:      noarch

%description    bash-completion
Bash command-line completion support for %{name}.

%package        fish-completion
Summary:        Fish Completion for %{name}
Group:          System/Shells
Supplements:    (%{name} and fish)
BuildArch:      noarch

%description    fish-completion
Fish command-line completion support for %{name}.

%package        zsh-completion
Summary:        Zsh Completion for %{name}
Group:          System/Shells
Supplements:    (%{name} and zsh)
BuildArch:      noarch

%description    zsh-completion
Zsh command-line completion support for %{name}.

%package        runtime
Summary:        Runtime files for %{name}
Recommends:     %{name}

%description runtime
Helix runtime files. Separated due to how huge the runtime files are.
The runtime contains tree-sitter and grammars that makes run helix normally
if there is no runtime present in the users config directory specifically
`XDG_CONFIG_HOME/helix`.

%prep
%autosetup -a1 -p1 -c -n %{name}-%{version}
mkdir -p .cargo
cp %{SOURCE2} .cargo/config.toml

# Replace RUNTIME dir
sed -e 's#@HELIX_RUNTIME_DIR@#%{_libdir}/%{name}#' -i helix-loader/src/lib.rs

# Remove shell definitions
sed -e '/^\#\!\/usr\/bin\/env .*/d' -i contrib/completion/hx.*

%build
export HELIX_DISABLE_AUTO_GRAMMAR_BUILD=true
%{cargo_build}
HELIX_RUNTIME="$PWD/runtime" ./target/release/hx --grammar build

# Shell completions
sed -i "s|hx|helix|g" contrib/completion/hx.*

# Desktop file
sed -i "s|hx|helix|g" contrib/Helix.desktop

%install
install -d -m 0755 %{buildroot}%{_bindir}
install -m 0755 target/release/hx %{buildroot}%{_bindir}/%{name}

install -d -m 0755 %{buildroot}%{_helix_runtimedir}
cp -av "runtime/queries" %{buildroot}%{_helix_runtimedir}
cp -av "runtime/themes" %{buildroot}%{_helix_runtimedir}
find "%{_builddir}/%{name}-%{version}/runtime/grammars" -type f -name '*.so' -exec \
    install --verbose -Dm 755 {} -t "%{buildroot}%{_helix_runtimedir}/grammars" \;
install -Dm644 runtime/tutor -t %{buildroot}%{_helix_runtimedir}

# Desktop application file
install -Dm644 -T %{_builddir}/%{name}-%{version}/contrib/Helix.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop
%suse_update_desktop_file %{name}

# Icon
install -Dm644 -T %{_builddir}/%{name}-%{version}/logo.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

# Shell completions
install -Dm644 -T %{_builddir}/%{name}-%{version}/contrib/completion/hx.bash %{buildroot}%{_datadir}/bash-completion/completions/%{name}
install -Dm644 -T %{_builddir}/%{name}-%{version}/contrib/completion/hx.fish %{buildroot}%{_datadir}/fish/vendor_completions.d/%{name}.fish
install -Dm644 -T %{_builddir}/%{name}-%{version}/contrib/completion/hx.zsh %{buildroot}%{_datadir}/zsh/site-functions/_%{name}

%pre
if [ -l "%{_helix_runtimedir}" ] ; then
    rm -f "%{_helix_runtimedir}"
fi

%files
%license LICENSE
%doc README.md CHANGELOG.md languages.toml docs/CONTRIBUTING.md docs/architecture.md docs/vision.md
%{_bindir}/%{name}

# Desktop application file
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/applications/*

%dir %{_libdir}/helix

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
%{_datadir}/bash-completion/*

%files fish-completion
%dir %{_datadir}/fish
%{_datadir}/fish/*

%files zsh-completion
%dir %{_datadir}/zsh
%{_datadir}/zsh/*

%changelog
