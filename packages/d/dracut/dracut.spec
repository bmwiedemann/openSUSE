#
# spec file for package dracut
#
# Copyright (c) 2026 SUSE LLC
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
%define rbrelease %(r=%{release}; echo ${r%%.*})

%if 0%{?suse_version} >= 1550
%define dracut_sbindir %{_sbindir}
%else
%define dracut_sbindir /sbin
%endif

Name:           dracut
Version:        109+suse.35.g1fdbb27e
Release:        0
Summary:        Event driven initramfs infrastructure
License:        GPL-2.0-only AND GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          System/Base
URL:            https://github.com/dracut-ng/dracut-ng
Source0:        dracut-%{version}.tar.xz
Source1:        dracut-rpmlintrc
Source2:        README.susemaint
# Temporary files for locations outside of /usr and /etc (jsc#PED-14785 - comply
# with immutable mode).
Source3:        dracut-rpm-tmpfiles.conf
# Example configuration to add the debug module.
Source4:        99-debug.conf
# Default by-uuid persistent policy.
Source5:        persistent_policy.conf
# Specific by-path persistent policy for s390x (bsc#915218).
Source6:        s390x_persistent_policy.conf
BuildRequires:  bash
BuildRequires:  cargo
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  libxslt
BuildRequires:  pkgconfig(libkmod)
# dracut >= 108 needs to be compiled with libsystemd.pc present to enable
# parsing .note.dlopen JSON entries from the libsystemd-shared-*.so library,
# in order to resolve dlopen() dependencies.
BuildRequires:  pkgconfig(libsystemd) >= 257
BuildRequires:  rust
BuildRequires:  pkgconfig(systemd) >= 257
BuildRequires:  rubygem(asciidoctor)
Requires:       %{_bindir}/get_kernel_version
Requires:       bash
Requires:       coreutils
Requires(post): coreutils
Requires:       cpio
Requires:       elfutils
Requires:       file
Requires:       filesystem
Requires:       findutils
Requires:       gawk
Requires:       grep
Requires:       hardlink
Requires:       modutils
Requires:       pigz
Requires:       sed
# dracut >= 108 needs the sd-json API added in systemd-v257 to resolve dlopen()
# dependencies.
Requires:       systemd >= 257
Recommends:     (tpm2.0-tools if tpm2-0-tss)
Requires:       udev > 166
Requires:       util-linux >= 2.21
Requires:       util-linux-systemd >= 2.36.2
Recommends:     xz
Requires:       zstd
# We use 'btrfs fi usage' that was not present before.
Conflicts:      btrfsprogs < 3.18
# suse-module-tools >= 15.4.7 is prepared for the removal of mkinitrd-suse.sh
Conflicts:      suse-module-tools < 15.4.7
%{?systemd_requires}
Requires:       (jq if (nvme-cli or systemd-boot or grub2-x86_64-efi-bls))

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
# Split-provides for upgrade from SLES12 SP1 to SLES12 SP2.
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

echo -e "#!/bin/bash\nDRACUT_VERSION=%{version}-%{rbrelease}" > %{buildroot}%{dracutlibdir}/dracut-version.sh

# Remove architecture specific modules.
%ifnarch ppc ppc64 ppc64le ppc64p7
rm -rf %{buildroot}%{dracutlibdir}/modules.d/70ppcmac
%endif
%ifnarch s390 s390x
rm -rf %{buildroot}%{dracutlibdir}/modules.d/68cms
rm -rf %{buildroot}%{dracutlibdir}/modules.d/69cio_ignore
rm -rf %{buildroot}%{dracutlibdir}/modules.d/73zipl
rm -rf %{buildroot}%{dracutlibdir}/modules.d/74dasd
rm -rf %{buildroot}%{dracutlibdir}/modules.d/74dasd_mod
rm -rf %{buildroot}%{dracutlibdir}/modules.d/74dcssblk
rm -rf %{buildroot}%{dracutlibdir}/modules.d/74zfcp
rm -rf %{buildroot}%{dracutlibdir}/modules.d/74znet
%else
rm -rf %{buildroot}%{dracutlibdir}/modules.d/10warpclock
%endif

