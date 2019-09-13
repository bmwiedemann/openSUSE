#
# spec file for package [hexter]
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


# See also http://en.opensuse.org/openSUSE:Specfile_guidelines

Name:           hexter
Version:        1.0.3
Release:        0
Summary:        A Yamaha DX7 software synthesizer for DSSI
License:        GPL-2.0+
Url:            http://dssi.sourceforge.net/hexter.html
Group:          Productivity/Multimedia/Sound/Midi
Source0:        http://downloads.sourceforge.net/project/dssi/hexter/%{version}/%{name}-%{version}.tar.bz2
BuildRequires:  alsa-devel
BuildRequires:  dssi-devel
BuildRequires:  gtk2-devel
BuildRequires:  libjack-devel
BuildRequires:  liblo-devel
BuildRequires:  ladspa-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
Requires:       dssi
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

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
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
find . %{buildroot} -name "*.la" -print -delete

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING README TODO
%dir %{_libdir}/dssi/hexter
%dir %{_datadir}/hexter
%dir %{_libdir}/dssi
%{_libdir}/dssi/hexter.so
%{_libdir}/dssi/hexter/hexter_gtk
%{_datadir}/%{name}/dx7_roms.dx7
%{_datadir}/%{name}/fb01_roms_converted_12.dx7
%{_datadir}/%{name}/fb01_roms_converted_34.dx7
%{_datadir}/%{name}/fb01_roms_converted_5.dx7
%{_datadir}/%{name}/tx7_roms.dx7

%changelog
