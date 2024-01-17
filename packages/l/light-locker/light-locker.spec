#
# spec file for package light-locker
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


Name:           light-locker
Version:        1.9.0
Release:        0
Summary:        A simple locker using LightDM
License:        GPL-2.0-or-later
URL:            https://github.com/the-cavalry/light-locker
Source:         https://github.com/the-cavalry/light-locker/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  intltool
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(dbus-glib-1) >= 0.30
BuildRequires:  pkgconfig(gobject-2.0) >= 2.25.6
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libsystemd) >= 209
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xscrnsaver)
BuildRequires:  pkgconfig(xxf86vm)
Requires:       lightdm >= 1.7.10
Recommends:     %{name}-lang
%glib2_gsettings_schema_requires

%description
light-locker is a simple locker that aims to have simple, sane, secure
defaults and be well integrated with the desktop while not carrying any
desktop-specific dependencies.
It relies on LightDM for locking and unlocking your session via systemd.

%lang_package

%prep
%setup -q

[ $(readlink README) != README.md ]
rm README && ln -s README.md README

%build
%meson \
  -Ddpms-ext=true      \
  -Dmit-ext=true       \
  -Dxf86gamma-ext=true
%meson_build

%install
%meson_install
%find_lang %{name}

%files
%license COPYING
%doc AUTHORS NEWS README.md
%{_bindir}/%{name}
%{_bindir}/%{name}-command
%{_datadir}/glib-2.0/schemas/*%{name}.gschema.xml
%{_sysconfdir}/xdg/autostart/%{name}.desktop
%{_mandir}/man?/%{name}*.?%{?ext_man}

%files lang -f %{name}.lang

%changelog
