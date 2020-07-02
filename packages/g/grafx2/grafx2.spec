#
# spec file for package grafx2
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           grafx2
Version:        2.7.2950
Release:        0
Summary:        Pixel Art editor
License:        GPL-2.0-only
Group:          Productivity/Graphics/Bitmap Editors
URL:            http://grafx2.tk
Source:         https://gitlab.com/GrafX2/grafX2/-/jobs/428763304/artifacts/raw/grafx2-%{version}-src.tgz
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(SDL_image)
BuildRequires:  pkgconfig(SDL_ttf)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(lua)
BuildRequires:  pkgconfig(sdl)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  libtiff-devel
BuildRequires:  libpng16-devel

%description
GrafX2 is a bitmap paint program inspired by the Amiga programs Deluxe Paint and Brilliance

%prep
%setup -q -n grafx2

%build
cd src
make %{?_smp_mflags}

%install
cd src
make install PREFIX=%{_prefix} DESTDIR=%{buildroot}

mkdir -p %{buildroot}%{_datadir}/applications
mkdir -p %{buildroot}%{_datadir}/metainfo

%suse_update_desktop_file grafx2 -r Graphics 2DGraphics

mkdir -p %{buildroot}%{_datadir}/pixmaps
mv %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/grafx2.xpm %{buildroot}%{_datadir}/pixmaps/grafx2.xpm
mv %{buildroot}%{_bindir}/grafx2-sdl %{buildroot}%{_bindir}/grafx2

%if 0%{?suse_version} < 1500
%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun
%endif

%files
%{_bindir}/grafx2
%{_datadir}/grafx2
%{_datadir}/applications/grafx2.desktop
%{_datadir}/metainfo/grafx2.appdata.xml
%{_datadir}/pixmaps/grafx2.xpm
%{_datadir}/icons/hicolor/scalable/apps/grafx2.svg

%changelog
