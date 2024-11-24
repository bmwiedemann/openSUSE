#
# spec file for package localsearch
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


%define lsAPI 3.0
%define tinysparql_basever 3.8

Name:           localsearch
Version:        3.8.1
Release:        0
Summary:        Search tool and indexer using tinysparql
License:        GPL-2.0-or-later
Group:          System/GUI/GNOME
URL:            https://gitlab.gnome.org/GNOME/localsearch
Source0:        %{name}-%{version}.tar.zst
BuildRequires:  asciidoc
BuildRequires:  giflib-devel
BuildRequires:  intltool >= 0.40.0
BuildRequires:  libtiff-devel
BuildRequires:  libtool
BuildRequires:  meson >= 0.51.0
BuildRequires:  pkgconfig
BuildRequires:  vala
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(enca) >= 1.9
BuildRequires:  pkgconfig(exempi-2.0) >= 2.1.0
BuildRequires:  pkgconfig(gexiv2)
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.62.0
BuildRequires:  pkgconfig(glib-2.0) >= 2.62.0
BuildRequires:  pkgconfig(gmodule-2.0) >= 2.62.0
BuildRequires:  pkgconfig(gobject-introspection-1.0)
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
BuildRequires:  pkgconfig(tinysparql-3.0)
BuildRequires:  pkgconfig(totem-plparser)
BuildRequires:  pkgconfig(upower-glib) >= 0.9.0
# The schema files moved from libtracker-common to tracker-miners
Conflicts:      libtracker-common-1_0 < 1.99
# Make sure tracker is being updated to 1.99 too
Conflicts:      tracker < 3.7.99
Obsoletes:      tracker-miner-rss <= 2.2.2
Requires:       tinysparql >= %{tinysparql_basever}
# Dropped tracker-miner-files subpackage / Rename to localsearch
# Make upgrades after rename go well
Provides:       tracker-miners-files = %{version}
Obsoletes:      tracker-miner-files < 3.7.99
Obsoletes:      tracker-miners < 3.7.99

%description
LocalSearch is a desktop-neutral object database, tag/metadata database,
search tool and indexer.

These are the sources for the search tool and indexer (e.g. files, rss)

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
%find_lang %{name}3

%post
%systemd_user_post localsearch-3.service localsearch-control-3.service localsearch-writeback-3.service

%preun
%systemd_user_preun localsearch-3.service localsearch-control-3.service localsearch-writeback-3.service

