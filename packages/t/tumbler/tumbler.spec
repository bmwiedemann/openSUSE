#
# spec file for package tumbler
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


%bcond_with git
%bcond_with libffmpegthumbnailer
%define libname libtumbler-1-0

Name:           tumbler
Version:        4.18.0
Release:        0
Summary:        Thumbnail Management for Xfce
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Productivity/Graphics/Other
URL:            https://docs.xfce.org/xfce/thunar/tumbler
Source:         https://archive.xfce.org/src/xfce/%{name}/4.18/%{name}-%{version}.tar.bz2
Source1:        custom_thumbnailers.tar.gz
BuildRequires:  intltool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gio-2.0) >= 2.50.0
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.50.0
BuildRequires:  pkgconfig(glib-2.0) >= 2.50.0
BuildRequires:  pkgconfig(gmodule-2.0) >= 2.50.0
BuildRequires:  pkgconfig(gthread-2.0) >= 2.50.0
BuildRequires:  pkgconfig(libxfce4util-1.0) >= 4.17.1
# GdkPibuxf thumbnailer plugin
BuildRequires:  pkgconfig(gdk-pixbuf-2.0) >= 2.14
# FreeType2 font thumbnailer plugin
BuildRequires:  pkgconfig(freetype2)
# JPEG thumbnailer plugin with EXIF support
BuildRequires:  pkgconfig(libjpeg)
%if %{with libffmpegthumbnailer}
# ffmpeg video thumbnailer plugin
BuildRequires:  pkgconfig(libffmpegthumbnailer)
%endif
# gstreamer video thumbnailer plugin
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
# poppler PDF/PS thumbnailer plugin
BuildRequires:  pkgconfig(poppler-glib)
# ODF thumbnailer plugin
BuildRequires:  pkgconfig(libgsf-1)
# libopenraw thumbnailer plugin
BuildRequires:  libopenraw-devel
# freedesktop.org cache plugin
BuildRequires:  pkgconfig(libpng)
# OMDB cover plugin
BuildRequires:  pkgconfig(libcurl)
# EPUB Plugin
BuildRequires:  (pkgconfig(libgepub-0.6) or pkgconfig(libgepub-0.7))
%if %{with git}
BuildRequires:  xfce4-dev-tools
%endif
# no matter what rpmlint says, we need the same lib-version
Requires:       %libname = %{version}
Recommends:     ffmpegthumbnailer

%description
Tumbler is a D-Bus service for applications to request thumbnails for various
URI schemes and MIME types. It is an implementation of the thumbnail management
D-Bus specification described on http://live.gnome.org/ThumbnailerSpec and
extensible through a plugin interface or via specialized thumbnailer services
implemented in accordance to the thumbnail management D-Bus specification.

%package -n %{name}-folder-thumbnailer
Summary:        Thumbnailer for folders
Group:          Productivity/Graphics/Other
Requires:       ImageMagick
Suggests:       thunar >= 1.8.2
Supplements:    (%{name} and thunar)

%description -n %{name}-folder-thumbnailer
A thumbnailer to show custom folder thumbnails in Thunar

%package -n %{name}-webp-thumbnailer
Summary:        Thumbnailer for WebP images
Group:          Productivity/Graphics/Other
Requires:       ImageMagick
Supplements:    (%{name} and ImageMagick)

%description -n %{name}-webp-thumbnailer
A thumbnailer for WebP images

%package -n %{libname}
Summary:        Tumbler Library
Group:          System/Libraries
Recommends:     %{name}-lang = %{version}

%description -n %{libname}
This package provides the shared library component of tumbler.

%package devel
Summary:        Development Files for tumbler
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Recommends:     %{name}-doc = %{version}

%description devel
This package contains the development files needed for developing tumbler
plugins.

%package doc
Summary:        Developer Documentation for tumbler
Group:          Documentation/HTML
BuildArch:      noarch

%description doc
This package provides the developer documentation for tumbler.

