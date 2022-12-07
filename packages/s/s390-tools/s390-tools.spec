#
# spec file for package s390-tools
#
# Copyright (c) 2001-2022 SUSE LLC
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
%if 0%{?suse_version} < 1550 && 0%{?sle_version} <= 150300
# systemd-rpm-macros is wrong in 15.3 and below
%define _modprobedir /lib/modprobe.d
%endif
%global modprobe_d_files 90-s390-tools.conf
%if 0%{?usrmerged}
%define _mysbindir %{_sbindir}
%else
%define _mysbindir /sbin
%endif

Name:           s390-tools
Version:        2.24.0
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
%if 0%{?usrmerged}
Source11:       dasd_reload.opensuse
Source12:       mkdump.pl.opensuse
%else
Source11:       dasd_reload.suse
Source12:       mkdump.pl.suse
%endif
Source13:       sysconfig.osasnmpd
Source14:       zfcp_san_disc
Source15:       mkdump.8
Source18:       zpxe.rexx
Source19:       rules.xpram
Source20:       rules.hw_random
%if 0%{?usrmerged}
Source21:       59-graf.rules.opensuse
%else
Source21:       59-graf.rules.suse
%endif
Source22:       s390-tools-zdsfs.caution.txt
%if 0%{?usrmerged}
Source23:       README.SUSE.opensuse
%else
Source23:       README.SUSE.suse
%endif
Source24:       cputype
Source25:       cputype.1
Source26:       cio_ignore.service
Source27:       setup_cio_ignore.sh
Source28:       59-prng.rules
Source29:       59-zfcp-compat.rules
Source30:       90-s390-tools.conf
%if 0%{?usrmerged}
Source31:       detach_disks.sh.opensuse
Source32:       killcdl.opensuse
%else
Source31:       detach_disks.sh.suse
Source32:       killcdl.suse
%endif
Source33:       lgr_check
Source34:       sysconfig.virtsetup
Source35:       virtsetup.service
%if 0%{?usrmerged}
Source36:       virtsetup.sh.opensuse
%else
Source36:       virtsetup.sh.suse
%endif
Source37:       appldata.service
Source38:       hsnc.service
%if 0%{?usrmerged}
Source39:       vmlogrdr.service.opensuse
%else
Source39:       vmlogrdr.service.suse
%endif
Source40:       xpram.service
Source41:       pkey.conf

### Obsolete scripts and man pages to be removed once changes in other tools are made
### That's been delayed to at least SLES12 SP1, but I'm leaving the comments here.
Source86:       read_values.c
Source87:       read_values.8
Source88:       ctc_configure
%if 0%{?usrmerged}
Source89:       dasd_configure.opensuse
Source90:       iucv_configure.opensuse
%else
Source89:       dasd_configure.suse
Source90:       iucv_configure.suse
%endif
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

# IBM patches
Patch001:       s390-tools-sles15sp5-zipl-boot-disable-Warray-bounds-for-now.patch
Patch002:       s390-tools-sles15sp5-util_lockfile-fix-includes.patch
Patch003:       s390-tools-sles15sp5-ap_tools-ap-check-use-new-mdevctl-install-location.patch
# SUSE patches
Patch900:       s390-tools-sles12-zipl_boot_msg.patch
Patch901:       s390-tools-sles15-sysconfig-compatible-dumpconf.patch
Patch902:       s390-tools-sles12-create-filesystem-links.patch
%if 0%{?usrmerged}
Patch903:       s390-tools-sles12-update-by_id-links-on-change-and-add-action.patch.opensuse
%else
Patch903:       s390-tools-sles12-update-by_id-links-on-change-and-add-action.patch.suse
%endif
Patch904:       s390-tools-sles15sp3-Allow-multiple-device-arguments.patch
Patch905:       s390-tools-sles15sp3-Format-devices-in-parallel.patch
Patch906:       s390-tools-sles15sp3-Implement-Y-yast_mode.patch
Patch907:       s390-tools-sles15sp3-Implement-f-for-backwards-compability.patch
Patch908:       s390-tools-sles15sp3-dasdfmt-retry-BIODASDINFO-if-device-is-busy.patch
Patch909:       s390-tools-sles12-fdasd-skip-partition-check-and-BLKRRPART-ioctl.patch
Patch910:       s390-tools-sles15sp1-11-zdev-Do-not-call-zipl-on-initrd-update.patch
Patch911:       s390-tools-sles15sp5-remove-no-pie-link-arguments.patch
Patch999:       s390-tools-sles15sp5-fix-chown-commands-syntax.patch

