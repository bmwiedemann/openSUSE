#
# spec file for package smuxi
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           smuxi
Version:        1.0.7
Release:        0
# FIXME: when db4o is in Factory, uncomment BuildRequires for it
Url:            http://www.smuxi.org
Source0:        http://www.smuxi.org/jaws/data/files/%{name}-%{version}.tar.gz
Summary:        Smart MUltipleXed Irc
#BuildRequires:  indicate-sharp
License:        GPL-2.0+
Group:          Productivity/Networking/IRC
BuildRequires:  intltool
BuildRequires:  mono-devel >= 2.6
BuildRequires:  update-desktop-files
BuildRequires:  mono(System.Web.Extensions)
#BuildRequires:  pkgconfig(db4o) >= 8.0
BuildRequires:  pkgconfig(dbus-sharp-1.0)
BuildRequires:  pkgconfig(dbus-sharp-glib-1.0)
BuildRequires:  pkgconfig(glade-sharp-2.0) >= 2.8
BuildRequires:  pkgconfig(glib-sharp-2.0) >= 2.8
BuildRequires:  pkgconfig(gtk-sharp-2.0) >= 2.8
BuildRequires:  pkgconfig(gtkspell-2.0)
BuildRequires:  pkgconfig(log4net)
BuildRequires:  pkgconfig(nini-1.1)
BuildRequires:  pkgconfig(notify-sharp)
BuildRequires:  pkgconfig(stfl) >= 0.21
Recommends:     %{name}-frontend-gnome
%if 0%{suse_version} >= 1100
Recommends:     %{name}-server
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Smuxi is an irssi-inspired, flexible, user-friendly and cross-platform
IRC client for advanced users, targeting the GNOME desktop.

%package engine
Summary:        Smart MUltipleXed Irc - Engine Library
Group:          Productivity/Networking/IRC
Requires:       mono-data-sqlite
Recommends:     %{name}-engine-irc
Recommends:     %{name}-engine-lang
Recommends:     %{name}-engine-twitter
Recommends:     %{name}-engine-xmpp

%description engine
Smuxi is an irssi-inspired, flexible, user-friendly and cross-platform
IRC client for advanced users, targeting the GNOME desktop.

%package engine-campfire
Summary:        Smart MUltipleXed Irc - Campfire Engine
Group:          Productivity/Networking/IRC
Requires:       %{name}-engine = %{version}
Recommends:     %{name}-engine-campfire-lang

%description engine-campfire
Smuxi is an irssi-inspired, flexible, user-friendly and cross-platform
IRC client for advanced users, targeting the GNOME desktop.

%package engine-irc
Summary:        Smart MUltipleXed Irc - IRC Engine
Group:          Productivity/Networking/IRC
Requires:       %{name}-engine = %{version}
Recommends:     %{name}-engine-irc-lang

%description engine-irc
Smuxi is an irssi-inspired, flexible, user-friendly and cross-platform
IRC client for advanced users, targeting the GNOME desktop.

%package engine-jabbr
Summary:        Smart MUltipleXed Irc - Jabber Engine
Group:          Productivity/Networking/IRC
Requires:       %{name}-engine = %{version}
Recommends:     %{name}-engine-jabbr-lang

%description engine-jabbr
Smuxi is an irssi-inspired, flexible, user-friendly and cross-platform
IRC client for advanced users, targeting the GNOME desktop.

%package engine-twitter
Summary:        Smart MUltipleXed Irc - Twitter Engine
Group:          Productivity/Networking/Other
Requires:       %{name}-engine = %{version}
Recommends:     %{name}-engine-twitter-lang

%description engine-twitter
Smuxi is an irssi-inspired, flexible, user-friendly and cross-platform
Twitter client for advanced users, targeting the GNOME desktop.

%package engine-xmpp
Summary:        Smart MUltipleXed Irc - XMPP Engine
Group:          Productivity/Networking/Other
Requires:       %{name}-engine = %{version}

%description engine-xmpp
Smuxi is an irssi-inspired, flexible, user-friendly and cross-platform
XMPP client for advanced users, targeting the GNOME desktop.

%package frontend
Summary:        Smart MUltipleXed Irc - Frontend Library
Group:          Productivity/Networking/IRC
Requires:       %{name}-engine = %{version}
Recommends:     %{name}-frontend-lang

%description frontend
Smuxi is an irssi-inspired, flexible, user-friendly and cross-platform
IRC client for advanced users, targeting the GNOME desktop.

%package frontend-gnome
Summary:        Smart MUltipleXed Irc - GNOME Frontend
Group:          Productivity/Networking/IRC
Requires:       %{name}-frontend = %{version}
Requires:       mono-locale-extras
Recommends:     %{name}-frontend-gnome-lang

%description frontend-gnome
Smuxi is an irssi-inspired, flexible, user-friendly and cross-platform
IRC client for advanced users, targeting the GNOME desktop.

