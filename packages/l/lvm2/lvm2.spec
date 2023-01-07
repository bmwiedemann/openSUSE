#
# spec file
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


%define _unpackaged_files_terminate_build 0
%define libname libdevmapper1_03
%define libname_event libdevmapper-event1_03
%define _udevdir %(pkg-config --variable=udevdir udev)
%define cmdlib liblvm2cmd2_03
%define lvm2_version              2.03.16
# For device_mapper_version, it's package version, see bsc#1199074.
# Also note there is another dm version on below "sed -ie ... VERSION_DM".
%define upstream_device_mapper_version  1.02.185
%define device_mapper_version           %{lvm2_version}_1.02.185
%define thin_provisioning_version 0.7.0
%define _supportsanlock 1
%define dlm_version     4.0.9
# from lvm2 version 2.03, suse obsoleted clvm, cmirrord, liblvm2app & liblvm2cmd.
# so the obseletes version is 2.03
%define lvm2_clvm_version 2.03
%define lvm2_cmirrord_version 2.03
%define liblvm2app2_2_version 2.03
%define liblvm2cmd2_02_version 2.03

%if 0%{_supportsanlock} == 1
  %define sanlock_version 3.3.0
%endif

%global flavor @BUILD_FLAVOR@%{nil}
%define psuffix %{nil}

%if "%{flavor}" == "devicemapper"
  %define psuffix -device-mapper
  %bcond_without devicemapper
%else
  %bcond_with devicemapper
%endif

%if "%{flavor}" == "lockd"
  %define psuffix -lvmlockd
  %bcond_without lockd
%else
  %bcond_with lockd
%endif

Name:           lvm2%{psuffix}
Version:        %{lvm2_version}
Release:        0
Summary:        Logical Volume Manager Tools
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          System/Base
URL:            https://www.sourceware.org/lvm2/
Source:         ftp://sourceware.org/pub/lvm2/LVM2.%{version}.tgz
Source1:        lvm.conf
Source2:        lvm2-rpmlintrc
Source42:       ftp://sourceware.org/pub/lvm2/LVM2.%{version}.tgz.asc
Source99:       baselibs.conf

# Upstream patches
Patch0001:      0001-devices-file-move-clean-up-after-command-is-run.patch
Patch0002:      0002-devices-file-fail-if-devicesfile-filename-doesn-t-ex.patch
Patch0003:      0003-filter-mpath-handle-other-wwid-types-in-blacklist.patch
Patch0004:      0004-filter-mpath-get-wwids-from-sysfs-vpd_pg83.patch
Patch0005:      0005-pvdisplay-restore-reportformat-option.patch
Patch0006:      0006-exit-with-error-when-devicesfile-name-doesn-t-exist.patch
Patch0007:      0007-report-fix-pe_start-column-type-from-NUM-to-SIZ.patch
Patch0008:      0008-_vg_read_raw_area-fix-segfault-caused-by-using-null-.patch
Patch0009:      0009-mm-remove-libaio-from-being-skipped.patch
Patch0010:      0010-dmsetup-check-also-for-ouf-of-range-value.patch
Patch0011:      0011-devices-drop-double-from-sysfs-path.patch
Patch0012:      0012-devices-file-fix-pvcreate-uuid-matching-pvid-entry-w.patch
Patch0013:      0013-vgimportdevices-change-result-when-devices-are-not-a.patch
Patch0014:      0014-vgimportdevices-fix-locking-when-creating-devices-fi.patch
Patch0015:      bug-1203216_lvmlockd-purge-the-lock-resources-left-in-previous-l.patch
# SUSE patches: 1000+ for LVM
# Never upstream
Patch1001:      cmirrord_remove_date_time_from_compilation.patch
Patch1002:      fate-309425_display-dm-name-for-lv-name.patch
Patch1003:      bug-935623_dmeventd-fix-dso-name-wrong-compare.patch
Patch1004:      bug-998893_make_pvscan_service_after_multipathd.patch
Patch1005:      bug-1184687_Add-nolvm-for-kernel-cmdline.patch
Patch1006:      fate-31841-01_fsadm-add-support-to-resize-check-btrfs-filesystem.patch
Patch1007:      fate-31841-02_man-add-support-for-btrfs.patch
Patch1008:      fate-31841-03_tests-new-test-suite-of-fsadm-for-btrfs.patch
# SUSE patches 2000+ for device mapper, udev rules
Patch2001:      bug-1012973_simplify-special-case-for-md-in-69-dm-lvm-metadata.patch
# SUSE patches 3000+ for test code
Patch3001:      bug-1184124-link-tests-as-PIE.patch
# SUSE patches 4000+ for lvm2.spec
Patch4001:      bug-1037309_Makefile-skip-compliling-daemons-lvmlockd-directory.patch
# To detect modprobe during build
BuildRequires:  kmod-compat
BuildRequires:  libaio-devel
BuildRequires:  pkgconfig
BuildRequires:  thin-provisioning-tools >= %{thin_provisioning_version}
BuildRequires:  pkgconfig(libudev)
Requires:       device-mapper >= %{device_mapper_version}
Requires:       modutils
Requires(post): coreutils
Requires(postun):coreutils
Provides:       lvm = %{version}
Obsoletes:      lvm2-cmirrord <= %{lvm2_cmirrord_version}
%{?systemd_requires}

