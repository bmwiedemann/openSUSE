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
Version:        0.3
Release:        0
Summary:        The openSUSEway desktop environment meta package
Group:          System/GUI/Other
URL:            https://github.com/openSUSE/openSUSEway
Source0:        https://github.com/openSUSE/openSUSEway/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
License:        MIT
BuildArch:      noarch

%description
This meta package aggregates openSUSEway desktop enviroment packages.

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

## Sway
install -D -p -m 644 .config/sway/config %{buildroot}%{_sysconfdir}/sway/config
install -D -p -m 644 .config/sway/env %{buildroot}%{_sysconfdir}/sway/env
install -D -p -m 644 .config/sway/config.d/50-openSUSE %{buildroot}%{_sysconfdir}/sway/config.d/50-openSUSE

### alacritty
# so far doesn't have special branding package and it doesn't support system wide config
install -D -p -m 644 .config/alacritty/alacritty.yml %{buildroot}%{_sysconfdir}/alacritty/alacritty.yml
#set alacritty config to the system dir
sed -i -e "s|alacritty.*|alacritty --config-file %{_sysconfdir}/alacritty/alacritty.yml|g" %{buildroot}%{_sysconfdir}/sway/config.d/50-openSUSE

## wofi
install -D -p -m 644 .config/wofi/config %{buildroot}%{_sysconfdir}/wofi/config
install -D -p -m 644 .config/wofi/style.css %{buildroot}%{_sysconfdir}/wofi/style.css
#set wofi config and style to the system dir
sed -i -e "s|wofi --show.*|wofi --conf=%{_sysconfdir}/wofi/config --style=%{_sysconfdir}/wofi/style.css|g" %{buildroot}%{_sysconfdir}/sway/config.d/50-openSUSE

## waybar
install -D -p -m 644 .config/waybar/config %{buildroot}%{_sysconfdir}/xdg/waybar/config
install -D -p -m 644 .config/waybar/style.css %{buildroot}%{_sysconfdir}/xdg/waybar/style.css

%clean
rm -rf %{buildroot}

%files -n sway-branding-openSUSE
%dir %{_sysconfdir}/sway
%config(noreplace) %{_sysconfdir}/sway/config
%config(noreplace) %{_sysconfdir}/sway/env
%dir %{_sysconfdir}/sway/config.d
%config(noreplace) %{_sysconfdir}/sway/config.d/50-openSUSE

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

