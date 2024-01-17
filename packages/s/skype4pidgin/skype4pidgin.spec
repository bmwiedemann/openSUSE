#
# spec file for package skype4pidgin
#
# Copyright (c) 2022 SUSE LLC
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


Name:           skype4pidgin
Version:        1.7
Release:        0
Summary:        Libpurple plugin for SkypeWeb API
License:        GPL-3.0-or-later
Group:          Productivity/Networking/Instant Messenger
URL:            https://eion.robbmob.com/
Source:         https://github.com/EionRobb/skype4pidgin/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# For directory ownership.
BuildRequires:  pidgin
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(purple)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(zlib)

%description
This is a SkypeWeb Plugin for libpurple/Pidgin. It lets you view
and chat with all your Skype buddies from within Pidgin.

%package -n libpurple-plugin-skypeweb
Summary:        Libpurple plugin for SkypeWeb API
Group:          Productivity/Networking/Instant Messenger
Enhances:       libpurple
# libpurple-plugin-skype was last used in openSUSE Leap 15.0.
Obsoletes:      libpurple-plugin-skype < %{version}
Obsoletes:      libpurple-plugin-skype-lang < %{version}

%description -n libpurple-plugin-skypeweb
This is a SkypeWeb Plugin for libpurple. It lets you view and chat
with all your Skype buddies from within Pidgin.

%package -n pidgin-plugin-skypeweb
Summary:        Pidgin plugin for SkypeWeb API
Group:          Productivity/Networking/Instant Messenger
Requires:       libpurple-plugin-skypeweb = %{version}
%requires_ge    pidgin
Enhances:       pidgin
Supplements:    packageand(libpurple-plugin-skypeweb:pidgin}
# pidgin-plugin-skype was last used in openSUSE Leap 15.0.
Obsoletes:      pidgin-plugin-skype < %{version}

%description -n pidgin-plugin-skypeweb
This is a SkypeWeb Plugin for Pidgin. It lets you view and chat
with all your Skype buddies from within Pidgin.

%prep
%setup -q

%build
%make_build -C skypeweb

%install
%make_install -C skypeweb

%files -n libpurple-plugin-skypeweb
%license skypeweb/gpl3.txt
%doc skypeweb/README.md
%{_libdir}/purple-2/libskypeweb.so

%files -n pidgin-plugin-skypeweb
%{_datadir}/pixmaps/pidgin/protocols/*/skype.png
%{_datadir}/pixmaps/pidgin/protocols/*/skypeout.png
%{_datadir}/pixmaps/pidgin/emotes/skype/

%changelog
