#
# spec file for package unbound
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
  %define _fillupdir /var/adm/fillup-templates
%endif

%bcond_without python2
%bcond_without python3
%bcond_without munin
%bcond_without hardened_build
%bcond_without dnstap
%bcond_without systemd

#
%define _sharedstatedir /var/lib/
%define ldns_version 1.6.16

#
%define piddir /run

Name:           unbound
Version:        1.12.0
Release:        0
#
#
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  flex
BuildRequires:  ldns-devel >= %{ldns_version}
BuildRequires:  libevent-devel
BuildRequires:  libexpat-devel
BuildRequires:  libsodium-devel
BuildRequires:  openssl-devel
%if %{with dnstap}
BuildRequires:  libfstrm-devel
BuildRequires:  libprotobuf-c-devel >= 1.0.0
BuildRequires:  protobuf-c >= 1.0.0
%endif
%if %{with python2}
BuildRequires:  python-rpm-macros
BuildRequires:  python2-devel
BuildRequires:  swig
%endif
%if %{with python3}
BuildRequires:  python-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  swig
%endif

Requires:       ldns >= %{ldns_version}
# until we figured something else out for the unbound-anchor part in the systemd unit file
Requires:       sudo
%if %{with systemd}
BuildRequires:  pkgconfig(libsystemd)
%{?systemd_requires}
%endif
#
URL:            https://www.unbound.net/
Source:         https://www.unbound.net/downloads/unbound-%{version}.tar.gz
Source1:        unbound.service
Source2:        unbound.conf
Source3:        unbound.munin
Source4:        unbound_munin_
Source5:        root.key
Source6:        dlv.isc.org.key
Source7:        unbound-keygen.service
Source8:        tmpfiles-unbound.conf
Source9:        example.com.key
Source10:       example.com.conf
Source11:       block-example.com.conf
# From http://data.iana.org/root-anchors/icannbundle.pem
Source12:       icannbundle.pem
Source13:       root.anchor
Source14:       unbound.sysconfig
Source15:       unbound-anchor.timer
Source16:       unbound-munin.README
Source18:       unbound-anchor.service

Summary:        Validating, recursive, and caching DNS(SEC) resolver
License:        BSD-3-Clause
Group:          Productivity/Networking/DNS/Servers

%description
Unbound is a validating, recursive, and caching DNS(SEC) resolver.

The C implementation of Unbound is developed and maintained by NLnet
Labs. It is based on ideas and algorithms taken from a java prototype
developed by Verisign labs, Nominet, Kirei and ep.net.

Unbound is designed as a set of modular components, so that also
DNSSEC (secure DNS) validation and stub-resolvers (that do not run
as a server, but are linked into an application) are easily possible.

%define libname libunbound8
%package -n %{libname}
Requires:       %{name}-anchor >= %{version}
#
Summary:        Shared library from unbound
Group:          Development/Libraries/C and C++

%description -n %{libname}
Unbound is a validating, recursive, and caching DNS(SEC) resolver.

This package holds the shared library from unbound.

%if %{with_munin}
%package munin
Summary:        Plugin for the munin / munin-node monitoring package
Group:          System/Daemons
Requires:       %{name} = %{version}
Requires:       bc
Requires:       munin-node
BuildArch:      noarch

%description munin
Unbound is a validating, recursive, and caching DNS(SEC) resolver.

This package holds the plugin for the munin / munin-node monitoring package
%endif

%package devel
Requires:       %{libname} = %{version}
Requires:       ldns-devel >= %{ldns_version}
Requires:       openssl-devel
Provides:       libunbound-devel = %{version}-%{release}
#
Summary:        Development files for libunbound
Group:          Development/Libraries/C and C++

%description devel
Unbound is a validating, recursive, and caching DNS(SEC) resolver.

This package holds the development files to work with libunbound.

%package anchor
#
Summary:        Unbound Anchor cert management tools
Group:          Productivity/Networking/DNS/Servers
Requires(pre):  shadow

%description anchor
Unbound is a validating, recursive, and caching DNS(SEC) resolver.

This package contains the tools to manage the anchor certs.

