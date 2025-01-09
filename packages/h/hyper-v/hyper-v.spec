#
# spec file for package hyper-v
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


%define hv_kvp_daemon hv_kvp_daemon
%define hv_vss_daemon hv_vss_daemon
%define hv_fcopy_daemon hv_fcopy_daemon
%define vmbus_bufring vmbus_bufring
%define hv_fcopy_uio_daemon hv_fcopy_uio_daemon
%define include_uapi_linux_hyperv include_uapi_linux_hyperv
%define chardev_kvp vmbus/hv_kvp
%define chardev_vss vmbus/hv_vss
%define chardev_fcopy vmbus/hv_fcopy
%define helper_dir /usr/lib/%name

Name:           hyper-v
ExclusiveArch:  %ix86 x86_64 aarch64
%{?systemd_requires}
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(systemd)
# Due to usage of char device instead of netlink
Conflicts:      kernel < 4.2
Summary:        Microsoft Hyper-V tools
License:        GPL-2.0-only
Supplements:    modalias(dmi:*svnMicrosoftCorporation*pnVirtualMachine*rnVirtualMachine*)
Supplements:    modalias(pci:v00001414d00005353sv*sd*bc*sc*i*)
URL:            http://www.kernel.org
# Arbitrary version number
Version:        9
Release:        0
Source0:        hyper-v.lsvmbus.py
Source7:        hyper-v.compare-with-upstream.sh
Source8:        hyper-v.tools.hv.vmbus_bufring.h
Source9:        hyper-v.include.linux.hyperv.h
Source10:       hyper-v.tools.hv.hv_kvp_daemon.c
Source11:       hyper-v.tools.hv.vmbus_bufring.c
Source12:       hyper-v.tools.hv.hv_vss_daemon.c
Source13:       hyper-v.tools.hv.hv_fcopy_uio_daemon.c
Source14:       hyper-v.tools.hv.hv_fcopy_daemon.c
Source20:       hyper-v.tools.hv.hv_get_dhcp_info.sh
Source21:       hyper-v.tools.hv.hv_get_dns_info.sh
Source22:       hyper-v.tools.hv.hv_set_ifconfig.sh

Patch0:         hyper-v.kvp.gethostname.patch

%description
This package contains the Microsoft Hyper-V tools.

%prep
%setup -Tc
cp -vL %{S:8} %vmbus_bufring.h
cp -vL %{S:9} %include_uapi_linux_hyperv.h
cp -vL %{S:10} .
cp -vL %{S:11} %vmbus_bufring.c
cp -vL %{S:12} %hv_vss_daemon.c
cp -vL %{S:13} %hv_fcopy_uio_daemon.c
cp -vL %{S:14} %hv_fcopy_daemon.c
%patch -P 0 -p1
mv `basename %{S:10}` %hv_kvp_daemon.c

%build
sed -i~ '/#include <linux.hyperv.h>/d' %hv_kvp_daemon.c
sed -i~ '/#include <linux.hyperv.h>/d' %hv_vss_daemon.c
sed -i~ '/#include <linux.hyperv.h>/d' %hv_fcopy_uio_daemon.c
sed -i~ '/#include <linux.hyperv.h>/d' %hv_fcopy_daemon.c
gcc \
	$RPM_OPT_FLAGS \
	-Wno-unused-variable \
	-Wno-pointer-sign \
	-D_GNU_SOURCE \
	-g \
	%hv_kvp_daemon.c \
	-include %include_uapi_linux_hyperv.h \
	-DCN_KVP_IDX=0x9 \
	-DCN_KVP_VAL=0x1 \
	-DKVP_SCRIPTS_PATH= \
	-pthread \
	-o %hv_kvp_daemon
gcc \
	$RPM_OPT_FLAGS \
	-Wno-unused-variable \
	-Wno-pointer-sign \
	-D_GNU_SOURCE \
	-g \
	%hv_vss_daemon.c \
	-include %include_uapi_linux_hyperv.h \
	-DCN_VSS_IDX=0xa \
	-DCN_VSS_VAL=0x1 \
	-o %hv_vss_daemon
gcc \
	$RPM_OPT_FLAGS \
	-Wno-unused-variable \
	-Wno-pointer-sign \
	-D_GNU_SOURCE \
	-g \
	%hv_fcopy_daemon.c \
	-include %include_uapi_linux_hyperv.h \
	-o %hv_fcopy_daemon

%ifarch %ix86 x86_64
gcc \
	$RPM_OPT_FLAGS \
	-Wno-unused-variable \
	-Wno-pointer-sign \
	-Wno-address-of-packed-member \
	-D_GNU_SOURCE \
	-g \
	%vmbus_bufring.c \
	%hv_fcopy_uio_daemon.c \
	-include %include_uapi_linux_hyperv.h \
	-o %hv_fcopy_uio_daemon
%endif

