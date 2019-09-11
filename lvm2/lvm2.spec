#
# spec file for package lvm2
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


%define _unpackaged_files_terminate_build 0
%define _udevdir %(pkg-config --variable=udevdir udev)
%define applib liblvm2app2_2
%define cmdlib liblvm2cmd2_02

### COMMON-DEF-BEGIN ###
%define lvm2_version              2.02.180
%define device_mapper_version     1.02.149
%define thin_provisioning_version 0.7.0
### COMMON-DEF-END ###

Name:           lvm2
Version:        %{lvm2_version}
Release:        0
Summary:        Logical Volume Manager Tools
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          System/Base
Url:            http://www.sourceware.org/lvm2/
Source:         ftp://sources.redhat.com/pub/lvm2/LVM2.%{version}.tgz
Source1:        lvm.conf
Source42:       ftp://sources.redhat.com/pub/lvm2/LVM2.%{version}.tgz.asc
BuildRequires:  gcc-c++
BuildRequires:  libaio-devel
BuildRequires:  libcorosync-devel
BuildRequires:  libselinux-devel
# To detect modprobe during build
BuildRequires:  kmod-compat
BuildRequires:  pkgconfig
BuildRequires:  readline-devel
BuildRequires:  thin-provisioning-tools >= %{thin_provisioning_version}
BuildRequires:  pkgconfig(blkid)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(udev)
Requires:       device-mapper >= %{device_mapper_version}
Requires:       modutils
Requires(post): coreutils
Requires(postun): coreutils
Provides:       lvm = %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{?systemd_requires}

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

# 3000+ for test code
Patch3001:      bug-950089_test-fix-lvm2-testsuite-build-error.patch
Patch3002:      bug-1043040_test-fix-read-ahead-issues-in-test-scripts.patch
Patch3003:      bug-1072624_test-lvmetad_dump-always-timed-out-when-using-nc.patch
Patch3004:      tests-specify-python3-as-the-script-interpreter.patch

# patches specif for lvm2.spec
Patch4001:      bug-1037309_Makefile-skip-compliling-daemons-lvmlockd-directory.patch

%description
Programs and man pages for configuring and using the LVM2 Logical
Volume Manager.

%prep
%setup -q -n LVM2.%{version}
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
%patch3002 -p1
%patch3003 -p1
%patch3004 -p1
%patch4001 -p1

%build
extra_opts="
    --enable-applib
    --enable-blkid_wiping
    --enable-cmdlib
    --enable-lvmetad
    --enable-lvmpolld
    --enable-realtime
    --with-cache=internal
    --with-default-locking-dir=/run/lock/lvm
    --with-default-pid-dir=/run
    --with-default-run-dir=/run/lvm
    --enable-cmirrord
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
%make_install
make install_system_dirs DESTDIR=%{buildroot}
make install_systemd_units DESTDIR=%{buildroot}
make install_systemd_generators DESTDIR=%{buildroot}
make install_tmpfiles_configuration DESTDIR=%{buildroot}
# Install configuration file
install -m 644 %{SOURCE1} "%{buildroot}/%{_sysconfdir}/lvm/"
# Install testsuite
make -C test install DESTDIR=%{buildroot}

pushd "%{buildroot}/%{_libdir}"
ln -sf liblvm2cmd.so.2.02 liblvm2cmd.so
ln -sf liblvm2app.so.2.2 liblvm2app.so
for i in libdevmapper-event-lvm2{mirror,raid,snapshot,thin}; do
    ln -sf "device-mapper/$i.so" "$i.so"
    ln -sf "device-mapper/$i.so" "$i.so.2.02"
done
popd

#rc compat symlinks
ln -s service %{buildroot}%{_sbindir}/rcblk-availability
ln -s service %{buildroot}%{_sbindir}/rclvm2-lvmetad
ln -s service %{buildroot}%{_sbindir}/rclvm2-monitor
ln -s service %{buildroot}%{_sbindir}/rclvm2-lvmpolld

