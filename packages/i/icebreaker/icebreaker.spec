#
# spec file for package icebreaker
#
# Copyright (c) 2021 SUSE LLC
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


Name:           icebreaker
Version:        2.2.0
Release:        0
Summary:        An addictive action-puzzle game involving bouncing penguins
License:        GPL-2.0-or-later
Group:          Amusements/Games/Board/Puzzle
URL:            http://www.mattdm.org/icebreaker/
Source:         https://mattdm.org/icebreaker/2.2.x/icebreaker-%{version}.tar.xz
# PATCH-FIX-OPENSUSE Workaround a syntax error
Patch0:         version.patch
# PATCH-FIX-OPENSUSE This must have been designed with a version of GCC that detects less warnings.
Patch1:         cflags.patch
BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig(SDL_mixer)
BuildRequires:  pkgconfig(sdl)

%description
IceBreaker is an action-puzzle game in which you must capture penguins from
an Antarctic iceberg so they can be shipped to Finland, where they are
essential to a secret plot for world domination. To earn the highest Geek
Cred, trap them in the smallest space in the shortest time while losing the
fewest lives. IceBreaker was inspired by (but is far from an exact clone of)
Jezzball by Dima Pavlovsky.

%prep
%autosetup -p1

%build
%make_build VERSION=%{version} OPTIMIZE="%{optflags}" prefix=%{_prefix}

%install
%make_install VERSION=%{version} prefix=%{buildroot}%{_prefix}

desktop-file-install --dir=%{buildroot}%{_datadir}/applications icebreaker.desktop
install -Dm0644 metainfo.xml %{buildroot}%{_datadir}/metainfo/org.mattdm.icebreaker.metainfo.xml

%files
%license LICENSE
%doc README README.themes TODO ChangeLog
%{_bindir}/icebreaker
%{_datadir}/applications/icebreaker.desktop
%{_datadir}/metainfo/org.mattdm.icebreaker.metainfo.xml
%{_datadir}/icebreaker
%{_mandir}/man6/*

%changelog
