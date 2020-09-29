#
# spec file for package pix
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


Name:           pix
Version:        2.4.11
Release:        0
Summary:        Image viewer and browser utility
License:        GPL-2.0-or-later
Group:          Productivity/Graphics/Viewers
URL:            https://github.com/linuxmint/pix
Source:         https://github.com/linuxmint/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
#PATCH-FIX-UPSTREAM dead_mozay@opensuse.org - exiv2 0.27 Exiv2::Error has changed from an int to an Exiv2::ErrorCode enum
Patch0:         pix-exiv2-error.patch
BuildRequires:  bison
BuildRequires:  dcraw
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  gnome-common
BuildRequires:  itstool
BuildRequires:  libjpeg-devel
BuildRequires:  libtiff-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(clutter-1.0) >= 1.0.0
BuildRequires:  pkgconfig(clutter-gtk-1.0) >= 1.0.0
BuildRequires:  pkgconfig(exiv2) >= 0.21
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.34.0
BuildRequires:  pkgconfig(gsettings-desktop-schemas)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  pkgconfig(gstreamer-video-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(libbrasero-burn3) >= 3.2.0
# Disabled until upstreams ports to current libopenraw
#BuildRequires:  pkgconfig(libopenraw-0.1)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(librsvg-2.0) >= 2.34.0
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(libsoup-gnome-2.4) >= 2.36.0
BuildRequires:  pkgconfig(libwebp) >= 0.2.0
BuildRequires:  pkgconfig(sm) >= 1.0.0
BuildRequires:  pkgconfig(webkit2gtk-4.0)
BuildRequires:  pkgconfig(zlib)
Requires:       xapps-common
Recommends:     %{name}-lang
%glib2_gsettings_schema_requires

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

%prep
%autosetup -p1

%build
NOCONFIGURE=1 gnome-autogen.sh
export SUID_CFLAGS=-fPIE
export SUID_LDFLAGS=-pie
%configure\
  --disable-static       \
  --disable-silent-rules \
  --enable-libraw        \
  --with-smclient=xsmp
make %{?_smp_mflags} V=1

%install
%make_install

find %{buildroot} -type f -name "*.la" -delete -print
%suse_update_desktop_file %{name}
%suse_update_desktop_file %{name}-import
%find_lang %{name} %{?no_lang_C}
%fdupes %{buildroot}%{_prefix}

%if 0%{?suse_version} < 1500
%post
%desktop_database_post
%icon_theme_cache_post
%glib2_gsettings_schema_post

%postun
%desktop_database_postun
%icon_theme_cache_postun
%glib2_gsettings_schema_postun
%endif

%files
%license COPYING
%doc README debian/changelog
%doc %{_datadir}/help/C/%{name}/
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
%{_includedir}/%{name}-*/
%{_datadir}/aclocal/%{name}.m4
%{_libdir}/pkgconfig/%{name}-*.pc

%changelog
