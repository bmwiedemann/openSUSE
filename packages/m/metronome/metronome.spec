#
# spec file for package metronome
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


%define         appid com.github.artemanufrij.metronome
Name:           metronome
Version:        1.0.0
Release:        0
Summary:        Audible beat generator
License:        GPL-3.0-or-later
URL:            https://github.com/artemanufrij/metronome
Source:         %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  meson >= 0.40.0
BuildRequires:  pkgconfig
BuildRequires:  vala
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)

%description
A program for the Pantheon Desktop, that produces an audible beat — a click
or other sound — at regular intervals that the user can set in beats
per minute (BPM).

%lang_package

%prep
%autosetup

mv debian/copyright COPYING

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name}
%fdupes %{buildroot}

%files
%license COPYING
%doc README.md
%{_bindir}/%{appid}
%{_datadir}/applications/%{appid}.desktop
%{_datadir}/%{appid}
%{_datadir}/glib-2.0/schemas/org.pantheon.metronome.gschema.xml
%{_datadir}/icons/hicolor/*/apps/%{appid}.svg
%{_datadir}/metainfo/%{appid}.appdata.xml

%files lang -f %{name}.lang

%changelog
