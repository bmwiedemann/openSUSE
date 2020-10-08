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
Version:        1.2.3
Release:        0
Summary:        ALSA UCM Profiles
License:        BSD-3-Clause
Url:            http://www.alsa-project.org/
Source:         ftp://ftp.alsa-project.org/pub/lib/alsa-ucm-conf-%{version}.tar.bz2
Patch1:         0001-bytcr-rt5640-Fix-DMIC1-not-working-when-connected-ov.patch
Patch2:         0002-bytcr-rt5651-Fix-high-noise-level-soft-input-on-DMIC.patch
Patch3:         0003-chtrt5645-Add-ASUSTeKCOMPUTERINC.-T101HA-1.0.conf-sy.patch
Patch4:         0004-sof-hda-dsp-don-t-fail-if-Auto-Mute-control-is-not-p.patch
Patch5:         0005-ucm2-use-Include-Syntax-3.patch
Patch6:         0006-chtrt5645-merge-all-possible-configurations-to-HiFi..patch
Patch7:         0007-cht-bsw-rt5672-merge-all-possible-configurations-to-.patch
Patch8:         0008-chtnau8824-merge-all-possible-configurations-to-HiFi.patch
Patch9:         0009-ucm.conf-add-support-for-the-kernel-module-name-tree.patch
Patch10:        0010-sof-hda-dsp-make-Headphone-Playback-Switch-condition.patch
Patch11:        0011-sof-hda-dsp-add-initial-kcontrol-values.patch
Patch12:        0012-sof-hda-dsp-make-the-boot-init-optional-for-all-cont.patch
Patch13:        0013-bdw-rt5677-add-support-for-legacy-and-SOF-drivers.patch
Patch14:        0014-broadwell-rt286-add-SOF-support.patch
Patch15:        0015-sof-soundwire-initial-UCM2-version.patch
Patch16:        0016-sof-soundwire-cleanups-recommended-by-the-ucm-valida.patch
Patch17:        0017-sof-soundwire-rewrite-for-syntax-3.patch
Patch18:        0018-sof-hda-dsp-fix-the-device-order-Hdmi-devices.patch
Patch19:        0019-HDA-Intel-add-support-for-AMD-acp-microphone-devices.patch
Patch20:        0020-DAISY-I2S-move-to-Samsung-snow-snow.conf.patch
Patch21:        0021-DB410c-move-to-Qualcomm-apq8016-sbc.patch
Patch22:        0022-DB820c-DB845c-move-to-Qualcomm-tree.patch
Patch23:        0023-PAZ00-tegraalc5632-move-to-Tegra-alc5632-tree.patch
Patch24:        0024-VEYRON-I2C-move-to-Rockchip-max98090-tree.patch
Patch25:        0025-Pandaboard-ES-move-to-OMAP-abe-twl6040-tree.patch
Patch26:        0026-GoogleNyan-move-to-Tegra-max98090.patch
Patch27:        0027-SDP4430-Move-to-OMAP-abe-twl6040-SDP4430-tree.patch
Patch28:        0028-Fix-invalid-Regex-Type-in-various-Condition-blocks.patch
Patch29:        0029-cht-bsw-rt5672-Add-Lenovo-Miix-2-10-specific-configu.patch
Patch30:        0030-cht-bsw-rt5672-Add-Lenovo-ThinkPad-10-specific-confi.patch
Patch31:        0031-cht-bsw-rt5672-Boost-ADC-volume-a-bit.patch
Patch32:        0032-chtrt5645-Restore-stereo-sound-output-when-switching.patch
Patch33:        0033-DB820c-Correctly-move-DB820c-to-Qualcomm-apq8096.patch
Patch34:        0034-sof-hda-dsp-fixup-typo-in-Hdmi.conf.patch
Patch35:        0035-sof-hda-dsp-use-sof-hda-dsp-Hdmi.conf.patch
Patch36:        0036-hda-hdmi-add-HDMI4-HDMI5-HDMI6-devices.patch
Patch37:        0037-update-ucm2-README.md-more-kernel-module-lookup-clar.patch
Patch38:        0038-ucm2-Add-config-for-Rockchip-rk3399-gru-sound.patch
Patch39:        0039-amd-renoir-acp-use-the-machine-driver-s-name-for-top.patch
Patch40:        0040-amd-renoir-acp-Add-Syntax-3-in-the-module-lib-Linked.patch
Patch41:        0041-Correct-conflicting-mic-in-max98090.patch
Patch42:        0042-HDA-Intel-HiFi-dual-Fix-the-Rear-Mic-s-Jack-name.patch
Patch43:        0043-USB-Audio-Dell-WD15-Dock-make-input-and-output-volum.patch
Patch44:        0044-Rockchip-rk3399-gru-sound-remove-zero-PCM-subdevice.patch
Patch45:        0045-ucm2-ucm.conf-fix-the-fix-the-sysfs-kernel-module-pa.patch
Patch46:        0046-Revert-amd-renoir-acp-use-the-machine-driver-s-name-.patch
Patch47:        0047-ucm2-module-rename-rk3399-gru-sound.conf-snd_soc_rk3.patch
Patch48:        0048-ucm2-HDA-acp-add-Capture-simple-mixer-element-to-the.patch
Patch49:        0049-HDA-Intel-only-add-the-acp-dmic-to-the-sound-card-wi.patch
Patch50:        0050-Add-support-for-Lenovo-ThinkStation-P620-Main-Audio.patch
Patch51:        0051-ucm2-Qualcomm-sdm845-fixes-HDMI-select-card-and-HiFi.patch
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
%patch37 -p1
%patch38 -p1
%patch39 -p1
%patch40 -p1
%patch41 -p1
%patch42 -p1
%patch43 -p1
%patch44 -p1
%patch45 -p1
%patch46 -p1
%patch47 -p1
%patch48 -p1
%patch49 -p1
%patch50 -p1
%patch51 -p1
#
# workaround for a regression on openQA (muted as default)
#
mv ucm2/HDA-Intel/HDA-Intel.conf ucm2/HDA-Intel/HDA-Intel-broken.conf

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
