#
# spec file for package kernel-firmware-ath10k
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
%define git_version 536cc58d9db164b0e2a47f7f33996b0cf194691a

Name:           kernel-firmware-ath10k
Version:        20251205
Release:        0
Summary:        Kernel firmware files for Atheros QCA988x WiFi drivers
License:        GPL-2.0-or-later AND SUSE-Firmware
Group:          System/Kernel
URL:            https://git.kernel.org/cgit/linux/kernel/git/firmware/linux-firmware.git/
Source0:        %{name}-%{version}.tar.xz
Source1:        https://github.com/openSUSE/kernel-firmware-tools/archive/refs/tags/20251118.tar.gz#/kernel-firmware-tools-20251118.tar.gz
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
Supplements:    modalias(of:N*T*Cqcom%2Cipq4019-wifi)
Supplements:    modalias(of:N*T*Cqcom%2Cipq4019-wifiC*)
Supplements:    modalias(pci:v00000777d000011ACsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v0000168Cd0000003Csv*sd*bc*sc*i*)
Supplements:    modalias(pci:v0000168Cd0000003Esv*sd*bc*sc*i*)
Supplements:    modalias(pci:v0000168Cd00000040sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v0000168Cd00000041sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v0000168Cd00000042sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v0000168Cd00000046sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v0000168Cd00000050sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v0000168Cd00000056sv*sd*bc*sc*i*)
Supplements:    modalias(sdio:c*v0271d050A*)
Supplements:    modalias(sdio:c*v0271d0701*)
Supplements:    modalias(usb:v13B1p0042d*dc*dsc*dp*ic*isc*ip*in*)

%description
This package contains kernel firmware files for Atheros QCA988x WiFi drivers.

%prep
%autosetup -p1
tar xf %{S:1} --strip-components=1
# strip down WHENCE for the topic
scripts/strip-topic-whence.sh ath10k < WHENCE > WHENCE.new
mv WHENCE.new WHENCE

%build
# nothing to do

%install
./copy-firmware.sh -v --xz -j1 %{buildroot}%{_firmwaredir}
scripts/install-licenses.sh ath10k %{buildroot}%{_licensedir}/%{name}
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