%if %{with devicemapper}
BuildRequires:  gcc-c++
BuildRequires:  suse-module-tools
BuildRequires:  pkgconfig(libselinux)
BuildRequires:  pkgconfig(libsepol)
BuildRequires:  pkgconfig(systemd)
%else
BuildRequires:  libcorosync-devel
BuildRequires:  pkgconfig(blkid)
%if %{with lockd}
BuildRequires:  libdlm-devel >= %{dlm_version}
BuildRequires:  pkgconfig(libsystemd)
%if 0%{_supportsanlock} == 1
BuildRequires:  sanlock-devel >= %{sanlock_version}
%endif
%else
BuildRequires:  gcc-c++
BuildRequires:  libselinux-devel
BuildRequires:  readline-devel
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(udev)
%endif
%endif

%description
Programs and man pages for configuring and using the LVM2 Logical
Volume Manager.

%prep
%setup -q -n LVM2.%{version}
%patch0001 -p1
%patch0002 -p1
%patch0003 -p1
%patch0004 -p1
%patch0005 -p1
%patch0006 -p1
%patch0007 -p1
%patch0008 -p1
%patch0009 -p1
%patch0010 -p1
%patch0011 -p1
%patch0012 -p1
%patch0013 -p1
%patch0014 -p1
%patch0015 -p1
%patch1001 -p1
%patch1002 -p1
%patch1003 -p1
%patch1004 -p1
%patch1005 -p1
%patch1006 -p1
%patch1007 -p1
%patch1008 -p1
%patch2001 -p1
%patch3001 -p1

%if !%{with lockd}
%patch4001 -p1
%endif

%build
%if !%{with devicemapper} && !%{with lockd}
extra_opts="
    --enable-blkid_wiping
    --with-cache=internal
    --with-writecache=internal
    --with-integrity=internal
    --with-default-locking-dir=/run/lock/lvm
    --with-default-pid-dir=/run
    --with-default-run-dir=/run/lvm
    --enable-fsadm
    --enable-write_install
    --with-vdo=internal
    --with-vdo-format=%{_bindir}/vdoformat
"
%endif

%if %{with lockd}
extra_opts="
    --enable-blkid_wiping
    --with-default-locking-dir=/run/lock/lvm
    --with-default-pid-dir=/run
    --with-default-run-dir=/run/lvm
    --with-cluster=internal
    --enable-lvmlockd-dlm
    --enable-lvmlockd-dlmcontrol
%if 0%{_supportsanlock} == 1
    --enable-lvmlockd-sanlock
%endif
"
%endif

