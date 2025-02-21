#
# spec file for package kernel-firmware-mediatek
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
%define git_version 6cf959daab2a38d074b059f73c24aab9d4dbcbc3

Name:           kernel-firmware-mediatek
Version:        20250220
Release:        0
Summary:        Kernel firmware files for Mediatek network drivers
License:        GPL-2.0-or-later AND SUSE-Firmware
Group:          System/Kernel
URL:            https://git.kernel.org/cgit/linux/kernel/git/firmware/linux-firmware.git/
Source0:        %{name}-%{version}.tar.xz
# URL:          https://github.com/openSUSE/kernel-firmware-tools/
Source1:        kernel-firmware-tools-20250218.tar.xz
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
Provides:       ralink-firmware = %{version}
Obsoletes:      ralink-firmware < %{version}
Supplements:    modalias(of:N*T*Cmediatek,mt7622-bluetooth)
Supplements:    modalias(of:N*T*Cmediatek,mt7622-bluetoothC*)
Supplements:    modalias(of:N*T*Cmediatek,mt7663u-bluetooth)
Supplements:    modalias(of:N*T*Cmediatek,mt7663u-bluetoothC*)
Supplements:    modalias(of:N*T*Cmediatek,mt7668u-bluetooth)
Supplements:    modalias(of:N*T*Cmediatek,mt7668u-bluetoothC*)
Supplements:    modalias(of:N*T*Cmediatek,mt8183-scp)
Supplements:    modalias(of:N*T*Cmediatek,mt8183-scpC*)
Supplements:    modalias(of:N*T*Cmediatek,mt8186-scp)
Supplements:    modalias(of:N*T*Cmediatek,mt8186-scpC*)
Supplements:    modalias(of:N*T*Cmediatek,mt8188-scp)
Supplements:    modalias(of:N*T*Cmediatek,mt8188-scp-dual)
Supplements:    modalias(of:N*T*Cmediatek,mt8188-scp-dualC*)
Supplements:    modalias(of:N*T*Cmediatek,mt8188-scpC*)
Supplements:    modalias(of:N*T*Cmediatek,mt8192-scp)
Supplements:    modalias(of:N*T*Cmediatek,mt8192-scpC*)
Supplements:    modalias(of:N*T*Cmediatek,mt8195-scp)
Supplements:    modalias(of:N*T*Cmediatek,mt8195-scp-dual)
Supplements:    modalias(of:N*T*Cmediatek,mt8195-scp-dualC*)
Supplements:    modalias(of:N*T*Cmediatek,mt8195-scpC*)
Supplements:    modalias(pci:v00000B48d00007922sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000014C3d00000608sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000014C3d00000616sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000014C3d00000717sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000014C3d00007602sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000014C3d00007610sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000014C3d00007611sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000014C3d00007612sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000014C3d00007615sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000014C3d00007630sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000014C3d00007650sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000014C3d00007662sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000014C3d00007663sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000014C3d00007920sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000014C3d00007922sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000014C3d00007925sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000014C3d00007961sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000014C3d00007990sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000014C3d00007991sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000014C3d00007992sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000014C3d0000799Asv*sd*bc*sc*i*)
Supplements:    modalias(sdio:c*v037Ad7663*)
Supplements:    modalias(sdio:c*v037Ad7668*)
Supplements:    modalias(sdio:c*v037Ad7901*)
Supplements:    modalias(sdio:c*v037Ad7961*)
Supplements:    modalias(usb:v045Ep02E6d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v045Ep02FEd*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v04BBp0951d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v057Cp8502d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v057Cp8503d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0586p3425d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v07B8p7610d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0846p9014d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0846p9053d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0846p9060d*dc*dsc*dp*icFFiscFFipFFin*)
Supplements:    modalias(usb:v0B05p17D1d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0B05p17D3d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0B05p17DBd*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0B05p17EBd*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0B05p180Bd*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0B05p1833d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0DF6p0075d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0DF6p0079d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0E8Dp760Ad*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0E8Dp760Bd*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0E8Dp7610d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0E8Dp7612d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0E8Dp7630d*dc*dsc*dp*icFFisc02ipFFin*)
Supplements:    modalias(usb:v0E8Dp7632d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0E8Dp7650d*dc*dsc*dp*icFFisc02ipFFin*)
Supplements:    modalias(usb:v0E8Dp7925d*dc*dsc*dp*icFFiscFFipFFin*)
Supplements:    modalias(usb:v0E8Dp7961d*dc*dsc*dp*icFFiscFFipFFin*)
Supplements:    modalias(usb:v13B1p003Ed*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v13D3p3431d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v13D3p3434d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v148Fp7601d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v148Fp760Ad*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v148Fp760Bd*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v148Fp760Cd*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v148Fp760Dd*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v148Fp7610d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v148Fp761Ad*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v2001p3D02d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v2001p3D04d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v2019pAB31d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v20F4p806Bd*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v2357p0105d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v2357p010Bd*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v2357p0123d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v2717p4106d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v293Cp5702d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v2955p0001d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v2955p1001d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v2955p1003d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v2A5Fp1000d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v2C4Ep0103d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v3574p6211d*dc*dsc*dp*icFFiscFFipFFin*)
Supplements:    modalias(usb:v35BCp0107d*dc*dsc*dp*icFFiscFFipFFin*)
Supplements:    modalias(usb:v7392p7710d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v7392pA711d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v7392pB711d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v7392pC711d*dc*dsc*dp*ic*isc*ip*in*)

%description
This package contains kernel firmware files for Mediatek network drivers.

%prep
%autosetup -a1 -p1
# strip down WHENCE for the topic
scripts/strip-topic-whence.sh mediatek < WHENCE > WHENCE.new
mv WHENCE.new WHENCE

%build
# nothing to do

%install
./copy-firmware.sh -v --xz -j1 %{buildroot}%{_firmwaredir}
scripts/install-licenses.sh mediatek %{buildroot}%{_licensedir}/%{name}
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
