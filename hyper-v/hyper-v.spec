#
# spec file for package hyper-v
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define hv_kvp_daemon hv_kvp_daemon
%define hv_vss_daemon hv_vss_daemon
%define hv_fcopy_daemon hv_fcopy_daemon
%define helper_dir /usr/lib/%{name}

Name:           hyper-v
ExclusiveArch:  %ix86 x86_64
# systemd for post 13.1 releases
%if 0%{?suse_version} > 1310
%define use_systemd 1
%else
%define use_systemd 0
%endif
%if %{use_systemd}
%{?systemd_requires}
BuildRequires:  pkgconfig(systemd)
%else
PreReq:         %insserv_prereq
Requires(pre):  coreutils
%endif
# Due to usage of char device instead of netlink
Conflicts:      kernel < 4.2
Summary:        Microsoft Hyper-V tools
License:        GPL-2.0-only
Group:          System/Kernel
Supplements:    modalias(dmi:*svnMicrosoftCorporation*pnVirtualMachine*rnVirtualMachine*)
Supplements:    modalias(pci:v00001414d00005353sv*sd*bc*sc*i*)
Url:            http://www.kernel.org
# Arbitrary version number
Version:        7
Release:        0
Source0:        hyper-v.lsvmbus.py
Source5:        hyper-v.kvptest.ps1.txt
Source7:        hyper-v.compare-with-upstream.sh
Source9:        hyper-v.include.linux.hyperv.h
Source10:       hyper-v.tools.hv.hv_kvp_daemon.c
Source11:       hyper-v.init.sh
Source12:       hyper-v.tools.hv.hv_vss_daemon.c
Source13:       hyper-v.init.vss.sh
Source14:       hyper-v.tools.hv.hv_fcopy_daemon.c
Source15:       hyper-v.init.fcopy.sh
Source20:       hyper-v.tools.hv.hv_get_dhcp_info.sh
Source21:       hyper-v.tools.hv.hv_get_dns_info.sh
Source22:       hyper-v.tools.hv.hv_set_ifconfig.sh

BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This package contains the Microsoft Hyper-V tools.

%prep
%setup -Tc
cp -avL %{S:5} kvptest.ps1.txt
cp -vL %{S:9} %{hv_kvp_daemon}.h
cp -vL %{S:10} %{hv_kvp_daemon}.c
cp -vL %{S:12} %{hv_vss_daemon}.c
cp -vL %{S:14} %{hv_fcopy_daemon}.c

%build
sed -i~ '/#include <linux.hyperv.h>/d' %{hv_kvp_daemon}.c
sed -i~ '/#include <linux.hyperv.h>/d' %{hv_vss_daemon}.c
sed -i~ '/#include <linux.hyperv.h>/d' %{hv_fcopy_daemon}.c
gcc \
	$RPM_OPT_FLAGS \
	-Wno-unused-variable \
	-Wno-pointer-sign \
	-D_GNU_SOURCE \
	-g \
	%{hv_kvp_daemon}.c \
	-include %{hv_kvp_daemon}.h \
	-DCN_KVP_IDX=0x9 \
	-DCN_KVP_VAL=0x1 \
	-DKVP_SCRIPTS_PATH= \
	-o %{hv_kvp_daemon}
gcc \
	$RPM_OPT_FLAGS \
	-Wno-unused-variable \
	-Wno-pointer-sign \
	-D_GNU_SOURCE \
	-g \
	%{hv_vss_daemon}.c \
	-include %{hv_kvp_daemon}.h \
	-DCN_VSS_IDX=0xa \
	-DCN_VSS_VAL=0x1 \
	-o %{hv_vss_daemon}
gcc \
	$RPM_OPT_FLAGS \
	-Wno-unused-variable \
	-Wno-pointer-sign \
	-D_GNU_SOURCE \
	-g \
	%{hv_fcopy_daemon}.c \
	-include %{hv_kvp_daemon}.h \
	-o %{hv_fcopy_daemon}

