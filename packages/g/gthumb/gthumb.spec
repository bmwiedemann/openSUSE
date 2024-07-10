#
# spec file for package gthumb
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


Name:           gthumb
Version:        3.12.6
Release:        0
# FIXME: Add libchamplain BuildRequires once the map feature is considered stable.
Summary:        An Image Viewer and Browser for GNOME
License:        GPL-2.0-or-later
Group:          Productivity/Graphics/Viewers
URL:            https://wiki.gnome.org/Apps/gthumb
Source0:        %{name}-%{version}.tar.zst

BuildRequires:  AppStream
BuildRequires:  bison
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  gnome-doc-utils-devel
BuildRequires:  intltool >= 0.50.1
BuildRequires:  itstool
BuildRequires:  libjpeg-devel
BuildRequires:  libtiff-devel
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(appstream) >= 0.14.6
BuildRequires:  pkgconfig(champlain-0.12) >= 0.12.0
BuildRequires:  pkgconfig(champlain-gtk-0.12) >= 0.12.0
BuildRequires:  pkgconfig(clutter-1.0) >= 1.12.0
BuildRequires:  pkgconfig(clutter-gtk-1.0) >= 1.0.0
BuildRequires:  pkgconfig(colord) >= 1.3
BuildRequires:  pkgconfig(exiv2) >= 0.21
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.36.0
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gsettings-desktop-schemas)
BuildRequires:  pkgconfig(gstreamer-1.0) >= 1.0.0
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  pkgconfig(gstreamer-video-1.0)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.16
BuildRequires:  pkgconfig(json-glib-1.0) >= 0.15.0
BuildRequires:  pkgconfig(lcms2) >= 2.6
BuildRequires:  pkgconfig(libbrasero-burn3) >= 3.2.0
BuildRequires:  pkgconfig(libheif) >= 1.11
BuildRequires:  pkgconfig(libjxl)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libraw) >= 0.14
BuildRequires:  pkgconfig(librsvg-2.0) >= 2.34.0
BuildRequires:  pkgconfig(libsecret-1) >= 0.11
BuildRequires:  pkgconfig(libsoup-2.4) >= 2.42
BuildRequires:  pkgconfig(libwebp) >= 0.2.0
BuildRequires:  pkgconfig(zlib)
%if 0%{?suse_version} < 1315
BuildRequires:  pkgconfig(webkit2gtk-3.0)
%else
BuildRequires:  pkgconfig(webkit2gtk-4.0)
%endif

%description
gThumb lets you browse your hard disk, showing you thumbnails of image
files. It also lets you view single files (including GIF animations),
add comments to images, organize images in catalogs, print images, view
slide shows, set your desktop background, and more.

%package devel
Summary:        An Image Viewer and Browser for GNOME - Development Files
Group:          Development/Libraries/GNOME
Requires:       %{name} = %{version}

%description devel
gThumb lets you browse your hard disk, showing you thumbnails of image
files. It also lets you view single files (including GIF animations),
add comments to images, organize images in catalogs, print images, view
slide shows, set your desktop background, and more.

%lang_package

%prep
%autosetup -p1

%build
%meson \
	-Dlibchamplain=true \
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
%doc AUTHORS NEWS README.md
%doc %{_datadir}/help/C/%{name}/
%{_bindir}/gthumb
%{_datadir}/gthumb/
%{_libdir}/gthumb/
%{_libexecdir}/gthumb/
%if 0%{?sle_version} > 150300 || 0%{?suse_version} > 1590
%dir %{_datadir}/metainfo/
%{_datadir}/metainfo/org.gnome.gThumb.appdata.xml
%endif
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/org.gnome.gThumb*
%{_datadir}/glib-2.0/schemas/org.gnome.gthumb.*.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.gthumb.enums.xml
%{_datadir}/glib-2.0/schemas/org.gnome.gthumb.gschema.xml
%{_mandir}/man1/gthumb.1%{?ext_man}

%files devel
%doc MAINTAINERS
%{_includedir}/%{name}/
%{_datadir}/aclocal/gthumb.m4
%{_libdir}/pkgconfig/*.pc

%files lang -f %{name}.lang

%changelog
