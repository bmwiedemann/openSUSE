#
# spec file for package pingus
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


%if 0%{?suse_version} > 1210
%define with_wiimote False
%else
%define with_wiimote True
%endif

Name:           pingus
Version:        0.7.6
Release:        0
Summary:        Free Lemmings-like puzzle game
License:        GPL-3.0+
Group:          Amusements/Games/Logic
Url:            http://pingus.seul.org/
# Downloaded from https://code.google.com/p/pingus/source/checkout
# Packed as tar.bz2
Source0:        %{name}-%{version}+git-6a1153a.tar.bz2
# PATCH-FIX-UPSTREAM Issue 136, Add .desktop file to source package
Source1:        %{name}.desktop
# PATCH-FIX-UPSTREAM pingus-0.7.6-Makefile.patch -- Issue 144, use /usr for prefix, fix man, permissions
Patch1:         %{name}-%{version}-Makefile.patch
# PATCH-FIX-UPSTREAM pingus-0.7.6-SConscript.patch -- Issue 145, Fix linking against X11 and adds wii support
Patch2:         %{name}-%{version}-SConscript.patch
# PATCH-FIX-UPSTREAM pingus-scons-on-py3.patch dimstar@opensuse.org -- Fix build with scons using python3 as interpreter
Patch3:         pingus-scons-on-py3.patch
%if 0%{?suse_version}
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  update-desktop-files
%endif
BuildRequires:  bluez-devel
%if 0%{?suse_version} > 1325
BuildRequires:  libboost_headers-devel
%else
BuildRequires:  boost-devel
%endif
BuildRequires:  dos2unix
BuildRequires:  gcc-c++
BuildRequires:  libcwiid-devel
BuildRequires:  libpng-devel
BuildRequires:  scons
BuildRequires:  pkgconfig(SDL_image)
BuildRequires:  pkgconfig(SDL_mixer)
BuildRequires:  pkgconfig(xi)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Pingus is a free Lemmings-like puzzle game covered under the GNU GPL.
It features currently 77 playable levels.

You can use to see which languages are supported

    pingus --list-languages

And start with

    pingus --language de


If you wish to play the other levels

    pingus /usr/share/pingus/levels/playable/some-level
    pingus /usr/share/pingus/levels/incoming/some-level
    pingus /usr/share/pingus/levels/wip/some-level

The other, probably more userfriendly, way is to simply load them into
the level editor and then click the play button.

%prep
%setup -q -n %{name}
%patch1
%patch2
%patch3 -p1

# Convert to unix line end
dos2unix data/po/pl.po data/levels/incoming/*.pingus \
         data/images/pingus/README

# SED-FIX-UPSTREAM -- Issue 144, Fix datadir
sed -i 's|set_path("data")|set_path("%{_datadir}/%{name}")|' \
    src/pingus/pingus_main.cpp

# SED-FIX-UPSTREAM -- Issue 145, Fix linking against X11
sed -i 's|'SDL_mixer', 'png'|'SDL_mixer', 'png', 'X11'|' \
    src/engine/input/SConstruct.main

# SED-FIX-UPSTREAM -- Issue 146, Remove debug, add missing includes and allow wii support to compile
sed -i -e 's|"pingus/debug.hpp"|<iostream>|' \
    -i -e '/pout(PINGUS_DEBUG_INPUT)/d' \
    src/engine/input/xinput/xinput_driver.cpp
sed -i -e :a -e '\%/#include "engine/input/xinput/xinput_driver.hpp"%!b' \
    -e $'n;/namespace Input {/i\\\n#include <iostream>' -e ba src/engine/input/xinput/xinput_device.cpp
sed -i -e 's|"pingus/debug.hpp"|<iostream>|' \
    -i -e '/WiimoteDriver: (wiimote:button/,+2d' \
    -i -e '/WiimoteDriver: (wiimote:axis/,+3d' \
    src/engine/input/wiimote/wiimote_driver.cpp

%build
mkdir -p build
scons %{?_smp_mflags} CCFLAGS="%{optflags}" with_wiimote=%{with_wiimote} \
      with_linuxusbmouse=True with_linuxevdev=True with_xinput=True

%install
%make_install

# install icons
install -Dm 0644 data/images/icons/pingus.png %{buildroot}/%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
install -Dm 0644 data/images/icons/pingus-icon.png %{buildroot}/%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
install -Dm 0644 data/images/icons/pingus.svg %{buildroot}/%{_datadir}/icons/hicolor/scalable/apps/%{name}.png

# install Desktop file
install -Dm 0644 %{S:1} %{buildroot}%{_datadir}/applications/%{name}.desktop

%if 0%{?suse_version}
    %suse_update_desktop_file %{name}
    %fdupes -s %{buildroot}%{_prefix}
%endif

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING NEWS README TODO
%{_bindir}/%{name}
%{_mandir}/man6/%{name}.6%{ext_man}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/
%{_datadir}/%{name}

%changelog
