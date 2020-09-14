#
# spec file for package redis
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


%define _data_dir       %{_localstatedir}/lib/%{name}
%define _log_dir        %{_localstatedir}/log/%{name}
%define _conf_dir       %{_sysconfdir}/%{name}
Name:           redis
Version:        6.0.8
Release:        0
Summary:        Persistent key-value database
License:        BSD-3-Clause
URL:            https://redis.io
Source0:        http://download.redis.io/releases/redis-%{version}.tar.gz
Source1:        %{name}.logrotate
Source2:        %{name}.target
Source3:        %{name}@.service
Source4:        %{name}.tmpfiles.d
Source5:        README.SUSE
Source6:        %{name}.sysctl
Source7:        %{name}-sentinel@.service
Source8:        %{name}-sentinel.target
Source9:        %{name}-user.conf
Source10:       https://raw.githubusercontent.com/redis/redis-hashes/master/README#/redis.hashes
# PATCH-MISSING-TAG -- See https://wiki.opensuse.org/openSUSE:Packaging_Patches_guidelines
Patch0:         %{name}-conf.patch
Patch1:         getMcontextEip-return-value.patch
Patch3:         reproducible.patch
Patch4:         ppc-atomic.patch
BuildRequires:  pkgconfig
BuildRequires:  sysuser-shadow
BuildRequires:  sysuser-tools
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(systemd)
Recommends:     logrotate
%sysusers_requires

%description
%{name} is an advanced key-value store. It is similar to memcached but the dataset
is not volatile, and values can be strings, exactly like in memcached,
but also lists, sets, and ordered sets. All this data types can be manipulated
with atomic operations to push/pop elements, add/remove elements, perform server
side union, intersection, difference between sets, and so forth. Redis supports
different kind of sorting abilities.

%prep
echo "`grep -F %{name}-%{version}.tar.gz %{SOURCE10} | cut -d' ' -f4`  %{SOURCE0}" | sha256sum -c
%setup -q
%patch0
%patch1 -p1
%patch3 -p1
%patch4 -p1

%build
export HOST=OBS # for reproducible builds
%make_build CFLAGS="%{optflags}" BUILD_WITH_SYSTEMD=yes
%sysusers_generate_pre %{SOURCE9} redis

%install
install -m 0750 -d \
  %{buildroot}%{_sbindir} \
  %{buildroot}%{_log_dir} \
  %{buildroot}%{_data_dir} \
  %{buildroot}%{_conf_dir} \
  %{buildroot}%{_log_dir}/default \
  %{buildroot}%{_data_dir}/default

install -Dpm 0755 src/%{name}-benchmark  %{buildroot}%{_bindir}/%{name}-benchmark
install -Dpm 0755 src/%{name}-cli        %{buildroot}%{_bindir}/%{name}-cli

install -Dpm 0755 src/%{name}-server     %{buildroot}%{_sbindir}/%{name}-server

ln -sfv ../sbin/redis-server             %{buildroot}%{_bindir}/%{name}-check-aof
ln -sfv ../sbin/redis-server             %{buildroot}%{_bindir}/%{name}-check-rdb
ln -sfv ../sbin/redis-server             %{buildroot}%{_sbindir}/%{name}-check-aof
ln -sfv ../sbin/redis-server             %{buildroot}%{_sbindir}/%{name}-check-rdb
ln -sfv ../sbin/redis-server             %{buildroot}%{_sbindir}/%{name}-sentinel

perl -p -i -e 's|daemonize yes|daemonize no|g' %{name}.conf
install -Dm 0640 redis.conf              %{buildroot}%{_conf_dir}/default.conf.example
install -Dm 0660 sentinel.conf           %{buildroot}%{_conf_dir}/sentinel.conf.example

# some sysctl stuff
install -Dm 0644 %{SOURCE6} %{buildroot}%{_sysconfdir}/sysctl.d/00-%{name}.conf
install -Dm 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/logrotate.d/%{name}
install -Dm 0644 %{SOURCE2} %{buildroot}%{_unitdir}/%{name}.target
install -Dm 0644 %{SOURCE3} %{buildroot}%{_unitdir}/%{name}@.service
install -Dm 0644 %{SOURCE4} %{buildroot}%{_tmpfilesdir}/%{name}.conf
install -Dm 0644 %{SOURCE7} %{buildroot}%{_unitdir}/%{name}-sentinel@.service
install -Dm 0644 %{SOURCE8} %{buildroot}%{_unitdir}/%{name}-sentinel.target

ln -sf %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}
cp %{SOURCE5} README.SUSE

mkdir -p %{buildroot}%{_sysusersdir}
install -m 644 %{SOURCE9} %{buildroot}%{_sysusersdir}/

%check
cat <<EOF
---------------------------------------------------
The test suite often fails to start a server, with
'child process exited abnormally' -- sometimes it works.
---------------------------------------------------
EOF
%make_build test || true

%pre -f redis.pre
%service_add_pre redis.target redis@.service redis-sentinel.target redis-sentinel@.service

%post
%tmpfiles_create %{_tmpfilesdir}/%{name}.conf
%service_add_post redis.target redis@.service redis-sentinel.target redis-sentinel@.service
echo "See %{_docdir}/%{name}/README.SUSE to continue"

%preun
%service_del_preun redis.target redis@.service redis-sentinel.target redis-sentinel@.service

%postun
%service_del_postun redis.target redis@.service redis-sentinel.target redis-sentinel@.service

%files
%license COPYING
%doc 00-RELEASENOTES BUGS CONTRIBUTING README.md
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%config(noreplace) %{_sysconfdir}/sysctl.d/00-%{name}.conf
%{_bindir}/%{name}-*
%{_sbindir}/%{name}-*
%{_sbindir}/rc%{name}
%{_tmpfilesdir}/%{name}.conf
%{_sysusersdir}/redis-user.conf
%{_unitdir}/%{name}@.service
%{_unitdir}/%{name}.target
%{_unitdir}/%{name}-sentinel@.service
%{_unitdir}/%{name}-sentinel.target
%doc README.SUSE
%config(noreplace) %attr(-,root,%{name}) %{_conf_dir}/
%dir %attr(0750,%{name},%{name}) %{_data_dir}
%dir %attr(0750,%{name},%{name}) %{_data_dir}/default
%dir %attr(0750,%{name},%{name}) %{_log_dir}

%changelog
