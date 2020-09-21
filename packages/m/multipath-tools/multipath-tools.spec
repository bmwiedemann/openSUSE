#
# spec file for package multipath-tools
#
# Copyright (c) 2020 SUSE LLC
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


# Whether to build libdmmp
# Default YES except for SLE12 / Leap 42
%if 0%{?suse_version} >= 1500
%bcond_without libdmmp
%else
%bcond_with libdmmp
%endif

# "make test" disabled on SLE12 (cmocka not available)
%if 0%{?suse_version} >= 1500
%bcond_without check
%else
%bcond_with check
%endif

# This should match the version in libdmmp/Makefile
%define _libdmmp_version 0.2.0
%define libdmmp_version %(echo %{_libdmmp_version} | tr . _)

# path prefix for systemd unit files and udev rules
%define _sysdir usr/lib

Name:           multipath-tools
Version:        0.8.4+192+suse.1bc10ad
Release:        0
Summary:        Tools to Manage Multipathed Devices with the device-mapper
License:        GPL-2.0-only
Group:          System/Base
URL:            http://christophe.varoqui.free.fr/
Source:         multipath-tools-%{version}.tar.xz
Source1:        multipath.conf
# SUSE policy: disable partition deletion by default
Source2:        dont-del-part-nodes.rules
# Dracut conf file to make sure 11-dm-parts.rules is included in initrd
Source3:        dm-parts.conf
Source4:        libmpathpersist-example.c
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{?systemd_requires}
BuildRequires:  libaio-devel
BuildRequires:  pkgconfig(devmapper)
%if 0%{?with_libdmmp} == 1
BuildRequires:  pkgconfig(json-c)
%endif
BuildRequires:  readline-devel
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(liburcu)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(udev)
%if 0%{?with_check} == 1
BuildRequires:  pkgconfig(cmocka)
%endif
# For regenerate-initrd-posttrans
# For now, we still need to require suse-module-tools
# See https://github.com/openSUSE/rpm-config-SUSE/pull/6
BuildRequires:  suse-module-tools
Requires(post):	suse-module-tools
Requires:       device-mapper >= 1.2.78
Requires:       kpartx
Requires:       sg3_utils
Obsoletes:      multipath-tools-rbd <= %{version}
PreReq:         coreutils grep

%description
This package provides the multipath tool and the multipathd daemon
to manage dm-multipath devices. multipath can detect and set up
multipath maps. multipathd sets up multipath maps automatically,
monitors path devices for failure, removal, or addition, and applies
the necessary changes to the multipath maps to ensure continuous
availability of the map devices.

# Currently, it makes no sense to split out libmpathpersist and libmpathcmd
# separately. libmultipath has no stable API at all, and it depends
# on libmpathcmd (to be fixed). libmpathpersist depends on libmultipath
# and it loads prioritizers (to be fixed) and checkers.
%package -n libmpath0
Summary:        Libraries for multipath-tools
# This is for libmpathcmd, which is useless without multipathd.
# No hard dependency here - we don't want to pull in all dependencies
# of multipath-tools.
License:        GPL-2.0-only AND LGPL-2.1-only AND LGPL-2.0-or-later
Group:          System/Libraries
Recommends:     multipath-tools
Conflicts:      multipath-tools < 0.8.0

%description -n libmpath0
libmpathpersist provides a C API for handling of SCSI persistent
reservations for device-mapper multipath devices. libmpathcmd
provides a C API for sending commands to a running multipathd
instance.

%package -n kpartx
Summary:        Manages partition tables on device-mapper devices
License:        GPL-2.0-only
Group:          System/Base
Requires:       device-mapper

%description -n kpartx
The kpartx program maps linear devmaps to device partitions, which
makes multipath maps partionable.

%package devel
Summary:        Development libraries for multipath-tools
License:        GPL-2.0-only AND LGPL-2.0-or-later
Group:          Development/Libraries/C and C++
Requires:       libmpath0 = %{version}

%description devel
This package contains the development libraries for multipath-tools
and libmpathpersist.

%package -n libdmmp%{libdmmp_version}
Summary:        C API for multipath-tools
License:        GPL-3.0-or-later
Group:          System/Libraries
Requires:       multipath-tools

%description -n libdmmp%{libdmmp_version}
This library enables the use of libmultipath commands from C code.

%package -n libdmmp-devel
Summary:        Header files for multipath-tools C API
License:        GPL-3.0-or-later
Group:          Development/Libraries/C and C++
Requires:       libdmmp%{libdmmp_version} = %{version}

%description -n libdmmp-devel
This package provides development files and documentation for libdmmp.

%define makeflags %{!?with_libdmmp:ENABLE_LIBDMMP=0}
%define dirflags LIB=%{_lib} usr_prefix=%{_prefix} SYSTEMDPATH=%{_sysdir}

%prep
%setup -q -n multipath-tools-%{version}
# This must be before autopatch for code 12, otherwise build error
cp %{SOURCE4} .
%autopatch -p1

%build
[ -n "$SOURCE_DATE_EPOCH" ] && export KBUILD_BUILD_TIMESTAMP=@$SOURCE_DATE_EPOCH
# %%make_build is not supported in SLE12
%{?make_build}%{!?make_build:make %{?_smp_mflags}} \
 CC="%__cc" OPTFLAGS="%{optflags}" %{dirflags} %{makeflags}

