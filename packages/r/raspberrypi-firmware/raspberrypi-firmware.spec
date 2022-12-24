#
# spec file for package raspberrypi-firmware
#
# Copyright (c) 2022 SUSE LLC
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


%if 0%{?suse_version} < 1550 && 0%{?sle_version} <= 150300
# systemd-rpm-macros is wrong in 15.3 and below
%define _modprobedir /lib/modprobe.d
%endif
%global modprobe_d_files 50-rpi3.conf

Name:           raspberrypi-firmware
Version:        2022.12.12
Release:        0
Summary:        Binary bootloader and firmware files for Raspberry Pi
License:        SUSE-Firmware
Group:          System/Boot
URL:            https://github.com/raspberrypi/firmware/
Source0:        raspberrypi-firmware-%{version}.tar.bz2
Source1:        get-from-git.sh
Source99:       %{name}-rpmlintrc
Requires(post): util-linux
Requires(preun):util-linux
Recommends:     raspberrypi-firmware-config
Recommends:     raspberrypi-firmware-dt
Supplements:    modalias(of:NfirmwareT*Craspberrypi%2Cbcm2835-firmwareC*)
BuildArch:      noarch

%description
Binary bootloader and firmware files for Raspberry Pi

%package extra
Summary:        Extra bootloaders for Raspberry Pi
Group:          System/Boot
Requires:       raspberrypi-firmware = %{version}-%{release}
Requires(post): util-linux
Requires(preun):util-linux

%description extra
This package provides the console, experimental and debug
firmware files for Raspberry Pi

%package extra-pi4
Summary:        Extra bootloaders for Raspberry Pi
Group:          System/Boot
Requires:       raspberrypi-firmware = %{version}-%{release}
Requires(post): util-linux
Requires(preun):util-linux

%description extra-pi4
This package provides the console, experimental and debug
firmware files for Raspberry Pi 4

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}/boot/vc
cp -a boot/*.elf boot/*.bin boot/*.dat boot/LICENCE.broadcom %{buildroot}/boot/vc

mkdir -p %{buildroot}%{_prefix}/lib/sysctl.d/
cat > %{buildroot}%{_prefix}/lib/sysctl.d/50-rpi3.conf <<-'EOF'
	# Avoid running out of DMA pages for smsc95xx (bsc#1012449)
	vm.min_free_kbytes = 2048
EOF

mkdir -p %{buildroot}%{_modprobedir}/
cat > %{buildroot}%{_modprobedir}/50-rpi3.conf <<-'EOF'
	# Prevent too many page allocations (bsc#1012449)
	options smsc95xx turbo_mode=N
EOF

mkdir -p %{buildroot}%{_prefix}/lib/dracut/dracut.conf.d/
cat > %{buildroot}%{_prefix}/lib/dracut/dracut.conf.d/raspberrypi_modules.conf <<-'EOF'
	# Add necessary kernel modules to the initrd
	add_drivers+=" bcm2835_dma dwc2 " # bsc#1084272
	add_drivers+=" pcie-brcmstb " # boo#1162669
EOF

%pre
# Avoid restoring outdated stuff in posttrans
for _f in %{?modprobe_d_files}; do
    [ ! -f "/etc/modprobe.d/${_f}.rpmsave" ] || \
        mv -f "/etc/modprobe.d/${_f}.rpmsave" "/etc/modprobe.d/${_f}.rpmsave.old" || :
done

%post
if mountpoint -q /boot/efi && [[ ! -L /boot/efi ]]; then
  for f in start.elf start4.elf fixup.dat fixup4.dat bootcode.bin; do
    cp /boot/vc/$f /boot/efi/
  done
fi

%preun
if [ $1 -eq 0 ] && mountpoint -q /boot/efi && [[ ! -L /boot/efi ]]; then
  for f in start.elf start4.elf fixup.dat fixup4.dat bootcode.bin; do
    rm -f /boot/efi/$f
  done
fi

%posttrans
# Migration of modprobe.conf files to _modprobedir
for _f in %{?modprobe_d_files}; do
    [ ! -f "/etc/modprobe.d/${_f}.rpmsave" ] || \
        mv -fv "/etc/modprobe.d/${_f}.rpmsave" "/etc/modprobe.d/${_f}" || :
done

%post extra
if mountpoint -q /boot/efi && [[ ! -L /boot/efi ]]; then
  for suffix in _cd _db _x; do
    cp /boot/vc/start${suffix}.elf /boot/efi/
    cp /boot/vc/fixup${suffix}.dat /boot/efi/
  done
fi

%preun extra
if [ $1 -eq 0 ] && mountpoint -q /boot/efi && [[ ! -L /boot/efi ]]; then
  for suffix in _cd _db _x; do
    rm -f /boot/efi/start${suffix}.elf
    rm -f /boot/efi/fixup${suffix}.dat
  done
fi

%post extra-pi4
if mountpoint -q /boot/efi && [[ ! -L /boot/efi ]]; then
  for suffix in 4cd 4db 4x; do
    cp /boot/vc/start${suffix}.elf /boot/efi/
    cp /boot/vc/fixup${suffix}.dat /boot/efi/
  done
fi

%preun extra-pi4
if [ $1 -eq 0 ] && mountpoint -q /boot/efi && [[ ! -L /boot/efi ]]; then
  for suffix in 4cd 4db 4x; do
    rm -f /boot/efi/start${suffix}.elf
    rm -f /boot/efi/fixup${suffix}.dat
  done
fi

%files
%license /boot/vc/LICENCE.broadcom
%dir /boot/vc
/boot/vc/start.elf
/boot/vc/start4.elf
/boot/vc/fixup.dat
/boot/vc/fixup4.dat
/boot/vc/bootcode.bin
%dir %{_prefix}/lib/dracut/
%dir %{_prefix}/lib/dracut/dracut.conf.d/
%{_prefix}/lib/dracut/dracut.conf.d/raspberrypi_modules.conf
%dir %{_modprobedir}
%{_modprobedir}/50-rpi3.conf
%dir %{_prefix}/lib/sysctl.d/
%{_prefix}/lib/sysctl.d/50-rpi3.conf

%files extra
/boot/vc/start_cd.elf
/boot/vc/start_db.elf
/boot/vc/start_x.elf
/boot/vc/fixup_cd.dat
/boot/vc/fixup_db.dat
/boot/vc/fixup_x.dat

%files extra-pi4
/boot/vc/start4cd.elf
/boot/vc/start4db.elf
/boot/vc/start4x.elf
/boot/vc/fixup4cd.dat
/boot/vc/fixup4db.dat
/boot/vc/fixup4x.dat

%changelog
