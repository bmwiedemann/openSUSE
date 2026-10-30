#
# spec file for package sushi
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


%global __requires_exclude typelib\\(LOKDocView\\)

Name:           sushi
Version:        51.2
Release:        0
Summary:        Quick Previewer for Nautilus
License:        SUSE-GPL-2.0-with-plugin-exception and GPL-2.0-or-later
Group:          Productivity/File utilities
URL:            https://gitlab.gnome.org/GNOME/sushi
Source0:        %{name}-%{version}.tar.xz
Source99:       sushi-rpmlintrc

BuildRequires:  blueprint-compiler
BuildRequires:  gjs
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildSystem:    meson

%description
Sushi is a quick previewer for Nautilus, the GNOME desktop file manager.

%lang_package

%generate_buildrequires
%meson_buildrequires

%install -a
sed -i 's|/usr/bin/env -S /usr/bin/gjs -m|/usr/bin/gjs -m|' %{buildroot}/usr/bin/sushi
sed -i 's|/usr/bin/env -S /usr/bin/gjs -m|/usr/bin/gjs -m|' %{buildroot}/usr/libexec/org.gnome.NautilusPreviewer
%find_lang %{name} %{?no_lang_C}

%files
%license COPYING
%doc AUTHORS NEWS README.md
%{_bindir}/%{name}
%{_datadir}/applications/org.gnome.NautilusPreviewer.desktop
%{_datadir}/dbus-1/services/org.gnome.NautilusPreviewer.service
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.NautilusPreviewer.svg
%{_datadir}/metainfo/org.gnome.NautilusPreviewer.metainfo.xml
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/gir-1.0
%{_datadir}/%{name}/gir-1.0/Sushi-1.0.gir
%{_datadir}/%{name}/org.gnome.NautilusPreviewer.data.gresource
%{_datadir}/%{name}/org.gnome.NautilusPreviewer.src.gresource
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/girepository-1.0
%{_libdir}/%{name}/girepository-1.0/Sushi-1.0.typelib
%{_libdir}/%{name}/libsushi-1.0.so
%dir %{_libdir}/%{name}/web-process-extensions
%{_libdir}/%{name}/web-process-extensions/libsushiwebprocessextension.so
%{_libexecdir}/org.gnome.NautilusPreviewer

%files lang -f %{name}.lang

%changelog
