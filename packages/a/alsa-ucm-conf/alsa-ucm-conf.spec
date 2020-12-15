#
# spec file for package alsa-ucm-conf
#
# Copyright (c) 2020 SUSE LLC
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


Name:           alsa-ucm-conf
Version:        1.2.4
Release:        0
Summary:        ALSA UCM Profiles
License:        BSD-3-Clause
URL:            http://www.alsa-project.org/
Source:         ftp://ftp.alsa-project.org/pub/lib/alsa-ucm-conf-%{version}.tar.bz2
Patch1:         0001-fix-the-ucm2-codecs-hda-hdmi.conf-use.patch
Patch2:         0002-codecs-hda-hdmi.conf-add-DisplayPort-to-the-device-d.patch
Patch3:         0003-sof-soundwire-use-the-codecs-hda-hdmi.conf-macro.patch
Patch4:         0004-Revert-ucm2-HDA-acp-add-Capture-simple-mixer-element.patch
Patch5:         0005-chtnau8824-Fix-mono-speaker-config-not-working.patch
Patch6:         0006-chtnau8824-Add-support-for-laptops-using-stereo-DMIC.patch
Patch7:         0007-chtnau8824-Boost-analog-mic-volumes-a-bit.patch
Patch8:         0008-rt715-init-setup-ADC07-to-a-proper-volume.patch
Patch9:         0009-sof-hda-dsp-Set-Master-Playback-Switch-on-in-the-Boo.patch
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This package contains the profiles files for ALSA UCM (Use Case Manager).

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1

%build

%install
mkdir -p %{buildroot}%{_datadir}/alsa
cp -a ucm %{buildroot}%{_datadir}/alsa/
cp -a ucm2 %{buildroot}%{_datadir}/alsa/

%files
%defattr(-, root, root)
%doc README.md
%license LICENSE
%{_datadir}/alsa

%changelog
