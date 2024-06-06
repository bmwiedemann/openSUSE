#
# spec file for package xen
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
# needssslcertforbuild


#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif

# Tumbleweed now defines _libexecdir as /usr/libexec
# Keep it at the original location (/usr/lib) for backward compatibility
%define _libexecdir /usr/lib

Name:           xen
ExclusiveArch:  %ix86 x86_64 aarch64
%define xen_build_dir xen-4.18.2-testing
#
%define with_gdbsx 0
%define with_dom0_support 0
%ifarch x86_64
%bcond_without xen_debug
%bcond_without xen_stubdom
%else
%bcond_with    xen_debug
%bcond_with    xen_stubdom
%endif
#
%define qemu_arch i386
%ifarch x86_64
%define with_gdbsx 1
%define with_dom0_support 1
%endif
#
%ifarch %arm aarch64
%define with_dom0_support 1
%define qemu_arch aarch64
%endif
#
%define xen_install_suffix %{nil}
%ifarch x86_64
%define xen_install_suffix .gz
%endif
# EFI requires gcc 4.6 or newer
# gcc46 is available in 12.1 or sles11sp2
# gcc47 is available in sles11sp3
# gcc48 is available in sles11sp4
# 12.2+ have gcc 4.7 as default compiler
%define with_gcc47 0
%define with_gcc48 0
%define _fwdefdir /etc/sysconfig/SuSEfirewall2.d/services
%systemd_requires
BuildRequires:  pkgconfig(libsystemd)
%define with_systemd_modules_load %{_prefix}/lib/modules-load.d
PreReq:         %fillup_prereq
%ifarch %arm aarch64
%if 0%{?suse_version} > 1320 || ( 0%{?suse_version} == 1315 && 0%{?sle_version} > 120200 )
BuildRequires:  libfdt-devel
%else
BuildRequires:  libfdt1-devel
%endif
%endif
BuildRequires:  bison
BuildRequires:  fdupes
%if 0%{?suse_version} > 1315
BuildRequires:  figlet
%endif
BuildRequires:  flex
BuildRequires:  glib2-devel
BuildRequires:  libaio-devel
BuildRequires:  libbz2-devel
BuildRequires:  libnl3-devel
BuildRequires:  libpixman-1-0-devel
BuildRequires:  libuuid-devel
BuildRequires:  libxml2-devel
BuildRequires:  libyajl-devel
%if %{with xen_stubdom}
%if 0%{?suse_version} < 1230
BuildRequires:  texinfo
%else
BuildRequires:  makeinfo
%endif
%endif
BuildRequires:  acpica
BuildRequires:  ncurses-devel
BuildRequires:  openssl-devel
BuildRequires:  python3-devel
BuildRequires:  xz-devel
BuildRequires:  pkgconfig(systemd)
%ifarch x86_64
BuildRequires:  gcc-32bit
BuildRequires:  gcc-c++
%if %{?with_gcc47}0
BuildRequires:  gcc47
%endif
%if %{?with_gcc48}0
BuildRequires:  gcc48
%endif
BuildRequires:  glibc-32bit
BuildRequires:  glibc-devel-32bit
BuildRequires:  makeinfo
%endif
%ifarch x86_64
BuildRequires:  pesign-obs-integration
%endif
Provides:       installhint(reboot-needed)

Version:        4.18.2_05
Release:        0
Summary:        Xen Virtualization: Hypervisor (aka VMM aka Microkernel)
License:        GPL-2.0-only
Group:          System/Kernel
Source0:        xen-4.18.2-testing-src.tar.bz2
Source1:        stubdom.tar.bz2
Source2:        mini-os.tar.bz2
Source9:        xen.changes
Source10:       README.SUSE
Source11:       boot.xen
Source12:       boot.local.xenU
Source13:       xen-supportconfig
Source14:       logrotate.conf
Source21:       block-npiv-common.sh
Source22:       block-npiv
Source23:       block-npiv-vport
Source24:       block-dmmd
# Xen API remote authentication sources
Source30:       etc_pam.d_xen-api
Source31:       xenapiusers
# Init script and sysconf file for pciback
Source34:       init.pciback
Source35:       sysconfig.pciback
Source36:       xen2libvirt.py
# Systemd service files
Source41:       xencommons.service
Source42:       xen-dom0-modules.service
Source10172:    xendomains-wait-disks.sh
Source10173:    xendomains-wait-disks.LICENSE
Source10174:    xendomains-wait-disks.README.md
Source10183:    xen_maskcalc.py
# For xen-libs
Source99:       baselibs.conf
# Upstream patches
Patch1:         6617d62c-x86-hvm-Misra-Rule-19-1-regression.patch
Patch2:         6627a4ee-vRTC-UIP-set-for-longer-than-expected.patch
Patch3:         6627a5fc-x86-MTRR-inverted-WC-check.patch
Patch4:         662a6a4c-x86-spec-reporting-of-BHB-clearing.patch
Patch5:         662a6a8d-x86-spec-adjust-logic-to-elide-LFENCE.patch
Patch6:         663090fd-x86-gen-cpuid-syntax.patch
Patch7:         663a383c-libxs-open-xenbus-fds-as-O_CLOEXEC.patch
Patch8:         663a4f3e-x86-cpu-policy-migration-IceLake-to-CascadeLake.patch
Patch9:         663d05b5-x86-ucode-distinguish-up-to-date.patch
Patch10:        663eaa27-libxl-XenStore-error-handling-in-device-creation.patch
# EMBARGOED security fixes
# libxc
Patch301:       libxc-bitmap-long.patch
Patch302:       libxc-sr-xl-migration-debug.patch
Patch303:       libxc-sr-readv_exact.patch
Patch304:       libxc-sr-save-show_transfer_rate.patch
Patch305:       libxc-sr-save-mfns.patch
Patch306:       libxc-sr-save-types.patch
Patch307:       libxc-sr-save-errors.patch
Patch308:       libxc-sr-save-iov.patch
Patch309:       libxc-sr-save-rec_pfns.patch
Patch310:       libxc-sr-save-guest_data.patch
Patch311:       libxc-sr-save-local_pages.patch
Patch312:       libxc-sr-restore-pfns.patch
Patch313:       libxc-sr-restore-types.patch
Patch314:       libxc-sr-restore-mfns.patch
Patch315:       libxc-sr-restore-map_errs.patch
Patch316:       libxc-sr-restore-populate_pfns-pfns.patch
Patch317:       libxc-sr-restore-populate_pfns-mfns.patch
Patch318:       libxc-sr-restore-read_record.patch
Patch319:       libxc-sr-restore-handle_buffered_page_data.patch
Patch320:       libxc-sr-restore-handle_incoming_page_data.patch
Patch321:       libxc-sr-LIBXL_HAVE_DOMAIN_SUSPEND_PROPS.patch
Patch322:       libxc-sr-precopy_policy.patch
Patch323:       libxc-sr-max_iters.patch
Patch324:       libxc-sr-min_remaining.patch
Patch325:       libxc-sr-abort_if_busy.patch
Patch326:       libxc-sr-xg_sr_bitmap.patch
Patch327:       libxc-sr-xg_sr_bitmap-populated_pfns.patch
Patch328:       libxc-sr-restore-hvm-legacy-superpage.patch
Patch329:       libxc-sr-track-migration-time.patch
Patch330:       libxc-sr-number-of-iterations.patch
# Our platform specific patches
Patch400:       xen-destdir.patch
Patch401:       vif-bridge-no-iptables.patch
Patch402:       vif-bridge-tap-fix.patch
Patch403:       xl-conf-default-bridge.patch
Patch404:       xl-conf-disable-autoballoon.patch
Patch405:       xen-arch-kconfig-nr_cpus.patch
Patch406:       suse-xendomains-service.patch
Patch407:       replace-obsolete-network-configuration-commands-in-s.patch
Patch408:       ignore-ip-command-script-errors.patch
# Needs to go upstream
Patch420:       suspend_evtchn_lock.patch
Patch421:       vif-route.patch
Patch422:       gcc14-fixes.patch
# Other bug fixes or features
Patch450:       xen.sysconfig-fillup.patch
Patch451:       xenconsole-no-multiple-connections.patch
Patch452:       hibernate.patch
Patch453:       stdvga-cache.patch
Patch454:       xl-save-pc.patch
Patch455:       pygrub-boot-legacy-sles.patch
Patch456:       pygrub-handle-one-line-menu-entries.patch
Patch461:       libxl.max_event_channels.patch
Patch463:       libxl.add-option-to-disable-disk-cache-flushes-in-qdisk.patch
Patch464:       xen.libxl.dmmd.patch
Patch465:       xenstore-run-in-studomain.patch
Patch466:       libxl.helper_done-crash.patch
Patch467:       libxl.LIBXL_HOTPLUG_TIMEOUT.patch
# python3 conversion patches
Patch500:       build-python3-conversion.patch
Patch501:       migration-python3-conversion.patch
Patch502:       bin-python3-conversion.patch
# Hypervisor and PV driver Patches
Patch600:       xen.bug1026236.suse_vtsc_tolerance.patch
Patch601:       x86-ioapic-ack-default.patch
Patch602:       xenwatchdogd-restart.patch
Patch621:       xen.build-compare.doc_html.patch
# Build patches
URL:            http://www.cl.cam.ac.uk/Research/SRG/netos/xen/
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%define pyver %(python3 -c "import sys; print(sys.version.rpartition('.')[0])")

