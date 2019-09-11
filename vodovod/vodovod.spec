#
# spec file for package vodovod
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


%define _lver 1.10
%define _svnrev svn23
Name:           vodovod
Version:        %{_lver}_%{_svnrev}
Release:        0
Summary:        Pipe connecting action puzzle game
License:        GPL-2.0+
Group:          Amusements/Games/Arcade/Logic
Url:            http://home.gna.org/vodovod/
Source0:        %{name}-%{_lver}+%{_svnrev}.tar.bz2
Source1:        %{name}.png
Source2:        %{name}.desktop
# Fix bad C++ code
Patch0:         %{name}-%{_lver}-hiscore.h.patch
%if 0%{?suse_version}
BuildRequires:  fdupes
BuildRequires:  update-desktop-files
%endif
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(SDL_image)
BuildRequires:  pkgconfig(SDL_mixer)
BuildRequires:  pkgconfig(SDL_ttf)
BuildRequires:  pkgconfig(sdl)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
You get a limited number of pipes on each level and need to combine
them such that water from the house at the top of the screen can flow
to the storage tank at the bottom. Points will be awarded per each
pipe segment through which water flows, and the goal of the game is
to reach a high score. Some of the levels also have obstacles where
pipes cannot be placed. The game is playable with joystick/joypad as
well.

%prep
%setup -q -n %{name}-svn
%patch0

# Fix path
sed -i 's|= /usr/local|= /usr|' Makefile

%build
make %{?_smp_mflags} CXXFLAGS="%{optflags}"

%install
%make_install
%find_lang %name

# install icons
install -Dm 0644 icon.ico %{buildroot}%{_datadir}/%{name}
install -Dm 0644 %{S:1} %{buildroot}/%{_datadir}/icons/hicolor/48x48/apps/%{name}.png

# install Desktop file
install -Dm 0644 %{S:2} %{buildroot}%{_datadir}/applications/%{name}.desktop

# install score
mkdir -p %{buildroot}%{_localstatedir}/games/
touch %{buildroot}%{_localstatedir}/games/%{name}.sco

%if 0%{?suse_version}
    %suse_update_desktop_file %{name}
    %fdupes -s %{buildroot}%{_prefix}
%endif

%files -f %name.lang
%defattr(-,root,root,-)
%doc CHANGES COPYING html
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/
%{_datadir}/%{name}
%dir %{_localstatedir}/games
# Correct Permissions
%attr(0664,games,games) %{_localstatedir}/games/%{name}.sco

%changelog
