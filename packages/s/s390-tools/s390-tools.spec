#
# spec file for package s390-tools
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
# needssslcertforbuild


%define rbrelease $(echo %{release} | sed 's/\.[0-9][0-9]*$//' )

%if ! %{defined _fillupdir}
  %define _fillupdir %{_localstatedir}/adm/fillup-templates
%endif

Name:           s390-tools
Version:        2.41.0
Release:        0
Summary:        S/390 tools like zipl and dasdfmt for s390x (plus selected tools for x86_64)
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
#
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
Source25:       cputype.8
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

### SUSE programs, scripts and man pages to be removed once changes in other tools are made
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
Source200:      vendor.tar.zst
###

###
# IBM patches
Patch100:       s390-tools-hyptop-opts-Replace-sort_field-option-with-sort.patch
Patch101:       s390-tools-hyptop-opts-Fix-long-command-line-option-abbreviations.patch
###
# SUSE patches
Patch900:       s390-tools-combined.patch
Patch901:       s390-tools-dasdfmt-reworked.patch
###
Patch905:       s390-tools-Remove-phmac_s390.patch
###
Patch910:       s390-tools-ALP-zdev-live.patch
###

BuildRequires:  curl-devel
BuildRequires:  dracut
BuildRequires:  fuse3-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gettext-tools
BuildRequires:  glib2-devel
BuildRequires:  glibc-devel-static
BuildRequires:  libcryptsetup-devel >= 2.8.2
BuildRequires:  libjson-c-devel
BuildRequires:  libnl3-devel
BuildRequires:  libxml2-devel
BuildRequires:  mdevctl
BuildRequires:  ncurses-devel
BuildRequires:  net-snmp-devel
BuildRequires:  openssl-devel >= 1.1.1l
BuildRequires:  pesign-obs-integration
BuildRequires:  systemd-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  sysuser-tools
BuildRequires:  tcpd-devel
BuildRequires:  zlib-devel-static
%{?sysusers_requires}
### s390x
%ifarch s390x
BuildRequires:  kernel-zfcpdump
BuildRequires:  perl-Bootloader >= 0.4.15
BuildRequires:  qclib-devel-static
%endif
### Cargo
BuildRequires:  rust
BuildRequires:  cargo
BuildRequires:  cargo-packaging
BuildRequires:  clang-devel
BuildRequires:  llvm-devel
BuildRequires:  openssl
###
# Don't build with pie to avoid problems with zipl
#!BuildIgnore:  gcc-PIE
Requires:       coreutils
Requires:       procps
Requires:       util-linux
%ifarch s390x
BuildRequires:  libica-devel-static
Requires:       gawk
Requires:       perl-base
Requires:       rsync
Requires:       s390-tools-genprotimg-data
Requires:       tar
Provides:       group(cpacfstats)
Provides:       group(ts-shell)
Provides:       group(zkeyadm)
%endif
Requires(post): %fillup_prereq
Requires(post): permissions
Requires(pre):  shadow
Recommends:     blktrace
Provides:       s390utils:/sbin/dasdfmt
%ifarch x86_64
Recommends:     s390-tools-genprotimg-data
%endif
###
ExclusiveArch:  s390x x86_64

%description
This package contains the tools (s390x, x86_64) needed to use Linux on IBM z Systems
and exploit many of the various capabilities of the hardware or z/VM. For example:

 - s390x
dasdfmt  - low-level format tool for ECKD DASD
fdasd    - partitions ECKD DASDs with z/OS compatible disk layout
zipl     - boot loader and dump DASD initializer
zgetdump - tool to get linux system dumps from DASD

 - x86_64
pvimg      - create a protected virtualization image (genprotimg)
pvattest   - create, perform, and verify protected virtualization attestation measurements
pvsecret   - manage secrets for IBM Secure Execution guests.

Note: There is an auxiliary data package - s390-tools-genprotimg-data.

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
BuildArch:      noarch
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