BuildRequires:  curl-devel
BuildRequires:  dracut
BuildRequires:  fuse3-devel
BuildRequires:  gcc-c++
BuildRequires:  gettext-tools
BuildRequires:  glib2-devel
BuildRequires:  glibc-devel-static
BuildRequires:  kernel-zfcpdump
BuildRequires:  libcryptsetup-devel > 2.0.3
BuildRequires:  libjson-c-devel
BuildRequires:  libxml2-devel
BuildRequires:  mdevctl
BuildRequires:  ncurses-devel
BuildRequires:  net-snmp-devel
BuildRequires:  openssl-devel >= 1.1.1l
BuildRequires:  pesign-obs-integration
BuildRequires:  qclib-devel-static
BuildRequires:  systemd-devel
BuildRequires:  tcpd-devel
BuildRequires:  zlib-devel-static
# Don't build with pie to avoid problems with zipl
#!BuildIgnore:  gcc-PIE
Requires:       coreutils
Requires:       gawk
Requires:       perl-base
Requires:       procps
Requires:       rsync
Requires:       tar
Requires:       util-linux
Requires(post): %fillup_prereq
Requires(post): permissions
Requires(pre):  shadow
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

%package -n libekmfweb1
Summary:        IBM Enterprise Key Management Foundation - Web Edition client library
License:        MIT
Group:          System/Libraries

%description -n libekmfweb1
libekmfweb1 is a client library that provides access to IBM' Enterprise Key
Management Foundation – Web Edition.0 EKMF Web provides efficient and
security-rich centralized key management for IBM z/OS data set encryption
on IBM Z servers.

%package -n libekmfweb1-devel
Summary:        IBM Enterprise Key Management Foundation - Web Edition client library
License:        MIT
Group:          Development/Libraries/C and C++
Requires:       libekmfweb1 = %{version}

%description -n libekmfweb1-devel
libekmfweb1 is a client library that provides access to IBM' Enterprise Key
Management Foundation – Web Edition.0 EKMF Web provides efficient and
security-rich centralized key management for IBM z/OS data set encryption
on IBM Z servers.

%package -n libkmipclient1
Summary:        IBM Key Management Interoperability Protocol (KMIP) client library
License:        MIT
Group:          System/Libraries

%description -n libkmipclient1
Key Management Interoperability Protocol (KMIP) is a client/server
communication protocol for the storage and maintenance of key,
certificate, and secret objects. This client library enables secure
creation and storage of cryptographic objects on the IBM Security Key
Lifecycle Manager server. You must configure client devices to connect
to the server for key management operations.

%package -n libkmipclient1-devel
Summary:        Header files for the IBM Z KMIP client library
License:        MIT
Group:          Development/Libraries/C and C++
Requires:       libkmipclient1 = %{version}

%description -n libkmipclient1-devel
This package provides the header files and symbolic link to the
shared library for the IBM Z KMIP client library.

%package chreipl-fcp-mpath
Summary:        Use multipath information for re-IPL path failover
License:        MIT
Group:          System/Boot
BuildRequires:  bash
BuildRequires:  coreutils
## Required for build+install with ENABLE_DOC=1
#BuildRequires:  pandoc
BuildRequires:  sed
#BuildRequires:  gawk
#BuildRequires:  gzip
Requires:       bash
# Required for use with HAVE_DRACUT=1
Requires:       dracut
Requires:       multipath-tools
Requires:       udev
Requires(post): udev

%description chreipl-fcp-mpath
The chreipl-fcp-mpath toolset monitors udev events about paths to the
re-IPL volume. If the currently configured FCP re-IPL path becomes
unavailable, the toolset checks for operational paths to the same
volume. If available, it reconfigures the FCP re-IPL settings to use an
operational path.

%prep
%autosetup -p1

cp -vi %{SOURCE22} CAUTION

%build

