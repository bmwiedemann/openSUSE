#
# spec file for package sway
#
# Copyright (c) 2020 SUSE LLC
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


Name:           sway
Version:        1.4
Release:        0
Summary:        Window manager for Wayland compatible with i3
License:        MIT
Group:          System/GUI/Other
URL:            https://github.com/swaywm/sway
Source0:        https://github.com/swaywm/sway/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source2:        sway.keyring
Patch0:         sway-1.0-include.patch
Patch1:         0001-Fix-compiling-with-fno-common.patch
BuildRequires:  gcc-c++
#BuildRequires:  libxslt-tools
BuildRequires:  libevdev-devel
BuildRequires:  libpixman-1-0-devel
BuildRequires:  meson >= 0.48.0
BuildRequires:  pam-devel
BuildRequires:  pkgconfig
BuildRequires:  scdoc >= 1.9.2
BuildRequires:  wlroots-devel >= 0.5
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
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(xkbcommon)
Requires:       %{name}-branding >= %{version}
Requires:       ImageMagick
Requires:       ffmpeg
%if 0%{?suse_version}
# I definitely recommend Xwayland
Recommends:     xorg-x11-server-wayland
%endif

%description
"SirCmpwn's Wayland window manager" is a work in progress i3-compatible window
manager for Wayland.

%package branding-upstream
Summary:        Upstream branding of %{name}
Group:          System/GUI/Other
Requires:       %{name} = %{version}
Supplements:    packageand(%{name}:branding-upstream)
Conflicts:      otherproviders(%{name}-branding)
Provides:       %{name}-branding = %{version}
BuildArch:      noarch
#BRAND: /etc/sway/config contains upstream config and brand

%description branding-upstream
This package provides the upstream look and feel for sway.


%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
export CFLAGS="%{optflags}"
%meson \
%if 0%{?suse_version} < 1550
  -Dtray=disabled
%endif

%meson_build

%install
%meson_install

%files
%license LICENSE
%doc README.md CONTRIBUTING.md
%{_bindir}/%{name}*
%dir %{_sysconfdir}/sway/security.d
%config(noreplace) %{_sysconfdir}/sway/security.d/00-defaults
%{_mandir}/man?/%{name}*
%{_datadir}/wayland-sessions/
%dir %{_datadir}/backgrounds
%{_datadir}/backgrounds/sway
%{_datadir}/bash-completion
%{_datadir}/fish
%{_datadir}/zsh

%files branding-upstream
%dir %{_sysconfdir}/sway
%config(noreplace) %{_sysconfdir}/sway/config

%changelog
