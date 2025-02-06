#
# spec file for package sway
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


%define contribver 1.10

Name:           sway
Version:        1.10.1
Release:        0
Summary:        Window manager for Wayland compatible with i3
License:        MIT
Group:          System/GUI/Other
URL:            https://github.com/swaywm/sway
Source0:        https://github.com/swaywm/sway/releases/download/%{version}/%{name}-%{version}.tar.gz
Source1:        https://github.com/swaywm/sway/releases/download/%{version}/%{name}-%{version}.tar.gz.sig
Source2:        https://emersion.fr/.well-known/openpgpkey/hu/dj3498u4hyyarh35rkjfnghbjxug6b19#/%{name}.keyring
Source3:        sway-portals.conf
Source4:        https://github.com/OctopusET/sway-contrib/archive/refs/tags/%{contribver}-contrib.0.tar.gz#/sway-contrib-%{contribver}.tar.gz
Source5:        sway.rpmlintrc
BuildRequires:  gcc-c++
#BuildRequires:  libxslt-tools
BuildRequires:  libevdev-devel
BuildRequires:  fdupes
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
BuildRequires:  pkgconfig(wlroots-0.18)
BuildRequires:  pkgconfig(xkbcommon)
# WARNING: do not set this to versioned, as it breaks other branding providers
# such as openSUSEway (bsc#1222579)
Requires:       %{name}-branding
%if 0%{?suse_version}
# I definitely recommend Xwayland
Recommends:     xorg-x11-server-wayland
%endif
Recommends:     swaybar
Recommends:     swaynag
Recommends:     xdg-desktop-portal-wlr

# For file picker and other stuff and for the sway-portal.conf
Recommends:     xdg-desktop-portal-gtk

%description
Sway is a tiling Wayland compositor and a drop-in replacement for the i3
window manager for X11. It works with your existing i3 configuration and
supports most of i3's features, plus a few extras.

%package branding-upstream
Summary:        Upstream branding of %{name}
Group:          System/GUI/Other
Requires:       %{name} = %{version}
Supplements:    (%{name} and branding-upstream)
Conflicts:      %{name}-branding
Provides:       %{name}-branding = %{version}
BuildArch:      noarch
#BRAND: /etc/sway/config contains upstream config and brand

%description branding-upstream
This package provides the upstream look and feel for sway.

%package contrib
Summary:        Contributed scripts for %{name}
Version:        %{contribver}
Group:          System/GUI/Other
# autoname-workspaces & inactive-windows-transparency
Requires:       python3-i3ipc
# for grimshot
Requires:       grim
Requires:       jq
Requires:       slurp
Requires:       sway
Requires:       wl-clipboard
BuildArch:      noarch

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
mkdir -p contrib
tar xvf %{SOURCE4} --strip-components=1 -C contrib/
pushd contrib
rm -rf .github
find -type f -name "*.py" -execdir sed -i 's,#!/usr/bin/env python$,#!/usr/bin/python3,' {} \;
find -type f -name "*.py" -execdir sed -i 's,#!/usr/bin/env python3$,#!/usr/bin/python3,' {} \;
find -type f -name "grimpicker" -execdir sed -i 's,#!/usr/bin/env python3$,#!/usr/bin/python3,' {} \;
find -type f -name "*.py" -execdir sed -i 's,#!/usr/bin/python$,#!/usr/bin/python3,' {} \;
popd

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
install -Dpm 0644 -t %{buildroot}%{_mandir}/man1 contrib/grimshot/*.1
install -Dpm 0755 -t %{buildroot}%{_bindir} contrib/grimshot/grimshot

# Move over other contrib files to /usr/share/sway/contrib folder
mkdir -p %{buildroot}%{_datadir}/%{name}/
cp -r contrib %{buildroot}%{_datadir}/%{name}/contrib
find %{buildroot}%{_datadir}/%{name}/contrib -type f -exec "chmod 0644 {}" \;
# Remove it since it's installed in /usr/bin
rm -v %{buildroot}%{_datadir}/%{name}/contrib/grimshot/grimshot

# XDP >= 0.18.0 requires a portal for the environment and onwards
install -Dpm 0644 -t %{buildroot}%{_datadir}/xdg-desktop-portal/ %{SOURCE3}

%fdupes %{buildroot}%{_prefix}

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
%dir %{_datadir}/xdg-desktop-portal
%{_datadir}/xdg-desktop-portal/sway-portals.conf

%files branding-upstream
%dir %{_sysconfdir}/sway
%config(noreplace) %{_sysconfdir}/sway/config

%files contrib
%license LICENSE
%{_bindir}/grimshot
%{_mandir}/man1/grimshot*
%dir %{_datadir}/sway
%dir %{_datadir}/sway/contrib
%{_datadir}/sway/contrib/*

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