rm -rf %{buildroot}%{dracutlibdir}/dracut.conf.d/*
install -D -m 0644 dracut.conf.d/opensuse/01-dist.conf %{buildroot}%{dracutlibdir}/dracut.conf.d/01-dist.conf
install -m 0644 %{SOURCE4} %{buildroot}%{_sysconfdir}/dracut.conf.d/99-debug.conf
%ifnarch %ix86
install -m 0644 dracut.conf.d/fips/10-fips.conf %{buildroot}%{_sysconfdir}/dracut.conf.d/10-fips.conf
install -m 0644 dracut.conf.d/ima/10-ima.conf %{buildroot}%{_sysconfdir}/dracut.conf.d/10-ima.conf
%endif

# Install persistent policy config.
%ifarch s390 s390x
install -m 0644 %{SOURCE6} %{buildroot}%{_sysconfdir}/dracut.conf.d/10-persistent_policy.conf
%else
install -m 0644 %{SOURCE5} %{buildroot}%{_sysconfdir}/dracut.conf.d/10-persistent_policy.conf
%endif

# Install tmpfiles config.
mkdir -p %{buildroot}%{_tmpfilesdir}
install -m 644 %{SOURCE3} %{buildroot}%{_tmpfilesdir}/dracut.conf

# Remove tests.
rm -rf %{buildroot}%{dracutlibdir}/test
rm -rf %{buildroot}%{dracutlibdir}/modules.d/70test*

%post
# Check whether /var/run has been converted to a symlink.
if [ ! -L /var/run ]; then
    grep -q '^[ 	]*GRUB_CMDLINE_LINUX_DEFAULT=.*rd.convertfs' /etc/default/grub || \
    sed -i '/^[ 	]*GRUB_CMDLINE_LINUX_DEFAULT.*/s/"$/ rd.convertfs"/' /etc/default/grub  || :
    if ! grep --no-message 'add_dracutmodules+=" convertfs "' /etc/dracut.conf.d/05-convertfs.conf; then
        cat >>/etc/dracut.conf.d/05-convertfs.conf<<EOF
add_dracutmodules+=" convertfs "
EOF
    fi
fi
# Clean up after the conversion is done.
if [ -L /var/run ] && [ -f /etc/dracut.conf.d/05-convertfs.conf ]; then
    sed -i '/^[ 	]*GRUB_CMDLINE_LINUX_DEFAULT.*/s/rd.convertfs//' /etc/default/grub || :
    [ -f /etc/dracut.conf.d/05-convertfs.conf ] && sed -i '/add_dracutmodules+="[ 	]*convertfs[ 	]*"/d' /etc/dracut.conf.d/05-convertfs.conf || :
    [ -s /etc/dracut.conf.d/05-convertfs.conf ] || rm -f /etc/dracut.conf.d/05-convertfs.conf || :
    [ -d /var/lock.lockmove~ ] && rm -rf /var/lock.lockmove~ || :
    [ -d /var/run.runmove~ ] && rm -rf /var/run.runmove~ || :
fi

# Remove obsolete legacy fillup template for /etc/sysconfig/kernel.
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
%config %{_sysconfdir}/dracut.conf.d/10-fips.conf
%{dracutlibdir}/modules.d/11fips
%{dracutlibdir}/modules.d/11fips-crypto-policies
%endif

%ifnarch %ix86
%files ima
%license COPYING
%config %{_sysconfdir}/dracut.conf.d/10-ima.conf
%{dracutlibdir}/modules.d/75securityfs
%{dracutlibdir}/modules.d/76masterkey
%{dracutlibdir}/modules.d/77integrity
%endif

%files tools
%{_bindir}/dracut-catimages
%{_mandir}/man8/dracut-catimages.8*
%{_tmpfilesdir}/dracut.conf

%files extra
%license COPYING

%{dracutlibdir}/modules.d/10dash
%{dracutlibdir}/modules.d/12caps
%ifarch ppc ppc64 ppc64le ppc64p7
%{dracutlibdir}/modules.d/70ppcmac
%endif
%ifarch s390 s390x
# RH-specific s390 modules, we take another approach.
%{dracutlibdir}/modules.d/74dasd
%{dracutlibdir}/modules.d/74dasd_mod
%{dracutlibdir}/modules.d/74zfcp
%endif
%{dracutlibdir}/modules.d/81busybox

%files
%license COPYING
%doc README.md NEWS.md AUTHORS
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
%{dracutlibdir}/dracut-cpio

