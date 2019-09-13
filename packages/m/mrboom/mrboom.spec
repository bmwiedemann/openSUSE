#
# spec file for package mrboom
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2018, Martin Hauke <mardnh@gmx.de>
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


Name:           mrboom
Version:        4.7
Release:        0
Summary:        A Bomberman clone
License:        MIT
Group:          Amusements/Games/Action/Other
URL:            http://mrboom.mumblecore.org
#Git-Clone:     https://github.com/Javanaise/mrboom-libretro.git
Source:         https://github.com/Javanaise/%{name}-libretro/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(SDL2_mixer)
BuildRequires:  pkgconfig(libmodplug)
BuildRequires:  pkgconfig(minizip)
BuildRequires:  pkgconfig(sdl2)

%description
This is an SDL2 version of the original 1999 version of Mr. Boom.
The goal of the game is to bomb away enemies and other players.

%prep
%setup -q -n %{name}-libretro-%{version}

%build
export CFLAGS="%{optflags} -fPIE"
export CXXFLAGS="%{optflags} -fPIE"
export LDFLAGS="-pie"
make mrboom LIBSDL2=1 %{?_smp_mflags}

%install
%make_install PREFIX=%{_prefix} MANDIR=share/man/man6
# icons
for i in 16x16 32x32 48x48 256x256; do
  install -D -m0644 Assets/hicolor/$i/apps/%{name}.png %{buildroot}%{_datadir}/icons/hicolor/$i/apps/%{name}.png
done
# desktop file
%suse_update_desktop_file -c %{name} %{name} "8 player Bomberman clone" %{name} %{name} Game ArcadeGame ActionGame

%if 0%{?suse_version} < 1500
%post
%desktop_database_post

%postun
%desktop_database_postun
%endif

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man6/%{name}.6%{?ext_man}

%changelog
