#
# spec file for package ds4-battery-monitor
#
# Copyright (c) 2026 SUSE LLC and contributors
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

Name:           ds4-battery-monitor
Version:        0.1.2
Release:        0
Summary:        DualShock 4 battery monitor tray icon
License:        MIT
Group:          System/GUI/Other
URL:            https://github.com/Jonatas-Goncalves/ds4-battery-monitor
Source0:        https://github.com/Jonatas-Goncalves/ds4-battery-monitor/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:      noarch

%description
A lightweight UDP-based battery monitor for DualShock 4 controllers
with support for multiple devices and dynamic tray icons.

%prep
%setup -q

%build
# Nothing to compile (pure python script)

%install
install -D -m 0755 ds4-battery-monitor.py %{buildroot}%{_bindir}/ds4-battery-monitor
install -D -m 0644 ds4-battery-monitor.service %{buildroot}%{_userunitdir}/ds4-battery-monitor.service

mkdir -p %{buildroot}%{_datadir}/%{name}/icons
install -m 0644 icons/{ds4_15.png,ds4_25.png,ds4_50.png,ds4_100.png} %{buildroot}%{_datadir}/%{name}/icons/

%files
%license LICENSE
%{_bindir}/ds4-battery-monitor
%{_userunitdir}/ds4-battery-monitor.service
%{_datadir}/%{name}/

%changelog
