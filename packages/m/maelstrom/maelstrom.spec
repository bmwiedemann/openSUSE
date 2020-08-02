#
# spec file for package maelstrom
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


Name:           maelstrom
Version:        3.0.6
Release:        0
Summary:        High Quality Asteroids Clone
License:        GPL-2.0+ and CC-BY-3.0
Group:          Amusements/Games/Action/Shoot
Url:            http://slouken.libsdl.org/projects/Maelstrom/
Source:         http://slouken.libsdl.org/projects/Maelstrom/src/Maelstrom-3.0.6.tar.gz
Source1:        %{name}.png
Source2:        %{name}.desktop
Source3:        %{name}.appdata.xml
# PATCH-FIX-OPENSUSE - maelstrom-3.0.6-COPYING.GPL.patch -- Correct FSF Address
Patch0:         %{name}-3.0.6-COPYING.GPL.patch
# PATCH-FIX-OPENSUSE - maelstrom-3.0.6-Maelstrom-netd.c.patch -- Add missing includes
Patch1:         %{name}-3.0.6-Maelstrom-netd.c.patch
# PATCH-FIX-OPENSUSE - maelstrom-3.0.6-buttonlist.h.patch -- Fix deprecated code
Patch2:         %{name}-3.0.6-buttonlist.h.patch
# PATCH-FIX-OPENSUSE - maelstrom-3.0.6-controls.cpp.patch -- Fix deprecated code
Patch3:         %{name}-3.0.6-controls.cpp.patch
# PATCH-FIX-OPENSUSE - maelstrom-3.0.6-load.cpp.patch -- Fix deprecated code
Patch4:         %{name}-3.0.6-load.cpp.patch
# PATCH-FIX-OPENSUSE - maelstrom-3.0.6-maclib_macres.cpp.patch -- Fix deprecated code
Patch5:         %{name}-3.0.6-maclib_macres.cpp.patch
# PATCH-FIX-OPENSUSE - maelstrom-3.0.6-main.cpp.patch -- Fix deprecated code
Patch6:         %{name}-3.0.6-main.cpp.patch
# PATCH-FIX-OPENSUSE - maelstrom-3.0.6-myerror.cpp.patch -- Fix deprecated code
Patch7:         %{name}-3.0.6-myerror.cpp.patch
# PATCH-FIX-OPENSUSE - maelstrom-3.0.6-netlogic_game.cpp.patch -- Fix deprecated code
Patch8:         %{name}-3.0.6-netlogic_game.cpp.patch
# PATCH-FIX-OPENSUSE - maelstrom-3.0.6-netscore.cpp.patch -- Fix deprecated code
Patch9:         %{name}-3.0.6-netscore.cpp.patch
# PATCH-FIX-OPENSUSE - maelstrom-3.0.6-screenlib_SDL_FrameBuf.cpp.patch -- Fix deprecated code
Patch10:        %{name}-3.0.6-screenlib_SDL_FrameBuf.cpp.patch
%if 0%{?suse_version}
BuildRequires:  fdupes
BuildRequires:  update-desktop-files
%endif
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(SDL_net)
BuildRequires:  pkgconfig(sdl)
Provides:       Maelstrom = %{version}
Obsoletes:      Maelstrom < %{version}

%description
You are on space patrol. Blast asteroids, fight UFOs, and get extra
weapons. Beware of supernovae and black holes.

A port of the high resolution, fast action Asteroids-style
Mac game Maelstrom originally written by Ambrosia Software.
Unique to this port is a kick-butt network play mode.

%prep
%setup -q -n Maelstrom-%{version}
%patch0
%patch1
%patch2
%patch3
%patch4
%patch5
%patch6
%patch7
%patch8
%patch9
%patch10

# Fix paths
sed -i 's|games/||' configure.in
sed -i 's|@GAME_INSTALLDIR@|$(DESTDIR)@GAME_INSTALLDIR@|g' Makefile.am Makefile.in

%build
AUTOMAKE='automake --foreign' autoreconf -fi
%configure \
  --prefix=%{_datadir} \
  --bindir=%{_prefix}/bin
make %{?_smp_mflags}

%install
%make_install install-binPROGRAMS

# Remove not needed files
rm -rf Docs/Makefile* %{buildroot}%{_datadir}/Maelstrom/Images/Makefile*

# install icon
install -Dm 0644 %{S:1} %{buildroot}/%{_datadir}/icons/hicolor/48x48/apps/%{name}.png

# install Desktop file
install -Dm 0644 %{S:2} %{buildroot}%{_datadir}/applications/%{name}.desktop

# install software gallery metadata
install -Dm 0644 %{S:3} %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml

%if 0%{?suse_version}
    %suse_update_desktop_file %{name}
    %fdupes -s %{buildroot}%{_prefix}
%endif

mkdir -p %{buildroot}%{_localstatedir}/games
mv %{buildroot}%{_datadir}/Maelstrom/Maelstrom-Scores %{buildroot}%{_localstatedir}/games/
ln -sf %{_localstatedir}/games/Maelstrom-Scores %{buildroot}%{_datadir}/Maelstrom/Maelstrom-Scores

%files
%defattr(-,root,root,-)
%doc COPYING* CREDITS Changelog README* Docs/*
%{_bindir}/Maelstrom*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/
%{_datadir}/Maelstrom
%dir %{_localstatedir}/games/
%attr(0664, games, games)%{_localstatedir}/games/Maelstrom-Scores
%dir %{_datadir}/appdata
%{_datadir}/appdata/%{name}.appdata.xml

%changelog
