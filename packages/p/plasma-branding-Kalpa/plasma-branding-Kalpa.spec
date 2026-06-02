#
# spec file for package plasma-branding-Kalpa
#
# Copyright (c) 2026 SUSE LLC and contributors
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
Version:        20260601
Release:        0
Summary:        Kalpa Desktop default settings
License:        MIT
URL:            https://codeberg.org/KalpaDesktop/plasma-branding-Kalpa
Source:         %{name}-%{version}.tar.gz

BuildRequires:  cmake
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
Provides:       branding-Kalpa = %{version}
Provides:       plasma-branding = %{version}
Provides:       plasma-branding-MicroOS = %{version}
# Do not obsolete plasma-branding-MicroOS just yet
# Obsoletes:      plasma-branding-MicroOS
Conflicts:      plasma-branding-MicroOS = %{version}
Conflicts:      plasma-branding = %{version}
Supplements:    (plasma and branding-Kalpa)
BuildArch:      noarch

%description
This package provides default configurations and applications for Kalpa Desktop

%prep
%autosetup -p1

%build
%cmake

%install
%cmake_install

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
%license LICENSE
%dir %{_datadir}/kalpa
%dir %{_distconfdir}/skel/.config/autostart
%dir %{_datadir}/kio
%dir %{_datadir}/kio/servicemenus
%dir %{_distconfdir}/transactional-update.conf.d
%dir %{_prefix}/lib/sddm
%dir %{_prefix}/lib/sddm/sddm.conf.d
%dir %{_userunitdir}/transactional-update-notifier.service.d
%{_datadir}/kalpa/flathub.flatpakrepo
%{_datadir}/kio/servicemenus/*.desktop
%ifnarch aarch64
%{_distconfdir}/skel/.config/autostart/kalpa-firstboot.desktop
%{_bindir}/kalpa-firstboot
%endif
%ifarch aarch64
%{_distconfdir}/skel/.config/autostart/kalpa-firstboot-aarch64.desktop
%{_bindir}/kalpa-firstboot-aarch64
%endif
%{_distconfdir}/transactional-update.conf.d/50-desktop.conf
%{_userunitdir}/distrobox-upgrade-all.service
%{_userunitdir}/distrobox-upgrade-all.timer
%{_distconfdir}/sudoers.d/50-kalpa
%{_datadir}/polkit-1/rules.d/49-kalpa.rules
%{_prefix}/lib/sddm/sddm.conf.d/
%{_distconfdir}/xdg/
%{_userunitdir}/transactional-update-notifier.service.d/set-notification-priority.conf
%{_datadir}/discover/

%changelog
