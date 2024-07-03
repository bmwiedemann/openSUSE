#
# spec file for package circuslinux
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


Name:           circuslinux
BuildRequires:  SDL-devel
BuildRequires:  SDL_image-devel
BuildRequires:  SDL_mixer-devel
BuildRequires:  automake
BuildRequires:  update-desktop-files
Summary:        A Clone of the Atari 2600 Game "Circus Atari"
License:        GPL-1.0
Group:          Amusements/Games/Action/Breakout
Version:        1.0.3
Release:        0
Source:         %{name}-%{version}.tar.bz2
Source1:        %{name}.desktop
Patch0:         %{name}-%{version}.patch
Url:            http://www.newbreedsoftware.com/circus-linux/
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The object is to move a teeter-totter back and forth across the screen
to bounce clowns into the air. When they reach the top, they pop rows
of balloons, and then fall back down.

%prep
%autosetup -p0

%build
AUTOMAKE='automake --foreign' autoreconf -fi
%configure \
  --datadir=%{_datadir}/games
make %{?_smp_mflags}

%install
make DESTDIR=$RPM_BUILD_ROOT install
find $RPM_BUILD_ROOT%{_datadir}/games/circuslinux -type f -exec chmod 644 {} \;
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/circuslinux-*
%suse_update_desktop_file -i %{name} Game ArcadeGame
install -D -m 0644 data/images/icon.png $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png

%files
%defattr(-,root,root)
%doc AUTHORS.txt COPYING.txt INSTALL.txt README.txt CHANGES.txt FAQ.txt README-SDL.txt
%{_bindir}/*
%dir %{_datadir}/games/circuslinux
%{_datadir}/games/circuslinux/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
