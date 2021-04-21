#
# spec file for package hexchat
#
# Copyright (c) 2021 SUSE LLC
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


Name:           hexchat
Version:        2.14.3
Release:        0
Summary:        A graphical IRC (chat) client
License:        GPL-2.0-or-later
Group:          Productivity/Networking/IRC
URL:            https://hexchat.github.io/
Source0:        https://dl.%{name}.net/%{name}/%{name}-%{version}.tar.xz
Source1:        hexchat-migrate-sh
Source2:        https://dl.%{name}.net/%{name}/%{name}-%{version}.tar.xz.asc
Source3:        hexchat.keyring
# PATCH-FEATURE-SLE migrate-configuration-from-xchat.patch tyang@suse.com fate#318480 -- replace xchat with hexchat
Patch1:         migrate-configuration-from-xchat.patch
# PATCH-FIX-UPSTREAM 2559.patch dimstar@opensuse.org -- fix segfault on lua_pop with Lua 5.4.3
Patch2:         https://patch-diff.githubusercontent.com/raw/hexchat/hexchat/pull/2559.patch
BuildRequires:  hicolor-icon-theme
BuildRequires:  intltool
BuildRequires:  lua-devel
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  python3-devel >= 3.8
BuildRequires:  perl(ExtUtils::Embed)
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(gio-2.0) >= 2.34.0
BuildRequires:  pkgconfig(gmodule-2.0) >= 2.34.0
BuildRequires:  pkgconfig(gtk+-2.0) >= 2.24.0
BuildRequires:  pkgconfig(iso-codes)
BuildRequires:  pkgconfig(libcanberra) >= 0.22
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libpci)
BuildRequires:  pkgconfig(libproxy-1.0)
BuildRequires:  pkgconfig(openssl) >= 0.9.8
BuildRequires:  pkgconfig(x11)
Recommends:     %{name}-lang
Recommends:     hwdata
Recommends:     iso-codes
# Provide us as replacement from 1315+
Provides:       xchat = %{version}
Obsoletes:      xchat < %{version}

%description
HexChat is a graphical IRC chat client for the X Window System.
It allows to join multiple IRC channels (chat rooms) at the same time,
talk publicly, private one-on-one conversations, etc. File transfers
are possible.

%package devel
Summary:        Development Files for HexChat
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Recommends:     %{name}-plugins-perl = %{version}
Recommends:     %{name}-plugins-python3 = %{version}

%description devel
This package includes files needed to develop HexChat modules.

%package plugins-perl
Summary:        Plugin for HexChat adds support for Perl scripts
Group:          System/Libraries
%{?libperl_requires}

%description plugins-perl
The HexChat plugin providing the Perl scripting interface.

%package plugins-lua
Summary:        Plugin for HexChat adds support for LUA scripts
Group:          System/Libraries
Requires:       lua

%description plugins-lua
The HexChat plugin providing the LUA scripting interface.

%package plugins-python3
Summary:        Plugin for HexChat adds support for Python3 scripts
Group:          System/Libraries
Provides:       plugins-python = %{version}
Obsoletes:      plugins-python < %{version}

%description plugins-python3
The HexChat plugin providing the Python 3 scripting interface.

%lang_package

%prep
%autosetup -p1

%build
%meson \
    -Dwith-gtk=true \
    -Dwith-ssl=true \
    -Dwith-dbus=true \
    -Dwith-libproxy=true \
    -Dwith-libnotify=true \
    -Dwith-libcanberra=true \
    -Dwith-plugin=true \
    -Dwith-checksum=true \
    -Dwith-fishlim=true \
    -Dwith-lua=lua \
    -Dwith-perl=perl \
    -Dwith-python=python3-embed \
    -Dwith-sysinfo=true
%meson_build

%install
%meson_install
install -Dm 0755 %{SOURCE1} %{buildroot}%{_libdir}/hexchat/$(basename %{SOURCE1})
%find_lang %{name}

%files
%license COPYING
%doc readme.md
%{_bindir}/%{name}
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
%{_libdir}/hexchat/hexchat-migrate-sh
%{_libdir}/%{name}/plugins/checksum.so
%{_libdir}/%{name}/plugins/fishlim.so
%{_libdir}/%{name}/plugins/sysinfo.so
%{_datadir}/applications/io.github.Hexchat.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/*/apps/%{name}.svg
%dir %{_datadir}/metainfo/
%{_datadir}/metainfo/io.github.Hexchat.appdata.xml
%{_datadir}/dbus-1/services/org.%{name}.service.service
%{_mandir}/man1/%{name}.1%{ext_man}

%files devel
%{_includedir}/%{name}-plugin.h
%{_libdir}/pkgconfig/%{name}-plugin.pc

%files plugins-perl
%{_libdir}/%{name}/plugins/perl.so

%files plugins-lua
%{_libdir}/%{name}/plugins/lua.so

%files plugins-python3
%{_libdir}/%{name}/plugins/python.so

%files lang -f %{name}.lang

%changelog
