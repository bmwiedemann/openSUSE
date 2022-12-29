#
# spec file for package wezterm
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


%global rustflags -Clink-arg=-Wl,-z,relro,-z,now -C debuginfo=2

Name:           wezterm
Version:        20221119.145034.49b9839f+g21
Release:        0
Summary:        GPU-accelerated cross-platform terminal emulator and multiplexer
URL:            https://github.com/wez/wezterm
License:        (Apache-2.0 OR MIT) AND BSD-3-Clause AND (0BSD OR MIT OR Apache-2.0) AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR BSL-1.0 OR MIT) AND (Apache-2.0 OR MIT) AND (Apache-2.0 OR MIT) AND (Apache-2.0 OR MIT OR BSD-2-Clause) AND (Apache-2.0 OR MIT OR Zlib) AND (Apache-2.0 OR MIT OR Zlib) AND (MIT OR Unlicense) AND (Apache-2.0 OR Zlib OR MIT) AND Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND CC0-1.0 AND ISC AND LGPL-2.1-only AND MIT AND MPL-2.0 AND WTFPL AND Zlib AND MIT
Source0:        %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
Source2:        cargo_config
Requires:       terminfo
BuildRequires:  Mesa-libEGL-devel

BuildRequires:  rust+cargo >= 1.43
%if 0%{?suse_version} > 1500
BuildRequires:  cargo-packaging
%endif
ExclusiveArch:  %{rust_arches}

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  libxkbcommon-devel
BuildRequires:  libxkbcommon-x11-devel
BuildRequires:  ncurses-devel
BuildRequires:  perl
BuildRequires:  pkgconfig
BuildRequires:  python-nautilus-common-files
BuildRequires:  python3
BuildRequires:  wayland-devel
BuildRequires:  xcb-util-devel
BuildRequires:  xcb-util-image-devel
BuildRequires:  xcb-util-keysyms-devel
BuildRequires:  xcb-util-wm-devel
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(libssh2)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(tic)
BuildRequires:  pkgconfig(xcb)

%description
Wezterm is a GPU-accelerated terminal emulator written in Rust. It supports
ligatures, font fallback and true color. It features dynamic color schemes, hyperlinks,
and multiplex terminal panes.

%package mux-server
Summary:        Multiplexer server for %{name}
Recommends:     %{name} = %{version}

%description mux-server
Multiplexer server for wezterm for running on a headless system.

%package bash-completion
Summary:        Bash Completion for %{name}
Requires:       bash-completion
Supplements:    (%{name} and bash-completion)
BuildArch:      noarch

%description bash-completion
Bash completion support for %{name}.

%package fish-completion
Summary:        Fish Completion for %{name}
Supplements:    (%{name} and fish)
BuildArch:      noarch

%description fish-completion
Fish completion script for %{name}.

%package zsh-completion
Summary:        ZSH Completion for %{name}
Supplements:    (%{name} and zsh)
BuildArch:      noarch

%description zsh-completion
Zsh completion script for %{name}.

%prep
%autosetup -a1
mkdir -p .cargo
cp %{SOURCE2} .cargo/config
tic -vvv -x -o terminfo termwiz/data/%{name}.terminfo
printf "%{version}" > .tag

%build
%if 0%{?suse_version} > 1500
%{cargo_build} --all-features
%else
export CARGO_FEATURE_VENDORED=1
export RUSTFLAGS='%{rustflags}'
cargo build --offline --release --all-features
%endif

%install
install -Dm 0755 %{_builddir}/%{name}-%{version}/target/release/wezterm %{buildroot}%{_bindir}/wezterm
install -Dm 0755 %{_builddir}/%{name}-%{version}/target/release/wezterm-gui %{buildroot}%{_bindir}/wezterm-gui
install -Dm 0755 %{_builddir}/%{name}-%{version}/target/release/wezterm-mux-server %{buildroot}%{_bindir}/wezterm-mux-server
install -Dm 0755 %{_builddir}/%{name}-%{version}/target/release/strip-ansi-escapes %{buildroot}%{_bindir}/strip-ansi-escapes

install -Dm 0644 terminfo/w/wezterm %{buildroot}%{_datadir}/terminfo/w/wezterm
install -Dm 0644 assets/%{name}.desktop %{buildroot}%{_datadir}/applications/org.wezfurlong.%{name}.desktop
install -Dm 0644 assets/icon/%{name}-icon.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/org.wezfurlong.%{name}.svg
install -Dm 0644 assets/%{name}.appdata.xml %{buildroot}%{_datadir}/metainfo/org.wezfurlong.%{name}.appdata.xml
install -Dm 0644 assets/shell-integration/* -t %{buildroot}%{_sysconfdir}/profile.d
install -Dm 0644 assets/%{name}-nautilus.py %{buildroot}%{_datadir}/nautilus-python/extensions/%{name}-nautilus.py

# Bash completion
install -D -m 0644 assets/shell-completion/bash %{buildroot}%{_datadir}/bash-completion/completions/wezterm
install -D -m 0644 assets/shell-completion/bash %{buildroot}%{_datadir}/bash-completion/completions/wezterm-gui

# Zsh completion
install -D -m 0644 assets/shell-completion/zsh %{buildroot}%{_datadir}/zsh/site-functions/_wezterm
install -D -m 0644 assets/shell-completion/zsh %{buildroot}%{_datadir}/zsh/site-functions/_wezterm-gui

# Fish completion
install -D -m 0644 assets/shell-completion/fish %{buildroot}%{_datadir}/fish/vendor_completions.d/wezterm.fish
install -D -m 0644 assets/shell-completion/fish %{buildroot}%{_datadir}/fish/vendor_completions.d/wezterm-gui.fish

%files
%license LICENSE.md
%doc README.md CONTRIBUTING.md
%{_bindir}/wezterm
%{_bindir}/wezterm-gui
%{_bindir}/strip-ansi-escapes
%{_datadir}/terminfo/w/wezterm
%{_datadir}/applications/org.wezfurlong.wezterm.desktop
%{_datadir}/icons/hicolor/scalable/apps/org.wezfurlong.wezterm.svg
%{_datadir}/metainfo/org.wezfurlong.wezterm.appdata.xml
%{_datadir}/nautilus-python/extensions/wezterm-nautilus.py
%config %{_sysconfdir}/profile.d/wezterm.sh

%files mux-server
%license LICENSE.md
%doc README.md CONTRIBUTING.md
%{_bindir}/wezterm-mux-server

%files bash-completion
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/wezterm
%{_datadir}/bash-completion/completions/wezterm-gui

%files fish-completion
%dir %{_datadir}/fish
%dir %{_datadir}/fish/vendor_completions.d
%{_datadir}/fish/vendor_completions.d/wezterm.fish
%{_datadir}/fish/vendor_completions.d/wezterm-gui.fish

%files zsh-completion
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_wezterm
%{_datadir}/zsh/site-functions/_wezterm-gui

%changelog
