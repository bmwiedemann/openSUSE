#
# spec file for package apache2-mod_nss
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
#


%if ! %{defined apache_apxs}
%define    apache_apxs %{_sbindir}/apxs
%define    apache apache2
%define    apache_libexecdir %(%{apxs} -q LIBEXECDIR)
%define    apache_sysconfdir %(%{apxs} -q SYSCONFDIR)
%define    apache_includedir %(%{apxs} -q INCLUDEDIR)
%define    apache_serverroot %(%{apxs} -q PREFIX)
%define    apache_mmn        %(MMN=$(%{apxs} -q LIBEXECDIR)_MMN; test -x $MMN && $MMN)
%endif
%define    apache_sysconf_nssdir %{apache_sysconfdir}/mod_nss.d
Name:           apache2-mod_nss
Version:        1.0.18
Release:        0
Summary:        SSL/TLS module for the Apache HTTP server
License:        Apache-2.0
Group:          Productivity/Networking/Web/Servers
URL:            https://pagure.io/mod_nss
Source:         https://releases.pagure.org/mod_nss/mod_nss-%{version}.tar.gz
Source1:        mod_nss.conf.in
Source2:        listen_nss.conf
Source4:        README-SUSE.txt
Source5:        vhost-nss.template
Patch1:         mod_nss-migrate.patch
Patch2:         mod_nss-gencert-correct-ownership.patch
Patch4:         mod_nss-gencert_use_ss_instead_of_netstat.patch
Patch5:         mod_nss-gencert_stronger_password.patch
BuildRequires:  apache-rpm-macros
BuildRequires:  apache2-devel >= 2.4.18
BuildRequires:  apr-devel
BuildRequires:  apr-util-devel
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  curl
BuildRequires:  findutils
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  iproute2
BuildRequires:  libtool
BuildRequires:  mozilla-nspr-devel >= 4.6.3
BuildRequires:  mozilla-nss-devel >= 3.25
BuildRequires:  mozilla-nss-tools
BuildRequires:  pkgconfig
Requires:       %{apache_mmn}
Requires:       %{apache_suse_maintenance_mmn}
Requires:       apache2 >= 2.4.18
Requires:       findutils
Requires:       iproute2
Requires:       mozilla-nss >= 3.25
Requires(post): mozilla-nss-tools
Provides:       mod_nss

%description
The mod_nss module provides strong cryptography for the Apache Web
server via the Secure Sockets Layer (SSL) and Transport Layer
Security (TLS) protocols using the Network Security Services (NSS)
security library.

%prep
%setup -q -n mod_nss-%{version}
%autopatch -p1

# Touch expression parser sources to prevent regenerating it
touch nss_expr_*.[chyl]

%build
CFLAGS="%{optflags} -fcommon"
export CFLAGS
NSPR_INCLUDE_DIR=`%{_bindir}/pkg-config --variable=includedir nspr`
NSPR_LIB_DIR=`%{_bindir}/pkg-config --variable=libdir nspr`
NSS_INCLUDE_DIR=`%{_bindir}/pkg-config --variable=includedir nss`
NSS_LIB_DIR=`%{_bindir}/pkg-config --variable=libdir nss`
NSS_BIN=`%{_bindir}/pkg-config --variable=exec_prefix nss`
# For some reason mod_nss can't find nss on SUSE unless we do the following
C_INCLUDE_PATH="%{_includedir}/nss3:%{_includedir}/nspr4:%{_includedir}/apache2-prefork/"
export C_INCLUDE_PATH
# no more patching a config file...
cp -a %{SOURCE1} ./nss.conf.in
cp -a %{SOURCE4} .
chmod 644 ./nss.conf.in
autoreconf -fvi
%configure \
    --with-nss-lib=$NSS_LIB_DIR \
    --with-nss-inc=$NSS_INCLUDE_DIR \
    --with-nspr-lib=$NSPR_LIB_DIR \
    --with-nspr-inc=$NSPR_INCLUDE_DIR \
    --with-apxs=%{apache_apxs} \
    --enable-ecc \
    --with-apr-config
make %{?_smp_mflags} all

