#
# spec file for package kernel-firmware-qlogic
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

Name:           kernel-firmware-qlogic
Version:        20250206
Release:        0
Summary:        Kernel firmware files for QLogic network drivers
License:        SUSE-Firmware AND GPL-2.0-or-later AND GPL-2.0-only
Group:          System/Kernel
URL:            https://git.kernel.org/cgit/linux/kernel/git/firmware/linux-firmware.git/
Source0:        %{name}-%{version}.tar.xz
# URL:          https://github.com/openSUSE/kernel-firmware-tools/
Source1:        kernel-firmware-tools-20250211.tar.xz
Source2:        %{name}-rpmlintrc
Source3:        git_id
Source10:       aliases
Source11:       extrawhence
Source12:       ql2600_fw.bin
Source13:       ql2700_fw.bin
Source14:       ql8300_fw.bin
Source15:       topicprovs
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
Provides:       qlogic-firmware = %{version}
Obsoletes:      qlogic-firmware < %{version}
Supplements:    modalias(pci:v00001657d00000013sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001657d00000014sv*sd*bc0Csc04i00*)
Supplements:    modalias(pci:v00001657d00000017sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001657d00000021sv*sd*bc0Csc04i00*)
Supplements:    modalias(pci:v00001657d00000022sv*sd*bc0Csc04i00*)
Supplements:    modalias(pci:v00001657d00000023sv*sd*bc0Csc04i00*)
Supplements:    modalias(pci:v00001657d00000014sv*sd*bc02sc00i*)
Supplements:    modalias(pci:v00001657d00000022sv*sd*bc02sc00i*)
Supplements:    modalias(fs-ipathfs)
Supplements:    modalias(pci:v00001077d00007220sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001077d00007322sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001FC1d00000010sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001077d00001634sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001077d00001636sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001077d00001644sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001077d00001654sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001077d00001656sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001077d00001664sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001077d00001666sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001077d00008070sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001077d00008090sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001077d0000165Csv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001077d00008080sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001077d0000165Esv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001077d00008084sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001077d00001016sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001077d00001020sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001077d00001080sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001077d00001216sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001077d00001240sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001077d00001280sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001077d00002031sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001077d00002061sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001077d00002071sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001077d00002081sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001077d00002089sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001077d00002100sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001077d00002200sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001077d00002261sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001077d00002271sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001077d00002281sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001077d00002289sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001077d00002300sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001077d00002312sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001077d00002322sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001077d00002422sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001077d00002432sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001077d00002532sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001077d00005422sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001077d00005432sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001077d00006312sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001077d00006322sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001077d00008001sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001077d00008021sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001077d00008031sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001077d00008044sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001077d00008432sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001077d0000F001sv*sd*bc*sc*i*)

%description
This package contains kernel firmware files for QLogic network drivers.


%prep
%autosetup -a1 -p1
# strip down WHENCE for the topic
scripts/strip-topic-whence.sh qlogic < WHENCE > WHENCE.new
mv WHENCE.new WHENCE
scripts/extra-whence-setup.sh %{_sourcedir}

%build
# nothing to do

%install
./copy-firmware.sh -v --xz -j1 %{buildroot}%{_firmwaredir}
scripts/install-licenses.sh qlogic %{buildroot}%{_licensedir}/%{name}
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
