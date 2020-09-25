#
# spec file for package leechcraft
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


%bcond_without ffmpeg

%define plugin_dir %{_libdir}/leechcraft/plugins-qt5
%define translations_dir %{_datadir}/leechcraft/translations
%define settings_dir %{_datadir}/leechcraft/settings
%define qml_dir %{_datadir}/leechcraft/qml5

%define so_ver -qt5-0_6_75
%define LEECHCRAFT_VERSION 0.6.70-13907-g785196c688

%define db_postfix %{so_ver}_1
%define gui_postfix %{so_ver}_1
%define models_postfix %{so_ver}_1
%define network_postfix %{so_ver}_1
%define qml_postfix %{so_ver}_2
%define shortcuts_postfix %{so_ver}
%define sll_postfix %{so_ver}_1
%define svcauth_postfix %{so_ver}
%define sys_postfix %{so_ver}_1
%define tags_postfix %{so_ver}_1
%define threads_postfix %{so_ver}
%define x11_postfix %{so_ver}
%define xdg_postfix %{so_ver}
%define xpc_postfix %{so_ver}_2
%define xsd_postfix %{so_ver}

Name:           leechcraft
Version:        0.6.70+git.13907.g785196c688
Release:        0
Summary:        Modular Internet Client
License:        BSL-1.0
Group:          Productivity/Networking/Other
URL:            http://leechcraft.org

Source0:        leechcraft-%{LEECHCRAFT_VERSION}.tar.xz
Source4:        %{name}-rpmlintrc
Source8:        leechcraft-session.1
Source9:        lc_plugin_wrapper-qt5.1

# PATCH-FIX-OPENSUSE to save Qt 5.12 (i.e. Leap 15.2) compatibility.
Patch0:         leechcraft-Qt5_12.patch
# PATCH-FIX-OPENSUSE vs. Leap 15.2 qtermwidget' pkgconfig issue.
Patch1:         leechcraft-qtermwidget-Leap-15_2.patch
# PATCH-FIX-OPENSUSE leechcraft-libtorrent-legacy.patch
Patch2:         leechcraft-libtorrent-legacy.patch

BuildRequires:  cmake >= 3.8
BuildRequires:  fdupes
BuildRequires:  file-devel
%if 0%{?sle_version} > 150300 || 0%{?suse_version} > 1500
BuildRequires:  gcc-c++ >= 8
%else
BuildRequires:  gcc8-c++
%endif
BuildRequires:  hicolor-icon-theme
BuildRequires:  libQt5Gui-private-headers-devel >= 5.9
BuildRequires:  libQt5Sql5-sqlite >= 5.9
BuildRequires:  libboost_atomic-devel
BuildRequires:  libboost_chrono-devel
BuildRequires:  libboost_date_time-devel
BuildRequires:  libboost_filesystem-devel
BuildRequires:  libboost_locale-devel
BuildRequires:  libboost_program_options-devel
BuildRequires:  libboost_system-devel
BuildRequires:  libboost_thread-devel
BuildRequires:  libjpeg-devel
BuildRequires:  liblastfm-qt5-devel
BuildRequires:  libqt5-qtbase-common-devel >= 5.9
BuildRequires:  libqxmpp-qt5-devel >= 1.1
BuildRequires:  libsensors4-devel
BuildRequires:  libtidy-devel
BuildRequires:  pkgconfig
%if 0%{?suse_version} > 1325
BuildRequires:  wt-devel
%endif
BuildRequires:  cmake(Qt5LinguistTools) >= 5.9
BuildRequires:  pkgconfig(Qt5Concurrent) >= 5.9
BuildRequires:  pkgconfig(Qt5Core) >= 5.9
BuildRequires:  pkgconfig(Qt5DBus) >= 5.9
BuildRequires:  pkgconfig(Qt5Gui) >= 5.9
BuildRequires:  pkgconfig(Qt5Multimedia) >= 5.9
BuildRequires:  pkgconfig(Qt5Network) >= 5.9
BuildRequires:  pkgconfig(Qt5OpenGL) >= 5.9
BuildRequires:  pkgconfig(Qt5Positioning) >= 5.9
BuildRequires:  pkgconfig(Qt5PrintSupport) >= 5.9
BuildRequires:  pkgconfig(Qt5Qml) >= 5.9
BuildRequires:  pkgconfig(Qt5Quick) >= 5.9
BuildRequires:  pkgconfig(Qt5QuickWidgets) >= 5.9
BuildRequires:  pkgconfig(Qt5Qwt6) >= 5.9
BuildRequires:  pkgconfig(Qt5Script) >= 5.9
BuildRequires:  pkgconfig(Qt5Sensors) >= 5.9
BuildRequires:  pkgconfig(Qt5Sql) >= 5.9
BuildRequires:  pkgconfig(Qt5Svg) >= 5.9
BuildRequires:  pkgconfig(Qt5WebChannel) >= 5.9
BuildRequires:  pkgconfig(Qt5WebKit) >= 5.9
BuildRequires:  pkgconfig(Qt5WebKitWidgets) >= 5.9
BuildRequires:  pkgconfig(Qt5Widgets) >= 5.9
BuildRequires:  pkgconfig(Qt5X11Extras) >= 5.9
BuildRequires:  pkgconfig(Qt5Xml) >= 5.9
BuildRequires:  pkgconfig(Qt5XmlPatterns) >= 5.9
BuildRequires:  pkgconfig(bzip2)
%if 0%{?suse_version} > 1325 || 0%{?sle_version} >= 120300
BuildRequires:  pkgconfig(ddjvuapi)
%endif
BuildRequires:  pkgconfig(gstreamer-app-1.0)
BuildRequires:  pkgconfig(hunspell)
%if %{with ffmpeg}
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavdevice)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libchromaprint)
%endif
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libguess)
BuildRequires:  pkgconfig(libidn)
BuildRequires:  pkgconfig(libmaxminddb)
BuildRequires:  pkgconfig(libmtp)
BuildRequires:  pkgconfig(libnl-3.0)
BuildRequires:  pkgconfig(libotr)
BuildRequires:  pkgconfig(libpcre)
%if %{with ffmpeg}
BuildRequires:  pkgconfig(libpostproc)
%endif
%if 0%{?sle_version} > 150300 || 0%{?suse_version} > 1500
%ifarch %ix86 x86_64 ppc64 ppc64le
BuildRequires:  pkgconfig(libprojectM) >= 3
%endif
%endif
BuildRequires:  pkgconfig(libqrencode)
%if %{with ffmpeg}
BuildRequires:  pkgconfig(libswresample)
BuildRequires:  pkgconfig(libswscale)
%endif
BuildRequires:  pkgconfig(libtcmalloc)
%ifarch %ix86 x86_64 %arm ppc64le
%if 0%{?suse_version} > 1500
BuildRequires:  pkgconfig(libtorrent-rasterbar-1) >= 1.2.0
%else
BuildRequires:  pkgconfig(libtorrent-rasterbar) >= 1.2.0
%endif
%endif

BuildRequires:  pkgconfig(libudev)
%if 0%{?suse_version} > 1325 || 0%{?sle_version} >= 120300
BuildRequires:  pkgconfig(poppler-cpp)
BuildRequires:  pkgconfig(poppler-qt5)
%endif
BuildRequires:  pkgconfig(purple)
BuildRequires:  pkgconfig(qca2-qt5)
BuildRequires:  pkgconfig(qtermwidget5)
BuildRequires:  pkgconfig(speex)
BuildRequires:  pkgconfig(taglib) >= 1.6
BuildRequires:  pkgconfig(xcb-renderutil)
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(xdamage)
BuildRequires:  pkgconfig(xkbfile)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(xscrnsaver)

BuildConflicts: gstreamer-0_10-devel
BuildConflicts: gstreamer-0_10-plugins-base-devel
BuildConflicts: libgstapp-0_10
BuildConflicts: libgstinterfaces-0_10
BuildConflicts: libgstreamer-0_10

#!BuildIgnore:  openssl

Requires:       oxygen-icon-theme
Recommends:     %{name}-advancednotifications
Recommends:     %{name}-azoth-acetamide
Recommends:     %{name}-azoth-xoox
Recommends:     %{name}-bittorrent
Recommends:     %{name}-blogique
Recommends:     %{name}-dolozhee
Recommends:     %{name}-lackman
Recommends:     %{name}-monocle
Recommends:     %{name}-netstoremanager
Recommends:     %{name}-newlife
Recommends:     %{name}-poshuku
Recommends:     %{name}-scrobbler
Recommends:     %{name}-secman-simplestorage
Recommends:     %{name}-visualnotifications
Suggests:       %{name}-lastfmscrobble

%ifarch ppc64
Obsoletes:      %{name}-bittorrent
%endif
Obsoletes:      %{name}-choroid
Obsoletes:      %{name}-harbinger
%if 0%{?suse_version} < 1325 && 0%{?sle_version} <= 120200
Obsoletes:      %{name}-monocle
%endif
Obsoletes:      %{name}-nacheku
Obsoletes:      %{name}-popishu
Obsoletes:      %{name}-qrosp
Obsoletes:      %{name}-syncer
Obsoletes:      %{name}-vgrabber
Obsoletes:      %{name}-vtyulc

%description
LeechCraft is a modular "Internet client" application.

LeechCraft allows to browse the web, read RSS/Atom feeds, download
files via BitTorrent, HTTP, FTP and DC, automatically stream,
download or play podcasts and other media files and much more.

Features can be added via plugins that can be integrated with
each other, while staying abstract from the exact implementation.

This package contains the main LeechCraft executable, which connects
all the plugins with each other, routes requests between them, tracks
dependencies and performs several other housekeeping tasks.


%package advancednotifications
Summary:        LeechCraft Notifications framework Module
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Requires:       %{name}-visualnotifications = %{version}
Recommends:     %{name}-soundnotifications = %{version}

%description advancednotifications
This package provides an advanced notifications plugin for Leechcraft
which allows to customize notifications better.


%package aggregator
Summary:        LeechCraft RSS/Atom Aggregator Module
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Requires:       %{name}-http = %{version}
Requires:       libQt5Sql5-sqlite
Recommends:     %{name}-poshuku = %{version}
%if 0%{?suse_version} < 1325
Obsoletes:      %{name}-aggregator-webaccess
%endif

%description aggregator
This package provides a RSS/Atom feed reader plugin for LeechCraft.

It features:
 * RSS 0.92/0.93/1.0/2.0, Atom 0.3/1.0;
 * extensions like GeoRSS, MediaRSS, Comment API etc;
 * OPML support;
 * broadcatching and fetching arbitrary data with regexps;
 * tape mode for news display;
 * individual options for each channel like update interval;
 * storage either in SQLite or PostgreSQL;
 * exporting feeds to FB2 for further reading on handheld devices.

A web browser plugin is recommended to show the news in a fancy way.


%package aggregator-bodyfetch
Summary:        LeechCraft Aggregator Bodyfetch Module
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Requires:       %{name}-aggregator

%description aggregator-bodyfetch
This package provides a LeechCraft Aggregator plugin to automatically
fetch full bodies of news items and replace the original teasers from
RSS feeds with them, so that it appears like the full news stories
were originally there.

Fetching is done according to little scripts called recipes. For this to
work, a script provider like Qrosp should be installed. Please refer to the
guide to writing recipes if you are interested in writing your own.


%if 0%{?suse_version} > 1325
%package aggregator-webaccess
Summary:        LeechCraft Aggregator Web Interface Module
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name}-aggregator = %{version}

%description aggregator-webaccess
WebAccess provides a basic web interface for the
Aggregator feed reader, so one can read news
articles from a mobile device or another machine.
%endif

%package anhero
Summary:        LeechCraft Crash handler Module
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Requires:       gdb
Recommends:     %{name}-dolozhee

%description anhero
This package provides a crash handler plugin for LeechCraft
which shows backtraces and aids in sending bug reports.


%package auscrie
Summary:        LeechCraft Screenshooter Module
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Requires:       %{name}-imgaste = %{version}

%description auscrie
This package provides a LeechCraft plugin to make screenshots of
LeechCraft and then either save them locally or upload them to an
imagebin.


%package azoth
Summary:        LeechCraft Instant messenger Module
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Requires:       %{name}-azoth-chatstyler = %{version}
Requires:       %{name}-azoth-protocolplugin
Requires:       %{name}-securestorage = %{version}
Suggests:       %{name}-azoth-standardstyles
Obsoletes:      %{name}-azoth-astrality
Obsoletes:      %{name}-azoth-woodpecker

%description azoth
This package provides a modular, multi-protocol IM client for LeechCraft.

Protocol support is provided by corresponding plugins.
Unlike other multiprotocol clients which tend to implement only those
features that are present in all the protocols, Azoth is modelled after the
XMPP protocol, aiming to provide extensive and full support for XMPP while
remaining usable for other protocols.


%package azoth-abbrev
Summary:        LeechCraft Azoth Abbreviations Module
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name}-azoth-protocolplugin = %{version}
Suggests:       %{name}-xoox
Recommends:     %{name}-acetamide
Recommends:     %{name}-xoox

%description azoth-abbrev
This package provides abbreviations via commands like /abbrev, /unabbrev
and /listabbrevs for LeechCraft Azoth.


%package azoth-acetamide
Summary:        LeechCraft Azoth IRC Module
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name}-azoth = %{version}
Provides:       %{name}-azoth-protocolplugin
Recommends:     %{name}-azoth-mucommands

%description azoth-acetamide
This package provides an IRC protocol plugin for LeechCraft Azoth.

