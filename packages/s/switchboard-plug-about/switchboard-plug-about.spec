#
# spec file for package switchboard-plug-about
#
# Copyright (c) 2024 SUSE LLC
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


%define         appid io.elementary.settings.system
Name:           switchboard-plug-about
Version:        8.1.0
Release:        0
Summary:        Switchboard plug to show system information
License:        GPL-3.0-or-later
URL:            https://github.com/elementary/switchboard-plug-about
Source0:        %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         revert-progress-bar.patch
BuildRequires:  fdupes
BuildRequires:  meson >= 0.40.0
BuildRequires:  pkgconfig
BuildRequires:  vala
BuildRequires:  pkgconfig(appstream) >= 1.0.0
BuildRequires:  pkgconfig(fwupd)
BuildRequires:  pkgconfig(glib-2.0) >= 2.73.0
BuildRequires:  pkgconfig(granite-7)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libgtop-2.0)
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(packagekit-glib2)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(switchboard-3)
BuildRequires:  pkgconfig(udisks2)
Requires:       switchboard
Requires:       switcheroo-control

%description
About plug for Switchboard.

This plug displays information about the system.

%lang_package

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install
%fdupes %{buildroot}%{_datadir}
%find_lang %{appid}

%files
%license COPYING
%doc README.md
%dir %{_libdir}/{switchboard-3,switchboard-3/hardware}
%{_libdir}/switchboard-3/hardware/libsystem.so
%{_datadir}/metainfo/%{appid}.metainfo.xml.in

%files lang -f %{appid}.lang

%changelog
