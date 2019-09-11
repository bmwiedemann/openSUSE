#
# spec file for package lvm2-clvm
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


%define _supportsanlock 0

%define dlm_version     3.99.1
%if 0%{_supportsanlock} == 1
%define sanlock_version 3.3.0
%endif

### COMMON-DEF-BEGIN ###
%define lvm2_version              2.02.180
%define device_mapper_version     1.02.149
%define thin_provisioning_version 0.7.0
### COMMON-DEF-END ###
Name:           lvm2-clvm
Version:        %{lvm2_version}
Release:        0
Summary:        Clustered LVM2
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Productivity/Clustering/HA
Url:            http://sources.redhat.com/cluster/clvm/
Source:         ftp://sources.redhat.com/pub/lvm2/LVM2.%{lvm2_version}.tgz
Source1:        ftp://sources.redhat.com/pub/lvm2/LVM2.%{lvm2_version}.tgz.asc
# To detect modprobe during build
BuildRequires:  kmod-compat
BuildRequires:  libaio-devel
BuildRequires:  libcorosync-devel
BuildRequires:  libdlm-devel >= %{dlm_version}
BuildRequires:  pkgconfig
%if 0%{_supportsanlock} == 1
BuildRequires:  sanlock-devel >= %{sanlock_version}
%endif
BuildRequires:  thin-provisioning-tools >= %{thin_provisioning_version}
BuildRequires:  pkgconfig(blkid)
BuildRequires:  pkgconfig(devmapper)
BuildRequires:  pkgconfig(libudev)
Requires:       corosync
Requires:       device-mapper >= %{device_mapper_version}
Requires:       lvm2 = %{version}
Requires:       lvm2-cmirrord
Obsoletes:      cmirrord < %{version}
Provides:       cmirrord = %{version}
### COMMON-PATCH-BEGIN ###
# Upstream patches
Patch0001:      bug-1114113_metadata-prevent-writing-beyond-metadata-area.patch
Patch0002:      bug-1122666_devices-drop-open-error-message.patch
Patch0003:      bug-1137296_pvremove-vgextend-fix-using-device-aliases-with-lvmetad.patch
Patch0004:      bug-1135984_cache-support-no_discard_passdown.patch

# SUSE patches: 1000+ for LVM
# Never upstream
Patch1001:      cmirrord_remove_date_time_from_compilation.patch
Patch1002:      fate-309425_display-dm-name-for-lv-name.patch
Patch1003:      fate-31841_fsadm-add-support-for-btrfs.patch
Patch1004:      bug-935623_dmeventd-fix-dso-name-wrong-compare.patch
Patch1005:      bsc1080299-detect-clvm-properly.patch
Patch1006:      bug-998893_make_pvscan_service_after_multipathd.patch

#SUSE patches 2000+ for device mapper, udev rules
Patch2001:      bug-1012973_simplify-special-case-for-md-in-69-dm-lvm-metadata.patch
### COMMON-PATCH-END ###

# Patches for clvmd and cmirrord
Patch3001:      bug-978055_clvmd-try-to-refresh-device-cache-on-the-first-failu.patch

%description
A daemon for using LVM2 Logival Volumes in a clustered environment.

%prep
%setup -q -n LVM2.%{lvm2_version}

### COMMON-PREP-BEGIN ###
%patch0001 -p1
%patch0002 -p1
%patch0003 -p1
%patch0004 -p1
%patch1001 -p1
%patch1002 -p1
%patch1003 -p1
%patch1004 -p1
%patch1005 -p1
%patch1006 -p1
%patch2001 -p1
### COMMON-PREP-END ###

%patch3001 -p1

%build
extra_opts="
    --enable-applib
    --enable-blkid_wiping
    --enable-cmdlib
    --enable-lvmetad
    --enable-lvmpolld
    --enable-realtime
    --with-default-locking-dir=/run/lock/lvm
    --with-default-pid-dir=/run
    --with-default-run-dir=/run/lvm
    --with-clvmd=corosync
    --with-cluster=internal
    --enable-cmirrord
    --enable-lvmlockd-dlm
%if 0%{_supportsanlock} == 1
    --enable-lvmlockd-sanlock
%endif
"

### COMMON-CONFIG-BEGIN ###
export PATH=$PATH:/sbin:%{_prefix}/sbin
# Why this messy fix here? someone released a wrong version...
sed -ie "s/%{device_mapper_version}/1.03.01/g" VERSION_DM
%configure \
    --enable-dmeventd \
    --enable-cmdlib \
    --enable-udev_rules \
    --enable-udev_sync \
    --with-udev-prefix="%{_prefix}/" \
    --enable-selinux \
    --enable-pkgconfig \
    --with-usrlibdir=%{_libdir} \
    --with-usrsbindir=%{_sbindir} \
    --with-default-dm-run-dir=/run \
    --with-tmpfilesdir=%{_tmpfilesdir} \
    --with-thin=internal \
    --with-device-gid=6 \
    --with-device-mode=0640 \
    --with-device-uid=0 \
    --with-dmeventd-path=%{_sbindir}/dmeventd \
    --with-thin-check=%{_sbindir}/thin_check \
    --with-thin-dump=%{_sbindir}/thin_dump \
    --with-thin-repair=%{_sbindir}/thin_repair \
    $extra_opts
