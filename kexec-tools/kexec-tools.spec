#
# spec file for package kexec-tools
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


Name:           kexec-tools
Version:        2.0.19
Release:        0
Summary:        Tools for loading replacement kernels into memory
License:        GPL-2.0-or-later
Group:          System/Kernel
Source:         https://kernel.org/pub/linux/utils/kernel/kexec/%{name}-%{version}.tar.xz
Source1:        kexec-bootloader
Source2:        kexec-bootloader.8
Source3:        kexec-load.service
Source4:        %{name}-rpmlintrc
Patch2:         %{name}-xen-balloon-up.patch
Patch3:         %{name}-disable-test.patch
Patch14:        %{name}-vmcoreinfo-in-xen.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  systemd-rpm-macros
BuildRequires:  zlib-devel
#!BuildIgnore:  fop
#!BuildIgnore:  gcc-PIE
Requires:       perl-Bootloader
Requires(post): suse-module-tools
Requires(postun): suse-module-tools
%{?systemd_requires}
%ifarch         x86_64
BuildRequires:  pkgconfig
BuildRequires:  xen-devel
%endif

%description
Kexec is a user space utility for loading another kernel and asking the
currently running kernel to do something with it. A currently running
kernel may be asked to start the loaded kernel on reboot, or to start
the loaded kernel after it panics.

%prep
%setup -q
%patch2 -p1
%patch3 -p1
%patch14 -p1

%build
autoreconf -fvi
export CFLAGS="%{optflags}"
export BUILD_CFLAGS="%{optflags}"
%configure
make %{?_smp_mflags}

%install
%make_install
install -c -m 0644 %{SOURCE2} %{buildroot}/%{_mandir}/man8
mkdir -p %{buildroot}/%{_sbindir}
install -m 0755 %{SOURCE1} %{buildroot}/%{_sbindir}
mkdir -p %{buildroot}/%{_unitdir}
install -m644 %{SOURCE3} %{buildroot}/%{_unitdir}
ln -s service %{buildroot}%{_sbindir}/rckexec-load
#UsrMerge
mkdir -p %{buildroot}/sbin
ln -s %{_sbindir}/kexec %{buildroot}/sbin
#EndUsrMerge

%post
%service_add_post kexec-load.service
%{?regenerate_initrd_post}

%postun
%service_del_postun kexec-load.service
%{?regenerate_initrd_post}

%pre
%service_add_pre kexec-load.service

%preun
%service_del_preun kexec-load.service

%posttrans
%{?regenerate_initrd_posttrans}

# Compatibility cruft
# there is no %license prior to SLE12
%if %{undefined _defaultlicensedir}
%define license %doc
%else
# filesystem before SLE12 SP3 lacks /usr/share/licenses
%if 0%(test ! -d %{_defaultlicensedir} && echo 1)
%define _defaultlicensedir %_defaultdocdir
%endif
%endif
# End of compatibility cruft

%files
%license COPYING
%doc AUTHORS News TODO doc
%{_mandir}/man*/*
#UsrMerge
/sbin/kexec
#EndUsrMerge
%{_sbindir}/rckexec-load
%{_sbindir}/kexec
%{_sbindir}/kexec-bootloader
%{_sbindir}/vmcore-dmesg
%{_unitdir}/kexec-load.service

%changelog
