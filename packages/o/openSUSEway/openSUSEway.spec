#
# spec file for package openSUSEway
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


%define sway_version %(rpm -q --queryformat "%%{version}" sway)
%define waybar_version %(rpm -q --queryformat "%%{version}" waybar)

Name:           openSUSEway
Version:        0.13
Release:        0
Summary:        The openSUSEway desktop environment meta package
License:        MIT
Group:          Metapackages
URL:            https://github.com/openSUSE/openSUSEway
Source0:        https://github.com/openSUSE/openSUSEway/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE add-configuration-for-play-pause-next-prev-multimedi.patch gh#openSUSE/openSUSEway#41 mcepl@suse.com
# Add multimedia keys configuration
Patch0:         add-configuration-for-play-pause-next-prev-multimedi.patch
BuildArch:      noarch
BuildRequires:  aaa_base
BuildRequires:  systemd
Requires:       NetworkManager
Requires:       aaa_base
Recommends:     adwaita-qt5
Requires:       bzip2
Requires:       command-not-found
Requires:       curl
Recommends:     firefox
Requires:       gfxboot-branding-openSUSE
Requires:       git
Requires:       greetd
Requires:       grep
Requires:       gzip
Requires:       (gtkgreet or wlgreet)
Suggests:       imv
Requires:       jq
Requires:       less
Recommends:     libqt5-qtwayland
Suggests:       mpv
Requires:       pipewire
Recommends:     qt5ct
Requires:       sudo
Requires:       sway-branding-openSUSE
Requires:       tar
Suggests:       vifm
Suggests:       vim
Requires:       waybar-branding-openSUSE
Requires:       wget
Requires:       xdg-desktop-portal
Requires:       xdg-desktop-portal-wlr
Requires:       xdg-utils

%description
This meta package aggregates openSUSEway desktop enviroment packages.

%package -n     patterns-openSUSEway
%pattern_graphicalenvironments
Summary:        The openSUSEway desktop environment pattern
Group:          Metapackages
Provides:       pattern() = openSUSEway
Provides:       pattern-icon() = pattern-sway
Provides:       pattern-order() = 1460
Provides:       pattern-visible()
URL:            https://github.com/openSUSE/openSUSEway
BuildRequires:  patterns-rpm-macros
Requires:       openSUSEway

%description -n patterns-openSUSEway
This pattern installs the openSUSE look and feel for sway.

%package -n     sway-branding-openSUSE
Summary:        openSUSE branding of sway
Group:          System/GUI/Other
BuildRequires:  sway
Requires:       bc
Requires:       brightnessctl
Requires:       fontawesome-fonts
Requires:       jq
Requires:       pamixer
Requires:       patterns-sway-sway
Requires:       pavucontrol
Requires:       playerctl
Requires:       polkit-gnome
Requires:       sway
Requires:       wallpaper-branding-openSUSE
Requires:       wob
Provides:       sway-branding = %{version}
Conflicts:      otherproviders(sway-branding)
Supplements:    packageand(sway:branding-openSUSE)

#BRAND: /etc/sway/config and /etc/sway/config.d/
#BRAND: contain openSUSE config and branding

%description -n sway-branding-openSUSE
This package provides the openSUSE look and feel for sway.

%package -n     waybar-branding-openSUSE
Summary:        openSUSE branding of waybar
Group:          System/GUI/Other
BuildRequires:  waybar
Provides:       waybar-branding = %{version}
Conflicts:      otherproviders(waybar-branding)
Supplements:    packageand(waybar:branding-openSUSE)

#BRAND: /etc/xdg/waybar/config and /etc/xdg/waybar/style.css
#BRAND: contain openSUSE config and branding

%description -n waybar-branding-openSUSE
This package provides the openSUSE look and feel for waybar.

%prep
%autosetup -p1 -n openSUSEway-%{version}

%build

%install

## openSUSEway package
### qt5ct config to configure dark theme
install -D -p -m 644 qt5ct.conf %{buildroot}%{_sysconfdir}/xdg/qt5ct/qt5ct.conf
### greetd as a login manager
install -D -p -m 644 greetd/sway-config %{buildroot}%{_sysconfdir}/greetd/sway-config
install -D -p -m 644 greetd/config.toml %{buildroot}%{_sysconfdir}/greetd/config.toml.way
install -D -p -m 644 greetd/environments %{buildroot}%{_sysconfdir}/greetd/environments

## openSUSEway pattern package
mkdir -p %{buildroot}/%{_defaultdocdir}/patterns/
echo 'This file marks the pattern openSUSEway to be installed.' >%{buildroot}%{_defaultdocdir}/patterns/openSUSEway.txt

## Sway
install -D -p -m 644 .config/sway/config %{buildroot}%{_sysconfdir}/sway/config
install -D -p -m 644 .config/sway/env %{buildroot}%{_sysconfdir}/sway/env
install -D -p -m 644 .config/sway/config.d/50-openSUSE.conf %{buildroot}%{_sysconfdir}/sway/config.d/50-openSUSE.conf

