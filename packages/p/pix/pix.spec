#
# spec file for package pix
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           pix
Version:        3.4.7
Release:        0
Summary:        Image viewer and browser utility
License:        GPL-2.0-or-later
URL:            https://github.com/linuxmint/pix
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  bison
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  itstool
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(clutter-1.0) >= 1.0.0
BuildRequires:  pkgconfig(clutter-gtk-1.0) >= 1.0.0
BuildRequires:  pkgconfig(colord)
BuildRequires:  pkgconfig(exiv2) >= 0.21
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.34.0
BuildRequires:  pkgconfig(gsettings-desktop-schemas)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  pkgconfig(gstreamer-video-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libbrasero-burn3) >= 3.2.0
BuildRequires:  pkgconfig(libheif)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libjxl)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libraw)
BuildRequires:  pkgconfig(librsvg-2.0) >= 2.34.0
BuildRequires:  pkgconfig(libsecret-1)
%dnl BuildRequires:  pkgconfig(libsoup-2.4) >= 2.36.0
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(libwebp) >= 0.2.0
BuildRequires:  pkgconfig(sm) >= 1.0.0
%dnl BuildRequires:  pkgconfig(webkit2gtk-4.1)
BuildRequires:  pkgconfig(xapp) >= 2.5.0
BuildRequires:  pkgconfig(zlib)

%description
pix lets you browse your hard disk, showing you thumbnails of
image files.
It also lets you view single files (including GIF animations), add
comments to images, organise images in catalogs, print images, view
slide shows, set your desktop background, and more.

%lang_package

%package devel
Summary:        Image viewer and browser utility -- Development Files
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

%description devel
pix lets you browse your hard disk, showing you thumbnails of
image files.
It also lets you view single files (including GIF animations), add
comments to images, organise images in catalogs, print images, view
slide shows, set your desktop background, and more.

%package doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%description doc
This package offers you extended HTML documentation for %{name}

%prep
%autosetup

%build
%meson \
  -Dwarn-deprecated=true \
  -Drun-in-place=false \
  -Dexiv2=true \
  -Dclutter=true \
  -Dgstreamer=true \
  -Dlibchamplain=true \
  -Dlcms2=true \
  -Dcolord=true \
  -Dlibtiff=true \
  -Dlibwebp=true \
  -Dlibjxl=true \
  -Dlibheif=true \
  -Dlibraw=true \
  -Dlibrsvg=true \
  -Dlibsecret=true \
  -Dwebservices=false \
  -Dlibbrasero=true
%meson_build

%install
%meson_install

%suse_update_desktop_file %{name}
%suse_update_desktop_file %{name}-import
%find_lang %{name} %{?no_lang_C}
%fdupes %{buildroot}

%files
%license COPYING
%doc README.md AUTHORS MAINTAINERS PERFORMANCE
%{_bindir}/%{name}
%{_libdir}/%{name}/
%{_datadir}/%{name}/
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}*.*
%{_datadir}/glib-2.0/schemas/*%{name}*.gschema.xml
%{_datadir}/glib-2.0/schemas/*%{name}.enums.xml
%{_mandir}/man1/%{name}.1%{?ext_man}

%files lang -f %{name}.lang

%files devel
%{_includedir}/%{name}
%{_datadir}/aclocal/%{name}.m4
%{_libdir}/pkgconfig/%{name}.pc

%files doc
%{_datadir}/help/C/%{name}

%changelog
