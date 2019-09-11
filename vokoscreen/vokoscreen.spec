#
# spec file for package vokoscreen
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2015 Mariusz Fik <fisiu@opensuse.org>.
# Copyright (c) 2015 Packman team: http://packman.links2linux.org/
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


Name:           vokoscreen
Version:        2.5.0
Release:        0
Summary:        Screencast creator
License:        GPL-2.0
Group:          Productivity/Multimedia/Other
Url:            http://linuxecke.volkoh.de/vokoscreen/vokoscreen.html
Source:         https://github.com/vkohaupt/vokoscreen/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  libqt5-linguist
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(libv4l2)
BuildRequires:  pkgconfig(opencv)
BuildRequires:  pkgconfig(xrandr)
# Required for recording
Requires:       ffmpeg
# Required for mp3 audio
Requires:       lame

%description
vokoscreen is an easy to use screencast creator to record educational videos,
live recordings of browser, installation, videoconferences, etc.

%prep
%setup -q

%build
%qmake5
%make_jobs

%install
%qmake5_install

%post
%desktop_database_post

%postun
%desktop_database_postun

%files
%defattr(-,root,root)
%doc AUTHORS COPYING CHANGE CREDITS
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/%{name}.1%{ext_man}
%{_datadir}/pixmaps/%{name}.png

%changelog
