#
# spec file for package telegram-purple
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           telegram-purple
Version:        1.4.1
Release:        0
Summary:        Plugin for Pidgin for supporting Telegram messager
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Productivity/Networking/Instant Messenger
URL:            https://github.com/majn/telegram-purple
Source:         https://github.com/majn/telegram-purple/releases/download/v%{version}/%{name}_%{version}.orig.tar.gz
# PATCH-FIX-UPSTREAM telegram-purple-tl-parser-format-overflow.patch sor.alexei@meowr.ru -- Fix format overflow in tl-parser.
Patch0:         telegram-purple-tl-parser-format-overflow.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  intltool
BuildRequires:  libgcrypt-devel >= 1.6
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(purple)
BuildRequires:  pkgconfig(zlib)

%description
A Pidgin plugin that adds support for the Telegram messenger.

%package -n libpurple-plugin-telegram
Summary:        Plugin for libpurple for supporting Telegram messager
Group:          Productivity/Networking/Instant Messenger
Recommends:     libpurple-plugin-telegram-lang
Enhances:       libpurple
# telegram-purple was last used in openSUSE Leap 14.2.
Provides:       %{name} = %{version}
Obsoletes:      %{name} < %{version}

%description -n libpurple-plugin-telegram
A libpurple plugin that adds support for the Telegram messenger.

%lang_package -n libpurple-plugin-telegram

%package -n pidgin-plugin-telegram
Summary:        Plugin for Pidgin for supporting Telegram messager
Group:          Productivity/Networking/Instant Messenger
Requires:       libpurple-plugin-telegram = %{version}
%requires_ge    pidgin
Supplements:    packageand(libpurple-plugin-telegram:pidgin)
BuildArch:      noarch

%description -n pidgin-plugin-telegram
A Pidgin plugin that adds support for the Telegram messenger.

This package provides the icon set for Pidgin.

%prep
%setup -q -n %{name}
%patch0 -p1

%build
autoreconf -fi
%configure
make %{?_smp_mflags} V=1

%install
%make_install
%find_lang telegram-purple

%files -n libpurple-plugin-telegram
%license COPYING
%doc AUTHORS CHANGELOG.md README.md
%config %{_sysconfdir}/telegram-purple/
%{_libdir}/purple-2/telegram-purple.so
%dir %{_datadir}/appdata/
%{_datadir}/appdata/telegram-purple.metainfo.xml

%files -n libpurple-plugin-telegram-lang -f telegram-purple.lang

%files -n pidgin-plugin-telegram
%dir %{_datadir}/pixmaps/pidgin/
%dir %{_datadir}/pixmaps/pidgin/protocols/
%dir %{_datadir}/pixmaps/pidgin/protocols/*/
%{_datadir}/pixmaps/pidgin/protocols/*/telegram.*

%changelog