### COMMON-CONFIG-BEGIN ###
export PATH=$PATH:/sbin:%{_sbindir}
# Why this messy fix here? someone released a wrong version...
# There will change library version to 1.03.01, see output "dmsetup --version".
sed -ie "s/%{upstream_device_mapper_version}/1.03.01/g" VERSION_DM
%configure \
    --enable-dmeventd \
    --enable-dmfilemapd \
    --enable-lvmpolld \
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
    --disable-silent-rules \
    $extra_opts
### COMMON-CONFIG-END ###

%if %{with devicemapper}
  %make_build device-mapper
%else
  %make_build
%endif

%install
%if %{with devicemapper}
  make DESTDIR=%{buildroot} \
      install_device-mapper \
      install_systemd_units

  ln -s service %{buildroot}/%{_sbindir}/rcdm-event

  # provide 1.02 compat links for the shared libraries
  # this is needed for various binary packages
  ln -s libdevmapper.so.1.03 %{buildroot}/%{_libdir}/libdevmapper.so.1.02
  ln -s libdevmapper-event.so.1.03 %{buildroot}/%{_libdir}/libdevmapper-event.so.1.02

  # remove blkd, will be in lvm2 proper
  # without force on purpose to detect changes and fail if it happens
  rm %{buildroot}%{_sbindir}/blkdeactivate
  rm %{buildroot}%{_unitdir}/blk-availability.service
  rm %{buildroot}%{_unitdir}/lvm2-monitor.service
  rm %{buildroot}%{_mandir}/man8/blkdeactivate.8

  # remove files, which will be in lvm2 & lockd packages
  rm %{buildroot}%{_unitdir}/lvm2-lvmpolld.service
  rm %{buildroot}%{_unitdir}/lvm2-lvmpolld.socket
  rm %{buildroot}%{_unitdir}/lvmlockd.service
  rm %{buildroot}%{_unitdir}/lvmlocks.service

  # compat symlinks in /sbin remove with Leap 43
  %if 0%{?suse_version} < 1550
  mkdir -p %{buildroot}/sbin
  ln -s %{_sbindir}/dmsetup %{buildroot}/sbin/dmsetup
  %endif

%else

  %if %{with lockd}
    make DESTDIR=%{buildroot} \
        install_systemd_units install_systemd_generators
    make DESTDIR=%{buildroot} install -C daemons/lvmlockd

    # lvmlockd does not have separate target install the mans by hand for now
    install -m0644 -D man/lvmlockd.8 %{buildroot}%{_mandir}/man8/lvmlockd.8
    install -m0644 -D man/lvmlockctl.8 %{buildroot}%{_mandir}/man8/lvmlockctl.8

    # rc services symlinks
    ln -s service %{buildroot}%{_sbindir}/rclvm2-lvmlockd
    ln -s service %{buildroot}%{_sbindir}/rclvm2-lvmlocking

    # remove files from lvm2 split due to systemd_generators picking them up
    rm %{buildroot}%{_unitdir}/blk-availability.service
    rm %{buildroot}%{_unitdir}/dm-event.service
    rm %{buildroot}%{_unitdir}/dm-event.socket
    rm %{buildroot}%{_unitdir}/lvm2-monitor.service
    rm %{buildroot}%{_unitdir}/lvm2-lvmpolld.service
    rm %{buildroot}%{_unitdir}/lvm2-lvmpolld.socket
  %else
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
    ln -sf liblvm2cmd.so.2.03 liblvm2cmd.so
    for i in libdevmapper-event-lvm2{mirror,raid,snapshot,thin}; do
        ln -sf "device-mapper/$i.so" "$i.so"
        ln -sf "device-mapper/$i.so" "$i.so.2.03"
    done
    popd

    #rc compat symlinks
    ln -s service %{buildroot}%{_sbindir}/rcblk-availability
    ln -s service %{buildroot}%{_sbindir}/rclvm2-monitor
    ln -s service %{buildroot}%{_sbindir}/rclvm2-lvmpolld

    # Remove devicemapper binaries, plain rm so we fail if something change
    rm %{buildroot}%{_sbindir}/dmsetup
    rm %{buildroot}%{_sbindir}/dmeventd
    rm %{buildroot}%{_sbindir}/dmstats
    rm %{buildroot}%{_sbindir}/dmfilemapd
    rm %{buildroot}%{_udevrulesdir}/10-dm.rules
    rm %{buildroot}%{_udevrulesdir}/13-dm-disk.rules
    rm %{buildroot}%{_udevrulesdir}/95-dm-notify.rules
    rm %{buildroot}%{_unitdir}/dm-event.socket
    rm %{buildroot}%{_unitdir}/dm-event.service
    # See bsc#1037309 for more info
    rm %{buildroot}%{_unitdir}/lvmlockd.service
    rm %{buildroot}%{_unitdir}/lvmlocks.service
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
    rm %{buildroot}%{_mandir}/man8/dmfilemapd.8

    %if 0%{?suse_version} < 1550
      # compat symlinks in /sbin remove with Leap 43
      mkdir -p %{buildroot}/sbin
      pushd %{buildroot}/%{_sbindir}
      for i in {vg,pv,lv}*; do
          ln -s %{_sbindir}/$i %{buildroot}/sbin/$i
      done
      popd
    %endif

  %endif