%package genprotimg-data
Summary:        Auxiliary data used by genprotimg
License:        MIT
Group:          System/Boot
BuildArch:      noarch
Requires(pre):  filesystem

%description genprotimg-data
The pvimg (genprotimg) allows preparing and analyzing boot images
in the realm of IBM Secure Execution on a trusted environment,
such as the laptop of an admin by limiting the build targets
depending on the defined or detected host architecture.
This package provides auxiliary data used by pvimg(genprotimg).

### *** s390x ************************************************************************* ###
%ifarch s390x

%prep
%autosetup -p1 -a200

cp -vi %{SOURCE22} CAUTION

%build

# The "DISTRELEASE=%%{release}" needs to be on both the make and make install
# commands, since make install runs sed commands against various scripts to
# modify the "-v" output appropriately.

export OPT_FLAGS="$(echo "%{optflags}" | sed 's/-flto=auto//g')"
export KERNELIMAGE_MAKEFLAGS="%%{?_smp_mflags}"

%make_build \
     ARCH=s390x \
     ZFCPDUMP_DIR=%{_prefix}/lib/s390-tools/zfcpdump \
     DISTRELEASE=%{rbrelease} \
     UDEVRUNDIR=/run/udev \
     HAVE_CARGO=1 \
     HAVE_DRACUT=1 \
     HAVE_LIBNL3=1
###     all
gcc -static -o read_values ${OPT_FLAGS} %{SOURCE86} -lqc

# Generate sysusers configuration and pre-install scriptlet
cat > s390-tools-sysusers.conf <<EOF
# Type Name ID GID Home Shell
g ts-shell - - -
g zkeyadm - - -
g cpacfstats - - -
EOF

# This macro generates the %%pre scriptlet automatically
%sysusers_generate_pre s390-tools-sysusers.conf s390-tools s390-tools.conf

%install
mkdir -p %{buildroot}/boot/zipl
mkdir -p %{buildroot}%{_sysconfdir}/zkey/repository

%make_install \
     ARCH=s390x \
     ZFCPDUMP_DIR=%{_prefix}/lib/s390-tools/zfcpdump \
     DISTRELEASE=%{rbrelease} \
     SYSTEMDSYSTEMUNITDIR=%{_unitdir} \
     UDEVRUNDIR=/run/udev \
     HAVE_CARGO=1 \
     HAVE_DRACUT=1 \
     HAVE_LIBNL3=1

# Move sysconfig files to the fillup-templates directory
mkdir -p %{buildroot}%{_fillupdir}
pushd %{buildroot}%{_sysconfdir}/sysconfig/
for sysconffile in *; do
    mv -vi $sysconffile %{buildroot}%{_fillupdir}/sysconfig.$sysconffile
done
popd

install -D -m 0644 s390-tools-sysusers.conf %{buildroot}%{_sysusersdir}/s390-tools.conf

# Install utilities and man pages
install -m 755 read_values %{buildroot}/%{_bindir}/
install -m 644 -t %{buildroot}/%{_mandir}/man8 %{SOURCE87}

