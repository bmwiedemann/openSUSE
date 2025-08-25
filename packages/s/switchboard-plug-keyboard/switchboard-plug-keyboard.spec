#
# spec file for package switchboard-plug-keyboard
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%define         appid io.elementary.settings.keyboard
Name:           switchboard-plug-keyboard
Version:        8.1.0
Release:        0
Summary:        Switchboard Keyboard Plug
License:        GPL-3.0-or-later
URL:            https://github.com/elementary/switchboard-plug-keyboard
Source0:        %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  vala
BuildRequires:  pkgconfig(granite-7)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(ibus-1.0)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libgnomekbd)
BuildRequires:  pkgconfig(libgnomekbdui)
BuildRequires:  pkgconfig(libxklavier)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(switchboard-3)
Requires:       switchboard

%description
Adjust keyboard settings from Switchboard. This plug can be used to change
several keyboard settings, for example the delay and speed of the key
repetition, or the cursor blinking speed. You can change your keyboard
layout, and use multiple layouts at the same time. Keyboard shortcuts are
also part of this plug.

%lang_package

%prep
%autosetup -n settings-keyboard-%{version}

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{appid}
%fdupes %{buildroot}%{_datadir}

%files
%license COPYING
%doc README.md
%dir %{_libdir}/{switchboard-3,switchboard-3/hardware}
%{_libdir}/switchboard-3/hardware/libkeyboard.so
%{_datadir}/metainfo/%{appid}.metainfo.xml
%{_datadir}/glib-2.0/schemas/%{appid}.gschema.xml

%files lang -f %{appid}.lang

%changelog
