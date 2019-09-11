#
# spec file for package alacritty
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           alacritty
Version:        0.3.3
Release:        0
Summary:        A GPU-accelerated terminal emulator
License:        Apache-2.0
Group:          System/X11/Terminals
URL:            https://github.com/jwilm/alacritty/
Source:         https://github.com/jwilm/alacritty/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.xz
Source2:        alacritty.ico
BuildRequires:  cargo
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  freetype-devel
BuildRequires:  icoutils
BuildRequires:  libxcb-devel
BuildRequires:  pkgconfig
BuildRequires:  rust
BuildRequires:  update-desktop-files
BuildRequires:  xclip
BuildRequires:  pkgconfig(fontconfig)

%description
Alacritty is a terminal emulator written in Rust that leverages the GPU for
rendering.

%package bash-completion
Summary:        Bash Completion for %{name}
Group:          System/X11/Terminals
Requires:       bash-completion
Supplements:    packageand(%{name}:bash)
BuildArch:      noarch

%description bash-completion
The official bash completion script for alacritty. It includes support
for every argument that can currently be passed to alacritty.

%package fish-completion
Summary:        Fish Completion for %{name}
Group:          System/X11/Terminals
Supplements:    packageand(%{name}:fish)
BuildArch:      noarch

%description fish-completion
The official fish completion script for alacritty.

%package zsh-completion
Summary:        ZSH Completion for %{name}
Group:          System/X11/Terminals
Supplements:    packageand(%{name}:zsh)
BuildArch:      noarch

%description zsh-completion
The official zsh completion script for alacritty.

%prep
%setup -q -a1
cp --remove-destination %{S:2} extra/windows/
icotool -x -i 1 extra/windows/alacritty.ico -o extra/windows/alacritty.png
mkdir cargo-home
cat >cargo-home/config <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "./vendor"
EOF

%ifarch aarch64 ppc64le
# Remove checksum of config.guess and config.sub since aarch64 and ppc64le modify them
sed -i 's#"expat/conftools/config.guess":"ebaffe1c6683ae2c3dcabb87825a83b892f00391514756f7640c4a3dcafbad4f",##g' ./vendor/expat-sys/.cargo-checksum.json
sed -i 's#"expat/conftools/config.sub":"523cb028db907d1fbbcecdcac6737f9e2eeba48fb639231dbc5ae69238f276c9",##g' ./vendor/expat-sys/.cargo-checksum.json
%endif

%build
export CARGO_HOME=$PWD/cargo-home
cargo build --release %{?_smp_mflags}

%install
export CARGO_HOME=$PWD/cargo-home
cargo install --root=%{buildroot}%{_prefix} --path=./alacritty

# rm duplicate license and useless toml file
rm -fr %{buildroot}%{_datadir}
rm  %{buildroot}%{_prefix}/.crates.toml

# install man page and completions
install -Dm 0644 extra/linux/alacritty.desktop %{buildroot}/%{_datadir}/applications/Alacritty.desktop
install -Dm 0644 extra/windows/alacritty.png %{buildroot}/%{_datadir}/pixmaps/Alacritty.png
install -Dm 0644 extra/%{name}.man %{buildroot}/%{_mandir}/man1/%{name}.1
install -Dm 0644 extra/completions/%{name}.bash %{buildroot}/%{_datadir}/bash-completion/completions/%{name}
install -Dm 0644 extra/completions/%{name}.fish %{buildroot}/%{_datadir}/fish/vendor_completions.d/%{name}.fish
install -Dm 0644 extra/completions/_%{name}  %{buildroot}/%{_datadir}/zsh/site-functions/_%{name}

# install desktop file
%suse_update_desktop_file Alacritty

%fdupes %{buildroot}

%files
%license LICENSE-APACHE
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_datadir}/applications/Alacritty.desktop
%{_datadir}/pixmaps/Alacritty.png

%files bash-completion
%{_datadir}/bash-completion

%files fish-completion
%{_datadir}/fish

%files zsh-completion
%{_datadir}/zsh

%changelog
