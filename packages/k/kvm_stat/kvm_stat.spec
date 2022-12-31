#
# spec file for package kvm_stat
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


Name:           kvm_stat
%define version %(rpm -q --qf '%%{VERSION}' kernel-source)
Version:        %{version}
Release:        0
Summary:        Monitoring Tool for KVM guests
License:        GPL-2.0-only
Group:          System/Monitoring
URL:            http://www.kernel.org/
BuildArch:      noarch
BuildRequires:  asciidoc
BuildRequires:  kernel-source >= 5.2.0
BuildRequires:  libxslt-tools

Requires:       python3-curses
Recommends:     logrotate

Recommends:     kernel >= 5.2.0
Conflicts:      qemu < 2.6.90
Conflicts:      qemu-kvm < 2.6.90
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

# Patches 01 to 07 are for jsc#SLE-13784
Source1:        logrotate.kvm_stat
Patch01:        rework-command-line-sequence.patch
Patch02:        switch-to-argparse.patch
Patch03:        add-command-line-switch-s-to-update.patch
Patch04:        add-command-line-switch-c-to-csv.patch
Patch05:        add-command-line-switch-z-skip-zero-records.patch
Patch06:        add-command-line-switch-L-to-log-file.patch
Patch07:        add-sample-systemd-unit.patch
Patch08:        add-restart-delay.patch
# PAtch 09 is for bsc#1202924
Patch09:        tools-kvm_stat-fix-attack-vector-with-user-controlle.patch

%define XXX This package provides a userspace tool "kvm_stat", which displays KVM vm exit \
information as a means of monitoring vm behavior. The data is taken from the\
KVM debugfs files or the vm tracepoints and outputs them as a curses ui or\
simple text.

%description
%{XXX}

%package rebuild
Summary:        Empty package to ensure rebuilding kvm_stat in OBS
Group:          System/Monitoring
%requires_eq kernel-source

%description rebuild
This is empty package that ensures kvm_stat is rebuilt every time
kernel-default is rebuilt in OBS.

There is no reason to install this package.

%prep
# copy necessary files from kernel-source
(tar -C /usr/src/linux -c COPYING tools scripts) | tar -x

# Patches present upstream, since 5.7
%if "%(echo `echo -e "%{version}\\n5.7.0" | sort -V | head -n1 2> /dev/null`)" != "5.7.0"
%patch01 -p1
%patch02 -p1
%patch03 -p1
%patch04 -p1
%endif
# Patches present upstream, since 5.8
%if "%(echo `echo -e "%{version}\\n5.8.0" | sort -V | head -n1 2> /dev/null`)" != "5.8.0"
%patch05 -p1
%patch06 -p1
%patch07 -p1
%patch08 -p1
%endif
%if %{pkg_vcmp kernel-source < 6.1}
%patch09 -p1
%endif

%build
make -C tools/kvm/kvm_stat %{?_smp_mflags}

%install
# OBS checks don't like /usr/bin/env in script interpreter lines
sed -re '1 { s_^#! */usr/bin/env +/_#!/_ ; s_^#! */usr/bin/env +([^/])_#!/usr/bin/\1_ }' -i "tools/kvm/kvm_stat/kvm_stat"
make -C tools kvm_stat_install INSTALL_ROOT=%{buildroot}
%if 0%{?suse_version} > 1500
mkdir -p %{buildroot}%{_distconfdir}/logrotate.d
install -D -m 644 %{SOURCE1} %{buildroot}%{_distconfdir}/logrotate.d/kvm_stat
%else
install -D -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/logrotate.d/kvm_stat
%endif
install -D -m 644 tools/kvm/kvm_stat/kvm_stat.service %{buildroot}%{_unitdir}/kvm_stat.service
install -d %{buildroot}%{_sbindir}
ln -sf service %{buildroot}%{_sbindir}/rckvm_stat

%pre
%service_add_pre kvm_stat.service
%if 0%{?suse_version} > 1500
# Prepare for migration to /usr/etc; save any old .rpmsave
for i in logrotate.d/kvm_stat ; do
   test -f %{_sysconfdir}/${i}.rpmsave && mv -v %{_sysconfdir}/${i}.rpmsave %{_sysconfdir}/${i}.rpmsave.old ||:
done
%endif

%if 0%{?suse_version} > 1500
%posttrans
# Migration to /usr/etc, restore just created .rpmsave
for i in logrotate.d/kvm_stat ; do
   test -f %{_sysconfdir}/${i}.rpmsave && mv -v %{_sysconfdir}/${i}.rpmsave %{_sysconfdir}/${i} ||:
done
%endif

%post
%service_add_post kvm_stat.service

%preun
%service_del_preun kvm_stat.service

%postun
%service_del_postun kvm_stat.service

%files
%defattr(-, root, root)
%license COPYING
%{_unitdir}/kvm_stat.service
%if 0%{?suse_version} > 1500
%{_distconfdir}/logrotate.d/kvm_stat
%else
%config(noreplace) %{_sysconfdir}/logrotate.d/kvm_stat
%endif
%{_sbindir}/rckvm_stat
%{_bindir}/kvm_stat
%{_mandir}/man1/kvm_stat*

%files rebuild
%license COPYING

%changelog