%endif

%if %{with devicemapper}
%package -n device-mapper
Version:        %{device_mapper_version}
Release:        0
Summary:        Device Mapper Tools
Group:          System/Base
Requires:       thin-provisioning-tools >= %{thin_provisioning_version}
Requires(post): coreutils

%description -n device-mapper
Programs and man pages for configuring and using the device mapper.

%pre -n device-mapper
%service_add_pre dm-event.service dm-event.socket

%post -n device-mapper
%service_add_post dm-event.service dm-event.socket
%{?regenerate_initrd_post}

%posttrans -n device-mapper
%{?regenerate_initrd_posttrans}

%preun -n device-mapper
%service_del_preun dm-event.service dm-event.socket

%postun -n device-mapper
%service_del_postun dm-event.service dm-event.socket
%{?regenerate_initrd_post}

%files -n device-mapper
%license COPYING COPYING.LIB
%doc README
%doc udev/12-dm-permissions.rules
%if 0%{?suse_version} < 1550
/sbin/dmsetup
%endif
%{_sbindir}/dmsetup
%{_sbindir}/dmeventd
%{_sbindir}/dmstats
%{_sbindir}/dmfilemapd
%{_mandir}/man8/dmstats.8%{?ext_man}
%{_mandir}/man8/dmsetup.8%{?ext_man}
%{_mandir}/man8/dmeventd.8%{?ext_man}
%{_mandir}/man8/dmfilemapd.8%{?ext_man}
%{_udevrulesdir}/10-dm.rules
%{_udevrulesdir}/13-dm-disk.rules
%{_udevrulesdir}/95-dm-notify.rules
%{_unitdir}/dm-event.socket
%{_sbindir}/rcdm-event
%{_unitdir}/dm-event.service

%package -n %{libname}
Version:        %{device_mapper_version}
Release:        0
Summary:        Library for device-mapper
Group:          System/Libraries
Conflicts:      %{name} < %{version}

%description -n %{libname}
Device mapper main shared library

%files -n %{libname}
%{_libdir}/libdevmapper.so.1.03
%{_libdir}/libdevmapper.so.1.02

%post   -n %{libname}
%if 0%{?suse_version} < 1550
# in usrmerged scenario we better don't remove ourselves :-)
if [ -f /%{_lib}/libdevmapper.so.1.03 ]; then
  # Special migration - the library is now in %{_libdir}, but up to the point where
  # zypp removes the 'old' device-mapper package, the old library 'wins' the ldloader race
  # resulting in binaries asking for the newer version still getting the old one.
  # This in turn results in funny bugs like boo#1045396
  # Remove /%{_lib}/libdevmapper.so.1.02 - and the run ldconfig
  rm /%{_lib}/libdevmapper.so.1.03
