#
# spec file for package rspamd
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


%{echo: building for suse: ver:%{suse_version} arch:%{_arch} o:%{is_opensuse} "\n"}

%bcond_with split_out_client

%if 0%{?suse_version} > 1315 || 0%{?rhel_version} > 600 || 0%{?centos_version} > 600 || 0%{?fedora_version} >= 20 || 0%{?el7}%{?fc20}%{?fc21}%{?fc22}%{?fc23}%{?fc24}%{?fc25}
%bcond_without systemd
%else
%bcond_with    systemd
%endif

%global lua_abi_version 51

%ifarch %{ix86} x86_64
  %if 0%{?suse_version} > 1500 || 0%{?sle_version} >= 150500
    %bcond_without hyperscan
  %endif
  %if 0%{?suse_version} >= 1500
    %bcond_without luajit
  %else
    %bcond_with    luajit
  %endif
%endif

%if 0%{?suse_version} >= 1500 && ! 0%{?sle_version}
  %bcond_without ext_hiredis
%endif

%if 0%{?suse_version} >= 1500
  %bcond_without openblas
%endif

# fails to build atm
%bcond_with    utils

%define rspamd_user  _rspamd
%define rspamd_group %{rspamd_user}

%global _wwwdir /srv/www/webapps

%if 0%{?suse_version} && 0%{?suse_version} < 1550
%global force_gcc_version 9
%endif

Name:           rspamd
Version:        3.12.1
Release:        0
Summary:        Spam filtering system
License:        Apache-2.0
Group:          Productivity/Networking/Email/Utilities
URL:            https://rspamd.com/
Source0:        https://github.com/rspamd/rspamd/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        usr.bin.rspamd
Patch0:         rspamd-conf.patch
Patch1:         rspamd-after-redis-target.patch
%if !0%{?is_opensuse}
# because 80-check-malware-scan-clamav triggered in SLE-15-SP2
BuildRequires:  -post-build-checks-malwarescan
%endif
BuildRequires:  cmake >= 3.12
BuildRequires:  curl-devel
BuildRequires:  db-devel
BuildRequires:  file-devel
BuildRequires:  gcc%{?force_gcc_version}-c++
BuildRequires:  gd-devel
%if %{with hyperscan}
BuildRequires:  pkgconfig(libhs)
%endif
%if %{with jemalloc}
BuildRequires:  jemalloc-devel
%endif
BuildRequires:  libfann-devel
BuildRequires:  libicu-devel
%if %{with luajit}
BuildRequires:  luajit-devel
%else
BuildRequires:  lua%{?lua_abi_version}-devel
%endif
BuildRequires:  lua%{?lua_abi_version}-lpeg
Requires:       lua%{?lua_abi_version}-lpeg
%if %{with openblas}
BuildRequires:  openblas-devel
%endif
BuildRequires:  pcre2-devel
BuildRequires:  pkgconfig
%if %{with system_fmt}
BuildRequires:  pkgconfig(fmt)
%global with_system_fmt 1
%if !%{pkg_vcmp fmt-devel > 11}
Provides:       bundled(fmt) = 11.0.0
%global with_system_fmt 0
%endif
%else
Provides:       bundled(fmt) = 11.0.0
%global with_system_fmt 0
%endif
BuildRequires:  pkgconfig(glib-2.0) >= 2.28
%if %{with ext_hiredis}
BuildRequires:  pkgconfig(hiredis)
%endif
BuildRequires:  pkgconfig(libev)
%if 0%{?suse_version} >= 1500 && 0%{?suse_version} < 1599
BuildRequires:  pkgconfig(libnsl)
%endif
BuildRequires:  ragel
BuildRequires:  pkgconfig(libarchive) >= 3.0
BuildRequires:  pkgconfig(libsodium)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(sqlite3)
%if %{with systemd}
BuildRequires:  pkgconfig(systemd)
%{?systemd_ordering}
%endif
BuildRequires:  lapack-devel
BuildRequires:  pkgconfig(libunwind)
BuildRequires:  pkgconfig(libxxhash)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(openblas)
%if 0%{?with split_out_client}
Requires:       rspamd-client = %{version}
%else
Conflicts:      rspamd-client
%endif
BuildRequires:  apparmor-abstractions
Requires:       apparmor-abstractions
Requires(pre):  shadow
Provides:       group(%{rspamd_group})
Provides:       user(%{rspamd_user})

%description
Rspamd is a spam filtering system that allows evaluation of messages
by a number of rules including regular expressions, statistical analysis and
custom services such as URL black lists. Each message is analysed by rspamd and
given a "spam score".

According to this spam score and the user's settings, rspamd recommends an
action for the MTA to apply to the message, for example to pass, reject or add
a header.  Rspamd is designed to process hundreds of messages per second
simultaneously and has a number of features available.

%if 0%{?with split_out_client}
%package client
#
Summary:        Spam filtering system - Client tools
Group:          Productivity/Networking/Email/Utilities

