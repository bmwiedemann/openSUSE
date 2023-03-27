#
# spec file for package gnome-branding-MicroOS
#
# Copyright (c) 2023 SUSE LLC
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


Name:           gnome-branding-MicroOS
Summary:        MicroOS Desktop default settings
License:        BSD-3-Clause
Group:          System/GUI/GNOME
URL:            http://www.gtk.org/
Source:         COPYING
Source1:        MicroOS.gschema.override
Source2:        flathub.flatpakrepo
Source3:        mod-firstboot.desktop
Source4:        mod-firstboot
Source5:        50-desktop.conf
BuildArch:      noarch
BuildRequires:  flatpak
BuildRequires:  gio-branding-openSUSE
BuildRequires:  transactional-update
Requires:       flatpak
Requires:       gio-branding-openSUSE
Requires:       sound-theme-freedesktop
Requires:       transactional-update
Requires:       zenity
Conflicts:      plasma-branding-MicroOS
Version:        20230323
Release:        0

%description
This package provides MicroOS defaults for GNOME settings.

%prep
%setup -q -T -c %{name}-%{version}
cp -a %{SOURCE0} COPYING
cp -a %{SOURCE1} 30_MicroOS.gschema.override
cp -a %{SOURCE2} flathub.flatpakrepo
cp -a %{SOURCE3} mod-firstboot.desktop
cp -a %{SOURCE4} mod-firstboot
cp -a %{SOURCE5} 50-desktop.conf

%build

%install
install -d %{buildroot}%{_datadir}/glib-2.0/schemas
install -m0644 30_MicroOS.gschema.override %{buildroot}%{_datadir}/glib-2.0/schemas/
install -d %{buildroot}%{_prefix}/share/microos-desktop
install -m0644 flathub.flatpakrepo %{buildroot}%{_prefix}/share/microos-desktop
install -d %{buildroot}%{_sysconfdir}/skel/.config/autostart
install -m0644 mod-firstboot.desktop %{buildroot}%{_sysconfdir}/skel/.config/autostart/mod-firstboot.desktop
install -d %{buildroot}%{_bindir}
install -m0755 mod-firstboot %{buildroot}%{_bindir}/mod-firstboot
install -d %{buildroot}%{_prefix}%{_sysconfdir}/transactional-update.d
install -m644 50-desktop.conf %{buildroot}%{_prefix}%{_sysconfdir}/transactional-update.d/50-desktop.conf

%post

%postun

%files
%license COPYING
%{_datadir}/glib-2.0/schemas/30_MicroOS.gschema.override
%dir %{_prefix}/share/microos-desktop
%{_prefix}/share/microos-desktop/flathub.flatpakrepo
%dir %{_sysconfdir}/skel/.config
%dir %{_sysconfdir}/skel/.config/autostart
%config(noreplace) %{_sysconfdir}/skel/.config/autostart/mod-firstboot.desktop
%{_bindir}/mod-firstboot
%dir %{_prefix}%{_sysconfdir}/transactional-update.d
%{_prefix}%{_sysconfdir}/transactional-update.d/50-desktop.conf

%changelog
