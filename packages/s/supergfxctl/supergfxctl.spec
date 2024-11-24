#
# spec file for package supergfxctl
#
# Copyright (c) 2024 SUSE LLC
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


%global rustflags -Clink-arg=-Wl,-z,relro,-z,now

Name:           supergfxctl
Version:        5.2.4
Release:        0
Summary:        Super graphics mode controller
License:        MPL-2.0
URL:            https://gitlab.com/asus-linux/supergfxctl
Source0:        %{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
Source2:        %{name}-user.conf
Source3:        prime-run.sh
Group:          System/Daemons

## Patch for user-groups
Patch1:         user-group.patch

## Upstream GPU detection patch
Patch2:         GPUDetection.patch

BuildRequires:  cargo-packaging
BuildRequires:  pkgconfig
BuildRequires:  sysuser-tools
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(systemd)
Requires:       systemd

Conflicts:      bbswitch
Conflicts:      bumblebee
Conflicts:      bumblebee-status-module-nvidia-optimus-manager
Conflicts:      suse-prime
Conflicts:      system76-power

%sysusers_requires

%description
supergfxctl is a super graphics mode controller for laptops with hybrid nvidia.

%prep
%autosetup -a1 -p1

%build
%cargo_build
%sysusers_generate_pre %{SOURCE2} %{name} %{name}-user.conf

%install
%cargo_install

mkdir -p "%{buildroot}%{_bindir}"
install -D -m 0755 target/release/supergfxd %{buildroot}%{_bindir}/supergfxd
install -D -m 0755 target/release/supergfxctl %{buildroot}%{_bindir}/supergfxctl
install -D -m 0644 data/90-supergfxd-nvidia-pm.rules %{buildroot}%{_udevrulesdir}/90-supergfxd-nvidia-pm.rules
install -D -m 0644 data/org.supergfxctl.Daemon.conf  %{buildroot}%{_sysconfdir}/dbus-1/system.d/org.supergfxctl.Daemon.conf
install -D -m 0644 data/supergfxd.service %{buildroot}%{_unitdir}/supergfxd.service
install -D -m 0644 data/supergfxd.preset %{buildroot}%{_presetdir}/99-supergfxd.preset

install -D -m 0644 LICENSE %{buildroot}%{_datadir}/licenses/%{name}/LICENSE
install -D -m 0644 README.md %{buildroot}%{_datadir}/doc/%{name}/README.md

install -D -m 0644 %{SOURCE2} %{buildroot}%{_sysusersdir}/%{name}-user.conf

install -D -m 0755 %{SOURCE3} %{buildroot}%{_bindir}/prime-run

%pre -f %{name}.pre
%service_add_pre supergfxd.service

%post
%service_add_post supergfxd.service

%preun
%service_del_preun supergfxd.service

%postun
%service_del_postun_with_restart supergfxd.service
if [ -e %{_sysconfdir}/modprobe.d/nvidia.conf ]
then
    if grep -q "# options nvidia-drm.modeset=1" %{_sysconfdir}/modprobe.d/nvidia.conf
    then
        echo "optional nvidia-drm.modeset=1" > %{_sysconfdir}/modprobe.d/nvidia.conf
    fi
fi

%files
%license LICENSE
%{_bindir}/supergfxd
%{_bindir}/supergfxctl
%{_bindir}/prime-run
%{_unitdir}/supergfxd.service
%{_presetdir}/99-supergfxd.preset
%{_udevrulesdir}/90-supergfxd-nvidia-pm.rules
%{_sysusersdir}/%{name}-user.conf
%ghost %attr(0644,root,root) %{_sysconfdir}/modprobe.d/supergfxd.conf
%config %{_sysconfdir}/dbus-1/system.d/org.supergfxctl.Daemon.conf
%dir %{_datadir}/doc/%{name}
%{_datadir}/doc/%{name}/*

%changelog
