#
# spec file for package hyprland
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2025 SUSE LLC and contributors
# Copyright (c) 2022-24 Florian "sp1rit" <packaging@sp1rit.anonaddy.me>
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


%bcond_without devel

%define shortname hypr

Name:           hyprland
Version:        0.51.1
Release:        0
Summary:        Dynamic tiling Wayland compositor
License:        BSD-3-Clause
URL:            https://hyprland.org/
Source0:        %{name}-%{version}.tar.xz
Source99:       %{name}.rpmlintrc
Patch1:         meson-missing-wayland-include.patch
Patch2:         disable-donation-nag-popup.patch
Patch3:         pkg-config-with-deps.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++ >= 14
BuildRequires:  git
BuildRequires:  glaze-devel
BuildRequires:  glslang-devel
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(aquamarine) >= 0.9.3
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gbm) >= 17.1.0
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(hyprcursor) >= 0.1.9
BuildRequires:  pkgconfig(hyprgraphics) >= 0.1.3
BuildRequires:  pkgconfig(hyprlang) >= 0.3.2
BuildRequires:  pkgconfig(hyprutils) >= 0.8.2
BuildRequires:  pkgconfig(hyprwayland-scanner) >= 0.3.10
BuildRequires:  pkgconfig(libdrm) >= 2.4.118
BuildRequires:  pkgconfig(libinput) >= 1.14.0
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(pixman-1) >= 0.42.0
BuildRequires:  pkgconfig(re2)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(tomlplusplus)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(vulkan) >= 1.2.182
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.26
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(wayland-server) >= 1.22
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(xcb-renderutil)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xwayland)
%if 0%{?suse_version}
BuildRequires:  Mesa-libGLESv3-devel
%bcond_without  xcb_errors
%else
%bcond_with  xcb_errors
%endif
%if %{with xcb_errors}
BuildRequires:  pkgconfig(xcb-errors)
%endif
Recommends:     %{name}-wallpapers
%if %{with devel}
Suggests:       %{name}-devel
%endif

%description
Hyprland is a dynamic tiling Wayland compositor based on wlroots
that doesn't sacrifice on its looks.

It supports multiple layouts, fancy effects, has a very flexible IPC
model allowing for a lot of customization, and more.

%package wallpapers
Summary:        Hyprland wallpapers
BuildArch:      noarch

%description wallpapers
Additional wallpapers for hyprland.

%if %{with devel}
%package devel
Summary:        Files required to build Hyprland plugins
Requires:       %{name}
BuildArch:      noarch
%if 0%{?suse_version}
Requires:       Mesa-libGLESv2-devel
Requires:       Mesa-libGLESv3-devel
%endif

%description devel
This package contains the neccessary files that are required to
build plugins for hyprland.
%endif

%package bash-completion
Summary:        Bash Completion for %{name}
Group:          System/Shells
Requires:       %{name}
Requires:       awk
Requires:       bash-completion
Supplements:    (%{name} and bash-completion)
BuildArch:      noarch

%description bash-completion
The official bash completion script for %{name}.

%package fish-completion
Summary:        Fish Completion for %{name}
Group:          System/Shells
Requires:       %{name}
Requires:       awk
Requires:       fish
Supplements:    (%{name} and fish)
BuildArch:      noarch

%description fish-completion
The official fish completion script for %{name}.

%package zsh-completion
Summary:        ZSH Completion for %{name}
Group:          System/Shells
Requires:       %{name}
Requires:       awk
Requires:       zsh
Supplements:    (%{name} and zsh)
BuildArch:      noarch

%description zsh-completion
The official zsh completion script for %{name}.

%prep
%autosetup -p1
# at this point of time we do not have repository information anymore
# don't attemt to generate version.h from git, use our own.
sed -i '/version_h/d' meson.build
cat > src/version.h << EOF
#pragma once
#define GIT_COMMIT_HASH    "0000000000000000000000000000000000000000"
#define GIT_BRANCH         "openSUSE"
#define GIT_COMMIT_MESSAGE "Built for %_host"
#define GIT_COMMIT_DATE    "Thu Jan 01 00:00:00 1970"
#define GIT_DIRTY          ""
#define GIT_TAG            "%{version}"
#define GIT_COMMITS        "-1"
EOF
sed -i 's;REPLACE_ME_WITH_PREFIX;%{_prefix};' hyprpm/src/core/DataState.cpp

%build
%meson \
	-Dhyprpm=disabled \
	-Duwsm=disabled \
	-Dwlroots-hyprland:xcb-errors=%{?with_xcb_errors:enabled}%{!?with_xcb_errors:disabled}
%meson_build

%install
%meson_install --tags runtime,man%{?with_devel:,devel}

%files
%license LICENSE
%doc README.md
%{_bindir}/Hyprland
%{_bindir}/hyprland
%{_bindir}/hyprctl
%dir %{_datadir}/%{shortname}
%{_datadir}/%{shortname}/hyprland.conf
%{_datadir}/%{shortname}/lockdead.png
%{_datadir}/%{shortname}/lockdead2.png
%dir %{_datadir}/wayland-sessions/
%{_datadir}/wayland-sessions/%{name}.desktop
%dir %{_datadir}/xdg-desktop-portal
%{_datadir}/xdg-desktop-portal/%{name}-portals.conf
%{_mandir}/man1/Hyprland.*
%{_mandir}/man1/hyprctl.*

%files wallpapers
%{_datadir}/%{shortname}/wall*

%if %{with devel}
%files devel
%{_includedir}/%{name}
%{_datadir}/pkgconfig/%{name}.pc
%endif

%files bash-completion
%dir %{_datadir}/bash-completion/
%dir %{_datadir}/bash-completion/completions/
%{_datadir}/bash-completion/completions/hyprctl

%files fish-completion
%dir %{_datadir}/fish/
%dir %{_datadir}/fish/vendor_completions.d/
%{_datadir}/fish/vendor_completions.d/hyprctl.fish

%files zsh-completion
%dir %{_datadir}/zsh/
%dir %{_datadir}/zsh/site-functions/
%{_datadir}/zsh/site-functions/_hyprctl

%changelog
