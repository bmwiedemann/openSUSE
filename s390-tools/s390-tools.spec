#
# spec file for package s390-tools
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


#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir %{_localstatedir}/adm/fillup-templates
%endif

Name:           s390-tools
Version:        2.1.0
Release:        0
Summary:        S/390 tools like zipl and dasdfmt
License:        MIT
Group:          System/Kernel
URL:            https://github.com/ibm-s390-tools/s390-tools
Source:         https://github.com/ibm-s390-tools/s390-tools/archive/v%{version}.tar.gz#/s390-tools-%{version}.tar.gz
Source1:        s390-tools-rpmlintrc
Source2:        zipl.conf
Source3:        hsnc
Source4:        sysconfig.hsnc
Source5:        xpram
Source6:        sysconfig.xpram
Source7:        appldata
Source8:        sysconfig.appldata
Source10:       dasdro
Source11:       dasd_reload
Source12:       mkdump.pl
Source13:       sysconfig.osasnmpd
Source14:       zfcp_san_disc
Source15:       mkdump.8
Source18:       zpxe.rexx
Source19:       rules.xpram
Source20:       rules.hw_random
Source21:       59-graf.rules
Source22:       s390-tools-zdsfs.caution.txt
Source23:       README.SUSE
Source24:       cputype
Source25:       cputype.1
Source26:       cio_ignore.service
Source27:       setup_cio_ignore.sh
Source28:       59-prng.rules
Source29:       59-zfcp-compat.rules
Source30:       90-s390-tools.conf
Source31:       detach_disks.sh
Source32:       killcdl
Source33:       lgr_check
Source34:       sysconfig.virtsetup
Source35:       virtsetup.service
Source36:       virtsetup.sh
Source37:       appldata.service
Source38:       hsnc.service
Source39:       vmlogrdr.service
Source40:       xpram.service
Source41:       pkey.conf

### Obsolete scripts and man pages to be removed once changes in other tools are made
### That's been delayed to at least SLES12 SP1, but I'm leaving the comments here.
Source86:       read_values.c
Source87:       read_values.8
Source88:       ctc_configure
Source89:       dasd_configure
Source90:       iucv_configure
Source91:       qeth_configure
Source92:       zfcp_disk_configure
Source93:       zfcp_host_configure
Source94:       ctc_configure.8
Source95:       dasd_configure.8
Source96:       iucv_configure.8
Source97:       qeth_configure.8
Source98:       zfcp_disk_configure.8
Source99:       zfcp_host_configure.8
###

