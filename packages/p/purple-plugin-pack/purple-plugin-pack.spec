#
# spec file for package purple-plugin-pack
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2007 Ivan N. Zlatev <contact@i-nz.net>
# Copyright (c) 2009 Lukas Krejza <gryffus@hkfree.org>
# Copyright (c) 2011 Christoph Miebach <christoph.miebach@web.de>
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


Name:           purple-plugin-pack
Version:        2.7.0
Release:        0
Summary:        Compilation of plugins for libpurple and Pidgin
# FIXME: On new upstream version, check if GPLv3+ plugins are still under the same licence (add COPYING.GPL3 to the extras subpackage if present upstream).
License:        GPL-2.0-or-later AND GPL-3.0-or-later
Group:          Productivity/Networking/Instant Messenger
Url:            https://guifications.org/
Source:         https://bitbucket.org/rekkanoryo/purple-plugin-pack/downloads/%{name}-%{version}.tar.bz2
# PATCH-FIX-OPENSUSE purple-plugin-pack-fix-autoprofile-crash.patch -- Fix an Autoprofile crash when uptime is not being run in English.
Patch0:         purple-plugin-pack-fix-autoprofile-crash.patch
# PATCH-FIX-UPSTREAM purple-plugin_pack-fix-warning.patch christoph.miebach@web.de -- Fix typecasting from pointer to integer and back (commit ce0c3dc).
Patch1:         purple-plugin_pack-fix-warning.patch
BuildRequires:  intltool
BuildRequires:  pkgconfig
#BuildRequires:  talkfilters-devel
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(enchant)
BuildRequires:  pkgconfig(finch)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gnt)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(gtkspell-2.0) >= 2.0.2
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(pidgin)
BuildRequires:  pkgconfig(purple)
%if 0%{?suse_version} >= 1500
BuildRequires:  python2
%else
BuildRequires:  python
%endif

%description
The Purple Plugin Pack is a compilation of plugins for the libpurple
family of IM clients.

%package -n libpurple-plugin-pack
Summary:        Compilation of plugins for libpurple
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Instant Messenger
Recommends:     libpurple-plugin-pack-lang
Enhances:       libpurple
# purple-plugin_pack was last used in openSUSE 12.1.
Provides:       purple-plugin_pack = %{version}
Obsoletes:      purple-plugin_pack < %{version}
# purple-plugin-pack-lang was last used in openSUSE Leap 42.2.
Obsoletes:      %{name}-lang < %{version}-%{release}

%description -n libpurple-plugin-pack
The Purple Plugin Pack is a compilation of plugins for the
libpurple family of IM clients.

To avoid licence issues between GPLv3+ plugins and other plugins
that could be incompatible with GPLv3+, the GPLv3+ plugins are
split into the libpurple-plugin-pack-extras package.

%lang_package -n libpurple-plugin-pack

%package -n libpurple-plugin-pack-extras
Summary:        Compilation of plugins for libpurple -- GPLv3+ Plugins
License:        GPL-3.0-or-later
Group:          Productivity/Networking/Instant Messenger
Requires:       libpurple-plugin-pack = %{version}
Enhances:       libpurple-plugin-pack

%description -n libpurple-plugin-pack-extras
The Purple Plugin Pack is a compilation of plugins for the
libpurple family of IM clients.

This package contains GPLv3+ plugins. Their licence might cause
incompatibilities with other plugins.

%package -n pidgin-plugin-pack
Summary:        Compilation of plugins for Pidgin
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Instant Messenger
Requires:       libpurple-plugin-pack = %{version}
%requires_ge    pidgin
Supplements:    packageand(pidgin:libpurple-plugin-pack)
# pidgin-plugin_pack was last used in openSUSE 12.1.
Provides:       pidgin-plugin_pack = %{version}
Obsoletes:      pidgin-plugin_pack < %{version}

%description -n pidgin-plugin-pack
The Purple Plugin Pack is a compilation of plugins for the
libpurple family of IM clients.

This package provides the Pidgin plugins from the Purple Plugin Pack.

To avoid licence issues between GPLv+ plugins and other plugins
that could be incompatible with GPLv3+, the GPLv3+ plugins are split
into the pidgin-plugin-pack-extras package.

