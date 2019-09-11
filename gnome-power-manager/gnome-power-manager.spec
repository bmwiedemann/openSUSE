#
# spec file for package gnome-power-manager
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           gnome-power-manager
Version:        3.32.0
Release:        0
Summary:        Power Management for GNOME
License:        GPL-2.0-or-later
Group:          System/GUI/GNOME
URL:            https://projects.gnome.org/gnome-power-manager/
Source0:        https://download.gnome.org/sources/gnome-power-manager/3.32/%{name}-%{version}.tar.xz

BuildRequires:  docbook-utils-minimal
BuildRequires:  fdupes
BuildRequires:  libupower-glib-devel
BuildRequires:  meson >= 0.46.0
BuildRequires:  pkgconfig
BuildRequires:  translation-update-upstream
BuildRequires:  pkgconfig(gdk-3.0) >= 2.91.7
BuildRequires:  pkgconfig(glib-2.0) >= 2.45.8
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.3.8
Requires:       gnome-session-core
Requires:       upower
%glib2_gsettings_schema_requires

%description
GNOME Power Manager is a GNOME session daemon that acts as a policy
agent. It listens for system events and responds with
user-configurable actions.

%lang_package

%prep
%autosetup
translation-update-upstream

%build
%meson \
	-D enable-tests=false \
	%{nil}
%meson_build

%install
%meson_install

%find_lang %{name} %{?no_lang_C}
%fdupes %{buildroot}

%files
%license COPYING
%{_bindir}/gnome-power-statistics
%{_datadir}/applications/org.gnome.PowerStats.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.power-manager.gschema.xml
%{_datadir}/icons/hicolor/*/apps/*
%{_mandir}/man1/gnome-power-statistics.1%{ext_man}
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/org.gnome.PowerStats.appdata.xml

%files lang -f %{name}.lang

%changelog
