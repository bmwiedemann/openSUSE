#
# spec file for package ignition-dracut
#
# Copyright (c) 2020 SUSE LLC
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
Version:        0.0+git20200504.7ff38d9
Release:        0
Summary:        Dracut scripts for ignition
License:        BSD-2-Clause
Group:          System/Management
URL:            https://github.com/dustymabe/ignition-dracut
Source:         %{name}-%{version}.tar.xz
Source1:        ignition-mount-initrd-fstab.service
Source2:        ignition-dracut-rpmlintrc
Source3:        ignition-suse-generator
Source4:        module-setup.sh
Source5:        02_ignition_firstboot
Source6:        change-ignition-firstboot-path.conf
Source7:        README.SUSE
Source8:        ignition-setup-user-suse.sh
Source9:        prevent-boot-cycle.conf
Source20:       ignition-userconfig-timeout.conf
Source21:       ignition-userconfig-timeout-arm.conf
Patch3:         0003-Disable-resetting-UUID.patch
BuildRequires:  systemd-rpm-macros
BuildRequires:  update-bootloader-rpm-macros
Requires:       %{name}-grub2
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

%package grub2
Summary:        Files to trigger ignition firstboot with grub2
Group:          System/Management
Requires:       grub2
Requires(post): grub2
Requires(post): sed
Requires(post): virt-what

%description grub2
GRUB2 configuration which sets ignition.firstboot based on
/boot/writable/firstboot_happened and ignition.firstboot and a matching service
which creates firstboot_happened after the first boot.

%prep
%autosetup -p1

mkdir dracut/30ignition-microos grub
chmod +x %{SOURCE3} %{SOURCE4} %{SOURCE8}
cp %{SOURCE1} %{SOURCE3} %{SOURCE4} %{SOURCE8} %{SOURCE9} dracut/30ignition-microos/
%ifarch aarch64 %{arm}
cp %{SOURCE21} dracut/30ignition-microos/ignition-userconfig-timeout.conf
%else
cp %{SOURCE20} dracut/30ignition-microos/ignition-userconfig-timeout.conf
%endif
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

%post
%{?regenerate_initrd_post}
# Trigger creating the firstboot_happened file (in posttrans) on upgrades.
# This is needed for systems where the first boot happened before
# firstboot_happened got introduced and can be removed in the future.
if [ "$1" -ne 1 ]; then
    mkdir -p %{_rundir}/ignition-dracut/
    touch %{_rundir}/ignition-dracut/isupgrade
fi

%posttrans
%{?regenerate_initrd_posttrans}
if [ -f %{_rundir}/ignition-dracut/isupgrade ]; then
    # Done in posttrans so that read-only-root-fs could create the subvol
    mkdir -p /boot/writable
    [ -e /boot/writable/firstboot_happened ] || touch /boot/writable/firstboot_happened
fi

%pre grub2
%service_add_pre ignition-firstboot-complete.service

%post grub2
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
fi
%service_add_post ignition-firstboot-complete.service

%preun grub2
%service_del_preun ignition-firstboot-complete.service

%postun grub2
if [ "$1" = 0 ] ; then
    sed -i -E '/^GRUB_CMDLINE_LINUX_DEFAULT="/s/(\\\$)?ignition[._][^[:space:]"]+ ?//g' %{_sysconfdir}/default/grub
fi
%service_del_postun -n ignition-firstboot-complete.service

%posttrans grub2
%{?update_bootloader_posttrans}

%files
%license LICENSE
%doc README.SUSE
%dir %{_prefix}/lib/dracut/
%dir %{_prefix}/lib/dracut/modules.d/
%{_prefix}/lib/dracut/modules.d/99journald-conf/
%{_prefix}/lib/dracut/modules.d/99emergency-timeout/
%{_prefix}/lib/dracut/modules.d/30ignition/
%{_prefix}/lib/dracut/modules.d/30ignition-microos/

%files grub2
%license LICENSE
%doc README.SUSE
%dir %{_sysconfdir}/grub.d/
%{_sysconfdir}/grub.d/02_ignition_firstboot
/usr/lib/systemd/system/ignition-firstboot-complete.service
/usr/lib/systemd/system/ignition-firstboot-complete.service.d/

%changelog
