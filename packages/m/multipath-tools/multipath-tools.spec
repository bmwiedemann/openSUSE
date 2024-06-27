#
# spec file for package multipath-tools
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


%global _lto_cflags %{nil}
%global _make_output_sync -Orecurse

# multipath-tools auto-detects support for -D_FORTIFY_SOURCE.
# This will lead to a compilation error if the distro overrides
# -D_FORTIFY_SOURCE in optflags, unless it's preceded with -U_FORTIFY_SOURCE
%global mp_optflags %(echo %{optflags} | sed '/-U_FORTIFY_SOURCE/!s/-D_FORTIFY_SOURCE=[0-9]/-U_FORTIFY_SOURCE &/')

# Whether to build libdmmp - default YES
%bcond_without libdmmp

# Whether to run tests - default YES
%bcond_without check

# This should match the version in libdmmp/Makefile
%define _libdmmp_version 0.2.0
%define libdmmp_version %(echo %{_libdmmp_version} | tr . _)

Name:           multipath-tools
Version:        0.9.9+90+suse.f1d2f20
Release:        0
Summary:        Tools to Manage Multipathed Devices with the device-mapper
License:        GPL-2.0-only AND GPL-3.0-or-later
Group:          System/Base
URL:            http://christophe.varoqui.free.fr/
Source:         multipath-tools-%{version}.tar
# modprobe.d configuration file
Source1:        modprobe_d-scsi_dh.conf
# SUSE policy: disable partition deletion by default
Source2:        dont-del-part-nodes.rules
# Dracut conf file to make sure 11-dm-parts.rules is included in initrd
Source3:        dm-parts.conf
Source4:        libmpathpersist-example.c
Source6:        multipath-dracut.conf
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
BuildRequires:  pkgconfig(mount)
%if 0%{?with_check} == 1
BuildRequires:  pkgconfig(cmocka)
%endif
# For regenerate-initrd-posttrans
# For now, we still need to require suse-module-tools
# See https://github.com/openSUSE/rpm-config-SUSE/pull/6
BuildRequires:  suse-module-tools
Requires(post): suse-module-tools
Requires:       device-mapper >= 1.2.78
Requires:       kpartx
Requires:       sg3_utils
Obsoletes:      multipath-tools-rbd <= %{version}
PreReq:         coreutils
PreReq:         grep

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

%global extraversion %(echo %{version} | sed 's/^[^+]*//')
%define makeflags EXTRAVERSION="%{extraversion}" %{!?with_libdmmp:ENABLE_LIBDMMP=0}
%if 0%{?suse_version} < 1550
%define dirflags LIB=%{_lib}
%define sbindir /sbin
%define libdir  /%{_lib}
%else
%define dirflags LIB=%{_lib} prefix=%{_prefix} etc_prefix=
%define sbindir %{_sbindir}
%define libdir  %{_libdir}
%endif


%prep
%setup -q -n multipath-tools-%{version}
cp %{SOURCE4} .
%autopatch -p1

%build
[ -n "$SOURCE_DATE_EPOCH" ] && export KBUILD_BUILD_TIMESTAMP=@$SOURCE_DATE_EPOCH
%{make_build} OPTFLAGS="%{mp_optflags}" %{dirflags} %{makeflags} V=1

%if 0%{?with_check} == 1
%check
%{make_build} OPTFLAGS="%{mp_optflags}" %{dirflags} %{makeflags} V=1 test
%endif

%install
%make_install %{dirflags} %{makeflags} V=1
mkdir -p %{buildroot}%{_defaultlicensedir}
mkdir -p %{buildroot}/usr/sbin
mkdir -p %{buildroot}/usr/%{_lib}
%if 0%{?suse_version} < 1550
for x in mpathutil multipath mpathpersist mpathcmd mpathvalid; do
    rm -f %{buildroot}/%{_lib}/lib$x.so
    ln -sf /%{_lib}/lib$x.so.0  %{buildroot}/usr/%{_lib}/lib$x.so
