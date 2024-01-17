#
# spec file for package gnome-screenshot
#
# Copyright (c) 2022 SUSE LLC
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


Name:           gnome-screenshot
Version:        41.0
Release:        0
Summary:        Utility to take pictures of your screen
License:        GPL-2.0-or-later
Group:          System/GUI/GNOME
URL:            https://www.gnome.org
Source:         https://download.gnome.org/sources/gnome-screenshot/41/%{name}-%{version}.tar.xz
# PATCH-FIX-OPENSUSE gnome-screenshot-onlyshowin.patch dimstar@opensuse.org -- OnlyShowIn=GNOME: fix brp build check, allowing to use the icon from the gnome theme.
Patch0:         gnome-screenshot-onlyshowin.patch
# PATCH-FIX-UPSTREAM b60dad3c2536c17bd201f74ad8e40eb74385ed9f.patch -- Fix build with meson 0.60 and newer
Patch1:         https://gitlab.gnome.org/GNOME/gnome-screenshot/-/commit/b60dad3c2536c17bd201f74ad8e40eb74385ed9f.patch

BuildRequires:  appstream-glib
BuildRequires:  desktop-file-utils
BuildRequires:  meson >= 0.50.0
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(glib-2.0) >= 2.35.1
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.12.0
BuildRequires:  pkgconfig(libcanberra-gtk3)
BuildRequires:  pkgconfig(libhandy-1) >= 0.90.0
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
Conflicts:      gnome-utils < 3.3.1

%description
The screenshot tool captures the screen, a window, or an user-defined
area and save the snapshot image to a file.

%lang_package

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name}

%check
%meson_test

%files
%license COPYING
%doc NEWS README.md
%{_bindir}/%{name}
%{_datadir}/applications/org.gnome.Screenshot.desktop
%{_datadir}/dbus-1/services/org.gnome.Screenshot.service
%{_datadir}/glib-2.0/schemas/org.gnome.gnome-screenshot.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.Screenshot.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.Screenshot-symbolic.svg
%{_datadir}/metainfo/org.gnome.Screenshot.metainfo.xml
%{_mandir}/man1/%{name}.1%{?ext_man}

%files lang -f %{name}.lang

%changelog
