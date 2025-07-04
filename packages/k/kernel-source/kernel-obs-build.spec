#
# spec file for package kernel-obs-build
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
# needsrootforbuild


#!BuildIgnore: post-build-checks

%define patchversion 6.15.4
%define variant %{nil}

%include %_sourcedir/kernel-spec-macros

%if 0%{?suse_version}
%if "%{nil}"
%global kernel_flavor %{nil}
%else
%ifarch %ix86
%global kernel_flavor -pae
%else
%ifarch armv7l armv7hl
%global kernel_flavor -lpae
%else
%global kernel_flavor -default
%endif
%endif
%endif
%global kernel_package kernel%kernel_flavor-srchash-55e70a8c5b295edf08b06b423d5bb1617fbee148
%endif
%if 0%{?rhel_version}
%global kernel_package kernel
%endif

Name:           kernel-obs-build
Version:        6.15.4
%if 0%{?is_kotd}
Release:        <RELEASE>.g55e70a8
%else
Release:        0
%endif
Summary:        package kernel and initrd for OBS VM builds
License:        GPL-2.0-only
Group:          SLES
Provides:       kernel-obs-build-srchash-55e70a8c5b295edf08b06b423d5bb1617fbee148
BuildRequires:  coreutils
BuildRequires:  device-mapper
BuildRequires:  dracut
BuildRequires:  %kernel_package
BuildRequires:  util-linux
%if 0%{?suse_version} > 1550 || 0%{?sle_version} > 150200
BuildRequires:  zstd
%endif
ExclusiveArch:  aarch64 armv6hl armv7hl ppc64le riscv64 s390x x86_64

%description
This package is repackaging already compiled kernels to make them usable
inside of Open Build Service (OBS) VM builds. An initrd with some basic
kernel modules is generated as well, but further kernel modules can be
loaded during build when installing the kernel package.

%files
/.build.cmdline.*
/.build.console.*
/.build.hostarch.*
/.build.initrd.*
/.build.kernel.*

%prep

%build
# set 'date of last password change' to a static value (bsc#1189305)
sed -i 's/^\(root:\*:\)[1-9][0-9]*\(::::::\)/\142\2/' /etc/shadow
mkdir -p /usr/lib/dracut/modules.d/80obs
cat > /usr/lib/dracut/modules.d/80obs/module-setup.sh <<EOF
#!/bin/bash

# called by dracut
check() {
    return 0
}

# called by dracut
installkernel() {
    hostonly='' instmods obs
}

# called by dracut
install() {
    inst_hook pre-udev 10 "\$moddir"/setup_obs.sh
}
EOF
chmod a+rx /usr/lib/dracut/modules.d/80obs/module-setup.sh
cat > /usr/lib/dracut/modules.d/80obs/setup_obs.sh <<EOF
#!/bin/sh
info "Loading kernel modules for OBS"
info "  Loop..."
modprobe -q loop max_loop=64
info "  binfmt misc..."
modprobe -q binfmt_misc
EOF
chmod a+rx /usr/lib/dracut/modules.d/80obs/setup_obs.sh
# Configure systemd in kernel-obs-build's initrd not to limit TasksMax,
# we run with build as PID 1 (boo#965564)
echo "DefaultTasksMax=infinity" >> /etc/systemd/system.conf
echo "DefaultTasksAccounting=no" >> /etc/systemd/system.conf
echo 127.0.0.1 localhost > /etc/hosts # omit build-machine host name (boo#1084909)

# a longer list to have them also available for qemu cross builds where x86_64 kernel runs in eg. arm env.
# this list of modules where available on build workers of build.opensuse.org, so we stay compatible.
export KERNEL_MODULES="
	loop dm-crypt essiv dm-mod dm-snapshot binfmt-misc fuse kqemu squashfs ext2 ext3 ext4 btrfs
	xfs nf_conntrack_ipv6 binfmt_misc virtio_pci virtio_mmio virtio_blk virtio_rng fat vfat
	nls_cp437 nls_iso8859-1 ibmvscsi sd_mod e1000 ibmveth overlay 9p 9pnet_virtio qemu_fw_cfg
	algif_hash aegis128 xts bridge br_netfilter nf_nat nf_tables xt_conntrack iptable_nat iptable_filter
	iso9660"

# manually load all modules to make sure they're available
for i in $KERNEL_MODULES; do
(
  echo "info '  $i'"
  echo "modprobe -q $i"
) >> /usr/lib/dracut/modules.d/80obs/setup_obs.sh
done

ROOT=""
[ -e "/dev/vda" ] && ROOT="-d /dev/vda"
[ -e /dev/hda1 ] && ROOT="-d /dev/hda1" # for xen builds
%define kernel_name vmlinu?
%ifarch s390 s390x
%define kernel_name image
%endif
%ifarch %arm
%define kernel_name zImage
%endif
%ifarch aarch64 riscv64
%define kernel_name Image
%endif

# --host-only mode is needed for unlimited TasksMax workaround (boo#965564)
dracut --reproducible --host-only --no-hostonly-cmdline \
	--no-early-microcode --nofscks --strip --hardlink \
	--drivers="$KERNEL_MODULES" --force /tmp/initrd.kvm \
%if 0%{?suse_version} > 1550 || 0%{?sle_version} > 150200
	--compress "zstd -19 -T0" \
%endif
	$(echo /boot/%{kernel_name}-*%{kernel_flavor} | sed -n -e 's,[^-]*-\(.*'%{kernel_flavor}'\),\1,p')

#cleanup
rm -rf /usr/lib/dracut/modules.d/80obs

%install
install -d -m 0755 %{buildroot}
cp -v /boot/%{kernel_name}-*%{kernel_flavor} %{buildroot}/.build.kernel.kvm
cp -v /tmp/initrd.kvm %{buildroot}/.build.initrd.kvm

# inform worker kernel parameters to invoke
CMDLINE="elevator=noop nmi_watchdog=0 rw ia32_emulation=1"
echo "$CMDLINE" > %{buildroot}/.build.cmdline.kvm

# inform worker about availability of virtio-serial
touch %{buildroot}/.build.console.kvm
if grep -qx CONFIG_VIRTIO_CONSOLE=y /boot/config-*%{kernel_flavor} ; then
    echo "virtio" > %{buildroot}/.build.console.kvm
fi

#inform worker about arch
#see obs-build commit e47399d738e51
uname -m > %{buildroot}/.build.hostarch.kvm

%changelog
