#
# spec file for package kernel-firmware-amdgpu
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
%define git_version 5faab136de1a0f70f9bdcb3d9e29e7261aeeb9b4

Name:           kernel-firmware-amdgpu
Version:        20250219
Release:        0
Summary:        Kernel firmware files for AMDGPU graphics driver
License:        GPL-2.0-or-later AND SUSE-Firmware
Group:          System/Kernel
URL:            https://git.kernel.org/cgit/linux/kernel/git/firmware/linux-firmware.git/
Source0:        %{name}-%{version}.tar.xz
# URL:          https://github.com/openSUSE/kernel-firmware-tools/
Source1:        kernel-firmware-tools-20250218.tar.xz
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
Supplements:    modalias(pci:v00001002d*sv*sd*bc03sc00i00*)
Supplements:    modalias(pci:v00001002d*sv*sd*bc03sc80i00*)
Supplements:    modalias(pci:v00001002d*sv*sd*bc12sc00i00*)
Supplements:    modalias(pci:v00001002d00001304sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00001305sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00001306sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00001307sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00001309sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d0000130Asv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d0000130Bsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d0000130Csv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d0000130Dsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d0000130Esv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d0000130Fsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00001310sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00001311sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00001312sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00001313sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00001315sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00001316sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00001317sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00001318sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d0000131Bsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d0000131Csv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d0000131Dsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d000013FEsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d0000143Fsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d000015D8sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d000015DDsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d000015E7sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00001636sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00001638sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d0000164Csv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d0000164Dsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00001681sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00006600sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00006601sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00006602sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00006603sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00006604sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00006605sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00006606sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00006607sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00006608sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00006610sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00006611sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00006613sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00006617sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00006620sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00006621sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00006623sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00006631sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00006640sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00006641sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00006646sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00006647sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00006649sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00006650sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00006651sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00006658sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d0000665Csv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d0000665Dsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d0000665Fsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00006660sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00006663sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00006664sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00006665sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00006667sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d0000666Fsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d000066A0sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d000066A1sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d000066A2sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d000066A3sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d000066A4sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d000066A7sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d000066AFsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00006780sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00006784sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00006788sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d0000678Asv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00006790sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00006791sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00006792sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00006798sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00006799sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d0000679Asv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d0000679Bsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d0000679Esv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d0000679Fsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d000067A0sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d000067A1sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d000067A2sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d000067A8sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d000067A9sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d000067AAsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d000067B0sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d000067B1sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d000067B8sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d000067B9sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d000067BAsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d000067BEsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d000067C0sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d000067C1sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d000067C2sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d000067C4sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d000067C7sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d000067C8sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d000067C9sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d000067CAsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d000067CCsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d000067CFsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d000067D0sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d000067DFsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d000067E0sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d000067E1sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d000067E3sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d000067E7sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d000067E8sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d000067E9sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d000067EBsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d000067EFsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d000067FFsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00006800sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00006801sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00006802sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00006806sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00006808sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00006809sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00006810sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00006811sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00006816sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00006817sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00006818sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00006819sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00006820sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00006821sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00006822sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00006823sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00006824sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00006825sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00006826sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00006827sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00006828sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00006829sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d0000682Asv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d0000682Bsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d0000682Csv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d0000682Dsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d0000682Fsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00006830sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00006831sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00006835sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00006837sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00006838sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00006839sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d0000683Bsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d0000683Dsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d0000683Fsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00006860sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00006861sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00006862sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00006863sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00006864sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00006867sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00006868sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00006869sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d0000686Asv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d0000686Bsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d0000686Csv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d0000686Dsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d0000686Esv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d0000686Fsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d0000687Fsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00006900sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00006901sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00006902sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00006903sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00006907sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00006920sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00006921sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00006928sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00006929sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d0000692Bsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d0000692Fsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00006930sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00006938sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00006939sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d0000694Csv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d0000694Esv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d0000694Fsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00006980sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00006981sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00006985sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00006986sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00006987sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00006995sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00006997sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d0000699Fsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d000069A0sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d000069A1sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d000069A2sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d000069A3sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d000069AFsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00006FDFsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00007300sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d0000730Fsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00007310sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00007312sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00007318sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00007319sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d0000731Asv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d0000731Bsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d0000731Esv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d0000731Fsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00007340sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00007341sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00007347sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d0000734Fsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00007360sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00007362sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00007388sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d0000738Csv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d0000738Esv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00007390sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d000073A0sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d000073A1sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d000073A2sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d000073A3sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d000073A5sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d000073A8sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d000073A9sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d000073ABsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d000073ACsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d000073ADsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d000073AEsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d000073AFsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d000073BFsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d000073C0sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d000073C1sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d000073C3sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d000073DAsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d000073DBsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d000073DCsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d000073DDsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d000073DEsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d000073DFsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d000073E0sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d000073E1sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d000073E2sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d000073E3sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d000073E8sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d000073E9sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d000073EAsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d000073EBsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d000073ECsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d000073EDsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d000073EFsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d000073FFsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00007408sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d0000740Csv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d0000740Fsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00007410sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00007420sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00007421sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00007422sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00007423sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00007424sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d0000743Fsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00009830sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00009831sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00009832sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00009833sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00009834sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00009835sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00009836sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00009837sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00009838sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00009839sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d0000983Asv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d0000983Bsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d0000983Csv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d0000983Dsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d0000983Esv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d0000983Fsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00009850sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00009851sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00009852sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00009853sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00009854sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00009855sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00009856sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00009857sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00009858sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00009859sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d0000985Asv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d0000985Bsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d0000985Csv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d0000985Dsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d0000985Esv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d0000985Fsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00009870sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00009874sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00009875sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00009876sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d00009877sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001002d000098E4sv*sd*bc*sc*i*)

%description
This package contains kernel firmware files for AMDGPU graphics driver.

%prep
%autosetup -a1 -p1
# strip down WHENCE for the topic
scripts/strip-topic-whence.sh amdgpu < WHENCE > WHENCE.new
mv WHENCE.new WHENCE

%build
# nothing to do

%install
./copy-firmware.sh -v --xz -j1 %{buildroot}%{_firmwaredir}
scripts/install-licenses.sh amdgpu %{buildroot}%{_licensedir}/%{name}
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
