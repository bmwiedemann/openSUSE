#
# spec file for package kernel-firmware-brcm
#
# Copyright (c) 2025 SUSE LLC
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
%define __ksyms_path ^%{_firmwaredir}
%define git_version aaae2fb60f75b07d9c249ebe668524f7ddf51243

Name:           kernel-firmware-brcm
Version:        20250206
Release:        0
Summary:        Kernel firmware files for Broadcom wireless drivers
License:        SUSE-Firmware AND GPL-2.0-or-later AND GPL-2.0-only
Group:          System/Kernel
URL:            https://git.kernel.org/cgit/linux/kernel/git/firmware/linux-firmware.git/
Source0:        %{name}-%{version}.tar.xz
# URL:          https://github.com/openSUSE/kernel-firmware-tools/
Source1:        kernel-firmware-tools-20250211.tar.xz
Source2:        %{name}-rpmlintrc
Source3:        git_id
Source10:       aliases
Source11:       topicprovs
BuildRequires:  suse-module-tools
Requires(post): %{_bindir}/mkdir
Requires(post): %{_bindir}/touch
Requires(postun):%{_bindir}/mkdir
Requires(postun):%{_bindir}/touch
Requires(post): dracut >= 049
Conflicts:      kernel < 5.3
Conflicts:      kernel-firmware-uncompressed
BuildArch:      noarch
%if 0%{?suse_version} >= 1550
# make sure we have post-usrmerge filesystem package on TW
Conflicts:      filesystem < 84
%endif
Provides:       bcm43xx-firmware:/lib/firmware/brcm/brcmfmac43430-sdio.bin
Supplements:    modalias(pci:v000014E4d00004354sv*sd*bc02sc80i*)
Supplements:    modalias(pci:v000014E4d00004355sv000014E4sd00004355bc02sc80i*)
Supplements:    modalias(pci:v000014E4d00004365sv000014E4sd00004365bc02sc80i*)
Supplements:    modalias(pci:v000014E4d000043A3sv*sd*bc02sc80i*)
Supplements:    modalias(pci:v000014E4d000043BAsv*sd*bc02sc80i*)
Supplements:    modalias(pci:v000014E4d000043BBsv*sd*bc02sc80i*)
Supplements:    modalias(pci:v000014E4d000043BCsv*sd*bc02sc80i*)
Supplements:    modalias(pci:v000014E4d000043C3sv*sd*bc02sc80i*)
Supplements:    modalias(pci:v000014E4d000043C4sv*sd*bc02sc80i*)
Supplements:    modalias(pci:v000014E4d000043C5sv*sd*bc02sc80i*)
Supplements:    modalias(pci:v000014E4d000043CAsv*sd*bc02sc80i*)
Supplements:    modalias(pci:v000014E4d000043CBsv*sd*bc02sc80i*)
Supplements:    modalias(pci:v000014E4d000043CCsv*sd*bc02sc80i*)
Supplements:    modalias(pci:v000014E4d000043D3sv*sd*bc02sc80i*)
Supplements:    modalias(pci:v000014E4d000043D9sv*sd*bc02sc80i*)
Supplements:    modalias(pci:v000014E4d000043DCsv*sd*bc02sc80i*)
Supplements:    modalias(pci:v000014E4d000043E9sv*sd*bc02sc80i*)
Supplements:    modalias(pci:v000014E4d000043ECsv*sd*bc02sc80i*)
Supplements:    modalias(pci:v000014E4d000043EFsv*sd*bc02sc80i*)
Supplements:    modalias(pci:v000014E4d0000440Dsv*sd*bc02sc80i*)
Supplements:    modalias(pci:v000014E4d00004415sv*sd*bc02sc80i*)
Supplements:    modalias(pci:v000014E4d00004425sv*sd*bc02sc80i*)
Supplements:    modalias(pci:v000014E4d00004433sv*sd*bc02sc80i*)
Supplements:    modalias(pci:v000014E4d00004464sv*sd*bc02sc80i*)
Supplements:    modalias(pci:v000014E4d00004488sv*sd*bc02sc80i*)
Supplements:    modalias(pci:v000014E4d0000449Dsv*sd*bc02sc80i*)
Supplements:    modalias(pci:v000014E4d0000AA31sv*sd*bc02sc80i*)
Supplements:    modalias(pci:v000014E4d0000AA52sv*sd*bc02sc80i*)
Supplements:    modalias(sdio:c*v02D0d4324*)
Supplements:    modalias(sdio:c*v02D0d4329*)
Supplements:    modalias(sdio:c*v02D0d4330*)
Supplements:    modalias(sdio:c*v02D0d4334*)
Supplements:    modalias(sdio:c*v02D0d4335*)
Supplements:    modalias(sdio:c*v02D0d4339*)
Supplements:    modalias(sdio:c*v02D0d4345*)
Supplements:    modalias(sdio:c*v02D0d4354*)
Supplements:    modalias(sdio:c*v02D0d4355*)
Supplements:    modalias(sdio:c*v02D0d4356*)
Supplements:    modalias(sdio:c*v02D0d4359*)
Supplements:    modalias(sdio:c*v02D0d4373*)
Supplements:    modalias(sdio:c*v02D0dA804*)
Supplements:    modalias(sdio:c*v02D0dA887*)
Supplements:    modalias(sdio:c*v02D0dA94C*)
Supplements:    modalias(sdio:c*v02D0dA94D*)
Supplements:    modalias(sdio:c*v02D0dA962*)
Supplements:    modalias(sdio:c*v02D0dA9A4*)
Supplements:    modalias(sdio:c*v02D0dA9A6*)
Supplements:    modalias(sdio:c*v02D0dA9AF*)
Supplements:    modalias(sdio:c*v02D0dA9BF*)
Supplements:    modalias(sdio:c*v02D0dAAE8*)
Supplements:    modalias(sdio:c*v04B4dBD3D*)
Supplements:    modalias(usb:v043Ep3101d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v04B4p0BDCd*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v04B4pBD29d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0A5Cp0BDCd*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0A5CpBD17d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0A5CpBD1Ed*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0A5CpBD1Fd*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0A5CpBD27d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v13B1p0039d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(bcma:m04BFid0812rev11cl*)
Supplements:    modalias(bcma:m04BFid0812rev17cl*)
Supplements:    modalias(bcma:m04BFid0812rev18cl*)

%description
This package contains kernel firmware files for Broadcom wireless drivers.


%prep
%autosetup -a1 -p1
# strip down WHENCE for the topic
scripts/strip-topic-whence.sh brcm < WHENCE > WHENCE.new
mv WHENCE.new WHENCE

%build
# nothing to do

%install
./copy-firmware.sh -v --xz -j1 %{buildroot}%{_firmwaredir}
scripts/install-licenses.sh brcm %{buildroot}%{_licensedir}/%{name}
install -c -D -m 0644 WHENCE %{buildroot}%{_licensedir}/%{name}/WHENCE
install -c -D -m 0644 README.md %{buildroot}%{_docdir}/%{name}/README.md

%post
%{?regenerate_initrd_post}

%postun
%{?regenerate_initrd_post}

%posttrans
%{?regenerate_initrd_posttrans}

%files
%doc %{_docdir}/%{name}
%license %{_licensedir}/%{name}
%{_firmwaredir}

%changelog