%description client
Rspamd is a spam filtering system that allows evaluation of messages
by a number of rules including regular expressions, statistical analysis and
custom services such as URL black lists. Each message is analysed by rspamd and
given a "spam score".

According to this spam score and the user's settings, rspamd recommends an
action for the MTA to apply to the message, for example to pass, reject or add
a header.  Rspamd is designed to process hundreds of messages per second
simultaneously and has a number of features available.

This package holds the client tools (rspamc and rspamadm)
%endif

%prep
%autosetup -p1

%build
%if %{with luajit}
if ! [ "%{lua_abi_version}" = "$(pkg-config --variable=abiver luajit | tr -d '.')" ] ; then
  echo "the lua_abi_version define and the abi version of luajit do not match. please investigate. exiting."
  exit 1
fi
%endif
%if 0%{?force_gcc_version}
export CC="gcc-%{?force_gcc_version}"
export CXX="g++-%{?force_gcc_version}"
%endif
%cmake                                      \
%if 0%{?force_gcc_version}
  -DCMAKE_ASM_COMPILER="gcc-%{?force_gcc_version}" \
%else
  -DCMAKE_ASM_COMPILER="gcc"                \
%endif
%if 0%{suse_version} == 1315
  -DCMAKE_USER_MAKE_RULES_OVERRIDE=""       \
%endif
  -DCMAKE_SHARED_LINKER_FLAGS='-flto=auto -Wl,--as-needed -Wl,-z,now' \
  -DCMAKE_EXE_LINKER_FLAGS="%{?build_ldflags} -Wl,--as-needed -Wl,-z,now -pie" \
  -DRSPAMD_LIBDIR=%{_libdir}/rspamd         \
  -DCONFDIR=%{_sysconfdir}/rspamd           \
  -DMANDIR=%{_mandir}                       \
  -DDBDIR=%{_localstatedir}/lib/rspamd      \
  -DRUNDIR=%{_localstatedir}/run/rspamd     \
  -DLOGDIR=%{_localstatedir}/log/rspamd     \
  -DEXAMPLESDIR=%{_datadir}/examples/rspamd \
  -DPLUGINSDIR=%{_datadir}/rspamd/plugins   \
  -DLIBDIR=%{_libdir}/rspamd                \
  -DINCLUDEDIR=%{_includedir}               \
  -DWWWDIR=%{_wwwdir}/%{name}               \
  %if 0%{suse_version} > 1315
  -DENABLE_OPTIMIZATION=ON                  \
  %endif
  -DENABLE_REDIRECTOR=ON                    \
  -DENABLE_LIBUNWIND:BOOL=ON                \
  -DENABLE_BLAS:BOOL=ON                     \
  -DSYSTEM_XXHASH:BOOL=ON                   \
  -DCMAKE_SKIP_INSTALL_RPATH=ON             \
  -DCMAKE_SKIP_RPATH=OFF                    \
  %if %{with luajit}
  -DENABLE_LUAJIT=ON                        \
  %else
  -DENABLE_LUAJIT=OFF                       \
  %endif
  -DENABLE_DB=ON                            \
  -DENABLE_SQLITE=ON                        \
  -DENABLE_HIREDIS=ON                       \
  -DENABLE_URL_INCLUDE=ON                   \
  -DNO_SHARED=ON                            \
  -DINSTALL_EXAMPLES=ON                     \
  -DINSTALL_WEBUI=ON                        \
  %if %{with systemd}
  -DWANT_SYSTEMD_UNITS=ON                   \
  -DSYSTEMDDIR=%{_unitdir}                  \
  %else
  -DWANT_SYSTEMD_UNITS=OFF                  \
  %endif
  %if %{with hyperscan}
  -DENABLE_HYPERSCAN=ON                     \
  %endif
  -DENABLE_GD=ON                            \
  -DENABLE_FANN=ON                          \
  %if %{with utils}
  -DENABLE_UTILS=ON                         \
  %endif
  -DENABLE_PCRE2=ON                         \
  %if %{with jemalloc}
  -DENABLE_JEMALLOC=ON                      \
  %endif
  %if 0%{?with_system_fmt}
  -DSYSTEM_FMT=ON                           \
  %else
  -DSYSTEM_FMT=OFF                          \
  %endif
  -DSYSTEM_ZSTD=ON                          \
  -DDEBIAN_BUILD=1                          \
  -DRSPAMD_GROUP=%{rspamd_group}            \
  -DRSPAMD_USER=%{rspamd_user}
make %{?_smp_mflags}

%install
%cmake_install
perl -p -i -e 's|/usr/bin/env perl|/usr/bin/perl|g' %{buildroot}%{_bindir}/rspamd_stats

mkdir -p                                   \
  %{buildroot}%{_sbindir}                  \
  %{buildroot}%{_localstatedir}/lib/rspamd \
  %{buildroot}%{_localstatedir}/run/rspamd \
  %{buildroot}%{_localstatedir}/log/rspamd

