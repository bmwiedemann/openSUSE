#
# spec file for package open-iscsi
#
# Copyright (c) 2022 SUSE LLC
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


%define _home_dir %{_sysconfdir}/iscsi

# Ensure usr-merge does not effect existing SLE. Cannot use _sbindir
# directly since meson macros pass that on, and meson does not like
# setting it to "/sbin".  Also and move DB root to /var/lib/iscsi and
# lockdir to /run/lock/iscsi for Factory but not SLE (yet)
%if ! 0%{?is_opensuse}
# sle
%define _iscsi_sbindir /sbin
%define _lockdir %{_home_dir}
%if 0%{?suse_version} <= 1540
%define _dbroot %{_home_dir}
%else
%define _dbroot %{_sharedstatedir}/iscsi
%define _dbroot_new 1
%endif
%else
# opensuse
%define _iscsi_sbindir /usr/sbin
%define _lockdir %{_rundir}/lock/iscsi
%define _dbroot %{_sharedstatedir}/iscsi
%define _dbroot_new 1
%endif
%if 0%{?_dbroot_new}
%define _install_dbdir_move_readme_value true
%else
%define _install_dbdir_move_readme_value false
%endif

%define iscsi_minor_release 1
%define iscsi_patch_release 8
%define iscsi_patch_release_suse %{iscsi_patch_release}-suse
%define libname libopeniscsiusr0
%define libversion 0.2.0
Name:           open-iscsi
Version:        2.1.8
Release:        0
Summary:        Linux iSCSI Software Initiator
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Other
URL:            https://www.open-iscsi.com
Source:         %{name}-2.%{iscsi_minor_release}.%{iscsi_patch_release_suse}.tar.bz2
Patch1:         %{name}-SUSE-latest.diff.bz2
BuildRequires:  bison
BuildRequires:  db-devel < 5
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  libkmod-devel
BuildRequires:  libmount-devel
BuildRequires:  libtool
BuildRequires:  meson >= 0.54.0
BuildRequires:  open-isns-devel
BuildRequires:  openssl-devel >= 1.1.1c
BuildRequires:  perl
BuildRequires:  pkg-config
BuildRequires:  suse-module-tools
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(systemd)
Requires(post): coreutils
Requires:       %{libname} = %{libversion}
%{?systemd_requires}

%description
This is a transport independent implementation of RFC 3720
iSCSI. It is partitioned into user and kernel parts.

The kernel portion of Open-iSCSI implements the iSCSI data path (that
is, iSCSI Read and iSCSI Write), and consists of two loadable
modules: iscsi_if.ko and iscsi_tcp.ko, and is now is delivered
as part of the kernel.

The user-space part contains the entire control plane: configuration
manager, iSCSI Discovery, Login and Logout processing,
connection-level error processing, Nop-In and Nop-Out handling. It
comes with a daemon process called iscsid, and a management utility,
iscsiadm.

%package -n %{libname}
Version:        0.2.0
Release:        0
Summary:        The iSCSI User-level Library
Group:          System/Libraries
Obsoletes:      libopeniscsiusr0_1_0 <= 2.1.7
Obsoletes:      libopeniscsiusr0_2_0 <= 2.1.7

%description -n %{libname}
The iSCSI user-space API from the open-iscsi project.

%package -n iscsiuio
Version:        0.7.8.6
Release:        0
Summary:        Linux Broadcom NetXtremem II iscsi server
Group:          Productivity/Networking/Other
Requires:       logrotate

%description -n iscsiuio
This tool is to be used in conjunction with the Broadcom NetXtreme II Linux
driver (Kernel module name: "bnx2" and "bnx2x"), Broadcom CNIC driver,
and the Broadcom iSCSI driver (Kernel module name: "bnx2i").
This user-space tool is used in conjunction with the following
Broadcom Network Controllers:

* bnx2:  BCM5706, BCM5708, BCM5709 devices
* bnx2x: BCM57710, BCM57711, BCM57711E, BCM57712, BCM57712E,
         BCM57800, BCM57810, BCM57840 devices

