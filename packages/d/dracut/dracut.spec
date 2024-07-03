#
# spec file for package dracut
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


%define dracutlibdir %{_prefix}/lib/dracut

%if 0%{?suse_version} >= 1550
%define dracut_sbindir %{_sbindir}
%else
%define dracut_sbindir /sbin
%endif

Name:           dracut
Version:        059+suse.628.g20b345b4
Release:        0
Summary:        Event driven initramfs infrastructure
License:        GPL-2.0-only AND GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          System/Base
URL:            https://github.com/dracutdevs/dracut/wiki
Source0:        dracut-%{version}.tar.xz
Source1:        dracut-rpmlintrc
Source2:        README.susemaint
BuildRequires:  asciidoc
BuildRequires:  bash
BuildRequires:  cargo
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  libxslt
BuildRequires:  rust
BuildRequires:  pkgconfig(libkmod)
BuildRequires:  pkgconfig(systemd) >= 219
Requires:       %{_bindir}/get_kernel_version
Requires:       bash
Requires:       coreutils
Requires:       gawk
Requires(post): coreutils
Requires:       cpio
Requires:       elfutils
Requires:       file
Requires:       filesystem
Requires:       findutils
Requires:       grep
Requires:       hardlink
Requires:       modutils
Requires:       pigz
Requires:       sed
Requires:       systemd >= 219
Recommends:     (tpm2.0-tools if tpm2-0-tss)
Requires:       udev > 166
Requires:       util-linux >= 2.21
Requires:       util-linux-systemd >= 2.36.2
Recommends:     xz
Requires:       zstd
# We use 'btrfs fi usage' that was not present before
Conflicts:      btrfsprogs < 3.18
# suse-module-tools >= 15.4.7 is prepared for the removal of mkinitrd-suse.sh
Conflicts:      suse-module-tools < 15.4.7
%{?systemd_requires}

%description
Dracut contains tools to create a bootable initramfs for Linux kernels >= 2.6.
Dracut contains various modules which are driven by the event-based udev
and systemd. Having root on MD, DM, LVM2, LUKS is supported as well as
NFS, iSCSI, NBD, FCoE.

%ifnarch %ix86
%package fips
Summary:        Dracut modules to build a dracut initramfs with an integrity check
Group:          System/Base
Requires:       %{name} = %{version}-%{release}
Requires:       libkcapi-tools

%description fips
This package requires everything which is needed to build an
initramfs with dracut, which does an integrity check of the kernel
and its cryptography during startup.
%endif

%ifnarch %ix86
%package ima
Summary:        Dracut modules to build a dracut initramfs with IMA
Group:          System/Base
Requires:       %{name} = %{version}-%{release}
Requires:       evmctl
Requires:       keyutils

%description ima
This package requires everything which is needed to build an
initramfs (using dracut) which tries to load an IMA policy during startup.
%endif

%package tools
Summary:        Tools to build a local initramfs
Group:          System/Base
Requires:       %{name}
# split-provides for upgrade from SLES12 SP1 to SLES12 SP2
Provides:       %{name}:%{_bindir}/dracut-catimages

%description tools
This package contains tools to assemble the local initrd and host configuration.

%package extra
Summary:        Dracut modules usually not required for normal operation
Group:          System/Base
Requires:       %{name} = %{version}-%{release}

%description extra
This package contains all modules that are part of dracut upstream
but are not normally supported or required.

%prep
%autosetup

%build
%configure \
  --systemdsystemunitdir=%{_unitdir} \
  --bashcompletiondir=%{_datadir}/bash-completion/completions \
  --libdir=%{_prefix}/lib \
  --enable-dracut-cpio
%make_build all CFLAGS="%{optflags}" %{?_smp_mflags}

%install
%make_install

echo -e "#!/bin/bash\nDRACUT_VERSION=%{version}-%{release}" > %{buildroot}%{dracutlibdir}/dracut-version.sh

