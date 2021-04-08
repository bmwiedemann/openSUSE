#
# spec file for package sway
#
# Copyright (c) 2021 SUSE LLC
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
Version:        1.6
Release:        0
Summary:        Window manager for Wayland compatible with i3
License:        MIT
Group:          System/GUI/Other
URL:            https://github.com/swaywm/sway
Source0:        https://github.com/swaywm/sway/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source2:        sway.keyring
Patch0:         sway-1.0-include.patch
BuildRequires:  gcc-c++
#BuildRequires:  libxslt-tools
BuildRequires:  libevdev-devel
BuildRequires:  libpixman-1-0-devel
BuildRequires:  meson >= 0.48.0
BuildRequires:  pam-devel
BuildRequires:  pkgconfig
BuildRequires:  scdoc >= 1.9.2
BuildRequires:  wlroots-devel >= 0.13.0
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
Requires:       %{name}-branding
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

%package contrib
Summary:        Contributed scripts for %{name}
Group:          System/GUI/Other
BuildRequires:  python3-i3ipc

%description contrib
Contributed scripts from %{name} package.

%prep
%autosetup -p1

%build
export CFLAGS="%{optflags}"
%meson \
%if 0%{?suse_version} < 1550
  -Dtray=disabled \
%endif
  -Dsd-bus-provider=libsystemd

%meson_build

%install
%meson_install

# contrib
install -Dpm 0644 -t %{buildroot}%{_mandir}/man1 contrib/*.1
install -Dpm 0755 -t %{buildroot}%{_bindir} contrib/grimshot
install -Dpm 0755 contrib/autoname-workspaces.py \
    %{buildroot}%{_bindir}/autoname-workspaces
install -Dpm 0755 contrib/inactive-windows-transparency.py \
    %{buildroot}%{_bindir}/inactive-windows-transparency

%files
%license LICENSE
%doc README.md CONTRIBUTING.md
%{_bindir}/%{name}*
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

%files contrib
%license LICENSE
%{_bindir}/grimshot
%{_bindir}/inactive-windows-transparency
%{_bindir}/autoname-workspaces
%{_mandir}/man1/grimshot*

%changelog
