#
# spec file for package plasma-branding-Kalpa
#
# Copyright (c) 2024 SUSE LLC
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


Name:           plasma-branding-Kalpa
Version:        20240401
Release:        0
Summary:        Kalpa Desktop default settings
License:        BSD-3-Clause
URL:            http://kalpadesktop.org
Source:         COPYING
Source1:        flathub.flatpakrepo
Source2:        kalpa-firstboot.desktop
Source3:        kalpa-firstboot
Source4:        50-desktop.conf
Source5:        ark-addtoservicemenu.desktop
Source6:        ark-servicemenu.desktop
Source7:        distrobox-upgrade-all.service
Source8:        distrobox-upgrade-all.timer
Source9:        49-kalpa.rules
Source10:       50-kalpa
Source11:       kalpa-firstboot-aarch64.desktop
Source12:       kalpa-firstboot-aarch64
BuildRequires:  flatpak
BuildRequires:  polkit
BuildRequires:  sudo
BuildRequires:  systemd-rpm-macros
BuildRequires:  transactional-update
Requires:       flatpak
Requires:       kdialog
Requires:       polkit
Requires:       sound-theme-freedesktop
Requires:       sudo
Requires:       transactional-update
Conflicts:      gnome-branding-MicroOS
Provides:       plasma-branding = %{version}
Provides:       plasma-branding-MicroOS = %{version}
# Do not obsolete plasma-branding-MicroOS just yet
# Obsoletes:      plasma-branding-MicroOS
Conflicts:      plasma-branding-MicroOS = %{version}
BuildArch:      noarch

%description
This package provides default configurations and applications for openSUSE Kalpa.

%prep
%setup -q -T -c %{name}-%{version}
cp -a %{SOURCE0} COPYING
cp -a %{SOURCE1} flathub.flatpakrepo
%ifarch aarch64
cp -a %{SOURCE11} kalpa-firstboot-aarch64.desktop
cp -a %{SOURCE12} kalpa-firstboot-aarch64
%endif
%ifnarch aarch64
cp -a %{SOURCE2} kalpa-firstboot.desktop
cp -a %{SOURCE3} kalpa-firstboot
%endif
cp -a %{SOURCE4} 50-desktop.conf
cp -a %{SOURCE5} ark-addtoservicemenu.desktop
cp -a %{SOURCE6} ark-servicemenu.desktop
cp -a %{SOURCE7} distrobox-upgrade-all.service
cp -a %{SOURCE8} distrobox-upgrade-all.timer
cp -a %{SOURCE9} 49-kalpa.rules
cp -a %{SOURCE10} 50-kalpa

%build

%install
install -d %{buildroot}%{_datadir}/kalpa
install -m0644 flathub.flatpakrepo %{buildroot}%{_datadir}/kalpa
install -d %{buildroot}%{_sysconfdir}/skel/.config/autostart
%ifnarch aarch64
install -m0644 kalpa-firstboot.desktop %{buildroot}%{_sysconfdir}/skel/.config/autostart/kalpa-firstboot.desktop
install -d %{buildroot}%{_bindir}
install -m0755 kalpa-firstboot %{buildroot}%{_bindir}/kalpa-firstboot
%endif
%ifarch aarch64
install -m0644 kalpa-firstboot-aarch64.desktop %{buildroot}%{_sysconfdir}/skel/.config/autostart/kalpa-firstboot-aarch64.desktop
install -d %{buildroot}%{_bindir}
install -m0755 kalpa-firstboot-aarch64 %{buildroot}%{_bindir}/kalpa-firstboot-aarch64
%endif
install -d %{buildroot}%{_prefix}%{_sysconfdir}/transactional-update.conf.d
install -m644 50-desktop.conf %{buildroot}%{_prefix}%{_sysconfdir}/transactional-update.conf.d/50-desktop.conf
install -d %{buildroot}%{_sysconfdir}/skel/.local/share/kio/servicemenus
install -m0644 ark-addtoservicemenu.desktop %{buildroot}%{_sysconfdir}/skel/.local/share/kio/servicemenus/ark-addtoservicemenu.desktop
install -m0644 ark-servicemenu.desktop %{buildroot}%{_sysconfdir}/skel/.local/share/kio/servicemenus/ark-servicemenu.desktop
install -d %{buildroot}%{_userunitdir}
install -m0644 distrobox-upgrade-all.service %{buildroot}%{_userunitdir}/distrobox-upgrade-all.service
install -m0644 distrobox-upgrade-all.timer %{buildroot}%{_userunitdir}/distrobox-upgrade-all.timer
install -d %{buildroot}%{_distconfdir}/sudoers.d/
install -m0640 50-kalpa %{buildroot}%{_distconfdir}/sudoers.d/50-kalpa
install -d %{buildroot}%{_datadir}/polkit-1/rules.d/
install -m0444 49-kalpa.rules %{buildroot}%{_datadir}/polkit-1/rules.d/49-kalpa.rules

%pre
%systemd_user_pre distrobox-upgrade-all.service
%systemd_user_pre distrobox-upgrade-all.timer

%post
%systemd_user_post distrobox-upgrade-all.service
%systemd_user_post distrobox-upgrade-all.timer

%preun
%systemd_user_preun distrobox-upgrade-all.service
%systemd_user_preun distrobox-upgrade-all.timer

%files
%license COPYING
%dir %{_datadir}/kalpa
%{_datadir}/kalpa/flathub.flatpakrepo
%dir %{_sysconfdir}/skel/.config
%dir %{_sysconfdir}/skel/.config/autostart
%dir %{_sysconfdir}/skel/.local
%dir %{_sysconfdir}/skel/.local/share
%dir %{_sysconfdir}/skel/.local/share/kio
%dir %{_sysconfdir}/skel/.local/share/kio/servicemenus
%config %{_sysconfdir}/skel/.local/share/kio/servicemenus/*.desktop
%ifnarch aarch64
%config(noreplace) %{_sysconfdir}/skel/.config/autostart/kalpa-firstboot.desktop
%{_bindir}/kalpa-firstboot
%endif
%ifarch aarch64
%config(noreplace) %{_sysconfdir}/skel/.config/autostart/kalpa-firstboot-aarch64.desktop
%{_bindir}/kalpa-firstboot-aarch64
%endif
%dir %{_prefix}%{_sysconfdir}/transactional-update.conf.d
%{_prefix}%{_sysconfdir}/transactional-update.conf.d/50-desktop.conf
%{_userunitdir}/distrobox-upgrade-all.service
%{_userunitdir}/distrobox-upgrade-all.timer
%{_distconfdir}/sudoers.d/50-kalpa
%{_datadir}/polkit-1/rules.d/49-kalpa.rules

%changelog
