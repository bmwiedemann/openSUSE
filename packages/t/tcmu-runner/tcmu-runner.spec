#
# spec file for package tcmu-runner
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


%if 0%{?sle_version} == 0
%define         build_handler_glusterfs 1
%endif

%if 0%{?sle_version} == 0 || 0%{?sle_version} >= 120300
%ifarch aarch64 x86_64
%define         build_handler_rbd 1
%endif
%endif

%if 0%{?sle_version} == 0
%ifarch aarch64 x86_64
%define		build_handler_zbc 1
%endif
%endif

Name:           tcmu-runner
Version:        1.4.0
Release:        0
Summary:        A userspace daemon that handles the LIO TCM-User backstore
License:        Apache-2.0
Group:          System/Management
Url:            https://github.com/agrover/%{name}
Source:         %{name}-%{version}.tar.xz
Patch1:         %{name}-handler_file-add-libtcmu.patch
Patch2:         %{name}-remove-handler-path-install-prefix.patch
Patch3:         file_zbc-fixed-compile-error-under-ppc64le.patch
Patch4:         file_zbc-optionally-build-zbc-handler.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  cmake
BuildRequires:  glib2-devel
BuildRequires:  glibc-devel
%if 0%{?build_handler_glusterfs}
BuildRequires:  glusterfs-devel
%endif
%if 0%{?build_handler_rbd}
BuildRequires:  librbd-devel
%endif
%if 0%{?build_handler_zbc}
BuildRequires:  libzbc-devel
%endif
BuildRequires:  libkmod-devel
BuildRequires:  libnl3-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  zlib-devel
Requires:       libtcmu2 = %{version}
Requires:       logrotate
%{?systemd_requires}

%description
LIO is the SCSI target in the Linux kernel. It is entirely kernel
code, and allows exported SCSI logical  units (LUNs) to be backed
by regular files or block devices. But, if we want to get fancier with
the capabilities of the device we're emulating, the kernel is not
necessarily the right place. While there are userspace libraries for
compression, encryption, and clustered storage solutions like
Ceph or Gluster, these are not accessible from the kernel. 

The TCMU userspace-passthrough backstore allows a userspace process to
handle requests to a LUN. But since the kernel-user interface that
TCMU provides must be fast and flexible, it is complex enough that
we'd like to avoid each  userspace handler having to write boilerplate
code.

tcmu-runner handles the messy details of the TCMU interface -- UIO,
netlink, pthreads, and DBus -- and exports a more friendly C plugin
module API. Modules using this API are called "TCMU handlers". Handler
authors can write code just to handle the SCSI commands as desired,
and can also link with whatever userspace libraries they like.

%package -n libtcmu2
Summary:        Runtime libraries for tcmu-runner
Group:          System/Libraries

%description -n libtcmu2
This package contains the runtime libraries for tcmu-runner.

%if 0%{?build_handler_glusterfs}
%package handler-glusterfs
Summary:        GlusterFS handler for tcmu-runner
Group:          System/Libraries
Requires:       tcmu-runner = %{version}

%description handler-glusterfs
This package contains the GlusterFS handler for tcmu-runner, which
allows for LIO/tcmu logical units to be backed by GlusterFS provisioned
storage.
%endif

%if 0%{?build_handler_rbd}
%package handler-rbd
Summary:        Ceph RBD handler for tcmu-runner
Group:          System/Libraries
Requires:       tcmu-runner = %{version}

%description handler-rbd
This package contains the Ceph RADOS Block Device (RBD) handler for
tcmu-runner, which allows for LIO/tcmu logical units to be backed by
RBD images.
%endif

%if 0%{?build_handler_zbc}
%package handler-zbc
Summary:        Ceph ZBC handler for tcmu-runner
Group:          System/Libraries
Requires:       tcmu-runner = %{version}

%description handler-zbc
This package contains the Ceph RADOS ZBC disc emulation, using a
file backstore in tcmu-runner.
%endif

%prep
%setup
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
CMAKE_OPTIONS="\
	-DSUPPORT_SYSTEMD=1 \
%if 0%{?build_handler_glusterfs}
	-Dwith-glfs=1 \
%else
	-Dwith-glfs=0 \
%endif
%if 0%{?build_handler_rbd}
	-Dwith-rbd=1 \
%else
	-Dwith-rbd=0 \
%endif
%if 0%{?build_handler_zbc}
	-Dwith-zbc=1 \
%else
	-Dwith-zbc=0 \
%endif
"
%cmake -DCMAKE_SHARED_LINKER_FLAGS="-Wl,--as-needed -Wl,-z,now" \
	${CMAKE_OPTIONS}
make %{?_smp_mflags}

%install
%cmake_install
install -d -m 755 %{buildroot}/%{_sbindir}
ln -s %{_sbindir}/service %{buildroot}/%{_sbindir}/rctcmu-runner

%post
%{run_ldconfig}
%{service_add_post tcmu-runner.service}

%postun
%{service_del_postun tcmu-runner.service}
%{run_ldconfig}

%pre
%{service_add_pre tcmu-runner.service}

%preun
%{service_del_preun tcmu-runner.service}

%post -n libtcmu2 -p /sbin/ldconfig

%postun -n libtcmu2 -p /sbin/ldconfig

%files
%defattr(-,root,root)
%{_bindir}/tcmu-runner
%{_sbindir}/rctcmu-runner
%doc README.md
%license LICENSE.Apache2
%license LICENSE.LGPLv2.1
%dir %{_libdir}/tcmu-runner
%{_libdir}/tcmu-runner/handler_qcow.so
%dir %{_datadir}/dbus-1
%dir %{_datadir}/dbus-1/system-services
%{_datadir}/dbus-1/system-services/org.kernel.TCMUService1.service
%dir %{_sysconfdir}/dbus-1
%dir %{_sysconfdir}/dbus-1/system.d
%config %{_sysconfdir}/dbus-1/system.d/tcmu-runner.conf
%{_unitdir}/tcmu-runner.service
%doc %{_mandir}/man8/tcmu-runner.8%{ext_man}
%config %{_sysconfdir}/logrotate.d/tcmu-runner
%dir %{_sysconfdir}/tcmu
%config(noreplace) %{_sysconfdir}/tcmu/tcmu.conf

%files -n libtcmu2
%defattr(-,root,root)
%{_libdir}/libtcmu.so.2

%if 0%{?build_handler_glusterfs}
%files handler-glusterfs
%{_libdir}/tcmu-runner/handler_glfs.so
%endif

%if 0%{?build_handler_rbd}
%files handler-rbd
%{_libdir}/tcmu-runner/handler_rbd.so
%endif

%if 0%{?build_handler_zbc}
%files handler-zbc
%{_libdir}/tcmu-runner/handler_file_zbc.so
%endif

%changelog
