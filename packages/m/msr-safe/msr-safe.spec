#
# spec file for package msr-safe
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


Name:           msr-safe
Version:        1.7.0
Release:        0
Summary:        Kernel module and utility to control MSR access
License:        GPL-3.0-or-later
Group:          System/Fhs
URL:            https://github.com/LLNL/msr-safe
Source0:        https://github.com/LLNL/msr-safe/archive/v%{version}.tar.gz
Source1:        msr-safe.service
Source2:        msr-safe.sysconfig
Source3:        10-msr-safe.rules
Source4:        msr-safe.sh
Source5:        system-user-msr.conf
Patch0:         0000-msr_allowlist-diff.patch
Patch1:         0001-msr_batch-diff.patch
Patch2:         0002-msr_entry-diff.patch
Patch3:         0003-msr_version-diff.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  %kernel_module_package_buildreqs
BuildRequires:  kernel-default-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  sysuser-tools
Requires(post):   fillup
Requires(post):   udev
Requires(postun): udev

%kernel_module_package 

# Only supported on intel architectures
ExclusiveArch:  %{ix86} x86_64

%description
Userspace utility for the kernel module of the same name
for controlling detailed access to Model Specific Registers
of CPUs.

%package KMP
Summary:        Kernel module for fine-grained access to MSRs
Group:          System/Kernel

%description KMP
A kernel module which provides new /dev nodes for accessing Model
Speicific Registers in CPUs, and which offers an allowlist to control
which exact MSRs may be read.

%package -n system-user-msr
Summary:        System user msr & group msr
Group:          System/Fhs
%{sysusers_requires}

%description -n system-user-msr
This package provides the system account and group "msr".

%prep
%autosetup -n %{name}-%{version}

%build
for flavor in %{flavors_to_build}; do
    rm -rf obj/$flavor
    mkdir -p obj/$flavor
    cp -r msr* Makefile obj/$flavor
    %make_build -C %{kernel_source $flavor} M=$PWD/obj/$flavor
done
%make_build CPPFLAGS="-DVERSION=\\\"%{version}-%{release}\\\"" msrsave/msrsave
%sysusers_generate_pre %{SOURCE5} msr

%install
mkdir -p %{buildroot}%{_sysusersdir}
mkdir -p %{buildroot}%{_sysconfdir}/msr
make install DESTDIR=%{buildroot} prefix=%{_prefix} sbindir=%{_sbindir} mandir=%{_mandir}
install -d %{buildroot}/%{_datadir}/msr-safe/allowlists
install -m 0644 allowlists/* %{buildroot}%{_datadir}/msr-safe/allowlists/
install -Dm 0644 %{SOURCE1} %{buildroot}%{_unitdir}/msr-safe.service
install -Dm 0644 %{SOURCE2} %{buildroot}%{_fillupdir}/sysconfig.msr-safe
install -Dm 0644 %{SOURCE3} %{buildroot}%{_udevrulesdir}/10-msr-safe.rules
install -Dm 0755 %{SOURCE4} %{buildroot}%{_sbindir}/msr-safe
install -m 644 %{SOURCE5} %{buildroot}%{_sysusersdir}/system-user-msr.conf

export INSTALL_MOD_PATH=%{buildroot}
export INSTALL_MOD_DIR=extra/%{name}
for flavor in %{flavors_to_build} ; do
        make -C %{kernel_source $flavor} modules_install \
                M=$PWD/obj/$flavor
done

%pre
%service_add_pre msr-safe.service

%pre -n system-user-msr -f msr.pre

%post
%fillup_only -n msr-safe
%udev_rules_update
%service_add_post msr-safe.service

%preun
%service_del_preun msr-safe.service

%postun
%udev_rules_update
%service_del_postun msr-safe.service

%files -n system-user-msr
%defattr(-,root,root)
%{_sysusersdir}/system-user-msr.conf

%{_fillupdir}/sysconfig.msr-safe
%dir %{_datadir}/msr-safe
%dir %{_datadir}/msr-safe/allowlists
%{_datadir}/msr-safe/allowlists/*
%{_unitdir}/msr-safe.service
%{_udevrulesdir}/10-msr-safe.rules
%{_sbindir}/msrsave
%{_sbindir}/msr-safe
%{_mandir}/man1/msrsave.1%{?ext_man}

%changelog