%description
Xen is a virtual machine monitor for x86 that supports execution of
multiple guest operating systems with unprecedented levels of
performance and resource isolation.

This package contains the Xen Hypervisor. (tm)

[Hypervisor is a trademark of IBM]

%package libs
Summary:        Xen Virtualization: Libraries
License:        GPL-2.0-only
Group:          System/Kernel

%description libs
Xen is a virtual machine monitor for x86 that supports execution of
multiple guest operating systems with unprecedented levels of
performance and resource isolation.

This package contains the libraries used to interact with the Xen
virtual machine monitor.

In addition to this package you need to install xen and xen-tools
to use Xen.


Authors:
--------
    Ian Pratt <ian.pratt@cl.cam.ac.uk>


%if %{?with_dom0_support}0

%package tools
Summary:        Xen Virtualization: Control tools for domain 0
License:        GPL-2.0-only
Group:          System/Kernel
%if 0%{?suse_version} > 1500
BuildRequires:  pam-devel
%endif
%ifarch x86_64
%if 0%{?suse_version} >= 1315
Requires:       grub2-x86_64-xen
%endif
Recommends:     qemu-ovmf-x86_64
Requires:       qemu-x86
%endif
%ifarch %arm aarch64
Requires:       qemu-arm
%endif
Requires:       %{name} = %{version}-%{release}
Requires:       %{name}-libs = %{version}-%{release}
Recommends:     multipath-tools
Requires:       python3
Requires:       python3-curses
%ifarch %{ix86} x86_64
Requires:       qemu-seabios
%endif
# subpackage existed in 10.3
Provides:       xen-tools-ioemu = %{version}
Obsoletes:      xen-tools-ioemu < %{version}
Conflicts:      libvirt < 1.0.5

%description tools
Xen is a virtual machine monitor for x86 that supports execution of
multiple guest operating systems with unprecedented levels of
performance and resource isolation.

This package contains the control tools that allow you to start, stop,
migrate, and manage virtual machines.

In addition to this package you need to install xen and xen-libs
to use Xen.


Authors:
--------
    Ian Pratt <ian.pratt@cl.cam.ac.uk>


%ifarch x86_64
%package tools-xendomains-wait-disk
Summary:        Adds a new xendomains-wait-disks.service
License:        GPL-3.0-or-later
Group:          System/Kernel
Requires:       %{name}-tools = %{version}-%{release}
Requires:       coreutils
Requires:       sed
Requires:       vim
BuildArch:      noarch

%description tools-xendomains-wait-disk
This package adds a new service named xendomains-wait-disks.service,
that simply calls xendomains-wait-disks. xendomains-wait-disks script
loops checking for the presence of every disk used by domU that
xendomains.service will try to launch. The script returns when
all disks become available or xendomains-wait-disks.service expires.

xendomains-wait-disks.service has the same dependencies as
xendomains.service, but it adds itself as a Wanted service for xendomains.
If xendomains-wait-disks.service fails, xendomains.service is launched anyway.

https://github.com/luizluca/xen-tools-xendomains-wait-disk
%endif

%endif

%package tools-domU
Summary:        Xen Virtualization: Control tools for domain U
License:        GPL-2.0-only
Group:          System/Kernel
Conflicts:      %{name}-tools
Requires:       %{name}-libs = %{version}-%{release}

%description tools-domU
Xen is a virtual machine monitor for x86 that supports execution of
multiple guest operating systems with unprecedented levels of
performance and resource isolation.

This package contains tools that allow unprivileged domains to query
the virtualized environment.



Authors:
--------
    Ian Pratt <ian.pratt@cl.cam.ac.uk>

