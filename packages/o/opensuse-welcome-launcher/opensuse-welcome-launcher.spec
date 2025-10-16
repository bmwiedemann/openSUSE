#
# spec file for package opensuse-welcome-launcher
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           opensuse-welcome-launcher
Version:        1.0
Release:        0
Summary:        Welcome utility for openSUSE
License:        GPL-3.0-or-later AND MIT
Group:          System/X11/Utilities
URL:            https://github.com/openSUSE/openSUSE-welcome
Source0:        opensuse-welcome-launcher.sh
# Original filename was org.opensuse.opensuse_welcome.desktop
Source1:        org.opensuse.opensuse_welcome_launcher.desktop.in
Source3:        org.opensuse.opensuse_welcome_launcher.svg
Source4:        org.opensuse.opensuse_welcome_launcher-symbolic.svg
Recommends:     opensuse-welcome >= 0.1.10
Requires:       (gnome-tour if gnome-session)
BuildRequires:  hicolor-icon-theme
BuildRequires:  hicolor-icon-theme-branding-openSUSE
BuildArch:      noarch

%description
A simple wrapper to spawn relevant welcome tool on given desktop

%prep

%build

%install
# Create necessary directories
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_distconfdir}/xdg/autostart
mkdir -p %{buildroot}%{_datadir}/applications
mkdir -p %{buildroot}%{_datadir}/opensuse-welcome-launcher
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/scalable/apps
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/symbolic/apps

# Install launcher script
install -m 0755 %{SOURCE0} %{buildroot}%{_bindir}/opensuse-welcome-launcher

# Install desktop entries
install -d -m 0755 %{buildroot}%{_distconfdir}/xdg/autostart
sed "s|@PARAMS@||g" %{SOURCE1} > %{buildroot}%{_distconfdir}/xdg/autostart/org.opensuse.opensuse_welcome_launcher.desktop
install -d -m 0755 %{buildroot}%{_datadir}/applications
sed "s|@PARAMS@| --unconditional|g" %{SOURCE1} > %{buildroot}%{_datadir}/applications/org.opensuse.opensuse_welcome_launcher.desktop

# Install icons
install -m 0644 %{SOURCE3} %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/org.opensuse.opensuse_welcome_launcher.svg
install -m 0644 %{SOURCE4} %{buildroot}%{_datadir}/icons/hicolor/symbolic/apps/org.opensuse.opensuse_welcome_launcher-symbolic.svg

%files
%{_bindir}/opensuse-welcome-launcher
%{_distconfdir}/xdg/autostart/org.opensuse.opensuse_welcome_launcher.desktop
%{_datadir}/applications/org.opensuse.opensuse_welcome_launcher.desktop
%dir %{_datadir}/opensuse-welcome-launcher
%{_datadir}/icons/hicolor/scalable/apps/org.opensuse.opensuse_welcome_launcher.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.opensuse.opensuse_welcome_launcher-symbolic.svg

%changelog
