#
# spec file for package mhvtl
#
# Copyright (c) 2025 SUSE LLC
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


%ifnarch ppc s390x
%define buildkmp 1
%else
%define buildkmp 0
%endif

%define mhvtl_home_dir /var/lib/mhvtl

Name:           mhvtl
URL:            http://sites.google.com/site/linuxvtl2/
Version:        1.72_release+6.a11b6777660b
Release:        0
Requires:       mhvtl-kmp
Requires:       module-init-tools
Requires:       sg3_utils
%if 0%{buildkmp} == 1
BuildRequires:  %kernel_module_package_buildreqs
BuildRequires:  kernel-syms
BuildRequires:  module-init-tools
%endif
BuildRequires:  fdupes
BuildRequires:  modutils
BuildRequires:  openssl-devel
BuildRequires:  policycoreutils-python-utils
BuildRequires:  systemd-rpm-macros
BuildRequires:  zlib-devel
Summary:        Virtual Tape Library system
License:        GPL-2.0-only
Group:          System/Daemons
Source:         %{name}-%{version}.tar.xz
Source2:        %{name}.preamble
Patch1:         0001-kernel-config-replace-fgrep-with-grep-F.patch
Patch2:         0002-kernel-config-put-braces-around-debug-stmnt.patch
Patch3:         0003-Fix-external-declarations-of-crc32c.patch
Patch4:         0004-kernel-config-handle-del_timer_sync-kABI-rename.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{?systemd_ordering}

%{?!_systemdgeneratordir:%define _systemdgeneratordir %{_prefix}/lib/systemd/system-generators}
%{?!_firmware_path:%define _firmware_path %{_prefix}/lib/firmware}

%if 0%{buildkmp} == 1
%suse_kernel_module_package -n %{name} -p %{S:2} kdump ec2 um
%endif

%description
A Virtual Tape & Library system.

This package is composed of a KMP (mhvtl), which is also a psuedo HBA.

%package KMP
Summary:        Virtual Tape Library kernel module
License:        LGPL-2.1-or-later
Group:          System/Kernel

%description KMP
This is the kernel module package for the mhvtl Virtual Tape &
Library package.

This works in conjunction with the user-land commands and libraries
to enable tape emulation.

The vtl module is a stripped-down derivative of the scsi_debug kernel
module, plus a character device "back end" to pass the SCSI commands
through to user-space daemons.

%prep
%autosetup -p1 -n %{name}-%{version}

%build
[ -z "$SOURCE_DATE_EPOCH" ] || export KBUILD_BUILD_TIMESTAMP=@$SOURCE_DATE_EPOCH
make MHVTL_HOME_PATH=%{mhvtl_home_dir} VERSION=%{version} \
	SYSTEMD_GENERATOR_DIR=%{_systemdgeneratordir} \
	SYSTEMD_SERVICE_DIR=%{_unitdir} FIRMWAREDIR=%{_firmware_path}
