#
# spec file for package pink-pony
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


Name:           pink-pony
Version:        1.4.1
Release:        0
Summary:        3D racing game with ponies
License:        GPL-3.0+
Group:          Amusements/Games/Action/Arcade
Url:            http://code.google.com/p/pink-pony/
Source0:        http://pink-pony.googlecode.com/files/pink-pony-%{version}.tar.gz
Patch0:         datadir.patch
Patch1:         script.patch
Patch2:         pink-pony-1.4.1.diff

BuildRequires:  DevIL-devel
BuildRequires:  SDL-devel
BuildRequires:  SDL_mixer-devel
BuildRequires:  desktop-file-utils
BuildRequires:  ftgl-devel
BuildRequires:  ilmbase-devel
BuildRequires:  libsigc++2-devel
BuildRequires:  protobuf-devel
BuildRequires:  scons
BuildRequires:  pkgconfig(libglfw)

Requires:       pink-pony-data = %version

%package data
Summary:        3D racing game with ponies - data files
License:        GPL-3.0+ and CC-BY-SA-3.0 and CC-BY-3.0 and OFL-1.1 and CC0-1.0
Group:          Amusements/Games/Action/Arcade
BuildArch:      noarch
Requires:       pink-pony = %version

%description
Pink Pony is a Tron­-like multiplayer racing­ game. You control
little ponies that leave a trail of flowers everywhere they step.
You have to evade these trails and force other ponies into them.
The last pony standing wins the game. 

%description data
Pink Pony is a Tron­-like multiplayer racing­ game. You control
little ponies that leave a trail of flowers everywhere they step.
You have to evade these trails and force other ponies into them.
The last pony standing wins the game. 

 This package contains architecture-independent game data

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
export CCFLAGS="%optflags"
scons -f SConstruct %{?_smp_mflags} \
	prefix=/usr \
	resources_dir=/usr/share/pink-pony \
	lib_dir="${PWD}"

%install
install -d -m 755 %buildroot/usr/bin
install -d -m 755 %buildroot/usr/lib/pink-pony
install -d -m 755 %buildroot/usr/share/pixmaps
install -d -m 755 %buildroot/usr/share/pink-pony
install -m 755 Pony %buildroot/usr/lib/pink-pony/pink-pony.bin
install -m 755 install/pink-pony %buildroot/usr/bin/
install -m 644 install/pink-pony.png %buildroot/usr/share/pixmaps
install -m 644 pony.options %buildroot/usr/share/pink-pony
cp -r resources/* %buildroot/usr/share/pink-pony

desktop-file-install \
  --dir %{buildroot}%{_datadir}/applications           \
  install/pink-pony.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README
%{_bindir}/*
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/pixmaps/*
/usr/lib/pink-pony

%files data
%defattr(-,root,root,-)
%{_datadir}/pink-pony

%changelog
