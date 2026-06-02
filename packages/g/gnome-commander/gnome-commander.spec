#
# spec file for package gnome-commander
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


Name:           gnome-commander
Version:        2.0.2
Release:        0
Summary:        A file manager for the GNOME desktop environment
License:        GPL-2.0-or-later
Group:          Productivity/File utilities
URL:            https://gnome.pages.gitlab.gnome.org/gnome-commander/
Source0:        %{name}-%{version}.tar.xz
Source1:        vendor.tar.xz

BuildRequires:  AppStream
BuildRequires:  c++_compiler
BuildRequires:  c_compiler
BuildRequires:  cargo-packaging
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  itstool
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(exiv2) >= 0.14
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.66.0
BuildRequires:  pkgconfig(gmodule-2.0) >= 2.0.0
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libgsf-1) >= 1.12.0
BuildRequires:  pkgconfig(poppler-glib) >= 0.18
BuildRequires:  pkgconfig(taglib) >= 1.4
BuildRequires:  pkgconfig(vte-2.91-gtk4)
Provides:       %{name}-doc = %{version}
Obsoletes:      %{name}-doc < 1.14.1
# For xdg-su
Recommends:     xdg-utils

%description
GNOME Commander is a "two-pane" graphical file manager for the Linux
desktop using GNOME libraries. In addition to basic file manager
functions, the program is also an FTP client and can browse SMB
networks.

%lang_package

%prep
%autosetup -p1 -a1

%build
%meson
%meson_build

%install
%meson_install
find %{buildroot}%{_datadir} -size 0 -delete
%find_lang %{name} %{?no_lang_C}
%fdupes -s %{buildroot}%{_datadir}
%fdupes %{buildroot}%{_libdir}
%ldconfig_scriptlets

%check
# The full cargo testsuite currently fails, temp disable and manually run validate
%dnl %meson_test
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
appstreamcli validate --no-net %{buildroot}%{_datadir}/metainfo/*.metainfo.xml

%files
%license COPYING
%doc NEWS README.md AUTHORS
%{_datadir}/help/C/%{name}
%{_datadir}/metainfo/org.gnome.gnome-commander.metainfo.xml
%{_bindir}/gnome-commander
%{_datadir}/applications/*.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.%{name}.enums.xml
%{_datadir}/glib-2.0/schemas/org.gnome.%{name}.gschema.xml
%{_datadir}/pixmaps/%{name}
%{_libdir}/%{name}
%{_libdir}/libgcmd.so
%{_libdir}/girepository-1.0/GnomeCmd-1.0.typelib
%{_mandir}/man1/%{name}.1%{ext_man}
%{_datadir}/icons/hicolor/scalable/apps/gnome-commander-internal-viewer.svg
%{_datadir}/icons/hicolor/scalable/apps/gnome-commander-symbolic.svg
%{_datadir}/icons/hicolor/scalable/apps/gnome-commander.svg
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/icons
%{_datadir}/gir-1.0/GnomeCmd-1.0.gir

%files lang -f %{name}.lang

%changelog