# Standardized zfcpdump kernel image path (UsrMerge baseline)
install -D -m600 %{_prefix}/lib/modules/*-zfcpdump/image %{buildroot}%{_prefix}/lib/s390-tools/zfcpdump/zfcpdump-image

# System configs and udev rules
install -D -m 644 etc/cpuplugd.conf %{buildroot}%{_sysconfdir}/cpuplugd.conf
install -d -m 755 %{buildroot}%{_prefix}/lib/udev/rules.d
install -m 644 etc/udev/rules.d/*.rules %{buildroot}%{_prefix}/lib/udev/rules.d/
mv iucvterm/doc/ts-shell/iucvconn_on_login %{buildroot}%{_bindir}/iucvconn_on_login

# Install systemd services and scripts
install -D -m 644 %{SOURCE26} %{buildroot}/%{_unitdir}/cio_ignore.service
install -D -m 755 %{SOURCE27} %{buildroot}%{_prefix}/lib/systemd/scripts/setup_cio_ignore.sh
install -D -m 755 %{SOURCE31} %{buildroot}%{_prefix}/lib/systemd/scripts/detach_disks.sh
install -D -m 644 %{SOURCE35} %{buildroot}/%{_unitdir}/virtsetup.service
install -D -m 755 %{SOURCE36} %{buildroot}%{_prefix}/lib/systemd/scripts/virtsetup.sh
install -D -m 644 %{SOURCE37} %{buildroot}/%{_unitdir}/appldata.service
install -D -m 644 %{SOURCE38} %{buildroot}/%{_unitdir}/hsnc.service
install -D -m 644 %{SOURCE39} %{buildroot}/%{_unitdir}/vmlogrdr.service
install -D -m 644 %{SOURCE40} %{buildroot}/%{_unitdir}/xpram.service
install -D -m 644 %{SOURCE41} %{buildroot}%{_prefix}/lib/modules-load.d/pkey.conf

# Legacy source definitions mapped to modern unified files
cp %{SOURCE18} zpxe.rexx
cp %{SOURCE2} zipl.conf.sample
cp %{SOURCE23} README.SUSE

cd %{buildroot}
install -D -m 755 %{SOURCE3} %{buildroot}%{_prefix}/lib/systemd/scripts/hsnc
install -D -m 644 %{SOURCE4} %{buildroot}%{_fillupdir}/sysconfig.hsnc
install -D -m 755 %{SOURCE5} %{buildroot}%{_prefix}/lib/systemd/scripts/xpram
install -D -m 644 %{SOURCE6} %{buildroot}%{_fillupdir}/sysconfig.xpram
install -D -m 755 %{SOURCE7} %{buildroot}%{_prefix}/lib/systemd/scripts/appldata
install -D -m 644 %{SOURCE8} %{buildroot}%{_fillupdir}/sysconfig.appldata
install -D -m 755 %{SOURCE10} %{buildroot}%{_sbindir}/dasdro
install -D -m 755 %{SOURCE11} %{buildroot}%{_sbindir}/dasd_reload
install -D -m 755 %{SOURCE12} %{buildroot}%{_sbindir}/mkdump
install -D -m 644 %{SOURCE13} %{buildroot}%{_fillupdir}/sysconfig.osasnmpd
install -D -m 755 %{SOURCE14} %{buildroot}%{_sbindir}/zfcp_san_disc
install -D -m 644 %{SOURCE15} %{buildroot}/%{_mandir}/man8
install -D -m 644 %{SOURCE19} %{buildroot}%{_prefix}/lib/udev/rules.d/52-xpram.rules
install -D -m 644 %{SOURCE20} %{buildroot}%{_prefix}/lib/udev/rules.d/52-hw_random.rules
install -D -m 644 %{SOURCE21} %{buildroot}%{_prefix}/lib/udev/rules.d/59-graf.rules
install -D -m 644 %{SOURCE28} %{buildroot}%{_prefix}/lib/udev/rules.d/59-prng.rules
install -D -m 644 %{SOURCE29} %{buildroot}%{_prefix}/lib/udev/rules.d/59-zfcp-compat.rules
install -D -m 644 %{SOURCE30} %{buildroot}%{_modprobedir}/90-s390-tools.conf
install -D -m 755 %{SOURCE32} %{buildroot}%{_sbindir}/killcdl
install -D -m 755 %{SOURCE33} %{buildroot}%{_sbindir}/lgr_check
install -D -m 644 %{SOURCE34} %{buildroot}%{_fillupdir}/sysconfig.virtsetup

# Create rc symlinks in _sbindir
for svc in appldata hsnc vmlogrdr xpram cio_ignore cpacfstatsd cpi cpuplugd dumpconf mon_fsstatd mon_procd virtsetup opticsmon; do
    ln -s service %{buildroot}%{_sbindir}/rc${svc}
done

install -D -m 755 %{SOURCE24} %{buildroot}%{_bindir}/cputype
install -m 644 -t %{buildroot}/%{_mandir}/man8 %{SOURCE25}

mkdir -p %{buildroot}%{_tmpfilesdir}
cat > %{buildroot}%{_tmpfilesdir}/%{name}.conf <<EOF
d /var/log/ts-shell 2770 root ts-shell - -
EOF

### Obsolete scripts and man pages to be removed once changes in other tools are made
install -m 755 -t %{buildroot}%{_sbindir}/ %{SOURCE88} %{SOURCE91} %{SOURCE92} %{SOURCE93}
install %{SOURCE89} %{buildroot}%{_sbindir}/dasd_configure
install %{SOURCE90} %{buildroot}%{_sbindir}/iucv_configure
install -m 644 -t %{buildroot}/%{_mandir}/man8 %{SOURCE94} %{SOURCE95} %{SOURCE96} %{SOURCE97} %{SOURCE98} %{SOURCE99}

### lsmem/chmem have been added to util-linux
rm -fv %{buildroot}%{_mandir}/man8/lsmem.8* %{buildroot}%{_mandir}/man8/chmem.8*
rm -fv %{buildroot}%{_sbindir}/lsmem %{buildroot}%{_sbindir}/chmem

touch boot/zipl/active_devices.txt

mkdir -p %{buildroot}%{_libexecdir}/net-snmp/agents
cat <<EOT > %{buildroot}%{_libexecdir}/net-snmp/agents/osasnmpd
#!/bin/sh
PIDFILE=/run/osasnmpd.pid
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
chmod 755 %{buildroot}%{_libexecdir}/net-snmp/agents/osasnmpd

export BRP_PESIGN_FILES='/lib/s390-tools/stage3.bin'

%pre -f s390-tools.pre
# Consolidated service addition
%service_add_pre appldata.service cio_ignore.service cpacfstatsd.service cpi.service cpuplugd.service dumpconf.service hsnc.service mon_fsstatd.service mon_procd.service opticsmon.service virtsetup.service vmlogrdr.service xpram.service

%post
# Consolidated service addition
%service_add_post appldata.service cio_ignore.service cpacfstatsd.service cpi.service cpuplugd.service dumpconf.service hsnc.service mon_fsstatd.service mon_procd.service opticsmon.service virtsetup.service vmlogrdr.service xpram.service

# Apply tmpfiles setup for /var/log permissions
%tmpfiles_create %{_tmpfilesdir}/%{name}.conf

%{fillup_only -n appldata}
%{fillup_only -n cpi}
%{fillup_only -n dumpconf}
%{fillup_only -n hsnc}
%{fillup_only -n mon_fsstatd}
%{fillup_only -n mon_procd}
%{fillup_only -n mon_statd}
%{fillup_only -n opticsmon}
%{fillup_only -n virtsetup}
%{fillup_only -n xpram}

%{?regenerate_initrd_post}

%post -n osasnmpd
%{fillup_only -n osasnmpd}

%post -n libekmfweb1 -p /sbin/ldconfig
%post -n libkmipclient1 -p /sbin/ldconfig

%post chreipl-fcp-mpath
%udev_rules_update

%preun
%service_del_preun appldata.service cio_ignore.service cpacfstatsd.service cpi.service cpuplugd.service dumpconf.service hsnc.service mon_fsstatd.service mon_procd.service opticsmon.service virtsetup.service vmlogrdr.service xpram.service

%preun -n osasnmpd
%{stop_on_removal osasnmpd}

%postun
%service_del_postun appldata.service cio_ignore.service cpacfstatsd.service cpi.service cpuplugd.service dumpconf.service hsnc.service mon_fsstatd.service mon_procd.service opticsmon.service virtsetup.service vmlogrdr.service xpram.service

if [ ! -x /boot/zipl ]; then
	echo "Attention: After uninstalling this package, you will NOT be able to IPL from DASD anymore!"
fi

%{?regenerate_initrd_post}

%postun -n libekmfweb1 -p /sbin/ldconfig
%postun -n libkmipclient1 -p /sbin/ldconfig

%posttrans
%{?regenerate_initrd_posttrans}

%files
# --- Documentation & Licenses ---
%doc README.md README.SUSE iucvterm/doc/ts-shell zpxe.rexx zipl.conf.sample

# --- System Configuration (/etc) ---
%{_sysusersdir}/%{name}.conf
%{_tmpfilesdir}/%{name}.conf
%config(noreplace) %{_sysconfdir}/cpuplugd.conf
%config(noreplace) %{_sysconfdir}/ziplenv
%config(noreplace) /boot/zipl/active_devices.txt
%dir %{_sysconfdir}/cmsfs-fuse
%config(noreplace) %attr(0640,root,root) %{_sysconfdir}/cmsfs-fuse/filetypes.conf
%dir %{_sysconfdir}/iucvterm
%config(noreplace) %attr(0640,root,ts-shell) %{_sysconfdir}/iucvterm/*.conf
%dir %attr(0770,root,zkeyadm) %{_sysconfdir}/zkey
%dir %attr(0770,root,zkeyadm) %{_sysconfdir}/zkey/kmip
%dir %attr(0770,root,zkeyadm) %{_sysconfdir}/zkey/kmip/profiles
%dir %attr(0770,root,zkeyadm) %{_sysconfdir}/zkey/repository
%config(noreplace) %{_sysconfdir}/zkey/kmip/profiles/*
%config(noreplace) %{_sysconfdir}/zkey/kms-plugins.conf
%dir %{_sysconfdir}/mdevctl.d
%dir %{_sysconfdir}/mdevctl.d/scripts.d
%dir %{_sysconfdir}/mdevctl.d/scripts.d/callouts
%{_sysconfdir}/mdevctl.d/scripts.d/callouts/*
%config(noreplace) %attr(0755,root,root) %{_sysconfdir}/mdevctl.d/scripts.d/callouts/ap-check.sh

# --- Sysconfig / Fillup Templates ---
%{_fillupdir}/sysconfig.*
%exclude %{_fillupdir}/sysconfig.osasnmpd

# --- Binaries & Scripts ---
%{_bindir}/*
%{_sbindir}/*
/sbin/*

# --- System Libraries, Units, & Shared Data ---
%{_unitdir}/*
%dir %{_prefix}/lib/mdevctl
%dir %{_prefix}/lib/mdevctl/scripts.d
%dir %{_prefix}/lib/mdevctl/scripts.d/callouts
%{_prefix}/lib/mdevctl/scripts.d/callouts/*
%dir %{_prefix}/lib/s390-tools
%{_prefix}/lib/s390-tools/*
%dir %{_prefix}/lib/systemd/scripts
%{_prefix}/lib/systemd/scripts/*
%dir %{_datadir}/s390-tools
%{_datadir}/s390-tools/*
%dir %{_libdir}/zkey
%{_libdir}/zkey/*.so
/lib/s390-tools/*

# --- Boot & Dracut ---
%dir /boot/zipl
%dir %{_prefix}/lib/dracut/modules.d/95zdev
%{_prefix}/lib/dracut/modules.d/95zdev/*
%dir %{_prefix}/lib/dracut/modules.d/95zdev-kdump
%{_prefix}/lib/dracut/modules.d/95zdev-kdump/*
%dir %{_prefix}/lib/dracut/modules.d/96zdev-live
%{_prefix}/lib/dracut/modules.d/96zdev-live/*
%dir %{_prefix}/lib/dracut/modules.d/99ngdump
%{_prefix}/lib/dracut/modules.d/99ngdump/*
%{_prefix}/lib/dracut/dracut.conf.d/99-pkey.conf

# --- Kernel Modules & Udev ---
%dir %{_modprobedir}
%{_modprobedir}/90-s390-tools.conf
%{_prefix}/lib/modules-load.d/pkey.conf
%dir %{_prefix}/lib/udev/rules.d
%{_prefix}/lib/udev/rules.d/*

# --- Shell Completions ---
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/*
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/*

# --- Man Pages ---
%{_mandir}/man*/*

