#
# spec file for package squid
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


%define         squidlibexecdir %{_libexecdir}/squid
%define         squidconfdir %{_sysconfdir}/squid

%if 0%{?suse_version} > 1500 || 0%{?sle_version} >= 150300
%define         squidhelperdir %{squidlibexecdir}
%else
%define         squidhelperdir %{_sbindir}
%endif

Name:           squid
Version:        4.14
Release:        0
Summary:        Caching and forwarding HTTP web proxy
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Web/Proxy
URL:            http://www.squid-cache.org
Source0:        http://www.squid-cache.org/Versions/v4/squid-%{version}.tar.xz
Source1:        http://www.squid-cache.org/Versions/v4/squid-%{version}.tar.xz.asc
Source5:        pam.squid
Source6:        unsquid.pl
Source7:        %{name}.logrotate
Source9:        %{name}.permissions
Source10:       README.kerberos
Source11:       %{name}.service
Source12:       %{name}-user.conf
# http://lists.squid-cache.org/pipermail/squid-announce/2016-October/000064.html
Source13:       http://www.squid-cache.org/pgp.asc#/squid.keyring
Source15:       cache_dir.sed
Source16:       initialize_cache_if_needed.sh
Source17:       tmpfilesdir.squid.conf
Patch1:         missing_installs.patch
Patch2:         old_nettle_compat.patch
BuildRequires:  cppunit-devel
BuildRequires:  db-devel
BuildRequires:  ed
BuildRequires:  expat
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libcap-devel
BuildRequires:  libtool
BuildRequires:  openldap2-devel
BuildRequires:  opensp-devel
BuildRequires:  openssl-devel
BuildRequires:  pam-devel
BuildRequires:  pkgconfig
BuildRequires:  samba-winbind
BuildRequires:  sharutils
%if 0%{?suse_version} >= 1500
BuildRequires:  sysuser-shadow
BuildRequires:  sysuser-tools
%sysusers_requires
%else
Requires(pre):  shadow
%endif
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(gssrpc)
BuildRequires:  pkgconfig(kdb)
BuildRequires:  pkgconfig(krb5)
BuildRequires:  pkgconfig(libsasl2)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(nettle)
Requires(pre):  permissions
Recommends:     logrotate
Provides:       http_proxy
# due to package rename
# Wed Aug 15 17:40:30 UTC 2012
Provides:       %{name}3 = %{version}
Obsoletes:      %{name}3 < %{version}
%{?systemd_ordering}
%if 0%{?suse_version} >= 1330
BuildRequires:  libnsl-devel
%endif

%description
Squid is a caching proxy for the Web supporting HTTP(S), FTP, and
some others. It reduces bandwidth and improves response times by
caching and reusing frequently-requested web pages. Squid has
extensive access controls and can also be used as a server
accelerator.

%prep
%setup -q
cp %{SOURCE10} .

# upstream patches after RELEASE
perl -p -i -e 's|%{_prefix}/local/bin/perl|%{_bindir}/perl|' `find -name "*.pl"`
%patch1 -p1
%if 0%{?suse_version} < 1500
%patch2 -p1
%endif

