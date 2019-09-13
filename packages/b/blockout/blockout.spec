#
# spec file for package blockout
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           blockout
Version:        2.5
Release:        0
Summary:        A free clone of the original BlockOut DOS game
License:        GPL-2.0
Group:          Amusements/Games/Action/Arcade
Url:            http://blockout.net/

Source:         http://downloads.sf.net/blockout/bl25-src.tar.gz
Source2:        http://downloads.sf.net/blockout/bl25-linux-x86.tar.gz
Patch1:         automake.diff
Patch2:         compilefixes.diff
Patch3:         bl2home.diff
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkgconfig(SDL_mixer)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(sdl)

%description
BlockOut II is a free adaptation of the original BlockOut DOS game
edited by California Dreams in 1989. BlockOut II has the same
features than the original game with few graphic improvements. The
game has been designed to reproduce the original game kinematics as
accurately as possible.

%prep
# images, sounds, are in #2.
%setup -qn BL_SRC -a2
%patch -P 1 -P 2 -P 3 -p1

%build
autoreconf -fi
%configure
make %{?_smp_mflags}

%install
d="%buildroot/%_datadir/%name"
%make_install
mkdir -p "$d"
mv blockout/{images,sounds} "$d/"
find "$d/" -type f -exec chmod a-x "{}" "+"

%files
%defattr(-,root,root)
%_bindir/blockout
%_datadir/%name/

%changelog