Features:
 * Secure Sockets Layer (SSL) cryptographic protocol.
 * Channel bookmarks.
 * Automatic password entry.
 * Automatic login.


%package azoth-adiumstyles
Summary:        LeechCraft Azoth Adium Styles Module
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name}-azoth = %{version}
Provides:       %{name}-azoth-chatstyler

%description azoth-adiumstyles
This package provides an Adium styles support plugin for LeechCraft Azoth.


%package azoth-autoidler
Summary:        LeechCraft Azoth Module for automatic status change
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name}-azoth = %{version}

%description azoth-autoidler
This package provides a LeechCraft Azoth plugin which can
automatically change your status based on an inactivity period.


%package azoth-autopaste
Summary:        LeechCraft Azoth Autopaste Module
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name}-azoth = %{version}

%description azoth-autopaste
This package provides a plugin for LeechCraft Azoth with
which long messages can automatically be pasted to pastebins.


%package azoth-birthdaynotifier
Summary:        LeechCraft Azoth Birthday Notifier Module
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name}-azoth = %{version}

%description azoth-birthdaynotifier
This package provides a plugin for LeechCraft Azoth with which you
will be notified of your contacts' birthdays if they are present in
vCards.


%package azoth-chathistory
Summary:        LeechCraft Azoth Chat history Module
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name}-azoth = %{version}
Requires:       libQt5Sql5-sqlite

%description azoth-chathistory
This package provides a chat history plugin for LeechCraft Azoth.
It supports storing history from normal one-to-one chats as well as from
multiuser conferences and private chats in conferences. It also allows to
search the logs with SQL's LIKE expressions. SQLite is used for storage.


%package azoth-depester
Summary:        LeechCraft Azoth Ignore Module
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name}-azoth = %{version}

%description azoth-depester
This package provides a plugin for LeechCraft Azoth to ignore
unwanted participants.


%package azoth-embedmedia
Summary:        LeechCraft Azoth Media Objects Module
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name}-azoth = %{version}

%description azoth-embedmedia
This package provides an plugin for LeechCraft Azoth which
allows embedding different media objects in chat tabs.


%package azoth-herbicide
Summary:        LeechCraft Azoth Antispam Module
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name}-azoth = %{version}

%description azoth-herbicide
This package provides a basic antispam plugin for LeechCraft Azoth.

%package azoth-hili
Summary:        LeechCraft Azoth Conference highlights Module
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name}-azoth = %{version}

%description azoth-hili
This package provides a plugin for LeechCraft Azoth to customize
conference highlights.


%package azoth-isterique
Summary:        LeechCraft Azoth Module to remove CAPS
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name}-azoth = %{version}

%description azoth-isterique
This package provides a plugin for LeechCraft Azoth which
can remove excessive CAPS usage from incoming messages.


%package azoth-juick
Summary:        LeechCraft Azoth Juick.com service Module
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name}-azoth = %{version}

%description azoth-juick
This package contains a plugin for LeechCraft Azoth which
provides an enhanced experience with the juick.com microblogging service.


%package azoth-keeso
Summary:        LeechCraft Azoth Text transform Module
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name}-azoth = %{version}

%description azoth-keeso
This package provides a text transform plugin for LeechCraft Azoth.


%package azoth-lastseen
Summary:        LeechCraft Azoth module for "Last Seen" functionality
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name}-azoth = %{version}

%description azoth-lastseen
This package provides a plugin for LeechCraft Azoth which records
contacts' last online and availability time on the client side. It
does not depend on a concrete protocol implementation.


%package azoth-metacontacts
Summary:        LeechCraft Azoth Metacontacts Module
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name}-azoth = %{version}

%description azoth-metacontacts
This package provides a metacontacts support plugin for LeechCraft Azoth.


%package azoth-modnok
Summary:        LeechCraft Azoth LaTeX support Module
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name}-azoth = %{version}

%description azoth-modnok
This package provides a plugin for LeechCraft Azoth which
can render and display LaTeX formulae directly in chat windows.

It does not depend on the underlying protocol, and if the protocol supports
rich text formatting in outgoing messages, it is able to replace the formulas
with corresponding images in outgoing messages as well, so your buddies would
see nice rendered formulas instead of raw LaTeX code, even if their client
does not have a LaTeX formatter.


%package azoth-mucommands
Summary:        LeechCraft Azoth module for conference-oriented commands
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name}-azoth-protocolplugin = %{version}
Suggests:       %{name}-xoox
Recommends:     %{name}-acetamide
Recommends:     %{name}-xoox

%description azoth-mucommands
This package provides some common conference-oriented commands like
/vcard, /time, /last, /subject, /kick, /ban and so on for LeechCraft Azoth.


%package azoth-murm
Summary:        LeechCraft Azoth - VKontakte Module
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name}-azoth = %{version}
Provides:       %{name}-azoth-protocolplugin

%description azoth-murm
This package provides a special protocol subplugin for extensive VKontakte
messaging support for LeechCraft Azoth.


%package azoth-nativeemoticons
Summary:        LeechCraft Azoth Emoticon pack support
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name}-azoth = %{version}

%description azoth-nativeemoticons
This package provides an emoticons plugin for LeechCraft Azoth which
permits to use emoticon packs which are stored in Psi+, Kopete
format or Azoth format.


%package azoth-otroid
Summary:        LeechCraft Azoth Off-the-Record Module
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name}-azoth = %{version}

%description azoth-otroid
This package provides support for Off-the-Record messaging for LeechCraft Azoth.


%package azoth-rosenthal
Summary:        LeechCraft Azoth Spell Checker Module
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name}-azoth = %{version}
Requires:       %{name}-rosenthal = %{version}

%description azoth-rosenthal
This package provides a spell checker plugin for LeechCraft Azoth.

It is based on Hunspell or Myspell dictionaries.


%package azoth-shx
Summary:        LeechCraft Azoth Shell command runner Module
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name}-azoth = %{version}

%description azoth-shx
This package provides a shell command runner plugin for LeechCraft Azoth.


%package azoth-standardstyles
Summary:        LeechCraft Azoth Standard chat styles Module
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name}-azoth = %{version}
Provides:       %{name}-azoth-chatstyler

%description azoth-standardstyles
This package provides a standard styles support plugin for LeechCraft Azoth.

Standard styles are the ones in LeechCraft's own format.


%package azoth-vader
Summary:        LeechCraft Azoth MrIM Module
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name}-azoth = %{version}
Provides:       %{name}-azoth-protocolplugin

%description azoth-vader
This package provides a MRIM protocol plugin for LeechCraft Azoth.

The MRIM protocol is used in the Mail.Ru Agent IM service.

Vader is based on an own implementation of the MRIM protocol, partially based
on available (and outdated) official specs, and is partly reverse-engineered.

The following protocol features are supported:
 * Extended statuses.
 * Attention requests (alarms).
 * Publishing current tune and fetching others' tune.
 * Message delivery receipts.
 * Mailbox notifications.
 * Opening mailbox without login.
 * Authorization management.
 * Grouping contacts.


%package azoth-velvetbird
Summary:        LeechCraft Azoth libpurple Module
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name}-azoth = %{version}
Provides:       %{name}-azoth-protocolplugin

%description azoth-velvetbird
This package provides a plugin for LeechCraft Azoth which
makes the various protocols supported by libpurple available
in Azoth.


%package azoth-xoox
Summary:        LeechCraft Azoth XMPP Module
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name}-azoth = %{version}
Provides:       %{name}-azoth-protocolplugin
Recommends:     %{name}-azoth-mucommands

%description azoth-xoox
This package provides an XMPP protocol plugin for LeechCraft Azoth.

Feature highlights:
 * Media calls support (Jingle).
 * Support for PEP and current user activity, mood, tune and location.
 * Bookmarks with autojoin support.
 * Full support for MUCs.
 * Notifications about chat state participation.
 * Service discovery support.
 * Gateway support, with registration.
 * Support for various file transfer methods.
 * In-band registration of accounts (right from the client).
 * Privacy lists.
 * Encrypted and signed messages and presences.
 * Full CAPTCHA support.
 * Support for ad-hoc commands.
 * Support for exchanging roster items.
 * Search for contacts in Jabber.


%package azoth-xtazy
Summary:        LeechCraft Azoth Module for publishing current user tune
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name}-azoth = %{version}
Requires:       %{name}-xtazy = %{version}

%description azoth-xtazy
This package provides an Azoth plugin which allows to publish
the current user tune.


%ifarch %ix86 x86_64 %arm ppc64le
%package bittorrent
Summary:        LeechCraft BitTorrent client Module
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Recommends:     %{name}-summaryrepresentation = %{version}

%description bittorrent
This package provides a BitTorrent client for Leechcraft.

Features:
 * Support for DHT and magnet links
 * Sequential download mode where torrent is download sequentially.
 * Torrents queue, limiting number of seeding/leeching torrents.
 * Ability to rename files and directories in the torrent.
 * Selective download: possibility to select specific files from torrent.
 * Continue downloads left by any other client.
 * Support for sparse files.
 * Tags for torrents.
 * Global and per-torrent speed limits.
 * Connection number limits.
 * Fast resume support to avoid long startup times.
 * IP filter to block/unblock unwanted peers.
 * Support for extension protocol
%endif

%package blasq
Summary:        LeechCraft Image storage Module
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Requires:       %{name}-blasq-subplugin = %{version}
Obsoletes:      %{name}-blasq-spegnersi

%description blasq
This package provides a modular image storage plugin for LeechCraft
which supports different cloud image stores like Picasa or Flickr.


%package blasq-deathnote
Summary:        LeechCraft Blasq LiveJournal/FotoBilder client Module
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name}-blasq = %{version}
Provides:       %{name}-blasq-subplugin = %{version}

%description blasq-deathnote
This package provides a LiveJournal FotoBilder image storage client subplugin
for LeechCraft Blasq.


%package blasq-rappor
Summary:        LeechCraft Blasq VKontakte client Module
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name}-blasq = %{version}
Provides:       %{name}-blasq-subplugin = %{version}

%description blasq-rappor
This package provides a VKontakte image storage client subplugin
for LeechCraft Blasq.


%package blasq-vangog
Summary:        LeechCraft Blasq Picasa client Module
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name}-blasq = %{version}
Provides:       %{name}-blasq-subplugin = %{version}

%description blasq-vangog
This package provides a Picasa image storage client subplugin
for LeechCraft Blasq.


%package blogique
Summary:        LeechCraft Blogging client Module
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Requires:       %{name}-blogique-subplugin = %{version}
Recommends:     %{name}-lhtr

%description blogique
This package provides a modular blogging client plugin for LeechCraft
which itself supports different blogging platforms via different submodules.


%package blogique-hestia
Summary:        LeechCraft Blogique "Local blogging" Module
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Requires:       %{name}-blogique = %{version}
Provides:       %{name}-blogique-subplugin = %{version}

%description blogique-hestia
This package provides a local blogging subplugin for LeechCraft Blogique.


%package blogique-metida
Summary:        LeechCraft Blogique LiveJournal Module
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Requires:       %{name}-blogique = %{version}
Recommends:     %{name}-xtazy = %{version}
Provides:       %{name}-blogique-subplugin = %{version}

%description blogique-metida
This package provides a LiveJournal subplugin for LeechCraft Blogique.


%package certmgr
Summary:        LeechCraft SSL certificate Module
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}

%description certmgr
This package provides an SSL certificate manager plugin.


%package cpuload
Summary:        LeechCraft CPU Usage Monitoring Module
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Requires:       %{name}-sb2 = %{version}

%description cpuload
This package provides a quark for monitoring the CPU usage
for LeechCraft SB2. It currently uses /proc/stat.


%package cstp
Summary:        LeechCraft HTTP Module
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Provides:       %{name}-http

%description cstp
This package provides a HTTP implementation plugin for LeechCraft
which will mainly used by many other plugins like Aggregator or
SeekThru.

Features:
 * Support for redirects.
 * Automatic downloads from other plugins.
 * Support for continuing interrupted downloads.


%package dbusmanager
Summary:        LeechCraft D-Bus Module
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}

%description dbusmanager
This package provides a D-Bus implementation plugin for LeechCraft.


%package deadlyrics
Summary:        LeechCraft Lyrics finder Module
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Requires:       %{name}-http = %{version}
Requires:       %{name}-summaryrepresentation = %{version}
Provides:       %{name}-lyricsprovider

%description deadlyrics
This package provides a lyrics finder plugin for LeechCraft.

It is a simple client for searching song lyrics on various sites.
The search interface is available via LeechCraft Summary.