fi
%endif
/sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%package -n %{libname_event}
Version:        %{device_mapper_version}
Release:        0
Summary:        Event library for device-mapper
Group:          System/Libraries
Conflicts:      %{name} < %{version}

%description -n %{libname_event}
Device mapper event daemon shared library

%files -n %{libname_event}
%{_libdir}/libdevmapper-event.so.1.03
%{_libdir}/libdevmapper-event.so.1.02

%post -n %{libname_event} -p /sbin/ldconfig
%postun -n %{libname_event} -p /sbin/ldconfig

%package -n device-mapper-devel
Version:        %{device_mapper_version}
Release:        0
Summary:        Development package for the device mapper
Group:          Development/Libraries/C and C++
Requires:       %{libname_event} = %{device_mapper_version}
Requires:       %{libname} = %{device_mapper_version}
Requires:       device-mapper = %{device_mapper_version}

%description -n device-mapper-devel
Files needed for software development using the device mapper

%files -n device-mapper-devel
%{_libdir}/libdevmapper.so
%{_libdir}/libdevmapper-event.so
%{_includedir}/libdevmapper.h
%{_includedir}/libdevmapper-event.h
%{_libdir}/pkgconfig/devmapper.pc
%{_libdir}/pkgconfig/devmapper-event.pc

%else
%if %{with lockd}
%package -n lvm2-lockd
Summary:        LVM locking daemon
Group:          System/Base
Requires:       corosync
Requires:       device-mapper >= %{device_mapper_version}
Requires:       libdlm >= %{dlm_version}
Requires:       lvm2 = %{version}
Obsoletes:      lvm2-clvm <= %{lvm2_clvm_version}
%{?systemd_requires}
%if 0%{_supportsanlock} == 1
Requires:       sanlock >= %{sanlock_version}
%endif

%description -n lvm2-lockd
LVM commands use lvmlockd to coordinate access to shared storage.

%pre -n lvm2-lockd
%service_add_pre lvmlockd.service lvmlocks.service

%post -n lvm2-lockd
%service_add_post lvmlockd.service lvmlocks.service

%preun -n lvm2-lockd
%service_del_preun lvmlockd.service lvmlocks.service

%postun -n lvm2-lockd
%service_del_postun lvmlockd.service lvmlocks.service

%files -n lvm2-lockd
%defattr(-,root,root,)
%{_sbindir}/lvmlockd
%{_sbindir}/lvmlockctl
%{_mandir}/man8/lvmlockd.8%{?ext_man}
%{_mandir}/man8/lvmlockctl.8%{?ext_man}
%{_unitdir}/lvmlockd.service
%{_unitdir}/lvmlocks.service
%{_sbindir}/rclvm2-lvmlockd
%{_sbindir}/rclvm2-lvmlocking

%else

%pre
%service_add_pre blk-availability.service lvm2-monitor.service lvm2-lvmpolld.service lvm2-lvmpolld.socket

%post
/sbin/ldconfig
%{?regenerate_initrd_post}
%service_add_post blk-availability.service lvm2-monitor.service lvm2-lvmpolld.service lvm2-lvmpolld.socket
# Use %%tmpfiles_create when 13.2 is oldest in support scope
%{_bindir}/systemd-tmpfiles --create %{_tmpfilesdir}/lvm2.conf || :

%posttrans
%{?regenerate_initrd_posttrans}

%preun
%service_del_preun blk-availability.service lvm2-monitor.service lvm2-lvmpolld.service lvm2-lvmpolld.socket

%postun
/sbin/ldconfig
%{?regenerate_initrd_post}
%service_del_postun lvm2-lvmpolld.service lvm2-lvmpolld.socket
%service_del_postun_without_restart blk-availability.service lvm2-monitor.service

%files
%license COPYING COPYING.LIB
%doc README VERSION WHATS_NEW
%doc doc/lvm_fault_handling.txt

