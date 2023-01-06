#
# spec file for package sway
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


Name:           sway
Version:        1.8
Release:        0
Summary:        Window manager for Wayland compatible with i3
License:        MIT
Group:          System/GUI/Other
URL:            https://github.com/swaywm/sway
Source0:        https://github.com/swaywm/sway/releases/download/%{version}/%{name}-%{version}.tar.gz
Source1:        https://github.com/swaywm/sway/releases/download/%{version}/%{name}-%{version}.tar.gz.sig
Source2:        https://emersion.fr/.well-known/openpgpkey/hu/dj3498u4hyyarh35rkjfnghbjxug6b19#/%{name}.keyring
BuildRequires:  gcc-c++
#BuildRequires:  libxslt-tools
BuildRequires:  libevdev-devel
BuildRequires:  libpixman-1-0-devel
BuildRequires:  meson >= 0.60.0
BuildRequires:  pam-devel
BuildRequires:  pkgconfig
BuildRequires:  python3-i3ipc
BuildRequires:  scdoc >= 1.9.2
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(dbus-1) >= 1.10
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(json-c) >= 0.13
BuildRequires:  pkgconfig(libcap)
BuildRequires:  pkgconfig(libinput) >= 1.21.0
BuildRequires:  pkgconfig(libpcre)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.24
BuildRequires:  pkgconfig(wayland-server) >= 1.21.0
BuildRequires:  pkgconfig(wlroots) >= 0.16.0
BuildConflicts: pkgconfig(wlroots) >= 0.17.0
BuildRequires:  pkgconfig(xkbcommon)
Requires:       %{name}-branding
%if 0%{?suse_version}
# I definitely recommend Xwayland
Recommends:     xorg-x11-server-wayland
%endif
Recommends:     swaybar
Recommends:     swaynag
Requires:       xdg-desktop-portal-wlr

%description
"SirCmpwn's Wayland window manager" is a work in progress i3-compatible window
manager for Wayland.

%package branding-upstream
Summary:        Upstream branding of %{name}
Group:          System/GUI/Other
Requires:       %{name} = %{version}
Supplements:    (%{name} and branding-upstream)
Conflicts:      otherproviders(%{name}-branding)
Provides:       %{name}-branding = %{version}
BuildArch:      noarch
#BRAND: /etc/sway/config contains upstream config and brand

%description branding-upstream
This package provides the upstream look and feel for sway.

%package contrib
Summary:        Contributed scripts for %{name}
Group:          System/GUI/Other
# autoname-workspaces & inactive-windows-transparency
Requires:       python3-i3ipc
# for grimshot
Requires:       grim
Requires:       jq
Requires:       slurp
Requires:       sway
Requires:       wl-clipboard

%description contrib
Contributed scripts from %{name} package.

%package -n swaybar
Summary:        Bar program for %{name}
Group:          System/GUI/Other
Requires:       sway

%description -n swaybar
Bar program for %{name}.

%package -n swaynag
Summary:        Displays warning and error messages in %{name}
Group:          System/GUI/Other
Requires:       sway

%description -n swaynag
Displays warning and error messages in %{name}.

%prep
%autosetup -p1
for script in contrib/autoname-workspaces.py contrib/inactive-windows-transparency.py ; do
  sed -i1 's,#!/usr/bin/python$,#!/usr/bin/python3,' $script
done

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
%{_bindir}/sway
%{_bindir}/swaymsg
%{_mandir}/man1/sway.1.gz
%{_mandir}/man1/swaymsg.1.gz
%{_mandir}/man5/sway-input.5.gz
%{_mandir}/man5/sway-output.5.gz
%{_mandir}/man5/sway.5.gz
%{_mandir}/man7/sway-ipc.7.gz
%{_datadir}/wayland-sessions/
%dir %{_datadir}/backgrounds
%{_datadir}/backgrounds/sway
%{_datadir}/bash-completion/completions/sway
%{_datadir}/bash-completion/completions/swaymsg
%dir %{_datadir}/fish
%dir %{_datadir}/fish/vendor_completions.d
%{_datadir}/fish/vendor_completions.d/sway.fish
%{_datadir}/fish/vendor_completions.d/swaymsg.fish
%{_datadir}/zsh/site-functions/_sway
%{_datadir}/zsh/site-functions/_swaymsg

%files branding-upstream
%dir %{_sysconfdir}/sway
%config(noreplace) %{_sysconfdir}/sway/config

%files contrib
%license LICENSE
%{_bindir}/grimshot
%{_bindir}/inactive-windows-transparency
%{_bindir}/autoname-workspaces
%{_mandir}/man1/grimshot*

%files -n swaybar
%{_bindir}/swaybar
%{_mandir}/man5/sway-bar.5.gz
%{_mandir}/man7/swaybar-protocol.7.gz
%{_datadir}/bash-completion/completions/swaybar

%files -n swaynag
%{_bindir}/swaynag
%{_datadir}/fish/vendor_completions.d/swaynag.fish
%{_mandir}/man1/swaynag.1.gz
%{_mandir}/man5/swaynag.5.gz

%changelog
