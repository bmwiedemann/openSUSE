#
# spec file for package cdogs-sdl
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           cdogs-sdl
Version:        0.6.7
Release:        0
Summary:        Classic overhead run-and-gun game
License:        GPL-2.0-only AND BSD-2-Clause AND CC-BY-3.0 AND CC-BY-SA-3.0
Group:          Amusements/Games/Action/Shoot
URL:            http://cxong.github.io/cdogs-sdl
Source:         https://github.com/cxong/cdogs-sdl/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:         cdogs-sdl-buildfix.patch
BuildRequires:  cmake >= 2.8.2
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(SDL2_image)
BuildRequires:  pkgconfig(SDL2_mixer)
BuildRequires:  pkgconfig(libenet)
BuildRequires:  pkgconfig(physfs)
BuildRequires:  pkgconfig(sdl2)

%description
C-Dogs SDL is a classic overhead run-and-gun game, supporting up to
4 players in co-op and deathmatch modes. Customize your player, choose
from up to 11 weapons, and try over 100 user-created campaigns. Have fun!

%prep
%setup -q
%patch0 -p1

# use system enet
rm -rf src/cdogs/enet

dos2unix doc/original_readme.txt

# disable -Werror (aborts build on mere warnings)
sed 's| -Werror||' -i CMakeLists.txt

%build
%cmake -DCDOGS_DATA_DIR=%{_datadir}/%{name}/ -DUSE_SHARED_ENET=ON
make %{?_smp_mflags}

%install
%cmake_install

install -Dm0644 build/linux/cdogs-icon.16.png %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/cdogs-sdl.png
install -Dm0644 build/linux/cdogs-icon.22.png %{buildroot}%{_datadir}/icons/hicolor/22x22/apps/cdogs-sdl.png
install -Dm0644 build/linux/cdogs-icon.32.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/cdogs-sdl.png
install -Dm0644 build/linux/cdogs-icon.48.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/cdogs-sdl.png

install -Dm0644 build/linux/cdogs-sdl.appdata.xml %{buildroot}%{_datadir}/appdata/cdogs-sdl.appdata.xml

%fdupes %{buildroot}%{_datadir}

%if 0%{?suse_version} < 1330
%post
%desktop_database_post
%icon_theme_cache_post
%endif

%if 0%{?suse_version} < 1330
%postun
%desktop_database_postun
%icon_theme_cache_postun
%endif

%files
%{_datadir}/applications/%{name}.desktop
%{_bindir}/%{name}*
%{_datadir}/%{name}/
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%dir %{_datadir}/appdata/
%{_datadir}/appdata/%{name}.appdata.xml

%changelog