# Main binaries
%{_sbindir}/blkdeactivate
%{_sbindir}/fsadm
%{_sbindir}/lvm
%{_sbindir}/lvmconfig
%{_sbindir}/lvmdevices
%{_sbindir}/lvmdump
%{_sbindir}/lvmpolld
%{_sbindir}/lvm_import_vdo
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
%{_sbindir}/vgimportdevices
%{_sbindir}/vgmerge
%{_sbindir}/vgmknodes
%{_sbindir}/vgreduce
%{_sbindir}/vgremove
%{_sbindir}/vgrename
%{_sbindir}/vgs
%{_sbindir}/vgscan
%{_sbindir}/vgsplit
%{_sbindir}/rcblk-availability
%{_sbindir}/rclvm2-lvmpolld
%{_sbindir}/rclvm2-monitor
# compat symlinks in /sbin
%if 0%{?suse_version} < 1550
/sbin/lvm
/sbin/lvmconfig
/sbin/lvmdevices
/sbin/lvmdump
/sbin/lvmpolld
/sbin/lvm_import_vdo
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
/sbin/vgimportdevices
/sbin/vgmerge
/sbin/vgmknodes
/sbin/vgreduce
/sbin/vgremove
/sbin/vgrename
/sbin/vgs
/sbin/vgscan
/sbin/vgsplit
%endif
%{_mandir}/man5/lvm.conf.5%{?ext_man}
%{_mandir}/man7/lvmautoactivation.7%{?ext_man}
%{_mandir}/man7/lvmcache.7%{?ext_man}
%{_mandir}/man7/lvmraid.7%{?ext_man}
%{_mandir}/man7/lvmreport.7%{?ext_man}
%{_mandir}/man7/lvmthin.7%{?ext_man}
%{_mandir}/man7/lvmsystemid.7%{?ext_man}
%{_mandir}/man7/lvmvdo.7%{?ext_man}
%{_mandir}/man8/fsadm.8%{?ext_man}
%{_mandir}/man8/lvchange.8%{?ext_man}
%{_mandir}/man8/lvconvert.8%{?ext_man}
%{_mandir}/man8/lvcreate.8%{?ext_man}
%{_mandir}/man8/lvdisplay.8%{?ext_man}
%{_mandir}/man8/lvextend.8%{?ext_man}
%{_mandir}/man8/lvm.8%{?ext_man}
%{_mandir}/man8/lvm-config.8%{?ext_man}
%{_mandir}/man8/lvmconfig.8%{?ext_man}
%{_mandir}/man8/lvmdevices.8%{?ext_man}
%{_mandir}/man8/lvm-dumpconfig.8%{?ext_man}
%{_mandir}/man8/lvmdiskscan.8%{?ext_man}
%{_mandir}/man8/lvmdump.8%{?ext_man}
%{_mandir}/man8/lvm-fullreport.8%{?ext_man}
%{_mandir}/man8/lvmsadc.8%{?ext_man}
%{_mandir}/man8/lvmsar.8%{?ext_man}
%{_mandir}/man8/lvreduce.8%{?ext_man}
%{_mandir}/man8/lvremove.8%{?ext_man}
%{_mandir}/man8/lvrename.8%{?ext_man}
%{_mandir}/man8/lvresize.8%{?ext_man}
%{_mandir}/man8/lvs.8%{?ext_man}
%{_mandir}/man8/lvscan.8%{?ext_man}
%{_mandir}/man8/pvchange.8%{?ext_man}
%{_mandir}/man8/pvck.8%{?ext_man}
%{_mandir}/man8/pvcreate.8%{?ext_man}
%{_mandir}/man8/pvdisplay.8%{?ext_man}
%{_mandir}/man8/pvmove.8%{?ext_man}
%{_mandir}/man8/pvremove.8%{?ext_man}
%{_mandir}/man8/pvresize.8%{?ext_man}
%{_mandir}/man8/pvs.8%{?ext_man}
%{_mandir}/man8/pvscan.8%{?ext_man}
%{_mandir}/man8/vgcfgbackup.8%{?ext_man}
%{_mandir}/man8/vgcfgrestore.8%{?ext_man}
%{_mandir}/man8/vgchange.8%{?ext_man}
%{_mandir}/man8/vgck.8%{?ext_man}
%{_mandir}/man8/vgconvert.8%{?ext_man}
%{_mandir}/man8/vgcreate.8%{?ext_man}
%{_mandir}/man8/vgdisplay.8%{?ext_man}
%{_mandir}/man8/vgexport.8%{?ext_man}
%{_mandir}/man8/vgextend.8%{?ext_man}
%{_mandir}/man8/vgimport.8%{?ext_man}
%{_mandir}/man8/vgimportclone.8%{?ext_man}
%{_mandir}/man8/vgimportdevices.8%{?ext_man}
%{_mandir}/man8/vgmerge.8%{?ext_man}
%{_mandir}/man8/vgmknodes.8%{?ext_man}
%{_mandir}/man8/vgreduce.8%{?ext_man}
%{_mandir}/man8/vgremove.8%{?ext_man}
%{_mandir}/man8/vgrename.8%{?ext_man}
%{_mandir}/man8/vgs.8%{?ext_man}
%{_mandir}/man8/vgscan.8%{?ext_man}
%{_mandir}/man8/vgsplit.8%{?ext_man}
%{_mandir}/man8/blkdeactivate.8%{?ext_man}
%{_mandir}/man8/lvmpolld.8%{?ext_man}
%{_mandir}/man8/lvm-lvpoll.8%{?ext_man}
%{_mandir}/man8/lvm_import_vdo.8%{?ext_man}
%{_udevdir}/rules.d/11-dm-lvm.rules
%{_udevdir}/rules.d/69-dm-lvm.rules
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
%{_sysconfdir}/lvm/profile/vdo-small.profile
%dir %{_sysconfdir}/lvm/cache
%ghost %{_sysconfdir}/lvm/cache/.cache
%dir %{_sysconfdir}/lvm/archive
%dir %{_sysconfdir}/lvm/backup
%{_tmpfilesdir}/%{name}.conf
%{_unitdir}/blk-availability.service
%{_unitdir}/lvm2-monitor.service
%{_unitdir}/lvm2-lvmpolld.socket
%{_unitdir}/lvm2-lvmpolld.service
%dir %{_libdir}/device-mapper
%{_libdir}/device-mapper/libdevmapper-event-lvm2*.so
%{_libdir}/libdevmapper-event-lvm2*.so
%{_libdir}/libdevmapper-event-lvm2*.so.2.03

