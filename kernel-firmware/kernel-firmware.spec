#
# spec file for package kernel-firmware
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define __ksyms_path ^/lib/firmware
%define version_unconverted 20190712
Name:           kernel-firmware
Version:        20190712
Release:        0
Summary:        Linux kernel firmware files
License:        SUSE-Firmware AND GPL-2.0-only AND GPL-2.0-or-later AND MIT
Group:          System/Kernel
URL:            https://git.kernel.org/cgit/linux/kernel/git/firmware/linux-firmware.git/
# Created with umask 022; cd /_tmp
# After git clone https://git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware.git
# cd linux-firmware
# git archive --format=tar --prefix=kernel-firmware-$version/ -v master ./ | xz -9 -M 4G --check=crc32 -T 4 > /tmp/kernel-firmware-$version.tar.xz
#
Source0:        kernel-firmware-%{version}.tar.xz
# ast_dp501_fw.bin generated from header file of xf86-video-ast: MIT/X11 License
Source2:        ast_dp501_fw.bin
Source8:        ql2600_fw.bin
Source9:        ql2700_fw.bin
Source10:       ql8300_fw.bin
Source99:       %{name}-rpmlintrc
# temporary revert for the broken iwlwifi firmware (bsc#1142128)
Source100:      iwlwifi-9000-pu-b0-jf-b0-46.ucode
Source101:      iwlwifi-9260-th-b0-jf-b0-46.ucode
Source102:      iwlwifi-sha1sum
Patch100:       WHENCE-iwlwifi-9xxx-46-revert.patch
BuildRequires:  fdupes
BuildRequires:  suse-module-tools
Requires(post): coreutils
Requires(postun): coreutils
Provides:       bcm43xx-firmware:/lib/firmware/brcm/brcmfmac43430-sdio.bin
Provides:       qlogic-firmware
Obsoletes:      qlogic-firmware
Provides:       cxgb3-firmware
Obsoletes:      cxgb3-firmware
Provides:       ralink-firmware
Obsoletes:      ralink-firmware
Provides:       iwl1000-ucode
Obsoletes:      iwl1000-ucode
Provides:       iwl3945-ucode
Obsoletes:      iwl3945-ucode
Provides:       iwl4965-ucode
Obsoletes:      iwl4965-ucode
Provides:       iwl5000-ucode
Obsoletes:      iwl5000-ucode
Provides:       iwl5150-ucode
Obsoletes:      iwl5150-ucode
Provides:       iwl100-ucode
Obsoletes:      iwl100-ucode
Provides:       iwl6000-ucode
Obsoletes:      iwl6000-ucode
Provides:       iwl6050-ucode
Obsoletes:      iwl6050-ucode
Provides:       iwl6000g2-ucode
Obsoletes:      iwl6000g2-ucode
Provides:       ath3k-firmware
Obsoletes:      ath3k-firmware
Provides:       compat-wireless-firmware = 4.4
Obsoletes:      compat-wireless-firmware < 4.4
BuildArch:      noarch

%description
This package contains the firmware for in-kernel drivers that was
previously included in the kernel. It is shared by all kernels >=
2.6.27-rc1.

%package -n ucode-amd
Summary:        Microcode updates for AMD CPUs
Group:          System/Kernel
Requires(post): coreutils
Requires(postun): coreutils
# new style (after 3.12 kernel somewhen)
Supplements:    modalias(cpu:type%%3Ax86*ven0002*)
# old style (before 3.16 kernel)
Supplements:    modalias(x86cpu:vendor%%3A0002%%3Afamily%%3A*%%3Amodel%%3A*%%3Afeature%%3A*)

%description -n ucode-amd
This package contains the microcode files used by AMD CPUs.

%prep
%setup -q
%patch100 -p1
cp %{SOURCE2} %{SOURCE8} %{SOURCE9} %{SOURCE10} .
sha1sum --quiet -c %{SOURCE102} || exit 1
cp %{SOURCE100} .
cp %{SOURCE101} .

%build
# nothing to do

%install
mkdir -p %{buildroot}/lib/firmware
cp -avf * %{buildroot}/lib/firmware
rm -f %{buildroot}/lib/firmware/WHENCE
%fdupes %{buildroot}
# In alsa-firmware
rm -f %{buildroot}/lib/firmware/ctefx.bin
rm -f %{buildroot}/lib/firmware/ctspeq.bin
# Devel files
rm -rf %{buildroot}/lib/firmware/carl9170fw
# Devel files
rm -f %{buildroot}/lib/firmware/isci/{Makefile,README}
rm -f %{buildroot}/lib/firmware/isci/*.[ch]
# Remove check_whence.py; avoid useless python dependency (bsc#1101818)
rm -f %{buildroot}/lib/firmware/check_whence.py

%post
%{?regenerate_initrd_post}

%post -n ucode-amd
%{?regenerate_initrd_post}

%postun
%{?regenerate_initrd_post}

%postun -n ucode-amd
%{?regenerate_initrd_post}

%posttrans
%{?regenerate_initrd_posttrans}

%posttrans -n ucode-amd
%{?regenerate_initrd_posttrans}

%files
%defattr(0644,root,root,0755)
%doc WHENCE README
%license GPL-2 GPL-3 LICEN[CS]E.*
%exclude /lib/firmware/amd-ucode
%exclude /lib/firmware/LICENSE.amd-ucode
/lib/firmware/*

%files -n ucode-amd
%defattr(0644,root,root,0755)
/lib/firmware/amd-ucode
/lib/firmware/LICENSE.amd-ucode

%changelog