# remove architecture specific modules
%ifnarch ppc ppc64 ppc64le ppc64p7
rm -rf %{buildroot}%{dracutlibdir}/modules.d/90ppcmac
%endif
%ifnarch s390 s390x
rm -rf %{buildroot}%{dracutlibdir}/modules.d/80cms
rm -rf %{buildroot}%{dracutlibdir}/modules.d/81cio_ignore
rm -rf %{buildroot}%{dracutlibdir}/modules.d/91zipl
rm -rf %{buildroot}%{dracutlibdir}/modules.d/95dasd
rm -rf %{buildroot}%{dracutlibdir}/modules.d/95dasd_mod
rm -rf %{buildroot}%{dracutlibdir}/modules.d/95dcssblk
rm -rf %{buildroot}%{dracutlibdir}/modules.d/95zfcp
rm -rf %{buildroot}%{dracutlibdir}/modules.d/95znet
%else
rm -rf %{buildroot}%{dracutlibdir}/modules.d/00warpclock
%endif

mkdir -p %{buildroot}/boot/dracut
mkdir -p %{buildroot}%{_localstatedir}/lib/dracut/overlay
mkdir -p %{buildroot}%{_localstatedir}/log
touch %{buildroot}%{_localstatedir}/log/dracut.log

install -D -m 0644 dracut.conf.d/suse.conf.example %{buildroot}%{dracutlibdir}/dracut.conf.d/01-dist.conf
install -m 0644 suse/99-debug.conf %{buildroot}%{_sysconfdir}/dracut.conf.d/99-debug.conf
%ifnarch %ix86
install -m 0644 dracut.conf.d/fips.conf.example %{buildroot}%{_sysconfdir}/dracut.conf.d/40-fips.conf
install -m 0644 dracut.conf.d/ima.conf.example %{buildroot}%{_sysconfdir}/dracut.conf.d/40-ima.conf
%endif
# bsc#915218
%ifarch s390 s390x
install -m 0644 suse/s390x_persistent_policy.conf %{buildroot}%{_sysconfdir}/dracut.conf.d/10-persistent_policy.conf
%else
install -m 0644 suse/persistent_policy.conf %{buildroot}%{_sysconfdir}/dracut.conf.d/10-persistent_policy.conf
%endif

%if 0%{?suse_version}
rm -f %{buildroot}%{dracutlibdir}/modules.d/45ifcfg/write-ifcfg.sh
ln -s %{dracutlibdir}/modules.d/45ifcfg/write-ifcfg-suse.sh %{buildroot}%{dracutlibdir}/modules.d/45ifcfg/write-ifcfg.sh
%else
mv %{buildroot}%{dracutlibdir}/modules.d/45ifcfg/write-ifcfg.sh %{buildroot}%{dracutlibdir}/modules.d/45ifcfg/write-ifcfg-redhat.sh
ln -s %{dracutlibdir}/modules.d/45ifcfg/write-ifcfg-redhat.sh %{buildroot}%{dracutlibdir}/modules.d/45ifcfg/write-ifcfg.sh
%endif

# create a link to dracut-util to be able to parse kernel command line arguments at generation time
ln -s %{dracutlibdir}/dracut-util %{buildroot}%{dracutlibdir}/dracut-getarg

%post
# check whether /var/run has been converted to a symlink
if [ ! -L /var/run ]; then
    grep -q '^[ 	]*GRUB_CMDLINE_LINUX_DEFAULT=.*rd.convertfs' /etc/default/grub || \
    sed -i '/^[ 	]*GRUB_CMDLINE_LINUX_DEFAULT.*/s/"$/ rd.convertfs"/' /etc/default/grub  || :
    if ! grep --no-message 'add_dracutmodules+=" convertfs "' /etc/dracut.conf.d/05-convertfs.conf; then
        cat >>/etc/dracut.conf.d/05-convertfs.conf<<EOF
add_dracutmodules+=" convertfs "
EOF
    fi
fi
#clean up after the conversion is done
if [ -L /var/run ] && [ -f /etc/dracut.conf.d/05-convertfs.conf ]; then
    sed -i '/^[ 	]*GRUB_CMDLINE_LINUX_DEFAULT.*/s/rd.convertfs//' /etc/default/grub || :
    [ -f /etc/dracut.conf.d/05-convertfs.conf ] && sed -i '/add_dracutmodules+="[ 	]*convertfs[ 	]*"/d' /etc/dracut.conf.d/05-convertfs.conf || :
    [ -s /etc/dracut.conf.d/05-convertfs.conf ] || rm -f /etc/dracut.conf.d/05-convertfs.conf || :
    [ -d /var/lock.lockmove~ ] && rm -rf /var/lock.lockmove~ || :
    [ -d /var/run.runmove~ ] && rm -rf /var/run.runmove~ || :
