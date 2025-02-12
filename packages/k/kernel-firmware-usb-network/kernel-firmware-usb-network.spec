#
# spec file for package kernel-firmware-usb-network
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

Name:           kernel-firmware-usb-network
Version:        20250206
Release:        0
Summary:        Kernel firmware files for various USB WiFi / Ethernet drivers
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
Supplements:    modalias(usb:v03E8p0008d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v04BBp0901d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0506p03E8d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0506p11F8d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0557p2002d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0557p4000d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0565p0002d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0565p0003d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0565p0005d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v05E9p0008d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v05E9p0009d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v066Bp2202d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v06E1p0008d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v06E1p0009d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0707p0100d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v07AAp0001d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v07B8p4000d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v07C9pB010d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0846p1001d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0846p1002d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v085Ap0008d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v085Ap0009d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v087Dp5704d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0951p0008d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v095Ap3003d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v10BDp1427d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1342p0204d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v13D2p0400d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1485p0001d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1485p0002d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1645p0005d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1645p0008d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1645p8005d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1668p0323d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v2001p4000d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(sdio:c*v041Bd9116*)
Supplements:    modalias(sdio:c*v041Bd9330*)
Supplements:    modalias(usb:v1618p9113d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1618p9116d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0411p00D8d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0411p00D9d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0411p00E6d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0411p00F4d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0411p0116d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0411p0119d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0411p0137d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0471p200Ad*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v04BBp093Dd*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v04E8p4471d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v050Dp7050d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v050Dp705Ad*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v050Dp905Bd*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v050Dp905Cd*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0586p3415d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v06F8pE002d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v06F8pE010d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v06F8pE020d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0769p31F3d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v07AAp002Ed*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v07B8pB21Bd*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v07B8pB21Cd*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v07B8pB21Dd*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v07B8pB21Ed*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v07B8pB21Fd*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v07D1p3C03d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v07D1p3C04d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v07D1p3C06d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v07D1p3C07d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0812p3101d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v08DDp0120d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0B05p1723d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0B05p1724d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0CDEp001Cd*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0DB0p4600d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0DB0p6874d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0DB0p6877d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0DB0pA861d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0DB0pA874d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0DF6p0024d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0DF6p0027d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0DF6p002Fd*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0DF6p90ACd*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0DF6p9712d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0EB0p9021d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1044p8008d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1044p800Ad*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1371p9022d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1371p9032d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v13B1p0020d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v13B1p0023d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v13B1p0028d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1472p0009d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v148Fp2573d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v148Fp2671d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v148Fp9021d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v14B2p3C10d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v14B2p3C22d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v15A9p0004d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1631pC019d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1690p0722d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1740p3701d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1740p7100d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v178Dp02BEd*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v18C5p0002d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v18E8p6196d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v18E8p6229d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v18E8p6238d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1B75p7318d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v2019pAB01d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v2019pAB50d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v6933p5001d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v7167p3840d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v7392p7318d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v7392p7618d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v160Ap3184d*dc*dsc*dp*ic*isc*ip*in*)

%description
This package contains kernel firmware files for various USB WiFi / Ethernet drivers.


%prep
%autosetup -a1 -p1
# strip down WHENCE for the topic
scripts/strip-topic-whence.sh usb-network < WHENCE > WHENCE.new
mv WHENCE.new WHENCE

%build
# nothing to do

%install
./copy-firmware.sh -v --xz -j1 %{buildroot}%{_firmwaredir}
scripts/install-licenses.sh usb-network %{buildroot}%{_licensedir}/%{name}
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