%package -n pidgin-plugin-pack-extras
Summary:        Compilation of plugins for Pidgin -- GPLv3+ Plugins
License:        GPL-3.0-or-later
Group:          Productivity/Networking/Instant Messenger
Requires:       libpurple-plugin-pack-extras = %{version}
Requires:       pidgin-plugin-pack = %{version}
Enhances:       pidgin-plugin-pack
Supplements:    packageand(pidgin:libpurple-plugin-pack-extras)

%description -n pidgin-plugin-pack-extras
The Purple Plugin Pack is a compilation of plugins for the
libpurple family of IM clients.

This package provides the Pidgin plugins from the Purple Plugin Pack.

This package contains GPLv3+ plugins. Their licence might cause
incompatibilities with other plugins.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
export PYTHON=python2
%configure
make %{?_smp_mflags} V=1

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
%find_lang plugin_pack

%files -n libpurple-plugin-pack
%if 0%{?suse_version} >= 1500
%license COPYING
%else
%doc COPYING
%endif
%doc AUTHORS ChangeLog README
# Explicitly list plugins to notice when any is missing and to ease split with extras.
%{_libdir}/purple-2/autoprofile.so
%{_libdir}/purple-2/autoreply.so
%{_libdir}/purple-2/bash.so
%{_libdir}/purple-2/capsnot.so
%{_libdir}/purple-2/colorize.so
%{_libdir}/purple-2/dewysiwygification.so
%{_libdir}/purple-2/dice.so
%{_libdir}/purple-2/eight_ball.so
%{_libdir}/purple-2/findip.so
%{_libdir}/purple-2/flip.so
%{_libdir}/purple-2/google.so
%{_libdir}/purple-2/groupmsg.so
%{_libdir}/purple-2/highlight.so
%{_libdir}/purple-2/ignore.so
%{_libdir}/purple-2/irchelper.so
%{_libdir}/purple-2/irc-more.so
%{_libdir}/purple-2/libsnpp.so
%{_libdir}/purple-2/listhandler.so
%{_libdir}/purple-2/napster.so
%{_libdir}/purple-2/oldlogger.so
%{_libdir}/purple-2/showoffline.so
%{_libdir}/purple-2/simfix.so
%{_libdir}/purple-2/slashexec.so
%{_libdir}/purple-2/splitter.so
%{_libdir}/purple-2/sslinfo.so
%{_libdir}/purple-2/translate.so
%{_libdir}/purple-2/xmppprio.so

%files -n libpurple-plugin-pack-lang -f plugin_pack.lang

%files -n libpurple-plugin-pack-extras
%doc AUTHORS ChangeLog README
%{_libdir}/purple-2/ning.so
%{_libdir}/purple-2/okcupid.so
%{_libdir}/purple-2/omegle.so

%files -n pidgin-plugin-pack
%if 0%{?suse_version} >= 1500
%license COPYING
%else
%doc COPYING
%endif
%doc AUTHORS ChangeLog README
# Explicitly list plugins to notice when any is missing and to ease split with extras.
%{_libdir}/pidgin/album.so
%{_libdir}/pidgin/blistops.so
%{_libdir}/pidgin/convbadger.so
%{_libdir}/pidgin/difftopic.so
%{_libdir}/pidgin/enhancedhist.so
%{_libdir}/pidgin/gRIM.so
%{_libdir}/pidgin/icon_override.so
%{_libdir}/pidgin/infopane.so
%{_libdir}/pidgin/irssi.so
%{_libdir}/pidgin/lastseen.so
%{_libdir}/pidgin/listlog.so
%{_libdir}/pidgin/mystatusbox.so
%{_libdir}/pidgin/nicksaid.so
%{_libdir}/pidgin/pidgin-schedule.so
%{_libdir}/pidgin/plonkers.so
%{_libdir}/pidgin/sepandtab.so
%{_libdir}/pidgin/switchspell.so
%{_libdir}/pidgin/timelog.so
%{_libdir}/pidgin/xchat-chats.so
%{_datadir}/pixmaps/pidgin/protocols/*/napster.png

%files -n pidgin-plugin-pack-extras
%doc AUTHORS ChangeLog README
%{_datadir}/pixmaps/pidgin/protocols/*/okcupid.png

%changelog
