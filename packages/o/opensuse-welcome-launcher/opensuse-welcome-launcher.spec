#
# spec file for package opensuse-welcome-launcher
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



Name:           opensuse-welcome-launcher
Version:        1.0
Release:        0
Summary:        Welcome utility for openSUSE
License:        GPL-3.0-or-later AND MIT
Group:          System/X11/Utilities
URL:            https://github.com/openSUSE/openSUSE-welcome
Source0:        opensuse-welcome-launcher.sh
# Original filename was org.opensuse.opensuse_welcome.desktop
Source1:        org.opensuse.opensuse_welcome_launcher.desktop
Suggests:       opensuse-welcome

%description
A simple wrapper to spawn relevant welcome tool on given desktop

%prep

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_sysconfdir}/xdg/autostart

install -m 0755 %{SOURCE0} %{buildroot}%{_bindir}/opensuse-welcome-launcher
install -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/xdg/autostart/org.opensuse.opensuse_welcome_launcher.desktop

%files
%{_bindir}/opensuse-welcome-launcher
%{_sysconfdir}/xdg/autostart/org.opensuse.opensuse_welcome_launcher.desktop


%changelog