%install
# It is not a callable app anyway, so move it out of the way
bindir=%helper_dir/bin
mkdir -p %buildroot${bindir}
mkdir -p %buildroot%_sbindir
install -m755 %hv_kvp_daemon %buildroot${bindir}
install -m755 %hv_vss_daemon %buildroot${bindir}
install -m755 %hv_fcopy_daemon %buildroot${bindir}
%ifarch %ix86 x86_64
install -m755 %hv_fcopy_uio_daemon %buildroot${bindir}
%endif
cp -avL %{S:0} %buildroot%_sbindir/lsvmbus
chmod 0755 %buildroot%_sbindir/lsvmbus
cp -avL %{S:20} %buildroot${bindir}/hv_get_dhcp_info
cp -avL %{S:21} %buildroot${bindir}/hv_get_dns_info
cp -avL %{S:22} %buildroot${bindir}/hv_set_ifconfig
chmod 755 %buildroot${bindir}/*
d=%buildroot%_unitdir
mkdir -vp ${d}
#
tee ${d}/%hv_kvp_daemon.service <<EOF
# started via %_udevrulesdir/%name.rules
[Unit]
Description=Hyper-V KVP Daemon
After=local-fs.target
ConditionVirtualization=microsoft
ConditionPathExists=/dev/%chardev_kvp

[Service]
Environment="PATH=${bindir}:/usr/sbin:/usr/bin:/sbin:/bin"
ExecStart=${bindir}/%hv_kvp_daemon --no-daemon
Restart=on-failure

[Install]
WantedBy=default.target
EOF
#
tee ${d}/%hv_vss_daemon.service <<EOF
# started via %_udevrulesdir/%name.rules
[Unit]
Description=Hyper-V VSS Daemon
ConditionVirtualization=microsoft
ConditionPathExists=/dev/%chardev_vss

[Service]
ExecStart=${bindir}/%hv_vss_daemon --no-daemon
Restart=on-failure

[Install]
WantedBy=default.target
EOF
#
tee ${d}/%hv_fcopy_daemon.service <<EOF
# started via %_udevrulesdir/%name.rules
[Unit]
Description=Hyper-V host to guest file copy daemon
ConditionVirtualization=microsoft
ConditionPathExists=/dev/%chardev_fcopy

[Service]
ExecStart=${bindir}/%hv_fcopy_daemon --no-daemon
Restart=on-failure

[Install]
WantedBy=default.target
EOF
#
tee ${d}/%hv_fcopy_uio_daemon.service <<EOF
# started via %_udevrulesdir/%name.rules
[Unit]
Description=Hyper-V host to guest UIO file copy daemon
ConditionVirtualization=microsoft
ConditionPathExists=/sys/bus/vmbus/drivers/uio_hv_generic/new_id
ConditionPathExists=!/dev/%chardev_fcopy

[Service]
ExecStartPre=/bin/sh -c 'set -e;echo 34d14be3-dee4-41c8-9ae7-6b174977c192 > /sys/bus/vmbus/drivers/uio_hv_generic/new_id'
ExecStart=${bindir}/%hv_fcopy_uio_daemon --no-daemon
Restart=on-failure

[Install]
WantedBy=default.target
EOF
#
#
#
d=%buildroot%_udevrulesdir
mkdir -vp ${d}
tee ${d}/%name.rules <<EOF
ACTION=="add", KERNEL=="%chardev_kvp", TAG+="systemd", ENV{SYSTEMD_WANTS}+="%hv_kvp_daemon.service"
ACTION=="add", KERNEL=="%chardev_vss", TAG+="systemd", ENV{SYSTEMD_WANTS}+="%hv_vss_daemon.service"
ACTION=="add", KERNEL=="%chardev_fcopy", TAG+="systemd", ENV{SYSTEMD_WANTS}+="%hv_fcopy_daemon.service"
ACTION=="add", SUBSYSTEM=="vmbus", ATTRS{class_id}=="{34d14be3-dee4-41c8-9ae7-6b174977c192}", RUN{builtin}+="kmod load uio_hv_generic", TAG+="systemd", ENV{SYSTEMD_WANTS}+="%hv_fcopy_uio_daemon.service"
EOF
#
#
helper=inst_sys.sh
tee %buildroot${bindir}/${helper} <<'_EOF_'
#!/bin/bash
# Starting daemons via RUN== in udev rules is not supported.
# In inst-sys systemd is not used, so start all daemons manually.
bindir=%helper_dir/bin
declare -a helpers
test -c /dev/%chardev_kvp && helpers+=(%hv_kvp_daemon)
test -c /dev/%chardev_vss && helpers+=(%hv_vss_daemon)
if test -c /dev/%chardev_fcopy
then
	helpers+=(%hv_fcopy_daemon)
else
	modprobe -v uio_hv_generic
	if test -f /sys/bus/vmbus/drivers/uio_hv_generic/new_id
	then
		echo '34d14be3-dee4-41c8-9ae7-6b174977c192' > /sys/bus/vmbus/drivers/uio_hv_generic/new_id
		helpers+=(%hv_fcopy_uio_daemon)
	fi
fi
if test -d /sys/bus/vmbus/devices
then
	export PATH=${bindir}:$PATH
	echo -n "Starting hyper-v helpers:"
	for i in "${helpers[@]}"
	do
		if mkdir /run/$i
		then
			echo -n " $i"
			$i < /dev/null &
		fi
	done
	echo " ... done"
fi
_EOF_
chmod 755 %buildroot${bindir}/${helper}
#
%?python3_fix_shebang

%files
%_unitdir/*
%_udevrulesdir/*
%_sbindir/*
%helper_dir

# the relevant part is systemctl daemon-reload, due to udev triggers
%post
%service_add_post %hv_kvp_daemon %hv_vss_daemon %hv_fcopy_daemon %hv_fcopy_uio_daemon
%postun
%service_del_postun_without_restart %hv_kvp_daemon %hv_vss_daemon %hv_fcopy_daemon %hv_fcopy_uio_daemon

%changelog
