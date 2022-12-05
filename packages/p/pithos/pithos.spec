#
# spec file for package pithos
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2012-2014 Malcolm J Lewis <malcolmlewis@opensuse.org>
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


%global appid io.github.Pithos
Name:           pithos
Version:        1.6.0
Release:        0
Summary:        Native Pandora Radio client for Linux
License:        GPL-3.0-only
Group:          Productivity/Multimedia/Other
URL:            https://pithos.github.io
Source0:        https://github.com/pithos/pithos/releases/download/%{version}/pithos-%{version}.tar.xz
# Needed for automatic typelib() Requires.
BuildRequires:  gobject-introspection
BuildRequires:  hicolor-icon-theme
BuildRequires:  intltool
BuildRequires:  meson >= 0.50.0
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(python3) >= 3.4
Requires:       gstreamer-plugins-bad
Requires:       gstreamer-plugins-good
Requires:       python3-cairo
Requires:       python3-gobject-Gdk
# Implementation of secret service
Recommends:     gnome-keyring
BuildArch:      noarch

%description
Pithos is a native Pandora Radio client for Linux. It's much more
lightweight than the Pandora.com web client, and integrates with desktop
features such as media keys, notifications, and the sound menu.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

# Fix boo#1110032 - Create noarch pyc files
find %{buildroot} -name \*.pyc -delete
%py3_compile %{buildroot}

# Remove unnecessary icons
rm -rf %{buildroot}%{_datadir}/icons/ubuntu-mono*

%files
%license license
%doc README.md
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/%{appid}.desktop
%{_datadir}/glib-2.0/schemas/%{appid}.gschema.xml
%{_datadir}/icons/hicolor/
%{_datadir}/metainfo/%{appid}.appdata.xml
%dir %{_datadir}/dbus-1
%dir %{_datadir}/dbus-1/services
%{_datadir}/dbus-1/services/%{appid}.service
%{_mandir}/man1/pithos.1%{?ext_man}

%changelog