%if %{with python3}
%package -n python3-unbound
Summary:        Python modules and extensions for unbound
Group:          Applications/System
Requires:       %{libname} = %{version}
Obsoletes:      unbound-python
Provides:       unbound-python

%description -n python3-unbound
Unbound is a validating, recursive, and caching DNS(SEC) resolver.

This package holds the Python modules and extensions for unbound.
%endif

%if %{with python2}
%package -n python2-unbound
Summary:        Python modules and extensions for unbound
Group:          Applications/System
Requires:       %{libname} = %{version}

%description -n python2-unbound
Unbound is a validating, recursive, and caching DNS(SEC) resolver.

This package holds the Python modules and extensions for unbound.
%endif

%prep
%setup
%if %{with python2}
pushd ..
cp -pr %{name}-%{version} p2
popd
%endif

%build
export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags}"

%if %{with python2}
pushd ../p2
%configure \
  --disable-rpath \
  --with-libevent \
  --with-pthreads \
  --disable-static \
  --with-ldns=%{_prefix} \
  --enable-sha2 \
  --enable-gost \
  --enable-ecdsa \
  --enable-event-api \
  --enable-pie \
  --enable-relro-now \
  --enable-dnscrypt \
%if %{with dnstap}
  --enable-dnstap \
%endif
  --with-conf-file=%{_sysconfdir}/%{name}/unbound.conf \
  --with-pidfile=%{piddir}%{name}/%{name}.pid \
  --with-pythonmodule --with-pyunbound PYTHON=%{__python2}\
  --with-rootkey-file=%{_sharedstatedir}/unbound/root.key

make %{?_smp_mflags} all streamtcp
popd
%endif

%configure \
  --disable-rpath \
  --with-libevent \
  --with-pthreads \
  --disable-static \
  --with-ldns=%{_prefix} \
  --enable-sha2 \
  --enable-gost \
  --enable-ecdsa \
  --enable-event-api \
  --enable-pie \
  --enable-relro-now \
  --enable-dnscrypt \
%if %{with dnstap}
  --enable-dnstap \
%endif
  --with-conf-file=%{_sysconfdir}/%{name}/unbound.conf \
  --with-pidfile=%{piddir}%{name}/%{name}.pid \
%if %{with python3}
  --with-pythonmodule --with-pyunbound PYTHON=%{__python3}\
%endif
  --with-rootkey-file=%{_sharedstatedir}/unbound/root.key

make %{?_smp_mflags} all streamtcp

%install
%if %{with python2}
pushd ../p2
%make_install
popd
%endif

%make_install

install -d -m 0750                %{buildroot}/var/lib/unbound
install -d 0755                   %{buildroot}%{_unitdir}
install -p -m 0644 %{SOURCE1}     %{buildroot}%{_unitdir}/unbound.service
install -p -m 0644 %{SOURCE7}     %{buildroot}%{_unitdir}/unbound-keygen.service
install -p -m 0644 %{SOURCE2}     %{buildroot}%{_sysconfdir}/unbound
install -p -m 0644 %{SOURCE12}    %{buildroot}%{_sysconfdir}/unbound
install -D -p -m 0644 %{SOURCE14} %{buildroot}%{_fillupdir}/sysconfig.%{name}
ln -sf /usr/sbin/service          %{buildroot}%{_sbindir}/rcunbound
ln -sf /usr/sbin/service          %{buildroot}%{_sbindir}/rcunbound-keygen

install -p -m 0644 %{SOURCE15}    %{buildroot}%{_unitdir}/unbound-anchor.timer
install -p -m 0644 %{SOURCE18}    %{buildroot}%{_unitdir}/unbound-anchor.service
install -p -m 0644 %{SOURCE16}  .

%if %{with munin}
# Install munin plugin and its softlinks
install -d 0755                   %{buildroot}%{_sysconfdir}/munin/plugin-conf.d
install -p -m 0644 %{SOURCE3}     %{buildroot}%{_sysconfdir}/munin/plugin-conf.d/unbound
install -d 0755                   %{buildroot}%{_datadir}/munin/plugins/
install -p -m 0755 %{SOURCE4}     %{buildroot}%{_datadir}/munin/plugins/unbound
for plugin in unbound_munin_hits unbound_munin_queue unbound_munin_memory unbound_munin_by_type unbound_munin_by_class unbound_munin_by_opcode unbound_munin_by_rcode unbound_munin_by_flags unbound_munin_histogram; do
    ln -s unbound %{buildroot}%{_datadir}/munin/plugins/$plugin