%if 0%{buildkmp} == 1
for flavor in %flavors_to_build; do
	make -C kernel config.h
	rm -rf obj/$flavor
	mkdir -p obj/$flavor
	cp -a kernel/* obj/$flavor
	make -C /usr/src/linux-obj/%_target_cpu/$flavor EXTRA_CFLAGS="-Iinclude -DMHVTL_DEBUG -DHAVE_UNLOCKED_IOCTL" modules \
	      M=$PWD/obj/$flavor
done
%endif

%install
%make_install \
	MHVTL_HOME_PATH=%{mhvtl_home_dir} VERSION=%{version}_release LIBDIR=%{_libdir} \
	SYSTEMD_GENERATOR_DIR=%{_systemdgeneratordir} \
	SYSTEMD_SERVICE_DIR=%{_unitdir} FIRMWAREDIR=%{_firmware_path}
%fdupes %{buildroot}/%{_prefix}
%if 0%{buildkmp} == 1
export INSTALL_MOD_PATH=%{buildroot}
export INSTALL_MOD_DIR=updates
for flavor in %flavors_to_build; do
	make -C /usr/src/linux-obj/%_target_cpu/$flavor EXTRA_CFLAGS="-Iinclude -DMHVTL_DEBUG -DHAVE_UNLOCKED_IOCTL" modules_install \
	      M=$PWD/obj/$flavor
done
%endif
install -d -m 755 %{buildroot}%{_sbindir}
ln -s %{_sbindir}/service %{buildroot}/%{_sbindir}/rc%{name}
rm -rf %{buildroot}/%{mhvtl_home_dir}
install -d -m 755 %{buildroot}/%{mhvtl_home_dir}

%post
%{service_add_post mhvtl-load-modules.service mhvtl.target vtllibrary@.service vtltape@.service}
if [ "$1" = 1 ]; then
	%{_bindir}/make_vtl_media --force \
		--config-dir=%{_sysconfdir}/mhvtl \
		--home-dir=%{mhvtl_home_dir} \
		--mktape-path=%{_bindir}
fi

%preun
%{service_del_preun mhvtl-load-modules.service mhvtl.target vtllibrary@.service vtltape@.service}

%postun
%{service_del_postun mhvtl-load-modules.service mhvtl.target vtllibrary@.service vtltape@.service}

%pre
%{service_add_pre mhvtl-load-modules.service mhvtl.target vtllibrary@.service vtltape@.service}

%files
%defattr(-,root,root)
%doc README etc/library_contents.sample
%license COPYING
%{_sbindir}/rcmhvtl
%{_bindir}/mktape
%{_bindir}/edit_tape
%{_bindir}/dump_tape
%{_bindir}/preload_tape
%{_bindir}/tapeexerciser
%{_bindir}/make_vtl_media
%{_bindir}/update_device.conf
%{_bindir}/vtlcmd
%{_bindir}/vtllibrary
%{_bindir}/vtltape
%{_bindir}/generate_device_conf
%{_bindir}/mhvtl_kernel_mod_build
%{_bindir}/generate_library_contents
%{_libdir}/libvtlscsi.so
%{_libdir}/libvtlcart.so
%dir %{_firmware_path}
%dir %{_firmware_path}/mhvtl
%{_firmware_path}/mhvtl/mhvtl_kernel.tgz
%dir %{_sysconfdir}/mhvtl
%config(noreplace) %{_sysconfdir}/mhvtl/mhvtl.conf
%config(noreplace) %{_sysconfdir}/mhvtl/device.conf
%config(noreplace) %{_sysconfdir}/mhvtl/library_contents.10
%config(noreplace) %{_sysconfdir}/mhvtl/library_contents.30
%{_systemdgeneratordir}/
%{_unitdir}/mhvtl-load-modules.service
%{_unitdir}/mhvtl.target
%{_unitdir}/vtltape@.service
%{_unitdir}/vtllibrary@.service
%dir %{mhvtl_home_dir}
%ghost %attr(0644,root,root) %{mhvtl_home_dir}/*
%defattr(644,root,root)
%{_mandir}/man1/vtlcmd.1%{ext_man}
%{_mandir}/man1/vtllibrary.1%{ext_man}
%{_mandir}/man1/vtltape.1%{ext_man}
%{_mandir}/man1/preload_tape.1%{ext_man}
%{_mandir}/man1/mktape.1%{ext_man}
%{_mandir}/man1/make_vtl_media.1%{ext_man}
%{_mandir}/man1/edit_tape.1%{ext_man}
%{_mandir}/man1/dump_tape.1%{ext_man}
%{_mandir}/man1/tapeexerciser.1%{ext_man}
%{_mandir}/man1/update_device.conf.1%{ext_man}
%{_mandir}/man1/generate_device_conf.1%{ext_man}
%{_mandir}/man1/generate_library_contents.1%{ext_man}
%{_mandir}/man1/mhvtl_kernel_mod_build.1%{ext_man}
%{_mandir}/man5/device.conf.5%{ext_man}
%{_mandir}/man5/library_contents.5%{ext_man}
%{_mandir}/man5/mhvtl.conf.5%{ext_man}

%changelog
