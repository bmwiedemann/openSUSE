#
# spec file for package ssdl_bomber
#
# Copyright (c) 2024 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define oname   SDL_bomber
%define name1   bomber
%define name2   matcher

Name:           sdl_bomber
Version:        1.0.4
Release:        0
Summary:        SDL Bomberman clone
License:        GPL-2.0+
Group:          Amusements/Games/Action/Arcade
Url:            http://www.linuxmotors.com/SDL_bomber/
Source0:        http://www.linuxmotors.com/%{oname}/downloads/%{oname}-%{version}.tgz
Source1:        %{name}.sh
Source2:        %{name}-icons.tar
Source3:        %{name}.desktop
Source4:        %{name}-rpmlintrc
%if 0%{?suse_version}
BuildRequires:  update-desktop-files
%endif
BuildRequires:  pkgconfig(SDL_image)
BuildRequires:  pkgconfig(SDL_mixer)
BuildRequires:  pkgconfig(sdl)

%description
This is a SDL Bomberman clone.

You've got to blow up other players to win. Spacebar drops a bomb. Get away
and hope your enemy gets hit by the flame. The 'b' key is a 2nd control
for when you are lucky enough to pick up the bomb control--looks like a
bomb with a timer on it. When you have that the bomb won't go off until
detonated by another bomb, you are killed, or you press 'b'.

Blowing up bricks might result in prizes, most of which are good.
Skates = speed up
Bomb = allow you to have one more active bomb
flame = Increase bomb strength
turtle = makes you move very slowly
bomb with timer = controlled bomb detonation with 'b' key.
gold flame = Set flame strength to max

There isn't much point in playing the game alone (single player). In that
case the only thing to avoid is accidentally killing yourself. Big deal...
It's really a multiplayer game.

%prep
%setup -q -a2 -n %{oname}-%{version}
#patch0

# Remove not needed files
rm -fr data/CVS

%build
make %{?_smp_mflags} CPPFLAGS="%{optflags}"

%install
# install wrapper
install -Dm 0755 %{S:1} %{buildroot}%{_bindir}/%{name}

# install executables
mkdir -p %{buildroot}%{_libexecdir}/%{name}
install -Dm 0755 %{name1} %{buildroot}%{_libexecdir}/%{name}/%{name1}
install -Dm 0755 %{name2} %{buildroot}%{_libexecdir}/%{name}/%{name2}

# install directory
cp -a data %{buildroot}%{_libexecdir}/%{name}/

# install icons
for i in 22 32 48 64 72 96; do
    install -Dm 0644 icons/%{name}_${i}x${i}.png %{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/apps/%{name}.png
done

# install Desktop file
install -Dm 0644 %{S:3} %{buildroot}%{_datadir}/applications/%{name}.desktop

%if 0%{?suse_version}
    %suse_update_desktop_file %{name}
%endif

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog README
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor
%{_libexecdir}/%{name}

%changelog
