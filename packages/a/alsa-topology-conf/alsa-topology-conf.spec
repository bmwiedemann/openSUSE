#
# spec file for package alsa-topology-conf
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


%if 0%{?suse_version} < 1550
%define _firmwaredir /lib/firmware
%endif

Name:           alsa-topology-conf
Version:        1.2.5.1
Release:        0
Summary:        ALSA topology configurations
License:        BSD-3-Clause
URL:            https://www.alsa-project.org/
Source:         https://www.alsa-project.org/files/pub/lib/alsa-topology-conf-%{version}.tar.bz2
Source1:        skl_hda_dsp_generic-tplg.bin
%ifarch %ix86 x86_64 %arm aarch64 ppc64le riscv64
BuildRequires:  alsa-utils
%endif
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
# Skylake and Kayblake-LP
Supplements:    modalias(pci:v00008086d00009D70sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d00009D71sv*sd*bc*sc*i*)

%description
This package contains the configuration files for ALSA topology support.

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}%{_datadir}/alsa
cp -a topology %{buildroot}%{_datadir}/alsa/
mkdir -p %{buildroot}%{_firmwaredir}
install -c -m 0644 %{S:1} %{buildroot}%{_firmwaredir}/skl_hda_dsp_generic-tplg.bin

%ifarch %ix86 x86_64 %arm aarch64 ppc64le riscv64
%check
alsatplg -c topology/hda-dsp/skl_hda_dsp_generic-tplg.conf -o /tmp/skl_hda_dsp_generic-tplg.bin.$$
cmp -b %{S:1} /tmp/skl_hda_dsp_generic-tplg.bin.$$
rm -f /tmp/skl_hda_dsp_generic-tplg.bin.$$
%endif

%files
%defattr(-, root, root)
%doc README.md
%license LICENSE
%{_datadir}/alsa
%{_firmwaredir}/*

%changelog
