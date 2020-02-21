#
# spec file for package alsa-ucm-conf
#
# Copyright (c) 2020 SUSE LINUX GmbH, Nuernberg, Germany.
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
Version:        1.2.1.2
Release:        0
Summary:        ALSA UCM Profiles
License:        BSD-3-Clause
Url:            http://www.alsa-project.org/
Source:         ftp://ftp.alsa-project.org/pub/lib/alsa-ucm-conf-%{version}.tar.bz2
Patch1:         0001-sof-hda-dsp-Fix-the-Dmic0-CaptureMixerElem-for-v1.4..patch
Patch2:         0002-sof-hda-dsp-Use-more-strict-names-according-latest-u.patch
Patch3:         0003-README-remove-topologies-note.patch
Patch4:         0004-bytcht-es8316-Fix-missing-including-of-HeadPhones.co.patch
Patch5:         0005-ucm2-fix-the-verb-path-in-chtrt5645-chtrt5645-dmic2..patch
Patch6:         0006-broadwell-rt286-add-support-for-hardware-volume-conf.patch
Patch7:         0007-broxton-rt298-corrections-cleanups.patch
Patch8:         0008-bytcr-rt5640-cleanups-and-corrections.patch
Patch9:         0009-bytcr-rt5651-cleanups-and-corrections.patch
Patch10:        0010-bytcht-cx2072x-cleanups-and-corrections.patch
Patch11:        0011-bytcht-es8316-cleanups-and-corrections.patch
Patch12:        0012-DAISY-I2S-added-back-PCM-devices.patch
Patch13:        0013-DB410c-cleanups-and-corrections.patch
Patch14:        0014-DB820c-cleanups-and-corrections.patch
Patch15:        0015-Dell-WD15-Dock-cleaups-and-corrections.patch
Patch16:        0016-HDA-Intel-HiFi-dual-fixes-and-corrections.patch
Patch17:        0017-cht-bsw-rt5672-fixes-and-corrections.patch
Patch18:        0018-chtnau8824-fixes-and-corrections.patch
Patch19:        0019-skylake-rt286-fixes-and-corrections.patch
Patch20:        0020-SDP4430-corrections-and-fixes.patch
Patch21:        0021-sof-hda-dsp-fix-typo-PlaybackMixerMaster-PlaybackMas.patch
Patch22:        0022-broadwell-rt286-add-correct-prefix-to-Priority-field.patch
Patch23:        0023-GoogleNyan-comment-CaptureControl-what-is-this.patch
Patch24:        0024-VEYRON-I2S-corrections-and-fixes.patch
Patch25:        0025-SDP4430-corrections-and-fixes.patch
Patch26:        0026-chtrt5645-corrections-and-fixes.patch
Patch27:        0027-GoogleNyan-corrections-and-fixes.patch
Patch28:        0028-PAZ00-corrections-and-fixes.patch
Patch29:        0029-SDP4430-corrections-and-fixes.patch
Patch30:        0030-PandaBoard-corrections-and-fixes.patch
Patch31:        0031-PandaBoardES-corrections-and-fixes.patch
Patch32:        0032-kblrt5660-corrections-and-fixes.patch
Patch33:        0033-bytcr-rt5640-corrections-and-fixes.patch
Patch34:        0034-bytcht-es8316-corrections-and-fixes.patch
Patch35:        0035-sof-hda-dsp-corrections-and-fixes.patch
Patch36:        0036-ucm2-treewide-remove-Playback-and-Capture-channels-2.patch
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This package contains the profiles files for ALSA UCM (Use Case Manager).

%prep
%setup -q -c -a0
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
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch28 -p1
%patch29 -p1
%patch30 -p1
%patch31 -p1
%patch32 -p1
%patch33 -p1
%patch34 -p1
%patch35 -p1
%patch36 -p1

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
