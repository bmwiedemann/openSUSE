#
# spec file for package sof-firmware
#
# Copyright (c) 2023 SUSE LLC
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


%if 0%{?suse_version} < 1550
%define _firmwaredir /lib/firmware
%endif

%define sofversion  2.2.4
%define tplgversion 2.2.4

Name:           sof-firmware
Summary:        Firmware Data Files for SOF Drivers
License:        BSD-3-Clause
Group:          Hardware/Other
Version:        2.2.4
Release:        0
URL:            https://github.com/thesofproject/sof-bin
BuildRequires:  fdupes
Source:         https://github.com/thesofproject/sof-bin/releases/download/v%{sofversion}/sof-bin-v%{sofversion}.tar.gz
BuildArch:      noarch
# Merrifield
Supplements:    modalias(pci:v00008086d0000119Asv*sd*bc*sc*i*)
# Apollolake
Supplements:    modalias(pci:v00008086d00005A98sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d00001A98sv*sd*bc*sc*i*)
# Geminilake
Supplements:    modalias(pci:v00008086d00003198sv*sd*bc*sc*i*)
# Cannonlake
Supplements:    modalias(pci:v00008086d00009DC8sv*sd*bc*sc*i*)
# Coffeelake
Supplements:    modalias(pci:v00008086d0000A348sv*sd*bc*sc*i*)
# Icelake
Supplements:    modalias(pci:v00008086d000034C8sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d00003DC8sv*sd*bc*sc*i*)
# Jasperlake
Supplements:    modalias(pci:v00008086d000038C8sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d00004DC8sv*sd*bc*sc*i*)
# Cometlake
Supplements:    modalias(pci:v00008086d000002C8sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d000006C8sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d0000A3F0sv*sd*bc*sc*i*)
# Tigerlake
Supplements:    modalias(pci:v00008086d0000A0C8sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d000043C8sv*sd*bc*sc*i*)
# Elkhartlake
Supplements:    modalias(pci:v00008086d00004B55sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d00004B58sv*sd*bc*sc*i*)
# Alderlake
Supplements:    modalias(pci:v00008086d00007AD0sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d000051C8sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d000051CCsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d000054C8sv*sd*bc*sc*i*)
# Broadwell
Supplements:    modalias(acpi*:INT3438%3A*)
# Baytrail
Supplements:    modalias(acpi*:80860F28%3A*)
Supplements:    modalias(acpi*:808622A8%3A*)
%if 0%{?suse_version} >= 1550
# make sure we have post-usrmerge filesystem package on TW
Conflicts:      filesystem < 84
%endif

%description
Various firmware data files for SOF drivers.

%prep
%setup -q -n sof-bin-v%{sofversion}

%build

%install
mkdir -p %{buildroot}%{_firmwaredir}/intel
# due to the upgrade problem, we can't make sof-v* -> sof symlink
cp -a sof-v%{sofversion} %{buildroot}%{_firmwaredir}/intel/sof
cp -a sof-tplg-v%{tplgversion} %{buildroot}%{_firmwaredir}/intel/
ln -s sof-tplg-v%{tplgversion} %{buildroot}%{_firmwaredir}/intel/sof-tplg
%fdupes -s %{buildroot}

%files
%license LICENCE.*
%doc README.*
%{_firmwaredir}/*

%changelog
