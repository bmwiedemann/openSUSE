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
%define git_version 8b4de42e3432d1cdea4df82b2971486e143258f9

Name:           kernel-firmware-nvidia
Version:        20251018
Release:        0
Summary:        Kernel firmware files for Nvidia Tegra and graphics drivers
License:        GPL-2.0-or-later AND SUSE-Firmware
Group:          System/Kernel
URL:            https://git.kernel.org/cgit/linux/kernel/git/firmware/linux-firmware.git/
Source0:        %{name}-%{version}.tar.xz
Source1:        https://github.com/openSUSE/kernel-firmware-tools/archive/refs/tags/20251004.tar.gz#/kernel-firmware-tools-20251004.tar.gz
Source2:        %{name}-rpmlintrc
Source3:        git_id
Source10:       aliases
Source11:       post
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
Supplements:    modalias(of:N*T*Cnvidia%2Cgk20a)
Supplements:    modalias(of:N*T*Cnvidia%2Cgk20aC*)
Supplements:    modalias(of:N*T*Cnvidia%2Cgm20b)
Supplements:    modalias(of:N*T*Cnvidia%2Cgm20bC*)
Supplements:    modalias(of:N*T*Cnvidia%2Cgp10b)
Supplements:    modalias(of:N*T*Cnvidia%2Cgp10bC*)
Supplements:    modalias(of:N*T*Cnvidia%2Ctegra114-dc)
Supplements:    modalias(of:N*T*Cnvidia%2Ctegra114-dcC*)
Supplements:    modalias(of:N*T*Cnvidia%2Ctegra114-dsi)
Supplements:    modalias(of:N*T*Cnvidia%2Ctegra114-dsiC*)
Supplements:    modalias(of:N*T*Cnvidia%2Ctegra114-gr2d)
Supplements:    modalias(of:N*T*Cnvidia%2Ctegra114-gr2dC*)
Supplements:    modalias(of:N*T*Cnvidia%2Ctegra114-gr3d)
Supplements:    modalias(of:N*T*Cnvidia%2Ctegra114-gr3dC*)
Supplements:    modalias(of:N*T*Cnvidia%2Ctegra114-hdmi)
Supplements:    modalias(of:N*T*Cnvidia%2Ctegra114-hdmiC*)
Supplements:    modalias(of:N*T*Cnvidia%2Ctegra124-dc)
Supplements:    modalias(of:N*T*Cnvidia%2Ctegra124-dcC*)
Supplements:    modalias(of:N*T*Cnvidia%2Ctegra124-dpaux)
Supplements:    modalias(of:N*T*Cnvidia%2Ctegra124-dpauxC*)
Supplements:    modalias(of:N*T*Cnvidia%2Ctegra124-dsi)
Supplements:    modalias(of:N*T*Cnvidia%2Ctegra124-dsiC*)
Supplements:    modalias(of:N*T*Cnvidia%2Ctegra124-hdmi)
Supplements:    modalias(of:N*T*Cnvidia%2Ctegra124-hdmiC*)
Supplements:    modalias(of:N*T*Cnvidia%2Ctegra124-sor)
Supplements:    modalias(of:N*T*Cnvidia%2Ctegra124-sorC*)
Supplements:    modalias(of:N*T*Cnvidia%2Ctegra124-vic)
Supplements:    modalias(of:N*T*Cnvidia%2Ctegra124-vicC*)
Supplements:    modalias(of:N*T*Cnvidia%2Ctegra124-xusb)
Supplements:    modalias(of:N*T*Cnvidia%2Ctegra124-xusbC*)
Supplements:    modalias(of:N*T*Cnvidia%2Ctegra132-dsi)
Supplements:    modalias(of:N*T*Cnvidia%2Ctegra132-dsiC*)
Supplements:    modalias(of:N*T*Cnvidia%2Ctegra132-sor)
Supplements:    modalias(of:N*T*Cnvidia%2Ctegra132-sorC*)
Supplements:    modalias(of:N*T*Cnvidia%2Ctegra186-dc)
Supplements:    modalias(of:N*T*Cnvidia%2Ctegra186-dcC*)
Supplements:    modalias(of:N*T*Cnvidia%2Ctegra186-display)
Supplements:    modalias(of:N*T*Cnvidia%2Ctegra186-displayC*)
Supplements:    modalias(of:N*T*Cnvidia%2Ctegra186-dpaux)
Supplements:    modalias(of:N*T*Cnvidia%2Ctegra186-dpauxC*)
Supplements:    modalias(of:N*T*Cnvidia%2Ctegra186-nvdec)
Supplements:    modalias(of:N*T*Cnvidia%2Ctegra186-nvdecC*)
Supplements:    modalias(of:N*T*Cnvidia%2Ctegra186-sor)
Supplements:    modalias(of:N*T*Cnvidia%2Ctegra186-sorC*)
Supplements:    modalias(of:N*T*Cnvidia%2Ctegra186-vic)
Supplements:    modalias(of:N*T*Cnvidia%2Ctegra186-vicC*)
Supplements:    modalias(of:N*T*Cnvidia%2Ctegra186-xusb)
Supplements:    modalias(of:N*T*Cnvidia%2Ctegra186-xusbC*)
Supplements:    modalias(of:N*T*Cnvidia%2Ctegra194-dc)
Supplements:    modalias(of:N*T*Cnvidia%2Ctegra194-dcC*)
Supplements:    modalias(of:N*T*Cnvidia%2Ctegra194-display)
Supplements:    modalias(of:N*T*Cnvidia%2Ctegra194-displayC*)
Supplements:    modalias(of:N*T*Cnvidia%2Ctegra194-dpaux)
Supplements:    modalias(of:N*T*Cnvidia%2Ctegra194-dpauxC*)
Supplements:    modalias(of:N*T*Cnvidia%2Ctegra194-nvdec)
Supplements:    modalias(of:N*T*Cnvidia%2Ctegra194-nvdecC*)
Supplements:    modalias(of:N*T*Cnvidia%2Ctegra194-sor)
Supplements:    modalias(of:N*T*Cnvidia%2Ctegra194-sorC*)
Supplements:    modalias(of:N*T*Cnvidia%2Ctegra194-vic)
Supplements:    modalias(of:N*T*Cnvidia%2Ctegra194-vicC*)
Supplements:    modalias(of:N*T*Cnvidia%2Ctegra194-xusb)
Supplements:    modalias(of:N*T*Cnvidia%2Ctegra194-xusbC*)
Supplements:    modalias(of:N*T*Cnvidia%2Ctegra20-dc)
Supplements:    modalias(of:N*T*Cnvidia%2Ctegra20-dcC*)
Supplements:    modalias(of:N*T*Cnvidia%2Ctegra20-gr2d)
Supplements:    modalias(of:N*T*Cnvidia%2Ctegra20-gr2dC*)
Supplements:    modalias(of:N*T*Cnvidia%2Ctegra20-gr3d)
Supplements:    modalias(of:N*T*Cnvidia%2Ctegra20-gr3dC*)
Supplements:    modalias(of:N*T*Cnvidia%2Ctegra20-hdmi)
Supplements:    modalias(of:N*T*Cnvidia%2Ctegra20-hdmiC*)
Supplements:    modalias(of:N*T*Cnvidia%2Ctegra210-dc)
Supplements:    modalias(of:N*T*Cnvidia%2Ctegra210-dcC*)
Supplements:    modalias(of:N*T*Cnvidia%2Ctegra210-dpaux)
Supplements:    modalias(of:N*T*Cnvidia%2Ctegra210-dpauxC*)
Supplements:    modalias(of:N*T*Cnvidia%2Ctegra210-dsi)
Supplements:    modalias(of:N*T*Cnvidia%2Ctegra210-dsiC*)
Supplements:    modalias(of:N*T*Cnvidia%2Ctegra210-nvdec)
Supplements:    modalias(of:N*T*Cnvidia%2Ctegra210-nvdecC*)
Supplements:    modalias(of:N*T*Cnvidia%2Ctegra210-sor)
Supplements:    modalias(of:N*T*Cnvidia%2Ctegra210-sor1)
Supplements:    modalias(of:N*T*Cnvidia%2Ctegra210-sor1C*)
Supplements:    modalias(of:N*T*Cnvidia%2Ctegra210-sorC*)
Supplements:    modalias(of:N*T*Cnvidia%2Ctegra210-vic)
Supplements:    modalias(of:N*T*Cnvidia%2Ctegra210-vicC*)
Supplements:    modalias(of:N*T*Cnvidia%2Ctegra210-xusb)
Supplements:    modalias(of:N*T*Cnvidia%2Ctegra210-xusbC*)
Supplements:    modalias(of:N*T*Cnvidia%2Ctegra234-nvdec)
Supplements:    modalias(of:N*T*Cnvidia%2Ctegra234-nvdecC*)
Supplements:    modalias(of:N*T*Cnvidia%2Ctegra234-vic)
Supplements:    modalias(of:N*T*Cnvidia%2Ctegra234-vicC*)
Supplements:    modalias(of:N*T*Cnvidia%2Ctegra234-xusb)
Supplements:    modalias(of:N*T*Cnvidia%2Ctegra234-xusbC*)
Supplements:    modalias(of:N*T*Cnvidia%2Ctegra30-dc)
Supplements:    modalias(of:N*T*Cnvidia%2Ctegra30-dcC*)
Supplements:    modalias(of:N*T*Cnvidia%2Ctegra30-gr2d)
Supplements:    modalias(of:N*T*Cnvidia%2Ctegra30-gr2dC*)
Supplements:    modalias(of:N*T*Cnvidia%2Ctegra30-gr3d)
Supplements:    modalias(of:N*T*Cnvidia%2Ctegra30-gr3dC*)
Supplements:    modalias(of:N*T*Cnvidia%2Ctegra30-hdmi)
Supplements:    modalias(of:N*T*Cnvidia%2Ctegra30-hdmiC*)
Supplements:    modalias(pci:v000010DEd*sv*sd*bc03sc*i*)
Supplements:    modalias(pci:v000012D2d*sv*sd*bc03sc*i*)

%description
This package contains kernel firmware files for Nvidia Tegra and graphics drivers.

%prep
%autosetup -p1
tar xf %{S:1} --strip-components=1
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

%pretrans -p <lua>
paths = {"ad103", "ad104", "ad106", "ad107"}
for i = 1, 4 do
  path = "%{_firmwaredir}/nvidia/" .. paths[i]
  st = posix.stat(path)
  if st and st.type == "directory" then
    path2 = path .. ".rpmmoved"
    if not os.rename(path, path2) then
      print("Cannot rename " .. path .. " to " .. path2)
      os.exit(1)
    end
  end
end

%posttrans
for f in ad103 ad104 ad106 ad107; do
  if test -d %{_firmwaredir}/nvidia/$f.rpmmoved; then
    rm -rf %{_firmwaredir}/nvidia/$f.rpmmoved
  fi
done

%files
%doc %{_docdir}/%{name}
%license %{_licensedir}/%{name}
%{_firmwaredir}

%changelog
