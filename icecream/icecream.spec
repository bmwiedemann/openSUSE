#
# spec file for package icecream
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir %{_localstatedir}/adm/fillup-templates
%endif
Name:           icecream
Version:        1.2
Release:        0
Summary:        For Distributed Compile in the Network
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Development/Tools/Building
URL:            https://github.com/icecc/icecream
Source0:        https://github.com/icecc/icecream/archive/%{version}.tar.gz
Source1:        iceccd.xml
Source2:        iceccd.service
Source3:        iceccd-wrapper
Source4:        icecc-scheduler.xml
Source5:        icecc-scheduler.service
Source6:        icecc-scheduler-wrapper
Source7:        icecream-tmpfiles.conf
Source8:        sysconfig.icecream
BuildRequires:  docbook2x
BuildRequires:  firewall-macros
BuildRequires:  gcc-c++
BuildRequires:  libcap-ng-devel
BuildRequires:  libtool
BuildRequires:  libxslt-tools
BuildRequires:  lzo-devel
BuildRequires:  systemd-rpm-macros
Requires:       %{_bindir}/bzip2
Requires:       /bin/tar
Requires:       logrotate
Requires(pre):  %fillup_prereq
Requires(pre):  %{_sbindir}/groupadd
Requires(pre):  %{_sbindir}/useradd
%{?systemd_requires}
Recommends:     gcc-c++
%if 0%{?suse_version} > 1315
BuildRequires:  clang-devel
%endif

%description
Distributed compiler with a central scheduler to share build load.

%package -n libicecream-devel
Summary:        For Distributed Compile in the Network
Group:          Development/Tools/Building
Requires:       libcap-ng-devel
Requires:       libstdc++-devel
Requires:       lzo-devel

%description -n libicecream-devel
icecream is the next generation distcc.

%package -n icecream-clang-wrappers
Summary:        Distributed Compile Wrappers for Clang
Group:          Development/Tools/Building
Requires:       clang
Requires:       icecream
Supplements:    packageand(icecream:clang)

%description -n icecream-clang-wrappers
Wrapper symlinks for clang/clang++ for icecream distributed building.

%prep
%setup -q
cp %{SOURCE8} suse/
# DO NOT ADD PATCHES without github reference

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
autoreconf -fiv
%configure \
  --enable-clang-rewrite-includes \
  --enable-clang-wrappers \
  --libexecdir %{_libexecdir}
make %{?_smp_mflags} V=1

%install
%make_install templatesdir=%{_fillupdir}
# firewalld instead of SuSEfirewall2
rm -R %{buildroot}/%{_sysconfdir}/sysconfig/SuSEfirewall2.d
install -m644 -p -D %{SOURCE1} %{buildroot}%{_libexecdir}/firewalld/services/iceccd.xml
install -m644 -p -D %{SOURCE4} %{buildroot}%{_libexecdir}/firewalld/services/icecc-scheduler.xml
# unit files and wrappers
install -m644 -p -D %{SOURCE2} %{buildroot}%{_unitdir}/iceccd.service
install -m755 -p -D %{SOURCE3} %{buildroot}%{_libexecdir}/icecc/iceccd-wrapper
install -m644 -p -D %{SOURCE5} %{buildroot}%{_unitdir}/icecc-scheduler.service
install -m755 -p -D %{SOURCE6} %{buildroot}%{_libexecdir}/icecc/icecc-scheduler-wrapper
# make sure runtime directories are automatically created
install -m644 -p -D %{SOURCE7} %{buildroot}/%{_tmpfilesdir}/icecream.conf
# cleanup SysV init
rm %{buildroot}/%{_sysconfdir}/init.d/icecream
rm %{buildroot}/%{_sbindir}/rcicecream
ln -s service %{buildroot}/%{_sbindir}/rciceccd
ln -s service %{buildroot}/%{_sbindir}/rcicecc-scheduler
sed -i -e '1s@/usr/bin/env bash@/bin/bash@'  %{buildroot}/%{_bindir}/icecc-create-env

%preun
%service_del_preun iceccd.service icecc-scheduler.service

%pre
%{_sbindir}/groupadd -r icecream 2> /dev/null || :
%{_sbindir}/useradd -r -g icecream -s /bin/false -c "Icecream Daemon" -d %{_localstatedir}/cache/icecream icecream 2> /dev/null || :
%service_add_pre iceccd.service icecc-scheduler.service
# save state of old icecream SysV service
if [ "$1" -gt 1 ]; then
  /usr/sbin/systemd-sysv-convert --save icecream || :
fi

%post
%if 0%{?suse_version}
%fillup_only
%endif
%tmpfiles_create %_tmpfilesdir/icecream.conf
%firewalld_reload
# migrate runlevel settings
if [ "$1" -gt 1 ] && [ -e /var/lib/systemd/sysv-convert/database ] ; then
    grep -q 'ICECREAM_RUN_SCHEDULER="yes"' %{_sysconfdir}/sysconfig/icecream &&
        sed -i -e '/icecream\s/ p; s/icecream\s/icecc-scheduler /' /var/lib/systemd/sysv-convert/database
    sed -i -e '/icecream\s/ s/icecream\s/iceccd /' /var/lib/systemd/sysv-convert/database
fi
%service_add_post iceccd.service icecc-scheduler.service
# restart services
if [ "$1" -gt 1 ] ; then
    if systemctl -q is-active icecream ; then
        systemctl stop icecream
        systemctl start iceccd
        systemctl -q is-enabled icecc-scheduler && systemctl start icecc-scheduler
    fi
fi

%postun
%service_del_postun iceccd.service icecc-scheduler.service

%files
%doc README.md NEWS
%license COPYING
%config %{_sysconfdir}/logrotate.d/icecream
%{_bindir}/icecc-create-env
%{_bindir}/icecc-test-env
%{_bindir}/icecc
%{_bindir}/icerun
%{_sbindir}/icecc-scheduler
%{_sbindir}/iceccd
%{_sbindir}/rcicecc*
%{_mandir}/man*/*
%{_libexecdir}/icecc
%exclude %{_libexecdir}/icecc/bin/clang
%exclude %{_libexecdir}/icecc/bin/clang++
%dir %{_libexecdir}/firewalld/
%dir %{_libexecdir}/firewalld/services/
%{_libexecdir}/firewalld/services/icecc*.xml
%{_unitdir}/icecc*.service
%{_tmpfilesdir}/icecream.conf
%if 0%{?suse_version}
%{_fillupdir}/sysconfig.icecream
%endif
%attr(-,icecream,icecream) %{_localstatedir}/cache/icecream
%attr(-,icecream,icecream) %{_localstatedir}/log/icecream
%ghost /run/icecc

%files -n libicecream-devel
%{_includedir}/icecc
%{_libdir}/libicecc.*
%{_libdir}/pkgconfig/icecc.pc

%files -n icecream-clang-wrappers
%{_libexecdir}/icecc/bin/clang
%{_libexecdir}/icecc/bin/clang++

%changelog
