#
# spec file for package openclonk
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


Name:           openclonk
Version:        8.1
Release:        0
Summary:        Fast-paced 2D genre mix
License:        ISC AND CC-BY-3.0
Group:          Amusements/Games/Action/Other
Url:            http://www.openclonk.org/
Source:         http://www.openclonk.org/builds/release/%{version}/%{name}-%{version}-src.tar.bz2
# PATCH-FIX-UPSTREAM Fix https://github.com/openclonk/openclonk/pull/26
Patch1:         fix-CMakeLists.patch
BuildRequires:  cmake >= 3.0.2
BuildRequires:  hicolor-icon-theme
BuildRequires:  libjpeg-devel
BuildRequires:  pkgconfig
BuildRequires:  readline-devel
BuildRequires:  shared-mime-info
BuildRequires:  tinyxml-devel
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(SDL2_mixer)
BuildRequires:  pkgconfig(dri)
BuildRequires:  pkgconfig(freealut)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glew)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtksourceview-3.0)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libupnp)
BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xpm)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xxf86vm)
BuildRequires:  pkgconfig(zlib)
%if 0%{?suse_version} == 1315
BuildRequires:  gcc5-c++
%else
BuildRequires:  gcc-c++ >= 4.9
%endif
Requires:       %{name}-data = %{version}
ExclusiveArch:  %{ix86} x86_64

%description
Clonks are witty and nimble human-like creatures.
They build, run, dig and fight: everything in
real-time and in direct control, alone, with or
versus other players.

%package data
Summary:        Data files for %{name}
Group:          Amusements/Games/Action/Other
BuildArch:      noarch

%description data
This package contains the data files for %{name}.

%prep
%setup -q -n %{name}-release-%{version}-src
%patch1 -p1

rm -rf planet/Tests.c4f
chmod 644 COPYING TRADEMARK

%build
%cmake \
    -DOC_SYSTEM_DATA_DIR=%{_datadir}/%{name} \
    -DOC_SYSTEM_GAMES_DIR=%{_bindir} \
    -DCMAKE_CONFIGURATION_TYPE=RelWithDebInfo \
    -DUSE_GCC_STYLE_LTCG:BOOL=OFF \
    -DBUILD_SHARED_LIBS:BOOL=OFF \
%if 0%{?suse_version} == 1315
    -DCMAKE_C_COMPILER=gcc-5 \
    -DCMAKE_CXX_COMPILER=g++-5
%endif

make %{?_smp_mflags}

%install
%cmake_install

%if 0%{?suse_version} < 1330
%post
%desktop_database_post
%icon_theme_cache_post
%mime_database_post

%postun
%desktop_database_postun
%icon_theme_cache_postun
%mime_database_postun
%endif

%files
%doc TRADEMARK
%license COPYING
%{_bindir}/%{name}
%{_bindir}/c4group
%{_datadir}/appdata/openclonk.appdata.xml
%{_datadir}/applications/openclonk.desktop
%{_datadir}/icons/hicolor/*/apps/openclonk.png
%if 0%{?suse_version} <= 1320
%dir %{_datadir}/appdata/
%dir %{_datadir}/icons/hicolor/512x512
%dir %{_datadir}/icons/hicolor/512x512/apps
%endif

%files data
%license COPYING
%{_datadir}/%{name}

%changelog
