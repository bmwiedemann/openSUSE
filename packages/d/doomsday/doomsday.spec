#
# spec file for package doomsday
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           doomsday
Version:        2.1.1
Release:        0
Summary:        The Doomsday Engine: DOOM/Hertic/Hexen port with pretty graphics
License:        GPL-2.0-or-later AND GPL-2.0-only AND SUSE-GPL-2.0-with-linking-exception AND BSD-3-Clause AND LGPL-3.0-or-later
Group:          Amusements/Games/3D/Shoot
Url:            http://dengine.net/

#Git-Web:	https://github.com/skyjake/Doomsday-Engine
#Git-Clone:	git://github.com/skyjake/Doomsday-Engine
Source:         Doomsday-Engine-%version.tar.xz
Source2:        %name-rpmlintrc
Patch1:         doomsday-no-abs-icon.patch
Patch2:         doomsday-libs.diff
Patch3:         doomsday-notime.diff
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  Mesa-devel
BuildRequires:  cmake
%if 0%{?suse_version} < 1500
BuildRequires:  gcc6-c++
%else
BuildRequires:  gcc-c++ >= 6
%endif
BuildRequires:  libpng-devel
BuildRequires:  ncurses-devel
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5OpenGL)
BuildRequires:  pkgconfig(Qt5OpenGLExtensions)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(SDL2_mixer)
BuildRequires:  pkgconfig(fluidsynth)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(minizip)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(zzip-zlib-config)
# Doomsday uses a modified version of assimp, so no pkgconfig(assimp) here :-(
Provides:       bundled(assimp) = 3.1.1

%if 0%{?suse_version}
Recommends:     timidity timidity-eawpats
%endif
Provides:       jdoom = %version-%release
Provides:       jheretic = %version-%release
Provides:       jhexen = %version-%release
Obsoletes:      deng < %version-%release
Provides:       deng = %version-%release
# Mesa 9.2 has OpenGL 3.1, and doomsday 2.0 needs that.
Requires:       Mesa-libGL1 >= 9.2

%description
The Doomsday Engine is a source port with support for Doom, Heretic,
and Hexen. It does not support BOOM extensions.

%package launcher
Summary:        Graphical launcher for Doomsday
Group:          Amusements/Games/3D/Shoot
Requires:       %name = %version
BuildRequires:  python
%if 0%{?fedora_version}
Requires:       wxPython
%else
%py_requires
Requires:       python-wxWidgets
%endif
%if 0%{?suse_version} >= 1130 || 0%{?fedora_version}
BuildArch:      noarch
%endif

%description launcher
Snowberry is the official frontend of the Doomsday Engine. It is a
portable graphical game launcher, with support for configuring the
various types of games supported by Doomsday. It offers to save your
settings for launching a particular game (e.g., Doom).

%prep
%autosetup -n Doomsday-Engine-%version -p1

%build
pushd doomsday
cf="%optflags"
%if 0%{?suse_version} > 1320
cf="$cf -Wno-narrowing"
%endif
%if 0%{?suse_version} < 1500
export CC=gcc-6 CXX=g++-6
%endif
%cmake
make -O %{?_smp_mflags}

%install
b="%buildroot"
pushd doomsday/
%cmake_install
popd
d="$b/%_libdir/doomsday"
rm -Rf "$b/%_includedir" "$b/%_libdir/cmake" "$b/%_datadir/doc/texc" \
	"$d/cmake" "$d/pkgconfig" "$d"/*.a
mkdir -p "$b/%_datadir/pixmaps"
ln -s "%_datadir/%name/deng-shell-logo-256.png" "$b/%_datadir/pixmaps/"
ln -s "%_datadir/%name/deng-logo-256.png" "$b/%_datadir/pixmaps/"

mkdir -p "$b/%_sysconfdir/doomsday";
cat >"$b/%_sysconfdir/doomsday/paths" <<-EOF
	basedir: %_datadir/doomsday
	libdir: %_libdir/doomsday
	iwaddir: %_datadir/doom
EOF

%post
echo "INFO: %name: The global IWAD directory is %_datadir/doom.";
/sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%dir %_sysconfdir/doomsday
%config %_sysconfdir/doomsday/paths
%_bindir/*
%_libdir/libdeng*.so*
%_libdir/%name/
%_datadir/%name/
%_datadir/applications/*.desktop
%_datadir/pixmaps/*.png

%changelog
