#
# spec file for package yambar
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


Name:           yambar
Version:        1.8.0
Release:        0
Summary:        Modular statusbar for X11 and Wayland
License:        MIT
Group:          System/GUI/Other
URL:            https://codeberg.org/dnkl/yambar
Source:         https://codeberg.org/dnkl/yambar/archive/%{version}.tar.gz
BuildRequires:  meson >= 0.58
BuildRequires:  ninja
BuildRequires:  pkg-config
BuildRequires:  scdoc
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(fcft) < 4.0.0
BuildRequires:  pkgconfig(fcft) >= 3.0.0
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(libmpdclient)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(tllist) >= 1.0.1
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-aux)
BuildRequires:  pkgconfig(xcb-cursor)
BuildRequires:  pkgconfig(xcb-errors)
BuildRequires:  pkgconfig(xcb-event)
BuildRequires:  pkgconfig(xcb-ewmh)
BuildRequires:  pkgconfig(xcb-proto)
BuildRequires:  pkgconfig(xcb-randr)
BuildRequires:  pkgconfig(xcb-render)
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  pkgconfig(yaml-0.1)

%description
Simplistic and highly configurable status panel for X and Wayland.

%prep
%autosetup -n %{name}

%package devel
Summary:  Development files for %{name}
Group:    Development/Libraries
Requires: %{name}

%description devel
Modules for interacting and modifying yambar.

%package zsh-completion
Summary: Zsh Completion for %{name}
Group: System/Shells
Supplements: (%name and zsh)
Requires: zsh
BuildArch: noarch

%description zsh-completion
Zsh command-line completion support for %{name}.

%build
%{meson}
%{meson_build}

%install
%{meson_install}

%files
%license LICENSE
%doc README.md
%{_mandir}/man1/yambar.1%{?ext_man}
%{_mandir}/man5/yambar-decorations.5%{?ext_man}
%{_mandir}/man5/yambar-modules-alsa.5%{?ext_man}
%{_mandir}/man5/yambar-modules-backlight.5%{?ext_man}
%{_mandir}/man5/yambar-modules-battery.5%{?ext_man}
%{_mandir}/man5/yambar-modules-clock.5%{?ext_man}
%{_mandir}/man5/yambar-modules-cpu.5%{?ext_man}
%{_mandir}/man5/yambar-modules-foreign-toplevel.5%{?ext_man}
%{_mandir}/man5/yambar-modules-i3.5%{?ext_man}
%{_mandir}/man5/yambar-modules-label.5%{?ext_man}
%{_mandir}/man5/yambar-modules-mem.5%{?ext_man}
%{_mandir}/man5/yambar-modules-mpd.5%{?ext_man}
%{_mandir}/man5/yambar-modules-network.5%{?ext_man}
%{_mandir}/man5/yambar-modules-removables.5%{?ext_man}
%{_mandir}/man5/yambar-modules-river.5%{?ext_man}
%{_mandir}/man5/yambar-modules-script.5%{?ext_man}
%{_mandir}/man5/yambar-modules-sway-xkb.5%{?ext_man}
%{_mandir}/man5/yambar-modules-sway.5%{?ext_man}
%{_mandir}/man5/yambar-modules-xkb.5%{?ext_man}
%{_mandir}/man5/yambar-modules-xwindow.5%{?ext_man}
%{_mandir}/man5/yambar-modules.5%{?ext_man}
%{_mandir}/man5/yambar-particles.5%{?ext_man}
%{_mandir}/man5/yambar-tags.5%{?ext_man}
%{_mandir}/man5/yambar.5%{?ext_man}

%{_bindir}/yambar
%{_datadir}/applications/yambar.desktop
%{_datadir}/zsh/site-functions/_yambar

%files devel
%dir %{_includedir}/%{name}/
%dir %{_includedir}/%{name}/bar

%{_includedir}/%{name}/bar/bar.h
%{_includedir}/%{name}/color.h
%{_includedir}/%{name}/config-verify.h
%{_includedir}/%{name}/config.h
%{_includedir}/%{name}/decoration.h
%{_includedir}/%{name}/log.h
%{_includedir}/%{name}/module.h
%{_includedir}/%{name}/particle.h
%{_includedir}/%{name}/stride.h
%{_includedir}/%{name}/tag.h
%{_includedir}/%{name}/xcb.h
%{_includedir}/%{name}/yml.h

%dir %{_datadir}/doc/%{name}/
%license %{_datadir}/doc/%{name}/LICENSE
%doc %{_datadir}/doc/%{name}/README.md

%changelog