Patch1:         s390-tools-sles12-zipl_boot_msg.patch
Patch2:         s390-tools-sles12-sysconfig-compatible-dumpconf.patch
Patch3:         s390-tools-sles12-create-filesystem-links.patch
Patch4:         s390-tools-sles12-update-by_id-links-on-change-and-add-action.patch
Patch5:         s390-tools-sles15-Fixup-dasdfmt_get_volser.patch
Patch6:         s390-tools-sles15-Fixup-device-name-handling.patch
Patch7:         s390-tools-sles15-Drop-device_id-parameter.patch
Patch8:         s390-tools-sles15-Allow-multiple-device-arguments.patch
Patch9:         s390-tools-sles15-Format-devices-in-parallel.patch
Patch10:        s390-tools-sles15-Implement-Y-yast_mode.patch
Patch11:        s390-tools-sles15-Implement-f-for-backwards-compability.patch
Patch12:        dasdfmt-retry-BIODASDINFO-if-device-is-busy.patch
Patch13:        59-dasd.rules-wait_for.patch
Patch14:        s390-tools-sles12-fdasd-skip-partition-check-and-BLKRRPART-ioctl.patch
Patch15:        s390-tools-sles15-Fix-truncation-warning.patch
Patch16:        s390-tools-sles15-iucvterm-include-ctype-for-toupper.patch
Patch17:        s390-tools-sles15-zdev-Use-correct-path-to-vmcp-binary.patch
Patch18:        s390-tools-sles15-cpi-add-unit-install-section.patch
Patch19:        s390-tools-sles15-zipl-remove-invalid-dasdview-command-line-option.patch
Patch20:        s390-tools-sles15-ziomon-re-add-missing-line.patch
Patch21:        s390-tools-sles15-cpuplugd-Improve-systemctl-start-error-handling.patch
Patch22:        s390-tools-sles15-mon_tools-Improve-systemctl-start-error-handling.patch
Patch23:        s390-tools-sles15-lsluns-do-not-scan-all-if-filters-match-nothing.patch
Patch24:        s390-tools-sles15-lsluns-do-not-print-confusing-messages-when-a-filter.patch
Patch25:        s390-tools-sles15-lsluns-fix-flawed-formatting-of-man-page.patch
Patch26:        s390-tools-sles15-lsluns-enhance-usage-statement-and-man-page.patch
Patch27:        s390-tools-sles15-lsluns-clarify-discovery-use-case-relation-to-NPIV-a.patch
Patch28:        s390-tools-sles15-lsluns-point-out-IBM-Storwize-configuration-requirem.patch
Patch29:        s390-tools-sles15-lsluns-document-restriction-to-zfcp-only-systems.patch
Patch30:        s390-tools-sles15-lsluns-complement-alternative-tools-with-lszdev.patch
Patch31:        s390-tools-sles15-zdev-Enable-running-chzdev-from-unknown-root-devices.patch
Patch32:        s390-tools-sles15-zdev-Fix-zdev-dracut-module-aborting-on-unknown-root.patch
Patch33:        s390-tools-sles15-hmcdrvfs-fix-parsing-of-link-count.patch
Patch34:        s390-tools-sles15-dbginfo-add-data-for-ps-cpprot.patch
Patch35:        s390-tools-sles15-mon_procd-fix-parsing-of-proc-pid-stat.patch
Patch36:        s390-tools-sles15-1-lstape-fix-output-with-SCSI-lin_tape-and-multiple-pa.patch
Patch37:        s390-tools-sles15-2-lstape-fix-to-prefer-sysfs-to-find-lin_tape-device-n.patch
Patch38:        s390-tools-sles15-3-lstape-fix-output-without-SCSI-generic-sg.patch
Patch39:        s390-tools-sles15-4-lsluns-fix-to-prevent-error-messages-if-there-are-no.patch
Patch40:        s390-tools-sles15-5-lstape-fix-to-prevent-error-messages-if-there-are-no.patch
Patch41:        s390-tools-sles15-6-lstape-fix-description-of-type-and-devbusid-filter-f.patch
Patch42:        s390-tools-sles15-7-lstape-fix-SCSI-output-description-in-man-page.patch
Patch43:        s390-tools-sles15-8-lstape-fix-SCSI-HBA-CCW-device-bus-ID-e.g.-for-virti.patch
Patch44:        s390-tools-sles15sp1-0001-zkey-Add-properties-file-handling-routines.patch
Patch45:        s390-tools-sles15sp1-0002-zkey-Add-build-dependency-to-OpenSSL-libcrypto.patch
Patch46:        s390-tools-sles15sp1-0003-zkey-Add-helper-functions-for-comma-separated-string.patch
Patch47:        s390-tools-sles15sp1-0004-zkey-Externalize-secure-key-back-end-functions.patch
Patch48:        s390-tools-sles15sp1-0005-zkey-Add-keystore-implementation.patch
Patch49:        s390-tools-sles15sp1-0006-zkey-Add-keystore-related-commands.patch
Patch50:        s390-tools-sles15sp1-0007-zkey-Create-key-repository-and-group-during-make-ins.patch
Patch51:        s390-tools-sles15sp1-0008-zkey-Man-page-updates.patch
Patch52:        s390-tools-sles15sp1-0009-zkey-let-packaging-create-the-zkeyadm-group-and-perm.patch
Patch53:        s390-tools-sles15sp1-0010-zkey-Update-README-to-add-info-about-packaging-requi.patch
Patch54:        s390-tools-sles15sp1-0011-zkey-Typo-in-message.patch
Patch55:        s390-tools-sles15sp1-0012-zkey-Fix-memory-leak.patch
Patch56:        s390-tools-sles15sp1-0013-zkey-Fix-APQN-validation-routine.patch
Patch57:        s390-tools-sles15sp1-0014-zkey-Fix-generate-and-import-leaving-key-in-an-incon.patch
Patch58:        s390-tools-sles15sp1-0015-zkey-Add-zkey-cryptsetup-tool.patch
Patch59:        s390-tools-sles15sp1-0016-zkey-Add-man-page-for-zkey-cryptsetup.patch
Patch60:        s390-tools-sles15sp1-0017-zkey-Add-build-dependency-for-libcryptsetup-and-json.patch
Patch61:        s390-tools-sles15sp1-0018-zkey-Add-key-verification-pattern-property.patch
Patch62:        s390-tools-sles15sp1-0019-zkey-Add-volume-type-property-to-support-LUKS2-volum.patch
Patch63:        s390-tools-sles15sp1-01-lszcrypt-CEX6S-exploitation.patch
Patch64:        s390-tools-sles15sp1-02-lszcrypt-fix-date-and-wrong-indentation.patch
Patch65:        s390-tools-sles15sp1-01-chzcrypt-Corrections-at-the-chzcrypt-man-page.patch
Patch66:        s390-tools-sles15sp1-02-lszcrypt-support-for-alternate-zcrypt-device-drivers.patch
Patch67:        s390-tools-sles15sp1-01-zcryptctl-new-tool-zcryptctl-for-multiple-zcrypt-node.patch
Patch68:        s390-tools-sles15sp1-01-cpumf-Add-extended-counter-defintion-files-for-IBM-z.patch
Patch69:        s390-tools-sles15sp1-02-cpumf-z14-split-counter-sets-according-to-CFVN-CSVN-.patch
Patch70:        s390-tools-sles15sp1-03-cpumf-cpumf_helper-read-split-counter-sets-part-2-2.patch
Patch71:        s390-tools-sles15sp1-04-cpumf-correct-z14-counter-number.patch
Patch72:        s390-tools-sles15sp1-05-cpumf-add-missing-Description-tag-for-z13-z14-ctr-12.patch
Patch73:        s390-tools-sles15sp1-06-cpumf-correct-counter-name-for-z13-and-z14.patch
Patch74:        s390-tools-sles15sp1-07-cpumf-Add-IBM-z14-ZR1-to-the-CPU-Measurement-Facilit.patch
Patch75:        s390-tools-sles15sp1-01-util_path-add-function-to-check-if-a-path-exists.patch
Patch76:        s390-tools-sles15sp1-02-util_path-Add-description-for-util_path_exists.patch
Patch77:        s390-tools-sles15sp1-03-util_path-Make-true-false-handling-consistent-with-o.patch
Patch78:        s390-tools-sles15sp1-04-zpcictl-Introduce-new-tool-zpcictl.patch
Patch79:        s390-tools-sles15sp1-05-zpcictl-include-sys-sysmacros.h-to-avoid-minor-major.patch
Patch80:        s390-tools-sles15sp1-06-zpcictl-Rephrase-man-page-entries-and-tool-output.patch
Patch81:        s390-tools-sles15sp1-07-zpcictl-Use-fopen-instead-of-open-for-writes.patch
Patch82:        s390-tools-sles15sp1-08-zpcictl-Read-device-link-to-obtain-device-address.patch
Patch83:        s390-tools-sles15sp1-09-zpcictl-Make-device-node-for-NVMe-optional.patch
Patch84:        s390-tools-sles15sp1-10-zpcictl-Change-wording-of-man-page-and-help-output.patch
Patch85:        s390-tools-sles15sp1-dbginfo-gather-nvme-related-data.patch
Patch86:        s390-tools-sles15sp1-01-zdev-use-libutil-provided-path-functions.patch
Patch87:        s390-tools-sles15sp1-02-zdev-Prepare-for-firmware-configuration-file-support.patch
Patch88:        s390-tools-sles15sp1-03-zdev-Add-support-for-reading-firmware-configuration-.patch
Patch89:        s390-tools-sles15sp1-04-zdev-Implement-no-settle.patch
Patch90:        s390-tools-sles15sp1-05-zdev-Write-zfcp-lun-udev-rules-to-separate-files.patch
Patch91:        s390-tools-sles15sp1-06-zdev-Add-support-for-handling-auto-configuration-dat.patch
Patch92:        s390-tools-sles15sp1-07-zdev-Integrate-firmware-auto-configuration-with-drac.patch
Patch93:        s390-tools-sles15sp1-08-zdev-Integrate-firmware-auto-configuration-with-init.patch
Patch94:        s390-tools-sles15sp1-09-zdev-Implement-internal-device-attributes.patch
Patch95:        s390-tools-sles15sp1-10-zdev-Implement-support-for-early-device-configuratio.patch
Patch96:        s390-tools-sles15sp1-11-zdev-Do-not-call-zipl-on-initrd-update.patch
Patch97:        s390-tools-sles15sp1-zdev-fix-qeth-BridgePort-and-VNICC-conflict-checking.patch
Patch98:        s390-tools-sles15sp1-qethqoat-add-OSA-Express7S-support.patch
Patch99:        s390-tools-sles15sp1-01-zkey-Include-sbin-into-PATH-when-executing-commands.patch
Patch100:       s390-tools-sles15sp1-zkey-Enhance-error-message-about-missing-CCA-library.patch
Patch101:       s390-tools-sles15sp1-zdev-Also-include-the-ctc-driver-in-the-initrd.patch
Patch102:       s390-tools-sles15sp1-zcrypt-refine-lszcrypt-man-page.patch

