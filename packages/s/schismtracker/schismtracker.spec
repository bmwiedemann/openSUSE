#
# spec file for package schismtracker
#
# Copyright (c) 2022 SUSE LLC
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


Name:           schismtracker
Version:        20221201
Release:        0
Summary:        Music editor that matches the look and feel of Impulse Tracker
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Sound/Editors and Convertors
URL:            http://schismtracker.org/
Source:         https://github.com/schismtracker/schismtracker/archive/refs/tags/%version.tar.gz
Source2:        %name.desktop
Patch1:         schism-alsa.diff
Patch2:         schism-nodate.diff
Patch3:         schism-deptrack.diff
BuildRequires:  alsa-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  freeglut-devel
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  python3-base
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xv)

%description
Schism Tracker is a reimplementation of Impulse Tracker, a
program used to create music without the requirements of
specialized, expensive equipment, and with a unique "finger feel"
that is difficult to replicate in-part. The player is based on a
modified version of the Modplug engine, with a number of
bugfixes and changes to improve IT playback.

%prep
%autosetup -p1

%build
autoreconf -fi
%configure
%make_build

%install
b="%buildroot"
%make_install
for size in 16 22 24 32 36 48 64 72 96 128 192; do
	install -Dm 0644 "icons/schism-icon-$size.png" \
		"$b/%_datadir/icons/hicolor/${size}x$size/apps/%name.png"
done
install -Dm 0644 icons/schism-icon.svg \
	"$b/%_datadir/icons/hicolor/scalable/apps/%name.svg"
# install desktop file
%suse_update_desktop_file -i %name

%files
%license COPYING
%doc NEWS README.md
%_bindir/schismtracker
%_datadir/icons/hicolor
%_datadir/applications/*
%_datadir/pixmaps/*
%_mandir/man*/*

%changelog
