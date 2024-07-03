#
# spec file for package adaptec-firmware
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


%{?!_firmwaredir:%define _firmwaredir /lib/firmware}

Name:           adaptec-firmware
Summary:        Firmware files for Adaptec SAS Cards (AIC94xx Series)
License:        SUSE-Firmware
Group:          Hardware/Other
Source0:        aic94xx-seq.fw
Source1:        LICENSE
Version:        1.35
Release:        0
# Install into this non-root directory (required when norootforbuild is used):
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
# Modules: aic94xx.ko
Supplements:    modalias(pci:v00009005d00000410sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00009005d00000412sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00009005d0000041Esv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00009005d0000041Fsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00009005d00000430sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00009005d00000432sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00009005d0000043Esv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00009005d0000043Fsv*sd*bc*sc*i*)
# Generated with: extract-modaliases -i qla* kernel-default.rpm

%prep
cp %{S:1} .

%build
# There is nothing to build.

%install
# The firmware files must be installed in /lib/firmware
# because the firmware loader from udev searches there
mkdir -p %{buildroot}%{_firmwaredir}
install -m 644 %{S:0} %{buildroot}%{_firmwaredir}

%files
%defattr(-,root,root)
%doc LICENSE
%{_firmwaredir}/*

%description
Firmware files for the Adaptec AIC94xx (Razor) Series of SAS HBA
Adapters.



%changelog