# Remove devicemapper binaries, plain rm so we fail if something change
rm %{buildroot}%{_sbindir}/dmsetup
rm %{buildroot}%{_sbindir}/dmeventd
rm %{buildroot}%{_sbindir}/dmstats
rm %{buildroot}%{_udevrulesdir}/10-dm.rules
rm %{buildroot}%{_udevrulesdir}/13-dm-disk.rules
rm %{buildroot}%{_udevrulesdir}/95-dm-notify.rules
rm %{buildroot}%{_unitdir}/dm-event.socket
rm %{buildroot}%{_unitdir}/dm-event.service
# See bsc#1037309 for more info
rm %{buildroot}%{_unitdir}/lvm2-lvmlockd.service
rm %{buildroot}%{_unitdir}/lvm2-lvmlocking.service
rm %{buildroot}%{_includedir}/libdevmapper*.h
rm %{buildroot}%{_libdir}/libdevmapper.so.*
rm %{buildroot}%{_libdir}/libdevmapper-event.so.*
rm %{buildroot}%{_libdir}/libdevmapper.so
rm %{buildroot}%{_libdir}/libdevmapper-event.so
rm %{buildroot}%{_libdir}/pkgconfig/devmapper*.pc
rm %{buildroot}%{_mandir}/man8/lvmlockctl.8
rm %{buildroot}%{_mandir}/man8/lvmlockd.8
rm %{buildroot}%{_mandir}/man8/dmstats.8
rm %{buildroot}%{_mandir}/man8/dmsetup.8
rm %{buildroot}%{_mandir}/man8/dmeventd.8

# compat symlinks in /sbin remove with Leap 43
mkdir -p %{buildroot}/sbin
pushd %{buildroot}/%{_sbindir}
for i in {vg,pv,lv}*; do
    ln -s %{_sbindir}/$i %{buildroot}/sbin/$i
done
popd

%pre
%service_add_pre blk-availability.service lvm2-monitor.service lvm2-lvmetad.socket lvm2-lvmetad.service lvm2-lvmpolld.service lvm2-lvmpolld.socket

%post
/sbin/ldconfig
%{?regenerate_initrd_post}
%service_add_post blk-availability.service lvm2-monitor.service lvm2-lvmetad.socket lvm2-lvmetad.service lvm2-lvmpolld.service lvm2-lvmpolld.socket
# Use %%tmpfiles_create when 13.2 is oldest in support scope
%{_bindir}/systemd-tmpfiles --create %{_tmpfilesdir}/lvm2.conf || :

%posttrans
%{?regenerate_initrd_posttrans}

%preun
%service_del_preun blk-availability.service lvm2-monitor.service lvm2-lvmetad.service lvm2-lvmpolld.service lvm2-lvmpolld.socket

%postun
/sbin/ldconfig
%{?regenerate_initrd_post}
%service_del_postun blk-availability.service lvm2-monitor.service lvm2-lvmetad.service lvm2-lvmpolld.service lvm2-lvmpolld.socket

