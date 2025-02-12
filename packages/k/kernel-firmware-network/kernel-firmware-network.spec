#
# spec file for package kernel-firmware-network
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

Name:           kernel-firmware-network
Version:        20250206
Release:        0
Summary:        Kernel firmware files for various network drivers
License:        SUSE-Firmware AND GPL-2.0-or-later AND GPL-2.0-only
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
Supplements:    modalias(pci:v00001011d0000001Asv*sd*bc02sc00i*)
Supplements:    modalias(pci:v000010A9d00000009sv*sd*bc02sc00i*)
Supplements:    modalias(pci:v000010B7d00000001sv*sd*bc02sc00i*)
Supplements:    modalias(pci:v000012AEd00000001sv*sd*bc02sc00i*)
Supplements:    modalias(pci:v000012AEd00000002sv*sd*bc02sc00i*)
Supplements:    modalias(pci:v000012AEd000000FAsv*sd*bc02sc00i*)
Supplements:    modalias(pci:v00001385d0000620Asv*sd*bc02sc00i*)
Supplements:    modalias(pci:v00001385d0000630Asv*sd*bc02sc00i*)
Supplements:    modalias(pci:v00008086d00001029sv*sd*bc02sc00i*)
Supplements:    modalias(pci:v00008086d00001030sv*sd*bc02sc00i*)
Supplements:    modalias(pci:v00008086d00001031sv*sd*bc02sc00i*)
Supplements:    modalias(pci:v00008086d00001032sv*sd*bc02sc00i*)
Supplements:    modalias(pci:v00008086d00001033sv*sd*bc02sc00i*)
Supplements:    modalias(pci:v00008086d00001034sv*sd*bc02sc00i*)
Supplements:    modalias(pci:v00008086d00001038sv*sd*bc02sc00i*)
Supplements:    modalias(pci:v00008086d00001039sv*sd*bc02sc00i*)
Supplements:    modalias(pci:v00008086d0000103Asv*sd*bc02sc00i*)
Supplements:    modalias(pci:v00008086d0000103Bsv*sd*bc02sc00i*)
Supplements:    modalias(pci:v00008086d0000103Csv*sd*bc02sc00i*)
Supplements:    modalias(pci:v00008086d0000103Dsv*sd*bc02sc00i*)
Supplements:    modalias(pci:v00008086d0000103Esv*sd*bc02sc00i*)
Supplements:    modalias(pci:v00008086d00001050sv*sd*bc02sc00i*)
Supplements:    modalias(pci:v00008086d00001051sv*sd*bc02sc00i*)
Supplements:    modalias(pci:v00008086d00001052sv*sd*bc02sc00i*)
Supplements:    modalias(pci:v00008086d00001053sv*sd*bc02sc00i*)
Supplements:    modalias(pci:v00008086d00001054sv*sd*bc02sc00i*)
Supplements:    modalias(pci:v00008086d00001055sv*sd*bc02sc00i*)
Supplements:    modalias(pci:v00008086d00001056sv*sd*bc02sc00i*)
Supplements:    modalias(pci:v00008086d00001057sv*sd*bc02sc00i*)
Supplements:    modalias(pci:v00008086d00001059sv*sd*bc02sc00i*)
Supplements:    modalias(pci:v00008086d00001064sv*sd*bc02sc00i*)
Supplements:    modalias(pci:v00008086d00001065sv*sd*bc02sc00i*)
Supplements:    modalias(pci:v00008086d00001066sv*sd*bc02sc00i*)
Supplements:    modalias(pci:v00008086d00001067sv*sd*bc02sc00i*)
Supplements:    modalias(pci:v00008086d00001068sv*sd*bc02sc00i*)
Supplements:    modalias(pci:v00008086d00001069sv*sd*bc02sc00i*)
Supplements:    modalias(pci:v00008086d0000106Asv*sd*bc02sc00i*)
Supplements:    modalias(pci:v00008086d0000106Bsv*sd*bc02sc00i*)
Supplements:    modalias(pci:v00008086d00001091sv*sd*bc02sc00i*)
Supplements:    modalias(pci:v00008086d00001092sv*sd*bc02sc00i*)
Supplements:    modalias(pci:v00008086d00001093sv*sd*bc02sc00i*)
Supplements:    modalias(pci:v00008086d00001094sv*sd*bc02sc00i*)
Supplements:    modalias(pci:v00008086d00001095sv*sd*bc02sc00i*)
Supplements:    modalias(pci:v00008086d000010FEsv*sd*bc02sc00i*)
Supplements:    modalias(pci:v00008086d00001209sv*sd*bc02sc00i*)
Supplements:    modalias(pci:v00008086d00001229sv*sd*bc02sc00i*)
Supplements:    modalias(pci:v00008086d00002449sv*sd*bc02sc00i*)
Supplements:    modalias(pci:v00008086d00002459sv*sd*bc02sc00i*)
Supplements:    modalias(pci:v00008086d0000245Dsv*sd*bc02sc00i*)
Supplements:    modalias(pci:v00008086d000027DCsv*sd*bc02sc00i*)
Supplements:    modalias(auxiliary:ice.sf)
Supplements:    modalias(pci:v00008086d0000124Csv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d0000124Dsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d0000124Esv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d0000124Fsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d000012D1sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d000012D2sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d000012D3sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d000012D4sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d000012D5sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d000012D8sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d000012DAsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d000012DCsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d000012DDsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d000012DEsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d0000151Dsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d00001591sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d00001592sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d00001593sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d00001599sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d0000159Asv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d0000159Bsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d00001888sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d0000188Asv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d0000188Bsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d0000188Csv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d0000188Dsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d0000188Esv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d00001890sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d00001891sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d00001892sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d00001893sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d00001894sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d00001897sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d00001898sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d00001899sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d0000189Asv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d0000579Csv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d0000579Dsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d0000579Esv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d0000579Fsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000014C1d00000008sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000014C1d00000009sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00004040d00000001sv*sd*bc02sc00i00*)
Supplements:    modalias(pci:v00004040d00000002sv*sd*bc02sc00i00*)
Supplements:    modalias(pci:v00004040d00000003sv*sd*bc02sc00i00*)
Supplements:    modalias(pci:v00004040d00000004sv*sd*bc02sc00i00*)
Supplements:    modalias(pci:v00004040d00000005sv*sd*bc02sc00i00*)
Supplements:    modalias(pci:v00004040d00000024sv*sd*bc02sc00i00*)
Supplements:    modalias(pci:v00004040d00000025sv*sd*bc02sc00i00*)
Supplements:    modalias(pci:v00004040d00000100sv*sd*bc02sc00i00*)
Supplements:    modalias(pci:v00001077d00008020sv*sd*bc02sc00i00*)
Supplements:    modalias(pci:v00001077d00008030sv*sd*bc02sc00i00*)
Supplements:    modalias(pci:v00001077d00008040sv*sd*bc02sc00i00*)
Supplements:    modalias(pci:v00001077d00008430sv*sd*bc02sc00i00*)
Supplements:    modalias(pci:v00001077d00008440sv*sd*bc02sc00i00*)
Supplements:    modalias(pci:v00001077d00008830sv*sd*bc02sc00i00*)
Supplements:    modalias(pci:v00001077d00008C30sv*sd*bc02sc00i00*)
Supplements:    modalias(pci:v00001814d00000301sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001814d00000302sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001814d00000401sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00009004d00006915sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001FC9d00003009sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001FC9d00003010sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001FC9d00003014sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v0000106Bd00001645sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000010CFd000011A2sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001148d00004400sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001148d00004500sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000014E4d00001600sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000014E4d00001601sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000014E4d00001641sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000014E4d00001642sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000014E4d00001643sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000014E4d00001644sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000014E4d00001645sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000014E4d00001646sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000014E4d00001647sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000014E4d00001648sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000014E4d00001649sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000014E4d0000164Dsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000014E4d00001653sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000014E4d00001654sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000014E4d00001655sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000014E4d00001656sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000014E4d00001657sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000014E4d00001659sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000014E4d0000165Asv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000014E4d0000165Bsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000014E4d0000165Dsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000014E4d0000165Esv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000014E4d0000165Fsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000014E4d00001665sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000014E4d00001668sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000014E4d00001669sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000014E4d0000166Asv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000014E4d0000166Bsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000014E4d0000166Esv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000014E4d00001672sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000014E4d00001673sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000014E4d00001674sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000014E4d00001676sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000014E4d00001677sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000014E4d00001678sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000014E4d00001679sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000014E4d0000167Asv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000014E4d0000167Bsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000014E4d0000167Dsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000014E4d0000167Esv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000014E4d0000167Fsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000014E4d00001680sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000014E4d00001681sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000014E4d00001682sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000014E4d00001683sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000014E4d00001684sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000014E4d00001686sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000014E4d00001687sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000014E4d00001688sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000014E4d00001689sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000014E4d00001690sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000014E4d00001691sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000014E4d00001692sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000014E4d00001692sv00001025sd00000601bc*sc*i*)
Supplements:    modalias(pci:v000014E4d00001692sv00001025sd00000612bc*sc*i*)
Supplements:    modalias(pci:v000014E4d00001693sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000014E4d00001693sv000017AAsd00003056bc*sc*i*)
Supplements:    modalias(pci:v000014E4d00001694sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000014E4d00001696sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000014E4d00001698sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000014E4d00001699sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000014E4d0000169Asv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000014E4d0000169Bsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000014E4d0000169Csv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000014E4d0000169Dsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000014E4d000016A0sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000014E4d000016A6sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000014E4d000016A7sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000014E4d000016A8sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000014E4d000016B0sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000014E4d000016B1sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000014E4d000016B2sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000014E4d000016B3sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000014E4d000016B4sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000014E4d000016B5sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000014E4d000016B6sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000014E4d000016B7sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000014E4d000016C6sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000014E4d000016C7sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000014E4d000016DDsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000014E4d000016F3sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000014E4d000016F7sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000014E4d000016FDsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000014E4d000016FEsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000014E4d0000170Dsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000014E4d0000170Esv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000014E4d00001712sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000014E4d00001713sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v0000173Bd000003E8sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v0000173Bd000003E9sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v0000173Bd000003EAsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v0000173Bd000003EBsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000010B7d00009900sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000010B7d00009902sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000010B7d00009903sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000010B7d00009904sv*sd00001000bc*sc*i*)
Supplements:    modalias(pci:v000010B7d00009904sv*sd00001102bc*sc*i*)
Supplements:    modalias(pci:v000010B7d00009904sv*sd00002000bc*sc*i*)
Supplements:    modalias(pci:v000010B7d00009905sv*sd00001101bc*sc*i*)
Supplements:    modalias(pci:v000010B7d00009905sv*sd00001102bc*sc*i*)
Supplements:    modalias(pci:v000010B7d00009905sv*sd00002101bc*sc*i*)
Supplements:    modalias(pci:v000010B7d00009905sv*sd00002102bc*sc*i*)
Supplements:    modalias(pci:v000010B7d00009908sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000010B7d00009909sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000010B7d0000990Asv*sd*bc*sc*i*)

%description
This package contains kernel firmware files for various network drivers.


%prep
%autosetup -a1 -p1
# strip down WHENCE for the topic
scripts/strip-topic-whence.sh network < WHENCE > WHENCE.new
mv WHENCE.new WHENCE

%build
# nothing to do

%install
./copy-firmware.sh -v --xz -j1 %{buildroot}%{_firmwaredir}
scripts/install-licenses.sh network %{buildroot}%{_licensedir}/%{name}
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