%package lang
Summary:        Languages for package %{name}
Group:          System/Localization
Requires:       %{libname} = %{version}
Provides:       %{name}-lang-all = %{version}
Supplements:    packageand(bundle-lang-other:%{libname})
BuildArch:      noarch

%description lang
Provides translations to the package %{name}

%prep
%autosetup
sed -i "s/libopenraw-gnome-1.0/libopenraw-gnome-0.1/g" acinclude.m4
pkg-config --exists libgepub-0.7 && sed -i "s/gepub-0.6/gepub-0.7/g" configure || true

tar -xzf %SOURCE1

%build
%if %{with git}
NOCONFIGURE=1 ./autogen.sh
%configure \
	--disable-static
%else
%configure
%endif
%make_build

%install
%make_install

find %{buildroot} -type f -name "*.la" -delete -print

rm -rf %{buildroot}%{_datadir}/locale/{ast,kk,tl_PH,ur_PK}

%find_lang %{name} %{?no_lang_C}

mkdir %{buildroot}%{_datadir}/thumbnailers
mv custom_thumbnailers/*.thumbnailer %{buildroot}%{_datadir}/thumbnailers/
mkdir %{buildroot}%{_bindir}
mv custom_thumbnailers/folder-thumbnailer %{buildroot}%{_bindir}/

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README.md
%dir %{_sysconfdir}/xdg/tumbler/
%config(noreplace) %{_sysconfdir}/xdg/tumbler/tumbler.rc
%dir %{_libdir}/tumbler-1
%{_libdir}/tumbler-1/tumblerd
%dir %{_libdir}/tumbler-1/plugins
%dir %{_libdir}/tumbler-1/plugins/cache
%{_libdir}/tumbler-1/plugins/cache/tumbler-xdg-cache.so
%{_libdir}/tumbler-1/plugins/cache/tumbler-cache-plugin.so
%{_libdir}/tumbler-1/plugins/tumbler-cover-thumbnailer.so
%{_libdir}/tumbler-1/plugins/tumbler-desktop-thumbnailer.so
%if %{with libffmpegthumbnailer}
%{_libdir}/tumbler-1/plugins/tumbler-ffmpeg-thumbnailer.so
%endif
%{_libdir}/tumbler-1/plugins/tumbler-font-thumbnailer.so
%{_libdir}/tumbler-1/plugins/tumbler-gst-thumbnailer.so
%{_libdir}/tumbler-1/plugins/tumbler-jpeg-thumbnailer.so
%{_libdir}/tumbler-1/plugins/tumbler-odf-thumbnailer.so
%{_libdir}/tumbler-1/plugins/tumbler-pixbuf-thumbnailer.so
%{_libdir}/tumbler-1/plugins/tumbler-poppler-thumbnailer.so
%{_libdir}/tumbler-1/plugins/tumbler-raw-thumbnailer.so
%{_libdir}/tumbler-1/plugins/tumbler-gepub-thumbnailer.so
%dir %{_datadir}/dbus-1
%dir %{_datadir}/dbus-1/services
%{_datadir}/dbus-1/services/*.service
%dir %{_datadir}/thumbnailers
%dir %{_datadir}/icons/hicolor
%{_datadir}/icons/hicolor/*
%{_prefix}/lib/systemd/user/tumblerd.service

%files -n %{name}-folder-thumbnailer
%{_bindir}/folder-thumbnailer
%{_datadir}/thumbnailers/folder.thumbnailer

%files -n %{name}-webp-thumbnailer
%{_datadir}/thumbnailers/webp.thumbnailer

%files -n %{libname}
%license COPYING
%{_libdir}/libtumbler-1.so.*

%files lang -f %{name}.lang

%files devel
%{_includedir}/tumbler-1
%{_libdir}/pkgconfig/tumbler-1.pc
%{_libdir}/libtumbler-1.so

%files doc
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html
%doc %{_datadir}/gtk-doc/html/tumbler

%changelog