%if %{with systemd}
ln -fs %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}
%endif
ln -s rspamd/librspamd-actrie.so %{buildroot}%{_libdir}
ln -s rspamd/librspamd-server.so %{buildroot}%{_libdir}
ln -s rspamd/librspamd-ev.so %{buildroot}%{_libdir}
ln -s rspamd/librspamd-kann.so %{buildroot}%{_libdir}
ln -s rspamd/librspamd-replxx.so %{buildroot}%{_libdir}

install -d -m 0755 %{buildroot}%{_sysconfdir}/%{name}/local.d
cat > %{buildroot}%{_sysconfdir}/%{name}/local.d/worker-normal.inc << EOF
# If the mailer is running on the same host use a unix socket
#bind_socket = "/run/rspamd/worker.socket mode=0666";
EOF

cat > %{buildroot}%{_sysconfdir}/%{name}/local.d/worker-controller.inc << EOF
# If the mailer is running on the same host use a unix socket
#bind_socket = "/run/rspamd/worker-controller.socket mode=0666";
EOF

cat > %{buildroot}%{_sysconfdir}/%{name}/local.d/worker-proxy.inc << EOF
# If the mailer is running on the same host use a unix socket
#bind_socket = "/run/rspamd/worker-proxy.socket mode=0666";
EOF

install -d -m 0755 %{buildroot}%{_sysconfdir}/%{name}/override.d
mkdir -p %{buildroot}%{_sysconfdir}/apparmor.d/local/
install -D -m644 %{SOURCE1} %{buildroot}%{_sysconfdir}/apparmor.d/usr.bin.rspamd
echo "# Site-specific additions and overrides for 'usr.bin.rspamd'" > %{buildroot}%{_sysconfdir}/apparmor.d/local/usr.bin.rspamd

%pre
%{_sbindir}/groupadd -r %{rspamd_group} 2>/dev/null || :
%{_sbindir}/useradd -g %{rspamd_group} -c "Rmilter user" -s /bin/false -r %{rspamd_user} 2>/dev/null || :
#
# cleanup bad unser files from earlier 3.4 builds
# see https://github.com/rspamd/rspamd/issues/4329 for the details
#
echo "Cleaning up '*.unser' files in /var/lib/rspamd"
find /var/lib/rspamd/ -type f -name '*.unser' -delete -print ||:
%if 0%{?suse_version} && %{with systemd}
%service_add_pre %{name}.service

%post
#systemd-tmpfiles --create /usr/lib/tmpfiles.d/%%{name}.conf ||:
%service_add_post %{name}.service
%endif

%if 0%{?suse_version}
%preun
%if %{with systemd}
%service_del_preun %{name}.service
%else
%stop_on_removal %{name}
%endif
%endif

%if 0%{?suse_version}
%postun
%if %{with systemd}
%service_del_postun %{name}.service
%else
%restart_on_update %{name}
%insserv_cleanup
%endif
%endif

%files
%defattr(-,root,root)
%{_sbindir}/rc%{name}
%{_bindir}/rspamd
%{_bindir}/rspamd-%{version}
%{_bindir}/rspamd_stats
%{_libdir}/librspamd-actrie.so
%{_libdir}/librspamd-server.so
%{_libdir}/librspamd-ev.so
%{_libdir}/librspamd-kann.so
%{_libdir}/librspamd-replxx.so

%dir %{_libdir}/rspamd/
%{_libdir}/rspamd/librspamd-actrie.so
%{_libdir}/rspamd/librspamd-server.so
%{_libdir}/rspamd/librspamd-ev.so
%{_libdir}/rspamd/librspamd-kann.so
%{_libdir}/rspamd/librspamd-replxx.so

%config %{_sysconfdir}/apparmor.d/usr.bin.rspamd
%config(noreplace) %{_sysconfdir}/apparmor.d/local/usr.bin.rspamd

%dir %{_sysconfdir}/rspamd/
%config %{_sysconfdir}/rspamd/actions.conf
%config %{_sysconfdir}/rspamd/cgp.inc
%config %{_sysconfdir}/rspamd/common.conf
%config %{_sysconfdir}/rspamd/composites.conf
%config %{_sysconfdir}/rspamd/groups.conf
%config %{_sysconfdir}/rspamd/logging.inc
%config %{_sysconfdir}/rspamd/metrics.conf
%config %{_sysconfdir}/rspamd/modules.conf
%config %{_sysconfdir}/rspamd/options.inc
%config %{_sysconfdir}/rspamd/rspamd.conf
%config %{_sysconfdir}/rspamd/settings.conf
%config %{_sysconfdir}/rspamd/statistic.conf
%config %{_sysconfdir}/rspamd/worker-controller.inc
%config %{_sysconfdir}/rspamd/worker-fuzzy.inc
%config %{_sysconfdir}/rspamd/worker-normal.inc
%config %{_sysconfdir}/rspamd/worker-proxy.inc
%config %{_sysconfdir}/rspamd/lang_detection.inc

