#
# spec file for package s390-tools
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
# needssslcertforbuild


#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir %{_localstatedir}/adm/fillup-templates
%endif

Name:           s390-tools
Version:        2.11.0
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

Patch1:         s390-tools-sles15sp2-01-zkey-Separate-and-rework-CCA-host-library-loading.patch
Patch2:         s390-tools-sles15sp2-02-zkey-Move-utility-functions-into-separate-source-fil.patch
Patch3:         s390-tools-sles15sp2-03-zkey-Add-utility-function-to-get-the-serial-number-o.patch
Patch4:         s390-tools-sles15sp2-04-zkey-Add-utility-function-to-get-the-mkvp-of-a-crypt.patch
Patch5:         s390-tools-sles15sp2-05-zkey-add-function-to-iterate-over-all-available-CCA-.patch
Patch6:         s390-tools-sles15sp2-06-zkey-Add-function-to-print-the-MKVPs-of-APQNs.patch
Patch7:         s390-tools-sles15sp2-07-zkey-Add-function-to-cross-check-APQNs-for-valid-mas.patch
Patch8:         s390-tools-sles15sp2-08-zkey-Add-function-to-obtain-the-mkvp-of-a-secure-key.patch
Patch9:         s390-tools-sles15sp2-09-zkey-Display-MKVP-when-validating-a-secure-key.patch
Patch10:        s390-tools-sles15sp2-10-zkey-Cross-check-APQNs-when-generating-secure-keys.patch
Patch11:        s390-tools-sles15sp2-11-zkey-Cross-check-APQNs-when-validating-secure-keys.patch
Patch12:        s390-tools-sles15sp2-12-zkey-Cross-check-APQNs-when-importing-secure-keys.patch
Patch13:        s390-tools-sles15sp2-13-zkey-Cross-check-APQNs-when-changing-APQN-associatio.patch
Patch14:        s390-tools-sles15sp2-14-zkey-Add-function-to-select-a-specific-CCA-adapter.patch
Patch15:        s390-tools-sles15sp2-15-zkey-Add-function-to-select-a-CCA-adapter-by-mkvp.patch
Patch16:        s390-tools-sles15sp2-16-zkey-Select-CCA-adapter-when-re-enciphering.patch
Patch17:        s390-tools-sles15sp2-17-zkey-cryptsetup-Add-to-new-and-from-old-options.patch
Patch18:        s390-tools-sles15sp2-18-zkey-Display-key-type-with-list-and-validate-command.patch
Patch19:        s390-tools-sles15sp2-19-zkey-Allow-to-filter-list-output-by-key-type.patch
Patch20:        s390-tools-sles15sp2-20-zkey-Allow-to-specify-the-key-type-with-the-generate.patch
Patch21:        s390-tools-sles15sp2-21-zkey-Preparations-for-introducing-a-new-key-type.patch
Patch22:        s390-tools-sles15sp2-22-zkey-Introduce-the-CCA-AESCIPHER-key-type.patch
Patch23:        s390-tools-sles15sp2-23-zkey-Add-wrappers-for-the-new-IOCTLs-with-fallback-t.patch
Patch24:        s390-tools-sles15sp2-24-zkey-Add-helper-functions-to-build-lists-of-APQNs.patch
Patch25:        s390-tools-sles15sp2-25-zkey-Add-support-for-generating-AES-CIPHER-keys.patch
Patch26:        s390-tools-sles15sp2-26-zkey-Add-support-for-validating-AES-CIPHER-keys.patch
Patch27:        s390-tools-sles15sp2-27-zkey-Add-support-for-re-enciphering-AES-CIPHER-keys.patch
Patch28:        s390-tools-sles15sp2-28-zkey-Check-crypto-card-level-during-APQN-cross-check.patch
Patch29:        s390-tools-sles15sp2-29-zkey-Add-helper-function-to-query-the-CCA-firmware-v.patch
Patch30:        s390-tools-sles15sp2-30-zkey-Add-helper-function-to-convert-secure-keys-betw.patch
Patch31:        s390-tools-sles15sp2-31-zkey-Add-helper-function-to-restrict-export-of-secur.patch
Patch32:        s390-tools-sles15sp2-32-zkey-Add-helper-function-to-check-an-AES-CIPHER-key.patch
Patch33:        s390-tools-sles15sp2-33-zkey-Add-key-checks-when-importing-a-CCA-AESCIPHER-k.patch
Patch34:        s390-tools-sles15sp2-34-zkey-Add-convert-command-to-convert-keys-from-one-ty.patch
Patch35:        s390-tools-sles15sp2-35-zkey-Allow-zkey-cryptsetup-setkey-to-set-different-k.patch
Patch36:        s390-tools-sles15sp2-zcrypt-CEX7S-exploitation-support.patch
Patch37:        s390-tools-sles15sp2-zcryptstats-Add-support-for-CEX7.patch
Patch38:        s390-tools-sles15sp2-zkey-Fix-listing-of-keys-on-file-systems-reporting-D.patch
Patch39:        s390-tools-sles15sp2-zkey-Fix-display-of-clear-key-size-for-XTS-keys.patch
Patch40:        s390-tools-sles15sp2-zkey-Fix-display-of-XTS-attribute-for-validate-comma.patch
Patch41:        s390-tools-sles15sp2-zkey-Fix-display-of-clear-key-size-for-CCA-AESCIPHER.patch
Patch42:        s390-tools-sles15sp2-01-zipl-libc-Introduce-vsnprintf.patch
Patch43:        s390-tools-sles15sp2-02-zipl-libc-Fix-potential-buffer-overflow-in-printf.patch
Patch44:        s390-tools-sles15sp2-03-zipl-libc-Replace-sprintf-with-snprintf.patch
Patch45:        s390-tools-sles15sp2-04-zipl-libc-Indicate-truncated-lines-in-printf-with.patch
Patch46:        s390-tools-sles15sp2-01-zpcictl-Initiate-recover-after-reset.patch
Patch47:        s390-tools-sles15sp2-02-zpcictl-Rename-misleading-sysfs_write_data.patch
Patch48:        s390-tools-sles15sp2-03-zpcitctl-Exit-on-error-in-sysfs_report_error.patch
Patch49:        s390-tools-sles15sp2-01-zipl-fix-Wdiscarded-qualifiers.patch
Patch50:        s390-tools-sles15sp2-02-zipl-fix-Waddress-of-packed-member.patch
Patch51:        s390-tools-sles15sp2-03-zipl-remove-some-useless-__packed___-attributes.patch
Patch52:        s390-tools-sles15sp2-04-zipl-Fix-entry-point-for-stand-alone-kdump.patch
Patch53:        s390-tools-sles15sp2-05-zipl-Fix-dependency-generation-in-zipl-boot.patch
Patch54:        s390-tools-sles15sp2-06-zipl-Make-use-of-__packed-macro.patch
Patch55:        s390-tools-sles15sp2-07-zipl-define-__section-macro-and-make-use-of-it.patch
Patch56:        s390-tools-sles15sp2-08-zipl-Make-use-of-__noreturn-macro.patch
Patch57:        s390-tools-sles15sp2-09-zipl-Define-__noinline-macro-and-make-use-of-it.patch
Patch58:        s390-tools-sles15sp2-10-zipl-stage3-Mark-start_kernel-__noreturn.patch
Patch59:        s390-tools-sles15sp2-11-zipl-sclp-Remove-duplicate-macros.patch
Patch60:        s390-tools-sles15sp2-12-zipl-Make-address-size-mask-macros-UL.patch
Patch61:        s390-tools-sles15sp2-13-zipl-libc-Use-stdint.h-instead-of-self-defined-macro.patch
Patch62:        s390-tools-sles15sp2-14-zipl-Consolidate-IMAGE-macros.patch
Patch63:        s390-tools-sles15sp2-15-zipl-Consolidate-STAGE-2-3-macros.patch
Patch64:        s390-tools-sles15sp2-16-zipl-stfle-use-uint64_t-instead-of-u64.patch
Patch65:        s390-tools-sles15sp2-17-zipl-boot-fix-comment-in-stage3.lds.patch
Patch66:        s390-tools-sles15sp2-18-lib-zt_common-add-STATIC_ASSERT-macro.patch
Patch67:        s390-tools-sles15sp2-19-zipl-use-STATIC_ASSERT-macro-for-no-padding-verifica.patch
Patch68:        s390-tools-sles15sp2-20-Support-lib-zt_common.h-to-be-used-in-assembler-and-.patch
Patch69:        s390-tools-sles15sp2-21-zipl-move-IPL-related-definitions-into-separate-head.patch
Patch70:        s390-tools-sles15sp2-22-zipl-move-SIGP-related-functions-and-definitions-int.patch
Patch71:        s390-tools-sles15sp2-23-zipl-add-SIGP_SET_ARCHITECTURE-to-sigp.h-and-use-it.patch
Patch72:        s390-tools-sles15sp2-24-zipl-stage3-make-IPL_DEVICE-definition-consistent-wi.patch
Patch73:        s390-tools-sles15sp2-25-zipl-move-Linux-layout-definitions-into-separate-hea.patch
Patch74:        s390-tools-sles15sp2-26-zipl-tape0-use-constants-defined-in-linux_layout.h.patch
Patch75:        s390-tools-sles15sp2-27-zipl-use-STAGE3_ENTRY-for-STAGE3_LOAD_ADDRESS.patch
Patch76:        s390-tools-sles15sp2-28-zipl-move-loaders-layout-definitions-into-separate-h.patch
Patch77:        s390-tools-sles15sp2-29-zipl-s390.h-rename-inline-macro-into-__always_inline.patch
Patch78:        s390-tools-sles15sp2-30-zipl-move-__always_inline-barrier-__pa32-pa-to-zt_co.patch
Patch79:        s390-tools-sles15sp2-31-zipl-make-BLK_PWRT-unsigned-int.patch
Patch80:        s390-tools-sles15sp2-32-Consolidate-MIN-and-MAX-macros.patch
Patch81:        s390-tools-sles15sp2-33-zipl-remove-libc.h-include-in-s390.h.patch
Patch82:        s390-tools-sles15sp2-34-zipl-move-s390.h-to-include-boot-s390.h.patch
Patch83:        s390-tools-sles15sp2-35-zipl-libc-include-s390.h.patch
Patch84:        s390-tools-sles15sp2-36-include-boot-s390.h-move-panic-and-panic_notify-to-l.patch
Patch85:        s390-tools-sles15sp2-37-include-boot-s390.h-fixes-for-Werror-sign-conversion.patch
Patch86:        s390-tools-sles15sp2-38-zipl-refactor-all-EBCDIC-code-into-separate-files.patch
Patch87:        s390-tools-sles15sp2-39-zipl-sclp-add-macros-for-the-control-program-masks.patch
Patch88:        s390-tools-sles15sp2-40-zipl-sclp-add-sclp_print_ascii.patch
Patch89:        s390-tools-sles15sp2-41-zipl-libc-printf-print-on-linemode-and-ASCII-console.patch
Patch90:        s390-tools-sles15sp2-42-Consolidate-ALIGN-__ALIGN_MASK-ARRAY_SIZE-macros.patch
Patch91:        s390-tools-sles15sp2-43-genprotimg-boot-initial-bootloader-support.patch
Patch92:        s390-tools-sles15sp2-44-genprotimg-boot-use-C-pre-processor-for-linker-scrip.patch
Patch93:        s390-tools-sles15sp2-45-genprotimg-add-relocator-for-stage3b.patch
Patch94:        s390-tools-sles15sp2-46-README.md-remove-useless-empty-line.patch
Patch95:        s390-tools-sles15sp2-47-include-boot-s390.h-add-guard-for-struct-__vector128.patch
Patch96:        s390-tools-sles15sp2-48-genprotimg-introduce-new-tool-for-the-creation-of-PV.patch
Patch97:        s390-tools-sles15sp2-01-zipl-Add-missing-options-to-help-output.patch
Patch98:        s390-tools-sles15sp2-02-zipl-allow-stand-alone-secure-option-on-command-l.patch
Patch99:        s390-tools-sles15sp2-03-zipl-correct-secure-boot-config-handling.patch
Patch100:       s390-tools-sles15sp2-04-zipl-fix-zipl.conf-man-page-example-for-secure-boot.patch
Patch101:       s390-tools-sles15sp2-01-cpumf-add-new-deflate-counters-for-z15.patch
Patch102:       s390-tools-sles15sp2-vmcp-exit-code.patch
Patch103:       s390-tools-sles15sp2-zipl-prevent-endless-loop-during-IPL.patch
Patch104:       s390-tools-sles15sp2-zipl-check-for-valid-ipl-parmblock-lowcore-pointer.patch
Patch105:       s390-tools-sles15sp2-01-zipl-libc-libc_stop-move-noreturn-to-declaration.patch
Patch106:       s390-tools-sles15sp2-02-zipl-stage3-correctly-handle-diag308-response-code.patch
Patch107:       s390-tools-sles15sp2-lsluns-try-harder-to-find-udevadm.patch
Patch108:       s390-tools-sles15sp2-znetconf-introduce-better-ways-to-locate-udevadm.patch
Patch109:       s390-tools-sles15sp2-mon_tools-update-udevadm-location.patch

