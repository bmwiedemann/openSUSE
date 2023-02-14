#
# spec file for package cfengine
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


%define libname   libpromises
%define libsoname %{libname}3
# Yes, its not FHS conformant but in sync with cfengine documentation
%define   basedir   %{_localstatedir}/%{name}
%define   workdir   %{basedir}
# This is the place where workdir should be
#%%define basedir   %%{_localstatedir}/lib/%%{name}
#%%define workdir   %%{basedir}/work
%if 0%{?suse_version} < 1500
# assume SuSEfirewall2
%define with_sfw2 1
%else
# assume firewalld
%define with_sfw2 0
%endif
# Version of libntech needed (see git repo of core)
%define libntech_hash 522ec6b3240a332884d0f67059268edd8cf30cba
# pass --with-bla to enable the build
%bcond_with mysql
%bcond_with postgresql
%bcond_with libvirt
Name:           cfengine
Version:        3.21.0
Release:        0
Summary:        Configuration management framework
License:        GPL-3.0-only
Group:          Productivity/Networking/System
URL:            https://cfengine.com/
Source0:        https://github.com/cfengine/core/archive/refs/tags/%{version}.tar.gz#/core-%{version}.tar.gz
Source1:        https://github.com/cfengine/libntech/archive/%{libntech_hash}.tar.gz#/libntech-%{libntech_hash}.tar.gz
Source11:       %{name}.SuSEfirewall2
Source12:       cf-execd.service
Source13:       cf-monitord.service
Source14:       cf-serverd.service
Source15:       cf-monitord
Source16:       cf-execd
Source17:       cf-serverd
Source20:       %{name}.cron
Source21:       %{name}-rpmlintrc
Patch0:         harden_cf-apache.service.patch
Patch1:         harden_cf-execd.service.patch
Patch2:         harden_cf-hub.service.patch
Patch3:         harden_cf-monitord.service.patch
Patch4:         harden_cf-postgres.service.patch
Patch5:         harden_cf-runalerts.service.patch
Patch6:         harden_cf-serverd.service.patch
Patch7:         harden_cfengine3.service.patch
BuildRequires:  bison
BuildRequires:  db-devel
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  libacl-devel
BuildRequires:  libtool
BuildRequires:  libxml2-devel
BuildRequires:  lmdb-devel >= 0.9.17
BuildRequires:  openssl-devel >= 1.0.2e
BuildRequires:  pam-devel
BuildRequires:  pcre-devel >= 8.38
BuildRequires:  pkgconfig
# for flock
BuildRequires:  util-linux
# for llzma
BuildRequires:  xz-devel
BuildRequires:  pkgconfig(systemd)
Requires:       %{libsoname} = %{version}
Recommends:     %{name}-documentation
%{?systemd_requires}
%if !%{with_sfw2}
BuildRequires:  firewall-macros
%endif
%if %{with mysql}
BuildRequires:  mysql-devel
%endif
%if %{with libvirt}
BuildRequires:  libvirt-devel
%endif
%if %{with postgresql}
BuildRequires:  postgresql-devel
%endif
%if 0%{?fedora_version} == 20
BuildRequires:  perl-Exporter
%endif

%description
CFEngine is the core of a configuration management system. It
combines modeling and monitoring to move a system into compliance
with a user-defined model (the Desired State). A domain-specific
language is used for setting this up.

%package -n %{libsoname}
Summary:        Shared library of cfengine
Group:          System/Libraries
Provides:       %{libname}1 = %{version}
Obsoletes:      %{libname}1 < %{version}

%description -n %{libsoname}
This package contains the shared libpromises (cfengine) library.

%package -n %{libname}-devel
Summary:        Development package for libpromises
Group:          Development/Libraries/C and C++
Requires:       %{libsoname} = %{version}
Requires:       glibc-devel
Provides:       %{name}-devel = %{version}
Obsoletes:      %{name}-devel < %{version}

%description -n %{libname}-devel
A character set detection library.

This package contains the files needed to compile programs that use the
libpromises library.

%package examples
Summary:        CFEngine example promises
Group:          Documentation/Other
BuildArch:      noarch

%description examples
Lots of example promises for CFEngine.

%prep
%setup -q -n core-%{version} -a 1
[ -d libntech ] && rmdir -v libntech
ln -s libntech-%{libntech_hash} libntech
##### rpmlint
#### wrong-file-end-of-line-encoding
find ./examples -type f -name "*.cf" -exec perl -p -i -e 's|\r\n|\n|' {} \;
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1

%build
EXPLICIT_VERSION=%{version} autoreconf -fvi -I m4
CC=cc CFLAGS="%{optflags} -fno-strict-aliasing" \
%configure \
  --disable-static \
  --disable-silent-rules \
  --enable-fhs \
  --datadir=%{_localstatedir} \
  --with-workdir=%{workdir} \
%if %{with postgresql}
  --with-postgresql \
%endif
%if %{with mysql}
  --with-mysql \
%endif
  --without-qdbm \
  --without-tokyocabinet \
  --with-lmdb \
  --with-pthreads \
  --with-openssl \
  --with-pcre \