%package devel
Summary:        LeechCraft Development Files
License:        BSL-1.0
Group:          Development/Libraries/Other
Requires:       %{name} = %{version}
Requires:       cmake >= 3.8
Requires:       libQt5Gui-private-headers-devel
Requires:       libleechcraft-util-db%{db_postfix}               = %{version}
Requires:       libleechcraft-util-gui%{gui_postfix}             = %{version}
Requires:       libleechcraft-util-models%{models_postfix}       = %{version}
Requires:       libleechcraft-util-network%{network_postfix}     = %{version}
Requires:       libleechcraft-util-qml%{qml_postfix}             = %{version}
Requires:       libleechcraft-util-shortcuts%{shortcuts_postfix} = %{version}
Requires:       libleechcraft-util-sll%{sll_postfix}             = %{version}
Requires:       libleechcraft-util-svcauth%{svcauth_postfix}     = %{version}
Requires:       libleechcraft-util-sys%{sys_postfix}             = %{version}
Requires:       libleechcraft-util-tags%{tags_postfix}           = %{version}
Requires:       libleechcraft-util-x11%{x11_postfix}             = %{version}
Requires:       libleechcraft-util-xdg%{xdg_postfix}             = %{version}
Requires:       libleechcraft-util-xpc%{xpc_postfix}             = %{version}
Requires:       libleechcraft-util-xsd%{xsd_postfix}             = %{version}
Requires:       libqt5-linguist-devel >= 5.9
Requires:       pkgconfig(Qt5Concurrent) >= 5.9
Requires:       pkgconfig(Qt5DBus) >= 5.9
Requires:       pkgconfig(Qt5OpenGL) >= 5.9
Requires:       pkgconfig(Qt5PrintSupport) >= 5.9
Requires:       pkgconfig(Qt5Script) >= 5.9
Requires:       pkgconfig(Qt5Svg) >= 5.9
Requires:       pkgconfig(Qt5WebKitWidgets) >= 5.9
Requires:       pkgconfig(Qt5X11Extras) >= 5.9
Requires:       pkgconfig(Qt5XmlPatterns) >= 5.9
Recommends:     leechcraft-azoth-doc
Recommends:     leechcraft-doc
Recommends:     leechcraft-monocle-doc

%description devel
This package provides files required for development of
new LeechCraft modules.


%package devmon
Summary:        LeechCraft Device Monitor Module
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Recommends:     %{name}-secman = %{version}

%description devmon
This package provides a devices monitor plugin for LeechCraft.


%package dolozhee
Summary:        LeechCraft Issue reporting Module
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Recommends:     %{name}-secman = %{version}

%description dolozhee
This package provides a Dolozhee plugin for LeechCraft which
allows submitting bug reports and feature requests to the
LeechCraft issue tracker.


%package dumbeep
Summary:        LeechCraft DumBeep Module
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Recommends:     mplayer
Provides:       %{name}-soundnotifications = %{version}

%description dumbeep
This package provides a dumb sound notifier plugin for LeechCraft.

It uses Phonon as a backend, or something like aplay/mplayer.


%package eleeminator
Summary:        LeechCraft terminal plugin
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}

%description eleeminator
This package provides a terminal plugin for Leechcraft.


%package fenet
Summary:        LeechCraft Window Manager Module
License:        BSL-1.0
Group:          Productivity/Networking/Other
Provides:       %{name}-fenet-compton = %{version}
Recommends:     %{name}-cpuload
Recommends:     %{name}-hotsensors
Recommends:     %{name}-kbswitch
Recommends:     %{name}-krigstask
Recommends:     %{name}-laughty
Recommends:     %{name}-launchy
Recommends:     %{name}-lemon
Recommends:     %{name}-liznoo
Recommends:     %{name}-mellonetray
Recommends:     %{name}-ooronee
Recommends:     %{name}-sb2
Recommends:     %{name}-tpi
Recommends:     %{name}-vrooby
Recommends:     compton
Requires:       %{name} = %{version}
Requires:       %{name}-fenet-wm = %{version}

%description fenet
This package provides a WM control plugin for Leechcraft.


%package fenet-awesome
Summary:        Awesome Window Manager integration for LeechCraft
License:        BSL-1.0
Group:          Productivity/Networking/Other
BuildArch:      noarch
Provides:       %{name}-fenet-wm = %{version}
Requires:       %{name}-fenet = %{version}
Requires:       awesome

%description fenet-awesome
This package allows to start Leechcraft as a Desktop Environment with
the Awesome Window Manager.


%package fenet-kwin
Summary:        Kwin integration for LeechCraft
License:        BSL-1.0
Group:          Productivity/Networking/Other
BuildArch:      noarch
Provides:       %{name}-fenet-wm = %{version}
Requires:       %{name}-fenet = %{version}
Requires:       kwin5

%description fenet-kwin
This package allows to start Leechcraft as a Desktop Environment with
the KDE Window Manager.


%package fenet-openbox
Summary:        OpenBox Window Manager integration for LeechCraft
License:        BSL-1.0
Group:          Productivity/Networking/Other
BuildArch:      noarch
Provides:       %{name}-fenet-wm = %{version}
Requires:       %{name}-fenet = %{version}
Requires:       openbox

%description fenet-openbox
This package allows to start Leechcraft as a Desktop Environment with
the Openbox Window Manager.


%package gacts
Summary:        LeechCraft Global actions Module
License:        BSL-1.0 AND (LGPL-2.1-only OR CPL-1.0)
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}

%description gacts
This package provides a global shortcut manager for LeechCraft
with which global hotkeys can be set and used.


%package glance
Summary:        LeechCraft Opened tabs overview Module
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}

%description glance
This package provides a tabs overview plugin for Leechcraft
which shows a grid of overview thumbnails.


%package gmailnotifier
Summary:        LeechCraft GMail notifier Module
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Requires:       %{name}-http = %{version}
Recommends:     %{name}-sb = %{version}

%description gmailnotifier
This package provides a GMail notifications plugin for Leechcraft
which allows to show notifications about new mail in your GMail account.

It has a configurable frequency for updates and the number of last unread
messages shown.


%package historyholder
Summary:        LeechCraft History Module
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}

%description historyholder
This package provides a history keeper plugin for LeechCraft
which stores information about finished downloads and similar events,
and allows to search it by text, wildcard, regular expressions or tags.


%package hotstreams
Summary:        LeechCraft Radio streams Module
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name}-lmp = %{version}

%description hotstreams
This package provides a radio streams provider plugin for LeechCraft.


%package htthare
Summary:        LeechCraft HTTP Server Module
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}

%description htthare
This package provides content from local filesystem over LANs.
(Possibly also WANs, but, by default, only LAN interfaces are listened on).


%package imgaste
Summary:        LeechCraft Image Paster Module
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}

%description imgaste
This module provides a simple image paster plugin from LeechCraft.


%package intermutko
Summary:        LeechCraft HTTP Accept-Language header Module
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}

%description intermutko
This module provides a HTTP Accept-Language header configurator.


%package kbswitch
Summary:        LeechCraft keyboard switcher Module
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Requires:       setxkbmap

%description kbswitch
This module allows changing keyboard layouts from LeechCraft.


%package kinotify
Summary:        LeechCraft Kinetic notifications Module
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Provides:       %{name}-visualnotifications
Recommends:     %{name}-poshuku

%description kinotify
This package contains a fancy notifications plugin for LeechCraft.

It provides fancy kinetic notifications LeechCraft-wide instead of old-style
tray-based ones. It supports notifications with HTML markup, notification
actions (for example, "Open chat" action in a notification about incoming IM
message) and is fully themable.


%package knowhow
Summary:        LeechCraft "Tip of the day" Module
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}

%description knowhow
This package provides a tips plugin for LeechCraft which
displays a "tip of the day" window after launching LeechCraft.


%package krigstask
Summary:        LeechCraft Applications Switcher Module
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Requires:       %{name}-sb2 = %{version}

%description krigstask
This package provides an applications switcher quark for LeechCraft SB2.


%package lackman
Summary:        LeechCraft Package manager Module
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Requires:       %{name}-http = %{version}
Requires:       xz
Recommends:     %{name}-poshuku = %{version}

%description lackman
This package provides a package manager plugin for Leechcraft.

It allows to install script plugins, iconsets, translations, additional data
and other similar packages.

It also supports dependencies between packages as well as versioning and
automatic updates of the packages.

Features:
 * Allows installation of script plugins, icons and various other data.
 * Supports versioning and automatic updates of packages.
 * Supports dependencies between packages.
 * Operates in user's home directory.


%package lastfmscrobble
Summary:        LeechCraft Last.FM Scrobble Module
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Requires:       %{name}-lmp = %{version}
Provides:       %{name}-scrobbler

%description lastfmscrobble
This package contains the LastFMScrobble plugin for LeechCraft
which supports the Last.FM service. For example, it scrobbles tracks
from other players, requests similar artists (on demand by other players as
well), supports fetching album art, etc.

Features:
 * Scrobbling listened tracks from other players like LMP to Last.FM.
 * "Loving" listened tracks.
 * Support for requesting artists that are similar to a given artist.
 * Automatic fetching of album art.
 * Support for Last.FM radio.
 * Fetching personalized recommendations.
 * Fetching recent releases of artists that are in the user's collection.
 * Fetching artists biography.
 * Configurable language of the fetched information.


%package laughty
Summary:        LeechCraft Notification Server Module
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Conflicts:      %{name}-sysnotify

%description laughty
This package provides a desktop notifications server plugin for Leechcraft.


%package launchy
Summary:        LeechCraft Launcher Module
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Requires:       %{name}-sb = %{version}

%description launchy
This package provides a third-party application launcher plugin for Leechcraft.


%package lemon
Summary:        LeechCraft Network Monitor Module
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Requires:       %{name}-sb = %{version}

%description lemon
This package provides another Network Monitor plugin for Leechcraft.


%package lhtr
Summary:        LeechCraft HTML WYSIWYG editor Module
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Recommends:     %{name}-poshuku

%description lhtr
This package provides a HTML WYSIWYG editor plugin for Leechcraft,
usable with mail and blog modules.


%package liznoo
Summary:        LeechCraft Power management module
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Requires:       upower
Recommends:     %{name}-sb = %{version}

%description liznoo
This package provides a power manager plugin for Leechcraft
which makes use of upower.

Features:
 * Displays battery status in LeechCraft tray.
 * Displays battery charge and power consumption history.
 * Notifies other plugins about sleep and resume events. This way, plugins
   like Azoth can disconnect from servers gracefully on hibernation and
   reconnect properly on startup.
 * Allows the user to sleep/hibernate the system.
 * Notifies the user when device starts discharging or charging.
 * Notifies the user on low capacity.


%package lmp
Summary:        LeechCraft Media player Module
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Recommends:     %{name}-lyricsprovider
Recommends:     %{name}-gacts = %{version}
Recommends:     %{name}-scrobbler
Suggests:       %{name}-lastfmscrobble
Recommends:     %{name}-musiczombie = %{version}
Recommends:     ffmpeg
Requires:       gstreamer-plugins-base >= 1.0
Requires:       gstreamer-plugins-good >= 1.0
Requires:       libqt5-qtgraphicaleffects >= 5.9
Requires:       libqt5-qtquickcontrols >= 5.9
Recommends:     gstreamer-plugins-bad
Recommends:     gstreamer-plugins-libav
Provides:       %{name}-audioplayer
Provides:       %{name}-soundnotifications = %{version}

%description lmp
This package provides an audio player plugin for LeechCraft.
It uses Gstreamer as a backend, thus supporting major codecs.

Features:
 * Streaming media over Internet.
 * Play queue.
 * Support for automatic podcast playing (with a plugin like Aggregator).


%package lmp-brainslugz
Summary:        LeechCraft Collection Checker Module
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name}-scrobbler = %{version}
Suggests:       %{name}-lastfmscrobble = %{version}
Requires:       %{name}-lmp = %{version}
Requires:       %{name}-musiczombie = %{version}

%description lmp-brainslugz
This package provides a collection checker plugin for LeechCraft
to check the completeness of collections.


%package lmp-dumbsync
Summary:        LeechCraft Media synchronization Module
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name}-lmp = %{version}
Recommends:     %{name}-hotstreams = %{version}
Recommends:     %{name}-vrooby = %{version}

%description lmp-dumbsync
This package provides an audio syncing plugin for LeechCraft
to synchronize with Flash-like media players.


%package lmp-fradj
Summary:        LeechCraft Equalizer Module
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name}-lmp = %{version}

%description lmp-fradj
This package provides a 10-band equalizer.


%package lmp-graffiti
Summary:        LeechCraft Tag Manipulating Module
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name}-lmp = %{version}

%description lmp-graffiti
This package provides a tag editor plugin for LeechCraft
with with audio file tags can be manipulated.


%package lmp-httstream
Summary:        LeechCraft Music Streamer Module
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name}-lmp = %{version}

%description lmp-httstream
This package provides a streamer plugin for LeechCraft player
to stream music from LMP via HTTP.


%package lmp-mp3tunes
Summary:        LeechCraft mp3tunes.com Module
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name}-lmp = %{version}

%description lmp-mp3tunes
This package provides a LeechCraft plugin to
synchronizing with, and use the mp3tunes.com service.

Features:
 * Using many accounts.
 * Getting playlists.


%package lmp-mtpsync
Summary:        LeechCraft MtpSync Module
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name}-devmon = %{version}
Requires:       %{name}-lmp = %{version}

%description lmp-mtpsync
This package allows to synchronize with MTP devices via LeechCraft.


%if 0%{?sle_version} > 150300 || 0%{?suse_version} > 1500
%ifarch %ix86 x86_64 ppc64 ppc64le
%package lmp-potorchu
Summary:        LeechCraft Visualization Effects Module
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name}-lmp = %{version}

%description lmp-potorchu
This package provides visualization effects for the LeechCraft audio player.
%endif
%endif

%package lmp-ppl
Summary:        LeechCraft Portable Player Logging Module
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name}-lmp = %{version}

%description lmp-ppl
This package provides Portable Player Logging support for the LeechCraft audio player.


%package mellonetray
Summary:        LeechCraft Tray Area Module
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Requires:       %{name}-sb2 = %{version}

%description mellonetray
This package provides a tray area quark for third-party apps
for LeechCraft SB2.


