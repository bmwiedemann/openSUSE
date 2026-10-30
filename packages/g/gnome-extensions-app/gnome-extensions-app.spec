#
# spec file for package gnome-extensions-app
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


Name:           gnome-extensions-app
Version:        51.alpha
Release:        0
Summary:        Small app for managing GNOME Shell extensions
License:        GPL-2.0-or-later
URL:            https://gitlab.gnome.org/GNOME/gnome-extensions-app
Source0:        %{name}-%{version}.tar.xz
Source1:        libshew-0.gitmodule.tar.xz

BuildRequires:  AppStream
BuildRequires:  desktop-file-utils
BuildRequires:  gjs
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
Provides:       gnome-extensions = %{version}
Obsoletes:      gnome-extensions < %{version}

%description
GNOME Extensions is a small app for managing GNOME Shell
extensions.

%lang_package

%prep
%autosetup -p1
pushd subprojects
tar xf %{SOURCE1}
mv libshew-0.gitmodule libshew
popd

%build
%meson \
	%{nil}
%meson_build

%install
%meson_install
%find_lang %{name} %{?no_lang_C}
# Not needed, only used for nightly git snapshots
rm -f %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/org.gnome.Extensions.Devel.svg

%check
%meson_test

%files
%license COPYING
%doc README.md
%{_bindir}/gnome-extensions-app
%dir %{_libdir}/gnome-extensions-app
%dir %{_libdir}/gnome-extensions-app/girepository-1.0
%{_libdir}/gnome-extensions-app/girepository-1.0/Shew-0.typelib
%{_libdir}/gnome-extensions-app/libshew-0.so
%{_datadir}/applications/org.gnome.Extensions.desktop
%{_datadir}/dbus-1/services/org.gnome.Extensions.service
%{_datadir}/glib-2.0/schemas/org.gnome.Extensions.gschema.xml
%dir %{_datadir}/gnome-extensions-app
%{_datadir}/gnome-extensions-app/org.gnome.Extensions
%{_datadir}/gnome-extensions-app/org.gnome.Extensions.data.gresource
%{_datadir}/gnome-extensions-app/org.gnome.Extensions.src.gresource
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.Extensions.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.Extensions-symbolic.svg
%{_datadir}/metainfo/org.gnome.Extensions.metainfo.xml

%files lang -f %{name}.lang

%changelog

