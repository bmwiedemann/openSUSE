#
# spec file for package memcached
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


#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir %{_localstatedir}/adm/fillup-templates
%endif
%if 0%{?suse_version} > 1500
%bcond_without tls
%else
%bcond_with    tls
%endif
%if 0%{?suse_version} >= 1500
%bcond_without sysusers
%bcond_without tmpfiles
%else
%bcond_with    sysusers
%bcond_with    tmpfiles
%endif
Name:           memcached
Version:        1.6.38
Release:        0
Summary:        A high-performance, distributed memory object caching system
License:        BSD-3-Clause
Group:          Productivity/Networking/Other
URL:            https://memcached.org/
Source:         https://www.memcached.org/files/%{name}-%{version}.tar.gz
Source2:        %{name}.sysconfig
Source4:        memcached.service
Source5:        %{name}-sysusers.conf
Source6:        %{name}-tmpfiles.conf
Patch0:         harden_memcached.service.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  cyrus-sasl-devel
BuildRequires:  libevent-devel >= 2.0
BuildRequires:  libtool
BuildRequires:  pkgconfig
Requires(pre):  %fillup_prereq
Conflicts:      memcached-unstable
%if %{with tls}
BuildRequires:  openssl-devel >= 1.1.0
BuildRequires:  perl
BuildRequires:  perl-IO-Socket-SSL
BuildRequires:  perl-Net-SSLeay
%endif
%if %{with sysusers}
BuildRequires:  sysuser-tools
%sysusers_requires
%else
Requires(pre):  %{_sbindir}/groupadd
Requires(pre):  %{_sbindir}/useradd
%endif
%if 0%{?suse_version} > 1210
BuildRequires:  systemd-rpm-macros
%{?systemd_ordering}
%else
Requires(pre):  %insserv_prereq
%endif

%description
Memcached is a high-performance, distributed memory object caching
system, generic in nature, but intended for use in speeding up dynamic
web applications by alleviating database load.

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
%autosetup -p1

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
  --disable-extstore
  %endif

%make_build
%if %{with sysusers}
%sysusers_generate_pre %{SOURCE5} %{name} %{name}-user.conf
%endif

%install
%make_install
install -D  -m 0755 scripts/memcached-tool %{buildroot}%{_bindir}/memcached-tool
install -Dd -m 0751 %{buildroot}%{_localstatedir}/lib/%{name}
install -D  -m 0644 %{SOURCE2} %{buildroot}%{_fillupdir}/sysconfig.%{name}
install -d -m 755 %{buildroot}%{_sbindir}
ln -s  	%{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}
install -D  -m 0644 %{SOURCE4} %{buildroot}%{_unitdir}/%{name}.service
%if %{with sysusers}
install -D -m 0644 %{SOURCE5} %{buildroot}%{_sysusersdir}/%{name}-user.conf
%endif
%if %{with tmpfiles}
install -D -m 0644 %{SOURCE6} %{buildroot}%{_tmpfilesdir}/%{name}.conf
%endif

%check
%ifarch s390x
# bsc#1243673
rm t/ssl_session_resumption.t
%endif
%make_build test

%if %{with sysusers}
%pre -f memcached.pre
%else

%pre
getent group %{name} >/dev/null || \
	%{_sbindir}/groupadd -r %{name}
getent passwd %{name} >/dev/null || \
	%{_sbindir}/useradd -g %{name} -s /bin/false -r \
	-c "user for %{name}" -d %{_localstatedir}/lib/%{name} %{name}
%endif
%service_add_pre %{name}.service

%post
%service_add_post %{name}.service
%fillup_only %{name}
%if %{with tmpfiles}
%tmpfiles_create %{_tmpfilesdir}/%{name}.conf
%endif

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%files
%doc AUTHORS ChangeLog NEWS
%license COPYING
%{_bindir}/%{name}
%{_bindir}/memcached-tool
%{_sbindir}/rc%{name}
%{_mandir}/man1/%{name}.*
%{_unitdir}/%{name}.service
%{_fillupdir}/sysconfig.%{name}
%dir %attr(751,root,root) %{_localstatedir}/lib/%{name}
%if %{with sysusers}
%{_sysusersdir}/%{name}-user.conf
%endif
%if %{with tmpfiles}
%{_tmpfilesdir}/%{name}.conf
%dir %ghost %{_rundir}/%{name}
%endif

%files devel
%doc AUTHORS ChangeLog NEWS doc/*.txt
%license COPYING
%{_includedir}/%{name}

%changelog