%files
%defattr(-,root,root)
%doc README VERSION WHATS_NEW
%doc doc/lvm_fault_handling.txt
# Main binaries
%{_sbindir}/blkdeactivate
%{_sbindir}/fsadm
%{_sbindir}/lvm
%{_sbindir}/lvmconf
%{_sbindir}/lvmconfig
%{_sbindir}/lvmdump
%{_sbindir}/lvmetad
%{_sbindir}/lvmpolld
# Other files
%{_sbindir}/lvchange
%{_sbindir}/lvconvert
%{_sbindir}/lvcreate
%{_sbindir}/lvdisplay
%{_sbindir}/lvextend
%{_sbindir}/lvmdiskscan
%{_sbindir}/lvmsadc
%{_sbindir}/lvmsar
%{_sbindir}/lvreduce
%{_sbindir}/lvremove
%{_sbindir}/lvrename
%{_sbindir}/lvresize
%{_sbindir}/lvs
%{_sbindir}/lvscan
%{_sbindir}/pvchange
%{_sbindir}/pvck
%{_sbindir}/pvcreate
%{_sbindir}/pvdisplay
%{_sbindir}/pvmove
%{_sbindir}/pvremove
%{_sbindir}/pvresize
%{_sbindir}/pvs
%{_sbindir}/pvscan
%{_sbindir}/vgcfgbackup
%{_sbindir}/vgcfgrestore
%{_sbindir}/vgchange
%{_sbindir}/vgck
%{_sbindir}/vgconvert
%{_sbindir}/vgcreate
%{_sbindir}/vgdisplay
%{_sbindir}/vgexport
%{_sbindir}/vgextend
%{_sbindir}/vgimport
%{_sbindir}/vgimportclone
%{_sbindir}/vgmerge
%{_sbindir}/vgmknodes
%{_sbindir}/vgreduce
%{_sbindir}/vgremove
%{_sbindir}/vgrename
%{_sbindir}/vgs
%{_sbindir}/vgscan
%{_sbindir}/vgsplit
%{_sbindir}/rcblk-availability
%{_sbindir}/rclvm2-lvmetad
%{_sbindir}/rclvm2-lvmpolld
%{_sbindir}/rclvm2-monitor
# compat symlinks in /sbin
/sbin/lvm
/sbin/lvmconf
/sbin/lvmconfig
/sbin/lvmdump
/sbin/lvmetad
/sbin/lvmpolld
/sbin/lvchange
/sbin/lvconvert
/sbin/lvcreate
/sbin/lvdisplay
/sbin/lvextend
/sbin/lvmdiskscan
/sbin/lvmsadc
/sbin/lvmsar
/sbin/lvreduce
/sbin/lvremove
/sbin/lvrename
/sbin/lvresize
/sbin/lvs
/sbin/lvscan
/sbin/pvchange
/sbin/pvck
/sbin/pvcreate
/sbin/pvdisplay
/sbin/pvmove
/sbin/pvremove
/sbin/pvresize
/sbin/pvs
/sbin/pvscan
/sbin/vgcfgbackup
/sbin/vgcfgrestore
/sbin/vgchange
/sbin/vgck
/sbin/vgconvert
/sbin/vgcreate
/sbin/vgdisplay
/sbin/vgexport
/sbin/vgextend
/sbin/vgimport
/sbin/vgimportclone
/sbin/vgmerge
/sbin/vgmknodes
/sbin/vgreduce
/sbin/vgremove
/sbin/vgrename
/sbin/vgs
/sbin/vgscan
/sbin/vgsplit
%{_mandir}/man5/lvm.conf.5%{ext_man}
%{_mandir}/man7/lvmcache.7%{ext_man}
%{_mandir}/man7/lvmraid.7%{ext_man}
%{_mandir}/man7/lvmreport.7%{ext_man}
%{_mandir}/man7/lvmthin.7%{ext_man}
%{_mandir}/man7/lvmsystemid.7%{ext_man}
%{_mandir}/man8/fsadm.8%{ext_man}
%{_mandir}/man8/lvchange.8%{ext_man}
%{_mandir}/man8/lvconvert.8%{ext_man}
%{_mandir}/man8/lvcreate.8%{ext_man}
%{_mandir}/man8/lvdisplay.8%{ext_man}
%{_mandir}/man8/lvextend.8%{ext_man}
%{_mandir}/man8/lvm.8%{ext_man}
%{_mandir}/man8/lvm2-activation-generator.8%{ext_man}
%{_mandir}/man8/lvm-config.8%{ext_man}
%{_mandir}/man8/lvmconfig.8%{ext_man}
%{_mandir}/man8/lvm-dumpconfig.8%{ext_man}
%{_mandir}/man8/lvmconf.8%{ext_man}
%{_mandir}/man8/lvmdiskscan.8%{ext_man}
%{_mandir}/man8/lvmdump.8%{ext_man}
%{_mandir}/man8/lvm-fullreport.8%{ext_man}
%{_mandir}/man8/lvmsadc.8%{ext_man}
%{_mandir}/man8/lvmsar.8%{ext_man}
%{_mandir}/man8/lvreduce.8%{ext_man}
%{_mandir}/man8/lvremove.8%{ext_man}
%{_mandir}/man8/lvrename.8%{ext_man}
%{_mandir}/man8/lvresize.8%{ext_man}
%{_mandir}/man8/lvs.8%{ext_man}
%{_mandir}/man8/lvscan.8%{ext_man}
%{_mandir}/man8/pvchange.8%{ext_man}
%{_mandir}/man8/pvck.8%{ext_man}
%{_mandir}/man8/pvcreate.8%{ext_man}
%{_mandir}/man8/pvdisplay.8%{ext_man}
%{_mandir}/man8/pvmove.8%{ext_man}
%{_mandir}/man8/pvremove.8%{ext_man}
%{_mandir}/man8/pvresize.8%{ext_man}
%{_mandir}/man8/pvs.8%{ext_man}
%{_mandir}/man8/pvscan.8%{ext_man}
%{_mandir}/man8/vgcfgbackup.8%{ext_man}
%{_mandir}/man8/vgcfgrestore.8%{ext_man}
%{_mandir}/man8/vgchange.8%{ext_man}
%{_mandir}/man8/vgck.8%{ext_man}
%{_mandir}/man8/vgconvert.8%{ext_man}
%{_mandir}/man8/vgcreate.8%{ext_man}
%{_mandir}/man8/vgdisplay.8%{ext_man}
%{_mandir}/man8/vgexport.8%{ext_man}
%{_mandir}/man8/vgextend.8%{ext_man}
%{_mandir}/man8/vgimport.8%{ext_man}
%{_mandir}/man8/vgimportclone.8%{ext_man}
%{_mandir}/man8/vgmerge.8%{ext_man}
%{_mandir}/man8/vgmknodes.8%{ext_man}
%{_mandir}/man8/vgreduce.8%{ext_man}
%{_mandir}/man8/vgremove.8%{ext_man}
%{_mandir}/man8/vgrename.8%{ext_man}
%{_mandir}/man8/vgs.8%{ext_man}
%{_mandir}/man8/vgscan.8%{ext_man}
%{_mandir}/man8/vgsplit.8%{ext_man}
%{_mandir}/man8/lvmetad.8%{ext_man}
%{_mandir}/man8/blkdeactivate.8%{ext_man}
%{_mandir}/man8/lvmpolld.8%{ext_man}
%{_mandir}/man8/lvm-lvpoll.8%{ext_man}
%{_udevdir}/rules.d/11-dm-lvm.rules
%{_udevdir}/rules.d/69-dm-lvm-metad.rules
%dir %{_sysconfdir}/lvm
%config(noreplace) %{_sysconfdir}/lvm/lvm.conf
%config(noreplace) %{_sysconfdir}/lvm/lvmlocal.conf
%dir %{_sysconfdir}/lvm/profile
%{_sysconfdir}/lvm/profile/command_profile_template.profile
%{_sysconfdir}/lvm/profile/metadata_profile_template.profile
%{_sysconfdir}/lvm/profile/thin-generic.profile
%{_sysconfdir}/lvm/profile/thin-performance.profile
%{_sysconfdir}/lvm/profile/cache-mq.profile
%{_sysconfdir}/lvm/profile/cache-smq.profile
%{_sysconfdir}/lvm/profile/lvmdbusd.profile
%dir %{_sysconfdir}/lvm/cache
%ghost %{_sysconfdir}/lvm/cache/.cache
%dir %{_sysconfdir}/lvm/archive
%dir %{_sysconfdir}/lvm/backup
%{_tmpfilesdir}/%{name}.conf
%{_unitdir}/blk-availability.service
%{_unitdir}/lvm2-monitor.service
%{_unitdir}/lvm2-lvmetad.socket
%{_unitdir}/lvm2-lvmetad.service
%{_unitdir}/lvm2-pvscan@.service
%{_unitdir}/lvm2-lvmpolld.socket
%{_unitdir}/lvm2-lvmpolld.service
%{_libexecdir}/systemd/system-generators/lvm2-activation-generator
%dir %{_libdir}/device-mapper
%{_libdir}/device-mapper/libdevmapper-event-lvm2*.so
%{_libdir}/libdevmapper-event-lvm2*.so
%{_libdir}/libdevmapper-event-lvm2*.so.2.02

