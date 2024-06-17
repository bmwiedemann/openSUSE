#
# spec file for package coturn
#
# Copyright (c) 2023 SUSE LLC
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


%global _lto_cflags %{?_lto_cflags} -ffat-lto-objects
%if 0%{?suse_version} > 1320
%bcond_without  apparmor_reload
%else
%bcond_with     apparmor_reload
%endif
%bcond_without  apparmor
Name:           coturn
Version:        4.6.2
Release:        0
Summary:        TURN and STUN server for VoIP
License:        BSD-3-Clause
Group:          Productivity/Networking/Talk/Servers
URL:            https://github.com/coturn/coturn/
Source0:        https://github.com/coturn/coturn/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}.service
Source2:        %{name}.tmpfilesd
Source3:        %{name}.logrotate
Source4:        %{name}-user.conf
Source5:        %{name}.sysconfig
Source6:        %{name}.firewalld
Source7:        README.SUSE
Source8:        %{name}-apparmor-usr.bin.turnserver
Source9:        %{name}@.service
Patch0:         %{name}-turnserver_conf.patch
BuildRequires:  firewall-macros
BuildRequires:  libevent-devel >= 2.0.0
BuildRequires:  libmysqld-devel
BuildRequires:  p11-kit
BuildRequires:  pkgconfig
BuildRequires:  sysuser-tools
BuildRequires:  pkgconfig(hiredis)
BuildRequires:  pkgconfig(libpq)
BuildRequires:  pkgconfig(libssl) >= 1.0.2
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(systemd)
Requires(pre):  %fillup_prereq
Requires(pre):  shadow
Recommends:     logrotate

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

%{?systemd_ordering}
%sysusers_requires

%description
STUN (Session Traversal Utilities for NAT) and TURN (Traversal Using Relays
around NAT) are protocols that can be used to provide NAT traversal for VoIP
and WebRTC.

It can be used as a general-purpose network traffic TURN server and gateway,
too. On-line management interface (over telnet or over HTTPS) for the TURN
server is available.

%package        utils
Summary:        Coturn utils
Group:          Productivity/Networking/Talk/Servers

%description    utils
This package contains the TURN client utils.

%package        devel
Summary:        Coturn development headers
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

%description    devel
This package contains the TURN development headers.

%prep
%autosetup -p0 -n %{name}-%{version}

%build
%sysusers_generate_pre %{SOURCE4} %{name}

%configure \
	--confdir=%{_sysconfdir}/%{name} \
	--examplesdir=%{_docdir}/%{name} \
	--schemadir=%{_datadir}/%{name} \
	--manprefix=%{_datadir} \
	--docdir=%{_docdir}/%{name} \
	--turndbdir=%{_localstatedir}/lib/%{name} \
	--disable-rpath
%make_build

%check
%make_build test

%install
%make_install
mkdir -p %{buildroot}{%{_sysconfdir}/%{name}/tls,{%{_rundir},%{_localstatedir}/{lib,log}}/%{name},%{_unitdir},%{_sysusersdir},%{_sbindir},%{_sysconfdir}/apparmor.d/local}
install -Dpm 0644 %{SOURCE1} %{buildroot}%{_unitdir}/
install -Dpm 0644 %{SOURCE9} %{buildroot}%{_unitdir}/
install -Dpm 0644 %{SOURCE2} %{buildroot}%{_tmpfilesdir}/%{name}.conf
install -Dpm 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/logrotate.d/%{name}
install -Dpm 0644 %{SOURCE4} %{buildroot}%{_sysusersdir}/
install -Dpm 0644 %{SOURCE5} %{buildroot}%{_fillupdir}/sysconfig.%{name}
install -Dpm 0644 %{SOURCE6} %{buildroot}%{_prefix}/lib/firewalld/services/%{name}.xml
install -Dpm 0644 %{SOURCE7} %{buildroot}%{_docdir}/%{name}/
%if %{with apparmor}
install -Dpm 0644 %{SOURCE8} %{buildroot}%{_sysconfdir}/apparmor.d/usr.bin.turnserver
cat > %{buildroot}%{_sysconfdir}/apparmor.d/local/usr.bin.turnserver << EOF
# Site-specific additions and overrides for usr.bin.turnserver
# See /etc/apparmor.d/local/README for details.
EOF
%endif

install examples%{_sysconfdir}/turnserver.conf %{buildroot}%{_sysconfdir}/%{name}/turnserver.conf.default
install examples%{_sysconfdir}/turnserver.conf %{buildroot}%{_sysconfdir}/%{name}/turnserver.conf

sed -i \
    -e "s|^#*\(listening-port=.*\)|\1|" \
    -e "s|^#*\(tls-listening-port=.*\)|\1|" \
    -e "s|^#*\(listening-ip=\)$|\1|" \
    -e "s|^#*verbose|verbose|" \
    -e "s|^#*fingerprint|fingerprint|" \
    -e "s|^#*use-auth-secret|use-auth-secret|" \
    -e "s|^#\(static-auth-secret=.*\)|\1|" \
    -e "s|^#\(realm=\).*|\1|" \
    -e "s|^#\(total-quota=.*\)|\1|" \
    -e "s|^#\(bps-capacity=.*\)|\1|" \
    -e "s|^#\(stale-nonce=.*\)|\1|" \
    -e "s|^#*\(cert=.*\)|\1|" \
    -e "s|^#*\(pkey=.*\)|\1|" \
    -e "s|^#\(log-file=.*\)|\1|" \
    -e "s|^#*simple-log|simple-log|g" \
    -e "s|^#*no-multicast-peers|no-multicast-peers|g" \
    -e "s|^#*no-tlsv1|no-tlsv1|g" \
    -e "s|^#*no-tlsv1_1|no-tlsv1_1|g" \
    -e "/^#/d" -e "/^$/d" \
    %{buildroot}%{_sysconfdir}/%{name}/turnserver.conf

