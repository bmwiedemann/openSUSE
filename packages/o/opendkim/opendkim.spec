#
# spec file for package opendkim
#
# Copyright (c) 2021 SUSE LLC
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


%define full_version 2.11.0-Beta2
%define upname OpenDKIM
%define ver_odkim    2.11.0
%define ver_mt       1.6.0
%define sover_odkim  11
%define sover_rbl    1
%define sover_repute 1
%define sover_ut     1
%define sover_rrd    1
%define sover_vbr    2

%bcond_with     opendkim_sql
# RRD is off for now as it pulls too many dependencies when installing
%bcond_with     opendkim_rrd
%bcond_without  opendkim_libmemcached
%bcond_without  opendkim_reputation
%bcond_without  systemd

Name:           opendkim
Version:        %{ver_odkim}
Release:        0
Summary:        Milter based implementation of DKIM
License:        BSD-3-Clause AND Sendmail
Group:          Productivity/Networking/Email/Servers
URL:            http://www.opendkim.org/
Source0:        https://github.com/trusteddomainproject/OpenDKIM/archive/%{full_version}.tar.gz
Source2:        %{name}.keyring
Source3:        opendkim.service
Source4:        opendkim.tmpfiles.d
Source5:        opendkim.init
# PATCH-FIX-UPSTREAM opendkim-2.9.2_compiler_warnings.patch -- fix compiler warnings
Patch0:         opendkim-2.9.2_compiler_warnings.patch
# PATCH-FIX-OPENSUSE set default values in installed configuration file
Patch1:         %{name}-default_config.patch
# PATCH-FIX-UPSTREAM cve-2020-12272.patch -- LIBOPENDKIM: Confirm that the value of "d=" is properly formed.
Patch2:         cve-2020-12272.patch
# PATCH-FIX-UPSTREAM unbound-fix.patch -- Plug memory leak in Unbound callback function https://github.com/trusteddomainproject/OpenDKIM/pull/57/commits/0010ca7150b09c3c259c17bdd9431a8bfe39e299
Patch3:         unbound-fix.patch
Patch4:         harden_opendkim.service.patch
# PATCH-FIX-UPSTREAM fix-RSA_sign-call.patch -- Fix RSA sign call on big endian systems ref: https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1012506
Patch5:         fix-RSA_sign-call.patch
# PATCH-FIX-UPSTREAM rev-ares-deletion.patch.patch -- https://github.com/trusteddomainproject/OpenDKIM/pull/189
Patch6:         rev-ares-deletion.patch
# PATCH-FIX-UPSTREAM ares-missing-space.patch -- https://github.com/trusteddomainproject/OpenDKIM/pull/67
Patch7:         ares-missing-space.patch
# PATCH-FIX-UPSTREAM ftbfs-gcc-14-1075339.patch -- ref: https://bugs.debian.org/1075339
Patch8:         ftbfs-gcc-14-1075339.patch
# PATCH-FIX-UPSTREAM opendkim-2.10.3-incompatible-pointer-types.patch -- ref: https://bugs.gentoo.org/919366
Patch9:         opendkim-2.10.3-incompatible-pointer-types.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  curl-devel
BuildRequires:  cyrus-sasl-devel
BuildRequires:  db-devel
BuildRequires:  libbsd-devel
BuildRequires:  libevent-devel
BuildRequires:  libtool
BuildRequires:  lua51-devel
BuildRequires:  openldap2-devel
BuildRequires:  pkgconfig
BuildRequires:  postgresql-devel
BuildRequires:  sendmail-devel
BuildRequires:  tre-devel
BuildRequires:  unbound-devel
Requires(pre):  %{_sbindir}/groupadd
Requires(pre):  %{_sbindir}/useradd
Requires:       /usr/bin/openssl
BuildRequires:  libopenssl-devel
%if %{with opendkim_reputation}
BuildRequires:  libjansson-devel
%endif
%if %{with opendkim_libmemcached}
BuildRequires:  libmemcached-devel
%endif
%if %{with opendkim_sql}
BuildRequires:  opendbx-devel >= 1.3.7
%endif
%if %{with opendkim_rrd}
BuildRequires:  rrdtool-devel
%endif
%if %{with systemd}
BuildRequires:  pkgconfig(systemd)
%{?systemd_ordering}
%else
# FIXME: use proper Requires(pre/post/preun/...)
PreReq:         %fillup_prereq
PreReq:         %insserv_prereq
%endif
Provides:       group(%{name})
Provides:       user(%{name})