install -D -p -m 644 sway/sway-session.target %{buildroot}%{_unitdir}/sway-session.target
install -D -p -m 644 sway/sway.service %{buildroot}%{_unitdir}/sway.service
install -D -p -m 644 sway/sway.desktop %{buildroot}%{_datadir}/wayland-sessions/sway.desktop.brand
install -D -p -m 755 sway/sway-run.sh %{buildroot}%{_bindir}/sway-run.sh

### alacritty
# so far doesn't have special branding package and it doesn't support system wide config
install -D -p -m 644 .config/alacritty/alacritty.yml %{buildroot}%{_sysconfdir}/alacritty/alacritty.yml

## wofi
install -D -p -m 644 .config/wofi/config %{buildroot}%{_sysconfdir}/wofi/config
install -D -p -m 644 .config/wofi/style.css %{buildroot}%{_sysconfdir}/wofi/style.css
#set wofi config and style to the system dir
sed -i -e "s|wofi --show.*|wofi --conf=%{_sysconfdir}/wofi/config --style=%{_sysconfdir}/wofi/style.css|g" %{buildroot}%{_sysconfdir}/sway/config.d/50-openSUSE.conf

## waybar
install -D -p -m 644 .config/waybar/config %{buildroot}%{_sysconfdir}/xdg/waybar/config
install -D -p -m 644 .config/waybar/style.css %{buildroot}%{_sysconfdir}/xdg/waybar/style.css

%pre -n openSUSEway
# bug #1176195, don't force enviroment, cleaning up old installations
test -e %{_sysconfdir}/profile.d/openSUSEway.sh && rm %{_sysconfdir}/profile.d/openSUSEway.sh || true
test -e %{_prefix}/lib/environment.d/50-openSUSEway.conf && rm %{_prefix}/lib/environment.d/50-openSUSEway.conf || true

%post -n openSUSEway
test -e %{_sysconfdir}/greetd/config.toml && \
    mv -n %{_sysconfdir}/greetd/config.toml %{_sysconfdir}/greetd/config.toml.orig || true
cp %{_sysconfdir}/greetd/config.toml.way %{_sysconfdir}/greetd/config.toml

%postun -n openSUSEway
test -e %{_sysconfdir}/greetd/config.toml.orig && \
    mv %{_sysconfdir}/greetd/config.toml.orig %{_sysconfdir}/greetd/config.toml || true

%post -n sway-branding-openSUSE
test -e %{_datadir}/wayland-sessions/sway.desktop && \
    mv -n %{_datadir}/wayland-sessions/sway.desktop %{_datadir}/wayland-sessions/sway.desktop.orig || true
cp %{_datadir}/wayland-sessions/sway.desktop.brand %{_datadir}/wayland-sessions/sway.desktop

%postun -n sway-branding-openSUSE
test -e %{_datadir}/wayland-sessions/sway.desktop.orig && \
    mv %{_datadir}/wayland-sessions/sway.desktop.orig %{_datadir}/wayland-sessions/sway.desktop || true

%files
%dir %{_sysconfdir}/xdg/qt5ct/
%config(noreplace) %{_sysconfdir}/xdg/qt5ct/qt5ct.conf
%dir %{_sysconfdir}/greetd/
%attr(644,greeter,greeter) %config %{_sysconfdir}/greetd/config.toml.way
%attr(644,greeter,greeter) %config %{_sysconfdir}/greetd/sway-config
%attr(644,greeter,greeter) %config %{_sysconfdir}/greetd/environments

%files -n patterns-openSUSEway
%dir %{_defaultdocdir}/patterns
%{_defaultdocdir}/patterns/openSUSEway.txt

%files -n sway-branding-openSUSE
%dir %{_sysconfdir}/sway
%config %{_sysconfdir}/sway/config
%config %{_sysconfdir}/sway/env
%dir %{_sysconfdir}/sway/config.d
%config %{_sysconfdir}/sway/config.d/50-openSUSE.conf
%{_unitdir}/sway-session.target
%{_unitdir}/sway.service
%{_datadir}/wayland-sessions/sway.desktop.brand
%{_bindir}/sway-run.sh

%dir %{_sysconfdir}/alacritty
%config(noreplace) %{_sysconfdir}/alacritty/alacritty.yml

%dir %{_sysconfdir}/wofi
%config(noreplace) %{_sysconfdir}/wofi/config
%config(noreplace) %{_sysconfdir}/wofi/style.css

%files -n waybar-branding-openSUSE
%dir %{_sysconfdir}/xdg/waybar
%config(noreplace) %{_sysconfdir}/xdg/waybar/config
%config(noreplace) %{_sysconfdir}/xdg/waybar/style.css

%changelog
