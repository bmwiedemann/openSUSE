#
# spec file for package munge
#
# Copyright (c) 2019 SUSE LLC
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

%if 0%{?suse_version} >= 1210
%define have_systemd 1
%endif
%define lversion 2

%define munge_g %name
%if 0%{?have_systemd}
 %define munge_u %name
%else
 %define munge_u daemon
%endif

Name:           munge
Version:        0.5.13
Release:        0
Summary:        An authentication service for creating and validating credentials
License:        GPL-3.0-or-later AND LGPL-3.0-or-later
Group:          Productivity/Security
URL:            http://dun.github.io/munge/
Source0:        https://github.com/dun/munge/archive/%{name}-%{version}.tar.gz
Source1:        baselibs.conf
Source2:        sysconfig.munge
Source3:        README.SUSE
Patch0:         Make-SUSE-specific-adjustments.patch
BuildRequires:  libbz2-devel
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  zlib-devel
%if 0%{?suse_version} <= 1140
Requires(pre):  pwdutils
%else
Requires(pre):  shadow
%endif
%if 0%{?have_systemd}
BuildRequires:  systemd
BuildRequires:  systemd-rpm-macros
%{?systemd_requires}
%endif
Requires(post):     coreutils
Requires(postun):   coreutils
%if 0%{?suse_version} < 1310
%{!?_tmpfilesdir:%global _tmpfilesdir /usr/lib/tmpfiles.d}
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
MUNGE (MUNGE Uid 'N' Gid Emporium) is an authentication service for creating
and validating credentials.  It is designed to be highly scalable for use
in an HPC cluster environment.  It allows a process to authenticate the
UID and GID of another local or remote process within a group of hosts
having common users and groups.  These hosts form a security realm that is
defined by a shared cryptographic key.  Clients within this security realm
can create and validate credentials without the use of root privileges,
reserved ports, or platform-specific methods.

%package -n lib%{name}%{lversion}
Summary:        Libraries for applications using MUNGE
Group:          System/Libraries
Recommends:     munge

%description -n lib%{name}%{lversion}
A shared library for applications using the MUNGE authentication service.

%package devel
Requires:       lib%{name}%{lversion} = %{version}
Summary:        Headers and Libraries for building applications using %{name}
Group:          Development/Libraries/C and C++

%description devel
A header file and libraries for building applications using the %{name} 
authenication service.

%prep
%setup -n %{name}-%{name}-%{version}
%patch0 -p1
cp %{SOURCE3} .

%build
%configure
make %{?_smp_mflags}