%description
DomainKeys Identified Mail (DKIM) lets an organization take responsibility for
a message that is in transit.  The organization is a handler of the message,
either as its originator or as an intermediary. Their reputation is the basis
for evaluating whether to trust the message for further handling, such as
delivery. Technically DKIM provides a method for validating a domain name
identity that is associated with a message through cryptographic
authentication.

%package -n autobuild
Summary:        Multiple configuration build tool
License:        BSD-3-Clause
Group:          Development/Tools/Building

%description -n autobuild
Configures, builds and tests a source code package whose configuration is
provided by GNU's autoconf mechanism.

%package -n miltertest
Version:        %{ver_mt}
Release:        0
Summary:        Milter unit test utility
License:        BSD-3-Clause
Group:          Productivity/Networking/Diagnostic

%description -n miltertest
Simulates the MTA side of an MTA-milter interaction for testing a milter-aware
filter application.  It takes as input a script using the Lua language,
and by exporting some utility functions, makes it possible for users to
write scripts that exercise a filter.

%package -n libopendkim%{sover_odkim}
Summary:        Library for performing DKIM signing and verification
License:        BSD-3-Clause AND Sendmail
Group:          System/Libraries

%description -n libopendkim%{sover_odkim}
This package provides the shared library libopendkim which
performs DKIM signing and verification.

%package -n librbl%{sover_rbl}
Summary:        Realtime Blacklist (RBL) service library
License:        BSD-3-Clause
Group:          System/Libraries

%description -n librbl%{sover_rbl}
This package provides librbl which is an interface
to a facility to conduct Realtime Blacklist (RBL)
queries and return their results.  RBLs are described in RFC5782.

%package -n librepute%{sover_repute}
Summary:        Library for performing REPUTE queries for spammy domains
License:        BSD-3-Clause
Group:          System/Libraries

%description -n librepute%{sover_repute}
This package provides the shared library librepute which
performs REPUTE queries for spammy domains.



# Maybe change name (there is already an other libut...)

%package -n libut%{sover_ut}
Summary:        Library for assisting in URI construction from templates
License:        BSD-3-Clause
Group:          System/Libraries

%description -n libut%{sover_ut}
This package provides the shared library libut from opendkim which
assists in URI construction from templates.

%package -n libvbr%{sover_vbr}
Summary:        Library for assisting in Vouch By Refence functions
License:        BSD-3-Clause AND Sendmail
Group:          System/Libraries

%description -n libvbr%{sover_vbr}
This package provides the shared library libvbr which
assists in Vouch By Refence functions.

%package -n  libreprrd%{sover_rrd}
Summary:        Library for performing reputation queries for spammy domains using RRD tables
License:        BSD-3-Clause
Group:          System/Libraries

%description -n libreprrd%{sover_rrd}
This package provides the shared library libreprrd which
performs reputation queries for spammy domains using RRD tables.

%package devel
Summary:        Development files to develop with opendkim
License:        BSD-3-Clause AND Sendmail
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{ver_odkim}
Requires:       libopendkim%{sover_odkim} = %{ver_odkim}
Requires:       librbl%{sover_rbl} = %{ver_odkim}
Requires:       librepute%{sover_repute} = %{ver_odkim}
Requires:       libut%{sover_ut} = %{ver_odkim}
Requires:       libvbr%{sover_vbr} = %{ver_odkim}
%if %{with opendkim_rrd}
Requires:       libreprrd%{sover_rrd} = %{ver_odkim}
%endif

%description devel
DomainKeys Identified Mail (DKIM) lets an organization take responsibility for
a message that is in transit.  The organization is a handler of the message,
either as its originator or as an intermediary. Their reputation is the basis
for evaluating whether to trust the message for further handling, such as
delivery. Technically DKIM provides a method for validating a domain name
identity that is associated with a message through cryptographic
authentication.

This package holds the development files.

%prep
%setup -q -n %{upname}-%{full_version}
%patch -P 0 -p1
%patch -P 1
%patch -P 2 -p1
%patch -P 3 -p0
%patch -P 4 -p1
%patch -P 5 -p1
%patch -P 6 -p1
%patch -P 7 -p1
%patch -P 8 -p1
%patch -P 9 -p1

