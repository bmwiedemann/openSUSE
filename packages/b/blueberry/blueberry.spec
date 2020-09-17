#
# spec file for package blueberry
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


%define __requires_exclude typelib\\((St)\\)
Name:           blueberry
Version:        1.3.9
Release:        0
Summary:        A configuration tool for Bluetooth
License:        GPL-3.0-or-later
URL:            https://github.com/linuxmint/blueberry
Source:         https://github.com/linuxmint/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        blueberry-rfkill.rules
# PATCH-FIX-OPENSUSE blueberry-fix-rfkill-path.patch boo#1076134 sor.alexei@meowr.ru -- Fix rfkill's path.
Patch0:         blueberry-fix-rfkill-path.patch
BuildRequires:  bluez-tools
BuildRequires:  fdupes
BuildRequires:  gobject-introspection-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  python3
Requires:       bluez-tools
Requires:       gnome-bluetooth >= 3.14
Requires:       wmctrl
Recommends:     %{name}-lang
BuildArch:      noarch
%glib2_gsettings_schema_requires
Requires:       python3-dbus-python
Requires:       python3-gobject
Requires:       python3-gobject-Gdk
Requires:       python3-setproctitle
Requires:       util-linux

%description
Utility for Bluetooth devices graphical configuration.

%lang_package

%prep
%autosetup -p1
cp -a %{SOURCE1} %{name}-rfkill.rules
# Do not use env for Python scripts.
sed -i '/^#!/s/env python3$/python3/' usr/lib/blueberry/*
# Replace the icon with an existing one.
sed -i 's/^\(Icon=\).*$/\1%{name}/' .%{_datadir}/applications/%{name}.desktop

%build
%make_build

%install
cp -a .%{_prefix} %{buildroot}%{_prefix}
cp -a .%{_sysconfdir} %{buildroot}%{_sysconfdir}
install -Dpm 0644 %{name}-rfkill.rules \
  %{buildroot}%{_udevrulesdir}/61-%{name}-rfkill.rules
%find_lang %{name}
%fdupes %{buildroot}%{_datadir}/

%files
%license COPYING
%doc README.md debian/changelog
%{_bindir}/%{name}*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/glib-2.0/schemas/org.%{name}.gschema.xml
%{_datadir}/icons/hicolor/*/*/%{name}*
%{_prefix}/lib/%{name}/
%{_sysconfdir}/xdg/autostart/%{name}-obex-agent.desktop
%{_sysconfdir}/xdg/autostart/%{name}-tray.desktop
%{_udevrulesdir}/61-%{name}-rfkill.rules

%files lang -f %{name}.lang

%changelog