# SUSE patches
Patch900:       s390-tools-sles12-zipl_boot_msg.patch
Patch901:       s390-tools-sles12-sysconfig-compatible-dumpconf.patch
Patch902:       s390-tools-sles12-create-filesystem-links.patch
Patch903:       s390-tools-sles12-update-by_id-links-on-change-and-add-action.patch
Patch904:       s390-tools-sles15-Allow-multiple-device-arguments.patch
Patch905:       s390-tools-sles15-Format-devices-in-parallel.patch
Patch906:       s390-tools-sles15-Implement-Y-yast_mode.patch
Patch907:       s390-tools-sles15-Implement-f-for-backwards-compability.patch
Patch908:       dasdfmt-retry-BIODASDINFO-if-device-is-busy.patch
Patch909:       59-dasd.rules-wait_for.patch
Patch910:       s390-tools-sles12-fdasd-skip-partition-check-and-BLKRRPART-ioctl.patch
Patch911:       s390-tools-sles15sp2-Close-file-descriptor-when-checking-for-read-only.patch
Patch912:       s390-tools-sles15sp1-zdev-Also-include-the-ctc-driver-in-the-initrd.patch
Patch913:       s390-tools-sles15sp1-11-zdev-Do-not-call-zipl-on-initrd-update.patch

