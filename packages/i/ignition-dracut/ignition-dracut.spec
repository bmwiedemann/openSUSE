#
# spec file for package ignition-dracut
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           ignition-dracut
Version:        0.0+git20191001.cefb71c
Release:        0
Summary:        Dracut scripts for ignition
License:        BSD-2-Clause
Group:          System/Management
BuildArch:      noarch
URL:            https://github.com/dustymabe/ignition-dracut
Source:         %{name}-%{version}.tar.xz
Source1:        ignition-mount-initrd-fstab.service
Source2:        ignition-userconfig-timeout.conf
Source3:        ignition-suse-generator
Source4:        module-setup.sh
Source5:        01_suse_set_ignition
Source6:        change-ignition-firstboot-path.conf
Source7:        README.SUSE
Source8:        ignition-setup-user-suse.sh
Patch2:         0002-Support-different-flagfile-location.patch
Patch3:         0003-Disable-resetting-UUID.patch
BuildRequires:  suse-module-tools
BuildRequires:  update-bootloader-rpm-macros
PreReq:         sed
PreReq:         grub2
PreReq:         virt-what
Requires:       gptfdisk
Requires:       ignition
%{update_bootloader_requires}

%description
Ignition is an utility to manipulate disks and configuration files during
the initramfs. This includes partitioning disks, formatting partitions,
writing files (regular files, systemd units, etc.), and creating users.
On first boot, Ignition reads its configuration from a source of truth
(remote URL, network metadata service, hypervisor bridge, etc.) and applies
the configuration.
This package contains the dracut scripts for this.

%prep
%setup -q
%patch2 -p1
%patch3 -p1
mkdir dracut/30ignition-microos
chmod +x %{SOURCE3} %{SOURCE4}
cp %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE8} dracut/30ignition-microos/
cp %{SOURCE5} grub/
cp %{SOURCE6} systemd/
cp %{SOURCE7} .

%build

%install
install -d %{buildroot}%{_sysconfdir}/grub.d
install -d %{buildroot}%{_prefix}/lib/dracut/modules.d
install -d %{buildroot}%{_prefix}/lib/systemd/system
install -d %{buildroot}%{_prefix}/lib/systemd/system/ignition-firstboot-complete.service.d
install -p -m 0755 grub/* %{buildroot}%{_sysconfdir}/grub.d/
cp -av dracut/[0-9]* %{buildroot}%{_prefix}/lib/dracut/modules.d/
install -p -m 0644 systemd/*.service %{buildroot}%{_prefix}/lib/systemd/system/
install -p -m 0644 systemd/*.conf %{buildroot}%{_prefix}/lib/systemd/system/ignition-firstboot-complete.service.d/

%files
%license LICENSE
%doc README.SUSE
%{_sysconfdir}/grub.d
%{_prefix}/lib/dracut
%{_prefix}/lib/systemd/system/*
%config(noreplace) %{_sysconfdir}/grub.d/01_suse_set_ignition

%pre
%service_add_pre ignition-firstboot-complete.service

%post
%{?regenerate_initrd_post}
if [ "$1" = 1 ] ; then
    platform="$(virt-what)"
    case "${platform}" in
        *vmware*)     platform="vmware" ;;
        *virtualbox*) platform="virtualbox" ;;
        *kvm*|*qemu*) platform="qemu" ;;
        *)            platform="metal" ;;
    esac
    sed -i 's/^\(GRUB_CMDLINE_LINUX_DEFAULT="\)\(.*\)/\1ignition.platform.id='${platform}' \\$ignition_firstboot \2/' %{_sysconfdir}/default/grub
    %{?update_bootloader_refresh_post}
    # Trigger setting firstboot flag (in posttrans) only on new installations
    mkdir -p %{_rundir}/ignition-dracut/
    touch %{_rundir}/ignition-dracut/newinstall
fi
%service_add_post ignition-firstboot-complete.service

%preun
%service_del_preun ignition-firstboot-complete.service

%postun
if [ "$1" = 0 ] ; then
    sed -i -E '/^GRUB_CMDLINE_LINUX_DEFAULT="/s/(\\\$)?ignition[._][^[:space:]"]+ ?//g' %{_sysconfdir}/default/grub
    rm -f /boot/writable/ignition.firstboot
fi
%service_del_postun_without_restart ignition-firstboot-complete.service

%posttrans
%{?regenerate_initrd_posttrans}
if test -f %{_rundir}/ignition-dracut/newinstall; then
    %{?update_bootloader_posttrans}
    mkdir -p /boot/writable
    touch /boot/writable/ignition.firstboot
fi

%changelog