# Remove certs and keys
rm %{buildroot}%{_docdir}/%{name}%{_sysconfdir}/*.pem

# fix permissions
find %{buildroot}/%{_docdir} -type f -exec chmod 0644 {} +
chmod 0644 %{buildroot}%{_mandir}/man1/*
chmod 0644 %{buildroot}%{_datadir}/%{name}/*

# compatibility link
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}

# manually create and symlink man pages
rm %{buildroot}%{_mandir}/man1/{turnutils_*,coturn.1}
gzip %{buildroot}%{_mandir}/man1/*.1
ln -s turnserver.1.gz %{buildroot}%{_mandir}/man1/coturn.1.gz
for PKG in natdiscovery oauth peer stunclient uclient ; do
	ln -s turnutils.1.gz %{buildroot}%{_mandir}/man1/turnutils_$PKG.1.gz
done

%pre -f %{name}.pre
%service_add_pre %{name}.service
%service_add_pre %{name}@.service

%post
# generate static-auth-secret only on install, not on upgrade
if [ $1 -eq 1 ]; then
  sed -i -e "s|^\(static-auth-secret=\)north|\1$(openssl rand -hex 32)|" %{_sysconfdir}/%{name}/turnserver.conf
fi
%service_add_post %{name}.service
%service_add_post %{name}@.service
systemd-tmpfiles --create %{_prefix}/lib/tmpfiles.d/%{name}.conf
%{fillup_only -n %{name}}
%firewalld_reload
%if %{with apparmor} && %{with apparmor_reload}
%apparmor_reload %{_sysconfdir}/apparmor.d/usr.bin.turnserver
%endif

%preun
%service_del_preun %{name}.service
%service_del_preun %{name}@.service

%postun
%service_del_postun %{name}.service
%service_del_postun %{name}@.service

%files
%license LICENSE
%{_sysusersdir}/%{name}-user.conf
%{_sbindir}/rc%{name}
%{_fillupdir}/sysconfig.coturn
%dir %{_prefix}/lib/firewalld
%dir %{_prefix}/lib/firewalld/services
%{_prefix}/lib/firewalld/services/coturn.xml

%{_bindir}/turnserver
%{_bindir}/turnadmin
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*.redis
%{_datadir}/%{name}/*.sql
%attr(0750,-,-) %{_datadir}/%{name}/*.sh
%dir %{_docdir}/%{name}
%{_docdir}/%{name}/README.*
%exclude %{_docdir}/%{name}/README.turnutils
%exclude %{_docdir}/%{name}/INSTALL
%exclude %{_docdir}/%{name}/LICENSE
%exclude %{_docdir}/%{name}/postinstall.txt
%dir %{_docdir}/%{name}%{_sysconfdir}
%doc %{_docdir}/%{name}%{_sysconfdir}/*
%dir %{_docdir}/%{name}/scripts
%dir %{_docdir}/%{name}/scripts/*
%{_docdir}/%{name}/scripts/*.sh
%{_docdir}/%{name}/scripts/readme.txt
%doc %{_docdir}/%{name}/scripts/*/*

#Don't package schemas twice
%exclude %doc %{_docdir}/%{name}/schema.*

%{_mandir}/man1/coturn.1%{?ext_man}
%{_mandir}/man1/turnserver.1%{?ext_man}
%{_mandir}/man1/turnadmin.1%{?ext_man}

%dir %attr(0750,root,%{name}) %{_sysconfdir}/%{name}
%config(noreplace) %attr(0640,root,%{name}) %{_sysconfdir}/%{name}/turnserver.conf
%config %attr(0640,root,%{name}) %{_sysconfdir}/%{name}/turnserver.conf.default
%dir %attr(0750,%{name},root) %{_sysconfdir}/%{name}/tls
%{_unitdir}/coturn.service
%{_unitdir}/coturn@.service
%{_tmpfilesdir}/coturn.conf
%dir %ghost %attr(0750,%{name},%{name}) %{_rundir}/%{name}
%dir %attr(0750,%{name},%{name}) %{_localstatedir}/lib/%{name}
%dir %attr(0750,%{name},%{name}) %{_localstatedir}/log/%{name}
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}

%if %{with apparmor}
%dir %{_sysconfdir}/apparmor.d
%dir %{_sysconfdir}/apparmor.d/local
%config %{_sysconfdir}/apparmor.d/usr.bin.turnserver
%config(noreplace) %{_sysconfdir}/apparmor.d/local/usr.bin.turnserver
%endif

%files utils
%license LICENSE
%{_bindir}/turnutils_peer
%{_bindir}/turnutils_stunclient
%{_bindir}/turnutils_uclient
%{_bindir}/turnutils_oauth
%{_bindir}/turnutils_natdiscovery
%doc %{_docdir}/%{name}/README.turnutils
%{_mandir}/man1/turnutils.1%{?ext_man}
%{_mandir}/man1/turnutils_*.1%{?ext_man}

%files devel
%defattr(0644,root,root)
%license LICENSE
%{_includedir}/turn
%{_libdir}/libturnclient.a

%changelog
