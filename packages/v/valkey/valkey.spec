#
# spec file for package valkey
#
# Copyright (c) SUSE LLC
# Copyright (c) Jonathan Wright
# Copyright (c) Neal Gompa
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

%global make_flags CFLAGS="%{build_cflags}" DEBUG="" V="echo" PREFIX=%{buildroot}%{_prefix} BUILD_WITH_SYSTEMD=yes BUILD_TLS=yes

Name:           valkey
Version:        7.2.5
Release:        0
Summary:        Persistent key-value database
License:        BSD-3-Clause
URL:            https://valkey.io
Source0:        https://github.com/valkey-io/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}.logrotate
Source2:        %{name}.target
Source3:        %{name}@.service
Source4:        %{name}.tmpfiles.d
Source5:        README.SUSE
Source6:        %{name}.sysctl
Source7:        %{name}-sentinel@.service
Source8:        %{name}-sentinel.target
Source9:        %{name}-user.conf
Source10:       macros.%{name}
Source11:       migrate_redis_to_valkey.bash
# PATCH-FIX-UPSTREAM -- Fix for fallback for atomics on POWER
## From: https://github.com/valkey-io/valkey/pull/607
Patch0:         ppc-atomic.patch
# PATCH-FIX-OPENSUSE -- Adjust configs for openSUSE
Patch1001:      %{name}-conf.patch
BuildRequires:  jemalloc-devel
BuildRequires:  libopenssl-devel >= 1.1.1
BuildRequires:  pkgconfig
BuildRequires:  procps
BuildRequires:  python3
BuildRequires:  sysuser-shadow
BuildRequires:  sysuser-tools
BuildRequires:  tcl
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(systemd)
# there is no tcl-tls package yet, which is said to be needed for testing tls support
Recommends:     logrotate
%{?sysusers_requires}

%global valkey_modules_abi 1
%global valkey_modules_dir %{_libdir}/%{name}/modules
Provides:       valkey(modules_abi)%{?_isa} = %{valkey_modules_abi}

%description
Valkey is an advanced key-value store. It is similar to memcached but the dataset
is not volatile, and values can be strings, exactly like in memcached,
but also lists, sets, and ordered sets. All this data types can be manipulated
with atomic operations to push/pop elements, add/remove elements, perform server
side union, intersection, difference between sets, and so forth. It supports many
different kinds of sorting abilities.

%package        devel
Summary:        Development header for Valkey module development

%description    devel
Header file required for building loadable Valkey modules.

%package        compat-redis
Summary:        Conversion script and compatibility symlinks for Redis
Requires:       valkey = %{version}-%{release}
Conflicts:      redis
Obsoletes:      redis <= 7.2.5
Provides:       redis = %{version}-%{release}
BuildArch:      noarch

%description    compat-redis
This package contains compatibility symlinks and wrappers to enable
easy conversion from Redis to Valkey.

%prep
%autosetup -p1


# Module API version safety check
api=`sed -n -e 's/#define VALKEYMODULE_APIVER_[0-9][0-9]* //p' src/valkeymodule.h`
if test "$api" != "%{valkey_modules_abi}"; then
   : Error: Upstream API version is now ${api}, expecting %%{valkey_modules_abi}.
   : Update the valkey_modules_abi macro, the rpmmacros file, and rebuild.
   exit 1
fi

%build
%make_build %{make_flags}
%sysusers_generate_pre %{SOURCE9} %{name}

%install
%make_install %{make_flags}

install -pm0750 -d \
  %{buildroot}%{_log_dir} \
  %{buildroot}%{_data_dir} \
  %{buildroot}%{_conf_dir} \
  %{buildroot}%{_log_dir}/default \
  %{buildroot}%{_data_dir}/default

install -pDm644 src/%{name}module.h %{buildroot}%{_includedir}/%{name}module.h

install -Dpm0640 valkey.conf            %{buildroot}%{_conf_dir}/default.conf.example
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

cp %{SOURCE5} README.SUSE

mkdir -p %{buildroot}%{_sysusersdir}
install -pm0644 %{SOURCE9} %{buildroot}%{_sysusersdir}/

mkdir -p %{buildroot}%{_rpmmacrodir}
install -pm0644 %{SOURCE10} %{buildroot}%{_rpmmacrodir}/

mkdir -p %{buildroot}%{_libdir}/%{name}/modules

# Install valkey migration script
mkdir -p %{buildroot}%{_libexecdir}
install -pm0755 %{SOURCE11} %{buildroot}%{_libexecdir}/

%check
cat <<EOF
---------------------------------------------------
The test suite often fails to start a server, with
'child process exited abnormally' -- sometimes it works.
---------------------------------------------------
EOF
# Variable assignments need to match in all make invocations, otherwise it might recomplie. See https://github.com/redis/redis/issues/7337
%make_build test %{make_flags} || true

%pre -f %{name}.pre
%service_add_pre %{name}.target %{name}@.service %{name}-sentinel.target %{name}-sentinel@.service

%post
%tmpfiles_create %{_tmpfilesdir}/%{name}.conf
%service_add_post %{name}.target %{name}@.service %{name}-sentinel.target %{name}-sentinel@.service
echo "See %{_docdir}/%{name}/README.SUSE to continue"

%preun
%service_del_preun %{name}.target %{name}@.service %{name}-sentinel.target %{name}-sentinel@.service

%postun
%service_del_postun %{name}.target %{name}@.service %{name}-sentinel.target %{name}-sentinel@.service

%post compat-redis
%{_libexecdir}/migrate_redis_to_valkey.bash

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
%{_tmpfilesdir}/%{name}.conf
%{_sysusersdir}/%{name}-user.conf
%{_unitdir}/%{name}@.service
%{_unitdir}/%{name}.target
%{_unitdir}/%{name}-sentinel@.service
%{_unitdir}/%{name}-sentinel.target
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/modules
%doc README.SUSE
%config(noreplace) %attr(-,root,%{name}) %{_conf_dir}/
%dir %attr(0750,%{name},%{name}) %{_data_dir}
%dir %attr(0750,%{name},%{name}) %{_data_dir}/default
%dir %attr(0750,%{name},%{name}) %{_log_dir}
%ghost %dir %attr(0755,%{name},%{name}) /run/%{name}

%files devel
# main package is not required
%license COPYING
%{_includedir}/%{name}module.h
%{_rpmmacrodir}/macros.%{name}

%files compat-redis
%{_libexecdir}/migrate_redis_to_valkey.bash
%{_bindir}/redis-*


%changelog