### COMMON-CONFIG-END ###

%make_build

%install
make DESTDIR=%{buildroot} \
    install_cluster \
    install_systemd_units install_systemd_generators
make DESTDIR=%{buildroot} install -C daemons/lvmlockd
make DESTDIR=%{buildroot} install -C daemons/cmirrord

# lvmlockd does not have separate target install the mans by hand for now
install -m0644 -D man/lvmlockd.8 %{buildroot}%{_mandir}/man8/lvmlockd.8
install -m0644 -D man/lvmlockctl.8 %{buildroot}%{_mandir}/man8/lvmlockctl.8

# rc services symlinks
ln -s service %{buildroot}%{_sbindir}/rclvm2-cluster-activation
ln -s service %{buildroot}%{_sbindir}/rclvm2-clvmd
ln -s service %{buildroot}%{_sbindir}/rclvm2-cmirrord
ln -s service %{buildroot}%{_sbindir}/rclvm2-lvmlockd
ln -s service %{buildroot}%{_sbindir}/rclvm2-lvmlocking

# remove files from lvm2 split due to systemd_generators picking them up
rm %{buildroot}%{_unitdir}/blk-availability.service
rm %{buildroot}%{_unitdir}/dm-event.service
rm %{buildroot}%{_unitdir}/dm-event.socket
rm %{buildroot}%{_unitdir}/lvm2-monitor.service
rm %{buildroot}%{_mandir}/man8/lvm2-activation-generator.8
rm %{buildroot}%{_libexecdir}/systemd/system-generators/lvm2-activation-generator
rm %{buildroot}%{_unitdir}/lvm2-lvmetad.service
rm %{buildroot}%{_unitdir}/lvm2-lvmetad.socket
rm %{buildroot}%{_unitdir}/lvm2-lvmpolld.service
rm %{buildroot}%{_unitdir}/lvm2-lvmpolld.socket
rm %{buildroot}%{_unitdir}/lvm2-pvscan@.service

%files
%defattr(-,root,root)
%{_sbindir}/clvmd
%{_sbindir}/rclvm2-cluster-activation
%{_sbindir}/rclvm2-clvmd
%{_unitdir}/lvm2-clvmd.service
%{_unitdir}/lvm2-cluster-activation.service
%{_libexecdir}/systemd/lvm2-cluster-activation
%{_mandir}/man8/clvmd.8%{ext_man}

%package -n lvm2-cmirrord
Summary:        Clustered RAID 1 support using device-mapper and corosync
Group:          Productivity/Clustering/HA
Requires:       corosync
Requires:       device-mapper >= %{device_mapper_version}
Requires:       lvm2 = %{version}
Requires:       lvm2-clvm

%description -n lvm2-cmirrord
A daemon for using LVM2 Logival Volumes in a clustered environment.

%files -n lvm2-cmirrord
%defattr(-,root,root)
%{_sbindir}/cmirrord
%{_libexecdir}/systemd/system/lvm2-cmirrord.service
%{_sbindir}/rclvm2-cmirrord
%{_mandir}/man8/cmirrord.8%{ext_man}

%package -n lvm2-lockd
Summary:        LVM locking daemon
Group:          Productivity/Clustering/HA
Recommends:     libdlm >= %{dlm_version}
Requires:       lvm2 = %{version}
%if 0%{_supportsanlock} == 1
Requires:       sanlock >= %{sanlock_version}
%endif
%{?systemd_requires}

%description -n lvm2-lockd
LVM commands use lvmlockd to coordinate access to shared storage.

%pre -n lvm2-lockd
%service_add_pre lvm2-lvmlockd.service lvm2-lvmlocking.service

%post -n lvm2-lockd
%service_add_post lvm2-lvmlockd.service lvm2-lvmlocking.service

%preun -n lvm2-lockd
%service_del_preun lvm2-lvmlockd.service lvm2-lvmlocking.service

%postun -n lvm2-lockd
%service_del_postun lvm2-lvmlockd.service lvm2-lvmlocking.service

%files -n lvm2-lockd
%defattr(-,root,root,)
%{_sbindir}/lvmlockd
%{_sbindir}/lvmlockctl
%{_mandir}/man8/lvmlockd.8%{ext_man}
%{_mandir}/man8/lvmlockctl.8%{ext_man}
%{_unitdir}/lvm2-lvmlockd.service
%{_unitdir}/lvm2-lvmlocking.service
%{_sbindir}/rclvm2-lvmlockd
%{_sbindir}/rclvm2-lvmlocking

%changelog