BuildRequires:  dracut
BuildRequires:  fuse-devel
BuildRequires:  gcc-c++
BuildRequires:  gettext-tools
BuildRequires:  glibc-devel-static
BuildRequires:  kernel-zfcpdump
BuildRequires:  libcryptsetup-devel > 2.0.3
BuildRequires:  libjson-c-devel
BuildRequires:  libpfm-devel
BuildRequires:  ncurses-devel
BuildRequires:  net-snmp-devel
BuildRequires:  qclib-devel-static
BuildRequires:  tcpd-devel
BuildRequires:  zlib-devel-static
# Don't build with pie to avoid problems with zipl
#!BuildIgnore:  gcc-PIE
Requires(pre):  shadow
Requires(post): %fillup_prereq permissions
Requires:       coreutils
Requires:       gawk
Requires:       perl-base
Requires:       procps
Requires:       rsync
Requires:       tar
Requires:       util-linux
Recommends:     blktrace
Provides:       s390utils:/sbin/dasdfmt
ExclusiveArch:  s390x

%description
This package contains the tools needed to use Linux on IBM z Systems
and exploit many of the various capabilities of the hardware or z/VM.
For example:
dasdfmt  - low-level format tool for ECKD DASD
fdasd	 - partitions ECKD DASDs with z/OS compatible disk layout
zipl     - boot loader and dump DASD initializer
zgetdump - tool to get linux system dumps from DASD

