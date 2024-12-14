#
# spec file for package paprefs
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


Name:           paprefs
Version:        1.2
Release:        0
Summary:        PulseAudio Preferences
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Sound/Utilities
URL:            https://freedesktop.org/software/pulseaudio/paprefs
Source0:        %{url}/%{name}-%{version}.tar.xz

BuildRequires:  c++_compiler
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(giomm-2.4) >= 2.26
BuildRequires:  pkgconfig(gtkmm-3.0)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(sigc++-2.0)
Requires:       pulseaudio-module-gsettings

%description
PulseAudio Preferences (paprefs) is a simple GTK based configuration
dialog for the PulseAudio sound server.

Please note that this program can only configure local servers, and
requires that a special module module-gconf is loaded in the sound
server.

%lang_package

%prep
%autosetup -p1

%build
sed -i 's@Icon=.*@Icon=audio-speakers@' src/paprefs.desktop.in
%meson
%meson_build

%install
%meson_install
%find_lang %{name} %{?no_lang_C}

%files
%license LICENSE
%{_bindir}/*
%{_datadir}/paprefs
%{_datadir}/applications/*.desktop

%files lang -f %{name}.lang

%changelog
