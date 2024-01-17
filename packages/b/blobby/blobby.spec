#
# spec file for package blobby
#
# Copyright (c) 2020 SUSE LLC
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


Name:           blobby
Version:        1.0
Release:        0
Summary:        2D Arcade Beach Volleyball Game
License:        GPL-2.0-or-later
Group:          Amusements/Games/Action/Other
URL:            http://blobbyvolley.de/
Source0:        https://github.com/danielknobe/blobbyvolley2/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}.desktop
Source2:        %{name}.png
Source3:        %{name}.appdata.xml
# PATCH-FIX-UPSTREAM
Patch0:         networkmessage.patch
# PATCH-FIX-UPSTREAM
Patch1:         icon.patch
# PATCH-FIX-OPENSUSE
Patch2:         data-dir.patch
# PATCH-FIX-UPSTREAM c4f23db774ebd41a8111180eae0db90f4c59af92 - use cmake zip to not add timestamps (boo#1047218)
Patch3:         reproducible.patch
BuildRequires:  boost-devel
BuildRequires:  cmake >= 2.6
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  make
BuildRequires:  perl
BuildRequires:  physfs-devel
BuildRequires:  zip
BuildRequires:  pkgconfig(sdl2)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Blobby Volley is one of the most popular freeware games. This is caused
first by the simple play principle and second by the funny design of
the player. The short duration of a game is a reason for playing this
game in meantime.

%prep
%autosetup -p1 -n blobbyvolley2-%{version}

%build
%cmake
make %{?_smp_mflags}

%install
%cmake_install

install -m0644 -D %{SOURCE1} %{buildroot}%{_datadir}/applications/%{name}.desktop
install -m0644 -D %{SOURCE2} %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
install -m0644 -D %{SOURCE3} %{buildroot}%{_datadir}/metainfo/%{name}.appdata.xml

%fdupes %{buildroot}%{_datadir}/%{name}

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog README
%license COPYING
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
%{_datadir}/metainfo/%{name}.appdata.xml

%changelog
