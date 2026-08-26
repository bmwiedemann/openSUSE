#
# spec file for package zoitechat
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           zoitechat
Version:        2.19.0
Release:        0
Summary:        A graphical IRC (chat) client, fork of HexChat
License:        GPL-2.0-or-later
URL:            https://zoitechat.org/
Source0:        https://github.com/ZoiteChat/zoitechat/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        zoitechat-migrate-sh
Patch0:         zoitechat-migrate-config.patch
BuildRequires:  hicolor-icon-theme
BuildRequires:  intltool
BuildRequires:  lua-devel
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  publicsuffix
BuildRequires:  python3-cffi
BuildRequires:  python3-devel
BuildRequires:  perl(ExtUtils::Embed)
BuildRequires:  pkgconfig(appindicator3-0.1)
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(gio-2.0) >= 2.36.0
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22.0
BuildRequires:  pkgconfig(iso-codes)
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(libcanberra) >= 0.22
BuildRequires:  pkgconfig(libpci)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(openssl) >= 0.9.8
BuildRequires:  pkgconfig(x11)
Recommends:     %{name}-lang
Recommends:     hwdata
Recommends:     iso-codes
%if 0%{?suse_version} > 1600
BuildRequires:  glycin-loaders
%endif

%description
ZoiteChat is a graphical IRC chat client, a fork of HexChat.
It allows joining multiple IRC channels (chat rooms) at the same time,
talking publicly, private one-on-one conversations, etc. File transfers
are possible.

%package devel
Summary:        Development Files for ZoiteChat
Requires:       %{name} = %{version}
Recommends:     %{name}-plugins-perl = %{version}
Recommends:     %{name}-plugins-python3 = %{version}

%description devel
This package includes files needed to develop ZoiteChat modules.

%package plugins-perl
Summary:        Plugin for ZoiteChat adds support for Perl scripts
%{?libperl_requires}

%description plugins-perl
The ZoiteChat plugin providing the Perl scripting interface.

%package plugins-lua
Summary:        Plugin for ZoiteChat adds support for LUA scripts
Requires:       lua

%description plugins-lua
The ZoiteChat plugin providing the LUA scripting interface.

%package plugins-python3
Summary:        Plugin for ZoiteChat adds support for Python3 scripts
Requires:       python3-cffi
Provides:       plugins-python = %{version}
Obsoletes:      plugins-python < %{version}

%description plugins-python3
The ZoiteChat plugin providing the Python 3 scripting interface.

%lang_package

%prep
%autosetup -p1 -n zoitechat-%{version}
sed -i "s|@@LIBDIR@@|%{_libdir}|g" src/common/cfgfiles.c

%build
%meson \
    -Dc_std=gnu99 \
    -Dgtk-frontend=true \
    -Dtls=enabled \
    -Ddbus=enabled \
    -Dlibcanberra=enabled \
    -Dplugin=true \
    -Dwith-checksum=true \
    -Dwith-fishlim=true \
    -Dwith-lua=lua \
    -Dwith-perl=perl \
%if 0%{?suse_version} >= 1599
    -Dwith-python=python3-embed \
%else
    -Dwith-python=python3 \
%endif
    -Dwith-sysinfo=true
%meson_build

%install
%meson_install
%find_lang %{name}
install -D -p -m 0755 %{SOURCE1} %{buildroot}%{_libdir}/%{name}/%{name}-migrate-sh

%files
%license COPYING
%doc readme.md
%{_bindir}/%{name}
%{_libdir}/%{name}/%{name}-migrate-sh
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
%dir %{_libdir}/%{name}/python
%{_libdir}/%{name}/plugins/checksum.so
%{_libdir}/%{name}/plugins/fishlim.so
%{_libdir}/%{name}/plugins/sysinfo.so
%{_datadir}/applications/net.zoite.Zoitechat.desktop
%{_datadir}/icons/hicolor/*/apps/net.zoite.Zoitechat.png
%{_datadir}/icons/hicolor/*/apps/net.zoite.Zoitechat.svg
%dir %{_datadir}/metainfo/
%{_datadir}/metainfo/net.zoite.Zoitechat.appdata.xml
%{_datadir}/dbus-1/services/org.zoitechat.service.service
%{_mandir}/man1/%{name}.1%{?ext_man}

%files devel
%{_includedir}/%{name}-plugin.h
%{_libdir}/pkgconfig/%{name}-plugin.pc

%files plugins-perl
%{_libdir}/%{name}/plugins/perl.so

%files plugins-lua
%{_libdir}/%{name}/plugins/lua.so

%files plugins-python3
%{_libdir}/%{name}/plugins/python.so
%{_libdir}/%{name}/python/*.py

%files lang -f %{name}.lang

%changelog
