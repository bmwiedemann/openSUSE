#
# spec file for package river
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


Name:           river
Version:        0.3.3
Release:        0
Summary:        A dynamic tiling Wayland compositor
License:        GPL-3.0-only
URL:            https://codeberg.org/river/river
Source0:        https://codeberg.org/river/river/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1:        https://codeberg.org/river/river/releases/download/v%{version}/%{name}-%{version}.tar.gz.sig
Source2:        vendor.tar.zst
Source3:        river-run.sh
Source4:        river-portals.conf
Source5:        https://isaacfreund.com/public_key.txt#/%{name}.keyring
Source6:        README-suse-maintenance.md
BuildRequires:  libevdev-devel
BuildRequires:  libpixman-1-0-devel
BuildRequires:  pkgconfig
BuildRequires:  scdoc >= 1.9.2
BuildRequires:  zig
BuildRequires:  zig-rpm-macros
BuildRequires:  zstd
BuildRequires:  zstd
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(dbus-1) >= 1.10
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(json-c) >= 0.12.1
BuildRequires:  pkgconfig(libcap)
BuildRequires:  pkgconfig(libinput) >= 1.6.0
BuildRequires:  pkgconfig(libpcre)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.24
BuildRequires:  pkgconfig(wayland-server) >= 1.20.0
BuildRequires:  pkgconfig(wlroots) >= 0.17.2
BuildRequires:  pkgconfig(xkbcommon)
Recommends:     xorg-x11-server-wayland
# To make Qt apps work somewhat okay on Wayland and auto use it
# Otherwise, it will try to run under XWayland
Recommends:     libqt5-qtwayland
Recommends:     libqt5-qtwayland-32bit
Requires:       river-riverctl
Requires:       river-rivertile
Recommends:     river-contrib
# For file picker and other stuff and for the sway-portal.conf
Recommends:     xdg-desktop-portal-gtk

# Users may want to use XDP-hyprland
# Only suggest XDP-wlroots since river-portals.conf requires it
Suggests:       xdg-desktop-portal-wlr

ExclusiveArch:  x86_64 aarch64 riscv64 %{mips64}

%description
River is a dynamic tiling Wayland compositor with flexible runtime configuration.

%prep
%autosetup -n %{name}-%{version} -a2

%package        riverctl
Summary:        Command-line interface for controlling river
Group:          System/GUI/Other
Requires:       %{name}

%description    riverctl
A command-line utility used to control and configure river over the Wayland protocol.

%package        rivertile
Summary:        Tiled layout generator for river
Group:          System/GUI/Other
Requires:       %{name}

%description    rivertile
A layout generator for river. It provides a simple tiled layout with split main/secondary stacks.
The initial state may be configured with various options passed on startup. Some values may additionally be modified while rivertile is running with the help of riverctl.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries/Other
Requires:       %{name}
BuildArch:      noarch

%description    devel
Modules for interacting or modifying the River Wayland compositor.

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

%package        contrib
Summary:        Helper files for making river easy to use
Supplements:    (%{name} and river-contrib)
Requires:       river
BuildArch:      noarch

%description    contrib
This package contains files that make river easier to use such as
listing it to a Display Manager such as GDM with a desktop file or
setting up sane environmental variables before running river in
`river.sh`. These files are not part of the river project.

%build
%ifarch aarch64
%zig_build -Dpie -Dxwayland --global-cache-dir vendor/
%else
%zig_build -Dno-llvm -Dpie -Dxwayland --global-cache-dir vendor/
%endif

%install
mkdir -p %{buildroot}%{_datadir}/wayland-sessions
mkdir -p %{buildroot}%{_datadir}/river
%ifarch aarch64
%zig_install -Dpie -Dxwayland --global-cache-dir vendor/
%else
%zig_install -Dno-llvm -Dpie -Dxwayland --global-cache-dir vendor/
%endif

# Installing the desktop file for easy login manager access
sed -i 's|Exec=river|Exec=river-run.sh|' contrib/river.desktop
install -Dpm 0644 contrib/river.desktop %{buildroot}%{_datadir}/wayland-sessions
cp -rv contrib %{buildroot}%{_datadir}/river/contrib
cp -v %{SOURCE2} %{buildroot}%{_datadir}/river/contrib/

# Install convenient script to run river
install -Dpm 0755 %{SOURCE3} %{buildroot}%{_bindir}

# XDP >= 0.18.0 requires a portal for the environment and onwards
install -Dpm 0644 -t %{buildroot}%{_datadir}/xdg-desktop-portal/ %{SOURCE4}

%files
%license LICENSE
%doc README.md CONTRIBUTING.md example PACKAGING.md
%{_bindir}/river
%{_bindir}/river-run.sh
%dir %{_datadir}/wayland-sessions
%{_datadir}/wayland-sessions/river.desktop
%{_mandir}/man1/river.1%{?ext_man}
%dir %{_datadir}/xdg-desktop-portal
%{_datadir}/xdg-desktop-portal/%{name}-portals.conf

%files  riverctl
%{_bindir}/riverctl
%{_mandir}/man1/riverctl.1%{?ext_man}

%files rivertile
%{_bindir}/rivertile
%{_mandir}/man1/rivertile.1%{?ext_man}

%files devel
%{_datadir}/pkgconfig/river-protocols.pc
%dir %{_datadir}/river-protocols
%{_datadir}/river-protocols/river-layout-v3.xml

%files bash-completion
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/riverctl

%files fish-completion
%dir %{_datadir}/fish
%dir %{_datadir}/fish/vendor_completions.d
%{_datadir}/fish/vendor_completions.d/riverctl.fish

%files zsh-completion
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_riverctl

%files contrib
%dir %{_datadir}/river
%dir %{_datadir}/river/contrib
%{_datadir}/river/contrib/*

%changelog
