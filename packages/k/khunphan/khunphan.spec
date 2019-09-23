#
# spec file for package khunphan
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           khunphan
BuildRequires:  SDL_image-devel
BuildRequires:  SDL_mixer-devel
BuildRequires:  automake
BuildRequires:  freeglut-devel
BuildRequires:  gcc-c++
BuildRequires:  libdrm-devel
BuildRequires:  libpng-devel
BuildRequires:  libxml2-devel
BuildRequires:  update-desktop-files
BuildRequires:  xorg-x11-Mesa-devel
BuildRequires:  pkgconfig(glu)
Requires(pre):  pwdutils
Summary:        Traditional Thai Puzzle Board Game in 3D with Wooden Blocks
License:        GPL-2.0+
Group:          Amusements/Games/3D/Other
Version:        0.55
Release:        0
Source0:        http://www.ibiblio.org/pub/Linux/games/strategy/khunphan-0.55.tar.bz2
Source1:        %name.desktop
Source2:        configure.ac
Patch:          khunphan-0.55-codecleanup.diff
Patch1:         khunphan-freeglut.diff
Patch2:         khunphan-DESTDIR.diff
Patch3:         khunphan-0.55-png_uint_32.diff
# PATCH-FIX-UPSTREAM khunphan-libpng15.patch pgajdos@suse.com -- Support building with libpng15 (not sent upstream, no activity)
Patch4:         khunphan-libpng15.patch
Url:            http://geocities.com/khunphangame/
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%define _datadir /usr/share/games/

%description
The goal of this game is to move the biggest token to a specific
position. A tutorial and solution hint is available for beginners. The
game is visible as a three-dimensional model with different camera
positions. All movements, including the menus, are physically
calculated.

Different themes, like wood, rock, metal, marble, bubbles, and
painting, are available. Themes influence both the display and the
sound effects. Ambient and Drum & Bass music from Nifflas
(www.nifflas.com) gives the game a unique atmosphere.

%prep
%setup -q
%patch
%patch1
%patch2
%patch3
%patch4 -p1
chmod -x khunphan/{*.cpp,*.h}
rm -f aclocal.m4 acinclude.m4 configure.files configure.in*
cp %{S:2} .

%build
autoreconf -fi
%configure
make %{?_smp_mflags}

%install
%makeinstall
%suse_update_desktop_file -i %name Game LogicGame

%files
%attr(-,root,root) %doc README
%defattr(-,root,root)
%{_bindir}/*
%{_datadir}/*
/usr/share/applications/%name.desktop

%changelog
