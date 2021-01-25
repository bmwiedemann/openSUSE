#
# spec file for package alsa-ucm-conf
#
# Copyright (c) 2021 SUSE LLC
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
BuildRequires:  fdupes
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
Patch10:        0010-HDA-Intel-HiFi-dual-Add-EnableSequence-and-DisableSe.patch
Patch11:        0011-HDA-Intel-HiFi-dual-Add-BootSequence-and-disable-pla.patch
Patch12:        0012-chtrt5645-Enable-Internal-MIC-of-ECS-EF20EA.patch
Patch13:        0013-bytcr-rt5640-Add-support-for-devices-without-speaker.patch
Patch14:        0014-rt5640-Move-standard-DAC-setup-to-EnableSeq.conf.patch
Patch15:        0015-bytcr-rt5640-fix-the-execution-order.patch
Patch16:        0016-ucm2-add-initial-configuration-for-TRX40-Gigabyte-Ao.patch
Patch17:        0017-USB-Audio-ALC1220-Bump-analog-Speaker-priority-over-.patch
Patch18:        0018-USB-Audio-ALC1220-fix-indentation-for-Speaker-device.patch
Patch19:        0019-USB-Audio-fix-indentation-in-Gigabyte-Aorus-Master-M.patch
Patch20:        0020-chtnau8824-Add-a-SST-define-variable.patch
Patch21:        0021-kblrt5660-Fix-file-permissions.patch
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
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1

%build

%install
mkdir -p %{buildroot}%{_datadir}/alsa
cp -a ucm %{buildroot}%{_datadir}/alsa/
cp -a ucm2 %{buildroot}%{_datadir}/alsa/
%fdupes -s %{buildroot}

%files
%defattr(-, root, root)
%doc README.md
%license LICENSE
%{_datadir}/alsa

%changelog
