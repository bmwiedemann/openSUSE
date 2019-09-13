#
# spec file for package blobwars
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


Name:           blobwars
Version:        2.00
Release:        0
Summary:        Mission and Objective based 2D Platform Game
License:        GPL-2.0+
Group:          Amusements/Games/Action/Arcade
Url:            http://sourceforge.net/projects/blobwars/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1:        %{name}.appdata.xml
# PATCH-FIX-OPENSUSE - blobwars-icons_blobwars.desktop.patch -- Add GenericName and Category
Patch0:         %{name}-icons_blobwars.desktop.patch
# PATCH-FIX-UPSTREAM https://sourceforge.net/p/blobwars/patches/8/
Patch1:         reproducible.patch
%if 0%{?suse_version}
BuildRequires:  hicolor-icon-theme
BuildRequires:  update-desktop-files
%endif
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  pkgconfig
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(SDL2_image)
BuildRequires:  pkgconfig(SDL2_mixer)
BuildRequires:  pkgconfig(SDL2_net)
BuildRequires:  pkgconfig(SDL2_ttf)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Blob Wars : Metal Blob Solid. This is Episode I of the Blob Wars Saga.
This is a platform game, not unlike those found on the Amiga and SNES.
The object of the game is to take on the role of solider Blob, Bob,
and play through the various levels and attempt to rescue as many MIA
(Missing In Action) Blobs as possible. This is not quite as straight
forward as it sounds, since the MIAs will often be not directly
reachable and will require some extra thought. Bob also has to
contend with environmental hazards, alien invaders and assimilated Blobs.

%lang_package

%prep
%setup -q
%patch0
%patch1 -p1

# Correct Permissions
chmod 0644 Makefile*

# SED-FIX-OPENSUSE -- Fix paths and libraries
sed -i -e 's|USEPAK ?= 0|USEPAK ?= 1|;
           s|$(PREFIX)/games|$(PREFIX)/bin|;
           s|$(PREFIX)/share/games|$(PREFIX)/share|;
           s| -Werror||;
           s|$(CXX) $(LIBS) $(GAMEOBJS) -o $(PROG)|$(CXX) $(GAMEOBJS) $(LIBS) -o $(PROG)|;
           s|$(CXX) $(LIBS) $(PAKOBJS) -o pak|$(CXX) $(PAKOBJS) $(LIBS) -o pak|;
           s|$(CXX) $(LIBS) $(MAPOBJS) -o mapeditor|$(CXX) $(MAPOBJS) $(LIBS) -o mapeditor|' Makefile

# SED-FIX-OPENSUSE -- Fix pak
sed -i -e 's|gzclose(pak)|gzclose((gzFile)pak)|;
           s|gzclose(fp)|gzclose((gzFile)fp)|' src/pak.cpp

%build
make %{?_smp_mflags} CFLAGS="%{optflags}" \
     RELEASE=1 DOCDIR=%{_docdir}/%{name}/

%install
#make install
%make_install BINDIR=%{_bindir}/ DATADIR=%{_datadir}/%{name}/ DOCDIR=%{_docdir}/%{name}/

# install icons
for i in 16 32 48 64; do
    install -Dm 0644 icons/%{name}${i}x${i}.png \
            %{buildroot}/%{_datadir}/icons/hicolor/${i}x${i}/apps/%{name}.png
done

%find_lang %{name}

# Install appdata
mkdir -p %{buildroot}%{_datadir}/appdata
install -Dm 0644 %{S:1} %{buildroot}%{_datadir}/appdata

%if 0%{?suse_version}
    %suse_update_desktop_file %{name}
%endif

%files
%defattr(-,root,root)
%doc doc/*
%{_bindir}/%{name}
%{_datadir}/%{name}
%dir %{_datadir}/appdata
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png

%files lang -f %{name}.lang

%changelog
