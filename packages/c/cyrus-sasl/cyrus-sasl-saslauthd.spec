#
# spec file for package cyrus-sasl-saslauthd
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


#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif

Name:           cyrus-sasl-saslauthd
Version:        2.1.28
Release:        0
Summary:        The SASL Authentication Server
License:        BSD-4-Clause
Group:          Productivity/Networking/Other
URL:            https://github.com/cyrusimap/cyrus-sasl
Source:         https://github.com/cyrusimap/cyrus-sasl/releases/download/cyrus-sasl-%{version}/cyrus-sasl-%{version}.tar.gz
Source1:        cyrus-sasl-rc.tar.bz2
Source2:        README.Source
Source3:        baselibs.conf
Source4:        saslauthd.service
Patch:          cyrus-sasl.dif
Patch5:         cyrus-sasl-no_rpath.patch
Patch6:         cyrus-sasl-lfs.patch
Patch7:         fix_libpq-fe_include.diff
PreReq:         %fillup_prereq
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  gdbm-devel
BuildRequires:  krb5-devel
BuildRequires:  libtool
BuildRequires:  mysql-devel
BuildRequires:  openldap2-devel
BuildRequires:  opie
BuildRequires:  pam-devel
BuildRequires:  postgresql-devel
BuildRequires:  pkgconfig(systemd)
%{?systemd_requires}
Conflicts:      cyrus-sasl-saslauthd-bdb

%description
This daemon is required when using cyrus-sasl in server software that
should authenticate with PAM, for example.

%package -n     cyrus-sasl-ldap-auxprop
Summary:        The cyrus-sasl LDAP auxprop plugin
Group:          Productivity/Networking/Other
Requires:       cyrus-sasl = %{version}
Conflicts:      cyrus-sasl-ldap-auxprop-bdb

%description -n cyrus-sasl-ldap-auxprop
The LDAP auxprop plugin allows for tighter application/directory
integration.

%package -n     cyrus-sasl-sqlauxprop
Summary:        SQL auxprop plugin for cyrus-sasl
Group:          Development/Libraries/C and C++
Requires:       cyrus-sasl = %{version}
Conflicts:      cyrus-sasl-sqlauxprop-bdb

%description -n cyrus-sasl-sqlauxprop
The SQL auxprop plugin supports PostgreSQL and MySQL

%prep
%setup -n cyrus-sasl-%{version} -a 1
%patch
%patch5 -p1
%patch6 -p1
%patch7 -p1

%build
find . -name "*.cvsignore" -exec rm -fv "{}" "+"
autoreconf -f
export CFLAGS="-fno-strict-aliasing $RPM_OPT_FLAGS -DLDAP_DEPRECATED"
%configure --with-plugindir=%{_libdir}/sasl2 \
            --with-configdir=/etc/sasl2/:%{_libdir}/sasl2 \
            --with-saslauthd=/run/sasl2/ \
            --enable-checkapop=no \
            --enable-cram=no \
            --enable-digest=no \
            --enable-otp=no \
            --enable-srp=no \
            --enable-plain=no \
            --enable-anon=no \
            --enable-ntlm=no \
            --enable-passdss=no \
            --enable-sample=no \
            --enable-login=no \
            --enable-gssapi=yes \
            --enable-gs2=no \
            --enable-scram=no \
            --enable-krb4=no \
            --enable-sql \
            --with-mysql=/usr/include/mysql \
            --with-pgsql=/usr/include/pgsql \
            --enable-ldapdb=yes \
            --with-pam \
            --with-ldap
make sasldir=%{_libdir}/sasl2 %{?_smp_mflags}

%install
cd plugins
make DESTDIR=$RPM_BUILD_ROOT sasldir=%{_libdir}/sasl2 install
cd ..
cd saslauthd
make DESTDIR=$RPM_BUILD_ROOT sasldir=%{_libdir}/sasl2 install
ln -s service "%buildroot/%_sbindir/rcsaslauthd"
install -m 755 -d $RPM_BUILD_ROOT/run/sasl2
mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man8
install -m 644 saslauthd.mdoc $RPM_BUILD_ROOT/%{_mandir}/man8/saslauthd.8
mkdir -p $RPM_BUILD_ROOT/usr/bin
install -m 755 testsaslauthd $RPM_BUILD_ROOT/usr/bin/testsaslauthd
cd -
mkdir -p $RPM_BUILD_ROOT/sbin
install -D -m 644 SuSE/sysconfig.saslauthd $RPM_BUILD_ROOT%{_fillupdir}/sysconfig.saslauthd
rm -f $RPM_BUILD_ROOT/%{_mandir}/cat?/*
rm -f $RPM_BUILD_ROOT/%{_libdir}/sasl2/libsasldb*
rm -f $RPM_BUILD_ROOT/%{_libdir}/sasl2/libldapdb.la
rm -f $RPM_BUILD_ROOT/%{_libdir}/sasl2/libsql.la
rm -f $RPM_BUILD_ROOT/%{_libdir}/sasl2/libgs2.*
rm -f $RPM_BUILD_ROOT/%{_libdir}/sasl2/libgssapiv2.*

mkdir -p $RPM_BUILD_ROOT/%{_unitdir}
install -m 644 %{SOURCE4} $RPM_BUILD_ROOT/%{_unitdir}

%pre
%service_add_pre saslauthd.service

%preun
%service_del_preun saslauthd.service

%postun
%service_del_postun saslauthd.service

%post
%{fillup_only -n saslauthd}
%service_add_post saslauthd.service

%files
%license saslauthd/COPYING
%{_fillupdir}/sysconfig.saslauthd
%{_unitdir}/saslauthd.service
%dir %attr(0755, root, root) %ghost /run/sasl2
/usr/sbin/*
/usr/bin/*
%doc %{_mandir}/man8/*.gz
%doc saslauthd/ChangeLog saslauthd/LDAP_SASLAUTHD

%files -n cyrus-sasl-sqlauxprop
%dir %_libdir/sasl2/
%{_libdir}/sasl2/libsql.so*

%files -n cyrus-sasl-ldap-auxprop
%dir %_libdir/sasl2/
%{_libdir}/sasl2/libldapdb.so*

%changelog