%package frontend-gnome-irc
Summary:        Smart MUltipleXed Irc - IRC Library for GNOME Frontend
Group:          Productivity/Networking/IRC
Requires:       %{name}-engine-irc = %{version}
Requires:       %{name}-frontend-gnome = %{version}
Recommends:     %{name}-frontend-gnome-irc-lang
Supplements:    packageand(%{name}-frontend-gnome:%{name}-engine-irc)

%description frontend-gnome-irc
Smuxi is an irssi-inspired, flexible, user-friendly and cross-platform
IRC client for advanced users, targeting the GNOME desktop.

%package frontend-gnome-twitter
Summary:        Smart MUltipleXed Irc - TWITTER Library for GNOME Frontend
Group:          Productivity/Networking/IRC
Requires:       %{name}-engine-twitter = %{version}
Requires:       %{name}-frontend-gnome = %{version}
Recommends:     %{name}-frontend-gnome-twitter-lang
Supplements:    packageand(%{name}-frontend-gnome:%{name}-engine-twitter)

%description frontend-gnome-twitter
Smuxi is an irssi-inspired, flexible, user-friendly and cross-platform
IRC client for advanced users, targeting the GNOME desktop.

%package frontend-gnome-xmpp
Summary:        Smart MUltipleXed Irc - XMPP Library for GNOME Frontend
Group:          Productivity/Networking/IRC
Requires:       %{name}-engine-xmpp = %{version}
Requires:       %{name}-frontend-gnome = %{version}
Supplements:    packageand(%{name}-frontend-gnome:%{name}-engine-xmpp)

%description frontend-gnome-xmpp
Smuxi is an irssi-inspired, flexible, user-friendly and cross-platform
XMPP client for advanced users, targeting the GNOME desktop.

%package frontend-stfl
Summary:        Smart MUltipleXed Irc - Structured Terminal Form Frontend
Group:          Productivity/Networking/IRC
Requires:       %{name}-frontend = %{version}

%description frontend-stfl
Smuxi is an irssi-inspired, flexible, user-friendly and cross-platform
IRC client for advanced users.

This package provides the stfl (Structured Terminal Forms Library) based frontend.

%package message-buffer
Summary:        Smart MUltipleXed Irc - Structured Terminal Form Frontend
Group:          Productivity/Networking/IRC
Requires:       %{name}-frontend = %{version}
Recommends:     %{name}-message-buffer-lang

%description message-buffer
Smuxi is an irssi-inspired, flexible, user-friendly and cross-platform
IRC client for advanced users.

%package server
Summary:        Smart MUltipleXed Irc - Server
Group:          Productivity/Networking/IRC
Requires:       %{name}-engine = %{version}
Recommends:     %{name}-server-lang

%description server
Smuxi is an irssi-inspired, flexible, user-friendly and cross-platform
IRC client for advanced users, targeting the GNOME desktop.

%lang_package -n %{name}-engine
%lang_package -n %{name}-engine-irc
%lang_package -n %{name}-engine-jabbr
%lang_package -n %{name}-engine-campfire
%lang_package -n %{name}-engine-twitter
%lang_package -n %{name}-engine-xmpp
%lang_package -n %{name}-frontend
%lang_package -n %{name}-frontend-gnome
%lang_package -n %{name}-frontend-gnome-irc
%lang_package -n %{name}-frontend-gnome-xmpp
%lang_package -n %{name}-frontend-gnome-twitter
%lang_package -n %{name}-message-buffer
%lang_package -n %{name}-server
%prep
%setup -q

%build
%configure \
        --libdir=%{_prefix}/lib \
        MCS=%{_bindir}/dmcs
make

