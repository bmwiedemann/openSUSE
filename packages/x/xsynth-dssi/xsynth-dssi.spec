#
# spec file for package xsynth-dssi
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


Name:           xsynth-dssi
BuildRequires:  alsa-devel
BuildRequires:  cairo-devel
BuildRequires:  dssi-devel
BuildRequires:  gtk2-devel
BuildRequires:  libjack-devel
BuildRequires:  liblo-devel
BuildRequires:  update-desktop-files
Requires:       dssi
Summary:        Xsynth an analog-style (VCAs-VCF-VCO) synth plugin
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Sound/Midi
Version:        0.9.4
Release:        0
Url:            http://www.smbolton.com/linux.html
Source:         %{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The xsynth-dssi  package contains the Xsynth-DSSI plugin,
a classic-analog (VCOs-VCF-VCA) style software synthesizer
with an editor GUI. Xsynth-DSSI was written by Sean Bolton,
and was based on Steve Brooke's Xsynth code, but has since
aquired polyphonic operation, band-limited oscillators,
a better filter mode, and velocity-sensitive envelopes.

Author:
--------
    Sean Bolton <sean@smbolton.com>

%prep
%setup

%build
CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing -fPIC" \
%configure  --with-pic --libdir=%{_libdir}
make

%install
%makeinstall

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
[ "$RPM_BUILD_ROOT" != "/" -a -d $RPM_BUILD_ROOT ] && rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%license COPYING
%{_libdir}/dssi
%doc README ChangeLog TODO
%{_datadir}/%{name}/

%changelog