%dir %{_sysconfdir}/rspamd/local.d
%config(noreplace) %{_sysconfdir}/rspamd/local.d/worker-controller.inc
%config(noreplace) %{_sysconfdir}/rspamd/local.d/worker-normal.inc
%config(noreplace) %{_sysconfdir}/rspamd/local.d/worker-proxy.inc
%config(noreplace) %{_sysconfdir}/rspamd/local.d/module.conf.example

%dir %{_sysconfdir}/rspamd/lua.local.d/
%config(noreplace) %{_sysconfdir}/rspamd/lua.local.d/module.lua.example

%dir %{_sysconfdir}/rspamd/scores.d
%config(noreplace) %{_sysconfdir}/rspamd/scores.d/content_group.conf
%config(noreplace) %{_sysconfdir}/rspamd/scores.d/fuzzy_group.conf
%config(noreplace) %{_sysconfdir}/rspamd/scores.d/headers_group.conf
%config(noreplace) %{_sysconfdir}/rspamd/scores.d/hfilter_group.conf
%config(noreplace) %{_sysconfdir}/rspamd/scores.d/mime_types_group.conf
%config(noreplace) %{_sysconfdir}/rspamd/scores.d/mua_group.conf
%config(noreplace) %{_sysconfdir}/rspamd/scores.d/phishing_group.conf
%config(noreplace) %{_sysconfdir}/rspamd/scores.d/policies_group.conf
%config(noreplace) %{_sysconfdir}/rspamd/scores.d/rbl_group.conf
%config(noreplace) %{_sysconfdir}/rspamd/scores.d/statistics_group.conf
%config(noreplace) %{_sysconfdir}/rspamd/scores.d/subject_group.conf
%config(noreplace) %{_sysconfdir}/rspamd/scores.d/surbl_group.conf
%config(noreplace) %{_sysconfdir}/rspamd/scores.d/whitelist_group.conf

%dir %{_sysconfdir}/rspamd/maps.d
%config(noreplace) %{_sysconfdir}/rspamd/maps.d/dmarc_whitelist.inc
%config(noreplace) %{_sysconfdir}/rspamd/maps.d/exe_clickbait.inc
%config(noreplace) %{_sysconfdir}/rspamd/maps.d/maillist.inc
%config(noreplace) %{_sysconfdir}/rspamd/maps.d/mid.inc
%config(noreplace) %{_sysconfdir}/rspamd/maps.d/mime_types.inc
%config(noreplace) %{_sysconfdir}/rspamd/maps.d/redirectors.inc
%config(noreplace) %{_sysconfdir}/rspamd/maps.d/spf_dkim_whitelist.inc
%config(noreplace) %{_sysconfdir}/rspamd/maps.d/surbl-whitelist.inc

