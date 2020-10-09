#
# spec file for package dconf-editor
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


Name:           dconf-editor
Version:        3.36.7
Release:        0
Summary:        Graphical editor for the dconf key-based configuration system
License:        GPL-3.0-or-later
Group:          System/GUI/GNOME
URL:            https://wiki.gnome.org/Apps/DconfEditor
Source0:        https://download.gnome.org/sources/dconf-editor/3.36/%{name}-%{version}.tar.xz

BuildRequires:  appstream-glib-devel
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  vala >= 0.40.0
BuildRequires:  pkgconfig(dconf) >= 0.25.1
BuildRequires:  pkgconfig(glib-2.0) >= 2.55.1
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22.7
BuildRequires:  pkgconfig(libxml-2.0)

%description
dconf is a low-level configuration system. Its main purpose is to
provide a backend to GSettings on platforms that don't already
have configuration storage systems.

This package provides a graphical editor for the dconf database.

%lang_package

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%suse_update_desktop_file %{buildroot}%{_datadir}/applications/ca.desrt.dconf-editor.desktop SystemSetup X-GNOME-PersonalSettings
%find_lang %{name}

%files
%license COPYING
%{_bindir}/dconf-editor
%{_datadir}/metainfo/ca.desrt.dconf-editor.appdata.xml
%{_datadir}/applications/ca.desrt.dconf-editor.desktop
%{_datadir}/bash-completion/completions/dconf-editor
%{_datadir}/dbus-1/services/ca.desrt.dconf-editor.service
%{_datadir}/glib-2.0/schemas/ca.desrt.dconf-editor.gschema.xml
%{_datadir}/icons/hicolor/
%{_mandir}/man1/dconf-editor.1%{?ext_man}

%files lang -f %{name}.lang

%changelog