%install
%makeinstall
rm -f %{buildroot}%{_libdir}/*.la
rm -f %{buildroot}%{_libdir}/*.a
rm -f %{buildroot}%{_sysconfdir}/sysconfig/munge

# We don't want systemd file on SLE 11
%if 0%{!?have_systemd:1}
   test -d %{buildroot}%{_prefix}/lib/systemd && \
      rm -rf %{buildroot}%{_prefix}/lib/systemd
   test -f %{buildroot}/lib/systemd/system/munge.service && \
      rm -f %{buildroot}/lib/systemd/system/munge.service
   rm -f %{buildroot}/%{_tmpfilesdir}/munge.conf
   sed -i 's/USER="munge"/USER="%munge_u"/g' %{buildroot}/%{_initrddir}/%{name}
   ln -s -f %{_initrddir}/%{name} %{buildroot}%{_sbindir}/rc%{name}
   install -m 0755 -d %{buildroot}%{_fillupdir}
   cp -p %{S:2} %{buildroot}%{_fillupdir}/sysconfig.munge
%else
  sed -i 's/User=munge/User=%munge_u/g' %{buildroot}%{_unitdir}/munge.service
  sed -i 's/Group=munge/Group=%munge_g/g' %{buildroot}%{_unitdir}/munge.service
  sed -i 's/munge \+munge/%munge_u %munge_g/g' %{buildroot}%{_tmpfilesdir}/munge.conf
  rm -f %{buildroot}%{_initddir}/munge
  rmdir %{buildroot}%{_localstatedir}/run/munge
  ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}
%endif

%post -n lib%{name}%{lversion} -p /sbin/ldconfig

%postun -n lib%{name}%{lversion} -p /sbin/ldconfig

%pre
%if 0%{?have_systemd}
%service_add_pre munge.service
%endif
%define munge_home "%_localstatedir%_rundir/munge"
%define munge_descr "MUNGE authentication service"
getent group %munge_g >/dev/null || groupadd -r %munge_g
getent passwd %munge_u >/dev/null || useradd -r -g %munge_g -d %munge_home -s /bin/false -c %munge_descr %munge_u
exit 0

%preun
%if 0%{?have_systemd}
%service_del_preun munge.service
%else
%stop_on_removal munge
%endif

%define fixperm() [ -e %1 ] && /bin/chown -h %munge_u:%munge_g %1
%postun
if [ $1 -eq 1 ]
then
    %{fixperm %{_localstatedir}/log/munge}
    %{fixperm %{_localstatedir}/log/munge/munged.log}
    %{fixperm %{_localstatedir}/run/munge}
fi
%if 0%{?have_systemd}
%service_del_postun munge.service
%else
%restart_on_update munge
%insserv_cleanup
%endif

%post
if [ $1 -eq 1 ]
then
    %{fixperm %{_localstatedir}/log/munge}
    %{fixperm %{_localstatedir}/log/munge/munged.log}
    %{fixperm %{_localstatedir}/run/munge}
fi
unset tmpfile
tmpdir=$(mktemp -d /tmp/tmpdir-XXXXXXXXX)
if [ -e %{_sysconfdir}/munge/munge.key ]; then 
    # Preserve symlink so we can check for it
    cp -pP %{_sysconfdir}/munge/munge.key ${tmpdir}
fi
# Make sure this is no symlinks - this may have been created by an attacker!
if [ -e ${tmpdir}/munge.key -a ! -h ${tmpdir}/munge.key ]; then
    if [ $(/usr/bin/stat -c %U:%G:%a ${tmpdir}/munge.key) != \
    %munge_u:%munge_g:400 ]; then
	tmpfile=${tmpdir}/munge.key
    fi
else
    /usr/bin/rm -f ${tmpdir}/munge.key
    if [ -c /dev/urandom ]; then
	tmpfile=${tmpdir}/munge.key
	/bin/dd if=/dev/urandom bs=1 count=1024 > $tmpfile 2>/dev/null
    fi
fi
if [ -n "$tmpfile" ]; then
    /bin/chmod 0400 $tmpfile
    /bin/chown -h %munge_u:%munge_g $tmpfile
    /bin/mv -f $tmpfile %{_sysconfdir}/munge/munge.key
fi
/usr/bin/rm -rf ${tmpdir}
%if 0%{?have_systemd}
%service_add_post munge.service
systemd-tmpfiles --create %{_tmpfilesdir}/munge.conf
%else
%{fillup_and_insserv -i munge}
%endif

%files
%defattr(-,root,root,0755)
%doc AUTHORS
%license COPYING
%doc DISCLAIMER*
%doc HISTORY
%doc JARGON
%doc NEWS
%doc PLATFORMS
%doc QUICKSTART
%doc README
%doc TODO
%doc README.SUSE
%doc doc/*
%dir %attr(0700,%munge_u,%munge_g) %config %{_sysconfdir}/munge
%dir %attr(0711,%munge_u,%munge_g) %config %{_localstatedir}/lib/munge
%dir %attr(0700,%munge_u,%munge_g) %config %{_localstatedir}/log/munge
%{_bindir}/*
%{_sbindir}/*
%{_mandir}/*[^3]/*
%if 0%{?have_systemd}
%{_unitdir}/munge.service
%{_tmpfilesdir}/munge.conf
%else
%{_fillupdir}/sysconfig.munge
%attr(0755,%munge_u,%munge_g) %dir %{_localstatedir}/run/%{name}
%{_initddir}/munge
%endif

%files devel
%defattr(-,root,root,0755)
%{_includedir}/*
%{_mandir}/*3/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%files -n lib%{name}%{lversion}
%defattr(-,root,root,0755)
%{_libdir}/*.so.*

%changelog