%install
%if %{use_systemd}
# It is not a callable app anyway, so move it out of the way
bindir=%{helper_dir}/bin
%else
bindir=%{_sbindir}
%endif
mkdir -p $RPM_BUILD_ROOT${bindir}
mkdir -p $RPM_BUILD_ROOT%{helper_dir}/bin
install -m755 %{hv_kvp_daemon} $RPM_BUILD_ROOT${bindir}
install -m755 %{hv_vss_daemon} $RPM_BUILD_ROOT${bindir}
install -m755 %{hv_fcopy_daemon} $RPM_BUILD_ROOT${bindir}
install -D -m755 %{S:0} $RPM_BUILD_ROOT%{_sbindir}/lsvmbus
cp -avL %{S:20} $RPM_BUILD_ROOT%{helper_dir}/bin/hv_get_dhcp_info
cp -avL %{S:21} $RPM_BUILD_ROOT%{helper_dir}/bin/hv_get_dns_info
cp -avL %{S:22} $RPM_BUILD_ROOT%{helper_dir}/bin/hv_set_ifconfig
chmod 755 $RPM_BUILD_ROOT%{helper_dir}/bin/*
%if %{use_systemd}
d=$RPM_BUILD_ROOT%{_unitdir}
mkdir -vp ${d}
#
tee ${d}/%{hv_kvp_daemon}.service <<EOF
# started via %{_udevrulesdir}/%{hv_kvp_daemon}.rules
[Unit]
Description=Hyper-V KVP Daemon
# During startup the current hostname is cached, so start very late
Requires=network-online.target
After=network-online.target
ConditionVirtualization=microsoft

[Service]
Environment="PATH=%{helper_dir}/bin:/usr/sbin:/usr/bin:/sbin:/bin"
# Restart appears to work, but its unsupported
# Reboot required until kernel-user protocol is fixed
ExecStartPre=/usr/bin/mkdir /run/%{hv_kvp_daemon}
ExecStart=${bindir}/%{hv_kvp_daemon} --no-daemon
ExecReload=/usr/bin/false
Restart=no

[Install]
WantedBy=default.target
EOF
#
tee ${d}/%{hv_vss_daemon}.service <<EOF
# started via %{_udevrulesdir}/%{hv_vss_daemon}.rules
[Unit]
Description=Hyper-V VSS Daemon
ConditionVirtualization=microsoft

[Service]
# Restart appears to work, but its unsupported
# Reboot required until kernel-user protocol is fixed
ExecStartPre=/usr/bin/mkdir /run/%{hv_vss_daemon}
ExecStart=${bindir}/%{hv_vss_daemon} --no-daemon
ExecReload=/usr/bin/false
Restart=no

[Install]
WantedBy=default.target
EOF
#
tee ${d}/%{hv_fcopy_daemon}.service <<EOF
# started via %{_udevrulesdir}/%{hv_fcopy_daemon}.rules
[Unit]
Description=Hyper-V host to guest file copy daemon
ConditionVirtualization=microsoft

[Service]
ExecStart=${bindir}/%{hv_fcopy_daemon} --no-daemon

[Install]
WantedBy=default.target
EOF
#
#
#
d=$RPM_BUILD_ROOT%{_udevrulesdir}
mkdir -vp ${d}
tee ${d}/%{hv_kvp_daemon}.rules <<EOF
ACTION=="add", KERNEL=="vmbus/hv_kvp", TAG+="systemd", ENV{SYSTEMD_WANTS}+="%{hv_kvp_daemon}.service"
EOF
tee ${d}/%{hv_vss_daemon}.rules <<EOF
ACTION=="add", KERNEL=="vmbus/hv_vss", TAG+="systemd", ENV{SYSTEMD_WANTS}+="%{hv_vss_daemon}.service"
EOF
tee ${d}/%{hv_fcopy_daemon}.rules <<EOF
ACTION=="add", KERNEL=="vmbus/hv_fcopy", TAG+="systemd", ENV{SYSTEMD_WANTS}+="%{hv_fcopy_daemon}.service"
EOF
#
#
helper=inst_sys.sh
tee $RPM_BUILD_ROOT${bindir}/${helper} <<EOF
#!/bin/bash
# Starting daemons via RUN== in udev rules is not supported.
# In inst-sys systemd is not used, so start all daemons manually.
if test -d /sys/bus/vmbus/devices
then
	export PATH=${bindir}:\$PATH
	echo -n "Starting hyper-v helpers:"
	for i in \
		%{hv_kvp_daemon} \
		%{hv_vss_daemon} \
		%{hv_fcopy_daemon}
	do
		if mkdir /run/\$i
		then
			echo -n " \$i"
			\$i < /dev/null &
		fi
	done
	echo " ... done"
fi
EOF
chmod 755 $RPM_BUILD_ROOT${bindir}/${helper}
#
%else
mkdir -p $RPM_BUILD_ROOT/etc/init.d
install -m755 %{S:11} $RPM_BUILD_ROOT/etc/init.d/%{hv_kvp_daemon}
ln -sfvbn ../../etc/init.d/%{hv_kvp_daemon} $RPM_BUILD_ROOT${bindir}/rc%{hv_kvp_daemon}
install -m755 %{S:13} $RPM_BUILD_ROOT/etc/init.d/%{hv_vss_daemon}
ln -sfvbn ../../etc/init.d/%{hv_vss_daemon} $RPM_BUILD_ROOT${bindir}/rc%{hv_vss_daemon}
install -m755 %{S:15} $RPM_BUILD_ROOT/etc/init.d/%{hv_fcopy_daemon}
ln -sfvbn ../../etc/init.d/%{hv_fcopy_daemon} $RPM_BUILD_ROOT${bindir}/rc%{hv_fcopy_daemon}
%endif

%files
%defattr (-,root,root)
%doc kvptest.ps1.txt
%if %{use_systemd}
%{_unitdir}
%dir /usr/lib/udev
%{_udevrulesdir}
%else
/etc/init.d/*
%endif
%{_sbindir}/*
%{helper_dir}

%pre
# hv_kvp_daemon in SLES11 SP2 stored temporary state files in /var/opt
# move them to /var/lib and remove old directory, if possible.
if test -d /var/opt/hyperv
then
	if mkdir -p -v -m 0755 /var/lib/hyperv
	then
		cd /var/lib/hyperv
		for oldfile in /var/opt/hyperv/ifcfg-* /var/opt/hyperv/.kvp_pool_*
		do
			if test -e "${oldfile}"
			then
				mv -vfb "${oldfile}" . || :
			fi
		done
		cd - >/dev/null
	fi
	rmdir -v  /var/opt/hyperv || :
fi
%if %{use_systemd}
: nothing to do in case of systemd
%endif

%post
board_vendor=
product_name=
if cd /sys/class/dmi/id 2>/dev/null
then
	if test -r board_vendor
	then
		board_vendor="`cat board_vendor`"
	fi
	if test -r product_name
	then
		product_name="`cat product_name`"
	fi
	cd - >/dev/null
fi
if test "${board_vendor}" = "Microsoft Corporation" -a "${product_name}" = "Virtual Machine"
then
%if %{use_systemd}
: nothing to do in case of systemd
%else
	echo "Enabling %{hv_kvp_daemon} on '${product_name}' from '${board_vendor}'"
	%{insserv_force_if_yast %{hv_kvp_daemon}}
	echo "Enabling %{hv_vss_daemon} on '${product_name}' from '${board_vendor}'"
	%{insserv_force_if_yast %{hv_vss_daemon}}
	echo "Enabling %{hv_fcopy_daemon} on '${product_name}' from '${board_vendor}'"
	%{insserv_force_if_yast %{hv_fcopy_daemon}}
%endif
fi

%preun
%if %{use_systemd}
: nothing to do in case of systemd
%else
%stop_on_removal %{hv_kvp_daemon}
%stop_on_removal %{hv_vss_daemon}
%stop_on_removal %{hv_fcopy_daemon}
%endif

%postun
# no restart on update because the daemon can not be restarted
%if %{use_systemd}
: nothing to do in case of systemd
%else
%insserv_cleanup
%endif

%changelog