# --- Exclusions (Files packaged in subpackages) ---
%exclude %{_bindir}/zdsfs
%exclude %{_bindir}/hmcdrvfs
%exclude %{_sbindir}/lshmc
%exclude %{_sbindir}/osasnmpd
%exclude %{_mandir}/man1/zdsfs.1*
%exclude %{_mandir}/man1/hmcdrvfs.1*
%exclude %{_mandir}/man7/chreipl-fcp-mpath.7*
%exclude %{_mandir}/man8/lshmc.8*
%exclude %{_mandir}/man8/osasnmpd.8*
%exclude %{_prefix}/lib/udev/rules.d/57-osasnmpd.rules
%exclude /lib/s390-tools/stage3.bin
%exclude %{_datadir}/s390-tools/pvimg/stage3a.bin
%exclude %{_datadir}/s390-tools/pvimg/stage3b_reloc.bin
%exclude %{_prefix}/lib/udev/rules.d/70-chreipl-fcp-mpath.rules
%exclude /lib/s390-tools/chreipl_helper.device-mapper
%exclude /lib/s390-tools/chreipl_helper.md

%files -n osasnmpd
%{_sbindir}/osasnmpd
%{_libexecdir}/net-snmp/agents/osasnmpd
%{_mandir}/man8/osasnmpd.8%{?ext_man}
%{_prefix}/lib/udev/rules.d/57-osasnmpd.rules
%{_fillupdir}/sysconfig.osasnmpd

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
/lib/s390-tools/chreipl_helper.device-mapper
/lib/s390-tools/chreipl_helper.md
%{_prefix}/lib/udev/chreipl-fcp-mpath-is-ipl-tgt
%{_prefix}/lib/udev/chreipl-fcp-mpath-is-ipl-vol
%{_prefix}/lib/udev/chreipl-fcp-mpath-is-reipl-zfcp
%{_prefix}/lib/udev/chreipl-fcp-mpath-record-volume-identifier
%{_prefix}/lib/udev/chreipl-fcp-mpath-try-change-ipl-path
%{_udevrulesdir}/70-chreipl-fcp-mpath.rules
%{_mandir}/man7/chreipl-fcp-mpath.7%{?ext_man}