fi

# remove obsolete legacy fillup template for /etc/sysconfig/kernel
rm -f /var/adm/fillup-templates/sysconfig.kernel-mkinitrd

%{?regenerate_initrd_post}

%ifnarch %ix86
%post fips
%{?regenerate_initrd_post}
%endif

%ifnarch %ix86
%post ima
%{?regenerate_initrd_post}
%endif

%postun
%{?regenerate_initrd_post}

%ifnarch %ix86
%postun fips
%{?regenerate_initrd_post}
%endif

%ifnarch %ix86
%postun ima
%{?regenerate_initrd_post}
%endif

%posttrans
%{?regenerate_initrd_posttrans}

%ifnarch %ix86
%posttrans fips
%{?regenerate_initrd_posttrans}
%endif

%ifnarch %ix86
%posttrans ima
%{?regenerate_initrd_posttrans}
%endif

%ifnarch %ix86
%files fips
%license COPYING
%config %{_sysconfdir}/dracut.conf.d/40-fips.conf
%{dracutlibdir}/modules.d/01fips
%endif

%ifnarch %ix86
%files ima
%license COPYING
%config %{_sysconfdir}/dracut.conf.d/40-ima.conf
%{dracutlibdir}/modules.d/96securityfs
%{dracutlibdir}/modules.d/97masterkey
%{dracutlibdir}/modules.d/98integrity
%endif

%files tools
%{_bindir}/dracut-catimages
%{_mandir}/man8/dracut-catimages.8*
%dir /boot/dracut
%dir %{_localstatedir}/lib/dracut
%dir %{_localstatedir}/lib/dracut/overlay

%files extra
%license COPYING

%{dracutlibdir}/modules.d/00mksh
%{dracutlibdir}/modules.d/02caps
%{dracutlibdir}/modules.d/00dash
%{dracutlibdir}/modules.d/05busybox
%ifarch ppc ppc64 ppc64le ppc64p7
%{dracutlibdir}/modules.d/90ppcmac
%endif
%ifarch s390 s390x
# RH-specific s390 modules, we take another approach
%{dracutlibdir}/modules.d/95dasd
%{dracutlibdir}/modules.d/95zfcp
%{dracutlibdir}/modules.d/95znet
%endif

%files
%license COPYING
%doc README.md NEWS.md AUTHORS dracut.html
%doc docs/README.cross docs/README.generic docs/README.kernel
%doc docs/HACKING.md docs/dracut.png docs/dracut.svg
%{_bindir}/dracut
%{_bindir}/lsinitrd
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/dracut
%{_datadir}/bash-completion/completions/lsinitrd
%{_datadir}/pkgconfig/dracut.pc

%config(noreplace) %{_sysconfdir}/dracut.conf
%dir %{_sysconfdir}/dracut.conf.d
%dir %{dracutlibdir}/dracut.conf.d
%{dracutlibdir}/dracut.conf.d/01-dist.conf
%config %{_sysconfdir}/dracut.conf.d/99-debug.conf
%config %{_sysconfdir}/dracut.conf.d/10-persistent_policy.conf

%{_mandir}/man8/dracut.8*
%{_mandir}/man1/lsinitrd.1*
%{_mandir}/man7/dracut.kernel.7*
%{_mandir}/man7/dracut.cmdline.7*
%{_mandir}/man7/dracut.bootup.7*
%{_mandir}/man7/dracut.modules.7*
%{_mandir}/man8/dracut-cmdline.service.8*
%{_mandir}/man8/dracut-initqueue.service.8*
%{_mandir}/man8/dracut-pre-pivot.service.8*
%{_mandir}/man8/dracut-pre-trigger.service.8*
%{_mandir}/man8/dracut-pre-udev.service.8*
%{_mandir}/man8/dracut-mount.service.8.*
%{_mandir}/man8/dracut-pre-mount.service.8.*
%{_mandir}/man8/dracut-shutdown.service.8.*
%{_mandir}/man5/dracut.conf.5*