%if 0%{?suse_version} > 1325 || 0%{?sle_version} >= 120300
%package monocle
Summary:        LeechCraft Document viewer Module
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Requires:       %{name}-monocle-subplugin

%description monocle
This package provides a modular document viewer plugin for LeechCraft
which supports different formats via backends.


%package monocle-fxb
Summary:        FictionBook support for LeechCraft Monocle
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Requires:       %{name}-monocle = %{version}
Provides:       %{name}-monocle-subplugin

%description monocle-fxb
This package contains the FictionBook subplugin for LeechCraft Monocle.


%package monocle-dik
Summary:        MOBI support for LeechCraft Monocle
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Requires:       %{name}-monocle = %{version}
Provides:       %{name}-monocle-subplugin

%description monocle-dik
This package contains the MOBI subplugin for LeechCraft Monocle.


%package monocle-pdf
Summary:        PDF support for LeechCraft Monocle
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Requires:       %{name}-monocle = %{version}
Provides:       %{name}-monocle-subplugin

%description monocle-pdf
This package contains the PDF subplugin for LeechCraft Monocle.
PDF support is provided via the libpoppler backend.


%package monocle-postrus
Summary:        PostScript support for LeechCraft Monocle
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name}-monocle-pdf = %{version}
Requires:       ghostscript
Provides:       %{name}-monocle-subplugin

%description monocle-postrus
This package contains the PostRus subplugin for LeechCraft Monocle
which supports PostScript document support via the ghostscript utilities.


%package monocle-seen
Summary:        Djvu support for LeechCraft Monocle
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Requires:       %{name}-monocle = %{version}
Provides:       %{name}-monocle-subplugin

%description monocle-seen
This package contains a LeechCraft Monocle subplugin for djvu
document support via the djvulibre backend.
%endif

%package musiczombie
Summary:        LeechCraft Azoth MusicBrainz.org client Module
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Requires:       %{name}-lmp = %{version}

%description musiczombie
This package provides a MusicBrainz.org client plugin for LeechCraft.


%package namauth
Summary:        LeechCraft HTTP authentication Module
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}

%description namauth
This package provides providing standard HTTP authentication facilities for LeechCraft.


%package netstoremanager
Summary:        LeechCraft Network file storages Module
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Requires:       %{name}-netstoremanager-subplugin

%description netstoremanager
This package provides a network storage plugin for Leechcraft.

It allows to manage network storages such as Google Drive.
Different storages can be added to it without modifying the plugin itself.

Features:
 * Upload files from LeechCraft.
 * Maintain the list of uploaded files.
 * Delete the uploaded files (if supported by service).
 * Support for prolongating uploaded files (if supported by service).


%package netstoremanager-googledrive
Summary:        LeechCraft Google Drive storage Module
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name}-netstoremanager = %{version}
Provides:       %{name}-netstoremanager-subplugin

%description netstoremanager-googledrive
This package provides a Google Drive subplugin for Leechcraft NetStoreManager.


%package networkmonitor
Summary:        LeechCraft Network Monitor Module
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}

%description networkmonitor
This package provides a network monitor plugin for LeechCraft.

It allows to watch for HTTP requests and allows to inspect them and search
through the list.


%package newlife
Summary:        LeechCraft Importer Module
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}

%description newlife
This package provides a settings importer plugin for LeechCraft
which can import settings, preferences, etc. from various applications.

Currently it supports
 * Kopete: chat history.
 * Psi+: account settings, chat history.
 * Vacuum IM: account settings, chat history.
 * Akregator: feeds list, individual settings for each feed, like
update interval and custom storage parameters, Akregator's settings.
 * Firefox: history, bookmarks, RSS feeds (aka Live bookmarks).
 * Liferea: feeds list.


%package ooronee
Summary:        LeechCraft Text and Images Handler Module
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name}-sb2 = %{version}
Recommends:     %{name}-blasq
Recommends:     %{name}-imgaste
Recommends:     %{name}-pogooglue
Recommends:     %{name}-seekthru

%description ooronee
This package provides a Leechcraft quark handling text and images
dropped on it.

The dropped data is then sent to a data filter chosen by the user.
See more at http://leechcraft.org/concepts-data-filters .


%package otlozhu
Summary:        LeechCraft ToDo manager Module
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}

%description otlozhu
This package provides a GTD-inspired ToDo manager plugin for LeechCraft.


%package pintab
Summary:        LeechCraft Pinned tabs Module
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}

%description pintab
This package provides a pinning tab module for LeechCraft with which
it is possible to pin important tabs so that they occupy less space.


%package pogooglue
Summary:        LeechCraft Poshuku Google Search plugin
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Recommends:     %{name}-poshuku = %{version}

%description pogooglue
This package provides a LeechCraft plugin to do a Google search
with some selected text.


%package poshuku
Summary:        LeechCraft Web Browser Module
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Requires:       %{name}-poshuku-backend = %{version}
Provides:       %{name}-webbrowser
Recommends:     %{name}-imgaste = %{version}
Recommends:     %{name}-intermutko = %{version}

%description poshuku
This package provides a WebKit-based web browser plugin for LeechCraft.
Poshuku is extensible with plugins.

Currently it features:
 * integration with other plugins;
 * autodiscovery;
 * tagging bookmarks;
 * support for SQLite or PostgreSQL storage.


%package poshuku-autosearch
Summary:        LeechCraft Poshuku Autosearch Module
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name}-poshuku = %{version}

%description poshuku-autosearch
This package provides an autosearch plugin for LeechCraft Poshuku.


%package poshuku-cleanweb
Summary:        LeechCraft Poshuku Ad Filter Module
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name}-poshuku = %{version}

%description poshuku-cleanweb
This package provides an advertisement filter for LeechCraft Poshuku.

Features:
 * Support for Firefox AdBlock+ block lists.
 * Support for detection and subscription to such lists.
 * Automatic updates of block lists.
 * User filters: blocking arbitrary images.
 * Support for replacing Adobe Flash objects with a "Load flash" button.
 * Whitelists for the Flash blocker.


%package poshuku-dcac
Summary:        LeechCraft Poshuku DC/AC Module
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name}-poshuku = %{version}

%description poshuku-dcac
This package provides the DC/AC plugin for LeechCraft Poshuku
which inverts colors on web pages.


%package poshuku-fatape
Summary:        LeechCraft Poshuku Greasemonkey Module
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name}-poshuku = %{version}

%description poshuku-fatape
This package provides a Greasemonkey script plugin for LeechCraft Poshuku.
These scripts could be used for
adding new features to web pages (for example, embedding price comparisons
within shopping sites), fixing rendering bugs, combining data from multiple
webpages, and numerous other purposes.

This plugin supports almost all of the GreaseMonkey API and is compatible
with most userscripts present "in the wild".

FatApe usage is documented on the corresponding user guide page.


%package poshuku-filescheme
Summary:        LeechCraft Poshuku file: scheme module
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name}-poshuku = %{version}

%description poshuku-filescheme
This package provides file: scheme support for LeechCraft Poshuku,
allowing to navigate local resources.
FileScheme also supports "downloading" files from there.


%package poshuku-foc
Summary:        LeechCraft Poshuku Flash-on-Click module
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name}-poshuku = %{version}

%description poshuku-foc
This package provides Flash-on-Click support for LeechCraft Poshuku browser.


%package poshuku-fua
Summary:        LeechCraft Poshuku module to change the user agent
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name}-poshuku = %{version}

%description poshuku-fua
This package provides a fake user agent plugin for LeechCraft Poshuku
for setting different User-Agent strings for different URLs.

Features:
 * URLs are defined either by their substring or by regular expression.
 * Several popular predefined user agents are present.
 * Support for custom user-defined strings.
 * Support for automatic insertion of current platform, language, WebKit's
version etc. into the User-Agent string in arbitrary places.


%package poshuku-keywords
Summary:        LeechCraft Poshuku URL Keyword Support Module
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name}-poshuku = %{version}

%description poshuku-keywords
This package provides an LeechCraft Poshuku module for URL keywords.


%package poshuku-onlinebookmarks
Summary:        LeechCraft Poshuku Online Bookmarks Module
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name}-poshuku = %{version}
Requires:       %{name}-securestorage

%description poshuku-onlinebookmarks
This package provides an online bookmarks plugin for LeechCraft Poshuku
for synchronization of bookmarks with services like Read It Later
or Del.icio.us.


%package poshuku-onlinebookmarks-delicious
Summary:        LeechCraft Poshuku Onlinebookmarks Delicious Module
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name}-poshuku-onlinebookmarks = %{version}

%description poshuku-onlinebookmarks-delicious
This package contains a plugin for LeechCraft Poshuku Online Bookmarks
to support the Del.icio.us service.


%package poshuku-onlinebookmarks-readitlater
Summary:        LeechCraft Poshuku Onlinebookmarks ReadItLater Module
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name}-poshuku-onlinebookmarks = %{version}

%description poshuku-onlinebookmarks-readitlater
This package contains a plugin for LeechCraft Poshuku Online Bookmarks
to support the Read it Later service.


%package poshuku-qrd
Summary:        LeechCraft Poshuku QR coDe Module
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name}-poshuku = %{version}

%description poshuku-qrd
This package provides a QR coDe support plugin for LeechCraft Poshuku
which can represent the URL of a web page as a QR code.


%package poshuku-speeddial
Summary:        LeechCraft Poshuku Speed Dial Module
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name}-poshuku = %{version}

%description poshuku-speeddial
This package provides the Speed Dial support plugin for LeechCraft Poshuku.


%package poshuku-webkitview
Summary:        LeechCraft Poshuku WebKit-based backend Module
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name}-poshuku = %{version}
Provides:       %{name}-poshuku-backend = %{version}

%description poshuku-webkitview
This package provides WebKit-based backend for LeechCraft Poshuku browser.


%package rosenthal
Summary:        LeechCraft Spell Checker Module
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}

%description rosenthal
This package provides a spell checker plugin for LeechCraft.

It is based on Hunspell or Myspell dictionaries.


%package sb2
Summary:        LeechCraft SideBar2 Module
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Provides:       %{name}-sb = %{version}
Requires:       libqt5-qtquickcontrols >= 5.9

%description sb2
This package provides another side bar plugin for Leechcraft.

It is a sidebar with quick launch, tabs and tray areas.


%package scroblibre
Summary:        LeechCraft Submissions Protocol Scrobble Module
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name}-lmp = %{version}
Provides:       %{name}-scrobbler

%description scroblibre
This package contains a Scroblibre plugin for LeechCraft.

It is an implementation of the submissions protocol 1.2 with
support ( http://www.audioscrobbler.net/development/protocol )
for sites other than last.fm (libre.fm for now). It can
potentially handle arbitrary scrobbling URLs implementing the
submissions protocol, but it is not exposed in the GUI (yet).
 
Scroblibre is a supplement for the LastFMScrobble module, and the
latter is still the recommended one because of all the social
features it offers which Scroblibre lacks.


%package secman
Summary:        LeechCraft Security manager Module
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Requires:       %{name}-secman-simplestorage = %{version}
Provides:       %{name}-securestorage

%description secman
This package provides a security manager plugin for LeechCraft.

It is the base module for secure storage.
Particular storage backends are implemented by subplugins.


%package secman-simplestorage
Summary:        LeechCraft Simple storage Module
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name}-secman = %{version}

%description secman-simplestorage
This package provides a simple unencrypted storage backend for LeechCraft SecMan.


%package seekthru
Summary:        LeechCraft OpenSearch Module
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Requires:       %{name}-http = %{version}
Requires:       %{name}-summaryrepresentation = %{version}

%description seekthru
This package contains an OpenSearch plugin for LeechCraft
which provides a search client for OpenSearch-enabled web sites and engines.

Features:
 * Support for autodiscovery of OpenSearch-capable web sites.
 * Tagging of search engines.
 * Support for queries to several search engines at once.
 * Support search results in RSS/Atom format and subscribe to them
with a suitable plugin like Aggregator.
 * Show results in HTML format with a suitable plugin like Poshuku.


%package summary
Summary:        LeechCraft Summary info Module
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Provides:       %{name}-summaryrepresentation

%description summary
This package provides a summary plugin for LeechCraft which shows a
quick overview of LeechCraft's state. It shows current tasks like
leeching or seeding torrents and downloading files with
context-dependent actions and views. It also can collect status
information from other plugins like unread channels.

Summary also allows to perform searches via the installed plugins
like SeekThru or HistoryHolder.

Features:
 * List of current tasks and events with context-dependent actions
and views for selected items.
 * Support for gathering status information from other plugins.
 * Category-based search query support via other plugins.


%package sysnotify
Summary:        LeechCraft System notification Module
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Provides:       %{name}-visualnotifications
Conflicts:      %{name}-laughty

%description sysnotify
This package contains a system notification plugin for LeechCraft.
Notifications are provided implementations supporting FreeDesktop's
notification standard, like KDE 4.4 (or higher), Gnome, XFCE and others.


%package tabsessionmanager
Summary:        LeechCraft Tab Session Manager Module
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}

%description tabsessionmanager
This package provides a Tab Session Manager plugin for Leechcraft
which allows to automatically restore the last session and allows
to create named sessions.


%package tabslist
Summary:        LeechCraft TabsList Module
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}

%description tabslist
This package provides a tabs list plugin for Leechcraft
which can show the list of currently opened tabs
and allows to navigate between them.


%package textogroose
Summary:        LeechCraft Script-Based Lyrics Module
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name}-http = %{version}
Requires:       %{name}-summaryrepresentation = %{version}
Provides:       %{name}-lyricsprovider

