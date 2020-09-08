#
# spec file for package memcached
#
# Copyright (c) 2020 SUSE LLC
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

%if 0%{?suse_version} > 1500
%bcond_without tls
%else
%bcond_with    tls
%endif

Name:           memcached
Version:        1.6.6
Release:        0
Summary:        A high-performance, distributed memory object caching system
License:        BSD-3-Clause
Group:          Productivity/Networking/Other
URL:            http://memcached.org/
Source:         http://www.memcached.org/files/%{name}-%{version}.tar.gz
Source1:        %{name}.init
Source2:        %{name}.sysconfig
Source3:        memcached-rpmlintrc
Source4:        memcached.service
# PATCH-FIX-UPSTREAM gh#memcached/memcached#691
Patch:          use-signal-function-instead-of-sigignore.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  cyrus-sasl-devel
BuildRequires:  libevent-devel >= 2.0
BuildRequires:  libtool
%if %{with tls}
BuildRequires:  openssl-devel >= 1.1.0
BuildRequires:  perl-IO-Socket-SSL
BuildRequires:  perl-Net-SSLeay
%endif
BuildRequires:  pkgconfig
Requires(pre):  %fillup_prereq
Requires(pre):  %{_sbindir}/groupadd
Requires(pre):  %{_sbindir}/useradd
Conflicts:      memcached-unstable
%if 0%{?suse_version} > 1210
BuildRequires:  systemd-rpm-macros
%{?systemd_requires}
%else
Requires(pre):  %insserv_prereq
%endif

%description
Memcached is a high-performance, distributed memory object caching
system, generic in nature, but intended for use in speeding up dynamic
web applications by alleviating database load.

Danga Interactive developed memcached to enhance the speed of
LiveJournal.com, a site which was already doing 20 million+ dynamic
page views per day for 1 million users with a bunch of webservers and a
bunch of database servers. memcached dropped the database load to
almost nothing, yielding faster page load times for users, better
resource utilization, and faster access to the databases on a memcache
miss.

%package devel
Summary:        Files needed for development using memcached protocol
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

%description devel
Memcached is a high-performance, distributed memory object caching
system, generic in nature, but intended for use in speeding up dynamic
web applications by alleviating database load.

This package contains development files

%prep
%setup -q
%patch -p1

%build
autoreconf -fi
%configure \
%if %{with tls}
  --enable-tls \
%endif
  --enable-sasl \
  --enable-sasl-pwdb \
  --enable-seccomp \
  --disable-coverage \
  %ifarch s390 s390x ppc ppc64
  --disable-extstore \
  %endif
  --bindir=%{_sbindir}

make %{?_smp_mflags}

%install
%make_install
install -D  -m 0755 scripts/memcached-tool %{buildroot}%{_sbindir}/memcached-tool
install -Dd -m 0751 %{buildroot}%{_localstatedir}/lib/%{name}
install -D  -m 0644 %{SOURCE2} %{buildroot}%{_fillupdir}/sysconfig.%{name}
%if  0%{?suse_version} > 1210
ln -s  	%{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}
install -D  -m 0644 %{SOURCE4} %{buildroot}%{_unitdir}/%{name}.service
%else
install -D  -m 0755 %{SOURCE1} %{buildroot}%{_sysconfdir}/init.d/%{name}
ln -s  ../..%{_sysconfdir}/init.d/%{name} %{buildroot}%{_sbindir}/rc%{name}
%endif

%check
make %{?_smp_mflags} test

%pre
%{_sbindir}/groupadd -r %{name} >/dev/null 2>&1 || :
%{_sbindir}/useradd -g %{name} -s /bin/false -r -c "user for %{name}" -d %{_localstatedir}/lib/%{name} %{name} >/dev/null 2>&1 || :
%if 0%{?suse_version} > 1210
%service_add_pre %{name}.service
%endif

%post
%if 0%{?suse_version} > 1210
%service_add_post %{name}.service
%fillup_only %{name}
%else
%fillup_and_insserv %{name}
%endif

%preun
%if 0%{?suse_version} > 1210
%service_del_preun %{name}.service
%else
%stop_on_removal %{name}
%endif

%postun
%if 0%{?suse_version} > 1210
%service_del_postun %{name}.service
%else
%restart_on_update %{name}
%insserv_cleanup
%endif

%files
%doc AUTHORS ChangeLog NEWS
%license COPYING
%{_sbindir}/%{name}
%{_sbindir}/memcached-tool
%{_sbindir}/rc%{name}
%{_mandir}/man1/%{name}.*
%if 0%{?suse_version} > 1210
%{_unitdir}/%{name}.service
%else
%{_sysconfdir}/init.d/%{name}
%endif
%{_fillupdir}/sysconfig.%{name}
%dir %attr(751,root,root) %{_localstatedir}/lib/%{name}

%files devel
%doc AUTHORS ChangeLog NEWS doc/*.txt
%license COPYING
%{_includedir}/%{name}

%changelog
