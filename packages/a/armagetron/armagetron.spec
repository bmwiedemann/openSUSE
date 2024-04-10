#
# spec file for package armagetron
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


%define series 0.2.9
%define src_name %{name}ad
Name:           armagetron
Version:        %{series}.2.3
Release:        0
Summary:        OpenGL Game Similar to the Film Tron
License:        GPL-2.0-or-later
Group:          Amusements/Games/Action/Arcade
URL:            https://www.armagetronad.org
Source0:        https://launchpad.net/%{src_name}/%{series}/%{version}/+download/%{src_name}-%{version}.tbz
Patch0:         armagetron-desktop-files-installdir.patch
BuildRequires:  gcc-c++
BuildRequires:  libSDL_image-devel
BuildRequires:  libpng-devel
BuildRequires:  libtool
BuildRequires:  libxml2-devel
BuildRequires:  llvm-clang
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(SDL_image)
BuildRequires:  pkgconfig(SDL_mixer)
BuildRequires:  pkgconfig(glu)
Requires(post): coreutils

%description
In this game, race against other players on a permanently moving
lightcycle (virtual motorbike), which leaves a wall as a trace. The
lightcycles can make 90 degree turns and accelerate when driven close
to walls. The game is over if you hit a wall. The goal of the game is
to try to make your enemies hit the walls, while you avoid doing the
same. Unlike glTron, this program does not require 3D hardware support.

%prep
%autosetup -p1 -n armagetronad-%{version}

%build
autoreconf -fvi
# clang does not support lto yet
%define _lto_cflags %{nil}
tmpflags="%{optflags} -fPIE -pie"
export CC=clang
export CXX=clang++
# bypass boo#927268 for PowerPC clang
%ifarch ppc64 ppc64le
tmpflags=${tmpflags/-fstack-protector-strong}
%endif
%configure \
	--enable-music \
	--enable-glout \
	--disable-desktop \
	--disable-uninstall \
	--disable-dependency-tracking \
	--disable-games \
	--docdir=%{_docdir} \
	CXXFLAGS="${tmpflags}"
%make_build

%install
# the uninstall_location trick was copied from Fedora. Thanks for debugging it :)
%make_install uninstall_location=foobar
# some cleanups
rm %{buildroot}%{_sysconfdir}/armagetronad/rc.config
rm %{buildroot}%{_sysconfdir}/armagetronad/settings_dedicated.cfg
rm %{buildroot}%{_datadir}/armagetronad/scripts/relocate
rm %{buildroot}%{_bindir}/armagetronad-master
mv %{buildroot}%{_docdir}/armagetronad ./armagetron_doc
chmod -x %{buildroot}%{_datadir}/armagetronad/scripts/rcd_*
%suse_update_desktop_file armagetronad Game ArcadeGame

%files
%license COPYING
%doc README armagetron_doc/*
%config %{_sysconfdir}/armagetronad
%{_bindir}/armagetronad
%{_datadir}/armagetronad/
%{_datadir}/metainfo/armagetronad.appdata.xml
%{_datadir}/applications/*
%{_datadir}/pixmaps/*.png

%post
if [ ! -e %{_datadir}/armagetron/music/fire.xm ]; then
    if [ -r %{_datadir}/gltron/music/song_revenge_of_cats.it ]; then
	cp -a %{_datadir}/gltron/music/song_revenge_of_cats.it \
		%{_datadir}/armagetron/music/fire.xm
    fi
fi

%changelog