%install
%make_install
rm -f %{buildroot}%{_prefix}/lib/pkgconfig/*.pc
%find_lang %{name}-engine
%find_lang %{name}-engine-campfire
%find_lang %{name}-engine-irc
%find_lang %{name}-engine-jabbr
%find_lang %{name}-engine-twitter
%find_lang %{name}-engine-xmpp
%find_lang %{name}-frontend
%find_lang %{name}-frontend-gnome
%find_lang %{name}-frontend-gnome-irc
%find_lang %{name}-frontend-gnome-twitter
%find_lang %{name}-frontend-gnome-xmpp
%find_lang %{name}-message-buffer
%find_lang %{name}-server
%suse_update_desktop_file %{name}-frontend-gnome

%clean
rm -rf %buildroot

%if 0%{?suse_version} > 1130
%post frontend-gnome
%desktop_database_post
%icon_theme_cache_post
%endif

%if 0%{?suse_version} > 1130
%postun frontend-gnome
%desktop_database_postun
%icon_theme_cache_postun
%endif

%files
%defattr(-,root,root)
%doc BUGS LICENSE TODO FEATURES CREDITS
%dir %{_prefix}/lib/%{name}
%{_datadir}/icons/hicolor/*/apps/smuxi-group-chat.png
%{_datadir}/icons/hicolor/*/apps/smuxi-person-chat.png

%files engine
%defattr(-,root,root)
%doc LICENSE
%{_prefix}/lib/%{name}/Db4objects.Db4o.dll*
%{_prefix}/lib/%{name}/Nini.dll
%{_prefix}/lib/%{name}/%{name}-engine.dll*
%{_prefix}/lib/%{name}/%{name}-common.dll*

%files engine-lang -f %{name}-engine.lang

%files engine-campfire
%defattr(-,root,root)
%doc LICENSE
%{_prefix}/lib/%{name}/%{name}-engine-campfire.dll*
%{_prefix}/lib/%{name}/ServiceStack.*.dll*

%files engine-campfire-lang -f %{name}-engine-campfire.lang

%files engine-irc
%defattr(-,root,root)
%doc LICENSE
%{_prefix}/lib/%{name}/%{name}-engine-irc.dll*
%{_prefix}/lib/%{name}/Meebey.SmartIrc4net.dll*

%files engine-irc-lang -f %{name}-engine-irc.lang

%files engine-jabbr
%defattr(-,root,root)
%doc LICENSE
%{_prefix}/lib/%{name}/%{name}-engine-jabbr.dll*
%{_prefix}/lib/%{name}/JabbR.Client.dll*
%{_prefix}/lib/%{name}/Microsoft.AspNet.SignalR.Client.dll*

%files engine-jabbr-lang -f %{name}-engine-jabbr.lang

%files engine-twitter
%defattr(-,root,root)
%doc LICENSE
%{_prefix}/lib/%{name}/%{name}-engine-twitter.dll*
%{_prefix}/lib/%{name}/Newtonsoft.Json.dll*
%{_prefix}/lib/%{name}/Twitterizer2.dll*
%{_prefix}/lib/%{name}/Twitterizer2.Streaming.dll*

%files engine-twitter-lang -f %{name}-engine-twitter.lang

%files engine-xmpp
%defattr(-,root,root)
%doc LICENSE
%{_prefix}/lib/%{name}/%{name}-engine-xmpp.dll*
%{_prefix}/lib/%{name}/agsxmpp.dll*
%{_prefix}/lib/%{name}/StarkSoftProxy.dll*

%files engine-xmpp-lang -f %{name}-engine-xmpp.lang

%files frontend
%defattr(-,root,root)
%doc LICENSE
%{_prefix}/lib/%{name}/%{name}-frontend.dll*

%files frontend-lang -f %{name}-frontend.lang

%files frontend-gnome
%defattr(-,root,root)
%doc LICENSE
%{_bindir}/%{name}-frontend-gnome
%{_prefix}/lib/%{name}/%{name}-frontend-gnome.exe*
%dir %{_datadir}/appdata
%{_datadir}/appdata/smuxi-frontend-gnome.appdata.xml
%{_datadir}/applications/%{name}-frontend-gnome.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}-frontend-gnome.*
%{_mandir}/man1/%{name}-frontend-gnome.1%{?ext_man}

%files frontend-gnome-lang -f %{name}-frontend-gnome.lang

%files frontend-gnome-irc
%defattr(-,root,root)
%doc LICENSE
%{_prefix}/lib/%{name}/%{name}-frontend-gnome-irc.dll*

%files frontend-gnome-irc-lang -f %{name}-frontend-gnome-irc.lang

%files frontend-gnome-twitter
%defattr(-,root,root)
%doc LICENSE
%{_prefix}/lib/%{name}/%{name}-frontend-gnome-twitter.dll*

%files frontend-gnome-twitter-lang -f %{name}-frontend-gnome-twitter.lang

%files frontend-gnome-xmpp
%defattr(-,root,root)
%doc LICENSE
%{_prefix}/lib/%{name}/%{name}-frontend-gnome-xmpp.dll*

%files frontend-gnome-xmpp-lang -f %{name}-frontend-gnome-xmpp.lang

%files frontend-stfl
%defattr(-,root,root)
%doc LICENSE
%{_bindir}/%{name}-frontend-stfl
%{_prefix}/lib/%{name}/%{name}-frontend-stfl.exe*
%{_mandir}/man1/%{name}-frontend-stfl.1%{?ext_man}

%files message-buffer
%defattr(-,root,root)
%doc LICENSE
%{_bindir}/%{name}-message-buffer
%{_prefix}/lib/%{name}/%{name}-message-buffer.exe*
%{_mandir}/man1/%{name}-message-buffer.1%{?ext_man}

%files message-buffer-lang -f %{name}-message-buffer.lang

%files server
%defattr(-,root,root)
%doc LICENSE
%{_bindir}/%{name}-server
%{_mandir}/man1/%{name}-server.1%{?ext_man}
%{_prefix}/lib/%{name}/%{name}-server.exe*

%files server-lang -f %{name}-server.lang

%changelog
