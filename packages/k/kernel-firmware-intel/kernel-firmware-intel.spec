#
# spec file for package kernel-firmware-intel
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

Name:           kernel-firmware-intel
Version:        20250206
Release:        0
Summary:        Kernel firmware files for Intel-platform device drivers
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
Supplements:    modalias(pci:v00008086d00000F38sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d00001178sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d00001179sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d0000117Asv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d00001478sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d000022B8sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d000024F0sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d000024F1sv*sd*bc*sc*i*)
Supplements:    modalias(auxiliary:intel_ipu6.isys)
Supplements:    modalias(pci:v00008086d000002FCsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d000006FCsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d00000AA2sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d00001AA2sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d000022D8sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d000031A2sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d000034FCsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d000043FCsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d00004BB3sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d000051FCsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d000054FCsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d00005AA2sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d00007745sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d00007A78sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d00007AF8sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d00007E45sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d00007F78sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d00009D35sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d00009DFCsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d0000A0FCsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d0000A135sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d0000A37Csv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d0000A845sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d00001919sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d00001D60sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d00001D61sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d00001D62sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d00001D63sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d00001D64sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d00001D65sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d00001D66sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d00001D67sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d00001D68sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d00001D69sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d00001D6Asv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d00001D6Bsv*sd*bc*sc*i*)
Supplements:    modalias(acpi*:INTC1009%3A*)
Supplements:    modalias(acpi*:INTC1058%3A*)
Supplements:    modalias(acpi*:INTC1094%3A*)
Supplements:    modalias(acpi*:INTC10D0%3A*)
Supplements:    modalias(pci:v00008086d000019E2sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d000037C8sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d00000435sv*sd*bc*sc*i*)

%description
This package contains kernel firmware files for Intel-platform device drivers.


%prep
%autosetup -a1 -p1
# strip down WHENCE for the topic
scripts/strip-topic-whence.sh intel < WHENCE > WHENCE.new
mv WHENCE.new WHENCE

%build
# nothing to do

%install
./copy-firmware.sh -v --xz -j1 %{buildroot}%{_firmwaredir}
scripts/install-licenses.sh intel %{buildroot}%{_licensedir}/%{name}
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
