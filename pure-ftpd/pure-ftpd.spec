#
# spec file for package pure-ftpd
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           pure-ftpd
Version:        1.0.47
Release:        0
Summary:        A Lightweight, Fast, and Secure FTP Server
License:        BSD-3-Clause
Group:          Productivity/Networking/Ftp/Servers
URL:            https://www.pureftpd.org
Source0:        https://download.pureftpd.org/pub/%{name}/releases/%{name}-%{version}.tar.bz2
Source1:        https://download.pureftpd.org/pub/%{name}/releases/%{name}-%{version}.tar.bz2.minisig
Source2:        %{name}.keyring
Source3:        %{name}.init
Source4:        %{name}.pamd
Source5:        %{name}.xinetd
Source8:        %{name}.service
# PATCH-FEATURE-OPENSUSE %{name}-1.0.20_config.patch -- Custom service configs.
Patch0:         %{name}-1.0.20_config.patch
# PATCH-FEATURE-OPENSUSE %{name}-1.0.20_doc.patch -- Adjust command paths on documentation.
Patch1:         %{name}-1.0.20_doc.patch
# PATCH-FEATURE-OPENSUSE %{name}-1.0.20_virtualhosts.patch -- Custom VHOST_PATH on openSUSE.
Patch2:         %{name}-1.0.20_virtualhosts.patch
Patch5:         %{name}-1.0.20_ftpwho_path.patch
# PATCH-FIX-UPSTREAM %{name}-1.0.32-default_tcp_sedrcv_buffer_size.patch
Patch7:         %{name}-1.0.32-default_tcp_sedrcv_buffer_size.patch
# PATCH-FIX-OPENSUSE: bnc#789833
# won't be upstreamed, can be dropped when systemd will be only one init system and kernel get AUDIT_LOGINUID_IMMUTABLE
Patch8:         pure-ftpd-1.0.36-cap-audit-control.patch
Patch9:         pure-ftpd-apparmor.patch
Patch10:        pure-ftpd-malloc-limit.patch
BuildRequires:  libcap-devel
BuildRequires:  mysql-devel
BuildRequires:  openldap2-devel
BuildRequires:  pam-devel
BuildRequires:  postgresql-devel
Requires(pre):  coreutils
Provides:       ftp-server
Provides:       pureftpd = %{version}-%{release}
%if 0%{?suse_version} > 1500
BuildRequires:  postgresql-server-devel
%endif
BuildRequires:  pkgconfig(systemd)
%{?systemd_requires}
Requires(pre):  user(ftp)

%description
Pure-FTPd is a fast, production-quality, and standard-conforming FTP
server, based-on Troll-FTPd. Unlike other popular FTP servers, it has
no known security flaws, is trivial to set up, and is especially
designed for modern Linux kernels (setfsuid and sendfile capabilities)
. Features include: PAM support, IPv6, chroot()ed home directories,
virtual domains, built-in LS, anti-warez system, bandwidth throttling,
FXP, bounded ports for passive downloads, upload and download ratios,
Apache log files, and more.

%prep
%setup -q
%patch0
%patch1
%patch2
%patch5
%patch7
%patch8 -p1
%patch9 -p2
%patch10 -p1

%build
#CFLAGS="%{optflags} -DLDAP_DEPRECATED -fstack-protector -fvisibility=hidden"
%configure \
	--with-rfc2640 \
	--sysconfdir=%{_sysconfdir}/%{name} \
	--with-ldap \
	--with-paranoidmsg \
	--with-altlog \
	--with-virtualhosts \
	--with-ftpwho \
	--with-mysql \
	--with-nonalnum \
	--with-pgsql \
	--with-cookie \
	--with-throttling \
	--with-ratios \
	--with-uploadscript \
	--with-diraliases \
	--with-pam \
	--with-puredb \
	--with-sysquotas \
	--with-quotas \
	--with-inetd \
	--with-tls \
	--with-boring \
	--with-peruserlimits \
	--with-virtualchroot
make %{?_smp_mflags}

%install
%make_install

install -dD -m 0755 \
    %{buildroot}%{_sysconfdir}/{%{name},%{name}/vhosts,pam.d,openldap/schema}
install -m 0644 pure-ftpd.conf  %{buildroot}%{_sysconfdir}/%{name}

install -m 0644 %{SOURCE4} %{buildroot}%{_sysconfdir}/pam.d/pure-ftpd

install -m 0644 pureftpd.schema %{buildroot}%{_sysconfdir}/openldap/schema/

install -D -m 0644 usr.sbin.pure-ftpd %{buildroot}%{_sysconfdir}/apparmor/profiles/extras/usr.sbin.pure-ftpd

install -D -m0644 %{SOURCE8} %{buildroot}%{_unitdir}/%{name}.service
ln -sf service %{buildroot}%{_sbindir}/rc%{name}

%pre
%service_add_pre %{name}.service

%preun
%service_del_preun %{name}.service

%post
if [ -f etc/pure-ftpd.conf ]; then
        mv etc/pure-ftpd.conf etc/pure-ftpd/pure-ftpd.conf
fi
%service_add_post %{name}.service

%postun
%service_del_postun %{name}.service

%files
%license COPYING
%doc AUTHORS CONTACT NEWS THANKS README
%doc README.Configuration-File HISTORY README.Virtual-Users README.AppArmor
%doc README.LDAP pureftpd-ldap.conf README.MySQL README.PGSQL README.TLS
%{_mandir}/man8/*
%{_bindir}/*
%{_sbindir}/*
%dir %{_sysconfdir}/openldap
%dir %{_sysconfdir}/openldap/schema
%dir %{_sysconfdir}/%{name}
%dir %{_sysconfdir}/%{name}/vhosts
%dir %{_sysconfdir}/apparmor
%dir %{_sysconfdir}/apparmor/profiles
%dir %{_sysconfdir}/apparmor/profiles/extras
%config %{_sysconfdir}/openldap/schema/pureftpd.schema
%config %{_sysconfdir}/pam.d/pure-ftpd
%config(noreplace) %{_sysconfdir}/%{name}/pure-ftpd.conf
%config(noreplace) %{_sysconfdir}/apparmor/profiles/extras/usr.sbin.pure-ftpd

%{_unitdir}/%{name}.service

%changelog
