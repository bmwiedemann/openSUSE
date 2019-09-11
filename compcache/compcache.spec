#
# spec file for package compcache
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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
# nodebuginfo


#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif

%if %suse_version <= 1120
%define need_kmp	1
%else
%define need_kmp	0
%endif

%if %suse_version <= 1130
%define need_rzsctl	1
%else
%define need_rzsctl	0
%endif

Name:           compcache
%if %need_kmp
BuildRequires:  kernel-source
BuildRequires:  kernel-syms
BuildRequires:  module-init-tools
%endif
Version:        0.6.2
Release:        0
Summary:        Compressed RAM based swap device
License:        GPL-2.0
Group:          System/Kernel
Source0:        compcache-%{version}.tar.bz2
Source1:        sysconfig.compcache
Source2:        boot.compcache
Patch:          compcache-rzscontrol-cflags.diff
Patch1:         ramzswap-kernel-build-fix.diff
Url:            http://code.google.com/p/compcache/
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
PreReq:         %fillup_prereq
PreReq:         %insserv_prereq
%if %need_kmp
Requires:       compcache-kmp
%suse_kernel_module_package -n %{name} kdump um
%else
%if !%need_rzsctl
BuildArch:      noarch
%endif
%endif

%description
The compcache is a RAM-based block device acting as a swap disk. This
can effectively increase the available memory on your machine by
virtually swapping pages into the compressed memory.

This package contains the boot script for loading/unloading the
modules.

%if %need_kmp

%package KMP
Summary:        Kernel module for compressed RAM based swap device
Group:          System/Kernel

%description KMP
The compcache is a RAM-based block device acting as a swap disk. This
can effectively increase the available memory on your machine by
virtually swapping pages into the compressed memory.

This package contains the kernel module for compcache.
%endif

%prep
%setup -q
%patch -p1
%patch1 -p1

%build
%if %need_kmp
for flavor in %flavors_to_build; do
	rm -rf obj/$flavor
	mkdir -p obj/$flavor
	cp -al *.[ch] Makefile sub-projects obj/$flavor
	KERNEL_OBJ="/usr/src/linux-obj/%_target_cpu/$flavor"
	make -C ${KERNEL_OBJ} M=$PWD/obj/$flavor modules %{?_smp_mflags}
done
%endif
%if %need_rzsctl
make -C sub-projects/rzscontrol %{?_smp_mflags}
%endif

%install
%if %need_kmp
export INSTALL_MOD_PATH=$RPM_BUILD_ROOT
export INSTALL_MOD_DIR=updates
for flavor in %flavors_to_build; do
	KERNEL_OBJ="/usr/src/linux-obj/%_target_cpu/$flavor"
	make -C ${KERNEL_OBJ} M=$PWD/obj/$flavor modules_install %{?_smp_mflags}
done
%endif
%if %need_rzsctl
mkdir -p $RPM_BUILD_ROOT/usr/sbin
install -c -m 0755 sub-projects/rzscontrol/rzscontrol $RPM_BUILD_ROOT/usr/sbin
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
install -c -m 0644 sub-projects/rzscontrol/man/*.1 $RPM_BUILD_ROOT/%{_mandir}/man1
%endif
mkdir -p $RPM_BUILD_ROOT%{_fillupdir}
install -c -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_fillupdir}
mkdir -p $RPM_BUILD_ROOT/etc/init.d
install -c -m 0755 %{SOURCE2} $RPM_BUILD_ROOT/etc/init.d/

%post
%{fillup_only}

%preun
%stop_on_removal

%postun
%{insserv_cleanup}

%files
%defattr(-,root,root)
%if %need_rzsctl
/usr/sbin/*
%{_mandir}/man?/*
%endif
/etc/init.d/boot.compcache
%{_fillupdir}/sysconfig.compcache
%doc README Changelog

%changelog
