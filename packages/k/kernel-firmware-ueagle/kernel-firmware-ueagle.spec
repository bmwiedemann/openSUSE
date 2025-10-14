#
# spec file for package kernel-firmware-ueagle
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
%define git_version 757854f42d83aab44a72eedded3485887798a4fd

Name:           kernel-firmware-ueagle
Version:        20251004
Release:        0
Summary:        Kernel firmware files for Eagle IV USB ADSL modem driver
License:        GPL-2.0-or-later AND SUSE-Firmware
Group:          System/Kernel
URL:            https://git.kernel.org/cgit/linux/kernel/git/firmware/linux-firmware.git/
Source0:        %{name}-%{version}.tar.xz
Source1:        https://github.com/openSUSE/kernel-firmware-tools/archive/refs/tags/20251004.tar.gz#/kernel-firmware-tools-20251004.tar.gz
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
Supplements:    modalias(usb:v05CCp3350d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v05CCp3351d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v05CCp3352d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v05CCp3353d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v05CCp3362d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v05CCp3363d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0BAFp00F1d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0BAFp00F2d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0BAFp00F5d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0BAFp00F6d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0BAFp00F7d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0BAFp00F8d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0BAFp00F9d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0BAFp00FAd*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1039p2100d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1039p2101d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1039p2110d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1039p2111d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1039p2120d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1039p2121d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1039p2130d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1039p2131d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1110p9000d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1110p9001d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1110p900Fd*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1110p9010d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1110p9021d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1110p9022d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1110p9023d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1110p9024d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1110p9031d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1110p9032d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1110p9041d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v1110p9042d*dc*dsc*dp*ic*isc*ip*in*)

%description
This package contains kernel firmware files for Eagle IV USB ADSL modem driver.

%prep
%autosetup -p1
tar xf %{S:1} --strip-components=1
# strip down WHENCE for the topic
scripts/strip-topic-whence.sh ueagle < WHENCE > WHENCE.new
mv WHENCE.new WHENCE

%build
# nothing to do

%install
./copy-firmware.sh -v --xz -j1 %{buildroot}%{_firmwaredir}
scripts/install-licenses.sh ueagle %{buildroot}%{_licensedir}/%{name}
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
