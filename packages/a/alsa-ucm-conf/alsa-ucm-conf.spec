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
