#
# spec file for package gemrb
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


Name:           gemrb
Version:        0.9.1.1
Release:        0
Summary:        Game engine made with pre-rendered background
License:        GPL-2.0-or-later
Group:          Amusements/Games/RPG
URL:            http://www.gemrb.org/
Source:         https://github.com/%{name}/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         link-ptread-core-explicitly.patch
BuildRequires:  cmake >= 3.1
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  glibc-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(SDL2_mixer)
BuildRequires:  pkgconfig(SDL2_ttf)
BuildRequires:  pkgconfig(freetype2)
# reenable once OpenGL rendering stops being experimental (same for the cmake flags below)
# BuildRequires:  pkgconfig(glew)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libvlc)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(zlib)

%description
GemRB is an implementation of Bioware's Infinity Engine which was
written to support pseudo-3D role playing games based on the
Dungeons & Dragons ruleset.

You will need the original game files of Baldur's Gate and the Icewind
Dale series or Planescape: Torment to play.

%prep
%autosetup -p1
sed -ie 's,\(#!/usr/bin/python\)$,\13,' admin/extend2da.py

%build
rm -Rf CMakeCache.txt CMakeFiles/
%cmake -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} \
    -DLIB_DIR=%{_libdir} \
    -DPLUGIN_DIR=%{_libdir}/gemrb/plugins \
    -DDISABLE_WERROR=1 \
    -DCMAKE_VERBOSE_MAKEFILE:BOOL="true" \
#    -DOPENGL_BACKEND=OpenGL \
#    -DOpenGL_GL_PREFERENCE=GLVND
%make_jobs

%install
%cmake_install
%fdupes -s %{buildroot}/%{_datadir}/gemrb
rm %{buildroot}%{_datadir}/doc/gemrb/INSTALL
rm %{buildroot}%{_libdir}/libgemrb*.so

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%{_bindir}/extend2da.py
%{_bindir}/gemrb
%dir %{_libdir}/gemrb/plugins
%dir %{_libdir}/gemrb
%{_libdir}/gemrb/plugins/
%{_libdir}/lib*
%{_mandir}/man6/gemrb.6%{?ext_man}
%{_datadir}/gemrb/
%{_datadir}/doc/gemrb/
%{_datadir}/metainfo/org.gemrb.gemrb.metainfo.xml
%{_datadir}/pixmaps/gemrb.png
%dir %{_datadir}/icons/hicolor
%dir %{_datadir}/icons/hicolor/scalable
%dir %{_datadir}/icons/hicolor/scalable/apps
%{_datadir}/icons/hicolor/scalable/apps/gemrb.svg
%{_datadir}/applications/gemrb.desktop
%config %{_sysconfdir}/gemrb/

%changelog
