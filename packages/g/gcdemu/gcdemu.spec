#
# spec file for package gcdemu
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define __requires_exclude typelib\\(AppIndicator(|3)\\)
Name:           gcdemu
Version:        3.2.5
Release:        0
Summary:        GTK+ application for controlling CDEmu daemon
License:        GPL-2.0+
Group:          System/GUI/Other
Url:            https://cdemu.sourceforge.io/
Source0:        https://sourceforge.net/projects/cdemu/files/gcdemu/gcdemu-%{version}.tar.xz
BuildRequires:  gdk-pixbuf
BuildRequires:  cmake >= 3.7
BuildRequires:  gettext >= 0.15
BuildRequires:  gobject-introspection-devel
BuildRequires:  intltool >= 0.21
BuildRequires:  python3 >= 3.4
BuildRequires:  python3-gobject >= 3.0.0
BuildRequires:  update-desktop-files
Requires:       cdemu-daemon >= 3.0.0
Requires:       python3-gobject-Gdk
Recommends:     %{name}-lang
Recommends:     typelib(AppIndicator3)
BuildArch:      noarch
%glib2_gsettings_schema_requires

%description
It provides a graphic interface that allows performing the key
tasks related to controlling the CDEmu daemon, such as loading and
unloading devices, displaying devices' status and
retrieving/setting devices' debug masks.

In addition, the application listens to signals emitted by
CDEmu daemon and provides notifications via libnotify (provided
that python bindings are installed).

Features:
 * GTK+ application.
 * Supports communication via either session or system bus.
 * Device status display, device loading and unloading.
 * Support for getting/setting device's debug masks.
 * Daemon and device status changes notification via libnotify.

%lang_package

%prep
%setup -q

%build
%cmake
%make_build

%install
%cmake_install
%suse_update_desktop_file -r %{name} System Filesystem
%find_lang %{name}

%post
%glib2_gsettings_schema_post

%postun
%glib2_gsettings_schema_postun

%files
%license COPYING
%doc AUTHORS README
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}*
%{_datadir}/glib-2.0/schemas/*%{name}.gschema.xml

%files lang -f %{name}.lang
%defattr(-,root,root)

%changelog
