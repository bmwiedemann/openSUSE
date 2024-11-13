#
# spec file for package switchboard-plug-sound
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


%define         appid io.elementary.settings.sound
Name:           switchboard-plug-sound
Version:        8.0.0
Release:        0
Summary:        Sound plug for Switchboard
License:        GPL-3.0-or-later
URL:            https://github.com/elementary/switchboard-plug-sound
Source0:        %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  vala
BuildRequires:  pkgconfig(granite-7)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(switchboard-3)
Requires:       switchboard

%description
This plug allow to set the audio and microphone volume and several
sound-related settings.

%lang_package

%prep
%autosetup

%build
export CFLAGS="-Wincompatible-pointer-types"
%meson
%meson_build

%install
%meson_install
%fdupes %{buildroot}%{_datadir}
%find_lang %{appid}

%files
%license COPYING
%doc README.md
%dir %{_libdir}/{switchboard-3,switchboard-3/system}
%{_libdir}/switchboard-3/system/lib%{appid}.so
%{_datadir}/glib-2.0/schemas/sound.gschema.xml
%{_datadir}/metainfo/%{appid}.metainfo.xml

%files lang -f %{appid}.lang

%changelog
