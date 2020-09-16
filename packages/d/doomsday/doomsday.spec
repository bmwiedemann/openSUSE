#
# spec file for package doomsday
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


Name:           doomsday
Version:        2.2.2
Release:        0
Summary:        The Doomsday Engine: DOOM/Hertic/Hexen port with pretty graphics
License:        GPL-2.0-or-later AND GPL-2.0-only AND SUSE-GPL-2.0-with-linking-exception AND BSD-3-Clause AND LGPL-3.0-or-later
Group:          Amusements/Games/3D/Shoot
URL:            http://dengine.net/
Source:         http://downloads.sf.net/deng/doomsday-%version.tar.gz
Source2:        %name-rpmlintrc
Patch1:         doomsday-no-abs-icon.patch
Patch2:         doomsday-libs.diff
Patch3:         doomsday-notime.diff
BuildRequires:  Mesa-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++ >= 6
BuildRequires:  libcurl4
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
BuildRequires:  pkgconfig(xxf86vm)
BuildRequires:  pkgconfig(zzip-zlib-config)
# Mesa 9.2 has OpenGL 3.1, and doomsday 2.0 needs that.
Requires:       Mesa-libGL1 >= 9.2
# Doomsday uses a modified version of assimp, so no pkgconfig(assimp) here :-(
Provides:       jdoom = %version-%release
Provides:       jheretic = %version-%release
Provides:       jhexen = %version-%release
Provides:       bundled(assimp) = 3.3.1
Obsoletes:      deng < %version-%release
Provides:       deng = %version-%release

%description
The Doomsday Engine is a source port with support for Doom, Heretic,
and Hexen. It does not support BOOM extensions.

%package launcher
Summary:        Graphical launcher for Doomsday
Group:          Amusements/Games/3D/Shoot
BuildRequires:  python
Requires:       %name = %version
Requires:       python-wxWidgets
BuildArch:      noarch

%description launcher
Snowberry is the official frontend of the Doomsday Engine. It is a
portable graphical game launcher, with support for configuring the
various types of games supported by Doomsday. It offers to save your
settings for launching a particular game (e.g., Doom).

%prep
%autosetup -p1

%build
pushd doomsday
%cmake \
%ifarch aarch64 %arm
  -DDENG_OPENGL_API=GLES3 \
%endif
  -DCMAKE_SKIP_RPATH:BOOL=ON
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
%_datadir/metainfo/
%_datadir/icons/*
%_datadir/pixmaps/*.png

%changelog