This utility will provide the ARP and DHCP functionality for the iSCSI offload.
The communication to the driver is done via user-space I/O (Kernel module name
"uio").

%package devel
Version:        2.%{iscsi_minor_release}.%{iscsi_patch_release}
Release:        0
Summary:        The iSCSI User-level Library Development Library and Include files
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{libversion}
Requires:       %{name} = %{version}
Conflicts:      libopeniscsiusr0_1_0
Conflicts:      libopeniscsiusr0_2_0

%description devel
This development package contains the open-iscsi user-level library
include files and documentation. These are used to compile against
the libopeniscsiusr library.

%prep
%setup -q -n %{name}-2.%{iscsi_minor_release}.%{iscsi_patch_release_suse}
%patch1 -p1

%build
[ -z "$SOURCE_DATE_EPOCH" ] || export KBUILD_BUILD_TIMESTAMP=@$SOURCE_DATE_EPOCH
%meson --libdir=%{_libdir} \
	-Dc_flags="%{optflags} -fno-strict-aliasing -fno-common -DOFFLOAD_BOOT_SUPPORTED" \
	-Discsi_sbindir=%{_iscsi_sbindir} -Ddbroot=%{_dbroot} -Drulesdir=%{_udevrulesdir} -Dlockdir=%{_lockdir} \
	-Dinstall_dbdir_move_readme=%{_install_dbdir_move_readme_value} \
	--strip
%meson_build

%install
%meson_install
[ -d %{buildroot}%{_iscsi_sbindir} ] || mkdir -p %{buildroot}%{_iscsi_sbindir}
# create brcm_iscsiuio symlink if needed
[ -e %{buildroot}%{_iscsi_sbindir}/brcm_iscsiuio ] || \
    ln -s %{_iscsi_sbindir}/iscsiuio %{buildroot}%{_iscsi_sbindir}/brcm_iscsiuio
# create rc symlinks
ln -s %{_iscsi_sbindir}/service %{buildroot}%{_iscsi_sbindir}/rciscsi
ln -s %{_iscsi_sbindir}/service %{buildroot}%{_iscsi_sbindir}/rciscsid
ln -s %{_iscsi_sbindir}/service %{buildroot}%{_iscsi_sbindir}/rciscsiuio
ln -s %{_iscsi_sbindir}/service %{buildroot}%{_iscsi_sbindir}/rciscsi-init
(cd %{buildroot}/etc; ln -sf iscsi/iscsid.conf iscsid.conf)
# create an empty initiatorname file, as a package place holder
echo > %{buildroot}%{_home_dir}/initiatorname.iscsi
# rename iscsiuio logrotate file to proper name
%if 0%{?suse_version} > 1500
mkdir -p %{buildroot}%{_distconfdir}/logrotate.d
mv %{buildroot}%{_sysconfdir}/logrotate.d/iscsiuiolog %{buildroot}%{_distconfdir}/logrotate.d/iscsiuio
%else
mv %{buildroot}%{_sysconfdir}/logrotate.d/iscsiuiolog %{buildroot}%{_sysconfdir}/logrotate.d/iscsiuio
%endif
%fdupes %{buildroot}/%{_prefix}

%pre
%service_add_pre iscsi.service iscsid.service iscsid.socket iscsi-init.service

%post
%{?regenerate_initrd_post}
if [ ! -f %{_home_dir}/initiatorname.iscsi ] ; then
    %{_iscsi_sbindir}/iscsi-gen-initiatorname
fi
%if 0%{?_dbroot_new}
# move DB files if and only if not present in new location
for d in ifaces send_targets fw nodes static isns slp; do
    if [ -d %{_home_dir}/$d ]; then
	if [ -d %{_dbroot}/$d ]; then
	    echo "Warning: cannot copy DB directory %{_home_dir}/$d to %{_dbroot}/$d: already present" 1>&2
	else
	    cp -a %{_home_dir}/$d %{_dbroot}
	fi
    fi