%files
%license COPYING
%doc README.md
%{_bindir}/localsearch
%{_datadir}/dbus-1/interfaces/org.freedesktop.Tracker3.Miner.Files.Index.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.Tracker3.Miner.xml
%{_datadir}/dbus-1/services/org.freedesktop.LocalSearch3.Control.service
%{_datadir}/dbus-1/services/org.freedesktop.LocalSearch3.service
%{_datadir}/dbus-1/services/org.freedesktop.LocalSearch3.Writeback.service
%{_datadir}/dbus-1/services/org.freedesktop.Tracker3.Miner.Files.Control.service
%{_datadir}/dbus-1/services/org.freedesktop.Tracker3.Miner.Files.service
%{_datadir}/dbus-1/services/org.freedesktop.Tracker3.Writeback.service
%{_datadir}/glib-2.0/schemas/org.freedesktop.Tracker3.Extract.gschema.xml
%{_datadir}/glib-2.0/schemas/org.freedesktop.Tracker3.FTS.gschema.xml
%{_datadir}/glib-2.0/schemas/org.freedesktop.Tracker3.Miner.Files.gschema.xml
%{_datadir}/glib-2.0/schemas/org.freedesktop.TrackerMiners3.enums.xml
%dir %{_datadir}/localsearch3
%dir %{_datadir}/localsearch3/domain-ontologies
%dir %{_datadir}/localsearch3/extract-rules
%dir %{_datadir}/localsearch3/miners
%{_datadir}/localsearch3/domain-ontologies/default.rule
%{_datadir}/localsearch3/extract-rules/10-abw.rule
%{_datadir}/localsearch3/extract-rules/10-bmp.rule
%{_datadir}/localsearch3/extract-rules/10-comics.rule
%{_datadir}/localsearch3/extract-rules/10-desktop.rule
%{_datadir}/localsearch3/extract-rules/10-ebooks.rule
%{_datadir}/localsearch3/extract-rules/10-epub.rule
%{_datadir}/localsearch3/extract-rules/10-folder.rule
%{_datadir}/localsearch3/extract-rules/10-gif.rule
%{_datadir}/localsearch3/extract-rules/10-html.rule
%{_datadir}/localsearch3/extract-rules/10-ico.rule
%{_datadir}/localsearch3/extract-rules/10-jpeg.rule
%{_datadir}/localsearch3/extract-rules/10-mp3.rule
%{_datadir}/localsearch3/extract-rules/10-msoffice.rule
%{_datadir}/localsearch3/extract-rules/10-oasis.rule
%{_datadir}/localsearch3/extract-rules/10-pdf.rule
%{_datadir}/localsearch3/extract-rules/10-png.rule
%{_datadir}/localsearch3/extract-rules/10-ps.rule
%{_datadir}/localsearch3/extract-rules/10-raw.rule
%{_datadir}/localsearch3/extract-rules/10-svg.rule
%{_datadir}/localsearch3/extract-rules/10-tiff.rule
%{_datadir}/localsearch3/extract-rules/10-xps.rule
%{_datadir}/localsearch3/extract-rules/11-iso.rule
%{_datadir}/localsearch3/extract-rules/11-msoffice-xml.rule
%{_datadir}/localsearch3/extract-rules/15-executable.rule
%{_datadir}/localsearch3/extract-rules/15-games.rule
%{_datadir}/localsearch3/extract-rules/15-gstreamer-guess.rule
%{_datadir}/localsearch3/extract-rules/15-playlist.rule
%{_datadir}/localsearch3/extract-rules/15-text.rule
%{_datadir}/localsearch3/extract-rules/90-disc-generic.rule
%{_datadir}/localsearch3/extract-rules/90-gstreamer-audio-generic.rule
%{_datadir}/localsearch3/extract-rules/90-gstreamer-video-generic.rule
%{_datadir}/localsearch3/miners/org.freedesktop.Tracker3.Miner.Files.service
%dir %{_libdir}/localsearch-%{lsAPI}
%dir %{_libdir}/localsearch-%{lsAPI}/extract-modules
%dir %{_libdir}/localsearch-%{lsAPI}/trackertestutils
%dir %{_libdir}/localsearch-%{lsAPI}/writeback-modules
%{_libdir}/localsearch-%{lsAPI}/extract-modules/libextract-abw.so
%{_libdir}/localsearch-%{lsAPI}/extract-modules/libextract-bmp.so
%{_libdir}/localsearch-%{lsAPI}/extract-modules/libextract-desktop.so
%{_libdir}/localsearch-%{lsAPI}/extract-modules/libextract-disc-generic.so
%{_libdir}/localsearch-%{lsAPI}/extract-modules/libextract-dummy.so
%{_libdir}/localsearch-%{lsAPI}/extract-modules/libextract-epub.so
%{_libdir}/localsearch-%{lsAPI}/extract-modules/libextract-gif.so
%{_libdir}/localsearch-%{lsAPI}/extract-modules/libextract-gstreamer.so
%{_libdir}/localsearch-%{lsAPI}/extract-modules/libextract-html.so
%{_libdir}/localsearch-%{lsAPI}/extract-modules/libextract-icon.so
%{_libdir}/localsearch-%{lsAPI}/extract-modules/libextract-iso.so
%{_libdir}/localsearch-%{lsAPI}/extract-modules/libextract-jpeg.so
%{_libdir}/localsearch-%{lsAPI}/extract-modules/libextract-mp3.so
%{_libdir}/localsearch-%{lsAPI}/extract-modules/libextract-msoffice-xml.so
%{_libdir}/localsearch-%{lsAPI}/extract-modules/libextract-msoffice.so
%{_libdir}/localsearch-%{lsAPI}/extract-modules/libextract-oasis.so
%{_libdir}/localsearch-%{lsAPI}/extract-modules/libextract-pdf.so
%{_libdir}/localsearch-%{lsAPI}/extract-modules/libextract-playlist.so
%{_libdir}/localsearch-%{lsAPI}/extract-modules/libextract-png.so
%{_libdir}/localsearch-%{lsAPI}/extract-modules/libextract-ps.so
%{_libdir}/localsearch-%{lsAPI}/extract-modules/libextract-raw.so
%{_libdir}/localsearch-%{lsAPI}/extract-modules/libextract-text.so
%{_libdir}/localsearch-%{lsAPI}/extract-modules/libextract-tiff.so
%{_libdir}/localsearch-%{lsAPI}/extract-modules/libextract-xps.so
%{_libdir}/localsearch-%{lsAPI}/libtracker-extract.so
%{_libdir}/localsearch-%{lsAPI}/trackertestutils/__init__.py
%{_libdir}/localsearch-%{lsAPI}/trackertestutils/__main__.py
%{_libdir}/localsearch-%{lsAPI}/trackertestutils/dbusdaemon.py
%{_libdir}/localsearch-%{lsAPI}/trackertestutils/dconf.py
%{_libdir}/localsearch-%{lsAPI}/trackertestutils/helpers.py
%{_libdir}/localsearch-%{lsAPI}/trackertestutils/localsearch3-test-sandbox
%{_libdir}/localsearch-%{lsAPI}/trackertestutils/mainloop.py
%{_libdir}/localsearch-%{lsAPI}/trackertestutils/psutil_mini.py
%{_libdir}/localsearch-%{lsAPI}/trackertestutils/sandbox.py
%{_libdir}/localsearch-%{lsAPI}/trackertestutils/storehelper.py
%{_libdir}/localsearch-%{lsAPI}/writeback-modules/libwriteback-gstreamer.so
%{_libdir}/localsearch-%{lsAPI}/writeback-modules/libwriteback-xmp.so
%{_libexecdir}/localsearch-3
%{_libexecdir}/localsearch-control-3
%{_libexecdir}/localsearch-extractor-3
%{_libexecdir}/localsearch-writeback-3
%{_mandir}/man1/localsearch-3.1%{?ext_man}
%{_mandir}/man1/localsearch-daemon.1%{?ext_man}
%{_mandir}/man1/localsearch-extract.1%{?ext_man}
%{_mandir}/man1/localsearch-index.1%{?ext_man}
%{_mandir}/man1/localsearch-info.1%{?ext_man}
%{_mandir}/man1/localsearch-reset.1%{?ext_man}
%{_mandir}/man1/localsearch-search.1%{?ext_man}
%{_mandir}/man1/localsearch-status.1%{?ext_man}
%{_mandir}/man1/localsearch-tag.1%{?ext_man}
%{_mandir}/man1/localsearch-writeback-3.1%{?ext_man}
%{_sysconfdir}/xdg/autostart/localsearch-3.desktop
%{_userunitdir}/localsearch-3.service
%{_userunitdir}/localsearch-control-3.service
%{_userunitdir}/localsearch-writeback-3.service

%files lang -f %{name}3.lang

%changelog
