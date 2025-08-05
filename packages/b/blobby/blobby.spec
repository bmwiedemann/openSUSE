#
# spec file for package blobby
#
# Copyright (c) 2025 SUSE LLC
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
Version:        1.1.1
Release:        0
Summary:        2D Arcade Beach Volleyball Game
License:        GPL-2.0-or-later
Group:          Amusements/Games/Action/Other
URL:            https://blobbyvolley.de/
Source0:        https://github.com/danielknobe/blobbyvolley2/archive/v%{version}.tar.gz#/blobbyvolley2-%{version}.tar.gz
# PATCH-FIX-UPSTREAM blobbyvolley2-fix-non-void-return.patch - fixes control reaches end of non-void function
Patch0:         blobbyvolley2-fix-non-void-return.patch
# PATCH-FIX-OPENSUSE don't use integrated tinyxml
Patch1:         blobbyvolley2-1.1.1_external_tinyxml.patch
# PATCH_FIX-UPSTREAM https://github.com/danielknobe/blobbyvolley2/pull/152 - fix compatibility with Clang 19
Patch2:         blobbyvolley2-linked-list.patch
BuildRequires:  boost-devel
BuildRequires:  cmake >= 3.7
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  make
BuildRequires:  perl
BuildRequires:  physfs-devel
BuildRequires:  pkgconfig
BuildRequires:  zip
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(tinyxml2)

%description
Blobby Volley is one of the most popular freeware games. This is caused
first by the simple play principle and second by the funny design of
the player. The short duration of a game is a reason for playing this
game in meantime.

%prep
%autosetup -p1 -n blobbyvolley2-%{version}

%build
%cmake
%make_build

%install
%cmake_install

%fdupes %{buildroot}%{_datadir}/%{name}

%files
%doc AUTHORS ChangeLog
%license COPYING
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
%{_datadir}/metainfo/%{name}.appdata.xml

%changelog