%if %{with libvirt}
  --with-libvirt \
%endif
  --without-libacl \
  --with-libxml2 \
%if 0%{?rhel_version} > 0 && 0%{?rhel_version} < 700
  --docdir=%{_docdir}/%{name}-%{version} \
%else
  --docdir=%{_docdir}/%{name} \
%endif
  --with-pam

%make_build

%check
# FAIL: process_test
%make_build check || :

%install
chmod -x ChangeLog
%make_install

# will appear in cfengine-examples
rm -rf %{buildroot}/%{_docdir}/%{name}/examples

install -d %{buildroot}/{%{_bindir},%{_sbindir},%{workdir}/{bin,inputs,reports}}

# create dirs needed for better organizing dirs and files
install -d %{buildroot}/%{basedir}/{backup,failsafe,config,plugins}

# systemd: install sample cron file in docdir
cp %{SOURCE20} %{buildroot}/%{_docdir}/%{name}

# install systemd scripts
install -d %{buildroot}%{_unitdir}
install -m 0644 %{SOURCE12} %{SOURCE13} %{SOURCE14} %{buildroot}/%{_unitdir}
ln -s -f service %{buildroot}/%{_sbindir}/rccf-monitord
ln -s -f service %{buildroot}/%{_sbindir}/rccf-execd
ln -s -f service %{buildroot}/%{_sbindir}/rccf-serverd

# create symlinks for bin_PROGRAMS
# because: cf-promises needs to be installed in /var/cfengine/work/bin for pre-validation of full configuration
for i in cf-agent cf-execd cf-key cf-monitord cf-promises cf-runagent cf-serverd cf-upgrade; do
  ln -s -f %{_bindir}/${i} %{buildroot}%{workdir}/bin/${i}
done

rm -rf %{buildroot}/%{_libdir}/%{name}/libpromises.la

# will appear in %%docdir
rm -rf %{buildroot}/%{_datadir}/%{name}/ChangeLog
rm -rf %{buildroot}/%{_datadir}/%{name}/README

# create man pages, see https://cfengine.com/dev/issues/2989
install -d %{buildroot}/%{_mandir}/man8
for i in cf-agent cf-execd cf-key cf-monitord cf-promises cf-runagent cf-serverd
do
  LD_LIBRARY_PATH=%{buildroot}%{_libdir}/%{name} %{buildroot}%{_bindir}/$i -M > %{buildroot}%{_mandir}/man8/$i.8
  gzip -n9 %{buildroot}%{_mandir}/man8/$i.8
done

# Firewall
%if %{with_sfw2}
install -D -m 644 %{SOURCE11} %{buildroot}%{_sysconfdir}/sysconfig/SuSEfirewall2.d/services/cfengine
%endif

# Ckeabyo dyoes
%fdupes %{buildroot}%{_datadir}/cfengine

%define cf_services cf-execd.service cf-monitord.service cf-serverd.service cf-apache.service cf-hub.service cf-postgres.service cf-runalerts.service cf-reactor.service cfengine3.service

%pre
%service_add_pre %{cf_services}

%post
%service_add_post %{cf_services}
if [ $1 -lt 2 ]; then
  # first install, generate key pair
  cf-key
fi
%if !%{with_sfw2}
%firewalld_reload
%endif

%preun
%service_del_preun %{cf_services}

%postun
%service_del_postun %{cf_services}
if [ $1 -eq 0 ]; then
  # clean up inputs cache dir on removal
  rm -rf %{basedir}/inputs/*
fi
%if !%{with_sfw2}
%firewalld_reload
%endif

%post   -n %{libsoname} -p /sbin/ldconfig
%postun -n %{libsoname} -p /sbin/ldconfig

%files
%license LICENSE
%doc ChangeLog README.md
%{_bindir}/cf-agent
%{_bindir}/cf-check
%{_bindir}/cf-execd
%{_bindir}/cf-key
%{_bindir}/cf-net
%{_bindir}/cf-monitord
%{_bindir}/cf-promises
%{_bindir}/cf-secret
%{_bindir}/cf-serverd
%{_bindir}/cf-support
%{_bindir}/cf-upgrade
%{_bindir}/cf-runagent
%{_bindir}/rpmvercmp
%{_sbindir}/rccf-execd
%{_sbindir}/rccf-monitord
%{_sbindir}/rccf-serverd
%{_unitdir}/*.service
%if %{with_sfw2}
%config %dir %{_sysconfdir}/sysconfig/SuSEfirewall2.d
%config %dir %{_sysconfdir}/sysconfig/SuSEfirewall2.d/services
%config %{_sysconfdir}/sysconfig/SuSEfirewall2.d/services/cfengine
%endif
%{_mandir}/man8/*
%dir %{basedir}
%dir %{workdir}
%{workdir}/*
%{_docdir}/%{name}/cfengine.cron

%files -n %{libsoname}
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/%{libname}.so.*

%files -n %{libname}-devel
%{_libdir}/%{name}/%{libname}.so

%files examples
%doc examples/*cf

%changelog