%dir %{_sysconfdir}/rspamd/modules.d
%config(noreplace) %{_sysconfdir}/rspamd/modules.d/antivirus.conf
%config(noreplace) %{_sysconfdir}/rspamd/modules.d/aws_s3.conf
%config(noreplace) %{_sysconfdir}/rspamd/modules.d/arc.conf
%config(noreplace) %{_sysconfdir}/rspamd/modules.d/asn.conf
%config(noreplace) %{_sysconfdir}/rspamd/modules.d/bayes_expiry.conf
%config(noreplace) %{_sysconfdir}/rspamd/modules.d/bimi.conf
%config(noreplace) %{_sysconfdir}/rspamd/modules.d/chartable.conf
%config(noreplace) %{_sysconfdir}/rspamd/modules.d/clickhouse.conf
%config(noreplace) %{_sysconfdir}/rspamd/modules.d/contextal.conf
%config(noreplace) %{_sysconfdir}/rspamd/modules.d/dcc.conf
%config(noreplace) %{_sysconfdir}/rspamd/modules.d/dkim.conf
%config(noreplace) %{_sysconfdir}/rspamd/modules.d/dkim_signing.conf
%config(noreplace) %{_sysconfdir}/rspamd/modules.d/dmarc.conf
%config(noreplace) %{_sysconfdir}/rspamd/modules.d/elastic.conf
%config(noreplace) %{_sysconfdir}/rspamd/modules.d/emails.conf
%config(noreplace) %{_sysconfdir}/rspamd/modules.d/external_relay.conf
%config(noreplace) %{_sysconfdir}/rspamd/modules.d/external_services.conf
%config(noreplace) %{_sysconfdir}/rspamd/modules.d/force_actions.conf
%config(noreplace) %{_sysconfdir}/rspamd/modules.d/forged_recipients.conf
%config(noreplace) %{_sysconfdir}/rspamd/modules.d/fuzzy_check.conf
%config(noreplace) %{_sysconfdir}/rspamd/modules.d/greylist.conf
%config(noreplace) %{_sysconfdir}/rspamd/modules.d/gpt.conf
%config(noreplace) %{_sysconfdir}/rspamd/modules.d/history_redis.conf
%config(noreplace) %{_sysconfdir}/rspamd/modules.d/hfilter.conf
%config(noreplace) %{_sysconfdir}/rspamd/modules.d/http_headers.conf
%config(noreplace) %{_sysconfdir}/rspamd/modules.d/known_senders.conf
%config(noreplace) %{_sysconfdir}/rspamd/modules.d/maillist.conf
%config(noreplace) %{_sysconfdir}/rspamd/modules.d/metadata_exporter.conf
%config(noreplace) %{_sysconfdir}/rspamd/modules.d/metric_exporter.conf
%config(noreplace) %{_sysconfdir}/rspamd/modules.d/mid.conf
%config(noreplace) %{_sysconfdir}/rspamd/modules.d/mime_types.conf
%config(noreplace) %{_sysconfdir}/rspamd/modules.d/multimap.conf
%config(noreplace) %{_sysconfdir}/rspamd/modules.d/mx_check.conf
%config(noreplace) %{_sysconfdir}/rspamd/modules.d/neural.conf
%config(noreplace) %{_sysconfdir}/rspamd/modules.d/once_received.conf
%config(noreplace) %{_sysconfdir}/rspamd/modules.d/p0f.conf
%config(noreplace) %{_sysconfdir}/rspamd/modules.d/phishing.conf
%config(noreplace) %{_sysconfdir}/rspamd/modules.d/ratelimit.conf
%config(noreplace) %{_sysconfdir}/rspamd/modules.d/rbl.conf
%config(noreplace) %{_sysconfdir}/rspamd/modules.d/redis.conf
%config(noreplace) %{_sysconfdir}/rspamd/modules.d/regexp.conf
%config(noreplace) %{_sysconfdir}/rspamd/modules.d/replies.conf
%config(noreplace) %{_sysconfdir}/rspamd/modules.d/reputation.conf
%config(noreplace) %{_sysconfdir}/rspamd/modules.d/milter_headers.conf
%config(noreplace) %{_sysconfdir}/rspamd/modules.d/rspamd_update.conf
%config(noreplace) %{_sysconfdir}/rspamd/modules.d/spamassassin.conf
%config(noreplace) %{_sysconfdir}/rspamd/modules.d/spamtrap.conf
%config(noreplace) %{_sysconfdir}/rspamd/modules.d/spf.conf
%config(noreplace) %{_sysconfdir}/rspamd/modules.d/surbl.conf
%config(noreplace) %{_sysconfdir}/rspamd/modules.d/trie.conf
%config(noreplace) %{_sysconfdir}/rspamd/modules.d/url_redirector.conf
%config(noreplace) %{_sysconfdir}/rspamd/modules.d/whitelist.conf

%dir %{_sysconfdir}/rspamd/override.d
%config(noreplace) %{_sysconfdir}/rspamd/override.d/module.conf.example

%dir %{_sysconfdir}/rspamd/modules.local.d/
%config(noreplace) %{_sysconfdir}/rspamd/modules.local.d/module.conf.example

%dir %{_datadir}/rspamd

%{_datadir}/rspamd/effective_tld_names.dat

