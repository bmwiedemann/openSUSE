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

Name:           sof-firmware
Summary:        Firmware data files for SOF Drivers
License:        BSD-3-Clause
Group:          Hardware/Other
Version:        2023.09
Release:        0
URL:            https://www.sofproject.org/
BuildRequires:  fdupes
Source:         https://github.com/thesofproject/sof-bin/releases/download/v%{version}/sof-bin-%{version}.tar.gz
Patch1:         install-use-cp.patch
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
Supplements:    modalias(pci:v00008086d000051C9sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d000051CCsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d000051CDsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d000054C8sv*sd*bc*sc*i*)
# Raptorlake
Supplements:    modalias(pci:v00008086d00007A50sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d000051CAsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d000051CBsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d000051CEsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d000051CFsv*sd*bc*sc*i*)
# Metorlake
Supplements:    modalias(pci:v00008086d00007E28sv*sd*bc*sc*i*)
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
Firmware data files for Sound Open Firmware (SOF) drivers.

%prep
%setup -q -n sof-bin-%{version}
%patch1 -p1

%build

%install
mkdir -p %{buildroot}%{_firmwaredir}/intel
mkdir -p %{buildroot}%{_bindir}
FW_DEST=%{buildroot}%{_firmwaredir}/intel \
TOOLS_DEST=%{buildroot}%{_bindir} \
./install.sh
rm -rf %{buildroot}%{_bindir}
%fdupes -s %{buildroot}

# workaround for changing symlinked directory
%pre
if [ -L %{_firmwaredir}/intel/sof-tplg ]; then
  f=$(readlink -f %{_firmwaredir}/intel/sof-tplg)
  case $f in
    %{_firmwaredir}/intel/*)
      rm -rf $f
      rm -f %{_firmwaredir}/intel/sof-tplg;;
  esac
fi

%post
%{?regenerate_initrd_post}

%postun
%{?regenerate_initrd_post}

%posttrans
%{?regenerate_initrd_posttrans}

%files
%license LICENCE.* Notice.NXP
%doc README.*
%{_firmwaredir}/*

%changelog
