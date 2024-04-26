#
# spec file for package tracker-miners
#
# Copyright (c) 2024 SUSE LLC
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


%define tracker_basever 3.7

Name:           tracker-miners
Version:        3.7.2
Release:        0
Summary:        Various miners for Tracker
License:        GPL-2.0-or-later
Group:          System/GUI/GNOME
URL:            https://wiki.gnome.org/Projects/Tracker
Source0:        %{name}-%{version}.tar.zst
BuildRequires:  asciidoc
BuildRequires:  giflib-devel
BuildRequires:  intltool >= 0.40.0
BuildRequires:  libtiff-devel
BuildRequires:  libtool
BuildRequires:  meson >= 0.51.0
BuildRequires:  pkgconfig
BuildRequires:  tracker-data-files
BuildRequires:  vala
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(enca) >= 1.9
BuildRequires:  pkgconfig(exempi-2.0) >= 2.1.0
BuildRequires:  pkgconfig(gexiv2)
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.62.0
BuildRequires:  pkgconfig(glib-2.0) >= 2.62.0
BuildRequires:  pkgconfig(gmodule-2.0) >= 2.62.0
BuildRequires:  pkgconfig(gstreamer-1.0) >= 0.10.31
BuildRequires:  pkgconfig(gstreamer-audio-1.0) >= 0.10.31
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0) >= 0.10.31
BuildRequires:  pkgconfig(gstreamer-tag-1.0) >= 0.10.31
BuildRequires:  pkgconfig(icu-i18n) >= 4.8.1.1
BuildRequires:  pkgconfig(icu-uc) >= 4.8.1.1
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libcue) >= 2.0.0
BuildRequires:  pkgconfig(libexif) >= 0.6
BuildRequires:  pkgconfig(libgsf-1) >= 1.14.24
BuildRequires:  pkgconfig(libgxps)
BuildRequires:  pkgconfig(libiptcdata)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libnm)
BuildRequires:  pkgconfig(libosinfo-1.0) >= 0.2.9
BuildRequires:  pkgconfig(libseccomp) >= 2.0
BuildRequires:  pkgconfig(libxml-2.0) >= 2.6
BuildRequires:  pkgconfig(poppler-glib) >= 0.16.0
BuildRequires:  pkgconfig(totem-plparser)
BuildRequires:  pkgconfig(tracker-sparql-3.0) >= 3.5.0
BuildRequires:  pkgconfig(upower-glib) >= 0.9.0
# The schema files moved from libtracker-common to tracker-miners
Conflicts:      libtracker-common-1_0 < 1.99
# Make sure tracker is being updated to 1.99 too
Conflicts:      tracker < 1.99
Obsoletes:      tracker-miner-rss <= 2.2.2
Requires:       tracker >= %{tracker_basever}
%requires_ge    tracker-data-files

%description
Tracker is a desktop-neutral object database, tag/metadata database,
search tool and indexer.

These are the sources for the various miners (e.g. files, rss)

%package -n tracker-miner-files
Summary:        Tracker miner to index files and applications
Group:          System/GUI/GNOME
Requires:       %{name} >= %{version}

%description -n tracker-miner-files
Tracker is a desktop-neutral object database, tag/metadata database,
search tool and indexer.

This package contains a miner to index files and applications.

%lang_package

%prep
%autosetup -p1

%build
%meson \
	-Dsystemd_user_services_dir=%{_userunitdir} \
	-Dfunctional_tests=false \
	-Dminer_rss=false \
	%{nil}
%meson_build

%install
%meson_install
%find_lang tracker3-miners

%post
%systemd_user_post tracker-writeback-3.service tracker-miner-fs-3.service tracker-miner-fs-control-3.service

%preun
%systemd_user_preun tracker-writeback-3.service tracker-miner-fs-3.service tracker-miner-fs-control-3.service

%files
%license COPYING
%doc README.md
%{_bindir}/tracker3-daemon
%{_bindir}/tracker3-extract
%{_bindir}/tracker3-index
%{_bindir}/tracker3-info
%{_bindir}/tracker3-reset
%{_bindir}/tracker3-search
%{_bindir}/tracker3-status
%{_bindir}/tracker3-tag
%{_datadir}/dbus-1/interfaces/org.freedesktop.Tracker3.Miner.xml
%{_datadir}/dbus-1/services/org.freedesktop.Tracker3.Writeback.service
%{_datadir}/glib-2.0/schemas/org.freedesktop.Tracker3.Extract.gschema.xml
%{_datadir}/glib-2.0/schemas/org.freedesktop.Tracker3.FTS.gschema.xml
%dir %{_datadir}/tracker3
%{_datadir}/tracker3/commands/
%{_datadir}/tracker3-miners/
%dir %{_libdir}/tracker-miners-3.0
%{_libdir}/tracker-miners-3.0/extract-modules/
%{_libdir}/tracker-miners-3.0/libtracker-extract.so
%{_libdir}/tracker-miners-3.0/writeback-modules/
%{_libexecdir}/tracker-extract-3
%{_libexecdir}/tracker-writeback-3
%{_mandir}/man1/tracker3-daemon.1%{?ext_man}
%{_mandir}/man1/tracker3-extract.1%{?ext_man}
%{_mandir}/man1/tracker3-index.1%{?ext_man}
%{_mandir}/man1/tracker3-info.1%{?ext_man}
%{_mandir}/man1/tracker3-reset.1%{?ext_man}
%{_mandir}/man1/tracker3-search.1%{?ext_man}
%{_mandir}/man1/tracker3-status.1%{?ext_man}
%{_mandir}/man1/tracker3-tag.1%{?ext_man}
%{_mandir}/man1/tracker-writeback-3.1%{?ext_man}
%{_userunitdir}/tracker-writeback-3.service

%files -n tracker-miner-files
%{_datadir}/dbus-1/interfaces/org.freedesktop.Tracker3.Miner.Files.Index.xml
%{_datadir}/dbus-1/services/org.freedesktop.Tracker3.Miner.Files.Control.service
%{_datadir}/dbus-1/services/org.freedesktop.Tracker3.Miner.Files.service
%{_datadir}/glib-2.0/schemas/org.freedesktop.Tracker3.Miner.Files.gschema.xml
%{_datadir}/glib-2.0/schemas/org.freedesktop.TrackerMiners3.enums.xml
%{_libexecdir}/tracker-miner-fs-3
%{_libexecdir}/tracker-miner-fs-control-3
%{_mandir}/man1/tracker-miner-fs-3.1%{?ext_man}
%{_sysconfdir}/xdg/autostart/tracker-miner-fs-3.desktop
%{_userunitdir}/tracker-miner-fs-3.service
%{_userunitdir}/tracker-miner-fs-control-3.service

%files lang -f tracker3-miners.lang

%changelog
