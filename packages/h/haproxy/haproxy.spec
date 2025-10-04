#
# spec file for package haproxy
#
# Copyright (c) 2024 SUSE LLC
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

# => notes regarding QUIC in README.SUSE.PACKAGING

%define pkg_name haproxy
%define pkg_home %{_localstatedir}/lib/%{pkg_name}
%{!?vim_data_dir:%global vim_data_dir %{_datadir}/vim/%(readlink %{_datadir}/vim/current)}

%bcond_with awslc

%if 0%{?suse_version} > 1600 || %{with awslc}
%bcond_without quic
%else
%bcond_with quic
%endif

%if 0%{?suse_version} > 1500
%bcond_with    rc_symlink
%else
%bcond_without rc_symlink
%endif

%if 0%{?suse_version} >= 1230
%bcond_without tcp_fast_open
%bcond_without network_namespace
%else
%bcond_with tcp_fast_open
%bcond_with network_namespace
%endif

%if 0%{?suse_version} > 1320
%bcond_without lua
%else
%bcond_with    lua
%endif

%if 0%{?suse_version} >= 1310
%bcond_without systemd
%else
%bcond_with systemd
%endif

%bcond_without pcre2_jit

%bcond_without  apparmor
%if 0%{?suse_version} > 1320
%bcond_without apparmor_reload
%else
%bcond_with    apparmor_reload
%endif

%if 0%{?suse_version} >= 1500
%bcond_without sysusers
%bcond_without tmpfiles
%else
%bcond_with sysusers
%bcond_with tmpfiles
%endif

Name:           haproxy
Version:        3.2.6+git0.81568b2d1
Release:        0
#
Summary:        The Reliable, High Performance TCP/HTTP Load Balancer
License:        GPL-3.0-or-later AND LGPL-2.1-or-later
Group:          Productivity/Networking/Web/Proxy
#
URL:            https://www.haproxy.org/
#               source URL in _service file
Source:         haproxy-%{version}.tar.gz
Source1:        %{pkg_name}.init
Source2:        usr.sbin.haproxy.apparmor
Source3:        local.usr.sbin.haproxy.apparmor
Source4:        haproxy.cfg
Source5:        haproxy-user.conf
Source6:        haproxy-tmpfiles.conf
Source7:        README.SUSE
Source8:        README.SUSE.PACKAGING
#
Source98:       series
Source99:       haproxy-rpmlintrc
Patch1:         haproxy-1.6.0_config_haproxy_user.patch
Patch2:         haproxy-1.6.0-makefile_lib.patch
Patch3:         haproxy-1.6.0-sec-options.patch
Patch4:         haproxy-service.patch
BuildRequires:  libgcrypt-devel
BuildRequires:  pcre2-devel
BuildRequires:  pkgconfig
BuildRequires:  vim
BuildRequires:  zlib-devel
Provides:       %{name}-doc = %{version}
Obsoletes:      %{name}-doc < %{version}
Provides:       haproxy-1.5 = %{version}
Obsoletes:      haproxy-1.5 < %{version}
#
#
%if %{with apparmor}
%if 0%{?suse_version} <= 1315
BuildRequires:  apparmor-profiles
Recommends:     apparmor-profiles
%else
BuildRequires:  apparmor-abstractions
Recommends:     apparmor-abstractions
%endif
%if %{with apparmor_reload}
BuildRequires:  apparmor-rpm-macros
%endif
%endif
%if %{with lua}
BuildRequires:  lua-devel >= 5.3
%endif
%if %{with awslc}
BuildRequires:  aws-lc-devel
%else
BuildRequires:  openssl-devel
%endif
%if %{with systemd}
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(systemd)
%if %{with sysusers}
BuildRequires:  sysuser-shadow
BuildRequires:  sysuser-tools
%endif
%endif
%if %{with systemd}
%{?systemd_ordering}
%if %{with sysusers}
%sysusers_requires
%endif
%endif

%description
HAProxy implements an event-driven, mono-process model which enables support
for very high number of simultaneous connections at very high speeds.
Multi-process or multi-threaded models can rarely cope with thousands of
connections because of memory limits, system scheduler limits, and lock
contention everywhere. Event-driven models do not have these problems because
implementing all the tasks in user-space allows a finer resource and time
management. The down side is that those programs generally don't scale well on
multi-processor systems. That's the reason why they must be optimized to get
the most work done from every CPU cycle.

%prep
%autosetup -p1
cp %{SOURCE7} .

%build
%make_build \
    TARGET=linux-glibc \
    CPU="%{_target_cpu}" \
    USE_PCRE2=1 \
    %if %{with pcre2_jit}
    USE_PCRE2_JIT=1 \
    %endif
    %ifarch %{ix86}
    USE_REGPARM=1 \
    %endif
    USE_GETADDRINFO=1 \
%if %{with awslc}
    USE_OPENSSL_AWSLC=1 \
%else
    USE_OPENSSL=1 \
%endif
    %if %{with lua}
    USE_LUA=1 \
    %endif
    USE_ZLIB=1 \
    %if %{with tcp_fast_open}
    USE_TFO=1 \
    %endif
    %if %{with network_namespace}
    USE_NS=1 \
    %endif
%if %{with systemd}
    USE_SYSTEMD=1 \
%endif
    USE_PIE=1 \
    USE_STACKPROTECTOR=1 \
    USE_RELRO_NOW=1 \
    LIB="%{_lib}" \
    PREFIX="%{_prefix}" \
    USE_PROMEX=1 \
    %if %{with quic}
    USE_QUIC=1 \
%if %{without awslc}
    USE_QUIC_OPENSSL_COMPAT=1 \