%package -n %{applib}
Summary:        LVM2 application api library
Group:          System/Libraries
Conflicts:      %{name} < %{version}

%description -n %{applib}
LVM library for applications api

%post -n %{applib} -p /sbin/ldconfig
%postun -n %{applib} -p /sbin/ldconfig

%files -n %{applib}
%defattr(-,root,root)
%{_libdir}/liblvm2app.so.*

%package -n %{cmdlib}
Summary:        LVM2 command line library
Group:          System/Libraries
Conflicts:      %{name} < %{version}

%description -n %{cmdlib}
The lvm2 command line library allows building programs that manage
lvm devices without invoking a separate program.

%post -n %{cmdlib} -p /sbin/ldconfig
%postun -n %{cmdlib} -p /sbin/ldconfig

%files -n %{cmdlib}
%defattr(-,root,root)
%{_libdir}/liblvm2cmd.so.*

%package devel
Summary:        Development files for LVM2
Group:          Development/Libraries/C and C++
Requires:       %{applib} = %{version}
Requires:       %{cmdlib} = %{version}
Requires:       device-mapper-devel
Requires:       lvm2 = %{version}

%description devel
This package provides development files for the LVM2 Logical Volume Manager.

%files devel
%defattr(-,root,root)
%{_includedir}/lvm2cmd.h
%{_includedir}/lvm2app.h
%{_libdir}/pkgconfig/lvm2app.pc
%{_libdir}/liblvm2app.so
%{_libdir}/liblvm2cmd.so

%package testsuite
Summary:        LVM2 Testsuite
Group:          Development/Libraries/C and C++
Requires:       %{applib} = %{version}
Requires:       %{cmdlib} = %{version}
Requires:       lvm2 = %{version}

%description testsuite
An extensive functional testsuite for the LVM2 Logical Volume Manager.

%files testsuite
%defattr(-,root,root)
%{_datarootdir}/lvm2-testsuite/
%{_libexecdir}/lvm2-testsuite/
%{_bindir}/lvm2-testsuite

%changelog