%dir %{_prefix}/lib/kernel
%dir %{_prefix}/lib/kernel/install.d
%{_prefix}/lib/kernel/install.d/50-dracut.install
%{_prefix}/lib/kernel/install.d/51-dracut-rescue.install

%dir %{dracutlibdir}
%{dracutlibdir}/skipcpio
%{dracutlibdir}/dracut-functions.sh
%{dracutlibdir}/dracut-init.sh
%{dracutlibdir}/dracut-functions
%{dracutlibdir}/dracut-version.sh
%{dracutlibdir}/dracut-logger.sh
%{dracutlibdir}/dracut-initramfs-restore
%{dracutlibdir}/dracut-install
%{dracutlibdir}/dracut-util
%{dracutlibdir}/dracut-getarg
%{dracutlibdir}/dracut-cpio

%dir %{dracutlibdir}/modules.d
%{dracutlibdir}/modules.d/00bash
%{dracutlibdir}/modules.d/00systemd
%{dracutlibdir}/modules.d/00systemd-network-management
%ifnarch s390 s390x
%{dracutlibdir}/modules.d/00warpclock
%endif
%ifarch %ix86
%exclude %{dracutlibdir}/modules.d/01fips
%endif
%{dracutlibdir}/modules.d/01systemd-ac-power
%{dracutlibdir}/modules.d/01systemd-ask-password
%{dracutlibdir}/modules.d/01systemd-coredump
%{dracutlibdir}/modules.d/01systemd-hostnamed
%{dracutlibdir}/modules.d/01systemd-initrd
%{dracutlibdir}/modules.d/01systemd-integritysetup
%{dracutlibdir}/modules.d/01systemd-journald
%{dracutlibdir}/modules.d/01systemd-ldconfig
%{dracutlibdir}/modules.d/01systemd-modules-load
%{dracutlibdir}/modules.d/01systemd-networkd
%{dracutlibdir}/modules.d/01systemd-pcrphase
%{dracutlibdir}/modules.d/01systemd-portabled
%{dracutlibdir}/modules.d/01systemd-pstore
%{dracutlibdir}/modules.d/01systemd-repart
%{dracutlibdir}/modules.d/01systemd-resolved
%{dracutlibdir}/modules.d/01systemd-sysctl
%{dracutlibdir}/modules.d/01systemd-sysext
%{dracutlibdir}/modules.d/01systemd-sysusers
%{dracutlibdir}/modules.d/01systemd-timedated
%{dracutlibdir}/modules.d/01systemd-timesyncd
%{dracutlibdir}/modules.d/01systemd-tmpfiles
%{dracutlibdir}/modules.d/01systemd-udevd
%{dracutlibdir}/modules.d/01systemd-veritysetup
%{dracutlibdir}/modules.d/03modsign
%{dracutlibdir}/modules.d/03rescue
%{dracutlibdir}/modules.d/04watchdog
%{dracutlibdir}/modules.d/04watchdog-modules
%{dracutlibdir}/modules.d/06dbus-broker
%{dracutlibdir}/modules.d/06dbus-daemon
%{dracutlibdir}/modules.d/06rngd
%{dracutlibdir}/modules.d/09dbus
%{dracutlibdir}/modules.d/10i18n
%{dracutlibdir}/modules.d/30convertfs
%{dracutlibdir}/modules.d/35connman
%{dracutlibdir}/modules.d/35network-legacy
%{dracutlibdir}/modules.d/35network-manager
%{dracutlibdir}/modules.d/40network
%{dracutlibdir}/modules.d/45ifcfg
%{dracutlibdir}/modules.d/45url-lib
%{dracutlibdir}/modules.d/50drm
%{dracutlibdir}/modules.d/50plymouth
%{dracutlibdir}/modules.d/62bluetooth
%ifarch s390 s390x
%{dracutlibdir}/modules.d/80cms
%endif
%{dracutlibdir}/modules.d/80lvmmerge
%{dracutlibdir}/modules.d/80lvmthinpool-monitor
%exclude %{dracutlibdir}/modules.d/80test
%exclude %{dracutlibdir}/modules.d/80test-makeroot
%exclude %{dracutlibdir}/modules.d/80test-root
%ifarch s390 s390x
%{dracutlibdir}/modules.d/81cio_ignore
%endif
%{dracutlibdir}/modules.d/90btrfs
%{dracutlibdir}/modules.d/90crypt
%{dracutlibdir}/modules.d/90dm
%{dracutlibdir}/modules.d/90dmraid
%{dracutlibdir}/modules.d/90dmsquash-live
%{dracutlibdir}/modules.d/90dmsquash-live-autooverlay
%{dracutlibdir}/modules.d/90dmsquash-live-ntfs
%{dracutlibdir}/modules.d/90kernel-modules-extra
%{dracutlibdir}/modules.d/90kernel-modules
%{dracutlibdir}/modules.d/90kernel-network-modules
%{dracutlibdir}/modules.d/90livenet
%{dracutlibdir}/modules.d/90lvm
%{dracutlibdir}/modules.d/90mdraid
%{dracutlibdir}/modules.d/90multipath
%{dracutlibdir}/modules.d/90nvdimm
%{dracutlibdir}/modules.d/90overlayfs
%{dracutlibdir}/modules.d/90qemu
%{dracutlibdir}/modules.d/90qemu-net
%{dracutlibdir}/modules.d/91crypt-gpg
%{dracutlibdir}/modules.d/91crypt-loop
%{dracutlibdir}/modules.d/91fido2
%{dracutlibdir}/modules.d/91pcsc
%{dracutlibdir}/modules.d/91pkcs11
%{dracutlibdir}/modules.d/91tpm2-tss
%ifarch s390 s390x
%{dracutlibdir}/modules.d/91zipl
%endif
%{dracutlibdir}/modules.d/95cifs
%ifarch s390 s390x
%{dracutlibdir}/modules.d/95dasd_mod
%{dracutlibdir}/modules.d/95dcssblk
%endif
%{dracutlibdir}/modules.d/95debug
%{dracutlibdir}/modules.d/95fcoe
%{dracutlibdir}/modules.d/95fcoe-uefi
%{dracutlibdir}/modules.d/95fstab-sys
%{dracutlibdir}/modules.d/95iscsi
%{dracutlibdir}/modules.d/95lunmask
%{dracutlibdir}/modules.d/95nbd
%{dracutlibdir}/modules.d/95nfs
%{dracutlibdir}/modules.d/95nvmf
%{dracutlibdir}/modules.d/95resume
%{dracutlibdir}/modules.d/95rootfs-block
%{dracutlibdir}/modules.d/95ssh-client
%{dracutlibdir}/modules.d/95terminfo
%{dracutlibdir}/modules.d/95udev-rules
%{dracutlibdir}/modules.d/95virtfs
%{dracutlibdir}/modules.d/95virtiofs
%{dracutlibdir}/modules.d/97biosdevname
%ifarch %ix86
%exclude %{dracutlibdir}/modules.d/96securityfs
%exclude %{dracutlibdir}/modules.d/97masterkey
%exclude %{dracutlibdir}/modules.d/98integrity
%endif
%{dracutlibdir}/modules.d/98dracut-systemd
%{dracutlibdir}/modules.d/98ecryptfs
%{dracutlibdir}/modules.d/98pollcdrom
%{dracutlibdir}/modules.d/98selinux
%{dracutlibdir}/modules.d/98syslog
%{dracutlibdir}/modules.d/98usrmount
%{dracutlibdir}/modules.d/99base
%{dracutlibdir}/modules.d/99fs-lib
%{dracutlibdir}/modules.d/99img-lib
%{dracutlibdir}/modules.d/99memstrack
%{dracutlibdir}/modules.d/99shutdown
%{dracutlibdir}/modules.d/99squash
%{dracutlibdir}/modules.d/99suse
%{dracutlibdir}/modules.d/99suse-initrd
%{dracutlibdir}/modules.d/99uefi-lib
%attr(0640,root,root) %ghost %config(missingok,noreplace) %{_localstatedir}/log/dracut.log
%dir %{_unitdir}/initrd.target.wants
%dir %{_unitdir}/sysinit.target.wants
%{_unitdir}/*.service
%{_unitdir}/*/*.service

%changelog