%if 0%{?with_check} == 1
%check
# ld fails to resolve cmocka's __wrap symbols with -flto
# https://gcc.gnu.org/bugzilla/show_bug.cgi?id=88643
%define _lto_cflags %{nil}
make OPTFLAGS="%{optflags}" %{_make_output_sync} %{?_smp_mflags} test
%endif

%install
%make_install %{dirflags} %{makeflags}
mkdir -p %{buildroot}%{_defaultlicensedir}
mkdir -p %{buildroot}/usr/sbin
mkdir -p %{buildroot}/usr/%{_lib}
for x in multipath mpathpersist mpathcmd; do
    rm -f %{buildroot}/%{_lib}/lib$x.so
    ln -sf /%{_lib}/lib$x.so.0  %{buildroot}/usr/%{_lib}/lib$x.so
done
ln -sf /usr/sbin/service %{buildroot}/usr/sbin/rcmultipathd
mkdir -p %{buildroot}/usr/lib/modules-load.d
install -m 644 -D %{SOURCE1} "%{buildroot}/usr/lib/modules-load.d/multipath.conf"
install -m 644 %{SOURCE2} %{buildroot}%{_udevrulesdir}/00-dont-del-part-nodes.rules
install -m 644 -D %{SOURCE3} %{buildroot}/usr/lib/dracut/dracut.conf.d/dm-parts.conf

%post -n libmpath0 -p %{run_ldconfig}
%postun -n libmpath0 -p %{run_ldconfig}

%pre
[ -f /.buildenv ] && exit 0
%service_add_pre multipathd.socket multipathd.service

%post
[ -f /.buildenv ] && exit 0
%service_add_post multipathd.socket multipathd.service
%{?regenerate_initrd_post}
exit 0

%preun
%service_del_preun multipathd.service multipathd.socket

%postun
%{?regenerate_initrd_post}
%service_del_postun multipathd.service
%if 0%{?suse_version} >= 1550
%service_del_postun_without_restart multipathd.socket
%else
%service_del_postun -n multipathd.socket
%endif

%posttrans
%{?regenerate_initrd_posttrans}

%files
%defattr(-,root,root)
%doc README README.alua
# SLE12-SP2 and earlier: dracut filesystem not own /usr/share/licenses
%if 0%{?sle_version} && 0%{?sle_version} < 120300
%dir %{_defaultlicensedir}
%endif
%license LICENSES/GPL-2.0
%{_udevrulesdir}/11-dm-mpath.rules
%{_udevrulesdir}/56-multipath.rules
/sbin/multipath
/sbin/multipathd
/sbin/mpathpersist
/usr/sbin/rcmultipathd
%dir /%{_sysdir}/systemd/system
/%{_sysdir}/systemd/system/multipathd.service
/%{_sysdir}/systemd/system/multipathd.socket
%dir /usr/lib/modules-load.d
/usr/lib/modules-load.d/multipath.conf
%dir /usr/lib/dracut
%dir /usr/lib/dracut/dracut.conf.d

%{_mandir}/man8/multipath.8*
%{_mandir}/man5/multipath.conf.5*
%{_mandir}/man8/multipathd.8*
%{_mandir}/man8/mpathpersist.8*

%files -n libmpath0
/%{_lib}/libmultipath.so.0
/%{_lib}/libmpathcmd.so.0
/%{_lib}/libmpathpersist.so.0
/%{_lib}/multipath
%license LICENSES/GPL-2.0
%license LICENSES/LGPL-2.0
%license LICENSES/LGPL-2.1
%license README.licenses

%files devel
%defattr(-,root,root)
/usr/%{_lib}/libmultipath.so
/usr/%{_lib}/libmpathcmd.so
/usr/%{_lib}/libmpathpersist.so
/usr/include/mpath_cmd.h
/usr/include/mpath_persist.h
%{_mandir}/man3/mpath_persistent_*
%doc libmpathpersist-example.c

%files -n kpartx
%defattr(-,root,root)
%license LICENSES/GPL-2.0
/sbin/kpartx
%{_udevrulesdir}/00-dont-del-part-nodes.rules
%{_udevrulesdir}/11-dm-parts.rules
%{_udevrulesdir}/66-kpartx.rules
%{_udevrulesdir}/68-del-part-nodes.rules
/%{_sysdir}/udev/kpartx_id
# SLE12-SP1 and earlier: dracut does not own /usr/lib/dracut/dracut.conf.d
%if 0%{?sle_version}
%if 0%{?sle_version} <= 120100
%dir /%{_sysdir}/dracut/dracut.conf.d
%endif
%endif
/%{_sysdir}/dracut/dracut.conf.d/dm-parts.conf
%{_mandir}/man8/kpartx.8*

%posttrans -n kpartx
# The kpartx package contains udev rules that may need to be in initrd.
%{?regenerate_initrd_posttrans}

%post -n libdmmp%{libdmmp_version} -p %{run_ldconfig}
%postun -n libdmmp%{libdmmp_version} -p %{run_ldconfig}

%if 0%{?with_libdmmp} == 1

%files -n libdmmp%{libdmmp_version}
%defattr(-,root,root)
%license LICENSES/GPL-3.0
/%{_libdir}/libdmmp.so.%{_libdmmp_version}

%files -n libdmmp-devel
%defattr(-,root,root)
/%{_libdir}/libdmmp.so
%{_mandir}/man3/libdmmp.h*
%{_mandir}/man3/dmmp_*
%{_includedir}/libdmmp
%{_libdir}/pkgconfig/libdmmp.pc

%endif

%changelog