%build
autoreconf -iv
%configure                            \
  --includedir=%{_includedir}/%{name} \
  --disable-static                    \
  --disable-silent-rules              \
  --disable-live-testing              \
  --enable-atps                       \
  --enable-db_handle_pools            \
  --enable-diffheaders                \
  --enable-identity_header            \
  --enable-ldap_caching               \
  --enable-postgresql_reconnect_hack  \
  --enable-rate_limit                 \
  --enable-replace_rules              \
  %if %{with opendkim_rrd}
  --enable-reprrd                     \
  %else
  --disable-reprrd                    \
  %endif
  --enable-reputation                 \
  --enable-resign                     \
  --enable-sender_macro               \
  --enable-socketdb                   \
  --enable-stats                      \
  --enable-statsext                   \
  --enable-rbl                        \
  --enable-vbr                        \
  --enable-default_sender             \
  --enable-query_cache                \
  %if %{with opendkim_libmemcached}
  --with-libmemcached                 \
  %endif
  --with-tre                          \
  --with-lua                          \
  %if %{with opendkim_sql}
  --with-sql-backend=postgresql       \
  --with-odbx                         \
  %endif
  --with-openldap                     \
  --with-sasl                         \
%if 0
  --with-erlang                       \
%endif
  --with-unbound                      \
  --with-domain="example.com"

make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
# install the init script
%if %{with systemd}
install -D -m 0644 %{SOURCE3} %{buildroot}%{_unitdir}/%{name}.service
install -D -m 0644 %{SOURCE4} %{buildroot}%{_tmpfilesdir}/%{name}.conf
ln -s -f %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}
%else
install -D -m 0755 %{SOURCE5} %{buildroot}%{_sysconfdir}/%{name}/init.d/%{name}
ln -s -f %{_sysconfdir}/%{name}/init.d/%{name} %{buildroot}%{_sbindir}/rc%{name}
%endif
mkdir -p %{buildroot}%{_localstatedir}/lib/%{name}
install -D -m 0640 opendkim/opendkim.conf.sample %{buildroot}%{_sysconfdir}/%{name}/opendkim.conf
install -d -m 0750 %{buildroot}%{_sysconfdir}/%{name}/keys
# Fix doc (move to correct location and fix for splitted packages)
mkdir -p %{buildroot}%{_docdir}/autobuild
mv %{buildroot}%{_datadir}/doc/%{name}/autobuild.conf.sample %{buildroot}%{_docdir}/autobuild
%if "%{_datadir}/doc" != "%{_docdir}"
mv %{buildroot}%{_datadir}/doc/%{name} %{buildroot}%{_docdir}/%{name}
%endif
# Fix for libut
mkdir -p %{buildroot}%{_libdir}/%{name}-%{ver_odkim}
mv %{buildroot}%{_libdir}/libut.so* %{buildroot}%{_libdir}/%{name}-%{ver_odkim}
mkdir -p %{buildroot}%{_sysconfdir}/ld.so.conf.d/
echo "%{_libdir}/%{name}-%{ver_odkim}" > %{buildroot}%{_sysconfdir}/ld.so.conf.d/%{name}-%{ver_odkim}.conf

%pre
getent group  %{name} >/dev/null || \
	%{_sbindir}/groupadd -r %{name}
getent passwd %{name} >/dev/null || \
	%{_sbindir}/useradd -r -g %{name} -G unbound -d %{_localstatedir}/lib/%{name} -s /sbin/nologin -c "User for opendkim" %{name}
%if %{with systemd}
%service_add_pre %{name}.service
%endif

%preun
%if %{with systemd}
%service_del_preun %{name}.service
%else
%stop_on_removal %{name}
%endif

%post
# enable opendkim to read TrustAnchorFile
%{_sbindir}/usermod -a -G unbound %{name}
# enable postfix to write to opendkim.sock
getent passwd postfix && \
    %{_sbindir}/usermod -a -G %{name} postfix
%if %{with systemd}
systemd-tmpfiles --create %{_tmpfilesdir}/%{name}.conf || true
%service_add_post %{name}.service
%endif

%postun
%if %{with systemd}
%service_del_postun %{name}.service
%else
%restart_on_update %{name}
%insserv_cleanup
%endif

%post -n libut%{sover_ut} -p /sbin/ldconfig
%post -n libopendkim%{sover_odkim} -p /sbin/ldconfig
%post -n librbl%{sover_rbl} -p /sbin/ldconfig
%post -n librepute%{sover_repute} -p /sbin/ldconfig
%post -n libvbr%{sover_vbr} -p /sbin/ldconfig
%postun -n libut%{sover_ut} -p /sbin/ldconfig
%postun -n libopendkim%{sover_odkim} -p /sbin/ldconfig
%postun -n librbl%{sover_rbl} -p /sbin/ldconfig
%postun -n librepute%{sover_repute} -p /sbin/ldconfig
%postun -n libvbr%{sover_vbr} -p /sbin/ldconfig
%post -n libreprrd%{sover_rrd} -p /sbin/ldconfig
%postun -n libreprrd%{sover_rrd} -p /sbin/ldconfig

