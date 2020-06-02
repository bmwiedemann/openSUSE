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
Version:        1.2.2
Release:        0
Summary:        ALSA UCM Profiles
License:        BSD-3-Clause
Url:            http://www.alsa-project.org/
Source:         ftp://ftp.alsa-project.org/pub/lib/alsa-ucm-conf-%{version}.tar.bz2
Patch1:         0001-sof-bdw-rt5677-initial-port-to-UCM2.patch
Patch2:         0002-ucm2-treewide-JackHWMute-fixes.patch
Patch3:         0003-sof-hda-dsp-Support-systems-without-integrated-graph.patch
Patch4:         0004-hda-dsp-add-basic-ucm-config.patch
Patch5:         0005-update-README-files.patch
Patch6:         0006-bytcr-rt5651-Fix-dmic-check-in-HiFi-Components.conf.patch
Patch7:         0007-chtrt5645-Add-ASUSTeKCOMPUTERINC.-T100HAN-1.0-symlin.patch
Patch8:         0008-chtrt5645-Add-MEDION-E1239TMD60568-0.1-Wingman.conf-.patch
Patch9:         0009-chtrt5645-Remove-bogus-JackHWMute-settings.patch
Patch10:        0010-sof-hda-dsp-change-Headphones2-to-Mic2.patch
Patch11:        0011-ucm2-remove-empty-enable-disable-sequence-sections.patch
Patch12:        0012-ucm2-fix-indentation-use-tabs.patch
Patch13:        0013-Add-initial-support-for-Realtek-ALC1220-TRX40-mother.patch
Patch14:        0014-ucm2-fix-chtrt5650-configuration-ucm-validator.patch
Patch15:        0015-bytcr-rt5651-fix-the-cfg-mic-in1-cfg-mic-in12-match-.patch
Patch16:        0016-ucm-fix-wrong-If-in-sequence-in-HiFi-dual.conf.patch
Patch100:       0100-ucm2-Add-profile-for-Chromebook-Asus-C300.patch
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
%patch100 -p1

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