%package -n osasnmpd
Summary:        OSA-Express SNMP subagent
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Other
Requires:       perl

%description -n osasnmpd
Supports management information bases (MIBs) provided by OSA-Express
Fast Ethernet, Gigabit Ethernet, High Speed Token Ring and ATM Ethernet
LAN Emulation features in QDIO mode.

It extends the capabilities of the net-snmp master agent (snmpd) and
communicates with him via the AgentX protocol.


%package zdsfs
Summary:        QSAM access to z/OS data
License:        GPL-2.0-or-later AND NonFree
Group:          Productivity/Networking/Other

%description zdsfs
Use the zdsfs command for read access to z/OS data sets stored on one or more DASDs.

The zdsfs file system translates the record-based z/OS data sets to UNIX file system
semantics.  After mounting the devices, you can use common Linux tools to access
the files on the disk. Physical sequential data sets are represented as files.
Partitioned  data  sets  are  represented as directories, with each member being
represented as a file in that directory.

%package hmcdrvfs
Summary:        HMC drive file system based on FUSE
License:        GPL-2.0-only
Group:          System/Filesystems
Requires:       fuse

%description hmcdrvfs
This package contains a HMC drive file system based on FUSE and a tool
to list files and directories.

%prep
%autosetup -p1

cp -vi %{SOURCE22} CAUTION

%build

# The "DISTRELEASE=%%{release}" needs to be on both the make and make install
# commands, since make install runs sed commands against various scripts to
# modify the "-v" output appropriately.