%build
%define _lto_cflags %{nil}
autoreconf -fi
cd libltdl; autoreconf -fi; cd ..
export CFLAGS="%{optflags} -fPIE -fPIC -DOPENSSL_LOAD_CONF"
export CXXFLAGS="%{optflags} -fPIE -fPIC -DOPENSSL_LOAD_CONF"
export LDFLAGS="-Wl,--as-needed -Wl,--no-undefined -Wl,-z,relro,-z,now -pie"
%configure \
	--disable-strict-error-checking \
	--sysconfdir=%{squidconfdir} \
	--libexecdir=%{squidhelperdir} \
	--datadir=%{_datadir}/squid \
	--sharedstatedir=%{_localstatedir}/squid \
	--with-logdir=%{_localstatedir}/log/squid \
	--with-pidfile=/run/squid.pid \
	--with-dl \
	--enable-disk-io \
	--enable-storeio \
	--enable-removal-policies=heap,lru \
	--enable-icmp \
	--enable-delay-pools \
	--enable-esi \
	--enable-icap-client \
	--enable-useragent-log \
	--enable-referer-log \
	--enable-kill-parent-hack \
	--enable-arp-acl \
	--enable-ssl-crtd \
	--with-openssl \
	--enable-forw-via-db \
	--enable-cache-digests \
	--enable-linux-netfilter \
	--with-large-files \
	--enable-underscores \
	--enable-auth \
	--enable-auth-basic="SMB_LM,DB,fake,getpwnam,LDAP,NCSA,NIS,PAM,POP3,RADIUS,SASL,SMB" \
	--enable-auth-ntlm="SMB_LM,fake" \
	--enable-auth-negotiate \
	--enable-auth-digest \
	--enable-external-acl-helpers=LDAP_group,eDirectory_userip,file_userip,kerberos_ldap_group,session,unix_group,wbinfo_group,time_quota \
	--enable-stacktraces \
	--enable-x-accelerator-vary \
	--with-default-user=%{name} \
	--disable-ident-lookups \
	--enable-follow-x-forwarded-for \
	--disable-arch-native \
	--enable-security-cert-generators \
	--enable-security-cert-validators
make %{?_smp_mflags} -O SAMBAPREFIX=%{_prefix}
%if 0%{?suse_version} >= 1500
%sysusers_generate_pre %{SOURCE12} squid
%endif

%install
install -d -m 750 %{buildroot}%{_localstatedir}/{cache,log}/%{name}
install -d %{buildroot}%{_sbindir}

# make_install
%make_install SAMBAPREFIX=%{_prefix}

mv %{buildroot}{%{_sysconfdir}/%{name}/,%{_datadir}/%{name}/}mime.conf.default
ln -s %{_sysconfdir}/%{name}/mime.conf %{buildroot}%{_datadir}/%{name} # backward compatible

# install logrotate file
install -Dpm 644 %{SOURCE7} \
  %{buildroot}%{_sysconfdir}/logrotate.d/%{name}

