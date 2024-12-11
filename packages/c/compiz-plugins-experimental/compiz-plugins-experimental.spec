#
# spec file for package compiz-plugins-experimental
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


Name:           compiz-plugins-experimental
Version:        0.8.18
Release:        0
Summary:        OpenGL window and compositing manager experimental plugins
License:        GPL-2.0-or-later AND GPL-2.0-only
URL:            https://gitlab.com/compiz-reloaded/compiz-plugins-experimental
Source:         http://northfield.ws/projects/compiz/releases/%{version}/%{name}-%{version}.tar.xz
# PATCH-FIX-UPSTREAM compiz-plugins-experimental-0.8.18-fix-gcc-14.patch jskarvad@redhat.com -- Fix build with GCC-14 (commit 82c05c42).
Patch0:         compiz-plugins-experimental-0.8.18-fix-gcc-14.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(bcop) >= 0.7.3
BuildRequires:  pkgconfig(cairo) >= 1.0
BuildRequires:  pkgconfig(cairo-xlib)
BuildRequires:  pkgconfig(compiz) < 0.9
BuildRequires:  pkgconfig(compiz-animation) < 0.9
BuildRequires:  pkgconfig(compiz-cube) < 0.9
BuildRequires:  pkgconfig(compiz-mousepoll) < 0.9
BuildRequires:  pkgconfig(compiz-text) < 0.9
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glew)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(xscrnsaver)
Requires:       compiz < 0.9
Requires:       compiz-plugins-extra < 0.9
Requires:       compiz-plugins-main < 0.9
# compiz-plugins-unsupported was last used in openSUSE Leap 42.1.
Provides:       compiz-plugins-unsupported = %{version}
Obsoletes:      compiz-plugins-unsupported < %{version}
# compiz-plugin-photowheel was last used in openSUSE Leap 42.1.
Provides:       compiz-plugin-photowheel = %{version}
Obsoletes:      compiz-plugin-photowheel < %{version}
Provides:       compiz-plugins-git = %{version}
Obsoletes:      compiz-plugins-git < %{version}
ExcludeArch:    s390 s390x

%description
This package contains the experimental Compiz compositing
manager plugins.

Contains:
 * Atlantis: Render some sea animals inside of the transparent cube.
 * Cubemodel: Render still/animated 3D mesh models inside of the
   transparent cube.
 * Elements: Draw elements on screen.
 * Fakeargb: Makes a special colour of a window transparent.
 * Mswitch: Enables the switching of viewports with mouse gestures.
 * Snow: Displays falling snow over the desktop and windows.
 * Tile: Enables the tiling of windows on the desktop in a manner
   similar to awesome.
 * ... and more.

%lang_package

%package devel
Summary:        OpenGL window and compositing manager community plugins
Requires:       %{name} = %{version}
Requires:       pkgconfig(bcop)
Requires:       pkgconfig(compiz) < 0.9
Requires:       pkgconfig(gl)
Recommends:     pkgconfig(cairo) >= 1.0
Recommends:     pkgconfig(cairo-xlib)
Recommends:     pkgconfig(compiz-animation) < 0.9
Recommends:     pkgconfig(compiz-animationaddon) < 0.9
Recommends:     pkgconfig(compiz-cube) < 0.9
Recommends:     pkgconfig(compiz-mousepoll) < 0.9
Recommends:     pkgconfig(compiz-text) < 0.9
Recommends:     pkgconfig(xscrnsaver)

%description devel
This package contains the community unsupported Compiz compositing
manager plugins.

This package contain development files required for developing
other plugins.

%prep
%autosetup -p1

%build
NOCONFIGURE=1 ./autogen.sh
%configure \
  --disable-static
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
%find_lang %{name}

%files
%license COPYING
%doc AUTHORS NEWS README.md
%{_libdir}/compiz/*
%{_datadir}/compiz/*

%files lang -f %{name}.lang

%files devel
%{_includedir}/compiz/*

%changelog
