#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           openSUSE-software
Version:        0.1.1
Release:        0%{?dist}
Summary:        openSUSE software 
License:        GPL-2.0-or-later
Group:          System/GUI/
Url:            https://github.com/sunwxg/openSUSE-software
Source0:        https://github.com/sunwxg/openSUSE-software/releases/download/v%{version}/%{name}-%{version}.tar.xz
Source1:        openSUSE.software.policy
Source2:        additional.json

BuildRequires:  meson
BuildRequires:  cargo
BuildRequires:  rust >= 1.40
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(libhandy-1) >= 1.0.0
BuildRequires:  pkgconfig(gsettings-desktop-schemas) >= 3.11.5
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.20.0
BuildRequires:  pkgconfig(packagekit-glib2) >= 1.1.0
BuildRequires:  pkgconfig(polkit-gobject-1)
Requires:       PackageKit

%description
Application can update the system, search, install and remove the package, change the settings of repos. It achieves some functions of command zypper.

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install
install -D -m 644 %{SOURCE1} %{buildroot}%{_prefix}/share/%{name}/openSUSE.software.policy
install -D -m 644 %{SOURCE2} %{buildroot}%{_prefix}/share/%{name}/additional.json

%check
%meson_test

%files
%license LICENSE
%{_bindir}/%{name}
%{_bindir}/mod-repo
%{_datadir}/%{name}/
%{_datadir}/applications/openSUSE.software.desktop
%{_datadir}/glib-2.0/schemas/openSUSE.software.gschema.xml
%{_datadir}/dbus-1/services/openSUSE.software.service
%{_datadir}/icons/hicolor/scalable/apps/openSUSE.software.svg
%{_datadir}/icons/hicolor/symbolic/apps/openSUSE.software-symbolic.svg
#%{_datadir}/polkit-1/actions/openSUSE.software.policy
%{_sysconfdir}/xdg/autostart/openSUSE-software-service.desktop
%{_datadir}/metainfo/openSUSE.software.metainfo.xml

%changelog

