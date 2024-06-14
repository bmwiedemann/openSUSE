#
# spec file for package hyprland
#
# Copyright (c) 2024 SUSE LLC
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

Name:           hyprland
Version:        0.41.1
Release:        0
Summary:        Dynamic tiling Wayland compositor
License:        BSD-3-Clause
URL:            https://hyprland.org/
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  cmake
BuildRequires:  gcc-c++ >= 11
BuildRequires:  git
BuildRequires:  glslang-devel
BuildRequires:  jq
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gbm) >= 17.1.0
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(hwdata)
BuildRequires:  pkgconfig(hyprcursor) >= 0.1.9
BuildRequires:  pkgconfig(hyprlang) >= 0.3.2
BuildRequires:  pkgconfig(hyprutils) >= 0.1.2
BuildRequires:  pkgconfig(hyprwayland-scanner) >= 0.3.8
BuildRequires:  pkgconfig(libdisplay-info)
BuildRequires:  pkgconfig(libdrm) >= 2.4.118
BuildRequires:  pkgconfig(libinput) >= 1.14.0
BuildRequires:  pkgconfig(libseat) >= 0.2.0
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(pixman-1) >= 0.42.0
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

%description devel
This package contains the neccessary files that are required to
build plugins for hyprland.
%endif

%package bash-completion
Summary:        Bash Completion for %{name}
Group:          System/Shells
Requires:       %{name}
Requires:       bash-completion
Supplements:    (%{name} and bash-completion)
BuildArch:      noarch

%description bash-completion
The official bash completion script for %{name}.

%package fish-completion
Summary:        Fish Completion for %{name}
Group:          System/Shells
Requires:       %{name}
Requires:       fish
Supplements:    (%{name} and fish)
BuildArch:      noarch

%description fish-completion
The official fish completion script for %{name}.

%package zsh-completion
Summary:        ZSH Completion for %{name}
Group:          System/Shells
Requires:       %{name}
Requires:       zsh
Supplements:    (%{name} and zsh)
BuildArch:      noarch

%description zsh-completion
The official zsh completion script for %{name}.

%prep
%autosetup -p1

%build
%meson \
	 -Dwlroots-hyprland:xcb-errors=%{?with_xcb_errors:enabled}%{!?with_xcb_errors:disabled}
%meson_build

%install
%meson_install --tags runtime,man%{?with_devel:,devel}
%if %{with devel}
rm %{buildroot}/%{_libdir}/libwlroots.a %{buildroot}/%{_datadir}/pkgconfig/wlroots.pc
rm -rf %{buildroot}/%{_includedir}/wlr/
%endif

%files
%license LICENSE
%doc README.md
%{_bindir}/Hyprland
%{_bindir}/hyprctl
%{_bindir}/hyprpm
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/hyprland.conf
%dir %{_datadir}/wayland-sessions/
%{_datadir}/wayland-sessions/%{name}.desktop
%dir %{_datadir}/xdg-desktop-portal
%{_datadir}/xdg-desktop-portal/%{name}-portals.conf
%{_mandir}/man1/Hyprland.*
%{_mandir}/man1/hyprctl.*

%files wallpapers
%{_datadir}/%{name}/wall*

%if %{with devel}
%files devel
%{_includedir}/%{name}
%{_datadir}/pkgconfig/%{name}.pc
%endif

%files bash-completion
%dir %{_datadir}/bash-completion/
%dir %{_datadir}/bash-completion/completions/
%{_datadir}/bash-completion/completions/hyprctl
%{_datadir}/bash-completion/completions/hyprpm

%files fish-completion
%dir %{_datadir}/fish/
%dir %{_datadir}/fish/vendor_completions.d/
%{_datadir}/fish/vendor_completions.d/hyprctl.fish
%{_datadir}/fish/vendor_completions.d/hyprpm.fish

%files zsh-completion
%dir %{_datadir}/zsh/
%dir %{_datadir}/zsh/site-functions/
%{_datadir}/zsh/site-functions/_hyprctl
%{_datadir}/zsh/site-functions/_hyprpm

%changelog
