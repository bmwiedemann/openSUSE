#
# spec file for package decibels
#
# Copyright (c) 2023 SUSE LLC
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

%define lname   com.vixalien.decibels
%define sname   gi-typescript-definitions
%define scommit eb2a87a25c5e2fb580b605fbec0bd312fe34c492
Name:           decibels
Version:        0.1.4
Release:        0
Summary:        Play audio files with a waveform
License:        GPL-3.0-or-later
URL:            https://github.com/vixalien/decibels
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        https://gitlab.gnome.org/BrainBlasted/%{sname}/-/archive/%{scommit}/%{sname}-%{scommit}.tar.bz2
BuildRequires:  appstream-glib
BuildRequires:  desktop-file-utils
BuildRequires:  hicolor-icon-theme
BuildRequires:  meson
BuildRequires:  typescript
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gjs-1.0)
BuildRequires:  pkgconfig(gtk4)
Requires:       typelib(GstPlay)
Provides:       bundled(gi-types)
BuildArch:      noarch

%description
App that lets you play audio files. 
It has a modern and adaptive interface, with a waveform, simple playback controls, 
and the ability to control the speed at which the audio is played.

%lang_package

%prep
%setup -q
tar -xf %{SOURCE1} --strip-components 1 -C gi-types

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name}

%files
%license LICENCE
%doc README*
%{_bindir}/%{lname}
%dir %{_datadir}/%{lname}
%{_datadir}/%{lname}/%{lname}*
%{_datadir}/applications/%{lname}.desktop
%{_datadir}/icons/hicolor/*/*/%{lname}*
%{_datadir}/metainfo/%{lname}.metainfo.xml
%{_datadir}/glib-2.0/schemas/%{lname}.gschema.xml
%{_datadir}/dbus-1/services/%{lname}.service

%files lang -f %{name}.lang

%changelog