done
%endif

# install streamtcp used for monitoring / debugging unbound's port 80/443 modes
install -m 0755 streamtcp %{buildroot}%{_sbindir}/unbound-streamtcp
# install streamtcp man page
install -m 0644 testcode/streamtcp.1 %{buildroot}/%{_mandir}/man1/unbound-streamtcp.1

# Install tmpfiles.d config
install -d -m 0755         %{buildroot}%{_tmpfilesdir}/ \
                           %{buildroot}%{_sharedstatedir}/unbound
install -m 0644 %{SOURCE8} %{buildroot}%{_tmpfilesdir}/unbound.conf

# install root and DLV key - we keep a copy of the root key in old location,
# in case user has changed the configuration and we wouldn't update it there
install -m 0644 %{SOURCE5} %{SOURCE6} %{buildroot}%{_sysconfdir}/unbound/
install -m 0644 %{SOURCE13}           %{buildroot}%{_sharedstatedir}/unbound/root.key

# create softlink for all functions of libunbound man pages
for mpage in ub_ctx ub_result ub_ctx_create ub_ctx_delete ub_ctx_set_option ub_ctx_get_option ub_ctx_config ub_ctx_set_fwd ub_ctx_resolvconf ub_ctx_hosts ub_ctx_add_ta ub_ctx_add_ta_file ub_ctx_trustedkeys ub_ctx_debugout ub_ctx_debuglevel ub_ctx_async ub_poll ub_wait ub_fd ub_process ub_resolve ub_resolve_async ub_cancel ub_resolve_free ub_strerror ub_ctx_print_local_zones ub_ctx_zone_add ub_ctx_zone_remove ub_ctx_data_add ub_ctx_data_remove;
do
  echo ".so man3/libunbound.3" > %{buildroot}%{_mandir}/man3/${mpage}.3 ;
done

mkdir -p %{buildroot}%{piddir}/%{name}

# Install directories for easier config file drop in

mkdir -p %{buildroot}%{_sysconfdir}/unbound/{keys.d,conf.d,local.d}
install -m 0640 -p %{SOURCE9} %{buildroot}%{_sysconfdir}/unbound/keys.d/
install -m 0640 -p %{SOURCE10} %{buildroot}%{_sysconfdir}/unbound/conf.d/
install -m 0640 -p %{SOURCE11} %{buildroot}%{_sysconfdir}/unbound/local.d/

# Link unbound-control-setup.8 manpage to unbound-control.8
echo ".so man8/unbound-control.8" > %{buildroot}/%{_mandir}/man8/unbound-control-setup.8

%check
# it currently fails in the ldns unit test. which is weird as both come from the same project
make check ||:

%pre anchor
%if %{with systemd}
%service_add_pre  unbound-anchor.service unbound-anchor.timer
%endif
getent group unbound >/dev/null || groupadd -r unbound
getent passwd unbound >/dev/null || \
	useradd -g unbound -s /bin/false -r -c "unbound caching DNS server" \
	-d /var/lib/unbound unbound

%if %{with systemd}
%pre
%service_add_pre    unbound-keygen.service unbound.service
%endif

%if %{with systemd}
%post anchor
%service_add_post   unbound-anchor.service unbound-anchor.timer
%endif

%post
%fillup_only %{name}
%if %{with systemd}
systemd-tmpfiles --create  %{_tmpfilesdir}/unbound.conf  || :
%service_add_post   unbound-keygen.service unbound.service
%endif

%if %{with systemd}
%preun anchor
%service_del_preun  unbound-anchor.service unbound-anchor.timer
%endif

%preun
%if %{with systemd}
%service_del_preun  unbound-keygen.service unbound.service
%else
%stop_on_removal %{name}
%endif

%postun anchor
%if %{with systemd}
%service_del_postun unbound-anchor.service unbound-anchor.timer
%endif

%postun
%if %{with systemd}
%service_del_postun unbound-keygen.service unbound.service
%else
%restart_on_update %{name}
%{insserv_cleanup}
%endif

