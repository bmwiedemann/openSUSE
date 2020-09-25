#
# spec file for package tracker-miners
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


Name:           tracker2-miners
%define _name   tracker-miners
Version:        2.3.5
Release:        0
Summary:        Various miners for Tracker
License:        GPL-2.0-or-later
Group:          System/GUI/GNOME
URL:            https://wiki.gnome.org/Projects/Tracker
Source0:        https://download.gnome.org/sources/tracker-miners/2.3/%{_name}-%{version}.tar.xz

# PATCh-FIX-UPSTREAM tracker-miners-bsc1165635-crawl-timestamp.patch boo#1165635 mgorse@suse.com -- properly set crawl timestamp.
Patch0:         tracker-miners-bsc1165635-crawl-timestamp.patch

BuildRequires:  giflib-devel
BuildRequires:  intltool >= 0.40.0
BuildRequires:  libtiff-devel
BuildRequires:  libtool
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  vala
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(enca) >= 1.9
BuildRequires:  pkgconfig(exempi-2.0) >= 2.1.0
BuildRequires:  pkgconfig(flac) >= 1.2.1
BuildRequires:  pkgconfig(gexiv2)
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.44.0
BuildRequires:  pkgconfig(glib-2.0) >= 2.44.0
BuildRequires:  pkgconfig(gmodule-2.0) >= 2.44.0
BuildRequires:  pkgconfig(gstreamer-1.0) >= 0.10.31
BuildRequires:  pkgconfig(gstreamer-audio-1.0) >= 0.10.31
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0) >= 0.10.31
BuildRequires:  pkgconfig(gstreamer-tag-1.0) >= 0.10.31
BuildRequires:  pkgconfig(icu-i18n) >= 4.8.1.1
BuildRequires:  pkgconfig(icu-uc) >= 4.8.1.1
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libcue)
BuildRequires:  pkgconfig(libexif) >= 0.6
BuildRequires:  pkgconfig(libgsf-1) >= 1.14.24
BuildRequires:  pkgconfig(libgxps)
BuildRequires:  pkgconfig(libiptcdata)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libosinfo-1.0) >= 0.2.9
BuildRequires:  pkgconfig(libseccomp) >= 2.0
BuildRequires:  pkgconfig(libxml-2.0) >= 2.6
BuildRequires:  pkgconfig(poppler-glib) >= 0.16.0
BuildRequires:  pkgconfig(totem-plparser)
BuildRequires:  pkgconfig(tracker-miner-2.0) >= 2.2.0
BuildRequires:  pkgconfig(tracker-sparql-2.0) >= 2.2.0
BuildRequires:  pkgconfig(upower-glib) >= 0.9.0
BuildRequires:  pkgconfig(vorbisfile) >= 0.22
# The schema files moved from libtracker-common to tracker-miners
Conflicts:      libtracker-common-1_0 < 1.99
# Make sure tracker is being updated to 1.99 too
Conflicts:      tracker < 1.99
Obsoletes:      tracler-miners <= %{version}
Provides:       tracker-miners = %{version}
Obsoletes:      tracker-miner-rss <= 2.2.2
Obsoletes:      tracker-miner-files-lang <= %{version}

%description
Tracker is a desktop-neutral object database, tag/metadata database,
search tool and indexer.

These are the sources for the various miners (e.g. files, rss)

%package -n tracker2-miner-files
Summary:        Tracker miner to index files and applications
Group:          System/GUI/GNOME
Requires:       %{name} >= %{version}
Provides:       tracker-miner-files = %{version}
Obsoletes:      tracker-miner-files <= %{version}

%description -n tracker2-miner-files
Tracker is a desktop-neutral object database, tag/metadata database,
search tool and indexer.

This package contains a miner to index files and applications.

%lang_package

%prep
%autosetup -p1 -n %{_name}-%{version}

%build
%meson \
	-Dfunctional_tests=false \
	-Dsystemd_user_services=%{_userunitdir} \
	-Dminer_rss=false \
	%{nil}
%meson_build

%install
%meson_install
%find_lang %{_name}
rm -f %{_libdir}/tracker-miners-2.0/libtracker-miners-common.a

%files
%license COPYING
%doc README.md
%{_libexecdir}/tracker-extract
%{_libexecdir}/tracker-writeback
%{_mandir}/man1/tracker-extract.1%{ext_man}
%{_mandir}/man1/tracker-writeback.1%{ext_man}
%dir %{_datadir}/tracker
%dir %{_datadir}/tracker/miners
%{_datadir}/tracker/miners/org.freedesktop.Tracker1.Miner.Extract.service
%dir %{_datadir}/dbus-1
%dir %{_datadir}/dbus-1/services
%{_datadir}/dbus-1/services/org.freedesktop.Tracker1.Miner.Extract.service
%{_datadir}/dbus-1/services/org.freedesktop.Tracker1.Writeback.service
%{_datadir}/glib-2.0/schemas/org.freedesktop.TrackerMiners.enums.xml
%{_datadir}/glib-2.0/schemas/org.freedesktop.Tracker.Extract.gschema.xml
%{_datadir}/glib-2.0/schemas/org.freedesktop.Tracker.Writeback.gschema.xml
%{_datadir}/%{_name}/
%{_userunitdir}/tracker-extract.service
%{_userunitdir}/tracker-writeback.service
%dir %{_libdir}/tracker-miners-2.0
%{_libdir}/tracker-miners-2.0/extract-modules/
%{_libdir}/tracker-miners-2.0/writeback-modules/
%{_libdir}/tracker-miners-2.0/libtracker-extract.so

%files -n tracker2-miner-files
%{_libexecdir}/tracker-miner-fs
%{_mandir}/man1/tracker-miner-fs.1%{ext_man}
%{_userunitdir}/tracker-miner-fs.service
%{_datadir}/tracker/miners/org.freedesktop.Tracker1.Miner.Files.service
%{_datadir}/dbus-1/services/org.freedesktop.Tracker1.Miner.Files.service
%{_datadir}/glib-2.0/schemas/org.freedesktop.Tracker.Miner.Files.gschema.xml

%files lang -f %{_name}.lang

%changelog
