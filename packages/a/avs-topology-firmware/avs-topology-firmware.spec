#
# spec file for package avs-topology-firmware
#
# Copyright (c) 2024 SUSE LLC
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

%define pkgname avs-topology

Name:           avs-topology-firmware
Summary:        Firmware files for ASoC AVS drivers
License:        Apache-2.0
Group:          Hardware/Other
Version:        2024.02
Release:        0
URL:            https://github.com/thesofproject/avs-topology-xml/
Requires(post): coreutils
Source:         https://github.com/thesofproject/avs-topology-xml/releases/download/v2024.02/%{pkgname}_%{version}.tar.gz
BuildArch:      noarch
# info from snd-soc-avs driver
Supplements:    modalias(pci:v00008086d00003198sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d00005A98sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d00009D70sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d00009D71sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d0000A170sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d0000A171sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d0000A2F0sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d0000A3F0sv*sd*bc*sc*i*)

%description
Firmware data files for ASoC AVS sound driver.

%prep
%setup -q -n %{pkgname}

%build

%install
mkdir -p %{buildroot}%{_firmwaredir}
cp -a lib/firmware/* %{buildroot}%{_firmwaredir}/

%post
%{?regenerate_initrd_post}

%postun
%{?regenerate_initrd_post}

%posttrans
%{?regenerate_initrd_posttrans}

%files
%license LICENSE
%{_firmwaredir}/*

%changelog
