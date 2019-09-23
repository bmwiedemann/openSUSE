#
# spec file for package aseprite
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%if 0%{?suse_version} == 1315 && !0%{?is_opensuse}
# No tinyxml on SLE
%bcond_with tinyxml
%else
%bcond_without tinyxml
%endif
Name:           aseprite
Version:        1.1.7
Release:        0
Summary:        Animated sprite editor & pixel art tool
License:        GPL-2.0+ and MIT
Group:          Productivity/Graphics/Bitmap Editors
Source:         %{name}-%{version}.tar.bz2
# PATCH-FIX-UPSTREAM https://github.com/aseprite-gpl/aseprite/pull/7
Patch1:         appdata.patch
# PATCH-FIX-UPSTREAM https://github.com/aseprite-gpl/aseprite/pull/13
Patch2:         shared-gtest.patch
Url:            http://www.aseprite.org
BuildRequires:  cmake >= 2.6
BuildRequires:  gcc-c++
BuildRequires:  glibc-devel
BuildRequires:  pkgconfig(allegro)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  giflib-devel >= 5.1.0
BuildRequires:  gimp-devel
BuildRequires:  gtk2-devel
BuildRequires:  pkgconfig(libart-2.0)
BuildRequires:  libjpeg-devel
BuildRequires:  googletest-devel
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(loadpng)
%if %{with tinyxml}
BuildRequires:  tinyxml-devel
%endif
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xpm)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xxf86vm)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(xxf86dga)
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  update-desktop-files
BuildRequires:  shared-mime-info
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Aseprite is an open source program to create animated sprites
for websites and games.

%prep
%setup -q
%patch1 -p1
%patch2 -p1

# https://github.com/aseprite/aseprite/issues/617
rm -r third_party/{curl,freetype2,giflib,gtest,jpeg,libpng,libwebp,libwebp-cmake,loadpng,pixman-cmake,zlib}
%if %{with tinyxml}
rm -r third_party/tinyxml
%endif

%build
%cmake .. -DUSE_SHARED_ALLEGRO4=ON \
          -DUSE_SHARED_CURL=ON \
          -DUSE_SHARED_GIFLIB=ON \
          -DUSE_SHARED_JPEGLIB=ON \
          -DUSE_SHARED_LIBLOADPNG=ON \
          -DUSE_SHARED_LIBPNG=ON \
          -DUSE_SHARED_ZLIB=ON \
          -DUSE_SHARED_PIXMAN=ON \
          -DUSE_SHARED_FREETYPE=ON \
          -DUSE_SHARED_LIBWEBP=ON \
          -DUSE_SHARED_GTEST=ON \
          -DFULLSCREEN_PLATFORM=ON \
          %if %{with tinyxml}
          -DUSE_SHARED_TINYXML=ON \
          %endif
          -DWITH_DESKTOP_INTEGRATION=ON \
          -DENABLE_UPDATER=OFF

make aseprite %{?_smp_mflags}

%install
%cmake_install

install -m0644 -D data/icons/ase16.png %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
install -m0644 -D data/icons/ase32.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
install -m0644 -D data/icons/ase48.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
install -m0644 -D data/icons/ase64.png %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/%{name}.png

%fdupes -s %{buildroot}%{_datadir}

%post
%desktop_database_post
%icon_theme_cache_post
%mime_database_post

%postun
%desktop_database_postun
%icon_theme_cache_postun
%mime_database_postun

%files
%defattr(-,root,root)
%doc README.md LICENSE.txt
%{_bindir}/%{name}
%{_bindir}/%{name}-thumbnailer
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/thumbnailers/
%{_datadir}/icons/hicolor/
%dir %{_datadir}/appdata/
%{_datadir}/appdata/aseprite.appdata.xml

%changelog