%post   -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc doc/README doc/CREDITS doc/LICENSE doc/FEATURES
%attr(0755,unbound,unbound) %ghost %dir %{piddir}/%{name}
%attr(0640,root,unbound)    %config(noreplace) %{_sysconfdir}/%{name}/unbound.conf
%dir %attr(-,root,unbound)                     %{_sysconfdir}/%{name}/keys.d
%attr(0660,root,unbound)    %config(noreplace) %{_sysconfdir}/%{name}/keys.d/*.key
%dir %attr(-,root,unbound)                     %{_sysconfdir}/%{name}/conf.d
%attr(0660,root,unbound)    %config(noreplace) %{_sysconfdir}/%{name}/conf.d/*.conf
%dir %attr(-,root,unbound)                     %{_sysconfdir}/%{name}/local.d
%attr(0660,root,unbound)    %config(noreplace) %{_sysconfdir}/%{name}/local.d/*.conf
%{_sbindir}/unbound
%{_sbindir}/unbound-checkconf
%{_sbindir}/unbound-host
%{_sbindir}/unbound-control
%{_sbindir}/unbound-control-setup
%{_sbindir}/unbound-streamtcp
%{_mandir}/man1/unbound-host.1*
%{_mandir}/man5/unbound.conf.5*
%{_mandir}/man8/unbound.8*
%{_mandir}/man8/unbound-checkconf.8*
%{_mandir}/man8/unbound-control-setup.8*
%{_mandir}/man8/unbound-control.8*
%{_mandir}/man1/unbound-streamtcp.1*
%{_fillupdir}/sysconfig.%{name}
%if %{with systemd}
%{_tmpfilesdir}/unbound.conf
%{_unitdir}/unbound-keygen.service
%{_unitdir}/unbound.service
%endif
%{_sbindir}/rcunbound
%{_sbindir}/rcunbound-keygen

%files -n %{libname}
%defattr(-,root,root,-)
%{_libdir}/libunbound.so.*

%if %{with python3}
%files -n python3-unbound
%defattr(-,root,root,-)
%{python3_sitearch}/*
%doc libunbound/python/examples/*
%doc pythonmod/examples/*
%endif

%if %{with python2}
%files -n python2-unbound
%defattr(-,root,root,-)
%{python2_sitearch}/*
%doc ../p2/libunbound/python/examples/*
%doc ../p2/pythonmod/examples/*
%endif

%if %{with munin}
%files munin
%defattr(-,root,root,-)
%dir               %{_sysconfdir}/munin/
%dir               %{_sysconfdir}/munin/plugin-conf.d/
%config(noreplace) %{_sysconfdir}/munin/plugin-conf.d/unbound
%dir %{_datadir}/munin/
%dir %{_datadir}/munin/plugins/
     %{_datadir}/munin/plugins/unbound*
%doc unbound-munin.README
%endif

%files devel
%defattr(-,root,root,-)
%{_includedir}/unbound.h
%{_includedir}/unbound-event.h
%{_libdir}/libunbound.so
%exclude %{_libdir}/libunbound.la
%{_libdir}/pkgconfig/libunbound.pc
%{_mandir}/man3/libunbound.3*
%{_mandir}/man3/ub_*.3*

%files anchor
%defattr(-,root,root,-)
%dir %{_sysconfdir}/%{name}/
%{_sbindir}/unbound-anchor
%config %{_sysconfdir}/%{name}/icannbundle.pem
%{_unitdir}/unbound-anchor.timer
%{_unitdir}/unbound-anchor.service
%dir %attr(-,unbound,unbound) %{_sharedstatedir}/%{name}
%attr(0644,unbound,unbound) %config(noreplace) %{_sharedstatedir}/%{name}/root.key
%attr(0644,root,unbound)    %config(noreplace) %{_sysconfdir}/%{name}/dlv.isc.org.key
# just left for backwards compat with user changed unbound.conf files - format is different!
%attr(0644,root,unbound)    %config(noreplace) %{_sysconfdir}/%{name}/root.key
%{_mandir}/man8/unbound-anchor.8*
%doc doc/README doc/LICENSE

%changelog