%package devel
Summary:        Xen Virtualization: Headers and libraries for development
License:        GPL-2.0-only
Group:          System/Kernel
Requires:       %{name}-libs = %{version}
Requires:       libuuid-devel

%description devel
Xen is a virtual machine monitor for x86 that supports execution of
multiple guest operating systems with unprecedented levels of
performance and resource isolation.

This package contains the libraries and header files needed to create
tools to control virtual machines.



Authors:
--------
    Ian Pratt <ian.pratt@cl.cam.ac.uk>

%if %{?with_dom0_support}0

%package doc-html
Summary:        Xen Virtualization: HTML documentation
License:        GPL-2.0-only
Group:          Documentation/HTML

%description doc-html
Xen is a virtual machine monitor for x86 that supports execution of
multiple guest operating systems with unprecedented levels of
performance and resource isolation.

xen-doc-html contains the online documentation in HTML format. Point
your browser at file:/usr/share/doc/packages/xen/html/



Authors:
--------
    Ian Pratt <ian.pratt@cl.cam.ac.uk>
%endif

%prep
%setup -q -n %xen_build_dir -a 1 -a 2
%autosetup -D -T -n %xen_build_dir -p1

%build
%define _lto_cflags %{nil}

# we control the version info of this package
# to gain control of filename of xen.gz
XEN_VERSION=%{version}
XEN_VERSION=${XEN_VERSION%%%%.*}
XEN_SUBVERSION=%{version}
XEN_SUBVERSION=${XEN_SUBVERSION#*.}
XEN_SUBVERSION=${XEN_SUBVERSION%%%%.*}
XEN_EXTRAVERSION="%version-%release"
XEN_EXTRAVERSION="${XEN_EXTRAVERSION#*.}"
XEN_EXTRAVERSION="${XEN_EXTRAVERSION#*.}"
# remove trailing B_CNT to reduce build-compare noise
XEN_EXTRAVERSION="${XEN_EXTRAVERSION%%.*}"
XEN_FULLVERSION="$XEN_VERSION.$XEN_SUBVERSION.$XEN_EXTRAVERSION"
XEN_BUILD_DATE="`date -u -d '1970-01-01'`"
XEN_BUILD_TIME="`date -u -d '1970-01-01' +%%T`"
SMBIOS_REL_DATE="`date -u -d '1970-01-01' +%%m/%%d/%%Y`"
RELDATE="`date -u -d '1970-01-01' '+%%d %%b %%Y'`"
if test -r %{S:9}
then
	XEN_BUILD_DATE="` date -u -d \"$(sed -n '/@/{s/ - .*$//p;q}' %{S:9})\" `"
	XEN_BUILD_TIME="` date -u -d \"$(sed -n '/@/{s/ - .*$//p;q}' %{S:9})\" +%%T`"
	SMBIOS_REL_DATE="` date -u -d \"$(sed -n '/@/{s/ - .*$//p;q}' %{S:9})\" +%%m/%%d/%%Y`"
	RELDATE="` date -u -d \"$(sed -n '/@/{s/ - .*$//p;q}' %{S:9})\" '+%%d %%b %%Y'`"
fi
cat > .our_xenversion <<_EOV_
export WGET=$(type -P false)
export FTP=$(type -P false)
export GIT=$(type -P false)
%ifarch aarch64
# GCC10+ enables outline-atomics option by default and breaks the build, so disable it
%if 0%{?suse_version} >= 1550
export CFLAGS="%{optflags} -mno-outline-atomics"
%endif
%endif
export EXTRA_CFLAGS_XEN_TOOLS="%{optflags}"
export EXTRA_CFLAGS_QEMU_TRADITIONAL="%{optflags}"
export SMBIOS_REL_DATE="$SMBIOS_REL_DATE"
export RELDATE="$RELDATE"
XEN_VERSION=$XEN_VERSION
XEN_SUBVERSION=$XEN_SUBVERSION
XEN_EXTRAVERSION=$XEN_EXTRAVERSION
XEN_FULLVERSION=$XEN_FULLVERSION
_EOV_
source ./.our_xenversion
sed -i~ "
s/XEN_VERSION[[:blank:]]*=.*/XEN_VERSION = $XEN_VERSION/
s/XEN_SUBVERSION[[:blank:]]*=.*/XEN_SUBVERSION = $XEN_SUBVERSION/
s/XEN_EXTRAVERSION[[:blank:]]*?=.*/XEN_EXTRAVERSION = .$XEN_EXTRAVERSION/
s/XEN_FULLVERSION[[:blank:]]*=.*/XEN_FULLVERSION = $XEN_FULLVERSION/
s/XEN_BUILD_DATE[[:blank:]]*?=.*/XEN_BUILD_DATE = $XEN_BUILD_DATE/
s/XEN_BUILD_TIME[[:blank:]]*?=.*/XEN_BUILD_TIME = $XEN_BUILD_TIME/
s/XEN_BUILD_HOST[[:blank:]]*?=.*/XEN_BUILD_HOST = buildhost/
s/XEN_DOMAIN[[:blank:]]*?=.*/XEN_DOMAIN = suse.de/
" xen/Makefile
if diff -u xen/Makefile~ xen/Makefile
then
	: no changes?
fi

configure_flags=
configure_flags="--with-system-qemu=%{_bindir}/qemu-system-%{qemu_arch}"
%if %{with xen_stubdom}
configure_flags="${configure_flags} --enable-stubdom"
%else
# change the/our default to daemon due to lack of stubdom
sed -i~ 's/ XENSTORETYPE=domain$/ XENSTORETYPE=daemon/' tools/hotplug/Linux/launch-xenstore.in
configure_flags="${configure_flags} --disable-stubdom"
%endif
export PYTHON="/usr/bin/python3"
configure_flags="${configure_flags} --disable-qemu-traditional"
./configure \
        --disable-xen \
        --disable-pvshim \
        --enable-tools \
        --enable-docs \
        --prefix=/usr \
        --exec_prefix=/usr \
        --bindir=%{_bindir} \
        --sbindir=%{_sbindir} \
        --libdir=%{_libdir} \
        --libexecdir=%{_libexecdir} \
        --with-libexec-leaf-dir=%{name} \
        --datadir=%{_datadir} \
        --mandir=%{_mandir} \
        --includedir=%{_includedir} \
        --docdir=%{_defaultdocdir}/xen \
	--with-initddir=%{_initddir} \
	--with-rundir=%{_rundir} \
	--enable-systemd \
	--with-systemd=%{_unitdir} \
	--with-systemd-modules-load=%{with_systemd_modules_load} \
	--with-system-ovmf=%{_datadir}/qemu/ovmf-x86_64-xen-4m.bin \
	--with-system-seabios=%{_datadir}/qemu/bios-256k.bin \
        ${configure_flags}
make -C tools/include/xen-foreign %{?_smp_mflags}
make %{?_smp_mflags}
#

%install
source ./.our_xenversion
# tools
make \
	DESTDIR=%{buildroot} \
	SYSCONFIG_DIR=%{_fillupdir} \
	PKG_INSTALLDIR=%{_libdir}/pkgconfig \
	%{?_smp_mflags} \
	install
find %{buildroot} -ls
for i in %{buildroot}/%{_fillupdir}/*
do
	mv -v $i ${i%%/*}/sysconfig.${i##*/}
