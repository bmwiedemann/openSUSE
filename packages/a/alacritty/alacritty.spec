#
# spec file for package alacritty
#
# Copyright (c) 2025 SUSE LLC
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
Version:        0.15.0
Release:        0
Summary:        A GPU-accelerated terminal emulator
License:        Apache-2.0
URL:            https://github.com/alacritty/alacritty
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
Source3:        README.suse-maint
BuildRequires:  cargo-packaging
BuildRequires:  fdupes
BuildRequires:  libxcb-devel
BuildRequires:  libxkbcommon-devel
BuildRequires:  pkgconfig
BuildRequires:  rust >= 1.74
BuildRequires:  scdoc
BuildRequires:  update-desktop-files
BuildRequires:  xclip
BuildRequires:  pkgconfig(fontconfig)
# taken from vendor/freetype-sys/build.rs
BuildRequires:  pkgconfig(freetype2) >= 24.3.18
Suggests:       terminfo

%description
Alacritty is a terminal emulator written in Rust that leverages the GPU for
rendering.

%package bash-completion
Summary:        Bash Completion for %{name}
Requires:       bash-completion
Supplements:    (%{name} and bash)
BuildArch:      noarch

%description bash-completion
The official bash completion script for alacritty. It includes support
for every argument that can currently be passed to alacritty.

%package fish-completion
Summary:        Fish Completion for %{name}
Supplements:    (%{name} and fish)
BuildArch:      noarch

%description fish-completion
The official fish completion script for alacritty.

%package zsh-completion
Summary:        ZSH Completion for %{name}
Supplements:    (%{name} and zsh)
BuildArch:      noarch

%description zsh-completion
The official zsh completion script for alacritty.

%prep
%autosetup -a1

%build
%{cargo_build}

%install
mkdir -p "%{buildroot}%{_bindir}"
install -D -m 0755 target/release/alacritty %{buildroot}%{_bindir}/alacritty

# rm duplicate license and useless toml file
rm -fr %{buildroot}%{_datadir}

# install completions
install -Dm 0644 extra/linux/Alacritty.desktop \
    %{buildroot}/%{_datadir}/applications/Alacritty.desktop
install -Dm 0644 extra/logo/alacritty-simple.svg \
    %{buildroot}/%{_datadir}/pixmaps/Alacritty.svg
install -Dm 0644 extra/linux/org.alacritty.Alacritty.appdata.xml \
    %{buildroot}/%{_datadir}/appdata/org.alacritty.Alacritty.appdata.xml
install -Dm 0644 extra/completions/%{name}.bash \
    %{buildroot}/%{_datadir}/bash-completion/completions/%{name}
install -Dm 0644 extra/completions/%{name}.fish \
    %{buildroot}/%{_datadir}/fish/vendor_completions.d/%{name}.fish
install -Dm 0644 extra/completions/_%{name} \
    %{buildroot}/%{_datadir}/zsh/site-functions/_%{name}

# build and install manpages
mkdir -p %{buildroot}%{_mandir}/man{1,5}
scdoc < extra/man/%{name}.1.scd > %{buildroot}%{_mandir}/man1/%{name}.1
scdoc < extra/man/%{name}-msg.1.scd > %{buildroot}%{_mandir}/man1/%{name}-msg.1
scdoc < extra/man/%{name}.5.scd > %{buildroot}%{_mandir}/man5/%{name}.5
scdoc < extra/man/%{name}-bindings.5.scd > %{buildroot}%{_mandir}/man5/%{name}-bindings.5

# install desktop file
%suse_update_desktop_file Alacritty

%fdupes %{buildroot}%{_datadir}

%files
%license LICENSE-APACHE
%doc CHANGELOG.md CONTRIBUTING.md README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_mandir}/man1/%{name}-msg.1%{?ext_man}
%{_mandir}/man5/%{name}.5%{?ext_man}
%{_mandir}/man5/%{name}-bindings.5%{?ext_man}
%{_datadir}/applications/Alacritty.desktop
%{_datadir}/pixmaps/Alacritty.svg
%{_datadir}/appdata/org.alacritty.Alacritty.appdata.xml

%files bash-completion
%{_datadir}/bash-completion

%files fish-completion
%{_datadir}/fish

%files zsh-completion
%{_datadir}/zsh

%changelog
