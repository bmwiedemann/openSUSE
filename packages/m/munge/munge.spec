#
# spec file for package munge
#
# Copyright (c) 2026 SUSE LLC and contributors
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
  %define _fillupdir /var/adm/fillup-templates
%endif

%define lversion 2

%define munge_g %name
%define munge_u %name

Name:           munge
Version:        0.5.18
Release:        0
Summary:        An authentication service for creating and validating credentials
License:        GPL-3.0-or-later AND LGPL-3.0-or-later
Group:          Productivity/Security
URL:            https://dun.github.io/munge/
Source0:        https://github.com/dun/munge/archive/%{name}-%{version}.tar.gz
Source1:        baselibs.conf
Source2:        sysconfig.munge
Source3:        README.SUSE
Patch0:         Make-SUSE-specific-adjustments.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libbz2-devel
BuildRequires:  libtool
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
# For %%check
BuildRequires:  procps
BuildRequires:  zlib-devel
Requires:       logrotate
%if 0%{?suse_version} <= 1140
Requires(pre):  pwdutils
%else
Requires(pre):  shadow
%endif
Requires(post): coreutils
BuildRequires:  systemd-rpm-macros
BuildRequires:  sysuser-tools
BuildRequires:  pkgconfig(systemd)
%{?systemd_requires}
Requires(post): coreutils
Requires(postun): coreutils

%description
MUNGE (MUNGE Uid 'N' Gid Emporium) is an authentication service for
creating and validating user credentials.  It is designed to be highly
scalable for use in an HPC cluster environment.  It provides a portable
API for encoding the user's identity into a tamper-proof credential
that can be obtained by an untrusted client and forwarded by untrusted
intermediaries within a security realm.  Clients within this realm can
create and validate credentials without the use of root privileges,
reserved ports, or platform-specific methods.

%package -n lib%{name}%{lversion}
Summary:        Libraries for applications using MUNGE
Group:          System/Libraries
Recommends:     munge
# For compatibility with the MUNGE upstream SPEC file.
Provides:       munge-libs = %version

%description -n lib%{name}%{lversion}
A shared library for applications using the MUNGE authentication service.

%package devel
Requires:       lib%{name}%{lversion} = %{version}
Summary:        Headers and Libraries for building applications using %{name}
Group:          Development/Libraries/C and C++

%description devel
A header file and libraries for building applications using the %{name}
authenication service.

%{!?_rundir:%define _rundir %_localstatedir/run}
%define munge_run %_rundir/munge

%prep
%setup -n %{name}-%{name}-%{version}
%autopatch -p1

cp %{SOURCE3} .

%build
./bootstrap
%configure --disable-static \
    --with-crypto-lib=openssl \
    --with-logrotateddir=%{_sysconfdir}/logrotate.d \
    --with-pkgconfigdir=%{_libdir}/pkgconfig \
    --with-systemdunitdir=%{_unitdir} \
    --with-runstatedir=%{_rundir}
%if 0%{!?make_build:1}
%define make_build make %{?_smp_mflags}
%endif
%make_build