BuildRequires:  dracut
BuildRequires:  fuse-devel
BuildRequires:  gcc-c++
BuildRequires:  gettext-tools
BuildRequires:  glib2-devel
BuildRequires:  glibc-devel-static
BuildRequires:  kernel-zfcpdump
BuildRequires:  libcryptsetup-devel > 2.0.3
BuildRequires:  libjson-c-devel
BuildRequires:  libpfm-devel
BuildRequires:  ncurses-devel
BuildRequires:  net-snmp-devel
BuildRequires:  pesign-obs-integration
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
mkdir -p %{buildroot}%{_sysconfdir}/zkey/repository
%make_install \
     ZFCPDUMP_DIR=%{_prefix}/lib/s390-tools/zfcpdump \
     DISTRELEASE=%{release} \
     SYSTEMDSYSTEMUNITDIR=%{_unitdir} \
     HAVE_DRACUT=1

# The make install command puts things in /etc/sysconfig and not the
# fillup-templates directory. Let's try moving them where they belong
mkdir -p %{buildroot}%{_fillupdir}
pushd %{buildroot}%{_sysconfdir}/sysconfig/
for sysconffile in *
  do mv -vi $sysconffile %{buildroot}%{_fillupdir}/sysconfig.$sysconffile
  done
popd

install -m 755 read_values %{buildroot}/%{_bindir}/
install -m644 -t %{buildroot}/%{_mandir}/man8 %{SOURCE87}