%dir %{_datadir}/rspamd/languages
%{_datadir}/rspamd/languages/*

%dir %{_datadir}/rspamd/plugins
%{_datadir}/rspamd/plugins/aws_s3.lua
%{_datadir}/rspamd/plugins/bimi.lua
%{_datadir}/rspamd/plugins/external_relay.lua
%{_datadir}/rspamd/plugins/http_headers.lua
%{_datadir}/rspamd/plugins/antivirus.lua
%{_datadir}/rspamd/plugins/arc.lua
%{_datadir}/rspamd/plugins/asn.lua
%{_datadir}/rspamd/plugins/bayes_expiry.lua
%{_datadir}/rspamd/plugins/clickhouse.lua
%{_datadir}/rspamd/plugins/contextal.lua
%{_datadir}/rspamd/plugins/clustering.lua
%{_datadir}/rspamd/plugins/dcc.lua
%{_datadir}/rspamd/plugins/dkim_signing.lua
%{_datadir}/rspamd/plugins/dmarc.lua
%{_datadir}/rspamd/plugins/dynamic_conf.lua
%{_datadir}/rspamd/plugins/elastic.lua
%{_datadir}/rspamd/plugins/emails.lua
%{_datadir}/rspamd/plugins/external_services.lua
%{_datadir}/rspamd/plugins/force_actions.lua
%{_datadir}/rspamd/plugins/forged_recipients.lua
%{_datadir}/rspamd/plugins/fuzzy_collect.lua
%{_datadir}/rspamd/plugins/greylist.lua
%{_datadir}/rspamd/plugins/gpt.lua
%{_datadir}/rspamd/plugins/hfilter.lua
%{_datadir}/rspamd/plugins/history_redis.lua
%{_datadir}/rspamd/plugins/ip_score.lua
%{_datadir}/rspamd/plugins/known_senders.lua
%{_datadir}/rspamd/plugins/maillist.lua
%{_datadir}/rspamd/plugins/maps_stats.lua
%{_datadir}/rspamd/plugins/metadata_exporter.lua
%{_datadir}/rspamd/plugins/metric_exporter.lua
%{_datadir}/rspamd/plugins/mid.lua
%{_datadir}/rspamd/plugins/milter_headers.lua
%{_datadir}/rspamd/plugins/mime_types.lua
%{_datadir}/rspamd/plugins/multimap.lua
%{_datadir}/rspamd/plugins/mx_check.lua
%{_datadir}/rspamd/plugins/neural.lua
%{_datadir}/rspamd/plugins/once_received.lua
%{_datadir}/rspamd/plugins/p0f.lua
%{_datadir}/rspamd/plugins/phishing.lua
%{_datadir}/rspamd/plugins/ratelimit.lua
%{_datadir}/rspamd/plugins/rbl.lua
%{_datadir}/rspamd/plugins/replies.lua
%{_datadir}/rspamd/plugins/reputation.lua
%{_datadir}/rspamd/plugins/rspamd_update.lua
%{_datadir}/rspamd/plugins/settings.lua
%{_datadir}/rspamd/plugins/spamassassin.lua
%{_datadir}/rspamd/plugins/spamtrap.lua
%{_datadir}/rspamd/plugins/spf.lua
%{_datadir}/rspamd/plugins/trie.lua
%{_datadir}/rspamd/plugins/url_redirector.lua
%{_datadir}/rspamd/plugins/whitelist.lua

%dir %{_datadir}/rspamd/lualib
%{_datadir}/rspamd/lualib/ansicolors.lua
%{_datadir}/rspamd/lualib/argparse.lua
%{_datadir}/rspamd/lualib/fun.lua
%{_datadir}/rspamd/lualib/global_functions.lua
%{_datadir}/rspamd/lualib/lpegre.lua
%{_datadir}/rspamd/lualib/lua_auth_results.lua
%{_datadir}/rspamd/lualib/lua_aws.lua
%{_datadir}/rspamd/lualib/lua_bayes_learn.lua
%{_datadir}/rspamd/lualib/lua_cfg_transform.lua
%{_datadir}/rspamd/lualib/lua_cfg_utils.lua
%{_datadir}/rspamd/lualib/lua_clickhouse.lua
%{_datadir}/rspamd/lualib/lua_dkim_tools.lua
%{_datadir}/rspamd/lualib/lua_fuzzy.lua
%{_datadir}/rspamd/lualib/lua_lexer.lua
%{_datadir}/rspamd/lualib/lua_maps.lua
%{_datadir}/rspamd/lualib/lua_maps_expressions.lua
%{_datadir}/rspamd/lualib/lua_meta.lua
%{_datadir}/rspamd/lualib/lua_mime.lua
%{_datadir}/rspamd/lualib/lua_mime_types.lua
%{_datadir}/rspamd/lualib/lua_redis.lua
%{_datadir}/rspamd/lualib/lua_settings.lua
%{_datadir}/rspamd/lualib/lua_smtp.lua
%{_datadir}/rspamd/lualib/lua_stat.lua
%{_datadir}/rspamd/lualib/lua_tcp_sync.lua
%{_datadir}/rspamd/lualib/lua_urls_compose.lua
%{_datadir}/rspamd/lualib/lua_util.lua
%{_datadir}/rspamd/lualib/lua_verdict.lua
%{_datadir}/rspamd/lualib/lupa.lua
%{_datadir}/rspamd/lualib/plugins_stats.lua
%{_datadir}/rspamd/lualib/tableshape.lua
%{_datadir}/rspamd/lualib/lua_bayes_redis.lua
%{_datadir}/rspamd/lualib/lua_cache.lua

%dir %{_datadir}/rspamd/lualib/lua_content
%{_datadir}/rspamd/lualib/lua_content/ical.lua
%{_datadir}/rspamd/lualib/lua_content/init.lua
%{_datadir}/rspamd/lualib/lua_content/pdf.lua
%{_datadir}/rspamd/lualib/lua_content/vcard.lua

%dir %{_datadir}/rspamd/lualib/lua_ffi
%{_datadir}/rspamd/lualib/lua_ffi/common.lua
%{_datadir}/rspamd/lualib/lua_ffi/dkim.lua
%{_datadir}/rspamd/lualib/lua_ffi/init.lua
%{_datadir}/rspamd/lualib/lua_ffi/linalg.lua
%{_datadir}/rspamd/lualib/lua_ffi/spf.lua

%dir %{_datadir}/rspamd/lualib/lua_magic
%{_datadir}/rspamd/lualib/lua_magic/heuristics.lua
%{_datadir}/rspamd/lualib/lua_magic/init.lua
%{_datadir}/rspamd/lualib/lua_magic/patterns.lua
%{_datadir}/rspamd/lualib/lua_magic/types.lua

%dir %{_datadir}/rspamd/lualib/lua_scanners
%{_datadir}/rspamd/lualib/lua_scanners/avast.lua
%{_datadir}/rspamd/lualib/lua_scanners/clamav.lua
%{_datadir}/rspamd/lualib/lua_scanners/cloudmark.lua
%{_datadir}/rspamd/lualib/lua_scanners/common.lua
%{_datadir}/rspamd/lualib/lua_scanners/dcc.lua
%{_datadir}/rspamd/lualib/lua_scanners/fprot.lua
%{_datadir}/rspamd/lualib/lua_scanners/icap.lua
%{_datadir}/rspamd/lualib/lua_scanners/init.lua
%{_datadir}/rspamd/lualib/lua_scanners/kaspersky_av.lua
%{_datadir}/rspamd/lualib/lua_scanners/kaspersky_se.lua
%{_datadir}/rspamd/lualib/lua_scanners/oletools.lua
%{_datadir}/rspamd/lualib/lua_scanners/p0f.lua
%{_datadir}/rspamd/lualib/lua_scanners/pyzor.lua
%{_datadir}/rspamd/lualib/lua_scanners/razor.lua
%{_datadir}/rspamd/lualib/lua_scanners/savapi.lua
%{_datadir}/rspamd/lualib/lua_scanners/sophos.lua
%{_datadir}/rspamd/lualib/lua_scanners/spamassassin.lua
%{_datadir}/rspamd/lualib/lua_scanners/vadesecure.lua
%{_datadir}/rspamd/lualib/lua_scanners/virustotal.lua

%dir %{_datadir}/rspamd/lualib/lua_selectors
%{_datadir}/rspamd/lualib/lua_selectors/common.lua
%{_datadir}/rspamd/lualib/lua_selectors/extractors.lua
%{_datadir}/rspamd/lualib/lua_selectors/init.lua
%{_datadir}/rspamd/lualib/lua_selectors/maps.lua
%{_datadir}/rspamd/lualib/lua_selectors/transforms.lua

%dir %{_datadir}/rspamd/lualib/rspamadm
%{_datadir}/rspamd/lualib/rspamadm/clickhouse.lua
%{_datadir}/rspamd/lualib/rspamadm/configgraph.lua
%{_datadir}/rspamd/lualib/rspamadm/confighelp.lua
%{_datadir}/rspamd/lualib/rspamadm/configwizard.lua
%{_datadir}/rspamd/lualib/rspamadm/cookie.lua
%{_datadir}/rspamd/lualib/rspamadm/classifier_test.lua
%{_datadir}/rspamd/lualib/rspamadm/corpus_test.lua
%{_datadir}/rspamd/lualib/rspamadm/dmarc_report.lua
%{_datadir}/rspamd/lualib/rspamadm/dns_tool.lua
%{_datadir}/rspamd/lualib/rspamadm/fuzzy_convert.lua
%{_datadir}/rspamd/lualib/rspamadm/fuzzy_stat.lua
%{_datadir}/rspamd/lualib/rspamadm/grep.lua
%{_datadir}/rspamd/lualib/rspamadm/keypair.lua
%{_datadir}/rspamd/lualib/rspamadm/mime.lua
%{_datadir}/rspamd/lualib/rspamadm/publicsuffix.lua
%{_datadir}/rspamd/lualib/rspamadm/stat_convert.lua
%{_datadir}/rspamd/lualib/rspamadm/statistics_dump.lua
%{_datadir}/rspamd/lualib/rspamadm/template.lua
%{_datadir}/rspamd/lualib/rspamadm/vault.lua
%{_datadir}/rspamd/lualib/rspamadm/neural_test.lua
%{_datadir}/rspamd/lualib/rspamadm/dkim_keygen.lua
%{_datadir}/rspamd/lualib/rspamadm/fuzzy_ping.lua
%{_datadir}/rspamd/lualib/rspamadm/secretbox.lua
%{_datadir}/rspamd/lualib/rspamadm/ratelimit.lua

%dir %{_datadir}/rspamd/lualib/plugins
%{_datadir}/rspamd/lualib/plugins/dmarc.lua
%{_datadir}/rspamd/lualib/plugins/neural.lua
%{_datadir}/rspamd/lualib/plugins/rbl.lua
%{_datadir}/rspamd/lualib/plugins/ratelimit.lua

%dir %{_datadir}/rspamd/lualib/redis_scripts/
%{_datadir}/rspamd/lualib/redis_scripts/neural_maybe_invalidate.lua
%{_datadir}/rspamd/lualib/redis_scripts/neural_maybe_lock.lua
%{_datadir}/rspamd/lualib/redis_scripts/neural_save_unlock.lua
%{_datadir}/rspamd/lualib/redis_scripts/neural_train_size.lua
%{_datadir}/rspamd/lualib/redis_scripts/ratelimit_check.lua
%{_datadir}/rspamd/lualib/redis_scripts/ratelimit_cleanup_pending.lua
%{_datadir}/rspamd/lualib/redis_scripts/ratelimit_update.lua
%{_datadir}/rspamd/lualib/redis_scripts/bayes_cache_check.lua
%{_datadir}/rspamd/lualib/redis_scripts/bayes_cache_learn.lua
%{_datadir}/rspamd/lualib/redis_scripts/bayes_classify.lua
%{_datadir}/rspamd/lualib/redis_scripts/bayes_learn.lua
%{_datadir}/rspamd/lualib/redis_scripts/bayes_stat.lua

%dir %{_datadir}/rspamd/rules
%{_datadir}/rspamd/rules/archives.lua
%{_datadir}/rspamd/rules/bitcoin.lua
%{_datadir}/rspamd/rules/bounce.lua
%{_datadir}/rspamd/rules/content.lua
%{_datadir}/rspamd/rules/forwarding.lua
%{_datadir}/rspamd/rules/headers_checks.lua
%{_datadir}/rspamd/rules/html.lua
%{_datadir}/rspamd/rules/mid.lua
%{_datadir}/rspamd/rules/misc.lua
%{_datadir}/rspamd/rules/parts.lua
%{_datadir}/rspamd/rules/rspamd.lua
%{_datadir}/rspamd/rules/subject_checks.lua
%{_datadir}/rspamd/rules/regexp/urls.lua

%dir %{_datadir}/rspamd/rules/regexp
%{_datadir}/rspamd/rules/regexp/compromised_hosts.lua
%{_datadir}/rspamd/rules/regexp/headers.lua
%{_datadir}/rspamd/rules/regexp/misc.lua
%{_datadir}/rspamd/rules/regexp/upstream_spam_filters.lua
%{_datadir}/rspamd/rules/controller

%{_mandir}/man8/rspamd.8*

%{_unitdir}/rspamd.service

%dir %attr(750,%{rspamd_user},%{rspamd_group}) %{_localstatedir}/lib/rspamd
%dir %attr(750,%{rspamd_user},%{rspamd_group}) %{_localstatedir}/log/rspamd

%dir /srv/www
%dir %{_wwwdir}
%dir %{_wwwdir}/%{name}
%{_wwwdir}/%{name}/apple-touch-icon.png
%{_wwwdir}/%{name}/browserconfig.xml
%{_wwwdir}/%{name}/README.md
%{_wwwdir}/%{name}/favicon.ico
%{_wwwdir}/%{name}/favicon-16x16.png
%{_wwwdir}/%{name}/favicon-32x32.png
%{_wwwdir}/%{name}/index.html
%{_wwwdir}/%{name}/mstile-150x150.png
%{_wwwdir}/%{name}/safari-pinned-tab.svg

%{_wwwdir}/%{name}/css

%dir %{_wwwdir}/%{name}/fonts
%{_wwwdir}/%{name}/fonts/glyphicons-halflings-regular.ttf
%{_wwwdir}/%{name}/fonts/glyphicons-halflings-regular.woff
%{_wwwdir}/%{name}/fonts/glyphicons-halflings-regular.woff2

%dir %{_wwwdir}/%{name}/img
%{_wwwdir}/%{name}/img/asc.png
%{_wwwdir}/%{name}/img/desc.png
%{_wwwdir}/%{name}/img/rspamd_logo_navbar.png
%{_wwwdir}/%{name}/img/drop-area.svg

%dir %{_wwwdir}/%{name}/js
%{_wwwdir}/%{name}/js/main.js

%dir %{_wwwdir}/%{name}/js/app
%{_wwwdir}/%{name}/js/app/config.js
%{_wwwdir}/%{name}/js/app/graph.js
%{_wwwdir}/%{name}/js/app/history.js
%{_wwwdir}/%{name}/js/app/rspamd.js
%{_wwwdir}/%{name}/js/app/selectors.js
%{_wwwdir}/%{name}/js/app/stats.js
%{_wwwdir}/%{name}/js/app/symbols.js
%{_wwwdir}/%{name}/js/app/upload.js
%{_wwwdir}/%{name}/js/app/common.js
%{_wwwdir}/%{name}/js/app/libft.js

%{_wwwdir}/%{name}/js/lib

%if 0%{?with split_out_client}
%files client
%endif
%{_mandir}/man1/rspamadm.1*
%{_mandir}/man1/rspamc.1*
%{_bindir}/rspamadm
%{_bindir}/rspamadm-%{version}
%{_bindir}/rspamc
%{_bindir}/rspamc-%{version}

%changelog
