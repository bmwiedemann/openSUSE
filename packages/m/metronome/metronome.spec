#
# spec file for package metronome
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


Name:           metronome
Version:        1.0.0
Release:        0
Summary:        Audible beat generator
License:        GPL-3.0-or-later
Group:          Productivity/Multimedia/Other
URL:            https://github.com/artemanufrij/metronome
Source:         https://github.com/artemanufrij/metronome/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  meson >= 0.40.0
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  vala
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
Recommends:     %{name}-lang

%description
A program for Elementary OS that produces an audible beat — a click
or other sound — at regular intervals that the user can set in beats
per minute (BPM).

%lang_package

%prep
%setup -q

mv debian/copyright COPYING

%build
%meson
%meson_build

%install
%meson_install
%suse_update_desktop_file -r com.github.artemanufrij.metronome GTK AudioVideo Sequencer
%find_lang metronome %{name}.lang
%fdupes %{buildroot}%{_datadir}

%files
%license COPYING
%doc README.md
%{_bindir}/com.github.artemanufrij.metronome
%{_datadir}/applications/com.github.artemanufrij.metronome.desktop
%{_datadir}/com.github.artemanufrij.metronome
%{_datadir}/glib-2.0/schemas/org.pantheon.metronome.gschema.xml
%{_datadir}/icons/hicolor/*/*/com.github.artemanufrij.metronome.??g
%{_datadir}/metainfo/com.github.artemanufrij.metronome.appdata.xml

%files lang -f %{name}.lang

%changelog