### genprotimg
%files genprotimg-data
/lib/s390-tools/stage3.bin
%dir %{_datadir}/s390-tools/pvimg
%dir %{_datadir}/s390-tools/netboot
%{_datadir}/s390-tools/pvimg/stage3a.bin
%{_datadir}/s390-tools/pvimg/stage3b_reloc.bin

### _endif

### *** !s390x (x86_64) *************************************************************** ###
%else

%prep
%autosetup -p1 -a200

%build
export OPT_FLAGS="%{optflags}"
export KERNELIMAGE_MAKEFLAGS="%{?_smp_mflags}"

%make_build \
     DISTRELEASE=%{rbrelease} \
     UDEVRUNDIR=/run/udev \
     HAVE_CARGO=1 \
     HAVE_DRACUT=1

%install
%make_install \
     DISTRELEASE=%{rbrelease} \
     SYSTEMDSYSTEMUNITDIR=%{_unitdir} \
     UDEVRUNDIR=/run/udev \
     HAVE_CARGO=1 \
     HAVE_DRACUT=1

%files
# --- Binaries ---
%{_bindir}/*

# --- Shared Data ---
%dir %{_datadir}/s390-tools
%{_datadir}/s390-tools/pvimg/
%{_datadir}/s390-tools/netboot/

# --- Shell Completions ---
# Using wildcards prevents the need to manually list every new completion file
%{_datadir}/bash-completion/completions/*
%{_datadir}/zsh/site-functions/*

# --- Man Pages ---
%{_mandir}/man1/*

%endif

%changelog