%endif
    %endif
    %if %{with opentracing}
    USE_OT=1 \
    %endif
    %if %{with memory_profiling}
    USE_MEMORY_PROFILING=1 \
    %endif
    DEBUG_CFLAGS="%{optflags}" V=1
%if %{with systemd}
%make_build -C admin/systemd  PREFIX="%{_prefix}"
%if %{with sysusers}
%sysusers_generate_pre %{SOURCE5} haproxy haproxy-user.conf
%endif
%endif
%make_build admin/halog/halog DEBUG_CFLAGS="%{optflags}"

%install
install -D -m 0755 %{pkg_name}         %{buildroot}%{_sbindir}/%{pkg_name}
install -d -m 0750                     %{buildroot}%{_sysconfdir}/%{pkg_name}/
install    -m 0640 %{SOURCE4}              %{buildroot}%{_sysconfdir}/%{pkg_name}/%{pkg_name}.cfg

install -D -m 0755 admin/halog/halog %{buildroot}%{_sbindir}/haproxy-halog

%if %{with systemd}
install -D -m 0644 admin/systemd/%{pkg_name}.service  %{buildroot}%{_unitdir}/%{pkg_name}.service
%if %{with rc_symlink}
ln -sf /sbin/service   %{buildroot}%{_sbindir}/rc%{pkg_name}
%endif
%if %{with sysusers}
install -D -m 644 %{SOURCE5} %{buildroot}%{_sysusersdir}/haproxy-user.conf
%endif
%if %{with tmpfiles}
install -D -m 644 %{SOURCE6} %{buildroot}%{_tmpfilesdir}/%{name}.conf
%endif
%else
install -D -m 0755 %{SOURCE1}                      %{buildroot}%{_sysconfdir}/init.d/%{pkg_name}
ln -fs %{_sysconfdir}/init.d/%{pkg_name} %{buildroot}%{_sbindir}/rc%{pkg_name}
%endif

install -d -m 0750                          %{buildroot}%{pkg_home}
install -D -m 0644 admin/syntax-highlight/haproxy.vim     %{buildroot}%{vim_data_dir}/syntax/%{pkg_name}.vim
install -D -m 0644 doc/%{pkg_name}.1        %{buildroot}%{_mandir}/man1/%{pkg_name}.1
%if %{with apparmor}
install -D -m 0644 %{SOURCE2}                   %{buildroot}%{_sysconfdir}/apparmor.d/usr.sbin.haproxy
install -D -m 0644 %{SOURCE3}                   %{buildroot}%{_sysconfdir}/apparmor.d/local/haproxy
install -D -m 0644 %{SOURCE3}                   %{buildroot}%{_sysconfdir}/apparmor.d/local/usr.sbin.haproxy
%endif

rm examples/*init*


%if %{with systemd}
%if %{with sysusers}
%pre -f haproxy.pre
%else
%pre
%endif
%service_add_pre %{pkg_name}.service

%post
%if %{with apparmor} && %{with apparmor_reload}
%apparmor_reload %{_sysconfdir}/apparmor.d/usr.sbin.haproxy
%endif
%if %{with systemd}
%if %{with tmpfiles}
%tmpfiles_create %{_tmpfilesdir}/%{name}.conf
%endif
%endif
%service_add_post %{pkg_name}.service

%preun
%service_del_preun %{pkg_name}.service

%postun
%service_del_postun %{pkg_name}.service
%else
%pre
getent group %{pkg_name} >/dev/null || %{_sbindir}/groupadd -r %{pkg_name}
getent passwd %{pkg_name} >/dev/null || \
	%{_sbindir}/useradd  -g %{pkg_name} -s /bin/false -r \
	-c "user for %{pkg_name}" -d %{pkg_home} %{pkg_name}

%post
%fillup_and_insserv %{pkg_name}
%if %{with apparmor} && %{with apparmor_reload}
%apparmor_reload %{_sysconfdir}/apparmor.d/usr.sbin.haproxy
%endif

%preun
%stop_on_removal %{pkg_name}

%postun
%restart_on_update %{pkg_name}
%insserv_cleanup
%endif

%files
%license LICENSE
%doc README.SUSE CHANGELOG README.md
%doc doc/* examples/
%doc admin/netsnmp-perl/ admin/selinux/
%dir %attr(-,root,haproxy) %{_sysconfdir}/%{pkg_name}
%config(noreplace) %attr(-,root,haproxy) %{_sysconfdir}/%{pkg_name}/*
%if %{with systemd}
%{_unitdir}/%{pkg_name}.service
%if %{with sysusers}
%{_sysusersdir}/haproxy-user.conf
%endif
%if %{with tmpfiles}
%{_tmpfilesdir}/%{name}.conf
%dir %ghost %{_rundir}/%{name}
%endif
%else
%config(noreplace) %{_sysconfdir}/init.d/%{pkg_name}
%endif
%{_sbindir}/haproxy
%{_sbindir}/haproxy-halog
%if %{with rc_symlink}
%{_sbindir}/rchaproxy
%endif
%dir %attr(-,root,haproxy) %{pkg_home}
%{_mandir}/man1/%{pkg_name}.1%{?ext_man}
%dir %{_datadir}/vim
%dir %{vim_data_dir}
%dir %{vim_data_dir}/syntax
%{vim_data_dir}/syntax/%{pkg_name}.vim
%if %{with apparmor}
%if 0%{?suse_version} == 1110
%dir %{_sysconfdir}/apparmor.d/local/
%endif
%config(noreplace) %{_sysconfdir}/apparmor.d/usr.sbin.haproxy
%config(noreplace) %ghost %{_sysconfdir}/apparmor.d/local/haproxy
%config(noreplace) %ghost %{_sysconfdir}/apparmor.d/local/usr.sbin.haproxy
%endif

%changelog