%files -n autobuild
%license LICENSE
%doc %{_docdir}/autobuild
%{_bindir}/autobuild
%{_mandir}/man8/autobuild.8%{?ext_man}

%files -n miltertest
%license LICENSE
%{_bindir}/miltertest
%{_mandir}/man8/miltertest.8%{?ext_man}

%files -n libopendkim%{sover_odkim}
%{_libdir}/libopendkim.so.*

%files -n librbl%{sover_rbl}
%{_libdir}/librbl.so.*

%files -n librepute%{sover_repute}
%{_libdir}/librepute.so.*

%files -n libut%{sover_ut}
%dir %{_libdir}/%{name}-%{ver_odkim}
%{_libdir}/%{name}-%{ver_odkim}/libut.so.*
%config %{_sysconfdir}/ld.so.conf.d/%{name}-%{ver_odkim}.conf

%files -n libvbr%{sover_vbr}
%{_libdir}/libvbr.so.*

%if %{with opendkim_rrd}
%files -n libreprrd%{sover_rrd}
%{_libdir}/libreprrd.so.*
%endif

%files
%doc %{_docdir}/%{name}
#
%config(noreplace) %attr(-,root,%{name}) %{_sysconfdir}/%{name}
%dir %attr(750,%{name},%{name}) %{_sysconfdir}/%{name}/keys
%{_sbindir}/rc%{name}
%if %{with systemd}
%{_unitdir}/%{name}.service
%{_tmpfilesdir}/%{name}.conf
%ghost /run/opendkim
%else
%{_sysconfdir}/%{name}/init.d/%{name}
%endif
%dir %attr(750,%{name},%{name}) %{_localstatedir}/lib/%{name}
#
%{_sbindir}/opendkim
%{_sbindir}/opendkim-atpszone
%{_sbindir}/opendkim-expire
%{_sbindir}/opendkim-gengraphs
%{_sbindir}/opendkim-genkey
%{_sbindir}/opendkim-genrates
%{_sbindir}/opendkim-genstats
%{_sbindir}/opendkim-genzone
%{_sbindir}/opendkim-modtotals
%{_sbindir}/opendkim-rephistory
%{_sbindir}/opendkim-reportstats
%{_sbindir}/opendkim-stats
%{_sbindir}/opendkim-testkey
%{_sbindir}/opendkim-testmsg
%{_mandir}/man3/opendkim-lua.3%{?ext_man}
%{_mandir}/man5/opendkim.conf.5%{?ext_man}
%{_mandir}/man8/opendkim-atpszone.8%{?ext_man}
%{_mandir}/man8/opendkim-expire.8%{?ext_man}
%{_mandir}/man8/opendkim-gengraphs.8%{?ext_man}
%{_mandir}/man8/opendkim-genkey.8%{?ext_man}
%{_mandir}/man8/opendkim-genrates.8%{?ext_man}
%{_mandir}/man8/opendkim-genstats.8%{?ext_man}
%{_mandir}/man8/opendkim-genzone.8%{?ext_man}
%{_mandir}/man8/opendkim-modtotals.8%{?ext_man}
%{_mandir}/man8/opendkim-rephistory.8%{?ext_man}
%{_mandir}/man8/opendkim-stats.8%{?ext_man}
%{_mandir}/man8/opendkim-testkey.8%{?ext_man}
%{_mandir}/man8/opendkim-testmsg.8%{?ext_man}
%{_mandir}/man8/opendkim.8%{?ext_man}
%if %{with opendkim_rrd}
%{_bindir}/opendkim-reprrdimport
%{_mandir}/man8/opendkim-reprrdimport.8%{?ext_man}
%endif

%files devel
%{_includedir}/opendkim/
%{_libdir}/libopendkim.so
%{_libdir}/librbl.so
%{_libdir}/librepute.so
%{_libdir}/libvbr.so
%{_libdir}/%{name}-%{ver_odkim}/libut.so
%if %{with opendkim_rrd}
%{_libdir}/libreprrd.so
%endif
%{_libdir}/pkgconfig/opendkim.pc
%{_libdir}/pkgconfig/rbl.pc
%{_libdir}/pkgconfig/repute.pc
%{_libdir}/pkgconfig/ut.pc
%{_libdir}/pkgconfig/vbr.pc
%{_mandir}/man3/rbl.3%{?ext_man}
%{_mandir}/man3/ut.3%{?ext_man}
%{_mandir}/man3/vbr.3%{?ext_man}

%changelog
