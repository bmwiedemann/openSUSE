#
# spec file for package kernel-firmware-atheros
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

Name:           kernel-firmware-atheros
Version:        20250206
Release:        0
Summary:        Kernel firmware files for Atheros wireless drivers
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
Provides:       ath3k-firmware = %{version}
Obsoletes:      ath3k-firmware < %{version}
Supplements:    modalias(usb:v07D1p3A07d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v07D1p3A08d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v083Ap4506d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v083Ap4507d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0846p4250d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0846p4251d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0846p4300d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0846p4301d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0846p5F00d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0846p5F01d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0CDEp0012d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0CDEp0013d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0CF3p0001d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0CF3p0002d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0CF3p0003d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0CF3p0004d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0CF3p0005d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0CF3p0006d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0D8Ep7801d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0D8Ep7802d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0D8Ep7803d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0D8Ep7811d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0D8Ep7812d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v129Bp160Bd*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v129Bp160Cd*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1385p4250d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1385p4251d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1385p5F00d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1385p5F01d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1385p5F02d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1385p5F03d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1435p0826d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1435p0827d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1435p0828d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1435p0829d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v157Ep3006d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v157Ep3007d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v157Ep3205d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v157Ep3206d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v168Cp0001d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v168Cp0002d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1690p0710d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1690p0711d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1690p0712d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1690p0713d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v16ABp7801d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v16ABp7802d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v16ABp7811d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v16ABp7812d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v2001p3A00d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v2001p3A01d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v2001p3A02d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v2001p3A03d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v2001p3A04d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v2001p3A05d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v03F0p311Dd*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0489pE027d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0489pE02Cd*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0489pE036d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0489pE03Cd*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0489pE03Dd*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0489pE04Dd*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0489pE04Ed*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0489pE056d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0489pE057d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0489pE05Fd*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0489pE076d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0489pE078d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0489pE095d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v04C5p1330d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v04CAp3004d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v04CAp3005d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v04CAp3006d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v04CAp3007d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v04CAp3008d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v04CAp300Bd*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v04CAp300Dd*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v04CAp300Fd*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v04CAp3010d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v04CAp3014d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v04CAp3018d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v04F2pAFF1d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0930p0215d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0930p0219d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0930p021Cd*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0930p0220d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0930p0227d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0B05p17D0d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0CF3p0036d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0CF3p3000d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0CF3p3002d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0CF3p3004d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0CF3p3008d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0CF3p311Dd*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0CF3p311Ed*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0CF3p311Fd*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0CF3p3121d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0CF3p817Ad*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0CF3p817Bd*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0CF3pE003d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0CF3pE004d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0CF3pE005d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0CF3pE006d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0CF3pE019d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v13D3p3304d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v13D3p3362d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v13D3p3375d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v13D3p3393d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v13D3p3395d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v13D3p3402d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v13D3p3408d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v13D3p3423d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v13D3p3432d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v13D3p3472d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v13D3p3474d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v13D3p3487d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v13D3p3490d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(sdio:c*v0271d0300*)
Supplements:    modalias(sdio:c*v0271d0301*)
Supplements:    modalias(sdio:c*v0271d0400*)
Supplements:    modalias(sdio:c*v0271d0401*)
Supplements:    modalias(sdio:c*v0271d0402*)
Supplements:    modalias(sdio:c*v0271d0418*)
Supplements:    modalias(sdio:c*v0271d0419*)
Supplements:    modalias(usb:v04DAp390Dd*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0CF3p9374d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0CF3p9375d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v040Dp3801d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0411p017Fd*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0411p0197d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0471p209Ed*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v04CAp4605d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v04DAp3904d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v057Cp8403d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v07B8p9271d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v07D1p3A10d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v083ApA704d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0846p9018d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0846p9030d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0930p0A08d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0CF3p1006d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0CF3p20FFd*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0CF3p7010d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0CF3p7015d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0CF3p9271d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0CF3pB002d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0CF3pB003d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v13D3p3327d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v13D3p3328d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v13D3p3346d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v13D3p3348d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v13D3p3349d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v13D3p3350d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1EDAp2315d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(ar9170usb)
Supplements:    modalias(arusb_lnx)
Supplements:    modalias(usb:v0409p0249d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0409p02B4d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v04BBp093Fd*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v057Cp8401d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v057Cp8402d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0586p3417d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v07D1p3A09d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v07D1p3A0Fd*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v07D1p3C10d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v083ApF522d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0846p9001d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0846p9010d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0846p9040d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0ACEp1221d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0CDEp0023d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0CDEp0026d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0CDEp0027d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0CF3p1001d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0CF3p1002d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0CF3p1010d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0CF3p1011d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0CF3p9170d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1435p0326d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1435p0804d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1668p1200d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1B75p9170d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v2019p5304d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:vCACEp0300d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(pci:v000017CBd00001201sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001AE9d00000302sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001AE9d00000310sv*sd*bc*sc*i*)

%description
This package contains kernel firmware files for Atheros wireless drivers.


%prep
%autosetup -a1 -p1
# strip down WHENCE for the topic
scripts/strip-topic-whence.sh atheros < WHENCE > WHENCE.new
mv WHENCE.new WHENCE

%build
# nothing to do

%install
./copy-firmware.sh -v --xz -j1 %{buildroot}%{_firmwaredir}
scripts/install-licenses.sh atheros %{buildroot}%{_licensedir}/%{name}
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