done

#
udev_rulesdir=%{buildroot}/%{_udevrulesdir}
tools_domU_dir=%{buildroot}/%{_libexecdir}/%{name}-tools-domU
mkdir -p ${udev_rulesdir}
mkdir -p ${tools_domU_dir}
#
tee ${udev_rulesdir}/80-%{name}-tools-domU.rules <<'_EOR_'
# XenSource, Inc. Xen Platform Device
SUBSYSTEM=="pci", ATTR{modalias}=="pci:v00005853d00000001sv00005853sd00000001bcFFsc80i00", TAG+="systemd", ENV{SYSTEMD_WANTS}+="%{name}-vcpu-watch.service"
_EOR_
#
tee %{buildroot}/%{_unitdir}/%{name}-vcpu-watch.service <<'_EOS_'
[Unit]
Description=Listen to CPU online/offline events from dom0 toolstack

[Service]
Type=simple
ExecStart=%{_libexecdir}/%{name}-tools-domU/%{name}-vcpu-watch.sh
Restart=always
RestartSec=2
_EOS_
#
tee %{buildroot}/%{_libexecdir}/%{name}-tools-domU/%{name}-vcpu-watch.sh <<'_EOS_'
#!/bin/bash
unset LANG
unset ${!LC_*}
echo "$0 starting" >&2
xenstore-watch cpu | while read
do
  : xenstore event: ${REPLY}
  case "${REPLY}" in
    cpu)
      : just started
      ;;
    cpu/[0-9]/availability|cpu/[0-9][0-9]/availability)
      vcpu="${REPLY%%/*}"
      vcpu="${vcpu#*/}"
      sysfs="/sys/devices/system/cpu/cpu${vcpu}/online"
      if test -f "${sysfs}"
      then
        availability="`xenstore-read \"${REPLY}\"`"
        case "${availability}" in
          online|offline)
            if test "${availability}" = "online"
            then
              new_sysfs_state=1
            else
              new_sysfs_state=0
            fi
            read cur_sysfs_state rest < "${sysfs}"
            if test "${cur_sysfs_state}" = "${new_sysfs_state}"
            then
              : the vcpu "${vcpu}" already has state "${availability}" via "${sysfs}"
            else
              : setting vcpu "${vcpu}" to "${availability}" via "${sysfs}"
              echo "setting vcpu ${vcpu} to ${availability}" >&2
              echo "${new_sysfs_state}" > "${sysfs}"
            fi
          ;;
        esac
      fi
    ;;
    *)
      : unhandled
    ;;
  esac
done
exit 1
_EOS_
chmod 755 %{buildroot}/%{_libexecdir}/%{name}-tools-domU/%{name}-vcpu-watch.sh
#
tee ${udev_rulesdir}/60-persistent-xvd.rules <<'_EOR_'
ACTION=="remove", GOTO="xvd_aliases_end"
SUBSYSTEM!="block", GOTO="xvd_aliases_end"
KERNEL=="xvd*[!0-9]", IMPORT{program}=="%{name}-tools-domU.sh --devpath %%p --devtype $env{DEVTYPE}"
KERNEL=="xvd*[0-9]",  IMPORT{program}=="%{name}-tools-domU.sh --devpath %%p --devtype $env{DEVTYPE}"
KERNEL=="xvd*[!0-9]", ENV{VBD_HD_SYMLINK}=="hd[a-d]", SYMLINK+="$env{VBD_HD_SYMLINK}"
KERNEL=="xvd*[0-9]",  ENV{VBD_HD_SYMLINK}=="hd[a-d]", SYMLINK+="$env{VBD_HD_SYMLINK}%%n"
LABEL="xvd_aliases_end"
_EOR_
#
tee ${udev_rulesdir}/80-%{name}-channel-setup.rules <<'_EOF_'
SUBSYSTEM=="xen", DEVPATH=="/devices/console-[0-9]", IMPORT{program}=="xen-channel-setup.sh $attr{nodename} %%n"

SUBSYSTEM=="xen", DEVPATH=="/devices/console-[0-9]", ENV{XEN_CHANNEL_NAME}=="org.qemu.guest_agent.0", TAG+="systemd", ENV{SYSTEMD_WANTS}+="qemu-ga@hvc%%n.service"
_EOF_
#
dracut_moduledir=%{buildroot}/usr/lib/dracut/modules.d/50%{name}-tools-domU
mkdir -p ${dracut_moduledir}
tee ${dracut_moduledir}/module-setup.sh <<'_EOS_'
#!/bin/bash
check() {
  require_binaries xenstore-read || return 1
  return 0
}

depends() {
  return 0
}
install() {
  inst_multiple xenstore-read
  inst_multiple ${udevdir}/%{name}-tools-domU.sh
  inst_rules 60-persistent-xvd.rules
}
_EOS_
chmod 755 ${dracut_moduledir}/module-setup.sh
#
udev_programdir=%{buildroot}/usr/lib/udev
mkdir -p ${udev_programdir}
tee ${udev_programdir}/%{name}-tools-domU.sh <<'_EOS_'
#!/bin/bash
set -e
devpath=
devtype=
dev=
while test "$#" -gt 0
do
  : "$1"
  case "$1" in
    --devpath) devpath=$2 ; shift ;;
    --devtype) devtype=$2 ; shift ;;
    *) echo "$0: Unknown option $1" >&2 ; exit 1 ;;
  esac
  shift
done
test -n "${devpath}" || exit 1
test -n "${devtype}" || exit 1
cd "/sys/${devpath}"
case "${devtype}" in
  partition) cd .. ;;
esac
cd -P device
d="${PWD##*/}"
d="${d/-/\/}"
backend="`xenstore-read device/${d}/backend`"
dev="`xenstore-read \"${backend}\"/dev`"
test -n "${dev}" && echo "VBD_HD_SYMLINK=${dev}"
_EOS_
#
tee ${udev_programdir}/%{name}-channel-setup.sh <<'_EOF_'
#!/bin/bash

