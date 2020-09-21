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
License:        BSD-3-Clause
Group:          Hardware/Other
Version:        1.5.1
Release:        0
URL:            https://github.com/thesofproject/sof-bin
BuildRequires:  fdupes
# Created via git-archive manually from the git repo above with the tag;
# Unforutnately the upstream repo doesn't contain the releases.
# Note that this doesn't contain sources; the unsigned firmware can be built
# from SOF sources with external toolchains, but we need signed firmware from
# Intel, and hence the repo above collects the resultant binaries.
Source:         sof-bin-%{version}.tar.xz
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

%description
Various firmware data files for SOF drivers.

%prep
%setup -q -n sof-bin
# drop version number from sof-tplg directory
mv lib/firmware/intel/sof-tplg-v%{version} lib/firmware/intel/sof-tplg

%build

%install
mkdir -p %{buildroot}/lib/firmware/intel/
cp -a lib/firmware/intel/* %{buildroot}/lib/firmware/intel/
# create symlinks
(cd %{buildroot}/lib/firmware/intel/sof
for i in v%{version}/intel-signed/*.ri v%{version}/*.ri; do
    f=${i%%-v%{version}.ri}
    f=${f##*/}
    ln -s $i $f.ri
done

# fix up the missing firmware for Commet Lake and Coffee Lake
test -f sof-cml.ri || ln -s sof-cnl.ri sof-cml.ri
test -f sof-cfl.ri || ln -s sof-cnl.ri sof-cfl.ri

mkdir -p debug
cd debug
for i in ../v%{version}/*.ldc; do
    f=${i%%-v%{version}.ldc}
    f=${f##*/}
    ln -s $i $f.ldc
done
)
%fdupes -s %{buildroot}

%files
%license LICENCE.*
%doc README.*
/lib/firmware/*

%changelog
