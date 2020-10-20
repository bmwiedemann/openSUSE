#
# spec file for package ignition
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


Name:           ignition
Version:        2.7.0
Release:        0
Summary:        First boot installer and configuration tool
License:        Apache-2.0
Group:          System/Management
URL:            https://github.com/coreos/ignition
Source:         %{name}-%{version}.tar.xz
Source1:        ignition-mount-initrd-fstab.service
Source2:        ignition-rpmlintrc
Source3:        ignition-suse-generator
Source4:        module-setup.sh
Source5:        02_ignition_firstboot
Source6:        change-ignition-firstboot-path.conf
Source7:        README.SUSE
Source8:        ignition-setup-user-suse.sh
Source9:        ignition-enable-network.service
Source10:       ignition-enable-network.sh
Source20:       ignition-userconfig-timeout.conf
Source21:       ignition-userconfig-timeout-arm.conf
Patch2:         0002-allow-multiple-mounts-of-same-device.patch
BuildRequires:  dracut
BuildRequires:  libblkid-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  update-bootloader-rpm-macros
BuildRequires:  golang(API) >= 1.12
Requires:       %{name}-dracut-grub2
Requires:       dracut
Recommends:     %{_sbindir}/groupadd
Recommends:     %{_sbindir}/sgdisk
Recommends:     %{_sbindir}/useradd
Recommends:     %{_sbindir}/usermod
Recommends:     /sbin/mkfs.btrfs
Recommends:     /sbin/mkfs.ext4
Recommends:     /sbin/mkfs.vfat
Recommends:     /sbin/mkfs.xfs
Recommends:     /sbin/mkswap
Recommends:     /sbin/udevadm
Suggests:       /sbin/mdadm
Provides:       ignition-dracut = 0.0+git20200722.98ed51d
Obsoletes:      ignition-dracut < 0.0+git20200722.98ed51d
%{update_bootloader_requires}

%description
Ignition is an utility to manipulate disks and configuration files
during the initramfs. This includes partitioning disks, formatting
partitions, writing files (regular files, systemd units, etc.), and
creating users.
On first boot, Ignition reads its configuration from a source of truth
(remote URL, network metadata service, hypervisor bridge, etc.) and
applies the configuration.

%package dracut-grub2
Summary:        Files to trigger ignition firstboot with grub2
Group:          System/Management
Requires:       grub2
Requires(post): grub2
Requires(post): sed

%description dracut-grub2
GRUB2 configuration which sets ignition.firstboot based on
/boot/writable/firstboot_happened and ignition.firstboot and a matching service
which creates firstboot_happened after the first boot.

%prep
%setup -q
%patch2 -p1

mkdir dracut/30ignition-microos grub systemd_suse
chmod +x %{SOURCE3} %{SOURCE4} %{SOURCE8}
cp %{SOURCE1} %{SOURCE3} %{SOURCE4} %{SOURCE8} %{SOURCE9} %{SOURCE10} dracut/30ignition-microos/
%ifarch aarch64 %{arm}
cp %{SOURCE21} dracut/30ignition-microos/ignition-userconfig-timeout.conf
%else
cp %{SOURCE20} dracut/30ignition-microos/ignition-userconfig-timeout.conf
%endif
cp %{SOURCE5} grub/
cp %{SOURCE6} systemd_suse/
cp %{SOURCE7} .

%build
sed -i -e 's|go build -ldflags|go build -buildmode=pie -ldflags|g' build
env VERSION=%{version} GLDFLAGS='-X github.com/coreos/ignition/v2/internal/distro.selinuxRelabel=false -X github.com/coreos/ignition/v2/internal/distro.writeAuthorizedKeysFragment=false ' bash -x ./build

%install
make -o all install DESTDIR=%{buildroot}

install -d %{buildroot}%{_sysconfdir}/grub.d
install -d %{buildroot}%{_prefix}/lib/systemd/system/ignition-firstboot-complete.service.d
install -p -m 0755 grub/* %{buildroot}%{_sysconfdir}/grub.d/
install -p -m 0644 systemd_suse/*.conf %{buildroot}%{_prefix}/lib/systemd/system/ignition-firstboot-complete.service.d/

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

%pre dracut-grub2
%service_add_pre ignition-firstboot-complete.service

%post dracut-grub2
if [ "$1" = 1 ] ; then
    sed -i 's/^\(GRUB_CMDLINE_LINUX_DEFAULT="\)\(.*\)/\1\\$ignition_firstboot \2/' %{_sysconfdir}/default/grub
    %{?update_bootloader_refresh_post}
fi
%service_add_post ignition-firstboot-complete.service

%preun dracut-grub2
%service_del_preun ignition-firstboot-complete.service

%postun dracut-grub2
if [ "$1" = 0 ] ; then
    sed -i -E '/^GRUB_CMDLINE_LINUX_DEFAULT="/s/(\\\$)?ignition[._][^[:space:]"]+ ?//g' %{_sysconfdir}/default/grub
fi
%service_del_postun -n ignition-firstboot-complete.service

%files
%license LICENSE
%doc README.md README.SUSE docs
%{_prefix}/lib/dracut/modules.d/30ignition
%{_prefix}/lib/dracut/modules.d/30ignition-microos
%{_bindir}/ignition-validate

%files dracut-grub2
%license LICENSE
%doc README.SUSE
%{_sysconfdir}/grub.d/02_ignition_firstboot
%{_prefix}/lib/systemd/system/ignition-firstboot-complete.service
%{_prefix}/lib/systemd/system/ignition-firstboot-complete.service.d/

%changelog
