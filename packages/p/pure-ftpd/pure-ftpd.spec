#
# spec file for package pure-ftpd
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


Name:           pure-ftpd
Version:        1.0.51
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
Source6:        %{name}.ftpusers
Source8:        %{name}.service
# PATCH-FEATURE-OPENSUSE %{name}-1.0.20_config.patch -- Custom service configs.
Patch0:         %{name}-1.0.20_config.patch
# PATCH-FEATURE-OPENSUSE %{name}-1.0.20_doc.patch -- Adjust command paths on documentation.
Patch1:         %{name}-1.0.20_doc.patch
# PATCH-FEATURE-OPENSUSE %{name}-1.0.20_virtualhosts.patch -- Custom VHOST_PATH on openSUSE.
Patch2:         %{name}-1.0.20_virtualhosts.patch
Patch5:         %{name}-1.0.49_ftpwho_path.patch
# PATCH-FIX-UPSTREAM %{name}-1.0.50-default_tcp_sedrcv_buffer_size.patch -- bnc#407363
Patch7:         %{name}-1.0.50-default_tcp_sedrcv_buffer_size.patch
# PATCH-FIX-OPENSUSE: bnc#789833
# won't be upstreamed, can be dropped when systemd will be only one init system and kernel get AUDIT_LOGINUID_IMMUTABLE
Patch8:         pure-ftpd-1.0.36-cap-audit-control.patch
Patch9:         pure-ftpd-apparmor.patch
Patch10:        pure-ftpd-malloc-limit.patch
Patch11:        https://github.com/jedisct1/pure-ftpd/commit/2bbe0f25c6b905044803649a29df5f765f940b91.patch#:/CVE-2024-48208.patch
BuildRequires:  libcap-devel
BuildRequires:  libsodium-devel
BuildRequires:  mysql-devel
BuildRequires:  openldap2-devel
BuildRequires:  pam-devel
BuildRequires:  postgresql-devel
Requires(pre):  coreutils
Provides:       ftp-server
Provides:       pureftpd = %{version}-%{release}
%if 0%{?suse_version} > 1500 || 0%{?sle_version} >= 150200
BuildRequires:  postgresql-server-devel
%endif
BuildRequires:  pkgconfig(systemd)
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
%patch -P 0
%patch -P 1
%patch -P 2
%patch -P 5
%patch -P 7
%patch -P 8 -p1
%patch -P 9 -p2
%patch -P 10 -p1
%patch -P 11 -p1

%build
CFLAGS="%{optflags} -I%{_includedir}/mysql"
%configure \
        --docdir=%{_docdir}/%{name} \
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
	--with-virtualchroot \
	--with-extauth
%make_build

%install
%make_install

install -dD -m 0755 \
    %{buildroot}%{_sysconfdir}/{%{name},%{name}/vhosts,openldap/schema}
install -m 0644 pure-ftpd.conf  %{buildroot}%{_sysconfdir}/%{name}
install -m 0600 %{SOURCE6} $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/ftpusers
%if 0%{?suse_version} > 1500
install -dD -m 0755 %{buildroot}%{_pam_vendordir}
install -m 0644 %{SOURCE4} %{buildroot}%{_pam_vendordir}/pure-ftpd
%else
install -dD -m 0755 %{buildroot}%{_sysconfdir}/pam.d
install -m 0644 %{SOURCE4} %{buildroot}%{_sysconfdir}/pam.d/pure-ftpd
%endif

install -m 0644 pureftpd.schema %{buildroot}%{_sysconfdir}/openldap/schema/

install -D -m 0644 usr.sbin.pure-ftpd %{buildroot}%{_sysconfdir}/apparmor/profiles/extras/usr.sbin.pure-ftpd

install -D -m0644 %{SOURCE8} %{buildroot}%{_unitdir}/%{name}.service
ln -sf service %{buildroot}%{_sbindir}/rc%{name}

rm %{buildroot}/%{_docdir}/%{name}/README.MacOS-X
rm %{buildroot}/%{_docdir}/%{name}/pureftpd.schema
rm %{buildroot}/%{_docdir}/%{name}/pure-ftpd.conf

%pre
%service_add_pre %{name}.service
%if 0%{?suse_version} > 1500
# Prepare for migration to /usr/lib; save any old .rpmsave
for i in pam.d/pure-ftpd ; do
     test -f %{_sysconfdir}/${i}.rpmsave && mv -v %{_sysconfdir}/${i}.rpmsave %{_sysconfdir}/${i}.rpmsave.old ||:
done

%posttrans
# Migration to /usr/lib, restore just created .rpmsave
for i in pam.d/pure-ftpd ; do
     test -f %{_sysconfdir}/${i}.rpmsave && mv -v %{_sysconfdir}/${i}.rpmsave %{_sysconfdir}/${i} ||:
done
%endif

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
%doc FAQ AUTHORS NEWS THANKS README
%doc README.Configuration-File HISTORY README.Virtual-Users README.AppArmor
%doc README.LDAP pureftpd-ldap.conf README.MySQL pureftpd-mysql.conf
%doc README.PGSQL pureftpd-pgsql.conf README.TLS
%doc README.Donations README.Authentication-Modules
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
%if 0%{?suse_version} > 1500
%{_pam_vendordir}/pure-ftpd
%else
%config %{_sysconfdir}/pam.d/pure-ftpd
%endif
%config(noreplace) %{_sysconfdir}/%{name}/pure-ftpd.conf
%config(noreplace) %{_sysconfdir}/%{name}/ftpusers
%config(noreplace) %{_sysconfdir}/apparmor/profiles/extras/usr.sbin.pure-ftpd

%{_unitdir}/%{name}.service

%changelog
