#
# spec file for package awesfx
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           awesfx
Version:        0.5.2
Release:        0
Summary:        SoundFont Utilities for SB AWE32/64 and Emu10k1 Drivers
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Sound/Midi
Url:            https://github.com/tiwai/awesfx
Source:         awesfx-%{version}.tar.gz
Patch:          awesfx-0.5.1e-fix-bashisms.patch
BuildRequires:  alsa-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(udev)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%define _udevrulesdir %(pkg-config --variable=udevdir udev)/rules.d

%description
The AWESFX package includes utility programs for controlling the
wavetable function on SB AWE32/64 and Emu10k1 sound cards.

%prep
%setup -q
%patch -p1

%build
autoreconf -fi
CFLAGS="%{optflags} -fno-strict-aliasing" \
%configure
make %{?_smp_mflags}

%install
%make_install
# install udev and helper scripts
mkdir -p %{buildroot}%{_udevrulesdir}
install -c -m 0644 etc/*.rules %{buildroot}%{_udevrulesdir}
mkdir -p %{buildroot}%{_sysconfdir}/alsa.d
install -c -m 0755 etc/load-soundfont %{buildroot}%{_sysconfdir}/alsa.d
install -c -m 0755 etc/udev-soundfont %{buildroot}%{_sysconfdir}/alsa.d

%files
%defattr(-,root,root)
%doc AUTHORS COPYING README ChangeLog
%doc *.txt
%{_bindir}/*
%{_datadir}/sounds/sf2/
%doc %{_mandir}/*/*
%{_udevrulesdir}/*.rules
%{_sysconfdir}/alsa.d

%changelog