export OPT_FLAGS="%{optflags}"
export KERNELIMAGE_MAKEFLAGS="%%{?_smp_mflags}"
make %{?_smp_mflags} \
     ZFCPDUMP_DIR=%{_prefix}/lib/s390-tools/zfcpdump \
     DISTRELEASE=%{release}
gcc -static -o read_values ${OPT_FLAGS} %{SOURCE86} -lqc

%install
mkdir -p %{buildroot}/boot/zipl
mkdir -p %{buildroot}%{_sysconfdir}//zkey/repository
%make_install \
     ZFCPDUMP_DIR=%{_prefix}/lib/s390-tools/zfcpdump \
     DISTRELEASE=%{release} \
     SYSTEMDSYSTEMUNITDIR=%{_unitdir} \
     HAVE_DRACUT=1

install -m 755 read_values %{buildroot}/%{_bindir}/
install -m644 -t %{buildroot}/%{_mandir}/man8 %{SOURCE87}

export ROOT_BUILD_DIR="%{_builddir}/%{name}-%{version}/zfcpdump/kernel"
install -D -m600 /boot/image-*-zfcpdump %{buildroot}%{_prefix}/lib/s390-tools/zfcpdump/zfcpdump_part.image

install -D -m644 etc/cpuplugd.conf %{buildroot}%{_sysconfdir}/cpuplugd.conf
install -D -m644 etc/udev/rules.d/40-z90crypt.rules %{buildroot}%{_prefix}/lib/udev/rules.d/40-z90crypt.rules
install -D -m644 etc/udev/rules.d/57-osasnmpd.rules %{buildroot}%{_prefix}/lib/udev/rules.d/57-osasnmpd.rules
install -D -m644 etc/udev/rules.d/59-dasd.rules %{buildroot}%{_prefix}/lib/udev/rules.d/59-dasd.rules
install -D -m644 etc/udev/rules.d/90-cpi.rules %{buildroot}%{_prefix}/lib/udev/rules.d/90-cpi.rules
install -D -m644 etc/sysconfig/cpi %{buildroot}%{_fillupdir}/sysconfig.cpi
install -D -m644 etc/sysconfig/dumpconf %{buildroot}%{_fillupdir}/sysconfig.dumpconf
install -D -m644 etc/sysconfig/mon_fsstatd %{buildroot}%{_fillupdir}/sysconfig.mon_fsstatd
install -D -m644 etc/sysconfig/mon_procd %{buildroot}%{_fillupdir}/sysconfig.mon_procd
mv iucvterm/doc/ts-shell/iucvconn_on_login %{buildroot}%{_bindir}/iucvconn_on_login
install -D -m644 %{SOURCE26} %{buildroot}/%{_unitdir}/cio_ignore.service
install -D -m755 %{SOURCE27} %{buildroot}%{_prefix}/lib/systemd/scripts/setup_cio_ignore.sh
install -D -m755 %{SOURCE31} %{buildroot}%{_prefix}/lib/systemd/scripts/detach_disks.sh
install -D -m644 %{SOURCE35} %{buildroot}/%{_unitdir}/virtsetup.service
install -D -m755 %{SOURCE36} %{buildroot}%{_prefix}/lib/systemd/scripts/virtsetup.sh
install -D -m644 %{SOURCE37} %{buildroot}/%{_unitdir}/appldata.service
install -D -m644 %{SOURCE38} %{buildroot}/%{_unitdir}/hsnc.service
install -D -m644 %{SOURCE39} %{buildroot}/%{_unitdir}/vmlogrdr.service
install -D -m644 %{SOURCE40} %{buildroot}/%{_unitdir}/xpram.service
install -D -m644 %{SOURCE41} %{buildroot}%{_prefix}/lib/modules-load.d/pkey.conf

cp %{SOURCE18} zpxe.rexx
cp %{SOURCE2} zipl.conf.sample
cp  %{SOURCE23} README.SUSE