done
%endif
ln -sf service %{buildroot}/usr/sbin/rcmultipathd
install -m 644 -D %{SOURCE1} %{buildroot}/usr/lib/modprobe.d/90-scsi_dh.conf
install -m 644 %{SOURCE2} %{buildroot}%{_udevrulesdir}/00-dont-del-part-nodes.rules
install -m 644 -D %{SOURCE3} %{buildroot}/usr/lib/dracut/dracut.conf.d/dm-parts.conf
install -m 644 -D %{SOURCE6} %{buildroot}/usr/lib/dracut/dracut.conf.d/multipath.conf
sed -i 's,@TMPFILESDIR@,%{_tmpfilesdir},;s,@UDEVRULESDIR@,%{_udevrulesdir},' %{buildroot}/usr/lib/dracut/dracut.conf.d/multipath.conf

%post -n libmpath0 -p %{run_ldconfig}
%postun -n libmpath0 -p %{run_ldconfig}

%pre
[ -f /.buildenv ] && exit 0
%service_add_pre multipathd.socket multipathd.service

%post
[ -f /.buildenv ] && exit 0
%tmpfiles_create %{_tmpfilesdir}/multipath.conf
%service_add_post multipathd.socket multipathd.service
if [ $1 -eq 1 ]; then
    [ ! -x /sbin/modprobe ] || /sbin/modprobe dm_multipath || true
fi
%{?regenerate_initrd_post}
exit 0

%preun
%service_del_preun multipathd.service multipathd.socket

%postun
%{?regenerate_initrd_post}
%service_del_postun multipathd.service
%service_del_postun_without_restart multipathd.socket

%posttrans
%{?regenerate_initrd_posttrans}

%files
%doc README.md
%doc NEWS.md
%license LICENSES/GPL-2.0
%license LICENSES/GPL-3.0
%{_udevrulesdir}/11-dm-mpath.rules
%{_udevrulesdir}/56-multipath.rules
%{_udevrulesdir}/99-z-dm-mpath-late.rules
%{sbindir}/multipath
%{sbindir}/multipathd
%{sbindir}/multipathc
%{sbindir}/mpathpersist
/usr/sbin/rcmultipathd
%{_unitdir}/multipathd.service
%{_unitdir}/multipathd.socket
%if 0%{?suse_version} < 1550 && 0%{?sle_version} < 150300
%dir /usr/lib/modules-load.d
/usr/lib/modules-load.d/multipath.conf
%endif
%dir /usr/lib/dracut
%dir /usr/lib/dracut/dracut.conf.d
/usr/lib/dracut/dracut.conf.d/multipath.conf
/usr/lib/modprobe.d/90-scsi_dh.conf
%{_tmpfilesdir}/multipath.conf
%{_mandir}/man8/multipath.8*
%{_mandir}/man5/multipath.conf.5*
%{_mandir}/man8/multipathd.8*
%{_mandir}/man8/multipathc.8*
%{_mandir}/man8/mpathpersist.8*
%ghost %attr(700,root,root) /run/multipath

%files -n libmpath0
%{libdir}/libmultipath.so.0
%{libdir}/libmpathcmd.so.0
%{libdir}/libmpathpersist.so.0
%{libdir}/libmpathvalid.so.0
%{libdir}/libmpathutil.so.0
%{libdir}/multipath
%license LICENSES/GPL-2.0
%license LICENSES/LGPL-2.0
%license LICENSES/LGPL-2.1
%license README.licenses

%files devel
%{_libdir}/libmultipath.so
%{_libdir}/libmpathcmd.so
%{_libdir}/libmpathpersist.so
%{_libdir}/libmpathvalid.so
%{_libdir}/libmpathutil.so
/usr/include/mpath_cmd.h
/usr/include/mpath_persist.h
/usr/include/mpath_valid.h
%{_mandir}/man3/mpath_persistent_*
%doc libmpathpersist-example.c

%files -n kpartx
%license LICENSES/GPL-2.0
%{sbindir}/kpartx
%{_udevrulesdir}/00-dont-del-part-nodes.rules
%{_udevrulesdir}/11-dm-parts.rules
%{_udevrulesdir}/66-kpartx.rules
%{_udevrulesdir}/68-del-part-nodes.rules
/usr/lib/udev/kpartx_id
/usr/lib/dracut/dracut.conf.d/dm-parts.conf
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
%{_libdir}/libdmmp.so
%{_mandir}/man3/libdmmp.h*
%{_mandir}/man3/dmmp_*
%{_includedir}/libdmmp
%{_libdir}/pkgconfig/libdmmp.pc

%endif

%changelog
