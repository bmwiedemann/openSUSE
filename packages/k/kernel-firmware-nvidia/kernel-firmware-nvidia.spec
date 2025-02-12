#
# spec file for package kernel-firmware-nvidia
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

Name:           kernel-firmware-nvidia
Version:        20250206
Release:        0
Summary:        Kernel firmware files for Nvidia Tegra and graphics drivers
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
Supplements:    modalias(of:N*T*Cnvidia,gk20a)
Supplements:    modalias(of:N*T*Cnvidia,gk20aC*)
Supplements:    modalias(of:N*T*Cnvidia,gm20b)
Supplements:    modalias(of:N*T*Cnvidia,gm20bC*)
Supplements:    modalias(of:N*T*Cnvidia,gp10b)
Supplements:    modalias(of:N*T*Cnvidia,gp10bC*)
Supplements:    modalias(pci:v000010DEd*sv*sd*bc03sc*i*)
Supplements:    modalias(pci:v000012D2d*sv*sd*bc03sc*i*)
Supplements:    modalias(of:N*T*Cnvidia,tegra114-dc)
Supplements:    modalias(of:N*T*Cnvidia,tegra114-dcC*)
Supplements:    modalias(of:N*T*Cnvidia,tegra114-dsi)
Supplements:    modalias(of:N*T*Cnvidia,tegra114-dsiC*)
Supplements:    modalias(of:N*T*Cnvidia,tegra114-gr2d)
Supplements:    modalias(of:N*T*Cnvidia,tegra114-gr2dC*)
Supplements:    modalias(of:N*T*Cnvidia,tegra114-gr3d)
Supplements:    modalias(of:N*T*Cnvidia,tegra114-gr3dC*)
Supplements:    modalias(of:N*T*Cnvidia,tegra114-hdmi)
Supplements:    modalias(of:N*T*Cnvidia,tegra114-hdmiC*)
Supplements:    modalias(of:N*T*Cnvidia,tegra124-dc)
Supplements:    modalias(of:N*T*Cnvidia,tegra124-dcC*)
Supplements:    modalias(of:N*T*Cnvidia,tegra124-dpaux)
Supplements:    modalias(of:N*T*Cnvidia,tegra124-dpauxC*)
Supplements:    modalias(of:N*T*Cnvidia,tegra124-dsi)
Supplements:    modalias(of:N*T*Cnvidia,tegra124-dsiC*)
Supplements:    modalias(of:N*T*Cnvidia,tegra124-hdmi)
Supplements:    modalias(of:N*T*Cnvidia,tegra124-hdmiC*)
Supplements:    modalias(of:N*T*Cnvidia,tegra124-sor)
Supplements:    modalias(of:N*T*Cnvidia,tegra124-sorC*)
Supplements:    modalias(of:N*T*Cnvidia,tegra124-vic)
Supplements:    modalias(of:N*T*Cnvidia,tegra124-vicC*)
Supplements:    modalias(of:N*T*Cnvidia,tegra132-dsi)
Supplements:    modalias(of:N*T*Cnvidia,tegra132-dsiC*)
Supplements:    modalias(of:N*T*Cnvidia,tegra132-sor)
Supplements:    modalias(of:N*T*Cnvidia,tegra132-sorC*)
Supplements:    modalias(of:N*T*Cnvidia,tegra186-dc)
Supplements:    modalias(of:N*T*Cnvidia,tegra186-dcC*)
Supplements:    modalias(of:N*T*Cnvidia,tegra186-display)
Supplements:    modalias(of:N*T*Cnvidia,tegra186-displayC*)
Supplements:    modalias(of:N*T*Cnvidia,tegra186-dpaux)
Supplements:    modalias(of:N*T*Cnvidia,tegra186-dpauxC*)
Supplements:    modalias(of:N*T*Cnvidia,tegra186-nvdec)
Supplements:    modalias(of:N*T*Cnvidia,tegra186-nvdecC*)
Supplements:    modalias(of:N*T*Cnvidia,tegra186-sor)
Supplements:    modalias(of:N*T*Cnvidia,tegra186-sorC*)
Supplements:    modalias(of:N*T*Cnvidia,tegra186-vic)
Supplements:    modalias(of:N*T*Cnvidia,tegra186-vicC*)
Supplements:    modalias(of:N*T*Cnvidia,tegra194-dc)
Supplements:    modalias(of:N*T*Cnvidia,tegra194-dcC*)
Supplements:    modalias(of:N*T*Cnvidia,tegra194-display)
Supplements:    modalias(of:N*T*Cnvidia,tegra194-displayC*)
Supplements:    modalias(of:N*T*Cnvidia,tegra194-dpaux)
Supplements:    modalias(of:N*T*Cnvidia,tegra194-dpauxC*)
Supplements:    modalias(of:N*T*Cnvidia,tegra194-nvdec)
Supplements:    modalias(of:N*T*Cnvidia,tegra194-nvdecC*)
Supplements:    modalias(of:N*T*Cnvidia,tegra194-sor)
Supplements:    modalias(of:N*T*Cnvidia,tegra194-sorC*)
Supplements:    modalias(of:N*T*Cnvidia,tegra194-vic)
Supplements:    modalias(of:N*T*Cnvidia,tegra194-vicC*)
Supplements:    modalias(of:N*T*Cnvidia,tegra20-dc)
Supplements:    modalias(of:N*T*Cnvidia,tegra20-dcC*)
Supplements:    modalias(of:N*T*Cnvidia,tegra20-gr2d)
Supplements:    modalias(of:N*T*Cnvidia,tegra20-gr2dC*)
Supplements:    modalias(of:N*T*Cnvidia,tegra20-gr3d)
Supplements:    modalias(of:N*T*Cnvidia,tegra20-gr3dC*)
Supplements:    modalias(of:N*T*Cnvidia,tegra20-hdmi)
Supplements:    modalias(of:N*T*Cnvidia,tegra20-hdmiC*)
Supplements:    modalias(of:N*T*Cnvidia,tegra210-dc)
Supplements:    modalias(of:N*T*Cnvidia,tegra210-dcC*)
Supplements:    modalias(of:N*T*Cnvidia,tegra210-dpaux)
Supplements:    modalias(of:N*T*Cnvidia,tegra210-dpauxC*)
Supplements:    modalias(of:N*T*Cnvidia,tegra210-dsi)
Supplements:    modalias(of:N*T*Cnvidia,tegra210-dsiC*)
Supplements:    modalias(of:N*T*Cnvidia,tegra210-nvdec)
Supplements:    modalias(of:N*T*Cnvidia,tegra210-nvdecC*)
Supplements:    modalias(of:N*T*Cnvidia,tegra210-sor)
Supplements:    modalias(of:N*T*Cnvidia,tegra210-sor1)
Supplements:    modalias(of:N*T*Cnvidia,tegra210-sor1C*)
Supplements:    modalias(of:N*T*Cnvidia,tegra210-sorC*)
Supplements:    modalias(of:N*T*Cnvidia,tegra210-vic)
Supplements:    modalias(of:N*T*Cnvidia,tegra210-vicC*)
Supplements:    modalias(of:N*T*Cnvidia,tegra234-nvdec)
Supplements:    modalias(of:N*T*Cnvidia,tegra234-nvdecC*)
Supplements:    modalias(of:N*T*Cnvidia,tegra234-vic)
Supplements:    modalias(of:N*T*Cnvidia,tegra234-vicC*)
Supplements:    modalias(of:N*T*Cnvidia,tegra30-dc)
Supplements:    modalias(of:N*T*Cnvidia,tegra30-dcC*)
Supplements:    modalias(of:N*T*Cnvidia,tegra30-gr2d)
Supplements:    modalias(of:N*T*Cnvidia,tegra30-gr2dC*)
Supplements:    modalias(of:N*T*Cnvidia,tegra30-gr3d)
Supplements:    modalias(of:N*T*Cnvidia,tegra30-gr3dC*)
Supplements:    modalias(of:N*T*Cnvidia,tegra30-hdmi)
Supplements:    modalias(of:N*T*Cnvidia,tegra30-hdmiC*)
Supplements:    modalias(of:N*T*Cnvidia,tegra124-xusb)
Supplements:    modalias(of:N*T*Cnvidia,tegra124-xusbC*)
Supplements:    modalias(of:N*T*Cnvidia,tegra186-xusb)
Supplements:    modalias(of:N*T*Cnvidia,tegra186-xusbC*)
Supplements:    modalias(of:N*T*Cnvidia,tegra194-xusb)
Supplements:    modalias(of:N*T*Cnvidia,tegra194-xusbC*)
Supplements:    modalias(of:N*T*Cnvidia,tegra210-xusb)
Supplements:    modalias(of:N*T*Cnvidia,tegra210-xusbC*)
Supplements:    modalias(of:N*T*Cnvidia,tegra234-xusb)
Supplements:    modalias(of:N*T*Cnvidia,tegra234-xusbC*)

%description
This package contains kernel firmware files for Nvidia Tegra and graphics drivers.


%prep
%autosetup -a1 -p1
# strip down WHENCE for the topic
scripts/strip-topic-whence.sh nvidia < WHENCE > WHENCE.new
mv WHENCE.new WHENCE

%build
# nothing to do

%install
./copy-firmware.sh -v --xz -j1 %{buildroot}%{_firmwaredir}
scripts/install-licenses.sh nvidia %{buildroot}%{_licensedir}/%{name}
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