if test "$#" -ne 2; then
    exit 1
fi

channel_path="$1"
channel_num="$2"

name="`xenstore-read \"$channel_path\"/name`"
test -z "$name" && exit 1

if test $name != "org.qemu.guest_agent.0"; then
    exit 1
fi

mkdir -p /dev/xenchannel
devname=/dev/xenchannel/$name
# Xen's console devices are used for channels. See xen-pv-channel(7)
# for more details
ln -sfn /dev/hvc$channel_num $devname

echo "XEN_CHANNEL_NAME=$name"
_EOF_
chmod 755 ${udev_programdir}/*.sh

# EFI
%if %{?with_dom0_support}0
arch=`uname -m`
install_xen()
{
    local ext=""
    find %{buildroot}/boot -ls
    if [ -n "$1" ]; then
        ext="-$1"
        mv %{buildroot}/boot/xen-syms-${XEN_FULLVERSION} \
           %{buildroot}/boot/xen-syms${ext}-${XEN_FULLVERSION}
        mv %{buildroot}/boot/xen-${XEN_FULLVERSION}%{xen_install_suffix} \
           %{buildroot}/boot/xen${ext}-${XEN_FULLVERSION}%{xen_install_suffix}
        if test -d %{buildroot}/%{_libdir}/efi; then
            mv %{buildroot}/%{_libdir}/efi/xen-${XEN_FULLVERSION}.efi %{buildroot}/%{_libdir}/efi/xen${ext}-${XEN_FULLVERSION}.efi
            ln -sf xen${ext}-${XEN_FULLVERSION}.efi %{buildroot}/%{_libdir}/efi/xen${ext}-$XEN_VERSION.$XEN_SUBVERSION.efi
            ln -sf xen${ext}-${XEN_FULLVERSION}.efi %{buildroot}/%{_libdir}/efi/xen${ext}-$XEN_VERSION.efi
            ln -sf xen${ext}-${XEN_FULLVERSION}.efi %{buildroot}/%{_libdir}/efi/xen${ext}.efi
        fi
    elif test -d %{buildroot}/%{_libdir}/efi; then
        # Move the efi files to /usr/share/efi/<arch> (fate#326960)
        mkdir -p %{buildroot}/%{_datadir}/efi/$arch
        mv %{buildroot}/%{_libdir}/efi/xen*.efi %{buildroot}/%{_datadir}/efi/$arch/
        ln -s %{_datadir}/efi/$arch/xen-${XEN_FULLVERSION}.efi %{buildroot}/%{_libdir}/efi/xen.efi
    fi
    rm %{buildroot}/boot/xen-$XEN_VERSION.$XEN_SUBVERSION%{xen_install_suffix}
    rm %{buildroot}/boot/xen-$XEN_VERSION%{xen_install_suffix}
    rm %{buildroot}/boot/xen%{xen_install_suffix}
    # Do not link to links; grub cannot follow.
    ln -s xen${ext}-${XEN_FULLVERSION}%{xen_install_suffix} %{buildroot}/boot/xen${ext}-$XEN_VERSION.$XEN_SUBVERSION%{xen_install_suffix}
    ln -s xen${ext}-${XEN_FULLVERSION}%{xen_install_suffix} %{buildroot}/boot/xen${ext}-$XEN_VERSION%{xen_install_suffix}
    ln -s xen${ext}-${XEN_FULLVERSION}%{xen_install_suffix} %{buildroot}/boot/xen${ext}%{xen_install_suffix}
    if test -f xen-syms${ext}-${XEN_FULLVERSION}; then
        ln -sf xen-syms${ext}-${XEN_FULLVERSION} %{buildroot}/boot/xen-syms${ext}
    fi
    find %{buildroot}/boot -ls
}
export BRP_PESIGN_FILES="*.efi /lib/firmware"
CC=gcc
%if %{?with_gcc47}0
CC=gcc-4.7
%endif
%if %{?with_gcc48}0
CC=gcc-4.8
%endif
rm -fv xen/.config
echo CONFIG_REQUIRE_NX=y > xen/.config
echo CONFIG_DIT_DEFAULT=y >> xen/.config
%if %{with xen_debug}
echo CONFIG_DEBUG=y >> xen/.config
echo "CONFIG_DOM0_MEM=\"1G+10%%,max:64G\"" >> xen/.config
yes '' | make -C xen oldconfig
make -C xen install XEN_BUILD_DATE="$XEN_BUILD_DATE" XEN_BUILD_TIME="$XEN_BUILD_TIME" DEBUG_DIR=/boot DESTDIR=%{buildroot} CC=$CC %{?_smp_mflags}
install_xen dbg
make -C xen clean
%endif
echo CONFIG_DEBUG=n >> xen/.config
echo "CONFIG_DOM0_MEM=\"1G+10%%,max:64G\"" >> xen/.config
yes '' | make -C xen oldconfig
make -C xen install XEN_BUILD_DATE="$XEN_BUILD_DATE" XEN_BUILD_TIME="$XEN_BUILD_TIME" DEBUG_DIR=/boot DESTDIR=%{buildroot} CC=$CC %{?_smp_mflags}
install_xen
make -C xen clean
%endif

# On x86_64, qemu-xen was installed as /usr/lib/xen/bin/qemu-system-i386
# and advertised as the <emulator> in libvirt capabilities. Tool such as
# virt-install include <emulator> in domXML they produce, so we need to
# preserve the path. For x86_64, create a simple wrapper that invokes
# /usr/bin/qemu-system-i386
# Using qemu-system-x86_64 will result in an incompatible VM
%ifarch x86_64 aarch64
hardcoded_path_in_existing_domU_xml='%{_libexecdir}/%{name}/bin'
mkdir -vp %{buildroot}${hardcoded_path_in_existing_domU_xml}
tee %{buildroot}${hardcoded_path_in_existing_domU_xml}/qemu-system-%{qemu_arch} << 'EOF'
#!/bin/sh

exec %{_bindir}/qemu-system-%{qemu_arch} "$@"
EOF
chmod 0755 %{buildroot}${hardcoded_path_in_existing_domU_xml}/qemu-system-%{qemu_arch}

#
unit='%{_libexecdir}/%{name}/bin/xendomains-wait-disks'
mkdir -vp '%{buildroot}%{_libexecdir}/%{name}/bin'
cp -avL '%{SOURCE10172}' "%{buildroot}${unit}"
mkdir xendomains-wait-disk
cp -avL '%{SOURCE10173}' xendomains-wait-disk/LICENSE
cp -avL '%{SOURCE10174}' xendomains-wait-disk/README.md
tee %{buildroot}%{_unitdir}/xendomains-wait-disks.service <<_EOS_
[Unit]
Description=Xendomains - for those machines that will start, wait for their disks to appear
Requires=proc-xen.mount xenstored.service
After=proc-xen.mount xenstored.service xenconsoled.service xen-init-dom0.service
After=network-online.target
After=remote-fs.target
Before=xendomains.service
ConditionPathExists=/proc/xen/capabilities

[Service]
Type=oneshot
ExecStart=${unit}
TimeoutSec=5min

[Install]
WantedBy=xendomains.service
_EOS_
#
%endif

# Stubdom
%if %{?with_dom0_support}0
# Docs
mkdir -p %{buildroot}/%{_defaultdocdir}/xen/misc
for name in COPYING %SOURCE10 %SOURCE11 %SOURCE12; do
    install -m 644 $name %{buildroot}/%{_defaultdocdir}/xen/
done
for name in vtpm-platforms.txt crashdb.txt xenpaging.txt \
    xen-command-line.pandoc xenstore-paths.pandoc; do
    install -m 644 docs/misc/$name %{buildroot}/%{_defaultdocdir}/xen/misc/
done

# Xen utilities
install -m755 %SOURCE36 %{buildroot}/usr/sbin/xen2libvirt
install -m755 %SOURCE10183 %{buildroot}/usr/sbin/xen_maskcalc

rm -f %{buildroot}/etc/xen/README*
# Example config
mkdir -p %{buildroot}/etc/xen/{vm,examples,scripts}
mv %{buildroot}/etc/xen/xlexample* %{buildroot}/etc/xen/examples
rm -f %{buildroot}/etc/xen/examples/*nbd
install -m644 tools/xentrace/formats %{buildroot}/etc/xen/examples/xentrace_formats.txt

# Scripts
rm -f %{buildroot}/etc/xen/scripts/block-*nbd
install -m755 %SOURCE21 %SOURCE22 %SOURCE23 %SOURCE24 %{buildroot}/etc/xen/scripts/
mkdir -p %{buildroot}/usr/lib/supportconfig/plugins
install -m 755 %SOURCE13 %{buildroot}/usr/lib/supportconfig/plugins/xen

# Xen API remote authentication files and Logrotate files
install -m644 %SOURCE31 %{buildroot}/etc/xen/
%if 0%{?suse_version} > 1500
mkdir -p %{buildroot}%{_distconfdir}/logrotate.d
install -m644 -D %SOURCE14 %{buildroot}%{_distconfdir}/logrotate.d/xen
install -d %{buildroot}%{_pam_vendordir}
install -m644 %SOURCE30 %{buildroot}/%{_pam_vendordir}/xen-api
%else
install -m644 -D %SOURCE14 %{buildroot}%{_sysconfdir}/logrotate.d/xen
install -d %{buildroot}/etc/pam.d
install -m644 %SOURCE30 %{buildroot}/etc/pam.d/xen-api
%endif

# Directories
mkdir -p %{buildroot}/var/lib/xenstored
mkdir -p %{buildroot}/var/lib/xen/images
mkdir -p %{buildroot}/var/lib/xen/jobs
mkdir -p %{buildroot}/var/lib/xen/save
mkdir -p %{buildroot}/var/lib/xen/dump
mkdir -p %{buildroot}/var/log/xen
mkdir -p %{buildroot}/var/log/xen/console

# Systemd
cp -bavL %{S:41} %{buildroot}/%{_unitdir}
bn=`basename %{S:42}`
cp -bavL %{S:42} %{buildroot}/%{_unitdir}/${bn}
mods="`
for conf in $(ls %{buildroot}/%{with_systemd_modules_load}/*.conf)
do
	grep -v ^# $conf
	echo -n > $conf
done
`"
> mods
for mod in $mods
do
	# load by alias, if possible, to handle pvops and xenlinux
	alias="$mod"
	case "$mod" in
		xen-evtchn) ;;
		xen-gntdev) ;;
		xen-gntalloc) ;;
		xen-blkback) alias='xen-backend:vbd' ;;
		xen-netback) alias='xen-backend:vif' ;;
		xen-pciback) alias='xen-backend:pci' ;;
		evtchn) unset alias ;;
		gntdev) unset alias ;;
		netbk) alias='xen-backend:vif' ;;
		blkbk) alias='xen-backend:vbd' ;;
		xen-scsibk) unset alias ;;
		usbbk) unset alias ;;
		pciback) alias='xen-backend:pci' ;;
		xen-acpi-processor) ;;
		blktap2) unset alias ;;
		*) ;;
	esac
	if test -n "${alias}"
	then
		echo "ExecStart=-/bin/sh -c 'modprobe $alias || :'" >> mods
	fi
done
sort -u mods | tee -a %{buildroot}/%{_unitdir}/${bn}
rm -rfv %{buildroot}/%{_initddir}
install -m644 %SOURCE35 %{buildroot}/%{_fillupdir}/sysconfig.pciback

# Clean up unpackaged files
find %{buildroot} \( \
	-name .deps -o \
	-name README.blktap -o \
	-name README.xenmon -o \
	-name target-x86_64.conf -o \
	-name xen-mfndump -o \
	-name qcow-create -o \
	-name img2qcow -o \
	-name qcow2raw -o \
	-name qemu-bridge-helper -o \
	-name qemu-img-xen -o \
	-name qemu-nbd-xen -o \
	-name palcode-clipper -o \
	-name "*.dtb" -o \
	-name "openbios-*" -o \
	-name "petalogix*" -o \
	-name "ppc*" -o \
	-name "*.pyc" -o \
	-name "s390*" -o \
	-name "slof*" -o \
	-name "spapr*" -o \
	-name "*.egg-info" \) \
	-print -delete
# Wipe empty directories
if find %{buildroot}/usr -type d -print0 | xargs -0n1 rmdir -p 2>/dev/null
then
	:
fi

# "xl devd" has to be called manually in a driver domain
find %{buildroot} -name xendriverdomain.service -print -delete

# Create hardlinks for 3 .txt files and 1 .py
%fdupes %{buildroot}/%{_prefix}
find %{buildroot} -type f -size 0 -delete -print

%else
# !with_dom0_support

# 32 bit hypervisor no longer supported.  Remove dom0 tools.
rm -rf %{buildroot}/%{_datadir}/doc
rm -rf %{buildroot}/%{_datadir}/man
rm -rf %{buildroot}/%{_libexecdir}/%{name}
rm -rf %{buildroot}/%{_libdir}/python*
rm -rf %{buildroot}/%{_unitdir}
rm -rf %{buildroot}/%{_fillupdir}
rm -rf %{buildroot}/%{with_systemd_modules_load}
rm -rf %{buildroot}/usr/sbin
rm -rf %{buildroot}/etc/xen
rm -rf %{buildroot}/var
rm -f  %{buildroot}/%{_sysconfdir}/bash_completion.d/xl
rm -f  %{buildroot}/%{_sysconfdir}/init.d/xen*
rm -f  %{buildroot}/%{_bindir}/*trace*
rm -f  %{buildroot}/%{_bindir}/vchan-socket-proxy
rm -f  %{buildroot}/%{_bindir}/xenalyze*
rm -f  %{buildroot}/%{_bindir}/xenco*
rm -f  %{buildroot}/%{_bindir}/xen-cpuid
rm -f  %{buildroot}/%{_bindir}/pygrub
rm -f  %{buildroot}/%{_bindir}/remus
rm -f  %{buildroot}/usr/etc/qemu/target-x86_64.conf
rm -f  %{buildroot}/usr/libexec/qemu-bridge-helper
%endif

%if %{?with_dom0_support}0

%files
%defattr(-,root,root)
/boot/*
%{_libdir}/efi
%{_datadir}/efi

%endif

%files libs
%defattr(-,root,root)
%{_libdir}/xenfsimage/
%{_libdir}/*.so.*

%if %{?with_dom0_support}0

%files tools
%defattr(-,root,root)
/usr/bin/xenalyze
/usr/bin/xenstore*
/usr/bin/pygrub
/usr/bin/vchan-socket-proxy
/usr/bin/xencov_split
/usr/bin/xentrace_format
%ifarch x86_64
/usr/bin/xen-cpuid
%endif
/usr/sbin/xenbaked
/usr/sbin/xenconsoled
/usr/sbin/xencov
/usr/sbin/xenlockprof
/usr/sbin/xenmon
/usr/sbin/xenperf
/usr/sbin/xenpm
/usr/sbin/xenpmd
/usr/sbin/xenstored
/usr/sbin/xentop
/usr/sbin/xentrace
/usr/sbin/xentrace_setmask
/usr/sbin/xentrace_setsize
/usr/sbin/xenwatchdogd
/usr/sbin/flask-get-bool
/usr/sbin/flask-getenforce
/usr/sbin/flask-label-pci
/usr/sbin/flask-loadpolicy
/usr/sbin/flask-set-bool
/usr/sbin/flask-setenforce
%if %{?with_gdbsx}0
/usr/sbin/gdbsx
%endif
/usr/sbin/xl
/usr/sbin/xen2libvirt
/usr/sbin/xen-access
/usr/sbin/xen_maskcalc
%ifarch %ix86 x86_64
/usr/sbin/xen-hptool
/usr/sbin/xen-hvmcrash
/usr/sbin/xen-hvmctx
/usr/sbin/xen-kdd
/usr/sbin/xen-lowmemd
/usr/sbin/xen-memshare
/usr/sbin/xen-ucode
/usr/sbin/xen-mceinj
/usr/sbin/xen-vmtrace
%endif
/usr/sbin/xenhypfs
/usr/sbin/xen-livepatch
/usr/sbin/xen-diag
%dir %attr(700,root,root) /etc/xen
%dir /etc/xen/scripts
/etc/xen/scripts/block*
/etc/xen/scripts/external-device-migrate
/etc/xen/scripts/hotplugpath.sh
/etc/xen/scripts/launch-xenstore
/etc/xen/scripts/locking.sh
/etc/xen/scripts/logging.sh
/etc/xen/scripts/vif-*
/etc/xen/scripts/vscsi
/etc/xen/scripts/xen-hotplug-*
/etc/xen/scripts/xen-network-common.sh
/etc/xen/scripts/xen-script-common.sh
/etc/xen/scripts/colo-proxy-setup
/etc/xen/scripts/remus-netbuf-setup
%dir /usr/lib/supportconfig
%dir /usr/lib/supportconfig/plugins
/usr/lib/supportconfig/plugins/xen
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/bin
%exclude %{_libexecdir}/%{name}-tools-domU
%ifarch x86_64
%{_libexecdir}/%{name}/boot
%exclude %{_libexecdir}/%{name}/bin/xendomains-wait-disks
%endif
%{_fillupdir}/sysconfig.pciback
%{_fillupdir}/sysconfig.xencommons
%{_fillupdir}/sysconfig.xendomains
%dir /var/lib/xen
%dir %attr(700,root,root) /var/lib/xen/images
%dir %attr(700,root,root) /var/lib/xen/save
%dir %attr(700,root,root) /var/lib/xen/dump
%ifarch %ix86 x86_64
%dir %attr(700,root,root) /var/lib/xen/xenpaging
%endif
%dir /var/lib/xenstored
%dir /var/log/xen
%dir /var/log/xen/console
%if 0%{?suse_version} > 1500
%{_distconfdir}/logrotate.d/xen
%{_pam_vendordir}/xen-api
%else
%config(noreplace) %{_sysconfdir}/logrotate.d/xen
%config /etc/pam.d/xen-api
%endif
/etc/xen/auto
%config /etc/xen/examples
%config /etc/xen/cpupool
%config /etc/xen/vm
%config(noreplace) /etc/xen/xenapiusers
%config(noreplace) /etc/xen/xl.conf
%config %{_unitdir}
%exclude %{_unitdir}/%{name}-vcpu-watch.service
%exclude %{_unitdir}/xendomains-wait-disks.service
%config %{with_systemd_modules_load}
/etc/bash_completion.d/xl
%dir %{_libdir}/python%{pyver}/site-packages/grub
%dir %{_libdir}/python%{pyver}/site-packages/xen
%dir %{_libdir}/python%{pyver}/site-packages/xen/lowlevel
%dir %{_libdir}/python%{pyver}/site-packages/xen/migration
%{_libdir}/python%{pyver}/site-packages/grub/*
%{_libdir}/python%{pyver}/site-packages/xen/util.py
%{_libdir}/python%{pyver}/site-packages/xen/lowlevel/*
%{_libdir}/python%{pyver}/site-packages/xen/migration/*
%{_libdir}/python%{pyver}/site-packages/*.so
%dir %{_defaultdocdir}/xen
%{_defaultdocdir}/xen/COPYING
%{_defaultdocdir}/xen/README.SUSE
%{_defaultdocdir}/xen/boot.local.xenU
%{_defaultdocdir}/xen/boot.xen
%{_mandir}/man*/*

