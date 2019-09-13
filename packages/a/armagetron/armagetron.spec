#
# spec file for package armagetron
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


Name:           armagetron
Version:        0.2.8.3.4
Release:        0
Summary:        OpenGL Game Similar to the Film Tron
License:        GPL-2.0-or-later
Group:          Amusements/Games/Action/Arcade
URL:            http://armagetronad.sourceforge.net
Source:         https://sourceforge.net/projects/armagetronad/files/stable/%{version}/armagetronad-%{version}.src.tar.bz2
Source1:        armagetron_add.tar.bz2
# PATCH-FIX-OPENSUSE bmwiedemann -- fix build-compare
Patch0:         reproducible.patch
# PATCH-FIX-UPSTREAM https://bugs.launchpad.net/armagetronad/+bug/1596771 -- fix nullpointer dereferenceing which leads into segfault
Patch1:         fix-segv.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libpng-devel
BuildRequires:  libxml2-devel
BuildRequires:  llvm-clang
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(SDL_image)
BuildRequires:  pkgconfig(SDL_mixer)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(sdl)
Requires(post): coreutils

%description
In this game, race against other players on a permanently moving
lightcycle (virtual motorbike), which leaves a wall as a trace. The
lightcycles can make 90 degree turns and accelerate when driven close
to walls. The game is over if you hit a wall. The goal of the game is
to try to make your enemies hit the walls, while you avoid doing the
same. Unlike glTron, this program does not require 3D hardware support.

%prep
%setup -q -a 1 -n armagetronad-%{version}
%patch0 -p1
%patch1 -p1

%build
autoreconf -fi
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
make %{?_smp_mflags}

%install
# the uninstall_location trick was copied from Fedora. Thanks for debugging it :)
make DESTDIR=%{buildroot} install uninstall_location=foobar
mkdir -p %{buildroot}%{_datadir}/applications/
install armagetron_add/*.desktop       %{buildroot}%{_datadir}/applications/
mkdir -p %{buildroot}%{_datadir}/appdata
install -m644 armagetron_add/Armagetron.appdata.xml %{buildroot}%{_datadir}/appdata/
mkdir -p %{buildroot}%{_datadir}/pixmaps/
install -Dm644 armagetron_add/README.SuSE %{buildroot}%{_docdir}/%{name}/README.SUSE
pushd %{buildroot}
mv %{buildroot}%{_datadir}/armagetronad/desktop/icons/large/armagetronad.png %{buildroot}%{_datadir}/pixmaps/%{name}.png
ln -s %{_datadir}/pixmaps/%{name}.png %{buildroot}%{_datadir}/armagetronad/desktop/icons/large/armagetronad.png
popd
# some cleanups
rm %{buildroot}%{_sysconfdir}/armagetronad/rc.config
rm %{buildroot}%{_sysconfdir}/armagetronad/settings_dedicated.cfg
rm %{buildroot}%{_datadir}/armagetronad/language/update.py
rm %{buildroot}%{_datadir}/armagetronad/scripts/relocate
rm %{buildroot}%{_datadir}/armagetronad/desktop/*.desktop
mv %{buildroot}%{_docdir}/armagetronad ./armagetron_doc
%suse_update_desktop_file Armagetron Game ArcadeGame

%files
%license COPYING
%doc README armagetron_doc/*
%doc %{_docdir}/%{name}/README.SUSE
%config %{_sysconfdir}/armagetronad
%{_bindir}/armagetronad
%{_datadir}/armagetronad
%dir %{_datadir}/appdata
%{_datadir}/appdata/Armagetron.appdata.xml
%attr(644,root,root) %{_datadir}/applications/*
%{_datadir}/pixmaps/%{name}.png

%post
if [ ! -e %{_datadir}/armagetron/music/fire.xm ]; then
    if [ -r %{_datadir}/gltron/music/song_revenge_of_cats.it ]; then
	cp -a %{_datadir}/gltron/music/song_revenge_of_cats.it \
		%{_datadir}/armagetron/music/fire.xm
    fi
fi

%changelog