%description textogroose
This package provides a lyrics finder plugin for LeechCraft.

Textogroose is a kind of supplement to DeadLyrics for sites
too complex to be described by DeadLyrics rules.


%package touchstreams
Summary:        LeechCraft VK.com Streaming Module
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Requires:       %{name}-lmp = %{version}
Requires:       %{name}-musiczombie = %{version}

%description touchstreams
This package provides a VK.com music streaming plugin for Leechcraft.


%package tpi
Summary:        LeechCraft Task Progress Indicator Module
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Requires:       %{name}-sb2 = %{version}

%description tpi
This package provides a Task Progress Indicator quark plugin for Leechcraft.


%package vrooby
Summary:        LeechCraft Removable storage devices Manager
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}
Requires:       %{name}-sb = %{version}
Recommends:     udisks2

%description vrooby
This package provides a Vrooby plugin for LeechCraft
which allows to watch removable storage devices via D-Bus and udisks.


%package xproxy
Summary:        LeechCraft Proxy manager Module
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}

%description xproxy
This package provides an advanced proxy manager for LeechCraft
with which you can configure and use proxy servers.


%package xtazy
Summary:        LeechCraft Current user tune Module
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}

%description xtazy
This package provides a tune wrapper plugin for LeechCraft
with which you can get the current user tune via mpris protocol.


%package zalil
Summary:        LeechCraft File Uploader Module
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}

%description zalil
This package provides a file uploader plugin for LeechCraft
with which files can be uploaded to accountless filebin services.


%package -n libleechcraft-util-db%{db_postfix}
Summary:        Database utility library for LeechCraft
License:        BSL-1.0
Group:          Productivity/Networking/Other

%description -n libleechcraft-util-db%{db_postfix}
A library providing some commonly used database-related
classes and functions.


%package -n libleechcraft-util-gui%{gui_postfix}
Summary:        GUI utility library for LeechCraft
License:        BSL-1.0
Group:          Productivity/Networking/Other

%description -n libleechcraft-util-gui%{gui_postfix}
A library providing some commonly used GUI-related
widgets, classes and functions.


%package -n libleechcraft-util-models%{models_postfix}
Summary:        MVC utility library for LeechCraft
License:        BSL-1.0
Group:          Productivity/Networking/Other

%description -n libleechcraft-util-models%{models_postfix}
A library providing some commonly used models (as in MVC),
as well as model-related classes and functions.


%package -n libleechcraft-util-network%{network_postfix}
Summary:        Network utility library for LeechCraft
License:        BSL-1.0
Group:          Productivity/Networking/Other

%description -n libleechcraft-util-network%{network_postfix}
A library providing some commonly used
network classes and functions.


%package -n libleechcraft-util-qml%{qml_postfix}
Summary:        QML utility library for LeechCraft
License:        BSL-1.0
Group:          Productivity/Networking/Other
Requires:       libQtQuick5 >= 5.9

%description -n libleechcraft-util-qml%{qml_postfix}
A library providing some commonly used QML items as well as
QML-related classes and functions.


%package -n libleechcraft-util-shortcuts%{shortcuts_postfix}
Summary:        Shortcut utility library for LeechCraft
License:        BSL-1.0
Group:          Productivity/Networking/Other

%description -n libleechcraft-util-shortcuts%{shortcuts_postfix}
A library easing shortcut usage in LeechCraft, particularly the
configurable shortcuts subsystem.


%package -n libleechcraft-util-sll%{sll_postfix}
Summary:        Standard LeechCraft Library
License:        BSL-1.0
Group:          Productivity/Networking/Other

%description -n libleechcraft-util-sll%{sll_postfix}
A library providing some classes and algorithms, not directly
related to any other library.


%package -n libleechcraft-util-svcauth%{svcauth_postfix}
Summary:        Authenticators library for LeechCraft
License:        BSL-1.0
Group:          Productivity/Networking/Other

%description -n libleechcraft-util-svcauth%{svcauth_postfix}
A library providing authenticators for various services like VKontakte.


%package -n libleechcraft-util-sys%{sys_postfix}
Summary:        System utility library for LeechCraft
License:        BSL-1.0
Group:          Productivity/Networking/Other

%description -n libleechcraft-util-sys%{sys_postfix}
A library providing some commonly used system-related
classes and functions, like OS version parser, paths utilities or MIME
detector.


%package -n libleechcraft-util-tags%{tags_postfix}
Summary:        Tag utility library for LeechCraft
License:        BSL-1.0
Group:          Productivity/Networking/Other

%description -n libleechcraft-util-tags%{tags_postfix}
A library providing some classes and functions commonly used
with the LeechCraft tags subsystem.


%package -n libleechcraft-util-threads%{threads_postfix}
Summary:        Thread utility library for LeechCraft
License:        BSL-1.0
Group:          Productivity/Networking/Other

%description -n libleechcraft-util-threads%{threads_postfix}
A library providing some classes and functions commonly used
with the LeechCraft threads subsystem.


%package -n libleechcraft-util-x11%{x11_postfix}
Summary:        X11 utility library for LeechCraft
License:        BSL-1.0
Group:          Productivity/Networking/Other

%description -n libleechcraft-util-x11%{x11_postfix}
A library providing X11 wrappers for LeechCraft.


%package -n libleechcraft-util-xdg%{xdg_postfix}
Summary:        XDG utility library for LeechCraft
License:        BSL-1.0
Group:          Productivity/Networking/Other

%description -n libleechcraft-util-xdg%{xdg_postfix}
A library providing XDG parsers and other support methods and classes
for LeechCraft.


%package -n libleechcraft-util-xpc%{xpc_postfix}
Summary:        Cross-plugin communication utility library for LeechCraft
License:        BSL-1.0
Group:          Productivity/Networking/Other

%description -n libleechcraft-util-xpc%{xpc_postfix}
A library providing some commonly used primitives for
communications between different plugins in LeechCraft.


%package -n libleechcraft-util-xsd%{xsd_postfix}
Summary:        XSD utility library for LeechCraft
License:        BSL-1.0
Group:          Productivity/Networking/Other

%description -n libleechcraft-util-xsd%{xsd_postfix}
A library providing some classes to be used with the
XmlSettingsDialog LeechCraft subsystem.


%prep
%setup -q -n leechcraft-%{LEECHCRAFT_VERSION}
%if 0%{?sle_version} <= 150300 && 0%{?suse_version} < 1550
%patch0 -p1
%patch1 -p1
%endif
%if 0%{?suse_version} > 1500
%patch2 -p1
%endif

#removing non-free icons
rm -rf src/plugins/azoth/share/azoth/iconsets/clients/default

#removing hidden files
find src/plugins/azoth/plugins/adiumstyles/share/azoth/styles/adium/ -name ".?*" -delete

#setup permissions correctly to avoid false duplicates reported by rpmlint (bnc#784670)
find src -name '*.png' -or -name '*.css' -or -name '*.gif' -exec chmod 0644 {} +

%build
mkdir build && cd build

# bypass bug 927268 for PowerPC if clang is used above in place of gcc
tmpflags="%{optflags}"
%ifarch ppc64 ppc64le
# tmpflags=${tmpflags/-fstack-protector}
%endif

# NOTE that %%cmake macro breaks compiler configuring.
cmake ../src \
        -Wno-dev \
        -DGPTOOLS_MEM=True \
%if "%{_lib}" == "lib64"
        -DLIB_SUFFIX=64 \
%endif
        -DCMAKE_CXX_FLAGS="${tmpflags} -Doverride= $(pkg-config --cflags gstreamer-1.0)" \
        -DCMAKE_INSTALL_PREFIX=%{_prefix} \
        -DCMAKE_BUILD_TYPE=RelWithDebInfo \
%if 0%{?sle_version} <= 150300 && 0%{?suse_version} < 1550
        -DCMAKE_C_COMPILER=/usr/bin/gcc-8 \
        -DCMAKE_CXX_COMPILER=/usr/bin/g++-8 \
%endif
        -DSTRICT_LICENSING=True \
        -DWITH_DBUS_LOADERS=True \
        -DWITH_PCRE=True \
        -DWITH_QWT=True \
        -DENABLE_UTIL_TESTS=True \
        -DENABLE_ADVANCEDNOTIFICATIONS=True \
        -DENABLE_AGGREGATOR=True \
%if 0%{?suse_version} > 1325
                -DENABLE_AGGREGATOR_WEBACCESS=True \
%else
                -DENABLE_AGGREGATOR_WEBACCESS=False \
%endif
        -DENABLE_AUSCRIE=True \
        -DENABLE_AZOTH=True \
                -DENABLE_AZOTH_ABBREV=True \
                -DENABLE_AZOTH_ACETAMIDE=True \
                -DENABLE_AZOTH_ASTRALITY=False \
                -DENABLE_AZOTH_AUTOPASTE=True \
                -DENABLE_AZOTH_HERBICIDE=True \
                -DENABLE_AZOTH_MUCOMMANDS=True \
                -DENABLE_AZOTH_MUCOMMANDS_TESTS=True \
                -DENABLE_AZOTH_MURM=True \
                -DENABLE_AZOTH_OTROID=True \
                -DENABLE_AZOTH_SARIN=False \
                -DENABLE_AZOTH_SHX=True \
                -DENABLE_AZOTH_TRACOLOR=False \
                -DENABLE_AZOTH_VELVETBIRD=True \
                -DENABLE_AZOTH_WOODPECKER=False \
                -DENABLE_AZOTH_ZHEET=False \
                -DENABLE_CRYPT=True \
                -DENABLE_MEDIACALLS=False \
        -DENABLE_BLACKDASH=False \
        -DENABLE_BLASQ=True \
                -DENABLE_BLASQ_SPEGNERSI=False \
                -DENABLE_BLASQ_VANGOG=True \
        -DENABLE_BLOGIQUE=True \
        -DENABLE_CERTMGR=True \
        -DENABLE_CHOROID=False \
        -DENABLE_CPULOAD=True \
        -DENABLE_DEVMON=True \
        -DENABLE_DLNIWE=False \
        -DENABLE_DOLOZHEE=True \
        -DENABLE_DUMBEEP=True \
        -DENABLE_ELEEMINATOR=True \
        -DENABLE_FENET=True \
        -DENABLE_FONTIAC=False \
        -DENABLE_GACTS=True \
        -DENABLE_GLANCE=True \
        -DENABLE_GMAILNOTIFIER=True \
        -DENABLE_HARBINGER=False \
        -DENABLE_HOTSENSORS=False \
        -DENABLE_HOTSTREAMS=True \
        -DENABLE_HTTHARE=True \
        -DENABLE_IMGASTE=True \
        -DENABLE_INTERMUTKO=True \
        -DENABLE_KBSWITCH=True \
        -DENABLE_KNOWHOW=True \
        -DENABLE_KRIGSTASK=True \
        -DENABLE_LACKMAN=True \
                -DTESTS_LACKMAN=False \
        -DENABLE_LADS=False \
        -DENABLE_LASTFMSCROBBLE=True \
        -DENABLE_LAUGHTY=True \
        -DENABLE_LAUNCHY=True \
        -DENABLE_LEMON=True \
        -DENABLE_LHTR=True \
                -DWITH_LHTR_HTML=True \
%if 0%{?suse_version} > 1325
                -DUSE_LIBTIDY_HTML5=True \
%else
                -DUSE_LIBTIDY_HTML5=False \
%endif
        -DENABLE_LIZNOO=True \
        -DENABLE_LMP=True \
                -DENABLE_LMP_BRAINSLUGZ=True \
                -DENABLE_LMP_FRADJ=True \
                -DENABLE_LMP_GRAFFITI=True \
                -DENABLE_LMP_HTTSTREAM=True \
                -DENABLE_LMP_LIBGUESS=True \
                -DENABLE_LMP_MPRIS=True \
                -DENABLE_LMP_MTPSYNC=True \
%if 0%{?sle_version} > 150300 || 0%{?suse_version} > 1500
%ifarch %ix86 x86_64 ppc64 ppc64le
                -DENABLE_LMP_POTORCHU=True \
%else
                -DENABLE_LMP_POTORCHU=False \
%endif
%else
                -DENABLE_LMP_POTORCHU=False \
%endif
                -DENABLE_LMP_PPL=True \
                -DENABLE_LMP_PPL_TESTS=True \
        -DENABLE_MELLONETRAY=True \
%if 0%{?suse_version} > 1325 || 0%{?sle_version} >= 120300
        -DENABLE_MONOCLE=True \
                -DENABLE_MONOCLE_MU=False \
                -DENABLE_MONOCLE_PDF=True \
                -DENABLE_MONOCLE_POSTRUS=True \
%else
        -DENABLE_MONOCLE=False \
%endif
        -DENABLE_MUSICZOMBIE=True \
%if %{with ffmpeg}
                -DWITH_MUSICZOMBIE_CHROMAPRINT=True \
%else
                -DWITH_MUSICZOMBIE_CHROMAPRINT=False \
%endif
        -DENABLE_NACHEKU=False \
        -DENABLE_NAMAUTH=True \
        -DENABLE_NETSTOREMANAGER=True \
                -DENABLE_NETSTOREMANAGER_DROPBOX=False \
                -DENABLE_NETSTOREMANAGER_GOOGLEDRIVE=True \
        -DENABLE_NEWLIFE=True \
        -DENABLE_OORONEE=True \
        -DENABLE_OTLOZHU=True \
                -DENABLE_OTLOZHU_SYNC=False \
        -DENABLE_PINTAB=True \
        -DENABLE_POGOOGLUE=True \
        -DENABLE_POLEEMERY=False \
        -DENABLE_POPISHU=False \
        -DENABLE_POSHUKU=True \
                -DENABLE_IDN=True \
                -DENABLE_POSHUKU_AUTOSEARCH=True \
                -DENABLE_POSHUKU_DCAC=True \
