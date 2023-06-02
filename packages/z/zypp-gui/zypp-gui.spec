#
# spec file for package zypp-gui
#
# Copyright (c) 2023 SUSE LLC
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


Name:           zypp-gui
Version:        0.2.0
Release:        0%{?dist}
Summary:        Update the system, search, install and remove the package, configure the repos.
License:        GPL-2.0-or-later
Group:          System/GUI
URL:            https://github.com/sunwxg/zypp-gui
Source0:        https://github.com/sunwxg/zypp-gui/releases/download/v%{version}/%{name}-%{version}.tar.xz
Source1:        additional.json

BuildRequires:  cargo
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  rust >= 1.40
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gsettings-desktop-schemas) >= 3.11.5
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.20.0
BuildRequires:  pkgconfig(gtk4) >= 4.8
BuildRequires:  pkgconfig(libadwaita-1) >= 1.2.alpha
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(packagekit-glib2) >= 1.1.0
BuildRequires:  pkgconfig(polkit-gobject-1)
Requires:       PackageKit
Requires:       pkexec

%description
Application can update the system, search, install and remove the package, configure the repos. It achieves some functions of command zypper.

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install
install -D -m 644 %{SOURCE1} %{buildroot}%{_prefix}/share/%{name}/additional.json

%check
%meson_test

%files
%license LICENSE
%{_bindir}/%{name}
%{_bindir}/mod-repo
%{_datadir}/%{name}/
%{_datadir}/applications/zypp.gui.desktop
%{_datadir}/glib-2.0/schemas/zypp.gui.gschema.xml
%{_datadir}/dbus-1/services/zypp.gui.service
%{_datadir}/icons/hicolor/scalable/apps/zypp.gui.svg
%{_datadir}/icons/hicolor/symbolic/apps/zypp.gui-symbolic.svg
%{_datadir}/icons/hicolor/16x16/places/
%{_datadir}/polkit-1/actions/zypp.gui.policy
%{_sysconfdir}/xdg/autostart/zypp-gui-service.desktop
%{_datadir}/metainfo/zypp.gui.metainfo.xml

%changelog