%install
# The install target of the Makefile isn't used because that uses apxs
# which tries to enable the module in the build host httpd instead of in
# the build root.
mkdir -p %{buildroot}/%{apache_libexecdir}
mkdir -p %{buildroot}%{apache_sysconfdir}/conf.d
mkdir -p %{buildroot}%{apache_sysconfdir}/vhosts.d
mkdir -p %{buildroot}%{_sbindir}
mkdir -p %{buildroot}%{apache_sysconf_nssdir}

%if 0%{?suse_version}
perl -pi -e "s|\@apache_lib\@|%{_libdir}\/apache2|g" nss.conf
%endif

install -m 644 nss.conf %{buildroot}%{apache_sysconfdir}/conf.d/mod_nss.conf
install -m 644 %{SOURCE5} %{buildroot}%{apache_sysconfdir}/vhosts.d/vhost-nss.template
install -m 644 %{SOURCE2} %{buildroot}%{apache_sysconfdir}/listen_nss.conf
install -m 755 .libs/libmodnss.so %{buildroot}%{apache_libexecdir}/mod_nss.so
install -m 755 nss_pcache %{buildroot}%{_sbindir}/
install -m 755 gencert %{buildroot}%{_sbindir}/
install -m 755 migrate.pl %{buildroot}%{_sbindir}/mod_nss_migrate.pl

#ln -s $RPM_BUILD_ROOT/%%{apache_libexecdir}/libnssckbi.so $RPM_BUILD_ROOT%%{apache_sysconf_nssdir}/
%if 0%{?suse_version} <= 1500
touch %{buildroot}%{apache_sysconf_nssdir}/secmod.db
touch %{buildroot}%{apache_sysconf_nssdir}/cert8.db
touch %{buildroot}%{apache_sysconf_nssdir}/key3.db
%else
touch %{buildroot}%{apache_sysconf_nssdir}/pkcs11.txt
touch %{buildroot}%{apache_sysconf_nssdir}/cert9.db
touch %{buildroot}%{apache_sysconf_nssdir}/key4.db
%endif
touch %{buildroot}%{apache_sysconf_nssdir}/install.log
perl -pi -e "s:$NSS_LIB_DIR:$NSS_BIN:" %{buildroot}%{_sbindir}/gencert

%post
umask 077
# generate a self-signed certificate if there isn't either
# key3.db (old DBM format) or key4.db (new SQLite format)
if [ ! -e %{apache_sysconf_nssdir}/key3.db -a ! -e %{apache_sysconf_nssdir}/key4.db ]; then
    %{_sbindir}/gencert %{apache_sysconf_nssdir} > %{apache_sysconf_nssdir}/install.log 2>&1
    echo ""
    echo "%{name} certificate database generated."
    echo ""
fi
# Make sure that the database ownership is setup properly.
find %{apache_sysconf_nssdir} -user root -name "*.db" -exec /bin/chgrp -h www {} +
find %{apache_sysconf_nssdir} -user root -name "*.db" ! -type l -exec /bin/chmod 640 {} +

%files
%license LICENSE
%doc README docs/mod_nss.html README-SUSE.txt
%config(noreplace) %{apache_sysconfdir}/conf.d/mod_nss.conf
%config(noreplace) %{apache_sysconfdir}/vhosts.d/vhost-nss.template
%config(noreplace) %{apache_sysconfdir}/listen_nss.conf
%dir %{apache_libexecdir}
%{apache_libexecdir}/mod_nss.so
%dir %{apache_sysconf_nssdir}/
%if 0%{?suse_version} <= 1500
%ghost %attr(0640,root,www) %config(noreplace) %{apache_sysconf_nssdir}/secmod.db
%ghost %attr(0640,root,www) %config(noreplace) %{apache_sysconf_nssdir}/cert8.db
%ghost %attr(0640,root,www) %config(noreplace) %{apache_sysconf_nssdir}/key3.db
%else
%ghost %attr(0640,root,www) %config(noreplace) %{apache_sysconf_nssdir}/pkcs11.txt
%ghost %attr(0640,root,www) %config(noreplace) %{apache_sysconf_nssdir}/cert9.db
%ghost %attr(0640,root,www) %config(noreplace) %{apache_sysconf_nssdir}/key4.db
%endif
%ghost %config(noreplace) %{apache_sysconf_nssdir}/install.log
%{_sbindir}/nss_pcache
%{_sbindir}/gencert
%{_sbindir}/mod_nss_migrate.pl

%changelog