# The "DISTRELEASE=%%{release}" needs to be on both the make and make install
# commands, since make install runs sed commands against various scripts to
# modify the "-v" output appropriately.

export OPT_FLAGS="%{optflags}"
export KERNELIMAGE_MAKEFLAGS="%%{?_smp_mflags}"
%make_build \
     ZFCPDUMP_DIR=%{_prefix}/lib/s390-tools/zfcpdump \
     DISTRELEASE=%{release} \
     UDEVRUNDIR=/run/udev \
     HAVE_DRACUT=1
gcc -static -o read_values ${OPT_FLAGS} %{SOURCE86} -lqc

%install
mkdir -p %{buildroot}/boot/zipl
mkdir -p %{buildroot}%{_sysconfdir}/zkey/repository
%make_install \
     ZFCPDUMP_DIR=%{_prefix}/lib/s390-tools/zfcpdump \
     DISTRELEASE=%{release} \
     SYSTEMDSYSTEMUNITDIR=%{_unitdir} \
     UDEVRUNDIR=/run/udev \
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

# The "usrmerge" has happened in openSUSE:Factory, but not yet in SLES.
# Make sure we look for the zfcpdump kernel image in the right place.
%if 0%{?usrmerged}
install -D -m600 %{_prefix}/lib/modules/*-zfcpdump/image %{buildroot}%{_prefix}/lib/s390-tools/zfcpdump/zfcpdump-image
%else
install -D -m600 /boot/image-*-zfcpdump %{buildroot}%{_prefix}/lib/s390-tools/zfcpdump/zfcpdump-image
%endif

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
install -D -m755 %{SOURCE10} %{buildroot}%{_mysbindir}/dasdro
install -D -m755 %{SOURCE11} %{buildroot}%{_mysbindir}/dasd_reload
install -D -m755 %{SOURCE12} %{buildroot}%{_mysbindir}/mkdump
install -D -m644 %{SOURCE13} %{buildroot}%{_fillupdir}/sysconfig.osasnmpd
install -D -m755 %{SOURCE14} %{buildroot}%{_mysbindir}/zfcp_san_disc
install -D -m644 %{SOURCE15} %{buildroot}/%{_mandir}/man8
install -D -m644 %{SOURCE19} %{buildroot}%{_prefix}/lib/udev/rules.d/52-xpram.rules
install -D -m644 %{SOURCE20} %{buildroot}%{_prefix}/lib/udev/rules.d/52-hw_random.rules
install -D -m644 %{SOURCE21} %{buildroot}%{_prefix}/lib/udev/rules.d/59-graf.rules
install -D -m644 %{SOURCE28} %{buildroot}%{_prefix}/lib/udev/rules.d/59-prng.rules
install -D -m644 %{SOURCE29} %{buildroot}%{_prefix}/lib/udev/rules.d/59-zfcp-compat.rules
install -D -m644 %{SOURCE30} %{buildroot}%{_modprobedir}/90-s390-tools.conf
install -D -m755 %{SOURCE32} %{buildroot}%{_mysbindir}/killcdl
install -D -m755 %{SOURCE33} %{buildroot}%{_mysbindir}/lgr_check
install -D -m644 %{SOURCE34} %{buildroot}%{_fillupdir}/sysconfig.virtsetup

if [ ! -d %{_mysbindir} ]; then
    rm -f %{_mysbindir}
    mkdir -p %{_mysbindir}
fi
(cd %{buildroot}%{_sbindir}; ln -s service rcappldata)
(cd %{buildroot}%{_sbindir}; ln -s service rchsnc)
(cd %{buildroot}%{_sbindir}; ln -s service rcvmlogrdr)
(cd %{buildroot}%{_sbindir}; ln -s service rcxpram)
(cd %{buildroot}%{_sbindir}; ln -s service rccio_ignore)
(cd %{buildroot}%{_sbindir}; ln -s service rccpacfstatsd)
(cd %{buildroot}%{_sbindir}; ln -s service rccpi)
(cd %{buildroot}%{_sbindir}; ln -s service rccpuplugd)
(cd %{buildroot}%{_sbindir}; ln -s service rcdumpconf)
(cd %{buildroot}%{_sbindir}; ln -s service rcmon_fsstatd)
(cd %{buildroot}%{_sbindir}; ln -s service rcmon_procd)
(cd %{buildroot}%{_sbindir}; ln -s service rcvirtsetup)

if [ ! -d %{_bindir} ]; then
    rm -f %{_bindir}
    mkdir -p %{_bindir}
fi
install -D -m755 %{SOURCE24} %{buildroot}%{_bindir}/cputype

install -m644 -t %{buildroot}/%{_mandir}/man8 %{SOURCE25}

# If building for openSUSE, move all the binaries installed via
# the IBM-provided Makefile from /sbin to /usr/sbin/ to
# align with the openSUSE "usrmerge" project
%if 0%{?usrmerged}
mv -vi %{buildroot}/sbin/* %{buildroot}%{_mysbindir}/
%endif

### Obsolete scripts and man pages to be removed once changes in other tools are made
install -m755 -t %{buildroot}%{_mysbindir}/ %{SOURCE88} %{SOURCE91} %{SOURCE92} %{SOURCE93}
install %{SOURCE89} %{buildroot}%{_mysbindir}/dasd_configure
install %{SOURCE90} %{buildroot}%{_mysbindir}/iucv_configure
install -m644 -t %{buildroot}/%{_mandir}/man8 %{SOURCE94} %{SOURCE95} %{SOURCE96} %{SOURCE97} %{SOURCE98} %{SOURCE99}
###

### lsmem/chmem have been added to util-linux
rm -fv %{buildroot}%{_mandir}/man8/lsmem.8*
rm -fv %{buildroot}%{_mandir}/man8/chmem.8*
rm -fv %{buildroot}%{_mysbindir}/lsmem
rm -fv %{buildroot}%{_mysbindir}/chmem

find . ! -type d |
    sed 's/^.//;\-/man/-s/^.*$/%doc &.gz/' > %{_builddir}/%{name}-filelist
grep -v -E 'osasnmp|etc/ziplenv|\.conf$|ekmfweb.so|ekmfweb.h|kmipclient|kmip/profiles/.*profile$|chreipl-fcp-mpath' %{_builddir}/%{name}-filelist >%{_builddir}/%{name}.list
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
%{_mysbindir}/osasnmpd -f -P %{_localstatedir}/run/osasnmpd.real.pid \$OSASNMPD_PARAMETERS "\$@"
EOT
chmod 755 osasnmpd

export BRP_PESIGN_FILES='/lib/s390-tools/stage3.bin'

%verifyscript
%verify_permissions -e %{_localstatedir}/log/ts-shell/

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
# Avoid restoring outdated stuff in posttrans
for _f in %{?modprobe_d_files}; do
    [ ! -f "/etc/modprobe.d/${_f}.rpmsave" ] || \
        mv -f "/etc/modprobe.d/${_f}.rpmsave" "/etc/modprobe.d/${_f}.rpmsave.old" || :
done

%post
read INITPGM < /proc/1/comm
if [ "${INITPGM}" = "systemd" ]; then
  echo "Running systemctl daemon-reload."
  systemctl daemon-reload
fi

%set_permissions %{_localstatedir}/log/ts-shell/

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

%post -n libekmfweb1
ldconfig

%post -n libkmipclient1
ldconfig

%post chreipl-fcp-mpath
%udev_rules_update

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

%postun -n libekmfweb1
ldconfig

%postun -n libkmipclient1
ldconfig

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
# Migration of modprobe.conf files to _modprobedir
for _f in %{?modprobe_d_files}; do
    [ ! -f "/etc/modprobe.d/${_f}.rpmsave" ] || \
        mv -fv "/etc/modprobe.d/${_f}.rpmsave" "/etc/modprobe.d/${_f}" || :
done
%{?regenerate_initrd_posttrans}

%preun -n osasnmpd
%{stop_on_removal osasnmpd}

%files -f %{_builddir}/%{name}.list

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
%dir %attr(0770,root,zkeyadm) %{_sysconfdir}/zkey/kmip
%dir %attr(0770,root,zkeyadm) %{_sysconfdir}/zkey/kmip/profiles
%dir %attr(0770,root,zkeyadm) %{_sysconfdir}/zkey/repository
%config %{_sysconfdir}/zkey/kmip/profiles/*
%config(noreplace) %{_sysconfdir}/ziplenv
%dir %{_modprobedir}
%{_modprobedir}/90-s390-tools.conf
%config %{_sysconfdir}/cpuplugd.conf
%config %{_sysconfdir}/zkey/kms-plugins.conf
%config(noreplace) /boot/zipl/active_devices.txt
%dir %attr(2770,root,ts-shell) %{_localstatedir}/log/ts-shell
%dir %{_sysconfdir}/cmsfs-fuse
%config %attr(0640,root,root) %{_sysconfdir}/cmsfs-fuse/filetypes.conf
%dir %{_prefix}/lib/mdevctl
%dir %{_prefix}/lib/mdevctl/scripts.d
%dir %{_prefix}/lib/mdevctl/scripts.d/callouts
%dir %{_prefix}/lib/s390-tools
%dir %{_prefix}/lib/s390-tools/zfcpdump
%dir %{_prefix}/lib/udev/rules.d
%dir %{_prefix}/lib/systemd/scripts
%dir %{_datadir}/s390-tools
%dir %{_datadir}/s390-tools/netboot
%dir %{_datadir}/s390-tools/genprotimg
%dir %{_prefix}/lib/dracut/modules.d/95zdev
%dir %{_prefix}/lib/dracut/modules.d/99ngdump
%dir /boot/zipl
%dir %{_libdir}/zkey
%{_libdir}/zkey/zkey-ekmfweb.so
%dir /lib/s390-tools/
/lib/s390-tools/zipl.conf
%{_prefix}/lib/modules-load.d/pkey.conf
%exclude %{_prefix}/lib/udev/rules.d/57-osasnmpd.rules
%exclude %{_bindir}/zdsfs
%exclude %{_bindir}/hmcdrvfs
%exclude %{_sbindir}/lshmc
%exclude %{_mandir}/man1/zdsfs.1.gz
%exclude %{_mandir}/man1/hmcdrvfs.1.gz
%exclude %{_mandir}/man8/lshmc.8.gz

%files -n osasnmpd -f %{_builddir}/%{name}.osasnmp
%{_libexecdir}/net-snmp/agents/osasnmpd

%files zdsfs
%doc CAUTION
%{_bindir}/zdsfs
%{_mandir}/man1/zdsfs.1%{?ext_man}

%files hmcdrvfs
%{_bindir}/hmcdrvfs
%{_sbindir}/lshmc
%{_mandir}/man1/hmcdrvfs.1%{?ext_man}
%{_mandir}/man8/lshmc.8%{?ext_man}

%files -n libekmfweb1
%{_libdir}/libekmfweb.so.*

%files -n libekmfweb1-devel
%{_libdir}/libekmfweb.so
%dir %attr(755,root,root) %{_includedir}/ekmfweb
%attr(644,root,root) %{_includedir}/ekmfweb/ekmfweb.h

%files -n libkmipclient1
%{_libdir}/libkmipclient.so.*

%files -n libkmipclient1-devel
%{_libdir}/libkmipclient.so
%dir %attr(755,root,root) %{_includedir}/kmipclient
%attr(644,root,root) %{_includedir}/kmipclient/kmipclient.h

%files chreipl-fcp-mpath
%doc chreipl-fcp-mpath/README.md
## Requires build+install with ENABLE_DOC=1
#doc chreipl-fcp-mpath/README.html
%dir %{_prefix}/lib/chreipl-fcp-mpath/
%{_prefix}/lib/chreipl-fcp-mpath/*
%{_prefix}/lib/dracut/dracut.conf.d/70-chreipl-fcp-mpath.conf
%{_prefix}/lib/udev/chreipl-fcp-mpath-is-ipl-tgt
%{_prefix}/lib/udev/chreipl-fcp-mpath-is-ipl-vol
%{_prefix}/lib/udev/chreipl-fcp-mpath-is-reipl-zfcp
%{_prefix}/lib/udev/chreipl-fcp-mpath-record-volume-identifier
%{_prefix}/lib/udev/chreipl-fcp-mpath-try-change-ipl-path
%{_udevrulesdir}/70-chreipl-fcp-mpath.rules
%{_mandir}/man7/chreipl-fcp-mpath.7%{?ext_man}

%changelog
