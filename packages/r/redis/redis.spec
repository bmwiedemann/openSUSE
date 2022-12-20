#
# spec file for package redis
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


%define _data_dir       %{_localstatedir}/lib/%{name}
%define _log_dir        %{_localstatedir}/log/%{name}
%define _conf_dir       %{_sysconfdir}/%{name}
Name:           redis
Version:        7.0.7
Release:        0
Summary:        Persistent key-value database
License:        BSD-3-Clause
URL:            https://redis.io
Source0:        https://download.redis.io/releases/%{name}-%{version}.tar.gz
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
Patch3:         reproducible.patch
Patch4:         ppc-atomic.patch
BuildRequires:  jemalloc-devel
BuildRequires:  libopenssl-devel >= 1.1.1
BuildRequires:  pkgconfig
BuildRequires:  procps
BuildRequires:  sysuser-shadow
BuildRequires:  sysuser-tools
BuildRequires:  tcl
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(systemd)
# there is no tcl-tls package yet, which is said to be needed for testing tls support
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
%patch3 -p1
%patch4 -p1

%build
export HOST=OBS # for reproducible builds
%make_build CFLAGS="%{optflags}" \
        BUILD_WITH_SYSTEMD=yes \
        BUILD_TLS=yes
%sysusers_generate_pre %{SOURCE9} %{name}

%install
install -pm0750 -d \
  %{buildroot}%{_sbindir} \
  %{buildroot}%{_log_dir} \
  %{buildroot}%{_data_dir} \
  %{buildroot}%{_conf_dir} \
  %{buildroot}%{_log_dir}/default \
  %{buildroot}%{_data_dir}/default

install -Dpm0755 src/%{name}-benchmark  %{buildroot}%{_bindir}/%{name}-benchmark
install -Dpm0755 src/%{name}-cli        %{buildroot}%{_bindir}/%{name}-cli

install -Dpm0755 src/%{name}-server     %{buildroot}%{_sbindir}/%{name}-server

ln -sfv ../sbin/redis-server            %{buildroot}%{_bindir}/%{name}-check-aof
ln -sfv ../sbin/redis-server            %{buildroot}%{_bindir}/%{name}-check-rdb
ln -sfv ../sbin/redis-server            %{buildroot}%{_sbindir}/%{name}-check-aof
ln -sfv ../sbin/redis-server            %{buildroot}%{_sbindir}/%{name}-check-rdb
ln -sfv ../sbin/redis-server            %{buildroot}%{_sbindir}/%{name}-sentinel

perl -p -i -e 's|daemonize yes|daemonize no|g' %{name}.conf
install -Dpm0640 redis.conf             %{buildroot}%{_conf_dir}/default.conf.example
install -Dpm0660 sentinel.conf          %{buildroot}%{_conf_dir}/sentinel.conf.example

# some sysctl stuff
install -Dpm0644 %{SOURCE6} %{buildroot}/%{_prefix}/lib/sysctl.d/00-%{name}.conf
%if 0%{?suse_version} > 1500
mkdir -p %{buildroot}%{_distconfdir}/logrotate.d
install -Dpm0644 %{SOURCE1} %{buildroot}%{_distconfdir}/logrotate.d/%{name}
%else
install -Dpm0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/logrotate.d/%{name}
%endif
install -Dpm0644 %{SOURCE2} %{buildroot}%{_unitdir}/%{name}.target
install -Dpm0644 %{SOURCE3} %{buildroot}%{_unitdir}/%{name}@.service
install -Dpm0644 %{SOURCE4} %{buildroot}%{_tmpfilesdir}/%{name}.conf
install -Dpm0644 %{SOURCE7} %{buildroot}%{_unitdir}/%{name}-sentinel@.service
install -Dpm0644 %{SOURCE8} %{buildroot}%{_unitdir}/%{name}-sentinel.target

ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}
cp %{SOURCE5} README.SUSE

mkdir -p %{buildroot}%{_sysusersdir}
install -pm0644 %{SOURCE9} %{buildroot}%{_sysusersdir}/

%check
cat <<EOF
---------------------------------------------------
The test suite often fails to start a server, with
'child process exited abnormally' -- sometimes it works.
---------------------------------------------------
EOF
# Variable assignments need to match in all make invocations, otherwise it might recomplie. See https://github.com/redis/redis/issues/7337
%make_build test CFLAGS="%{optflags}" BUILD_WITH_SYSTEMD=yes BUILD_TLS=yes || true

%pre -f %{name}.pre
%service_add_pre %{name}.target %{name}@.service %{name}-sentinel.target %{name}-sentinel@.service
%if 0%{?suse_version} > 1500
# Prepare for migration to /usr/etc; save any old .rpmsave
for i in logrotate.d/%{name} ; do
   test -f %{_sysconfdir}/${i}.rpmsave && mv -v %{_sysconfdir}/${i}.rpmsave %{_sysconfdir}/${i}.rpmsave.old ||:
done
%endif

%if 0%{?suse_version} > 1500
%posttrans
# Migration to /usr/etc, restore just created .rpmsave
for i in logrotate.d/%{name} ; do
   test -f %{_sysconfdir}/${i}.rpmsave && mv -v %{_sysconfdir}/${i}.rpmsave %{_sysconfdir}/${i} ||:
done
%endif

%post
%tmpfiles_create %{_tmpfilesdir}/%{name}.conf
%service_add_post %{name}.target %{name}@.service %{name}-sentinel.target %{name}-sentinel@.service
echo "See %{_docdir}/%{name}/README.SUSE to continue"

%preun
%service_del_preun %{name}.target %{name}@.service %{name}-sentinel.target %{name}-sentinel@.service

%postun
%service_del_postun %{name}.target %{name}@.service %{name}-sentinel.target %{name}-sentinel@.service

%files
%license COPYING
%doc 00-RELEASENOTES BUGS README.md
%if 0%{?suse_version} > 1500
%{_distconfdir}/logrotate.d/%{name}
%else
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%endif
%{_prefix}/lib/sysctl.d/00-%{name}.conf
%{_bindir}/%{name}-*
%{_sbindir}/%{name}-*
%{_sbindir}/rc%{name}
%{_tmpfilesdir}/%{name}.conf
%{_sysusersdir}/%{name}-user.conf
%{_unitdir}/%{name}@.service
%{_unitdir}/%{name}.target
%{_unitdir}/%{name}-sentinel@.service
%{_unitdir}/%{name}-sentinel.target
%doc README.SUSE
%config(noreplace) %attr(-,root,%{name}) %{_conf_dir}/
%dir %attr(0750,%{name},%{name}) %{_data_dir}
%dir %attr(0750,%{name},%{name}) %{_data_dir}/default
%dir %attr(0750,%{name},%{name}) %{_log_dir}
%ghost %dir /run/%{name}

%changelog