%ifarch %ix86 x86_64
                -DENABLE_POSHUKU_DCAC_TESTS=True \
%else
                -DENABLE_POSHUKU_DCAC_TESTS=False \
%endif
                -DENABLE_POSHUKU_FOC=True \
                -DENABLE_POSHUKU_QRD=True \
                -DENABLE_POSHUKU_SPEEDDIAL=True \
        -DENABLE_QROSP=False \
        -DENABLE_SB2=True \
        -DENABLE_SCROBLIBRE=True \
        -DENABLE_SECMAN=True \
                -DTESTS_SECMAN=True \
        -DENABLE_SHELLOPEN=False \
        -DENABLE_SNAILS=False \
        -DENABLE_SYNCER=False \
        -DENABLE_TABSESSMANAGER=True \
        -DENABLE_TABSLIST=True \
        -DENABLE_TEXTOGROOSE=True \
%ifarch %ix86 x86_64 %arm ppc64le
        -DENABLE_TORRENT=True \
                 -DENABLE_BITTORRENT_GEOIP=True \
%else
        -DENABLE_TORRENT=False \
%endif
        -DENABLE_TOUCHSTREAMS=True \
        -DENABLE_TPI=True \
        -DENABLE_TWIFEE=False \
        -DENABLE_VTYULC=False \
        -DENABLE_VROOBY=True \
        -DENABLE_WKPLUGINS=False \
        -DENABLE_XPROXY=True \
        -DENABLE_ZALIL=True \
        -DLEECHCRAFT_VERSION="%{LEECHCRAFT_VERSION}"

make -k %{?_smp_mflags} VERBOSE=1

%install
%cmake_install

cp %{SOURCE8} %{SOURCE9} %{buildroot}%{_mandir}/man1

%fdupes -s %{buildroot}%{_datadir}/%{name}/translations
%fdupes -s %{buildroot}%{_datadir}/%{name}/azoth
%fdupes -s %{buildroot}%{_datadir}/%{name}/global_icons/flags
%fdupes -s %{buildroot}%{_datadir}/%{name}/themes

%check
cd build
ctest --output-on-failure

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig
%post   -n libleechcraft-util-db%{db_postfix} -p /sbin/ldconfig
%postun -n libleechcraft-util-db%{db_postfix} -p /sbin/ldconfig
%post   -n libleechcraft-util-gui%{gui_postfix} -p /sbin/ldconfig
%postun -n libleechcraft-util-gui%{gui_postfix} -p /sbin/ldconfig
%post   -n libleechcraft-util-models%{models_postfix} -p /sbin/ldconfig
%postun -n libleechcraft-util-models%{models_postfix} -p /sbin/ldconfig
%post   -n libleechcraft-util-network%{network_postfix} -p /sbin/ldconfig
%postun -n libleechcraft-util-network%{network_postfix} -p /sbin/ldconfig
%post   -n libleechcraft-util-qml%{qml_postfix} -p /sbin/ldconfig
%postun -n libleechcraft-util-qml%{qml_postfix} -p /sbin/ldconfig
%post   -n libleechcraft-util-shortcuts%{shortcuts_postfix} -p /sbin/ldconfig
%postun -n libleechcraft-util-shortcuts%{shortcuts_postfix} -p /sbin/ldconfig
%post   -n libleechcraft-util-sll%{sll_postfix} -p /sbin/ldconfig
%postun -n libleechcraft-util-sll%{sll_postfix} -p /sbin/ldconfig
%post   -n libleechcraft-util-svcauth%{svcauth_postfix} -p /sbin/ldconfig
%postun -n libleechcraft-util-svcauth%{svcauth_postfix} -p /sbin/ldconfig
%post   -n libleechcraft-util-sys%{sys_postfix} -p /sbin/ldconfig
%postun -n libleechcraft-util-sys%{sys_postfix} -p /sbin/ldconfig
%post   -n libleechcraft-util-tags%{tags_postfix} -p /sbin/ldconfig
%postun -n libleechcraft-util-tags%{tags_postfix} -p /sbin/ldconfig
%post   -n libleechcraft-util-threads%{threads_postfix} -p /sbin/ldconfig
%postun -n libleechcraft-util-threads%{threads_postfix} -p /sbin/ldconfig
%post   -n libleechcraft-util-x11%{x11_postfix} -p /sbin/ldconfig
%postun -n libleechcraft-util-x11%{x11_postfix} -p /sbin/ldconfig
%post   -n libleechcraft-util-xdg%{xdg_postfix} -p /sbin/ldconfig
%postun -n libleechcraft-util-xdg%{xdg_postfix} -p /sbin/ldconfig
%post   -n libleechcraft-util-xpc%{xpc_postfix} -p /sbin/ldconfig
%postun -n libleechcraft-util-xpc%{xpc_postfix} -p /sbin/ldconfig
%post   -n libleechcraft-util-xsd%{xsd_postfix} -p /sbin/ldconfig
%postun -n libleechcraft-util-xsd%{xsd_postfix} -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc CHANGELOG README.md
%license LICENSE
%{_bindir}/%{name}-qt5
%{_mandir}/man1/%{name}-qt5.1.*
%{_bindir}/%{name}-add-file
%{_mandir}/man1/%{name}-add-file.1.*
%{_bindir}/%{name}-handle-file
%{_mandir}/man1/%{name}-handle-file.1.*
%{_bindir}/lc_plugin_wrapper-qt5
%{_mandir}/man1/lc_plugin_wrapper-qt5.1.*
%{settings_dir}/coresettings.xml
%{_datadir}/applications/%{name}-qt5.desktop
%{_datadir}/icons/hicolor/*/*/*
%dir %{_datadir}/icons/hicolor/14x14
%dir %{_datadir}/icons/hicolor/14x14/apps
%dir %{_datadir}/leechcraft
%dir %{settings_dir}
%dir %{translations_dir}
%dir %{qml_dir}
%{translations_dir}/*craft_??.qm
%{translations_dir}/*craft_??_??.qm
%dir %{_libdir}/%{name}
%dir %{plugin_dir}
%{_libdir}/libleechcraft-util-qt5.so.*
%{_libdir}/lib%{name}-xsd-qt5.so.*
%{_datadir}/leechcraft/global_icons/
%dir %{_datadir}/leechcraft/themes
%dir %{_datadir}/leechcraft/themes/*
%{_datadir}/leechcraft/themes/*/*.rc
%exclude %{_datadir}/cmake/Modules/InitLCPlugin.cmake
%{qml_dir}/org/
%{qml_dir}/common/

%files advancednotifications
%defattr(-,root,root)
%{plugin_dir}/*craft_advancednotifications.so
%{translations_dir}/*craft_advancednotifications*
%{settings_dir}/advancednotificationssettings.xml
%{qml_dir}/advancednotifications
%{_datadir}/leechcraft/sounds

%files aggregator
%defattr(-,root,root)
%{settings_dir}/aggregatorsettings.xml
%{translations_dir}/*craft_aggregator_??.qm
%{translations_dir}/*craft_aggregator_??_??.qm
%{plugin_dir}/*craft_aggregator.so

%files aggregator-bodyfetch
%defattr(-,root,root)
%{plugin_dir}/*craft_aggregator_bodyfetch.so
%dir %{_datadir}/leechcraft/scripts
%{_datadir}/leechcraft/scripts/aggregator/

%if 0%{?suse_version} > 1325
%files aggregator-webaccess
%defattr(-,root,root)
%{plugin_dir}/*craft_aggregator_webaccess.so
%{settings_dir}/aggregatorwebaccesssettings.xml
%{translations_dir}/*craft_aggregator_webaccess*.qm
%endif

%files anhero
%defattr(-,root,root)
%{_bindir}/lc_anhero_crashprocess*
%{plugin_dir}/*craft_anhero.so
%{translations_dir}/*craft_anhero*
%doc %{_mandir}/man*/lc_anhero_crashprocess*

