#
# spec file for package jumpnbump
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
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



Name:           jumpnbump
BuildRequires:  SDL_image-devel
BuildRequires:  SDL_mixer-devel
BuildRequires:  SDL_net-devel
BuildRequires:  automake
BuildRequires:  update-desktop-files
BuildRequires:  xorg-x11
License:        GPL-2.0+
URL:            http://gnu.ethz.ch/jumpbump.mine.nu/
Group:          Amusements/Games/Action/Arcade
Version:        1.55
Release:        0
Requires:       python-gtk
Summary:        Funny Game with Cute Little Bunnies
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source:         %{name}-%{version}.tar.gz
Source1:        jumpnbump.desktop
Source2:        jumpnbump-levels-0.0.20020825_selected.tar.bz2
Patch0:         jumpnbump-1.55-jnbmenudefaults.diff
Patch1:         jumpnbump-1.55-version.patch
# http://repo.or.cz/w/jumpnbump.git
Patch20:        jumpnbump-1.50-Exit-fullscreen-mode-when-you-quit.diff
Patch21:        jumpnbump-1.50-Use-safe-temporary-files.diff
Patch22:        jumpnbump-1.50-exit-fullscreen-mode-early-to-avoid-crash.diff
Patch23:        jumpnbump-1.50-Import-jumpnbump_menu.diff
Patch24:        jumpnbump-1.50-handle-SDL-quit-event.diff
#
Patch50:        jumpnbump_menu-default.diff
Patch51:        jumpnbump-1.50-nodate.diff

%description
You are a cute little bunny and you have to avoid the other bunnies
trying to stomp on you and at the same time try to stomp on as many
opponents as possible. Jump & bump is multiplayer game only with up to
four players simultaneously. Gather the local crew and have a blast.

%prep
%setup -q -a 2 -n jumpnbump-1.50
%patch0 -p1
%patch1 -p0
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch50 -p1
%patch51 -p1

%build
./autogen.sh
%configure
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install 
install -m 755 modify/{gobpack,jnbpack,jnbunpack} %{buildroot}%{_bindir}
sed -e 's,/usr/share/games,%{_datadir},;s,/usr/games,%{_bindir},;s/jumpnbump-unpack/jnbunpack/' \
	< contrib/jumpnbump_menu/jumpnbump_menu.py \
	> %{buildroot}%{_bindir}/jumpnbump_menu
chmod 755 %{buildroot}%{_bindir}/jumpnbump_menu
install -m 644 contrib/jumpnbump_menu/jumpnbump_menu.glade %{buildroot}%{_datadir}/jumpnbump
#
# get rid of superfluous scripts
/bin/rm -v %{buildroot}%{_bindir}/jumpnbump{-kdialog,-xdialog,.fbcon,.svgalib}
/bin/rm -v %{buildroot}%{_bindir}/jnbmenu.tcl
#
rm -rf levelmaking/CVS
install -d -m 755 %{buildroot}%{_datadir}/pixmaps
install -m 644 sdl/*.xpm %{buildroot}%{_datadir}/pixmaps
#
cd jumpnbump-levels-*
for i in *.dat.bz2; do
	bunzip2 < "$i" > %{buildroot}%{_datadir}/jumpnbump/"${i%%.bz2}"
done
cd ..
#
%suse_update_desktop_file -i %name "Game ArcadeGame"

%files
%defattr(-,root,root)
%doc levelmaking
%doc AUTHORS COPYING ChangeLog README LINKS
%doc gob.txt
%{_bindir}/jumpnbump_menu
%{_bindir}/jumpnbump
%{_bindir}/gobpack
%{_bindir}/jnbpack
%{_bindir}/jnbunpack
%dir %{_datadir}/jumpnbump
%{_datadir}/jumpnbump/*
%{_datadir}/pixmaps/*
%doc %{_mandir}/man6/*
%{_datadir}/applications/*

%changelog
