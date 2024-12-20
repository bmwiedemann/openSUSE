#
# spec file for package squidGuard
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


%define sg_dbhome %{_localstatedir}/lib/squidGuard/db
%define sg_logdir %{_localstatedir}/log/squidGuard
%define sg_config %{_sysconfdir}/squidguard.conf
%define cgidir    /srv/www/cgi-bin
%define imgdir    /srv/www/htdocs/images
%define uname     maintain_squidguard-upstream
Name:           squidGuard
Version:        1.6.0
Release:        0
Summary:        Filter plugin for squid
License:        GPL-2.0-only
Group:          Productivity/Networking/Web/Proxy
URL:            http://www.squidguard.org/
# GIT-CLONE:    https://salsa.debian.org/joowie-guest/maintain_squidguard
Source0:        https://salsa.debian.org/joowie-guest/maintain_squidguard/-/archive/upstream/%{version}/%{uname}-%{version}.tar.bz2
Source1:        README.SUSE
Source2:        squidGuard.logrotate
Source3:        blocked.gif
Patch0:         squidGuard-mysql.patch
Patch1:         squidGuard-config.patch
Patch2:         default_config_pathfixes.patch
Patch3:         config_exit.patch
Patch4:         types.patch
BuildRequires:  bison
BuildRequires:  db-devel
BuildRequires:  flex
BuildRequires:  gettext
BuildRequires:  grep
BuildRequires:  libmysqlclient-devel
BuildRequires:  libtool
BuildRequires:  openldap2-devel
Requires:       http_proxy
Requires(pre):  http_proxy
Recommends:     logrotate
Recommends:     lynx

%description
SquidGuard is a filter, redirector, and access controller plugin for squid.
It lets you define multiple access rules with different restrictions for
different user groups on a squid cache. SquidGuard uses squid's standard
redirector interface.

%package doc
Summary:        Documentation and examples for squidGuard
Group:          Documentation/Other

%description doc
This package contains documentation for SquidGuard, a filter, redirector,
and access controller plugin for squid.

%prep
%autosetup -p1 -n %{uname}-%{version}
cp %{SOURCE1} .
# patch the test configs
pushd test 1>/dev/null
for i in test*.conf.in; do
	sed "s|logdir @TESTDIR@|logdir %{sg_logdir}|; \
		 s|dbhome @TESTDIR@|dbhome %{sg_dbhome}|" $i > $i.tmp
	mv -v $i.tmp $i
done

%build
export CFLAGS="%{optflags} -fcommon"
./autogen.sh
%configure \
	--with-squiduser=squid \
	--with-mysql \
	--with-nolog=yes \
	--with-db-inc=%{_includedir}/db4 \
	--with-sg-config=%{sg_config} \
	--with-sg-dbhome=%{sg_dbhome} \
	--with-sg-logdir=%{sg_logdir} \
	--with-ldap
%make_build
pushd contrib
%make_build
popd

%install
mkdir %{buildroot}%{_sysconfdir}
%make_install
# fix install dir
if [ -f %{buildroot}/%{_bindir}/squidGuard ]; then
	mkdir -p %{buildroot}/%{_sbindir}
	install -m755 %{buildroot}/%{_bindir}/squidGuard  %{buildroot}/%{_sbindir}/
	rm -rf %{buildroot}/%{_bindir}
fi
# install blacklist
mkdir -p %{buildroot}%{_localstatedir}/lib/squidGuard/db/blacklist
install -m 644 test/blacklist/* %{buildroot}%{_localstatedir}/lib/squidGuard/db/blacklist
# install cgi
mkdir -p %{buildroot}/%{cgidir}
mkdir -p %{buildroot}/%{imgdir}
install -m755 samples/*.cgi  %{buildroot}/%{cgidir}/
install -m644 samples/babel* %{buildroot}/%{cgidir}/
install -m644 %{SOURCE3}         %{buildroot}/%{imgdir}/blocked.gif
# prepare logdir
mkdir -p %{buildroot}%{sg_logdir}
# prepare logrotate
mkdir -p %{buildroot}%{_sysconfdir}/logrotate.d
sed "s|@SG_LOGDIR@|%{sg_logdir}|g" %{SOURCE2} > %{buildroot}%{_sysconfdir}/logrotate.d/%{name}
# clean up
rm -f {contrib,doc,samples,test}/{Makefile,*.in,*/*.in,.*.swp}
# install docu
mkdir -p %{buildroot}/%{_defaultdocdir}/%{name}
cp -r {contrib,doc,samples,test} %{buildroot}/%{_defaultdocdir}/%{name}/
cp ANNOUNCE CHANGELOG FAQ README* %{buildroot}/%{_defaultdocdir}/%{name}/

%files
%license GPL COPYING
%dir %{_defaultdocdir}/%{name}
%doc %{_defaultdocdir}/%{name}/ANNOUNCE
%doc %{_defaultdocdir}/%{name}/CHANGELOG
%doc %{_defaultdocdir}/%{name}/FAQ
%doc %{_defaultdocdir}/%{name}/README*
%attr(770, squid, squid) %dir %{_localstatedir}/lib/squidGuard
%attr(770, squid, squid) %dir %{sg_dbhome}
%attr(770, squid, squid) %dir %{sg_logdir}
%config(noreplace) %attr(660, squid, squid) %{sg_config}
%dir %attr(770, squid, squid) %{_localstatedir}/lib/squidGuard/db/blacklist
%config(noreplace) %attr(660, squid, squid) %{_localstatedir}/lib/squidGuard/db/blacklist/*
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%{_sbindir}/*
%dir /srv/www
%dir /srv/www/htdocs
%dir %{imgdir}
%dir %{cgidir}
%{cgidir}/*
%{imgdir}/*

%files doc
%license GPL COPYING
%doc %{_defaultdocdir}/%{name}/contrib
%doc %{_defaultdocdir}/%{name}/doc
%doc %{_defaultdocdir}/%{name}/samples
%doc %{_defaultdocdir}/%{name}/test

%changelog