%ifarch x86_64
%files tools-xendomains-wait-disk
%license xendomains-wait-disk/LICENSE
%doc xendomains-wait-disk/README.md
%config %{_unitdir}/xendomains-wait-disks.service
%config %attr(0755,root,root) %{_libexecdir}/%{name}/bin/xendomains-wait-disks
%endif
# with_dom0_support
%endif

%posttrans -n %{name}-tools-domU
%{?regenerate_initrd_posttrans}

%files tools-domU
%defattr(-,root,root)
%ifarch %ix86 x86_64
/usr/bin/xen-detect
%exclude /usr/bin/xenstore-control
%endif
/usr/bin/xenstore*
%if %{?with_dom0_support}0
%config %{_unitdir}/%{name}-vcpu-watch.service
%endif
%{_libexecdir}/%{name}-tools-domU
/usr/lib/udev
/usr/lib/dracut

%files devel
%defattr(-,root,root)
%{_libdir}/*.a
%{_libdir}/*.so
/usr/include/*
%{_libdir}/pkgconfig/xenlight.pc
%{_libdir}/pkgconfig/xlutil.pc
%{_libdir}/pkgconfig/xencall.pc
%{_libdir}/pkgconfig/xencontrol.pc
%{_libdir}/pkgconfig/xendevicemodel.pc
%{_libdir}/pkgconfig/xenevtchn.pc
%{_libdir}/pkgconfig/xenforeignmemory.pc
%{_libdir}/pkgconfig/xengnttab.pc
%{_libdir}/pkgconfig/xenguest.pc
%{_libdir}/pkgconfig/xenhypfs.pc
%{_libdir}/pkgconfig/xenstat.pc
%{_libdir}/pkgconfig/xenstore.pc
%{_libdir}/pkgconfig/xentoolcore.pc
%{_libdir}/pkgconfig/xentoollog.pc
%{_libdir}/pkgconfig/xenvchan.pc

%if %{?with_dom0_support}0

%files doc-html
%defattr(-,root,root)
%dir %{_defaultdocdir}/xen
%{_defaultdocdir}/xen/misc
%{_defaultdocdir}/xen/html

%post
if [ -x /sbin/update-bootloader ]; then
    /sbin/update-bootloader --refresh; exit 0
fi

%pre tools
%service_add_pre xencommons.service
%service_add_pre xendomains.service
%service_add_pre xen-watchdog.service
%service_add_pre xenstored.service
%service_add_pre xen-dom0-modules.service
%service_add_pre xenconsoled.service
%service_add_pre xen-init-dom0.service
%service_add_pre xen-qemu-dom0-disk-backend.service
%if 0%{?suse_version} > 1500
# Prepare for migration to /usr/etc; save any old .rpmsave
for i in logrotate.d/xen pam.d/xen-api ; do
   test -f %{_sysconfdir}/${i}.rpmsave && mv -v %{_sysconfdir}/${i}.rpmsave %{_sysconfdir}/${i}.rpmsave.old ||:
done
%endif

%if 0%{?suse_version} > 1500
%posttrans tools
# Migration to /usr/etc, restore just created .rpmsave
for i in logrotate.d/xen pam.d/xen-api ; do
   test -f %{_sysconfdir}/${i}.rpmsave && mv -v %{_sysconfdir}/${i}.rpmsave %{_sysconfdir}/${i} ||:
done
%endif

%post tools
%{fillup_only -n xencommons xencommons}
%{fillup_only -n xendomains xendomains}
%service_add_post xencommons.service
%service_add_post xendomains.service
%service_add_post xen-watchdog.service
%service_add_post xenstored.service
%service_add_post xen-dom0-modules.service
%service_add_post xenconsoled.service
%service_add_post xen-init-dom0.service
%service_add_post xen-qemu-dom0-disk-backend.service

if [ -f /etc/default/grub ] && ! (/usr/bin/grep GRUB_CMDLINE_XEN /etc/default/grub >/dev/null); then
    echo '# Xen boot parameters for all Xen boots' >> /etc/default/grub
    echo 'GRUB_CMDLINE_XEN=""' >> /etc/default/grub
    echo '# Xen boot parameters for non-recovery Xen boots (in addition to GRUB_CMDLINE_XEN)' >> /etc/default/grub
    echo 'GRUB_CMDLINE_XEN_DEFAULT=""' >> /etc/default/grub
fi
if [ -f %{_datadir}/grub2/i386-xen/grub.xen ] && [ ! -f %{_libexecdir}/%{name}/boot/pvgrub32.bin ]; then
 ln -sv %{_datadir}/grub2/i386-xen/grub.xen             %{_libexecdir}/%{name}/boot/pvgrub32.bin
fi
if [ -f %{_datadir}/grub2/x86_64-xen/grub.xen ] && [ ! -f %{_libexecdir}/%{name}/boot/pvgrub64.bin ]; then
 ln -sv %{_datadir}/grub2/x86_64-xen/grub.xen             %{_libexecdir}/%{name}/boot/pvgrub64.bin
fi

%preun tools
%service_del_preun xencommons.service
%service_del_preun xendomains.service
%service_del_preun xen-watchdog.service
%service_del_preun xenstored.service
%service_del_preun xen-dom0-modules.service
%service_del_preun xenconsoled.service
%service_del_preun xen-init-dom0.service
%service_del_preun xen-qemu-dom0-disk-backend.service

%postun tools
%if %{defined service_del_postun_without_restart}
%service_del_postun_without_restart xencommons.service
%service_del_postun_without_restart xendomains.service
%service_del_postun_without_restart xen-watchdog.service
%service_del_postun_without_restart xenstored.service
%service_del_postun_without_restart xen-dom0-modules.service
%service_del_postun_without_restart xenconsoled.service
%service_del_postun_without_restart xen-init-dom0.service
%service_del_postun_without_restart xen-qemu-dom0-disk-backend.service
%else
export DISABLE_RESTART_ON_UPDATE=yes
%service_del_postun xencommons.service
%service_del_postun xendomains.service
%service_del_postun xen-watchdog.service
%service_del_postun xenstored.service
%service_del_postun xen-dom0-modules.service
%service_del_postun xenconsoled.service
%service_del_postun xen-init-dom0.service
%service_del_postun xen-qemu-dom0-disk-backend.service
%endif

%endif

%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig

%changelog
