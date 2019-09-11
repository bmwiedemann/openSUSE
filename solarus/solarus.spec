#
# spec file for package solarus
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           solarus
Version:        1.6.0
Release:        0
Summary:        Zelda-like game engine
License:        GPL-3.0-or-later
Group:          Amusements/Games/RPG
Url:            http://www.solarus-engine.org/
Source:         http://www.solarus-games.org/downloads/solarus/%{name}-%{version}-src.tar.gz
# PATCH-FIX-UPSTREAM solarus-1.6.0-fix-desktop-exec.patch -- wrong Exec field in desktop file
Patch0:         solarus-1.6.0-fix-desktop-exec.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  physfs-devel
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Help)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(SDL2_image)
BuildRequires:  pkgconfig(SDL2_ttf)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(libmodplug)
BuildRequires:  pkgconfig(luajit)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(vorbis)

%description
Solarus is a Zelda-like game engine written in C++.

%package -n libsolarus1
Summary:        Zelda-like game engine
Group:          System/Libraries

%description -n libsolarus1
Solarus is a Zelda-like game engine written in C++.

%package devel
Summary:        Development files for solarus
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

%description devel
Development files for solarus, including header-files.

%prep
%setup -q
%patch0 -p1

%build
%cmake
make %{?_smp_mflags}

%install
%cmake_install

%if 0%{?suse_version} < 1330
%post
%icon_theme_cache_post
%desktop_database_post

%postun
%icon_theme_cache_postun
%desktop_database_postun
%endif

%post   -n libsolarus1 -p /sbin/ldconfig
%postun -n libsolarus1 -p /sbin/ldconfig

%files
%doc changelog.txt readme.md
%license license.txt
%{_bindir}/solarus-launcher
%{_bindir}/solarus-run
%dir %{_datadir}/appdata/
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_libdir}/libsolarus-gui.so
%{_mandir}/man6/solarus*

%files -n libsolarus1
%{_libdir}/libsolarus.so.*

%files devel
%{_includedir}/solarus
%{_libdir}/libsolarus.so

%changelog
