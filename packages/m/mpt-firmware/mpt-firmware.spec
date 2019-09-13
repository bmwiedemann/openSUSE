#
# spec file for package mpt-firmware
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define _udevrulesdir %(pkg-config --variable=udevdir udev)/rules.d
Name:           mpt-firmware
Version:        1.0
Release:        0
Summary:        Configuration files for autoloading mptctl at boot time
License:        GPL-2.0+
Group:          Hardware/Other
Source0:        mptctl.rules
Source3:        update-pci-id-list.sh
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(udev) > 176
Requires:       modutils
# Module: mptspi.ko
Supplements:    modalias(pci:v00001000d00000030sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v0000117Cd00000030sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001000d00000040sv*sd*bc*sc*i*)
# Module: mptsas.ko
Supplements:    modalias(pci:v00001000d00000050sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001000d00000054sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001000d00000056sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001000d00000058sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001000d00000059sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001000d00000062sv*sd*bc*sc*i*)
# Module: mptfc.ko
Supplements:    modalias(pci:v00001000d00000621sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001000d00000622sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001000d00000624sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001000d00000626sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001000d00000628sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001000d00000640sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001000d00000642sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001000d00000646sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001657d00000646sv*sd*bc*sc*i*)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%prep

%build
# There is nothing to build

%install
install -D -m644 %{SOURCE0} %{buildroot}%{_udevrulesdir}/81-mptctl.rules

%description
This package contains modprobe configuration files to autoload the
mptctl ioctl driver at boot time. The mptctl driver is an ioctl
character driver for the LSI Logic Fusion-MPT Host adapter series.
These adapters include

- Ultra320 53C1030, 53C1020

- Fiber Channel FC909, FC919, FC929, FC919X and FC929X

- SAS SAS1064, and SAS1068

%files
%defattr(-,root,root)
%{_udevrulesdir}/81-mptctl.rules

%changelog