%files auscrie
%defattr(-,root,root)
%{translations_dir}/*craft_auscrie_*.qm
%{plugin_dir}/lib%{name}_auscrie.so

%files azoth
%defattr(-,root,root)
%dir %{_datadir}/leechcraft/azoth
%dir %{_datadir}/leechcraft/azoth/styles
%{_datadir}/leechcraft/azoth/emoticons
%{_datadir}/leechcraft/azoth/iconsets
%{settings_dir}/azothsettings.xml
%{translations_dir}/*craft_azoth_??.qm
%{translations_dir}/*craft_azoth_??_??.qm
%{plugin_dir}/*craft_azoth.so

%files azoth-abbrev
%defattr(-,root,root)
%{plugin_dir}/*craft_azoth_abbrev.so
%{translations_dir}/*craft_azoth_abbrev_??.qm
%{translations_dir}/*craft_azoth_abbrev_??_??.qm

%files azoth-acetamide
%defattr(-,root,root)
%{settings_dir}/azothacetamidesettings.xml
%{translations_dir}/*craft_azoth_acetamide*
%{plugin_dir}/*craft_azoth_acetamide.so
%{_datadir}/applications/%{name}-azoth-acetamide-qt5.desktop

%files azoth-adiumstyles
%defattr(644,root,root,755)
%{plugin_dir}/*craft_azoth_adiumstyles*
%{_datadir}/leechcraft/azoth/styles/adium
%{translations_dir}/*craft_azoth_adiumstyles_*.qm

%files azoth-autoidler
%defattr(-,root,root)
%{plugin_dir}/*craft_azoth_autoidler*
%{settings_dir}/azothautoidlersettings.xml
%{translations_dir}/*craft_azoth_autoidler*

%files azoth-autopaste
%defattr(-,root,root)
%{settings_dir}/azothautopastesettings.xml
%{translations_dir}/*craft_azoth_autopaste*
%{plugin_dir}/*craft_azoth_autopaste.so

%files azoth-birthdaynotifier
%defattr(-,root,root)
%{plugin_dir}/*craft_azoth_birthdaynotifier.so
%{settings_dir}/azothbirthdaynotifiersettings.xml
%{translations_dir}/*craft_azoth_birthdaynotifier*

%files azoth-chathistory
%defattr(-,root,root)
%{translations_dir}/*craft_azoth_chathistory*
%{plugin_dir}/*craft_azoth_chathistory.so
%{settings_dir}/azothchathistorysettings.xml

%files azoth-depester
%defattr(-,root,root)
%{plugin_dir}/*craft_azoth_depester.so
%{translations_dir}/*craft_azoth_depester*

%files azoth-embedmedia
%defattr(-,root,root)
%{plugin_dir}/*craft_azoth_embedmedia.so
%{_datadir}/leechcraft/azoth/embedmedia

%files azoth-herbicide
%defattr(-,root,root)
%{plugin_dir}/*craft_azoth_herbicide.so
%{translations_dir}/*craft_azoth_herbicide*
%{settings_dir}/azothherbicidesettings.xml

%files azoth-hili
%defattr(-,root,root)
%{settings_dir}/azothhilisettings.xml
%{translations_dir}/*craft_azoth_hili*
%{plugin_dir}/*craft_azoth_hili.so

%files azoth-isterique
%defattr(-,root,root)
%{plugin_dir}/*craft_azoth_isterique*
%{settings_dir}/azothisteriquesettings.xml
%{translations_dir}/*craft_azoth_isterique*

%files azoth-juick
%defattr(-,root,root)
%{plugin_dir}/*craft_azoth_juick.so
%{translations_dir}/*craft_azoth_juick_*.qm

%files azoth-keeso
%defattr(-,root,root)
%{plugin_dir}/*craft_azoth_keeso.so

%files azoth-lastseen
%defattr(-,root,root)
%{plugin_dir}/*craft_azoth_lastseen*
%{translations_dir}/*craft_azoth_lastseen*

%files azoth-metacontacts
%defattr(-,root,root)
%{plugin_dir}/*craft_azoth_metacontacts*
%{translations_dir}/*craft_azoth_metacontacts*

%files azoth-modnok
%defattr(-,root,root)
%{plugin_dir}/*craft_azoth_modnok*
%{settings_dir}/azothmodnoksettings.xml
%{translations_dir}/*craft_azoth_modnok*
%{_datadir}/leechcraft/azoth/lc_azoth_modnok_latexconvert.sh

%files azoth-mucommands
%defattr(-,root,root)
%{plugin_dir}/*craft_azoth_mucommands.so
%{translations_dir}/*craft_azoth_mucommands_??.qm
%{translations_dir}/*craft_azoth_mucommands_??_??.qm

%files azoth-murm
%defattr(-,root,root)
%{plugin_dir}/*craft_azoth_murm.so
%{translations_dir}/*craft_azoth_murm*.qm
%{settings_dir}/azothmurmsettings.xml
%{_datadir}/leechcraft/azoth/murm

%files azoth-nativeemoticons
%defattr(-,root,root)
%{plugin_dir}/*craft_azoth_nativeemoticons.so
%{translations_dir}/*craft_azoth_nativeemoticons_*.qm

%files azoth-otroid
%defattr(-,root,root)
%{plugin_dir}/*craft_azoth_otroid.so
%{translations_dir}/*craft_azoth_otroid*.qm
%{settings_dir}/azothotroidsettings.xml

%files azoth-rosenthal
%defattr(-,root,root)
%{plugin_dir}/*craft_azoth_rosenthal.so
%{translations_dir}/*craft_azoth_rosenthal*

%files azoth-shx
%defattr(-,root,root)
%{plugin_dir}/*craft_azoth_shx.so
%{settings_dir}/azothshxsettings.xml
%{translations_dir}/*craft_azoth_shx_*.qm

%files azoth-standardstyles
%defattr(-,root,root)
%{plugin_dir}/*craft_azoth_standardstyles.so
%{_datadir}/leechcraft/azoth/styles/standard/
%{translations_dir}/*craft_azoth_standardstyles_*.qm

%files azoth-vader
%defattr(-,root,root)
%{translations_dir}/*craft_azoth_vader*
%{settings_dir}/azothvadersettings.xml
%{plugin_dir}/*craft_azoth_vader.so

%files azoth-velvetbird
%defattr(-,root,root)
%{plugin_dir}/*craft_azoth_velvetbird.so

%files azoth-xoox
%defattr(-,root,root)
%{translations_dir}/*craft_azoth_xoox*
%{plugin_dir}/*craft_azoth_xoox.so
%{_datadir}/applications/%{name}-azoth-xoox-qt5.desktop
%{settings_dir}/azothxooxsettings.xml

%files azoth-xtazy
%defattr(-,root,root)
%{settings_dir}/azothxtazysettings.xml
%{plugin_dir}/*craft_azoth_xtazy.so
%{translations_dir}/*craft_azoth_xtazy*

%ifarch %ix86 x86_64 %arm ppc64le
%files bittorrent
%defattr(-,root,root)
%{settings_dir}/torrentsettings.xml
%{translations_dir}/*craft_bittorrent_*.qm
%{plugin_dir}/*craft_bittorrent.so
%{_datadir}/applications/%{name}-bittorrent-qt5.desktop
%endif

%files blasq
%defattr(-,root,root)
%{plugin_dir}/lib%{name}_blasq.so
%{settings_dir}/blasqsettings.xml
%{qml_dir}/blasq
%{translations_dir}/*craft_blasq_??.qm
%{translations_dir}/*craft_blasq_??_??.qm

%files blasq-deathnote
%defattr(-,root,root)
%{plugin_dir}/lib%{name}_blasq_deathnote.so
%{translations_dir}/*craft_blasq_deathnote*.qm

%files blasq-rappor
%defattr(-,root,root)
%{plugin_dir}/lib%{name}_blasq_rappor.so
%{translations_dir}/*craft_blasq_rappor*.qm

%files blasq-vangog
%defattr(-,root,root)
%{plugin_dir}/lib%{name}_blasq_vangog.so
%{translations_dir}/*craft_blasq_vangog*.qm

%files blogique
%defattr(-,root,root)
%{plugin_dir}/lib%{name}_blogique.so
%{settings_dir}/blogiquesettings.xml
%{translations_dir}/*craft_blogique_??.qm
%{translations_dir}/*craft_blogique_??_??.qm
%dir %{qml_dir}/blogique
%{qml_dir}/blogique/*.qml
%{qml_dir}/blogique/*.js

%files blogique-hestia
%defattr(-,root,root)
%{plugin_dir}/lib%{name}_blogique_hestia.so
%{settings_dir}/blogiquehestiasettings.xml
%{translations_dir}/*craft_blogique_hestia*.qm

%files blogique-metida
%defattr(-,root,root)
%{plugin_dir}/lib%{name}_blogique_metida.so
%{settings_dir}/blogiquemetidasettings.xml
%{translations_dir}/*craft_blogique_metida*.qm

%files certmgr
%defattr(-,root,root)
%{plugin_dir}/lib%{name}_certmgr.so
%{settings_dir}/certmgrsettings.xml
%{translations_dir}/*craft_certmgr*.qm

%files cpuload
%defattr(-,root,root)
%{plugin_dir}/lib%{name}_cpuload.so
%{qml_dir}/cpuload
%{translations_dir}/*craft_cpuload*.qm

%files cstp
%defattr(-,root,root)
%{settings_dir}/cstpsettings.xml
%{translations_dir}/*craft_cstp*.qm
%{plugin_dir}/*leechcraft_cstp.so

%files dbusmanager
%defattr(-,root,root)
%{translations_dir}/*craft_dbusmanager*.qm
%{plugin_dir}/*leechcraft_dbusmanager.so

%files deadlyrics
%defattr(-,root,root)
%{translations_dir}/*craft_deadlyrics*.qm
%{plugin_dir}/*craft_deadlyrics.so

%files devel
%defattr(-,root,root)
%{_datadir}/leechcraft/cmake
%{_includedir}/%{name}
%{_libdir}/libleechcraft-util*.so
%{_libdir}/lib%{name}-xsd*.so
%{_datadir}/cmake/Modules/InitLCPlugin.cmake

%files devmon
%defattr(-,root,root)
%{plugin_dir}/lib%{name}_devmon.so
%{translations_dir}/*craft_devmon_*.qm

%files dolozhee
%defattr(-,root,root)
%{plugin_dir}/lib%{name}_dolozhee.so
%{translations_dir}/*craft_dolozhee_*.qm

%files dumbeep
%defattr(-,root,root)
%{plugin_dir}/lib%{name}_dumbeep.so
%{settings_dir}/dumbeepsettings.xml

%files eleeminator
%defattr(-,root,root)
%{plugin_dir}/lib%{name}_eleeminator.so
%{translations_dir}/*craft_eleeminator_??.qm
%{translations_dir}/*craft_eleeminator_??_??.qm
%{settings_dir}/eleeminatorsettings.xml

%files fenet
%defattr(-,root,root)
%{plugin_dir}/*craft_fenet.so
%{settings_dir}/fenetsettings.xml
%{_bindir}/%{name}-session
%{_mandir}/man1/*-session.1.*
%dir %{_datadir}/leechcraft/fenet
%dir %{_datadir}/leechcraft/fenet/compositing
%dir %{_datadir}/leechcraft/fenet/wms
%{_datadir}/xsessions/LCDE.desktop
%{translations_dir}/*craft_fenet_*.qm
%{_datadir}/leechcraft/fenet/compositing/*compton*

%files fenet-awesome
%defattr(-,root,root)
%dir %{_datadir}/leechcraft/fenet
%dir %{_datadir}/leechcraft/fenet/wms
%{_datadir}/leechcraft/fenet/wms/*awesome*

%files fenet-kwin
%defattr(-,root,root)
%dir %{_datadir}/leechcraft/fenet
%dir %{_datadir}/leechcraft/fenet/wms
%{_datadir}/leechcraft/fenet/wms/*kwin*

%files fenet-openbox
%defattr(-,root,root)
%dir %{_datadir}/leechcraft/fenet
%dir %{_datadir}/leechcraft/fenet/wms
%{_datadir}/leechcraft/fenet/wms/*openbox*

%files gacts
%defattr(-,root,root)
%doc src/plugins/gacts/3rdparty/qxt/LICENSE
%{plugin_dir}/*craft_gacts.so
%{translations_dir}/*craft_gacts_*.qm

%files glance
%defattr(-,root,root)
%{plugin_dir}/*craft_glance.so
%{translations_dir}/*craft_glance*

%files gmailnotifier
%defattr(-,root,root)
%{plugin_dir}/*craft_gmailnotifier.so
%{settings_dir}/gmailnotifiersettings.xml
%{translations_dir}/*craft_gmailnotifier*
%{qml_dir}/gmailnotifier/

%files historyholder
%defattr(-,root,root)
%{plugin_dir}/*leechcraft_historyholder.so
%{translations_dir}/*craft_historyholder*.qm

%files hotstreams
%defattr(-,root,root)
%{plugin_dir}/*craft_hotstreams.so
%{translations_dir}/*craft_hotstreams_*.qm

%files htthare
%defattr(-,root,root)
%{plugin_dir}/lib%{name}_htthare.so
%{settings_dir}/httharesettings.xml
%{translations_dir}/*craft_htthare_*.qm

%files imgaste
%defattr(-,root,root)
%{plugin_dir}/lib%{name}_imgaste.so
%{translations_dir}/*craft_imgaste_*.qm

%files intermutko
%defattr(-,root,root)
%{plugin_dir}/lib%{name}_intermutko.so
%{settings_dir}/intermutkosettings.xml
%{translations_dir}/*craft_intermutko_??.qm
%{translations_dir}/*craft_intermutko_??_??.qm

%files kbswitch
%defattr(-,root,root)
%{plugin_dir}/lib%{name}_kbswitch.so
%{settings_dir}/kbswitchsettings.xml
%{translations_dir}/*craft_kbswitch_*.qm
%{qml_dir}/kbswitch

%files kinotify
%defattr(-,root,root)
%{_datadir}/leechcraft/kinotify
%{settings_dir}/kinotifysettings.xml
%{plugin_dir}/*craft_kinotify.so
%{translations_dir}/*craft_kinotify_*.qm

%files knowhow
%defattr(-,root,root)
%{_datadir}/leechcraft/knowhow
%{plugin_dir}/*craft_knowhow.so
%{settings_dir}/knowhowsettings.xml

%files krigstask
%defattr(-,root,root)
%{plugin_dir}/lib%{name}_krigstask.so
%{qml_dir}/krigstask
%{translations_dir}/*craft_krigstask_*.qm

%files lackman
%defattr(-,root,root)
%{plugin_dir}/*craft_lackman.so
%{settings_dir}/lackmansettings.xml
%{translations_dir}/*craft_lackman*

%files lastfmscrobble
%defattr(-,root,root)
%{plugin_dir}/lib%{name}_lastfmscrobble.so
%{settings_dir}/lastfmscrobblesettings.xml
%{translations_dir}/*craft_lastfmscrobble_*.qm

%files laughty
%defattr(-,root,root)
%{plugin_dir}/lib%{name}_laughty.so
%{translations_dir}/*craft_laughty_*.qm

%files launchy
%defattr(-,root,root)
%{plugin_dir}/lib%{name}_launchy.so
%{translations_dir}/*craft_launchy_*.qm
%{qml_dir}/launchy

%files lemon
%defattr(-,root,root)
%{plugin_dir}/lib%{name}_lemon.so
%{qml_dir}/lemon/
%{translations_dir}/*craft_lemon_*.qm
%{settings_dir}/lemonsettings.xml

%files lhtr
%defattr(-,root,root)
%{plugin_dir}/lib%{name}_lhtr.so
%{translations_dir}/*craft_lhtr_*.qm
%{settings_dir}/lhtrsettings.xml

%files liznoo
%defattr(-,root,root)
%{plugin_dir}/lib%{name}_liznoo.so
%{settings_dir}/liznoosettings.xml
%{translations_dir}/*craft_liznoo_*.qm
%{qml_dir}/liznoo

%files lmp
%defattr(-,root,root)
%{settings_dir}/lmpsettings.xml
%{settings_dir}/lmpfilterrgsettings.xml
%{translations_dir}/*craft_lmp_??.qm
%{translations_dir}/*craft_lmp_??_??.qm
%{plugin_dir}/*craft_lmp.so
%{_datadir}/applications/%{name}-lmp*-qt5.desktop
%dir %{qml_dir}/lmp
%{qml_dir}/lmp/*.qml
%exclude %{qml_dir}/lmp/brainslugz

%files lmp-brainslugz
%defattr(-,root,root)
%{plugin_dir}/lib%{name}_lmp_brainslugz.so
%dir %{qml_dir}/lmp
%{qml_dir}/lmp/brainslugz
%{translations_dir}/*craft_lmp_brainslugz_*.qm

%files lmp-dumbsync
%defattr(-,root,root)
%{plugin_dir}/*craft_lmp_dumbsync.so
%{settings_dir}/lmpdumbsyncsettings.xml
%{translations_dir}/*craft_lmp_dumbsync_??.qm
%{translations_dir}/*craft_lmp_dumbsync_??_??.qm

%files lmp-fradj
%defattr(-,root,root)
%{plugin_dir}/*craft_lmp_fradj.so
%{translations_dir}/*craft_lmp_fradj_??.qm
%{translations_dir}/*craft_lmp_fradj_??_??.qm

%files lmp-graffiti
%defattr(-,root,root)
%{plugin_dir}/*craft_lmp_graffiti.so
%{translations_dir}/*craft_lmp_graffiti_??.qm
%{translations_dir}/*craft_lmp_graffiti_??_??.qm

%files lmp-httstream
%defattr(-,root,root)
%{plugin_dir}/*craft_lmp_httstream.so
%{settings_dir}/lmphttstreamfiltersettings.xml
%{translations_dir}/*craft_lmp_httstream_??.qm
%{translations_dir}/*craft_lmp_httstream_??_??.qm

%files lmp-mp3tunes
%defattr(-,root,root)
%{plugin_dir}/*craft_lmp_mp3tunes.so
%{settings_dir}/lmpmp3tunessettings.xml

%files lmp-mtpsync
%defattr(-,root,root)
%{plugin_dir}/*craft_lmp_mtpsync.so

%if 0%{?sle_version} > 150300 || 0%{?suse_version} > 1500
%ifarch %ix86 x86_64 ppc64 ppc64le
%files lmp-potorchu
%defattr(-,root,root)
%{plugin_dir}/*craft_lmp_potorchu.so
%{translations_dir}/*craft_lmp_potorchu_??.qm
%{translations_dir}/*craft_lmp_potorchu_??_??.qm
%endif
%endif

%files lmp-ppl
%defattr(-,root,root)
%{plugin_dir}/lib%{name}_lmp_ppl.so
%{translations_dir}/*craft_lmp_ppl_*.qm

%files mellonetray
%defattr(-,root,root)
%{plugin_dir}/lib%{name}_mellonetray.so
%{qml_dir}/mellonetray/
%{translations_dir}/*craft_mellonetray_*.qm

%if 0%{?suse_version} > 1325 || 0%{?sle_version} >= 120300
%files monocle
%defattr(-,root,root)
%{plugin_dir}/lib%{name}_monocle.so
%{translations_dir}/*craft_monocle_??.qm
%{translations_dir}/*craft_monocle_??_??.qm
%{settings_dir}/monoclesettings.xml

%files monocle-dik
%defattr(-,root,root)
%{plugin_dir}/lib%{name}_monocle_dik.so
%{translations_dir}/*craft_monocle_dik_??.qm
%{translations_dir}/*craft_monocle_dik_??_??.qm

%files monocle-fxb
%defattr(-,root,root)
%{plugin_dir}/lib%{name}_monocle_fxb.so
%{_datadir}/applications/%{name}-monocle-fxb-qt5.desktop
%{settings_dir}/monoclefxbsettings.xml
%{translations_dir}/*craft_monocle_fxb_??.qm
%{translations_dir}/*craft_monocle_fxb_??_??.qm

%files monocle-pdf
%defattr(-,root,root)
%{plugin_dir}/lib%{name}_monocle_pdf.so
%{_datadir}/applications/%{name}-monocle-pdf-qt5.desktop
%{settings_dir}/monoclepdfsettings.xml
%{translations_dir}/*craft_monocle_pdf_??.qm
%{translations_dir}/*craft_monocle_pdf_??_??.qm

%files monocle-postrus
%defattr(-,root,root)
%{plugin_dir}/lib%{name}_monocle_postrus.so
%{_datadir}/applications/%{name}-monocle-postrus-qt5.desktop
%{translations_dir}/*craft_monocle_postrus_??.qm
%{translations_dir}/*craft_monocle_postrus_??_??.qm

%files monocle-seen
%defattr(-,root,root)
%{plugin_dir}/lib%{name}_monocle_seen.so
%{_datadir}/applications/%{name}-monocle-seen-qt5.desktop
%{translations_dir}/*craft_monocle_seen_??.qm
%{translations_dir}/*craft_monocle_seen_??_??.qm
%endif

%files musiczombie
%defattr(-,root,root)
%{plugin_dir}/lib%{name}_musiczombie.so
%{translations_dir}/*craft_musiczombie_*.qm

%files namauth
%defattr(-,root,root)
%{plugin_dir}/lib%{name}_namauth.so
%{translations_dir}/*craft_namauth_*.qm

%files netstoremanager
%defattr(-,root,root)
%{plugin_dir}/*craft_netstoremanager.so
%{settings_dir}/netstoremanagersettings.xml
%{translations_dir}/*craft_netstoremanager_??.qm
%{translations_dir}/*craft_netstoremanager_??_??.qm

%files netstoremanager-googledrive
%defattr(-,root,root)
%{plugin_dir}/*craft_netstoremanager_googledrive.so
%{settings_dir}/nsmgoogledrivesettings.xml
%{translations_dir}/*craft_netstoremanager_googledrive_*.qm

%files networkmonitor
%defattr(-,root,root)
%{translations_dir}/*craft_networkmonitor*.qm
%{plugin_dir}/*craft_networkmonitor.so

%files newlife
%defattr(-,root,root)
%{translations_dir}/*craft_newlife*.qm
%{plugin_dir}/*craft_newlife.so

%files ooronee
%defattr(-,root,root)
%{plugin_dir}/lib%{name}_ooronee.so
%{settings_dir}/ooroneesettings.xml
%{qml_dir}/ooronee
%{translations_dir}/*craft_ooronee_*.qm

%files otlozhu
%defattr(-,root,root)
%{plugin_dir}/lib%{name}_otlozhu.so
%{translations_dir}/*craft_otlozhu_*.qm
%{settings_dir}/otlozhusettings.xml

%files pintab
%defattr(-,root,root)
%{plugin_dir}/*craft_pintab.so
%{translations_dir}/*craft_pintab_*.qm

%files pogooglue
%defattr(-,root,root)
%{plugin_dir}/*craft_pogooglue*
%{translations_dir}/*craft_pogooglue*

%files poshuku
%defattr(-,root,root)
%dir %{_datadir}/leechcraft/installed
%{_datadir}/leechcraft/installed/poshuku/
%{settings_dir}/poshukusettings.xml
%{translations_dir}/*craft_poshuku_??.qm
%{translations_dir}/*craft_poshuku_??_??.qm
%{plugin_dir}/*craft_poshuku.so

%files poshuku-autosearch
%defattr(-,root,root)
%{plugin_dir}/*craft_poshuku_autosearch.so
%{translations_dir}/*craft_poshuku_autosearch_*.qm

%files poshuku-cleanweb
%defattr(-,root,root)
%{settings_dir}/poshukucleanwebsettings.xml
%{translations_dir}/*craft_poshuku_cleanweb*.qm
%{plugin_dir}/*craft_poshuku_cleanweb.so

%files poshuku-dcac
%defattr(-,root,root)
%{plugin_dir}/*craft_poshuku_dcac.so
%{translations_dir}/*craft_poshuku_dcac_??.qm
%{translations_dir}/*craft_poshuku_dcac_??_??.qm
%{settings_dir}/poshukudcacsettings.xml

%files poshuku-fatape
%defattr(-,root,root)
%{settings_dir}/poshukufatapesettings.xml
%{plugin_dir}/*craft_poshuku_fatape.so
%{translations_dir}/*craft_poshuku_fatape_*.qm

%files poshuku-filescheme
%defattr(-,root,root)
%{translations_dir}/*craft_poshuku_filescheme_*.qm
%{plugin_dir}/*craft_poshuku_filescheme.so

%files poshuku-foc
%defattr(-,root,root)
%{translations_dir}/*craft_poshuku_foc_*.qm
%{plugin_dir}/*craft_poshuku_foc.so
%{settings_dir}/poshukufocsettings.xml

%files poshuku-fua
%defattr(-,root,root)
%{settings_dir}/poshukufuasettings.xml
%{translations_dir}/*craft_poshuku_fua*.qm
%{plugin_dir}/*craft_poshuku_fua.so

%files poshuku-keywords
%defattr(-,root,root,-)
%{plugin_dir}/*craft_poshuku_keywords.so
%{settings_dir}/poshukukeywordssettings.xml
%{translations_dir}/*craft_poshuku_keywords_*.qm

%files poshuku-onlinebookmarks
%defattr(-,root,root)
%{settings_dir}/poshukuonlinebookmarkssettings.xml
%{translations_dir}/*craft_poshuku_onlinebookmarks*.qm
%{plugin_dir}/*craft_poshuku_onlinebookmarks.so

%files poshuku-onlinebookmarks-delicious
%defattr(-,root,root)
%{plugin_dir}/*craft_poshuku_onlinebookmarks_delicious*

%files poshuku-onlinebookmarks-readitlater
%defattr(-,root,root)
%{plugin_dir}/*craft_poshuku_onlinebookmarks_readitlater.*

%files poshuku-qrd
%defattr(-,root,root)
%{plugin_dir}/lib%{name}_poshuku_qrd.so
%{translations_dir}/*craft_poshuku_qrd_??.qm
%{translations_dir}/*craft_poshuku_qrd_??_??.qm

%files poshuku-speeddial
%defattr(-,root,root)
%{plugin_dir}/lib%{name}_poshuku_speeddial.so
%{settings_dir}/poshukuspeeddialsettings.xml
%{translations_dir}/*craft_poshuku_speeddial_??.qm
%{translations_dir}/*craft_poshuku_speeddial_??_??.qm

%files poshuku-webkitview
%defattr(-,root,root)
%{settings_dir}/poshukuwebkitviewsettings.xml
%{translations_dir}/*craft_poshuku_webkitview*.qm
%{plugin_dir}/*craft_poshuku_webkitview.so

%files rosenthal
%defattr(-,root,root)
%{plugin_dir}/lib%{name}_rosenthal.so
%{translations_dir}/*craft_rosenthal*
%{settings_dir}/rosenthalsettings.xml

%files sb2
%defattr(-,root,root)
%{plugin_dir}/lib%{name}_sb2.so
%{qml_dir}/sb2/
%{settings_dir}/sb2panelsettings.xml
%{translations_dir}/*craft_sb2_*.qm

%files scroblibre
%defattr(-,root,root)
%{plugin_dir}/lib%{name}_scroblibre.so
%{settings_dir}/scroblibresettings.xml
%{translations_dir}/*craft_scroblibre_*.qm

%files secman
%defattr(-,root,root)
%{plugin_dir}/*craft_secman.so
%{translations_dir}/*craft_secman_*.qm

%files secman-simplestorage
%defattr(-,root,root)
%{plugin_dir}/*craft_secman_simplestorage.so

%files seekthru
%defattr(-,root,root)
%{settings_dir}/seekthrusettings.xml
%{translations_dir}/*craft_seekthru*.qm
%{plugin_dir}/*craft_seekthru.so

%files summary
%defattr(-,root,root)
%{translations_dir}/*craft_summary*.qm
%{plugin_dir}/*craft_summary.so

%files sysnotify
%defattr(-,root,root)
%{plugin_dir}/lib%{name}_sysnotify.so
%{translations_dir}/*craft_sysnotify_*.qm

%files tabsessionmanager
%defattr(-,root,root)
%{plugin_dir}/*craft_tabsessmanager.so
%{translations_dir}/*craft_tabsessmanager_*.qm

%files tabslist
%defattr(-,root,root)
%{plugin_dir}/*craft_tabslist.so
%{translations_dir}/*craft_tabslist*

%files textogroose
%defattr(-,root,root)
%{plugin_dir}/lib%{name}_textogroose.so

%files touchstreams
%defattr(-,root,root)
%{plugin_dir}/lib%{name}_touchstreams.so
%{translations_dir}/*craft_touchstreams*.qm
%{settings_dir}/touchstreamssettings.xml

%files tpi
%defattr(-,root,root)
%{plugin_dir}/lib%{name}_tpi.so
%{qml_dir}/tpi/

%files vrooby
%defattr(-,root,root)
%{plugin_dir}/lib%{name}_vrooby.so
%{translations_dir}/*craft_vrooby_*.qm
%{qml_dir}/vrooby

%files xproxy
%defattr(-,root,root)
%{plugin_dir}/lib%{name}_xproxy.so
%{settings_dir}/xproxysettings.xml
%{translations_dir}/*craft_xproxy_*.qm
%{_datadir}/leechcraft/scripts/xproxy

%files xtazy
%defattr(-,root,root)
%{settings_dir}/xtazysettings.xml
%{plugin_dir}/*craft_xtazy.so
%{translations_dir}/*craft_xtazy_??.qm
%{translations_dir}/*craft_xtazy_??_??.qm

%files zalil
%defattr(-,root,root)
%{plugin_dir}/*craft_zalil.so
%{translations_dir}/*craft_zalil_??.qm
%{translations_dir}/*craft_zalil_??_??.qm

%files -n libleechcraft-util-db%{db_postfix}
%defattr(-,root,root)
%{_libdir}/*-util-db*.so.*

%files -n libleechcraft-util-gui%{gui_postfix}
%defattr(-,root,root)
%{_libdir}/*-util-gui*.so.*

%files -n libleechcraft-util-models%{models_postfix}
%defattr(-,root,root)
%{_libdir}/*-util-models*.so.*

%files -n libleechcraft-util-network%{network_postfix}
%defattr(-,root,root)
%{_libdir}/*-util-network*.so.*

%files -n libleechcraft-util-qml%{qml_postfix}
%defattr(-,root,root)
%{_libdir}/*-util-qml*.so.*

%files -n libleechcraft-util-shortcuts%{shortcuts_postfix}
%defattr(-,root,root)
%{_libdir}/*-util-shortcuts*.so.*

%files -n libleechcraft-util-sll%{sll_postfix}
%defattr(-,root,root)
%{_libdir}/*-util-sll*.so.*

%files -n libleechcraft-util-svcauth%{svcauth_postfix}
%defattr(-,root,root)
%{_libdir}/*-util-svcauth*.so.*

%files -n libleechcraft-util-sys%{sys_postfix}
%defattr(-,root,root)
%{_libdir}/*-util-sys*.so.*

%files -n libleechcraft-util-tags%{tags_postfix}
%defattr(-,root,root)
%{_libdir}/*-util-tags*.so.*

%files -n libleechcraft-util-threads%{threads_postfix}
%defattr(-,root,root)
%{_libdir}/*-util-threads*.so.*

%files -n libleechcraft-util-x11%{x11_postfix}
%defattr(-,root,root)
%{_libdir}/*-util-x11*.so.*

%files -n libleechcraft-util-xdg%{xdg_postfix}
%defattr(-,root,root)
%{_libdir}/*-util-xdg*.so.*

%files -n libleechcraft-util-xpc%{xpc_postfix}
%defattr(-,root,root)
%{_libdir}/*-util-xpc*.so.*

%files -n libleechcraft-util-xsd%{xsd_postfix}
%defattr(-,root,root)
%{_libdir}/*-util-xsd*.so.*

%changelog