cd %{buildroot}
install -D -m755 %{SOURCE3} %{buildroot}%{_prefix}/lib/systemd/scripts/hsnc
install -D -m644 %{SOURCE4} %{buildroot}%{_fillupdir}/sysconfig.hsnc
install -D -m755 %{SOURCE5} %{buildroot}%{_prefix}/lib/systemd/scripts/xpram
install -D -m644 %{SOURCE6} %{buildroot}%{_fillupdir}/sysconfig.xpram
install -D -m755 %{SOURCE7} %{buildroot}%{_prefix}/lib/systemd/scripts/appldata
install -D -m644 %{SOURCE8} %{buildroot}%{_fillupdir}/sysconfig.appldata
install -D -m755 %{SOURCE10} sbin/dasdro
install -D -m755 %{SOURCE11} sbin/dasd_reload
install -D -m755 %{SOURCE12} sbin/mkdump
install -D -m644 %{SOURCE13} %{buildroot}%{_fillupdir}/sysconfig.osasnmpd
install -D -m755 %{SOURCE14} sbin/zfcp_san_disc
install -D -m644 %{SOURCE15} %{buildroot}/%{_mandir}/man8
install -D -m644 %{SOURCE19} %{buildroot}%{_prefix}/lib/udev/rules.d/52-xpram.rules
install -D -m644 %{SOURCE20} %{buildroot}%{_prefix}/lib/udev/rules.d/52-hw_random.rules
install -D -m644 %{SOURCE21} %{buildroot}%{_prefix}/lib/udev/rules.d/59-graf.rules
install -D -m644 %{SOURCE28} %{buildroot}%{_prefix}/lib/udev/rules.d/59-prng.rules
install -D -m644 %{SOURCE29} %{buildroot}%{_prefix}/lib/udev/rules.d/59-zfcp-compat.rules
install -D -m644 %{SOURCE30} %{buildroot}%{_sysconfdir}/modprobe.d/90-s390-tools.conf
install -D -m755 %{SOURCE32} %{buildroot}/sbin/killcdl
install -D -m755 %{SOURCE33} %{buildroot}/sbin/lgr_check
install -D -m644 %{SOURCE34} %{buildroot}%{_fillupdir}/sysconfig.virtsetup

if [ ! -d %{_sbindir} ]; then
    rm -f %{_sbindir}
    mkdir -p %{_sbindir}
fi
(cd usr/sbin; ln -s service rcappldata)
(cd usr/sbin; ln -s service rchsnc)
(cd usr/sbin; ln -s service rcvmlogrdr)
(cd usr/sbin; ln -s service rcxpram)
(cd usr/sbin; ln -s service rccio_ignore)
(cd usr/sbin; ln -s service rccpacfstatsd)
(cd usr/sbin; ln -s service rccpi)
(cd usr/sbin; ln -s service rccpuplugd)
(cd usr/sbin; ln -s service rcdumpconf)
(cd usr/sbin; ln -s service rcmon_fsstatd)
(cd usr/sbin; ln -s service rcmon_procd)
(cd usr/sbin; ln -s service rcvirtsetup)

if [ ! -d %{_bindir} ]; then
    rm -f %{_bindir}
    mkdir -p %{_bindir}
fi
install -D -m755 %{SOURCE24} usr/bin/cputype

install -m644 -t %{buildroot}/%{_mandir}/man8 %{SOURCE25}

### Obsolete scripts and man pages to be removed once changes in other tools are made
install -m755 -t sbin/ %{SOURCE88} %{SOURCE89} %{SOURCE90} %{SOURCE91} %{SOURCE92} %{SOURCE93}
install -m644 -t %{buildroot}/%{_mandir}/man8 %{SOURCE94} %{SOURCE95} %{SOURCE96} %{SOURCE97} %{SOURCE98} %{SOURCE99}
###

### lsmem/chmem have been added to util-linux
rm -fv %{buildroot}/%{_mandir}/man8/lsmem.8*
rm -fv %{buildroot}/%{_mandir}/man8/chmem.8*
rm -fv %{buildroot}/%{_sbindir}/lsmem
rm -fv %{buildroot}/%{_sbindir}/chmem

find . ! -type d |
    sed 's/^.//;\-/man/-s/^.*$/%doc &.gz/' > %{_builddir}/%{name}-filelist
