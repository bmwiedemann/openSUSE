#
# spec file for package device-mapper
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


%define libname libdevmapper1_03
%define libname_event libdevmapper-event1_03
### COMMON-DEF-BEGIN ###
%define lvm2_version              2.02.180
%define device_mapper_version     1.02.149
%define thin_provisioning_version 0.7.0
### COMMON-DEF-END ###
Name:           device-mapper
Version:        %{device_mapper_version}
Release:        0
Summary:        Device Mapper Tools
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          System/Base
Url:            http://www.sourceware.org/lvm2/
Source:         ftp://sources.redhat.com/pub/lvm2/LVM2.%{lvm2_version}.tgz
Source1:        ftp://sources.redhat.com/pub/lvm2/LVM2.%{lvm2_version}.tgz.asc
Source99:       baselibs.conf
# To detect modprobe during build
BuildRequires:  gcc-c++
BuildRequires:  kmod-compat
BuildRequires:  libaio-devel
BuildRequires:  pkgconfig
BuildRequires:  suse-module-tools
BuildRequires:  thin-provisioning-tools >= %{thin_provisioning_version}
BuildRequires:  pkgconfig(libselinux)
BuildRequires:  pkgconfig(libsepol)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(systemd)
Requires:       thin-provisioning-tools >= %{thin_provisioning_version}
Requires(post): coreutils
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

%description
Programs and man pages for configuring and using the device mapper.

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

%build
extra_opts=""

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

%make_build device-mapper

%install
make DESTDIR=%{buildroot} \
    install_device-mapper \
    install_systemd_units install_systemd_generators

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
rm %{buildroot}%{_mandir}/man8/lvm2-activation-generator.8

# compat symlinks in /sbin remove with Leap 43
mkdir -p %{buildroot}/sbin
ln -s %{_sbindir}/dmsetup %{buildroot}/sbin/dmsetup

%pre
%service_add_pre dm-event.service dm-event.socket

%post
%service_add_post dm-event.service dm-event.socket
%{?regenerate_initrd_post}

%posttrans
%{?regenerate_initrd_posttrans}

%preun
%service_del_preun dm-event.service dm-event.socket

%postun
%service_del_postun dm-event.service dm-event.socket
%{?regenerate_initrd_post}

%files
%defattr(-,root,root)
%license COPYING COPYING.LIB
%doc README
%doc udev/12-dm-permissions.rules
/sbin/dmsetup
%{_sbindir}/dmsetup
%{_sbindir}/dmeventd
%{_sbindir}/dmstats
%{_mandir}/man8/dmstats.8%{ext_man}
%{_mandir}/man8/dmsetup.8%{ext_man}
%{_mandir}/man8/dmeventd.8%{ext_man}
%{_udevrulesdir}/10-dm.rules
%{_udevrulesdir}/13-dm-disk.rules
%{_udevrulesdir}/95-dm-notify.rules
%{_unitdir}/dm-event.socket
%{_sbindir}/rcdm-event
%{_unitdir}/dm-event.service

%package -n %{libname}
Summary:        Library for device-mapper
Group:          System/Libraries
Conflicts:      %{name} < %{version}

%description -n %{libname}
Device mapper main shared library

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libdevmapper.so.1.03
%{_libdir}/libdevmapper.so.1.02

%post   -n %{libname}
if [ -f /%{_lib}/libdevmapper.so.1.03 ]; then
  # Special migration - the library is now in %{_libdir}, but up to the point where
  # zypp removes the 'old' device-mapper package, the old library 'wins' the ldloader race
  # resulting in binaries asking for the newer version still getting the old one.
  # This in turn results in funny bugs like boo#1045396
  # Remove /%{_lib}/libdevmapper.so.1.02 - and the run ldconfig
  rm /%{_lib}/libdevmapper.so.1.03
fi
 /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%package -n %{libname_event}
Summary:        Event library for device-mapper
Group:          System/Libraries
Conflicts:      %{name} < %{version}

%description -n %{libname_event}
Device mapper event daemon shared library

%files -n %{libname_event}
%defattr(-,root,root)
%{_libdir}/libdevmapper-event.so.1.03
%{_libdir}/libdevmapper-event.so.1.02

%post -n %{libname_event} -p /sbin/ldconfig
%postun -n %{libname_event} -p /sbin/ldconfig

%package devel
Summary:        Development package for the device mapper
Group:          Development/Libraries/C and C++
Requires:       %{libname_event} = %{device_mapper_version}
Requires:       %{libname} = %{device_mapper_version}
Requires:       device-mapper = %{device_mapper_version}

%description devel
Files needed for software development using the device mapper

%files devel
%defattr(-,root,root)
%{_libdir}/libdevmapper.so
%{_libdir}/libdevmapper-event.so
%{_includedir}/libdevmapper.h
%{_includedir}/libdevmapper-event.h
%{_libdir}/pkgconfig/devmapper.pc
%{_libdir}/pkgconfig/devmapper-event.pc

%changelog