%package -n %{cmdlib}
Summary:        LVM2 command line library
Group:          System/Libraries
Conflicts:      %{name} < %{version}
Obsoletes:      liblvm2app2_2 <= %{liblvm2app2_2_version}
Obsoletes:      liblvm2cmd2_02 <= %{liblvm2cmd2_02_version}

%description -n %{cmdlib}
The lvm2 command line library allows building programs that manage
lvm devices without invoking a separate program.

%post -n %{cmdlib} -p /sbin/ldconfig
%postun -n %{cmdlib} -p /sbin/ldconfig

%files -n %{cmdlib}
%{_libdir}/liblvm2cmd.so.*

%package devel
Summary:        Development files for LVM2
Group:          Development/Libraries/C and C++
Requires:       %{cmdlib} = %{version}
Requires:       device-mapper-devel
Requires:       lvm2 = %{version}

%description devel
This package provides development files for the LVM2 Logical Volume Manager.

%files devel
%{_includedir}/lvm2cmd.h
%{_libdir}/liblvm2cmd.so

%package testsuite
Summary:        LVM2 Testsuite
Group:          Development/Libraries/C and C++
Requires:       %{cmdlib} = %{version}
Requires:       lvm2 = %{version}

%description testsuite
An extensive functional testsuite for the LVM2 Logical Volume Manager.

%files testsuite
%{_datarootdir}/lvm2-testsuite/
%{_libexecdir}/lvm2-testsuite/
%{_bindir}/lvm2-testsuite

%endif
%endif

%changelog
