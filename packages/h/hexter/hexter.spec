#
# spec file for package hexter
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


Name:           hexter
Version:        1.1.1
Release:        0
Summary:        A Yamaha DX7 software synthesizer for DSSI
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Sound/Midi
URL:            https://github.com/smbolton/hexter
Source0:        %{URL}/releases/download/version_%{version}/hexter-%{version}.tar.bz2
BuildRequires:  alsa-devel
BuildRequires:  dssi-devel
BuildRequires:  gtk2-devel
BuildRequires:  ladspa-devel
BuildRequires:  libjack-devel
BuildRequires:  liblo-devel
BuildRequires:  pkgconfig
Requires:       dssi

%description
Hexter is a software synthesizer that models the sound generation of
a Yamaha DX7 synthesizer.  It can easily load most DX7 patch bank
files, edit those patches via a built-in editor or MIDI sys-ex
messages (ALSA systems only), and recreate the sound of the DX7 with
greater accuracy than any previous open-source emulation (that the
author is aware of....)

Hexter operates as a plugin for the DSSI Soft Synth Interface. DSSI
is a plugin API for software instruments (soft synths) with user
interfaces, permitting them to be hosted in-process by audio
applications.

%prep
%setup -q

%build
%configure
%make_build

%install
%make_install
find . %{buildroot} -name "*.la" -print -delete

%files
%license COPYING
%doc AUTHORS ChangeLog README.rst TODO
%dir %{_libdir}/dssi
%{_libdir}/dssi/hexter.so
%{_libdir}/dssi/hexter*
%{_datadir}/%{name}

%changelog
