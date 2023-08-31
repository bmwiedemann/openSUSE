#
# spec file for package gst123
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2012-2013 Pascal Bleser <pascal.bleser@opensuse.org>
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


Name:           gst123
Version:        0.4.1
Release:        0
Summary:        GStreamer based Command Line Music Player
License:        LGPL-2.0-or-later
Group:          Productivity/Multimedia/Sound/Players
URL:            https://space.twc.de/~stefan/gst123.php
Source:         https://github.com/swesterfeld/gst123/releases/download/%{version}/%{name}-%{version}.tar.bz2
Source1:        gst123.desktop
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-base-1.0)
BuildRequires:  pkgconfig(gstreamer-video-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(ncurses) >= 5

%description
The gst123 program is a command line player akin to ogg123 or mpg123,
but uses gstreamer for decoding, so supports all the codecs gstreamer
knows.

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install
install -D -m0644 "%{SOURCE1}" "%{buildroot}%{_datadir}/applications/%{name}.desktop"
%suse_update_desktop_file -r "%{name}" AudioVideo Player
%find_lang "%{name}" || echo -n >"%{name}.lang"

%files -f "%{name}.lang"
%license COPYING
%doc AUTHORS NEWS
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_datadir}/applications/%{name}.desktop

%changelog
