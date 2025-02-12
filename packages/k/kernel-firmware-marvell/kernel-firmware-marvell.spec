#
# spec file for package kernel-firmware-marvell
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

Name:           kernel-firmware-marvell
Version:        20250206
Release:        0
Summary:        Kernel firmware files for Marvell network drivers
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
Supplements:    modalias(sdio:c*v02DFd9103*)
Supplements:    modalias(sdio:c*v02DFd9104*)
Supplements:    modalias(usb:v05A3p8388d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1286p2001d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(pci:v000011ABd00002A0Asv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000011ABd00002A0Csv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000011ABd00002A24sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000011ABd00002A2Bsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000011ABd00002A30sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000011ABd00002A40sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000011ABd00002A41sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000011ABd00002A42sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000011ABd00002A43sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000011ABd00002B36sv*sd*bc*sc*i*)
Supplements:    modalias(usb:v05A3p8388d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1286p2001d*dc*dsc*dp*ic*isc*ip*in*)

%description
This package contains kernel firmware files for Marvell network drivers.


%prep
%autosetup -a1 -p1
# strip down WHENCE for the topic
scripts/strip-topic-whence.sh marvell < WHENCE > WHENCE.new
mv WHENCE.new WHENCE

%build
# nothing to do

%install
./copy-firmware.sh -v --xz -j1 %{buildroot}%{_firmwaredir}
scripts/install-licenses.sh marvell %{buildroot}%{_licensedir}/%{name}
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
