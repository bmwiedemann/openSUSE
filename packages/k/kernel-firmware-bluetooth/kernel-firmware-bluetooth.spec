#
# spec file for package kernel-firmware-bluetooth
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
%define git_version c1a774f36657e30e28a83002a8ebf5add44e02aa

Name:           kernel-firmware-bluetooth
Version:        20250408
Release:        0
Summary:        Kernel firmware files for various Bluetooth drivers
License:        GPL-2.0-or-later AND SUSE-Firmware
Group:          System/Kernel
URL:            https://git.kernel.org/cgit/linux/kernel/git/firmware/linux-firmware.git/
Source0:        %{name}-%{version}.tar.xz
Source1:        https://github.com/openSUSE/kernel-firmware-tools/archive/refs/tags/20250409.tar.gz#/kernel-firmware-tools-20250409.tar.gz
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
# make sure we have post-usrmerge filesystem package on TW
Conflicts:      filesystem < 84
%endif
Supplements:    modalias(of:N*T*Cusb1286%2C204e)
Supplements:    modalias(of:N*T*Cusb1286%2C204eC*)
Supplements:    modalias(of:N*T*Cusb4ca%2C301a)
Supplements:    modalias(of:N*T*Cusb4ca%2C301aC*)
Supplements:    modalias(of:N*T*Cusbcf3%2Ce300)
Supplements:    modalias(of:N*T*Cusbcf3%2Ce300C*)
Supplements:    modalias(usb:v*p*d*dc*dsc*dp*icE0isc01ip01in*)
Supplements:    modalias(usb:v*p*d*dcE0dsc01dp01ic*isc*ip*in*)
Supplements:    modalias(usb:v*p*d*dcE0dsc01dp04ic*isc*ip*in*)
Supplements:    modalias(usb:v044Ep3001d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v044Ep3002d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0489p*d*dc*dsc*dp*icFFisc01ip01in*)
Supplements:    modalias(usb:v04BFp030Ad*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v04CAp*d*dc*dsc*dp*icFFisc01ip01in*)
Supplements:    modalias(usb:v050Dp*d*dc*dsc*dp*icFFisc01ip01in*)
Supplements:    modalias(usb:v057Cp3800d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v05ACp*d*dc*dsc*dp*icFFisc01ip01in*)
Supplements:    modalias(usb:v05ACp8213d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v05ACp8215d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v05ACp8218d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v05ACp821Ad*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v05ACp821Bd*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v05ACp821Fd*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v05ACp8281d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0930p*d*dc*dsc*dp*icFFisc01ip01in*)
Supplements:    modalias(usb:v0A5Cp*d*dc*dsc*dp*icFFisc01ip01in*)
Supplements:    modalias(usb:v0A5Cp21E1d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0B05p*d*dc*dsc*dp*icFFisc01ip01in*)
Supplements:    modalias(usb:v0BB4p*d*dc*dsc*dp*icFFisc01ip01in*)
Supplements:    modalias(usb:v0BDBp1002d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0C10p0000d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v0E8Dp763Fd*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v105Bp*d*dc*dsc*dp*icFFisc01ip01in*)
Supplements:    modalias(usb:v13D3p*d*dc*dsc*dp*icFFisc01ip01in*)
Supplements:    modalias(usb:v19FFp0239d*dc*dsc*dp*ic*isc*ip*in*)
Supplements:    modalias(usb:v413Cp*d*dc*dsc*dp*icFFisc01ip01in*)
Supplements:    modalias(usb:v8087p0A5Ad*dc*dsc*dp*ic*isc*ip*in*)

%description
This package contains kernel firmware files for various Bluetooth drivers.

%prep
%autosetup -p1
tar xf %{S:1} --strip-components=1
# strip down WHENCE for the topic
scripts/strip-topic-whence.sh bluetooth < WHENCE > WHENCE.new
mv WHENCE.new WHENCE

%build
# nothing to do

%install
./copy-firmware.sh -v --xz -j1 %{buildroot}%{_firmwaredir}
scripts/install-licenses.sh bluetooth %{buildroot}%{_licensedir}/%{name}
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
