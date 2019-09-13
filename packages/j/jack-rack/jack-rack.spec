#
# spec file for package jack-rack
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           jack-rack
Version:        1.4.7
Release:        0
Summary:        LADSPA Effects Rack for JACK
License:        GPL-2.0+
Group:          Productivity/Multimedia/Sound/Utilities
Url:            http://jack-rack.sf.net/
Source:         %{name}-%{version}.tar.bz2
Patch0:         jack-rack-undeprec.dif
Patch1:         jack-rack-inc-fix.diff
Patch3:         jack-rack-ld_fix.diff
BuildRequires:  automake
BuildRequires:  ladspa-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(gail)
BuildRequires:  pkgconfig(gdk-2.0)
BuildRequires:  pkgconfig(gdk-x11-2.0)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(gtk+-unix-print-2.0)
BuildRequires:  pkgconfig(gtk+-x11-2.0)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(libxml-2.0)
#BuildRequires:  libgnomeui-devel
#BuildRequires:  pkgconfig(lrdf)
#BuildRequires:  pkgconfig(raptor2)
Requires:       jack
Requires:       ladspa

%description
JACK Rack is a stereo LADSPA effects rack for the JACK audio API.  You
can insert LADSPA effects through JACK Rack. It uses GTK+ 2 for the
GUI.

%prep
%setup -q
%patch0
%patch1
%patch3

%build
autoreconf -fi
%configure \
    --disable-gnome

make %{?_smp_mflags}

%install
%make_install
%suse_update_desktop_file jack-rack AudioVideo Music
%find_lang %{name}

%post
%desktop_database_post

%postun
%desktop_database_postun

%files -f %{name}.lang
%doc AUTHORS BUGS ChangeLog NEWS README THANKS TODO
%license COPYING
%{_bindir}/*
%{_datadir}/applications/*
%dir %{_datadir}/dtds
%{_datadir}/dtds/*
%{_datadir}/jack-rack
%{_datadir}/pixmaps/*.png

%changelog
