#
# spec file for package gthumb
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


Name:           gthumb
Version:        4.0
Release:        0
Summary:        An Image Viewer and Browser for GNOME
License:        GPL-2.0-or-later
Group:          Productivity/Graphics/Viewers
URL:            https://gitlab.gnome.org/GNOME/gthumb
Source0:        %{name}-%{version}.tar.xz

BuildRequires:  AppStream
BuildRequires:  c++_compiler
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  giflib-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libtiff-devel
BuildRequires:  meson
BuildRequires:  vala
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(appstream) >= 0.14.6
BuildRequires:  pkgconfig(colord) >= 1.3
BuildRequires:  pkgconfig(exiv2) >= 0.28
BuildRequires:  pkgconfig(glib-2.0) >= 2.36.0
BuildRequires:  pkgconfig(gsettings-desktop-schemas)
BuildRequires:  pkgconfig(gstreamer-1.0) >= 1.0.0
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  pkgconfig(gstreamer-video-1.0)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(lcms2) >= 2.6
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libheif) >= 1.11
BuildRequires:  pkgconfig(libjxl)
BuildRequires:  pkgconfig(libjxl_threads)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libportal)
BuildRequires:  pkgconfig(libportal-gtk4)
BuildRequires:  pkgconfig(libraw) >= 0.14
BuildRequires:  pkgconfig(librsvg-2.0) >= 2.34.0
BuildRequires:  pkgconfig(libwebp) >= 0.2.0
BuildRequires:  pkgconfig(libwebpdemux)
BuildRequires:  pkgconfig(zlib)
Obsoletes:      %{name}-devel < %{version}

%description
gThumb lets you browse your hard disk, showing you thumbnails of image
files. It also lets you view single files (including GIF animations),
add comments to images, organize images in catalogs, print images, view
slide shows, set your desktop background, and more.

%lang_package

%prep
%autosetup -p1

%build
%meson \
	%{nil}
%meson_build

%install
%meson_install
%find_lang %{name} %{?no_lang_C}
%fdupes %{buildroot}%{_prefix}

%check
%meson_test

%files
%license COPYING
%doc MAINTAINERS NEWS README.md
%{_bindir}/gthumb
%{_libexecdir}/gthumb/
%{_datadir}/applications/org.gnome.gthumb.desktop
%{_datadir}/icons/hicolor/*/apps/org.gnome.gthumb.png
%{_datadir}/icons/hicolor/*/apps/org.gnome.gthumb-symbolic.svg
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.gthumb.svg
%{_datadir}/glib-2.0/schemas/org.gnome.gthumb.*.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.gthumb.gschema.xml
%{_datadir}/metainfo/org.gnome.gthumb.metainfo.xml
%{_mandir}/man1/gthumb.1%{?ext_man}

%files lang -f %{name}.lang

%changelog
