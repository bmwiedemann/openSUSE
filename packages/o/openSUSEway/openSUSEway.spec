#
# spec file for package openSUSEway
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

%define sway_version %(rpm -q --queryformat "%%{version}" sway)
%define waybar_version %(rpm -q --queryformat "%%{version}" waybar)

Name:           openSUSEway
Version:        0.10
Release:        0
Summary:        The openSUSEway desktop environment meta package
Group:          Metapackages
URL:            https://github.com/openSUSE/openSUSEway
Source0:        https://github.com/openSUSE/openSUSEway/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
License:        MIT
BuildArch:      noarch
BuildRequires:  aaa_base
BuildRequires:  systemd
Requires:       aaa_base
Requires:       sway-branding-openSUSE
Requires:       waybar-branding-openSUSE
Requires:       sudo
Requires:       git
Requires:       jq
Requires:       wget
Requires:       curl
Requires:       vim
Requires:       tar
Requires:       gzip
Requires:       bzip2
Requires:       less
Requires:       grep
Requires:       vifm
Requires:       imv
Requires:       firefox
Requires:       NetworkManager
Requires:       mpv
Requires:       libqt5-qtwayland
Requires:       pipewire
Requires:       xdg-utils
Requires:       xdg-desktop-portal
Requires:       xdg-desktop-portal-wlr
Requires:       qt5ct
Requires:       adwaita-qt5
Requires:       wob
Requires:       pamixer
Requires:       command-not-found

%description
This meta package aggregates openSUSEway desktop enviroment packages.

%bcond_with betatest
%pattern_graphicalenvironments
%package -n     patterns-openSUSEway
Summary:        The openSUSEway desktop environment pattern
License:        MIT
Group:          Metapackages
Provides:       pattern() = openSUSEway
Provides:       pattern-category() = openSUSEway
Provides:       pattern-icon() = pattern-sway
Provides:       pattern-order() = 1460
Provides:       pattern-visible()
URL:            https://github.com/openSUSE/openSUSEway
BuildRequires:  patterns-rpm-macros
Requires:       openSUSEway

%description -n patterns-openSUSEway
This is an internal package that is used to create the patterns as part
of the installation source setup.  Installation of this package does
not make sense.

%package -n     sway-branding-openSUSE
Summary:        openSUSE branding of sway
Group:          System/GUI/Other
BuildRequires:	sway
Requires:       patterns-sway-sway
Requires:       wallpaper-branding-openSUSE
Requires:       brightnessctl
Requires:       pavucontrol
Requires:       fontawesome-fonts
Requires:       jq
Requires:       sway
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
install -D -p -m 644 openSUSEway.sh %{buildroot}%{_sysconfdir}/profile.d/openSUSEway.sh
install -D -p -m 644 .config/sway/env %{buildroot}%{_prefix}/lib/environment.d/50-openSUSEway.conf
### qt5ct config to configure dark theme
install -D -p -m 644 qt5ct.conf %{buildroot}/%{_sysconfdir}/xdg/qt5ct/qt5ct.conf

## openSUSEway pattern package
mkdir -p %{buildroot}/%{_defaultdocdir}/patterns/
echo 'This file marks the pattern openSUSEway to be installed.' >%{buildroot}/%{_defaultdocdir}/patterns/openSUSEway.txt

## Sway
install -D -p -m 644 .config/sway/config %{buildroot}%{_sysconfdir}/sway/config
install -D -p -m 644 .config/sway/env %{buildroot}%{_sysconfdir}/sway/env
install -D -p -m 644 .config/sway/config.d/50-openSUSE.conf %{buildroot}%{_sysconfdir}/sway/config.d/50-openSUSE.conf

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

%files
%config %{_sysconfdir}/profile.d/openSUSEway.sh
%config %{_prefix}/lib/environment.d/50-openSUSEway.conf
%dir %{_sysconfdir}/xdg/qt5ct/
%config(noreplace) %{_sysconfdir}/xdg/qt5ct/qt5ct.conf

%files -n patterns-openSUSEway
%dir %{_defaultdocdir}/patterns
%{_defaultdocdir}/patterns/openSUSEway.txt

%files -n sway-branding-openSUSE
%dir %{_sysconfdir}/sway
%config %{_sysconfdir}/sway/config
%config %{_sysconfdir}/sway/env
%dir %{_sysconfdir}/sway/config.d
%config %{_sysconfdir}/sway/config.d/50-openSUSE.conf

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