%install
%makeinstall
rm -f %{buildroot}%{_libdir}/*.la
rm -f %{buildroot}%{_libdir}/*.a

mkdir -p %{buildroot}%{_datarootdir}/licenses

install -m 0755 -d %{buildroot}%{_fillupdir}
sed -i -e "/missingok/a\ \ \ \ su munge munge" %{buildroot}/%{_sysconfdir}/logrotate.d/munge
# We don't want systemd file on SLE 11
  sed -i 's/User=munge/User=%munge_u/g' %{buildroot}%{_unitdir}/munge.service
  sed -i 's/Group=munge/Group=%munge_g/g' %{buildroot}%{_unitdir}/munge.service
  rm -f %{buildroot}%{_initddir}/munge
  rm -Rf %{buildroot}/%{munge_run}
  rm -Rf %{buildroot}/%{_rundir}
  ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}
  mv %{buildroot}%{_sysconfdir}/sysconfig/munge \
     %{buildroot}%{_fillupdir}/sysconfig.munge
  sed -i -e 's/^\(u \)[^ ]*\(.*\)/\1%munge_u\2/' %{buildroot}%{_sysusersdir}/%{name}.conf
  %sysusers_generate_pre %{buildroot}%{_sysusersdir}/%{name}.conf %{name} %{name}.conf

%check
# To debug add verbose=t to T_LOG_DRIVER variable in t/Makefile.am
make check

%post -n lib%{name}%{lversion} -p /sbin/ldconfig

%postun -n lib%{name}%{lversion} -p /sbin/ldconfig

%pre -f %{name}.pre
%service_add_pre munge.service

%preun
%service_del_preun munge.service

%define fixperm() [ -e %1 ] && /bin/chown -h %munge_u:%munge_g %1

%postun
if [ $1 -eq 1 ]
then
    %{fixperm %{_localstatedir}/log/munge}
    %{fixperm %{_localstatedir}/log/munge/munged.log}
    %{fixperm %munge_run}
else
    rm -f %{_sysconfdir}/munge/munge.key
fi
%service_del_postun munge.service

%post
if [ $1 -eq 1 ]
then
    %{fixperm %{_localstatedir}/log/munge}
    %{fixperm %{_localstatedir}/log/munge/munged.log}
    %{fixperm %munge_run}
fi
# This matches ' su  foo bar' as well as '  su=foo bar
grep -qE "^ *su" %{_sysconfdir}/logrotate.d/munge || \
    sed -i -e "/missingok/a\ \ \ \ su munge munge" %{_sysconfdir}/logrotate.d/munge
unset tmpfile
tmpdir=$(mktemp -d /tmp/tmpdir-XXXXXXXXX)
if [ -e %{_sysconfdir}/munge/munge.key ]; then
    # Preserve symlink so we can check for it
    cp -pP %{_sysconfdir}/munge/munge.key ${tmpdir}
fi
# Make sure this is no symlinks - this may have been created by an attacker!
if [ -e ${tmpdir}/munge.key -a ! -h ${tmpdir}/munge.key ]; then
    if [ $(/usr/bin/stat -c %U:%G:%a ${tmpdir}/munge.key) != \
    %munge_u:%munge_g:600 ]; then
	tmpfile=${tmpdir}/munge.key
    fi
else
    /usr/bin/rm -f ${tmpdir}/munge.key
    tmpfile=${tmpdir}/munge.key
    /usr/sbin/mungekey -c -b 8192 -k $tmpfile
fi
if [ -n "$tmpfile" ]; then
    /bin/chmod 0600 $tmpfile
    /bin/chown -h %munge_u:%munge_g $tmpfile
    /bin/mv -f $tmpfile %{_sysconfdir}/munge/munge.key
fi
/usr/bin/rm -rf ${tmpdir}
%service_add_post munge.service
%{fillup_only}

%files
%doc AUTHORS
%if 0%{?suse_version} < 1500
%dir %{_datarootdir}/licenses
%endif
%license COPYING
%doc DISCLAIMER*
%doc HISTORY
%doc JARGON
%doc NEWS
%doc PLATFORMS
%doc QUICKSTART
%doc README
%doc README.SUSE
%doc doc/*
%dir %attr(0700,%munge_u,%munge_g) %{_sysconfdir}/munge
%attr(0600,%munge_u,%munge_g) %config(noreplace) %ghost %{_sysconfdir}/munge/munge.key
%config(noreplace) %{_sysconfdir}/logrotate.d/munge
# bsc#1173167
#%%config(noreplace) %%ghost %%{_sysconfdir}/sysconfig/munge
%{_fillupdir}/sysconfig.munge
%dir %attr(0711,%munge_u,%munge_g) %{_localstatedir}/lib/munge
%attr(0600,%munge_u,%munge_g) %ghost %{_localstatedir}/lib/munge/munged.seed
%dir %attr(0700,%munge_u,%munge_g) %{_localstatedir}/log/munge
%attr(0640,%munge_u,%munge_g) %ghost %{_localstatedir}/log/munge/munged.log
%{_bindir}/*
%{_sbindir}/*
%{_mandir}/*[^3]/*
%dir %attr(0755,%munge_u,%munge_g) %ghost %{munge_run}
%{_unitdir}/munge.service
%dir %attr(0755,munge,munge) %ghost %{munge_run}/munged.pid
%{_sysusersdir}/%{name}.conf

%files devel
%{_includedir}/*
%{_mandir}/*3/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%files -n lib%{name}%{lversion}
%{_libdir}/*.so.*

%changelog
