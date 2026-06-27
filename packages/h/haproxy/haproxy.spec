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

%define main_binaries haproxy
%define extra_binaries haterm admin/halog/halog dev/haring/haring dev/gdb/libs-from-core dev/gdb/pm-from-core

%define pkg_name haproxy
%define pkg_home %{_localstatedir}/lib/%{pkg_name}
%{!?vim_data_dir:%global vim_data_dir %{_datadir}/vim/%(readlink %{_datadir}/vim/current)}

%bcond_with awslc

%if 0%{?suse_version} >= 1600 && 0%{?suse_version} < 1699
%define force_gcc_version 15
%endif

%if 0%{?suse_version} >= 1699  || %{with awslc}
%bcond_without quic
%else
%bcond_with quic
%endif

%bcond_without pcre2_jit

%bcond_without  apparmor

%bcond_with ech

%bcond_with opentelemetry

Name:           haproxy
Version:        3.4.1+git0.3e888a769
Release:        0
%if %{with opentelemetry}
%global otel_revision 6344dfa
%global otel_subdir   haproxy-opentelemetry-%{otel_revision}
%global otel_additional_source -a9
%endif
#
Summary:        The Reliable, High Performance TCP/HTTP Load Balancer
License:        GPL-3.0-or-later AND LGPL-2.1-or-later
Group:          Productivity/Networking/Web/Proxy
#
URL:            https://www.haproxy.org/
#               source URL in _service file
Source:         haproxy-%{version}.tar.gz
Source2:        usr.sbin.haproxy.apparmor
Source3:        local.usr.sbin.haproxy.apparmor
Source4:        haproxy.cfg
Source5:        haproxy-user.conf
Source6:        haproxy-tmpfiles.conf
Source7:        README.SUSE
Source8:        README.SUSE.PACKAGING
%if %{with opentelemetry}
Source9:        %{otel_subdir}.tar.gz
%endif
#
Source98:       series
Source99:       haproxy-rpmlintrc
# PATCH-OPENSUSE
Patch1:         haproxy-1.6.0_config_haproxy_user.patch
# PATCH-OPENSUSE
Patch2:         haproxy-1.6.0-makefile_lib.patch
# PATCH-OPENSUSE
Patch3:         haproxy-1.6.0-sec-options.patch
# PATCH-OPENSUSE
Patch4:         haproxy-service.patch
BuildRequires:  gcc%{?force_gcc_version}-c++
BuildRequires:  libgcrypt-devel
BuildRequires:  pcre2-devel
BuildRequires:  pkgconfig
BuildRequires:  vim
BuildRequires:  zlib-devel
%if %{with opentelemetry}
BuildRequires:  pkgconfig(opentelemetry-c-wrapper)
%endif
Provides:       %{name}-doc = %{version}
Obsoletes:      %{name}-doc < %{version}
Provides:       haproxy-1.5 = %{version}
Obsoletes:      haproxy-1.5 < %{version}
#
#
%if %{with apparmor}
BuildRequires:  apparmor-abstractions
Recommends:     apparmor-abstractions
BuildRequires:  apparmor-rpm-macros
%endif
BuildRequires:  lua-devel >= 5.3
%if %{with awslc}
BuildRequires:  aws-lc-devel
%else
BuildRequires:  openssl-devel
%endif
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  sysuser-shadow
BuildRequires:  sysuser-tools
%{?systemd_ordering}
%sysusers_requires
%if %{with opentelemetry}
#!BuildIgnore:  haproxy-implementation
Requires:       haproxy-implementation = %{version}-%{release}
Requires(post):   haproxy-implementation = %{version}-%{release}
Requires(postun): haproxy-implementation = %{version}-%{release}
Suggests:       haproxy-normal
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

