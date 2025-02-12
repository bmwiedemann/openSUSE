#
# spec file for package kernel-firmware-media
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

Name:           kernel-firmware-media
Version:        20250206
Release:        0
Summary:        Kernel firmware files for various Video4Linux drivers
License:        SUSE-Firmware AND GPL-2.0-or-later
Group:          System/Kernel
URL:            https://git.kernel.org/cgit/linux/kernel/git/firmware/linux-firmware.git/
Source0:        %{name}-%{version}.tar.xz
# URL:          https://github.com/openSUSE/kernel-firmware-tools/
Source1:        kernel-firmware-tools-20250211.tar.xz
Source2:        %{name}-rpmlintrc
Source3:        git_id
Source10:       aliases
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
Supplements:    modalias(pci:v000014F1d00005B7Asv*sd*bc*sc*i*)
Supplements:    modalias(i2c:cx25840)
Supplements:    modalias(pci:v00001131d00007146sv0000110Asd00000000bc*sc*i*)
Supplements:    modalias(pci:v00001131d00007146sv000013C2sd00000000bc*sc*i*)
Supplements:    modalias(pci:v00001131d00007146sv000013C2sd00000001bc*sc*i*)
Supplements:    modalias(pci:v00001131d00007146sv000013C2sd00000002bc*sc*i*)
Supplements:    modalias(pci:v00001131d00007146sv000013C2sd00000003bc*sc*i*)
Supplements:    modalias(pci:v00001131d00007146sv000013C2sd00000004bc*sc*i*)
Supplements:    modalias(pci:v00001131d00007146sv000013C2sd00000006bc*sc*i*)
Supplements:    modalias(pci:v00001131d00007146sv000013C2sd00000008bc*sc*i*)
Supplements:    modalias(pci:v00001131d00007146sv000013C2sd0000000Abc*sc*i*)
Supplements:    modalias(pci:v00001131d00007146sv000013C2sd0000000Ebc*sc*i*)
Supplements:    modalias(pci:v00001131d00007146sv000013C2sd00001002bc*sc*i*)
Supplements:    modalias(usb:v0B48p1003d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0B48p1004d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0B48p1005d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0413p6A05d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v048Dp9005d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v048Dp9006d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v048Dp9135d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v048Dp9306d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v07CAp0335d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v07CAp0337d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v07CAp0825d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v07CAp1835d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v07CAp1867d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v07CAp1871d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v07CAp2835d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v07CAp3835d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v07CAp4835d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v07CApA110d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v07CApA835d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v07CApA867d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v07CApB835d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0B05p1779d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0CCDp0093d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0CCDp0099d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0CCDp00AAd*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0CCDp10AEd*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0CCDp10B2d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v15A4p1000d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v15A4p1001d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v15A4p1002d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v15A4p1003d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v15A4p9035d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1B80pE409d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1B80pE410d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1B80pE411d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1D19p0100d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1F4DpA115d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v2013p025Ad*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v2013p0262d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v2040pF900d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0413p60F6d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0413p6F00d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0413p6F01d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v045Ep02D5d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v05D8p810Fd*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v07CApA807d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v07CApB568d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v07CApB808d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0B05p171Fd*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0B05p1736d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0B05p173Fd*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0CCDp0058d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0CCDp005Ad*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0CCDp0060d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0CCDp0062d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0CCDp0078d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0CCDp0081d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0CCDp00ABd*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0CCDp10A0d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0CCDp10A1d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0FD9p0011d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0FD9p0020d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0FD9p0021d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0FD9p003Fd*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1044p7001d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1044p7002d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v10B8p1BB2d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v10B8p1BB4d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v10B8p1E14d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v10B8p1E6Ed*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v10B8p1E78d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v10B8p1E80d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v10B8p1EBCd*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v10B8p1EBEd*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v10B8p1EF0d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v10B8p1F90d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v10B8p1F98d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v10B8p1F9Cd*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v10B8p1FA0d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v10B8p1FA8d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v10B8p1FAAd*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v10B8p2383d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v10B8p2384d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1164p0871d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1164p1E8Cd*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1164p1EDCd*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1164p1EFCd*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1164p1F08d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1164p2EDCd*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1415p0003d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v147Fp2758d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v14F7p0004d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1554p5010d3F00dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1554p5010d3[0-9A-E]*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1554p5010d[0-2]*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1584p6003d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1660p1921d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v185Bp1E78d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v185Bp1E80d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1E59p0002d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v2013p0245d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v2013p0248d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v2013p025Cd*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v2013p025Dd*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v2013p1FAAd*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v2040p5200d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v2040p7050d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v2040p7060d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v2040p7070d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v2040p7080d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v2040p8400d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v2040p9580d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v2040p9941d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v2040p9950d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v2040pB200d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v2040pB210d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v2304p0228d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v2304p0229d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v2304p022Cd*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v2304p022Ed*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v2304p0236d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v2304p0237d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v2304p023Ad*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v2304p023Bd*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v2304p023Dd*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v2304p023Ed*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v2304p0243d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v2304p0245d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v2304p0248d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v04C1p009Dd*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0602p1001d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(of:N*T*Camlogic,g12a-vdec)
Supplements:    modalias(of:N*T*Camlogic,g12a-vdecC*)
Supplements:    modalias(of:N*T*Camlogic,gxbb-vdec)
Supplements:    modalias(of:N*T*Camlogic,gxbb-vdecC*)
Supplements:    modalias(of:N*T*Camlogic,gxl-vdec)
Supplements:    modalias(of:N*T*Camlogic,gxl-vdecC*)
Supplements:    modalias(of:N*T*Camlogic,gxlx-vdec)
Supplements:    modalias(of:N*T*Camlogic,gxlx-vdecC*)
Supplements:    modalias(of:N*T*Camlogic,gxm-vdec)
Supplements:    modalias(of:N*T*Camlogic,gxm-vdecC*)
Supplements:    modalias(of:N*T*Camlogic,sm1-vdec)
Supplements:    modalias(of:N*T*Camlogic,sm1-vdecC*)
Supplements:    modalias(of:N*T*Cmediatek,mt8173-vpu)
Supplements:    modalias(of:N*T*Cmediatek,mt8173-vpuC*)
Supplements:    modalias(of:N*T*Csamsung,exynos3250-mfc)
Supplements:    modalias(of:N*T*Csamsung,exynos3250-mfcC*)
Supplements:    modalias(of:N*T*Csamsung,exynos5433-mfc)
Supplements:    modalias(of:N*T*Csamsung,exynos5433-mfcC*)
Supplements:    modalias(of:N*T*Csamsung,mfc-v10)
Supplements:    modalias(of:N*T*Csamsung,mfc-v10C*)
Supplements:    modalias(of:N*T*Csamsung,mfc-v5)
Supplements:    modalias(of:N*T*Csamsung,mfc-v5C*)
Supplements:    modalias(of:N*T*Csamsung,mfc-v6)
Supplements:    modalias(of:N*T*Csamsung,mfc-v6C*)
Supplements:    modalias(of:N*T*Csamsung,mfc-v7)
Supplements:    modalias(of:N*T*Csamsung,mfc-v7C*)
Supplements:    modalias(of:N*T*Csamsung,mfc-v8)
Supplements:    modalias(of:N*T*Csamsung,mfc-v8C*)
Supplements:    modalias(of:N*T*Ctesla,fsd-mfc)
Supplements:    modalias(of:N*T*Ctesla,fsd-mfcC*)
Supplements:    modalias(of:N*T*Cti,dra7-vpe)
Supplements:    modalias(of:N*T*Cti,dra7-vpeC*)

%description
This package contains kernel firmware files for various Video4Linux drivers.


%prep
%autosetup -a1 -p1
# strip down WHENCE for the topic
scripts/strip-topic-whence.sh media < WHENCE > WHENCE.new
mv WHENCE.new WHENCE

%build
# nothing to do

%install
./copy-firmware.sh -v --xz -j1 %{buildroot}%{_firmwaredir}
scripts/install-licenses.sh media %{buildroot}%{_licensedir}/%{name}
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