done
%endif
%service_add_post iscsi.service iscsid.service iscsid.socket iscsi-init.service

%posttrans
%{?regenerate_initrd_posttrans}

%preun
%service_del_preun iscsi.service iscsid.service iscsid.socket iscsi-init.service

%postun
%service_del_postun_without_restart iscsi.service
%service_del_postun iscsi.service iscsid.service iscsid.socket iscsi-init.service

%post   -n %{libname} -p %{run_ldconfig}
%postun -n %{libname} -p %{run_ldconfig}

%post -n iscsiuio
%service_add_post iscsiuio.service iscsiuio.socket

%postun -n iscsiuio
%service_del_postun iscsiuio.service iscsiuio.socket

%pre -n iscsiuio
%service_add_pre iscsiuio.service iscsiuio.socket

%preun -n iscsiuio
%service_del_preun iscsiuio.service iscsiuio.socket

%files
%dir %{_home_dir}
%{_sysconfdir}/iscsid.conf
%attr(0600,root,root) %config(noreplace) %{_home_dir}/iscsid.conf
%ghost %{_home_dir}/initiatorname.iscsi
%if 0%{?_dbroot_new}
%config %{_home_dir}/README.DB-files-moved
%endif
%dir %{_dbroot}
%dir %{_dbroot}/ifaces
%{_dbroot}/ifaces/iface.example
%attr(0644,root,root) %{_unitdir}/iscsid.service
%attr(0644,root,root) %{_unitdir}/iscsid.socket
%attr(0644,root,root) %{_unitdir}/iscsi-init.service
%attr(0644,root,root) %{_unitdir}/iscsi.service
%{_systemdgeneratordir}/ibft-rule-generator
%{_iscsi_sbindir}/rciscsi
%{_iscsi_sbindir}/rciscsid
%{_iscsi_sbindir}/rciscsi-init
%{_iscsi_sbindir}/iscsid
%{_iscsi_sbindir}/iscsiadm
%{_iscsi_sbindir}/iscsi-iname
%{_iscsi_sbindir}/iscsistart
%{_iscsi_sbindir}/iscsi-gen-initiatorname
%{_iscsi_sbindir}/iscsi_offload
%{_iscsi_sbindir}/iscsi_discovery
%{_iscsi_sbindir}/iscsi_fw_login
%doc README
%license COPYING
%{_mandir}/man8/iscsiadm.8%{ext_man}
%{_mandir}/man8/iscsid.8%{ext_man}
%{_mandir}/man8/iscsi_discovery.8%{ext_man}
%{_mandir}/man8/iscsistart.8%{ext_man}
%{_mandir}/man8/iscsi-iname.8%{ext_man}
%{_mandir}/man8/iscsi_fw_login.8%{ext_man}
%{_mandir}/man8/iscsi-gen-initiatorname.8%{ext_man}
%{_udevrulesdir}/50-iscsi-firmware-login.rules

%files -n %{libname}
%{_libdir}/libopeniscsiusr.so.*

%files -n iscsiuio
%{_iscsi_sbindir}/iscsiuio
%{_iscsi_sbindir}/brcm_iscsiuio
%{_mandir}/man8/iscsiuio.8%{ext_man}
%if 0%{?suse_version} > 1500
%dir %{_distconfdir}/logrotate.d
%{_distconfdir}/logrotate.d/iscsiuio
%else
%config %{_sysconfdir}/logrotate.d/iscsiuio
%endif
%attr(0644,root,root) %{_unitdir}/iscsiuio.service
%attr(0644,root,root) %{_unitdir}/iscsiuio.socket
%{_iscsi_sbindir}/rciscsiuio

%files devel
%{_includedir}/libopeniscsiusr*.h
%{_mandir}/man3/*.3%{ext_man}
%{_libdir}/libopeniscsiusr.so
%{_libdir}/pkgconfig/*.pc

%changelog