grep -v -E 'osasnmp|*\.conf$' %{_builddir}/%{name}-filelist >%{_builddir}/%{name}.list
grep    osasnmp[^-] %{_builddir}/%{name}-filelist >%{_builddir}/%{name}.osasnmp

touch boot/zipl/active_devices.txt
mkdir -p usr/lib/net-snmp/agents
cd	 usr/lib/net-snmp/agents
cat <<EOT >osasnmpd
#!/bin/sh
PIDFILE=%{_localstatedir}/run/osasnmpd.pid
function cleanup
{
        rm -f \$PIDFILE
        kill \`cat %{_localstatedir}/run/osasnmpd.real.pid\`
}
. %{_sysconfdir}/sysconfig/osasnmpd
trap cleanup 0
echo \$\$ >\$PIDFILE
%{_sbindir}/osasnmpd -f -P %{_localstatedir}/run/osasnmpd.real.pid \$OSASNMPD_PARAMETERS "\$@"
EOT
chmod 755 osasnmpd

%verifyscript
%verify_permissions -e %{_localstatedir}/log/ts-shell

%pre
# check for ts-shell group or create it
getent group ts-shell >/dev/null 2>&1 || groupadd -r ts-shell
# check for zkeyadm group or create it
getent group zkeyadm >/dev/null 2>&1 || groupadd -r zkeyadm
# check for cpacfstats group or create it
getent group cpacfstats >/dev/null 2>&1 || groupadd -r cpacfstats
%service_add_pre appldata.service
%service_add_pre cio_ignore.service
%service_add_pre cpacfstatsd.service
%service_add_pre cpi.service
%service_add_pre cpuplugd.service
%service_add_pre dumpconf.service
%service_add_pre hsnc.service
%service_add_pre mon_fsstatd.service
%service_add_pre mon_procd.service
%service_add_pre virtsetup.service
%service_add_pre vmlogrdr.service
%service_add_pre xpram.service

%post
read INITPGM < /proc/1/comm
if [ "${INITPGM}" = "systemd" ]; then
  echo "Running systemctl daemon-reload."
  systemctl daemon-reload
fi

%set_permissions %{_localstatedir}/log/ts-shell

# Create symbolic links to the scripts from setup and boot directories
%service_add_post appldata.service
%service_add_post cio_ignore.service
%service_add_post cpacfstatsd.service
%service_add_post cpi.service
%service_add_post cpuplugd.service
%service_add_post dumpconf.service
%service_add_post hsnc.service
%service_add_post mon_fsstatd.service
%service_add_post mon_procd.service
%service_add_post virtsetup.service
%service_add_post vmlogrdr.service
%service_add_post xpram.service

# Create the initial versions of the sysconfig files:
%{fillup_only -n appldata}
%{fillup_only -n cpi}
%{fillup_only -n dumpconf}
%{fillup_only -n hsnc}
%{fillup_only -n mon_fsstatd}
%{fillup_only -n mon_procd}
%{fillup_only -n mon_statd}
%{fillup_only -n virtsetup}
%{fillup_only -n xpram}

%triggerin -- kernel-default
grep -q '^%{_bindir}/ts-shell$' %{_sysconfdir}/shells \
	|| echo "%{_bindir}/ts-shell" >> %{_sysconfdir}/shells

%{?regenerate_initrd_post}

%post -n osasnmpd
%{fillup_only -n osasnmpd}

%preun
%service_del_preun appldata.service
%service_del_preun cio_ignore.service
%service_del_preun cpacfstatsd.service
%service_del_preun cpi.service
%service_del_preun cpuplugd.service
%service_del_preun dumpconf.service
%service_del_preun hsnc.service
%service_del_preun mon_fsstatd.service
%service_del_preun mon_procd.service
%service_del_preun virtsetup.service
%service_del_preun vmlogrdr.service
%service_del_preun xpram.service

%postun
%service_del_postun appldata.service
%service_del_postun cio_ignore.service
%service_del_postun cpacfstatsd.service
%service_del_postun cpi.service
%service_del_postun cpuplugd.service
%service_del_postun dumpconf.service
%service_del_postun hsnc.service
%service_del_postun mon_fsstatd.service
%service_del_postun mon_procd.service
%service_del_postun virtsetup.service
%service_del_postun vmlogrdr.service
%service_del_postun xpram.service

# Even though SLES15+ is systemd based, the build service doesn't
# run it, so we have to make sure we can safely issue the
# systemctl command.
read INITPGM < /proc/1/comm
if [ "${INITPGM}" = "systemd" ]; then
  echo "Running systemctl daemon-reload."
  systemctl daemon-reload
fi

if [ ! -x /boot/zipl ]; then
	echo "Attention, after uninstalling this package,"
	echo "you will NOT be able to IPL from DASD anymore!!!"
fi

if test x$1 = x0; then
	# remove ts-shell from /etc/shells
	grep -v '^%{_bindir}/ts-shell$' %{_sysconfdir}/shells > %{_sysconfdir}/shells.ts-new
	mv %{_sysconfdir}/shells.ts-new %{_sysconfdir}/shells
	chmod 0644 %{_sysconfdir}/shells
fi

%{?regenerate_initrd_post}

%posttrans
%{?regenerate_initrd_posttrans}

%preun -n osasnmpd
%{stop_on_removal osasnmpd}

%files -f %{_builddir}/%{name}.list
%defattr(-,root,root)
%doc README.md
%doc README.SUSE

%doc iucvterm/doc/ts-shell
%doc zpxe.rexx
%doc zipl.conf.sample
%dir %{_sysconfdir}/iucvterm
%config %attr(0640,root,ts-shell) %{_sysconfdir}/iucvterm/ts-audit-systems.conf
%config %attr(0640,root,ts-shell) %{_sysconfdir}/iucvterm/ts-authorization.conf
%config %attr(0640,root,ts-shell) %{_sysconfdir}/iucvterm/ts-shell.conf
%config %attr(0640,root,ts-shell) %{_sysconfdir}/iucvterm/unrestricted.conf
%dir %attr(0770,root,zkeyadm) %{_sysconfdir}/zkey
%dir %attr(0770,root,zkeyadm) %{_sysconfdir}/zkey/repository
%config %{_sysconfdir}/modprobe.d/90-s390-tools.conf
%config %{_sysconfdir}/cpuplugd.conf
%config(noreplace) /boot/zipl/active_devices.txt
%dir %attr(2770,root,ts-shell) %{_localstatedir}/log/ts-shell
%dir %{_sysconfdir}/cmsfs-fuse
%config %attr(0640,root,root) %{_sysconfdir}/cmsfs-fuse/filetypes.conf
%dir %{_prefix}/lib/s390-tools
%dir %{_prefix}/lib/s390-tools/zfcpdump
%dir %{_prefix}/lib/udev/rules.d
%dir %{_prefix}/lib/systemd/scripts
%dir %{_datadir}/s390-tools
%dir %{_datadir}/s390-tools/cpumf
%dir %{_datadir}/s390-tools/netboot
%dir %{_prefix}/lib/dracut/modules.d/95zdev
%dir /boot/zipl
%dir /lib/s390-tools/
%{_prefix}/lib/modules-load.d/pkey.conf
%exclude %{_prefix}/lib/udev/rules.d/57-osasnmpd.rules
%exclude %{_bindir}/zdsfs
%exclude %{_bindir}/hmcdrvfs
%exclude %{_sbindir}/lshmc
%exclude %{_mandir}/man1/zdsfs.1.gz
%exclude %{_mandir}/man1/hmcdrvfs.1.gz
%exclude %{_mandir}/man8/lshmc.8.gz

%files -n osasnmpd -f %{_builddir}/%{name}.osasnmp
%defattr(-,root,root)
%{_prefix}/lib/net-snmp/agents/osasnmpd

%files zdsfs
%defattr(-,root,root)
%doc CAUTION
%{_bindir}/zdsfs
%{_mandir}/man1/zdsfs.1%{?ext_man}

%files hmcdrvfs
%defattr(-,root,root)
%{_bindir}/hmcdrvfs
%{_sbindir}/lshmc
%{_mandir}/man1/hmcdrvfs.1%{?ext_man}
%{_mandir}/man8/lshmc.8%{?ext_man}

%changelog
