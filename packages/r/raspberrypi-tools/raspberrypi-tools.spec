#
# spec file for package raspberrypi
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


Name:           raspberrypi-tools
Version:        2020.09.24
Release:        0
Summary:        Tools for the Raspberry boards
License:        BSD-3-Clause
Group:          System/boot
URL:            https://github.com/raspberrypi/tools
Source0:        %{name}-%{version}.tar.bz2
Source1:        get-from-git.sh
Patch0:         armstub8-Add-PSCI-monitor-support-for-DBCM2711.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
ExclusiveArch:  aarch64
Requires(post): util-linux
Requires(preun): util-linux
Conflicts:      arm-trusted-firmware-rpi4
Recommends:     raspberrypi-firmware-config
Supplements:    modalias(of:N*T*Cbrcm%2Cbcm2711*C*)

%description
Assorted set of tools for Raspberry Pi boards

%package armstubs
Summary: Poor-man’s PSCI monitor for Raspberry Pi4

%description armstubs
PSCI EL3 monitor for Raspberry Pi4. Monitor is used to workaround
CVE-2017-5715 and CVE-2018-3639 for Cortex-A72 CPU used in BCM2711.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1

%build armstubs
export CC8=gcc
export LD8=ld
export OBJCOPY8=objcopy
export OBJDUMP8="objcopy -maarch64"
cd armstubs
make clean armstub8-gic-highperi-psci.bin armstub8-gic-psci.bin

%install armstubs
mkdir -p %{buildroot}%{_datadir}/%{name}
install -p -m 0644 armstubs/armstub8-gic-psci.bin %{buildroot}%{_datadir}/%{name}/armstub8-rpi4.bin
install -p -m 0644 armstubs/armstub8-gic-highperi-psci.bin %{buildroot}%{_datadir}/%{name}/armstub8-rpi4-hi.bin

%post armstubs
if mountpoint -q /boot/efi && [[ ! -L /boot/efi ]]; then
  for f in armstub8-rpi4.bin armstub8-rpi4-hi.bin; do
    cp %{_datadir}/%{name}/$f /boot/efi/
  done
fi

%preun armstubs
if [ $1 -eq 0 ] && mountpoint -q /boot/efi && [[ ! -L /boot/efi ]]; then
  for f in armstub8-rpi4.bin armstub8-rpi4-hi.bin; do
    rm -f /boot/efi/$f
  done
fi

%files armstubs
%defattr(-,root,root)
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/armstub8-rpi4.bin
%{_datadir}/%{name}/armstub8-rpi4-hi.bin

%changelog