%if %{with opentelemetry}
%package normal
Summary:        Normal haproxy binary package
Provides:       haproxy-implementation = %{version}-%{release}
Requires:       haproxy = %{version}-%{release}
Conflicts:      haproxy-implementation
Removepathpostfixes: -normal
%description normal
HAProxy implements an event-driven, mono-process model which enables support
for very high number of simultaneous connections at very high speeds.
Multi-process or multi-threaded models can rarely cope with thousands of
connections because of memory limits, system scheduler limits, and lock
contention everywhere. Event-driven models do not have these problems because
implementing all the tasks in user-space allows a finer resource and time
management. The down side is that those programs generally don't scale well on
multi-processor systems. That's the reason why they must be optimized to get
the most work done from every CPU cycle.

This package holds the normal haproxy binary without the opentelemetry feature.

%package opentelemetry
Summary:        Normal haproxy binary package
Provides:       haproxy-implementation = %{version}-%{release}
Requires:       haproxy = %{version}-%{release}
Conflicts:      haproxy-implementation
Removepathpostfixes: -otel
%description opentelemetry
HAProxy implements an event-driven, mono-process model which enables support
for very high number of simultaneous connections at very high speeds.
Multi-process or multi-threaded models can rarely cope with thousands of
connections because of memory limits, system scheduler limits, and lock
contention everywhere. Event-driven models do not have these problems because
implementing all the tasks in user-space allows a finer resource and time
management. The down side is that those programs generally don't scale well on
multi-processor systems. That's the reason why they must be optimized to get
the most work done from every CPU cycle.

This package holds the haproxy binary with the opentelemetry feature.

%endif

%prep
%autosetup -p1 %{?otel_additional_source}
cp %{SOURCE7} .

%build
%global shared_make_flags \\\
    %if 0%{?force_gcc_version} \
    CC="gcc-%{?force_gcc_version}" \\\
    CXX="g++-%{?force_gcc_version}" \\\
    %endif \
    TARGET=linux-glibc \\\
    USE_RELRO_NOW=1 \\\
    USE_STACKPROTECTOR=1 \\\
    USE_PIE=1 \\\
    USE_KTLS=1 \\\
    USE_PCRE2=1 \\\
    %if %{with pcre2_jit} \
    USE_PCRE2_JIT=1 \\\
    %endif \
    %ifarch %{ix86} \
    USE_REGPARM=1 \\\
    %endif \
    USE_GETADDRINFO=1 \\\
%if %{with awslc} \
    USE_OPENSSL_AWSLC=1 \\\
%else \
    USE_OPENSSL=1 \\\
%if %{with ech} \
    USE_QUIC_OPENSSL_COMPAT=1 \\\
    USE_ECH=1 \\\
%endif \
%endif \
    USE_LUA=1 \\\
    USE_ZLIB=1 \\\
    USE_TFO=1 \\\
    USE_NS=1 \\\
    LIB="%{_lib}" \\\
    PREFIX="%{_prefix}" \\\
    USE_PROMEX=1 \\\
    %if %{with quic} \
    USE_QUIC=1 \\\
%if %{without awslc} \
    USE_QUIC_OPENSSL_COMPAT=1 \\\
%endif \
    %endif \
    %if %{with opentracing} \
    USE_OT=1 \\\
    %endif \
    %if %{with memory_profiling} \
    USE_MEMORY_PROFILING=1 \\\
    %endif \
    OPT_CFLAGS="%{optflags}" V=1

%make_build %{shared_make_flags} %{main_binaries}

%if %{with opentelemetry}
for main_binary in %{main_binaries} ; do
  mv ${main_binary} ${main_binary}-normal
done
%make_build clean
%make_build %{shared_make_flags} EXTRA_MAKE="%{otel_subdir}" %{main_binaries}
for main_binary in %{main_binaries} ; do
  mv ${main_binary} ${main_binary}-otel
done
%make_build clean
%endif

%make_build -C admin/systemd  PREFIX="%{_prefix}"
%make_build %{shared_make_flags} %{extra_binaries}

%sysusers_generate_pre %{SOURCE5} haproxy haproxy-user.conf

%install
%if %{with opentelemetry}
for main_binary in %{main_binaries} ; do
  install -D -m 0755 ${main_binary}-{normal,otel} -t %{buildroot}%{_sbindir}