install -d -m 755 doc/scripts
install scripts/*.pl doc/scripts
cat > doc/scripts/cachemgr.readme <<-EOT
%if 0%{?suse_version} > 1500 || 0%{?sle_version} >= 150300
	cachemgr.cgi will now be found in %{squidhelperdir}
%else
	cachemgr.cgi will now be found in %{_libdir}/%{name}
%endif
EOT

%if 0%{?suse_version} <= 1500 && 0%{?sle_version} < 150300
install -dpm 755 %{buildroot}/%{_libdir}/%{name}
mv %{buildroot}%{_sbindir}/cachemgr.cgi %{buildroot}/%{_libdir}/%{name}
%endif

install -dpm 755 doc/contrib
install %{SOURCE6} doc/contrib
install -Dpm 644 %{SOURCE5} %{buildroot}%{_sysconfdir}/pam.d/%{name}

rm -rf %{buildroot}%{squidconfdir}/errors
for i in errors/*; do
  if [ -d $i ]; then
    mkdir -p %{buildroot}%{_datadir}/%{name}/$i
    install -m 644 $i/* %{buildroot}%{_datadir}/%{name}/$i
  fi
done
ln -sf %{_datadir}/%{name}/errors/en %{buildroot}%{squidconfdir}/errors

# fix file duplicates
%fdupes -s %{buildroot}%{_prefix}

# systemd
install -D -m 644 %{SOURCE11} %{buildroot}%{_unitdir}/%{name}.service
install -D -m 755 %{SOURCE15} %{buildroot}%{squidlibexecdir}/cache_dir.sed
install -D -m 755 %{SOURCE16} %{buildroot}%{squidlibexecdir}/initialize_cache_if_needed.sh
sed -i -e 's!%%{_libexecdir}!%{_libexecdir}!' %{buildroot}%{_unitdir}/%{name}.service
ln -sf %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}

# needed for smp support (bsc#1112695, bsc#1112066)
mkdir -p %{buildroot}%{_tmpfilesdir}
install -D -m 644 %{SOURCE17} %{buildroot}%{_tmpfilesdir}/squid.conf

# Move the MIB definition to the proper place (and name)
mkdir -p %{buildroot}%{_datadir}/snmp/mibs
mv %{buildroot}%{_datadir}/squid/mib.txt \
  %{buildroot}%{_datadir}/snmp/mibs/SQUID-MIB.txt

# Install sysusers file.
mkdir -p %{buildroot}%{_sysusersdir}
install -m 644 %{SOURCE12} %{buildroot}%{_sysusersdir}/

%check
# Fails in chroot environment
make check

%if 0%{?suse_version} >= 1500
%pre -f squid.pre
%else
%pre
# we need this group for /usr/sbin/pinger
getent group %{name} >/dev/null || %{_sbindir}/groupadd -g 31 -r %{name}
# we need this group for squid (ntlmauth)
# read access to /var/lib/samba/winbindd_privileged
getent group winbind >/dev/null || %{_sbindir}/groupadd -r winbind
getent passwd squid >/dev/null || \
  %{_sbindir}/useradd -c "WWW-proxy squid" -d %{_localstatedir}/cache/%{name} \
    -G winbind -g %{name} -o -u 31 -r -s /bin/false \
    %{name}
# if default group is not squid, change it
if [ "$(%{_bindir}/id -ng %{name} 2>/dev/null)" != "%{name}" ]; then
  %{_sbindir}/usermod -g %{name} %{name}
fi
# if squid is not member of winbind, add him
if [ $(%{_bindir}/id -nG %{name} 2>/dev/null | grep -q winbind; echo $?) -ne 0 ]; then
  %{_sbindir}/usermod -G winbind %{name}
fi
%endif
%service_add_pre %{name}.service

# update mode?
if [ "$1" -gt "1" ]; then
  if [ -e %{_sysconfdir}/%{name}.conf -a ! -L %{_sysconfdir}/%{name}.conf -a ! -e %{_sysconfdir}/%{name}/%{name}.conf ]; then
    echo "moving %{_sysconfdir}/%{name}.conf to %{_sysconfdir}/%{name}/%{name}.conf"
    mv %{_sysconfdir}/%{name}.conf %{_sysconfdir}/%{name}/%{name}.conf
  fi
fi

%post
%set_permissions %{squidhelperdir}/pinger
%set_permissions %{_localstatedir}/cache/squid/
%set_permissions %{_localstatedir}/log/squid/
%set_permissions %{squidhelperdir}/basic_pam_auth
%tmpfiles_create %{_tmpfilesdir}/squid.conf
%service_add_post squid.service

%preun
%service_del_preun squid.service

%verifyscript
%verify_permissions -e %{squidhelperdir}/pinger
%verify_permissions -e %{_localstatedir}/cache/squid/
%verify_permissions -e %{_localstatedir}/log/squid/
%verify_permissions -e %{squidhelperdir}/basic_pam_auth

%postun
%service_del_postun squid.service

%files
%ghost %dir %{_rundir}/%{name}
%license COPYING
%doc ChangeLog CONTRIBUTORS CREDITS
%doc QUICKSTART README RELEASENOTES.html SPONSORS*
%doc README.kerberos
%doc doc/contrib doc/scripts
%doc doc/debug-sections.txt src/%{name}.conf.default
%{_mandir}/man?/*
%{_unitdir}/%{name}.service
%{squidlibexecdir}/initialize_cache_if_needed.sh
%{squidlibexecdir}/cache_dir.sed
%verify(not user group mode) %attr(750,%{name},root) %dir %{_localstatedir}/cache/%{name}/
%verify(not user group mode) %attr(750,%{name},root) %dir %{_localstatedir}/log/%{name}/
%dir %{squidconfdir}
%dir %{_tmpfilesdir}
%dir %{_libexecdir}/%{name}
%{_tmpfilesdir}/squid.conf
%{_sysusersdir}/squid-user.conf
%config(noreplace) %{squidconfdir}/cachemgr.conf
%config(noreplace) %{squidconfdir}/errorpage.css
%config(noreplace) %{squidconfdir}/errors
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%config(noreplace) %{squidconfdir}/mime.conf
%config(noreplace) %{squidconfdir}/%{name}.conf
%config %{squidconfdir}/cachemgr.conf.default
%config %{squidconfdir}/errorpage.css.default
%config %{squidconfdir}/%{name}.conf.default
%config %{squidconfdir}/%{name}.conf.documented
%config %{_sysconfdir}/pam.d/%{name}
%dir %{_datadir}/%{name}
%dir %{_datadir}/snmp
%dir %{_datadir}/snmp/mibs
%{_datadir}/%{name}/errors
%{_datadir}/%{name}/icons
%{_datadir}/%{name}/mime.conf
%{_datadir}/%{name}/mime.conf.default
%{_datadir}/snmp/mibs/SQUID-MIB.txt
%{_bindir}/purge
%{_bindir}/squidclient
%{squidhelperdir}/basic_db_auth
%{squidhelperdir}/basic_fake_auth
%{squidhelperdir}/basic_getpwnam_auth
%{squidhelperdir}/basic_ldap_auth
%{squidhelperdir}/digest_edirectory_auth
%{squidhelperdir}/basic_ncsa_auth
%{squidhelperdir}/basic_nis_auth
%{squidhelperdir}/basic_pam_auth
%{squidhelperdir}/basic_pop3_auth
%{squidhelperdir}/basic_radius_auth
%{squidhelperdir}/basic_sasl_auth
%{squidhelperdir}/basic_smb_auth
%{squidhelperdir}/basic_smb_auth.sh
%{squidhelperdir}/basic_smb_lm_auth
%{squidhelperdir}/cert_tool
%{squidhelperdir}/digest_file_auth
%{squidhelperdir}/digest_ldap_auth
%{squidhelperdir}/diskd
%{squidhelperdir}/ext_edirectory_userip_acl
%{squidhelperdir}/ext_file_userip_acl
%{squidhelperdir}/ext_kerberos_ldap_group_acl
%{squidhelperdir}/ext_ldap_group_acl
%{squidhelperdir}/ext_session_acl
%{squidhelperdir}/ext_unix_group_acl
%{squidhelperdir}/ext_wbinfo_group_acl
%{squidhelperdir}/helper-mux
%{squidhelperdir}/log_db_daemon
%{squidhelperdir}/log_file_daemon
%{squidhelperdir}/negotiate_kerberos_auth
%{squidhelperdir}/negotiate_kerberos_auth_test
%{squidhelperdir}/negotiate_wrapper_auth
%{squidhelperdir}/ntlm_fake_auth
%{squidhelperdir}/ntlm_smb_lm_auth
%{squidhelperdir}/pinger
%{squidhelperdir}/security_fake_certverify
%{squidhelperdir}/security_file_certgen
%{squidhelperdir}/storeid_file_rewrite
%{squidhelperdir}/unlinkd
%{squidhelperdir}/url_fake_rewrite
%{squidhelperdir}/url_fake_rewrite.sh
%{squidhelperdir}/url_lfs_rewrite
%{squidhelperdir}/ext_time_quota_acl
%{_sbindir}/squid
%{_sbindir}/rcsquid
%if 0%{?suse_version} > 1500 || 0%{?sle_version} >= 150300
%dir %{squidhelperdir}
%{squidhelperdir}/cachemgr.cgi
%else
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/cachemgr.cgi
%endif

%changelog
