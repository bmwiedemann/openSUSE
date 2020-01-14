#
# spec file for package sof-firmware
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

Name:           sof-firmware
Summary:        Firmware Data Files for SOF Drivers
Version:        1.4.1
Release:        0
License:        BSD-3-Clause
Group:          Hardware/Other
Url:            https://www.sofproject.org/
BuildRequires:  fdupes
Source:         ftp://ftp.alsa-project.org/pub/misc/sof/sof-firmware-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
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
# Jasperlake
Supplements:    modalias(pci:v00008086d000038C8sv*sd*bc*sc*i*)
# Cometlake-LP
Supplements:    modalias(pci:v00008086d000002C8sv*sd*bc*sc*i*)
# Cometlake-H
Supplements:    modalias(pci:v00008086d000006C8sv*sd*bc*sc*i*)
# Tigerlake
Supplements:    modalias(pci:v00008086d0000A0C8sv*sd*bc*sc*i*)
# Elkhartlake
Supplements:    modalias(pci:v00008086d00004B55sv*sd*bc*sc*i*)

%description
Various firmware data files for SOF drivers.

%prep
%setup -q -c

%build

%install
mkdir -p %{buildroot}/lib/firmware/intel/
cp -a usr/lib/firmware/intel/* %{buildroot}/lib/firmware/intel/
rm -f %{buildroot}/lib/firmware/intel/*/LICENCE
mkdir -p %{buildroot}%{_licensedir}/%{name}
install -c -m0644 usr/lib/firmware/intel/sof/LICENCE %{buildroot}%{_licensedir}/%{name}
%fdupes -s %{buildroot}

%files
%defattr(-, root, root)
%license  %{_licensedir}/%{name}
/lib/firmware/*

%changelog
