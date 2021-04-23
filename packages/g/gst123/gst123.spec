#
# spec file for package gst123
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           gst123
Version:        0.3.5
Release:        0
Summary:        GStreamer based Command Line Music Player
License:        LGPL-2.0+
Group:          Productivity/Multimedia/Sound/Players
URL:            http://space.twc.de/~stefan/gst123.php
Source:         http://space.twc.de/~stefan/gst123/%{name}-%{version}.tar.bz2
Source1:        gst123.desktop
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-base-1.0)
BuildRequires:  pkgconfig(gstreamer-video-1.0)
BuildRequires:  pkgconfig(gtk+-2.0)
%if 0%{?suse_version} >= 1500
BuildRequires:  pkgconfig(ncurses) >= 5
%else
BuildRequires:  ncurses-devel
%endif

%description
The gst123 program is a command line player akin to ogg123 or mpg123,
but uses gstreamer for decoding, so supports all the codecs gstreamer
knows.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags} V=1

%install
%make_install
install -D -m0644 "%{SOURCE1}" "%{buildroot}%{_datadir}/applications/%{name}.desktop"
%suse_update_desktop_file -r "%{name}" AudioVideo Player
%find_lang "%{name}" || echo -n >"%{name}.lang"

%if 0%{?suse_version} < 1500
%post
%desktop_database_post

%postun
%desktop_database_postun
%endif

%files -f "%{name}.lang"
%doc AUTHORS COPYING NEWS
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{ext_man}
%{_datadir}/applications/%{name}.desktop

%changelog
