#
# spec file for package gnome-branding-Aeon
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2021 SUSE Software Solutions GmbH
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


Name:           gnome-branding-Aeon
Summary:        Aeon default settings
License:        BSD-3-Clause
Group:          System/GUI/GNOME
URL:            http://www.gtk.org/
Source:         COPYING
Source1:        Aeon.gschema.override
Source2:        flathub.flatpakrepo
Source3:        aeon-firstboot.desktop
Source4:        aeon-firstboot
Source5:        50-desktop.conf
Source6:        aeonwallpaper.png
Source7:        distrobox-upgrade-all.service
Source8:        distrobox-upgrade-all.timer
Source9:        50-aeon
Source10:       wallpaper-branding-Aeon.xml
Source11:       49-aeon.rules
Source12:       aeon-mig-firstboot
Source13:       vendor.conf
BuildArch:      noarch
BuildRequires:  flatpak
BuildRequires:  gio-branding-openSUSE
BuildRequires:  gnome-initial-setup
BuildRequires:  polkit
BuildRequires:  sudo
BuildRequires:  systemd-rpm-macros
BuildRequires:  transactional-update
Requires:       flatpak
Requires:       gio-branding-openSUSE
Requires:       gnome-initial-setup
Requires:       polkit
Requires:       sound-theme-freedesktop
Requires:       sudo
Requires:       transactional-update
Requires:       zenity
Obsoletes:      gnome-branding-MicroOS
Provides:       gnome-branding-MicroOS
Conflicts:      plasma-branding-MicroOS
Version:        20231005
Release:        0

%description
This package provides Aeon defaults for GNOME settings.

%prep
%setup -q -T -c %{name}-%{version}
cp -a %{SOURCE0} COPYING
cp -a %{SOURCE1} 30_Aeon.gschema.override
cp -a %{SOURCE2} flathub.flatpakrepo
cp -a %{SOURCE3} aeon-firstboot.desktop
cp -a %{SOURCE4} aeon-firstboot
cp -a %{SOURCE5} 50-desktop.conf
cp -a %{SOURCE6} aeonwallpaper.png
cp -a %{SOURCE7} distrobox-upgrade-all.service
cp -a %{SOURCE8} distrobox-upgrade-all.timer
cp -a %{SOURCE9} 50-aeon
cp -a %{SOURCE10} wallpaper-branding-Aeon.xml
cp -a %{SOURCE11} 49-aeon.rules
cp -a %{SOURCE12} aeon-mig-firstboot
cp -a %{SOURCE13} vendor.conf

%build

%install
install -d %{buildroot}%{_datadir}/glib-2.0/schemas
install -m0644 30_Aeon.gschema.override %{buildroot}%{_datadir}/glib-2.0/schemas/
install -d %{buildroot}%{_prefix}/share/aeon
install -m0644 flathub.flatpakrepo %{buildroot}%{_prefix}/share/aeon
install -d %{buildroot}%{_prefix}%{_sysconfdir}/skel/.config/autostart
install -m0644 aeon-firstboot.desktop %{buildroot}%{_prefix}%{_sysconfdir}/skel/.config/autostart/aeon-firstboot.desktop
install -d %{buildroot}%{_bindir}
install -m0755 aeon-firstboot %{buildroot}%{_bindir}/aeon-firstboot
install -m0755 aeon-mig-firstboot %{buildroot}%{_bindir}/aeon-mig-firstboot
install -d %{buildroot}%{_prefix}%{_sysconfdir}/transactional-update.conf.d
install -m644 50-desktop.conf %{buildroot}%{_prefix}%{_sysconfdir}/transactional-update.conf.d/50-desktop.conf
install -d %{buildroot}%{_datadir}/wallpapers
install -m0644 aeonwallpaper.png %{buildroot}%{_datadir}/wallpapers/aeonwallpaper.png
install -d %{buildroot}%{_userunitdir}
install -m0644 distrobox-upgrade-all.service %{buildroot}%{_userunitdir}/distrobox-upgrade-all.service
install -m0644 distrobox-upgrade-all.timer %{buildroot}%{_userunitdir}/distrobox-upgrade-all.timer
install -d %{buildroot}%{_prefix}%{_sysconfdir}/sudoers.d/
install -m0640 50-aeon %{buildroot}%{_prefix}%{_sysconfdir}/sudoers.d/50-aeon
install -d %{buildroot}%{_datadir}/gnome-background-properties
install -m0644 wallpaper-branding-Aeon.xml %{buildroot}%{_datadir}/gnome-background-properties/wallpaper-branding-Aeon.xml
install -d %{buildroot}%{_datadir}/polkit-1/rules.d/
install -m0444 49-aeon.rules %{buildroot}%{_datadir}/polkit-1/rules.d/49-aeon.rules
install -d %{buildroot}%{_datadir}/gnome-initial-setup/
install -m0644 vendor.conf %{buildroot}%{_datadir}/gnome-initial-setup/vendor.conf

%pre
%systemd_user_pre distrobox-upgrade-all.service
%systemd_user_pre distrobox-upgrade-all.timer

%post
%systemd_user_post distrobox-upgrade-all.service
%systemd_user_post distrobox-upgrade-all.timer

%preun
%systemd_user_preun distrobox-upgrade-all.service
%systemd_user_preun distrobox-upgrade-all.timer

%postun

%files
%license COPYING
%{_datadir}/glib-2.0/schemas/30_Aeon.gschema.override
%dir %{_prefix}/share/aeon
%{_prefix}/share/aeon/flathub.flatpakrepo
%dir %{_prefix}%{_sysconfdir}/skel/.config/autostart
%{_prefix}%{_sysconfdir}/skel/.config/autostart/aeon-firstboot.desktop
%{_bindir}/aeon-firstboot
%{_bindir}/aeon-mig-firstboot
%dir %{_prefix}%{_sysconfdir}/transactional-update.conf.d
%{_prefix}%{_sysconfdir}/transactional-update.conf.d/50-desktop.conf
%dir %{_datadir}/wallpapers
%{_datadir}/wallpapers/aeonwallpaper.png
%{_userunitdir}/distrobox-upgrade-all.service
%{_userunitdir}/distrobox-upgrade-all.timer
%{_prefix}%{_sysconfdir}/sudoers.d/50-aeon
%dir %{_datadir}/gnome-background-properties
%{_datadir}/gnome-background-properties/wallpaper-branding-Aeon.xml
%{_datadir}/polkit-1/rules.d/49-aeon.rules
%{_datadir}/gnome-initial-setup/vendor.conf

%changelog