%dir %{dracutlibdir}/modules.d
%{dracutlibdir}/modules.d/10bash
%{dracutlibdir}/modules.d/10systemd
%{dracutlibdir}/modules.d/10systemd-network-management
%ifnarch s390 s390x
%{dracutlibdir}/modules.d/10warpclock
%endif
%ifarch %ix86
%exclude %{dracutlibdir}/modules.d/11fips
%exclude %{dracutlibdir}/modules.d/11fips-crypto-policies
%endif
%{dracutlibdir}/modules.d/11systemd-ac-power
%{dracutlibdir}/modules.d/11systemd-ask-password
%{dracutlibdir}/modules.d/11systemd-battery-check
%{dracutlibdir}/modules.d/11systemd-bsod
%{dracutlibdir}/modules.d/11systemd-coredump
%{dracutlibdir}/modules.d/11systemd-creds
%{dracutlibdir}/modules.d/11systemd-cryptsetup
%{dracutlibdir}/modules.d/11systemd-hostnamed
%{dracutlibdir}/modules.d/11systemd-initrd
%{dracutlibdir}/modules.d/11systemd-integritysetup
%{dracutlibdir}/modules.d/11systemd-journald
%{dracutlibdir}/modules.d/11systemd-ldconfig
%{dracutlibdir}/modules.d/11systemd-modules-load
%{dracutlibdir}/modules.d/11systemd-networkd
%{dracutlibdir}/modules.d/11systemd-pcrphase
%{dracutlibdir}/modules.d/11systemd-portabled
%{dracutlibdir}/modules.d/11systemd-pstore
%{dracutlibdir}/modules.d/11systemd-repart
%{dracutlibdir}/modules.d/11systemd-resolved
%{dracutlibdir}/modules.d/11systemd-sysctl
%{dracutlibdir}/modules.d/11systemd-sysext
%{dracutlibdir}/modules.d/11systemd-timedated
%{dracutlibdir}/modules.d/11systemd-timesyncd
%{dracutlibdir}/modules.d/11systemd-tmpfiles
%{dracutlibdir}/modules.d/11systemd-udevd
%{dracutlibdir}/modules.d/11systemd-veritysetup
%{dracutlibdir}/modules.d/13modsign
%{dracutlibdir}/modules.d/13rescue
%{dracutlibdir}/modules.d/14watchdog
%{dracutlibdir}/modules.d/14watchdog-modules
%{dracutlibdir}/modules.d/16dbus-broker
%{dracutlibdir}/modules.d/16dbus-daemon
%{dracutlibdir}/modules.d/16rngd
%{dracutlibdir}/modules.d/19dbus
%{dracutlibdir}/modules.d/20i18n
%{dracutlibdir}/modules.d/30convertfs
%{dracutlibdir}/modules.d/35connman
%{dracutlibdir}/modules.d/35network-legacy
%{dracutlibdir}/modules.d/35network-manager
%{dracutlibdir}/modules.d/40network
%{dracutlibdir}/modules.d/45drm
%{dracutlibdir}/modules.d/45net-lib
%{dracutlibdir}/modules.d/45plymouth
%{dracutlibdir}/modules.d/45simpledrm
%{dracutlibdir}/modules.d/45systemd-import
%{dracutlibdir}/modules.d/45url-lib
%ifarch s390 s390x
%{dracutlibdir}/modules.d/68cms
%endif
%{dracutlibdir}/modules.d/68lvmmerge
%{dracutlibdir}/modules.d/68lvmthinpool-monitor
%ifarch s390 s390x
%{dracutlibdir}/modules.d/69cio_ignore
%endif
%{dracutlibdir}/modules.d/70bluetooth
%{dracutlibdir}/modules.d/70btrfs
%{dracutlibdir}/modules.d/70crypt
%{dracutlibdir}/modules.d/70dm
%{dracutlibdir}/modules.d/70dmraid
%{dracutlibdir}/modules.d/70dmsquash-live
%{dracutlibdir}/modules.d/70dmsquash-live-autooverlay
%{dracutlibdir}/modules.d/70dmsquash-live-ntfs
%{dracutlibdir}/modules.d/70fs-lib
%{dracutlibdir}/modules.d/70img-lib
%{dracutlibdir}/modules.d/70kernel-modules
%{dracutlibdir}/modules.d/70kernel-modules-export
%{dracutlibdir}/modules.d/70kernel-modules-extra
%{dracutlibdir}/modules.d/70kernel-network-modules
%{dracutlibdir}/modules.d/70livenet
%{dracutlibdir}/modules.d/70lvm
%{dracutlibdir}/modules.d/70mdraid
%{dracutlibdir}/modules.d/70multipath
%{dracutlibdir}/modules.d/70numlock
%{dracutlibdir}/modules.d/70nvdimm
%{dracutlibdir}/modules.d/70overlayfs
%{dracutlibdir}/modules.d/70pcmcia
%{dracutlibdir}/modules.d/70qemu
%{dracutlibdir}/modules.d/70qemu-net
%{dracutlibdir}/modules.d/70uefi-lib
%{dracutlibdir}/modules.d/73crypt-gpg
%{dracutlibdir}/modules.d/73crypt-loop
%{dracutlibdir}/modules.d/73fido2
%{dracutlibdir}/modules.d/73pcsc
%{dracutlibdir}/modules.d/73pkcs11
%{dracutlibdir}/modules.d/73tpm2-tss
%ifarch s390 s390x
%{dracutlibdir}/modules.d/73zipl
%endif
%{dracutlibdir}/modules.d/74cifs
%ifarch s390 s390x
%{dracutlibdir}/modules.d/74dcssblk
%endif
%{dracutlibdir}/modules.d/74debug
%{dracutlibdir}/modules.d/74fcoe
%{dracutlibdir}/modules.d/74fcoe-uefi
%{dracutlibdir}/modules.d/74fstab-sys
%{dracutlibdir}/modules.d/74hwdb
%{dracutlibdir}/modules.d/74iscsi
%{dracutlibdir}/modules.d/74lunmask
%{dracutlibdir}/modules.d/74nbd
%{dracutlibdir}/modules.d/74nfs
%{dracutlibdir}/modules.d/74nvmf
%{dracutlibdir}/modules.d/74resume
%{dracutlibdir}/modules.d/74rootfs-block
%{dracutlibdir}/modules.d/74rootfs-block-fallback
%{dracutlibdir}/modules.d/74squash-erofs
%{dracutlibdir}/modules.d/74squash-squashfs
%{dracutlibdir}/modules.d/74ssh-client
%{dracutlibdir}/modules.d/74terminfo
%{dracutlibdir}/modules.d/74udev-rules
%{dracutlibdir}/modules.d/74virtfs
%{dracutlibdir}/modules.d/74virtiofs
%ifarch s390 s390x
%{dracutlibdir}/modules.d/74znet
%endif
%ifarch %ix86
%exclude %{dracutlibdir}/modules.d/75securityfs
%endif
%{dracutlibdir}/modules.d/76biosdevname
%ifarch %ix86
%exclude %{dracutlibdir}/modules.d/76masterkey
%endif
%{dracutlibdir}/modules.d/76systemd-emergency
%{dracutlibdir}/modules.d/77dracut-systemd
%{dracutlibdir}/modules.d/77ecryptfs
%{dracutlibdir}/modules.d/77initqueue
%ifarch %ix86
%exclude %{dracutlibdir}/modules.d/77integrity
%endif
%{dracutlibdir}/modules.d/77pollcdrom
%{dracutlibdir}/modules.d/77selinux
%{dracutlibdir}/modules.d/77syslog
%{dracutlibdir}/modules.d/77usrmount
%{dracutlibdir}/modules.d/78systemd-sysusers
%{dracutlibdir}/modules.d/80base
%{dracutlibdir}/modules.d/84memstrack
%{dracutlibdir}/modules.d/85shell-interpreter
%{dracutlibdir}/modules.d/86shutdown
%{dracutlibdir}/modules.d/87squash
%{dracutlibdir}/modules.d/88squash-lib
%{dracutlibdir}/modules.d/99suse
%{dracutlibdir}/modules.d/99suse-initrd
%attr(0640,root,root) %ghost %config(missingok,noreplace) %{_localstatedir}/log/dracut.log
%dir %{_unitdir}/initrd.target.wants
%dir %{_unitdir}/sysinit.target.wants
%{_unitdir}/*.service
%{_unitdir}/*/*.service

%changelog
