#
# spec file for package kernel-firmware-serial
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
%define git_version f40eafe216833d083f4e5598b7f45e894c373ad1

Name:           kernel-firmware-serial
Version:        20250627
Release:        0
Summary:        Kernel firmware files for various serial drivers
License:        GPL-2.0-or-later AND SUSE-Firmware AND GPL-2.0-only
Group:          System/Kernel
URL:            https://git.kernel.org/cgit/linux/kernel/git/firmware/linux-firmware.git/
Source0:        %{name}-%{version}.tar.xz
Source1:        https://github.com/openSUSE/kernel-firmware-tools/archive/refs/tags/20250630.tar.gz#/kernel-firmware-tools-20250630.tar.gz
Source2:        %{name}-rpmlintrc
Source3:        git_id
Source10:       aliases
BuildRequires:  suse-module-tools
Requires(post): %{_bindir}/mkdir
Requires(post): %{_bindir}/touch
Requires(postun): %{_bindir}/mkdir
Requires(postun): %{_bindir}/touch
Requires(post): dracut >= 049
Conflicts:      kernel < 5.3
Conflicts:      kernel-firmware-uncompressed
BuildArch:      noarch
%if 0%{?suse_version} >= 1550
Conflicts:      (filesystem without may-perform-usrmerge)
%endif
Supplements:    modalias(pci:v000011FEd00000040sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000011FEd00000041sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000011FEd00000042sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000011FEd00000043sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000011FEd00000044sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000011FEd00000045sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000011FEd00000046sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000011FEd00000047sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000011FEd0000004Asv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000011FEd0000004Bsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000011FEd0000004Csv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000011FEd0000004Dsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000011FEd0000004Esv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000011FEd0000004Fsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000011FEd00000050sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000011FEd00000051sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000011FEd00000052sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000011FEd00000060sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000011FEd00000061sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000011FEd00000062sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000011FEd00000063sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000011FEd00000064sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000011FEd00000065sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000011FEd00000066sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000011FEd00000067sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000011FEd00000068sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000011FEd00000072sv*sd*bc*sc*i*)
Supplements:    modalias(usb:v0404p0202d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0404p0203d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0404p0310d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0404p0311d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0404p0312d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0451p3410d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0451p5052d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0451p5053d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0451p505Ad*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0451p505Fd*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0451p5152d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0451pF430d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v04B3p4543d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v04B3p454Bd*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v04B3p454Cd*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v05D9pA225d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v05D9pA758d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v05D9pA794d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v06CDp0101d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v06CDp0102d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v06CDp0103d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v06CDp0104d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v06CDp0105d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v06CDp0106d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v06CDp0107d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v06CDp0108d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v06CDp0109d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v06CDp010Ad*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v06CDp010Bd*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v06CDp010Cd*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v06CDp010Fd*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v06CDp0110d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v06CDp0112d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v06CDp0113d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v06CDp0114d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v06CDp0115d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v06CDp0118d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v06CDp0119d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v06CDp011Ad*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v06CDp011Bd*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v06CDp011Cd*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v06CDp0121d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v06CDp012Ad*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v06CDp0131d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v06CDp0135d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v06E0p0319d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v06E0pF108d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v06E0pF109d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v06E0pF110d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v06E0pF111d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v06E0pF112d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v06E0pF114d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v06E0pF115d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0710p0001d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0710p8001d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v085Ap8025d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v085Ap8027d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v10ACp0102d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v110Ap1110d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v110Ap1130d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v110Ap1131d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v110Ap1150d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v110Ap1151d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v110Ap1250d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v110Ap1251d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v110Ap1410d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v110Ap1450d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v110Ap1451d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v110Ap1613d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v110Ap1618d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v110Ap1653d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v110Ap1658d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v14B0p3410d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1608p0001d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1608p0002d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1608p0003d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1608p0004d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1608p0005d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1608p0006d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1608p0007d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1608p0008d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1608p000Cd*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1608p000Dd*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1608p000Ed*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1608p000Fd*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1608p0010d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1608p0011d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1608p0012d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1608p0013d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1608p0014d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1608p0018d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1608p0019d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1608p001Ad*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1608p0201d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1608p0205d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1608p0206d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1608p0207d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1608p020Cd*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1608p020Dd*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1608p0212d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1608p0215d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1608p0217d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1608p021Ad*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1608p021Bd*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1608p021Cd*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1608p021Dd*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1608p021Ed*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1608p0240d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1608p0241d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1608p0242d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1608p0243d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1608p0244d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1608p0247d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1608p0301d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1608p0302d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1608p0303d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1608p0304d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1608p0305d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1608p0306d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1608p0307d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1608p0308d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1608p0309d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1608p030Ad*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1608p030Bd*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1608p030Cd*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1608p030Ed*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1608p1403d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1608p1A01d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1645p8093d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1A61p3410d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1A61p3420d*dc*dsc*dp*ic*isc*ip*in*)

%description
This package contains kernel firmware files for various serial drivers.

%prep
%autosetup -p1
tar xf %{S:1} --strip-components=1
# strip down WHENCE for the topic
scripts/strip-topic-whence.sh serial < WHENCE > WHENCE.new
mv WHENCE.new WHENCE

%build
# nothing to do

%install
./copy-firmware.sh -v --xz -j1 %{buildroot}%{_firmwaredir}
scripts/install-licenses.sh serial %{buildroot}%{_licensedir}/%{name}
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
