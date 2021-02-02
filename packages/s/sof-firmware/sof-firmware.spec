#
# spec file for package sof-firmware
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


%define repo_version 1.6.1
%define package_version	1.6.1

%if 0%{?suse_version} < 1550
%define _firmwaredir /lib/firmware
%endif

Name:           sof-firmware
Summary:        Firmware Data Files for SOF Drivers
License:        BSD-3-Clause
Group:          Hardware/Other
Version:        1.6.1
Release:        0
URL:            https://github.com/thesofproject/sof-bin
BuildRequires:  fdupes
Source:         https://github.com/thesofproject/sof-bin/archive/v%{package_version}.tar.gz#/sof-bin-%{package_version}.tar.gz
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
# Broadwell
Supplements:    modalias(acpi*:INT3438:*)
# Baytrail
Supplements:    modalias(acpi*:80860F28:*)
Supplements:    modalias(acpi*:808622A8:*)

%description
Various firmware data files for SOF drivers.

%prep
%setup -q -n sof-bin-%{package_version}

%build

%install
mkdir -p %{buildroot}%{_firmwaredir}
ROOT=%{buildroot} SOF_VERSION=v%{repo_version} sh ./go.sh
# drop broken links
rm -f %{buildroot}%{_firmwaredir}/intel/sof/sof-jsl.ri
rm -f %{buildroot}%{_firmwaredir}/intel/sof/community/sof-jsl.ri
%fdupes -s %{buildroot}

# A grand opening of a monkey theater now:
# as rpm cannot handle the transition from a directory to a symlinked
# directory, we need many very ugly tricks to work around it.
# See bsc#1180287 and bsc#1181554

# At first, rename the old directory that will be overriden via symlink.
# This has to be done at pre, not preun.  Without this workaround, cpio
# expansion fails.
%pre
if test -d %{_firmwaredir}/intel/sof-tplg; then
  if ! test -h %{_firmwaredir}/intel/sof-tplg; then
    mv %{_firmwaredir}/intel/sof-tplg %{_firmwaredir}/intel/sof-tplg.old
  fi
fi

# At next, rename the symlink at post if the old package contained the
# directory; it's needed to avoid the old package removing the new contents
# mistakenly.  The old contents are removed here instead.
%post
if test -d %{_firmwaredir}/intel/sof-tplg.old; then
  mv %{_firmwaredir}/intel/sof-tplg %{_firmwaredir}/intel/sof-tplg.new
  rm -rf %{_firmwaredir}/intel/sof-tplg.old
fi

# At last in posttrans, recover the symlink again;
# it's the only place we can use after the old package triggers run
%posttrans
if test -h %{_firmwaredir}/intel/sof-tplg.new; then
  mv %{_firmwaredir}/intel/sof-tplg.new %{_firmwaredir}/intel/sof-tplg
  # remove stale files
  rm -f %{_firmwaredir}/intel/sof-tplg\;*
fi

%files
%license LICENCE.*
%doc README.*
%{_firmwaredir}/*

%changelog
