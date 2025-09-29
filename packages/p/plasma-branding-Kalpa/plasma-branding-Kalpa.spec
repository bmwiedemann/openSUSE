#
# spec file for package plasma-branding-Kalpa
#
# Copyright (c) 2025 SUSE LLC and contributors
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
Version:        20250926
Release:        0
Summary:        Kalpa Desktop default settings
License:        BSD-3-Clause
URL:            https://codeberg.org/KalpaDesktop/plasma-branding-Kalpa
Source:         %{name}-%{version}.tar.gz
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
Conflicts:      plasma-branding = %{version}
Supplements:    (plasma and branding-Kalpa)
BuildArch:      noarch

%description
This package provides default configurations and applications for openSUSE Kalpa.

%prep
%autosetup -p1

%build

%install
install -d %{buildroot}%{_datadir}/kalpa
install -m0644 usr/share/kalpa/flathub.flatpakrepo %{buildroot}%{_datadir}/kalpa
install -d %{buildroot}%{_distconfdir}/skel/.config/autostart
%ifnarch aarch64
install -m0644 usr/etc/skel/.config/autostart/kalpa-firstboot.desktop %{buildroot}%{_distconfdir}/skel/.config/autostart/kalpa-firstboot.desktop
install -d %{buildroot}%{_bindir}
install -m0755 usr/bin/kalpa-firstboot %{buildroot}%{_bindir}/kalpa-firstboot
%endif
%ifarch aarch64
install -m0644 usr/etc/skel/.config/autostart/kalpa-firstboot-aarch64.desktop %{buildroot}%{_distconfdir}/skel/.config/autostart/kalpa-firstboot-aarch64.desktop
install -d %{buildroot}%{_bindir}
install -m0755 usr/bin/kalpa-firstboot-aarch64 %{buildroot}%{_bindir}/kalpa-firstboot-aarch64
%endif
install -d %{buildroot}%{_distconfdir}/transactional-update.conf.d
install -m644 usr/etc/transactional-update.conf.d/50-desktop.conf %{buildroot}%{_distconfdir}/transactional-update.conf.d/50-desktop.conf
install -d %{buildroot}%{_datadir}/kio/servicemenus
install -m0644 usr/share/kio/servicemenus/ark-addtoservicemenu.desktop %{buildroot}%{_datadir}/kio/servicemenus/ark-addtoservicemenu.desktop
install -m0644 usr/share/kio/servicemenus/ark-servicemenu.desktop %{buildroot}%{_datadir}/kio/servicemenus/ark-servicemenu.desktop
install -d %{buildroot}%{_userunitdir}
install -m0644 usr/lib/systemd/user/distrobox-upgrade-all.service %{buildroot}%{_userunitdir}/distrobox-upgrade-all.service
install -m0644 usr/lib/systemd/user/distrobox-upgrade-all.timer %{buildroot}%{_userunitdir}/distrobox-upgrade-all.timer
install -d %{buildroot}%{_distconfdir}/sudoers.d/
install -m0640 usr/etc/sudoers.d/50-kalpa %{buildroot}%{_distconfdir}/sudoers.d/50-kalpa
install -d %{buildroot}%{_datadir}/polkit-1/rules.d/
install -m0444 usr/share/polkit-1/rules.d/49-kalpa.rules %{buildroot}%{_datadir}/polkit-1/rules.d/49-kalpa.rules
install -d %{buildroot}%{_prefix}/lib/sddm/sddm.conf.d/
install -m0644 usr/lib/sddm/sddm.conf.d/10-wayland.conf %{buildroot}%{_prefix}/lib/sddm/sddm.conf.d/10-wayland.conf
install -d %{buildroot}%{_prefix}/lib/systemd/user/transactional-update-notifier.service.d/
install -m0644 usr/lib/systemd/user/transactional-update-notifier.service.d/set-notification-priority.conf %{buildroot}%{_prefix}/lib/systemd/user/transactional-update-notifier.service.d/set-notification-priority.conf

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
%dir %{_distconfdir}/skel/.config/autostart
%dir %{_datadir}/kio
%dir %{_datadir}/kio/servicemenus
%{_datadir}/kio/servicemenus/*.desktop
%ifnarch aarch64
%config(noreplace) %{_distconfdir}/skel/.config/autostart/kalpa-firstboot.desktop
%{_bindir}/kalpa-firstboot
%endif
%ifarch aarch64
%config(noreplace) %{_distconfdir}/skel/.config/autostart/kalpa-firstboot-aarch64.desktop
%{_bindir}/kalpa-firstboot-aarch64
%endif
%dir %{_distconfdir}/transactional-update.conf.d
%{_distconfdir}/transactional-update.conf.d/50-desktop.conf
%{_userunitdir}/distrobox-upgrade-all.service
%{_userunitdir}/distrobox-upgrade-all.timer
%{_distconfdir}/sudoers.d/50-kalpa
%{_datadir}/polkit-1/rules.d/49-kalpa.rules
%dir %{_prefix}/lib/sddm
%dir %{_prefix}/lib/sddm/sddm.conf.d
%{_prefix}/lib/sddm/sddm.conf.d/10-wayland.conf
%dir %{_userunitdir}/transactional-update-notifier.service.d
%{_userunitdir}/transactional-update-notifier.service.d/set-notification-priority.conf

%changelog