export ROOT_BUILD_DIR="%{_builddir}/%{name}-%{version}/zfcpdump/kernel"
install -D -m600 /boot/image-*-zfcpdump %{buildroot}%{_prefix}/lib/s390-tools/zfcpdump/zfcpdump-image

install -D -m644 etc/cpuplugd.conf %{buildroot}%{_sysconfdir}/cpuplugd.conf
install -D -m644 etc/udev/rules.d/40-z90crypt.rules %{buildroot}%{_prefix}/lib/udev/rules.d/40-z90crypt.rules
install -D -m644 etc/udev/rules.d/57-osasnmpd.rules %{buildroot}%{_prefix}/lib/udev/rules.d/57-osasnmpd.rules
install -D -m644 etc/udev/rules.d/59-dasd.rules %{buildroot}%{_prefix}/lib/udev/rules.d/59-dasd.rules
install -D -m644 etc/udev/rules.d/90-cpi.rules %{buildroot}%{_prefix}/lib/udev/rules.d/90-cpi.rules
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
install -D -m755 %{SOURCE24} %{buildroot}%{_bindir}/cputype

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
mkdir -p ./%{_libexecdir}/net-snmp/agents
cd	 ./%{_libexecdir}/net-snmp/agents
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

export BRP_PESIGN_FILES='/lib/s390-tools/stage3.bin'

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
%dir %{_datadir}/s390-tools/genprotimg
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
%{_libexecdir}/net-snmp/agents/osasnmpd

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