done
%else
install -D -m 0755 %{main_binaries} -t %{buildroot}%{_sbindir}/
%endif
install -d -m 0750                         %{buildroot}%{_sysconfdir}/%{pkg_name}/
install -d -m 0750                         %{buildroot}%{_sysconfdir}/%{pkg_name}/conf.d/
install    -m 0640 %{SOURCE4}              %{buildroot}%{_sysconfdir}/%{pkg_name}/%{pkg_name}.cfg

for extra_binary in %{extra_binaries} ; do
install -D -m 0755 ${extra_binary}      %{buildroot}%{_sbindir}/haproxy-$(basename ${extra_binary})
done

install -D -m 0644 admin/systemd/%{pkg_name}.service  %{buildroot}%{_unitdir}/%{pkg_name}.service
install -D -m 644 %{SOURCE5} %{buildroot}%{_sysusersdir}/haproxy-user.conf
install -D -m 644 %{SOURCE6} %{buildroot}%{_tmpfilesdir}/%{name}.conf
install -d -m 0750                          %{buildroot}%{pkg_home}
install -D -m 0644 admin/syntax-highlight/haproxy.vim     %{buildroot}%{vim_data_dir}/syntax/%{pkg_name}.vim
install -D -m 0644 doc/%{pkg_name}.1        %{buildroot}%{_mandir}/man1/%{pkg_name}.1
%if %{with apparmor}
install -D -m 0644 %{SOURCE2}                   %{buildroot}%{_sysconfdir}/apparmor.d/usr.sbin.haproxy
install -D -m 0644 %{SOURCE3}                   %{buildroot}%{_sysconfdir}/apparmor.d/local/haproxy
install -D -m 0644 %{SOURCE3}                   %{buildroot}%{_sysconfdir}/apparmor.d/local/usr.sbin.haproxy
%endif

rm examples/*init*


%pre -f haproxy.pre
%service_add_pre %{pkg_name}.service

%post
%if %{with apparmor}
%apparmor_reload %{_sysconfdir}/apparmor.d/usr.sbin.haproxy
%endif
%tmpfiles_create %{_tmpfilesdir}/%{name}.conf
%service_add_post %{pkg_name}.service

%preun
%service_del_preun %{pkg_name}.service

%postun
%service_del_postun %{pkg_name}.service

%files
%license LICENSE
%doc README.SUSE CHANGELOG README.md
%if %{with opentelemetry}
%doc %{otel_subdir}/README*
%endif
%doc doc/* examples/
%doc admin/netsnmp-perl/ admin/selinux/
%dir %attr(-,root,haproxy) %{_sysconfdir}/%{pkg_name}
%dir %attr(-,root,haproxy) %{_sysconfdir}/%{pkg_name}/conf.d/
%config(noreplace) %attr(-,root,haproxy) %{_sysconfdir}/%{pkg_name}/*
%{_unitdir}/%{pkg_name}.service
%{_sysusersdir}/haproxy-user.conf
%{_tmpfilesdir}/%{name}.conf
%dir %ghost %attr(0750,root,haproxy) %{_rundir}/%{name}
%if %{without opentelemetry}
%{_sbindir}/haproxy
%endif
%{_sbindir}/haproxy-halog
%{_sbindir}/haproxy-haterm
%{_sbindir}/haproxy-haring
%{_sbindir}/haproxy-libs-from-core
%{_sbindir}/haproxy-pm-from-core
%dir %ghost %{pkg_home}
%{_mandir}/man1/%{pkg_name}.1%{?ext_man}
%dir %{_datadir}/vim
%dir %{vim_data_dir}
%dir %{vim_data_dir}/syntax
%{vim_data_dir}/syntax/%{pkg_name}.vim
%if %{with apparmor}
%config(noreplace) %{_sysconfdir}/apparmor.d/usr.sbin.haproxy
%config(noreplace) %ghost %{_sysconfdir}/apparmor.d/local/haproxy
%config(noreplace) %ghost %{_sysconfdir}/apparmor.d/local/usr.sbin.haproxy
%endif

%if %{with opentelemetry}
%files normal
%{_sbindir}/haproxy-normal

%files opentelemetry
%{_sbindir}/haproxy-otel
%endif

%changelog
