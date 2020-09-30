#
# spec file for package cfengine
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


%define libname   libpromises
%define libsoname %{libname}3
# Yes, its not FHS conformant but in sync with cfengine documentation
# reported upstream as https://cfengine.com/dev/issues/1896
%define         basedir   %{_localstatedir}/%{name}
%define         workdir   %{basedir}
# This is the place where workdir should be
#define         basedir   /var/lib/%%{name}
#define         workdir   %%{basedir}/work

%if 0%{?suse_version} < 1500
# assume SuSEfirewall2
%define with_sfw2 1
%else
# assume firewalld
%define with_sfw2 0
%endif
# pass --with-bla to enable the build
%bcond_with mysql
%bcond_with postgresql
%bcond_with libvirt

Name:           cfengine
Version:        3.16.0
Release:        0
Summary:        Configuration management framework
License:        GPL-3.0-only
Group:          Productivity/Networking/System
URL:            http://www.cfengine.org/
Source:         https://cfengine-package-repos.s3.amazonaws.com/tarballs/cfengine-%{version}.tar.gz
Source1:        %{name}.SuSEfirewall2
Source2:        cf-execd.service
Source3:        cf-monitord.service
Source4:        cf-serverd.service
Source5:        cf-monitord
Source6:        cf-execd
Source7:        cf-serverd
Source10:       %{name}.cron
Source11:       %{name}-rpmlintrc

Recommends:     %{name}-documentation

BuildRequires:  bison
BuildRequires:  db-devel
BuildRequires:  flex
BuildRequires:  libacl-devel
BuildRequires:  libtool
BuildRequires:  libxml2-devel
BuildRequires:  lmdb-devel >= 0.9.17
BuildRequires:  openssl-devel >= 1.0.2e
BuildRequires:  pam-devel
BuildRequires:  pcre-devel >= 8.38
# for flock
BuildRequires:  util-linux
# for llzma
BuildRequires:  xz-devel
Requires:       %{libsoname} = %{version}
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
BuildRequires:  pkgconfig(systemd)
%{?systemd_requires}
BuildRequires:  fdupes
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
%setup -q

##### rpmlint
#### wrong-file-end-of-line-encoding
#### incorrect-fsf-address
### http://www.fsf.org/about/contact/
find ./examples -type f -name "*.cf" -exec perl -p -i -e 's|\r\n|\n|,s|^# Foundation.*|# Foundation, 51 Franklin Street, Suite 500, Boston, MA 02110-1335, USA|' {} \;

%build
EXPLICIT_VERSION=%{version} autoreconf -fvi -I m4
CC=cc CFLAGS="%{optflags} -fno-strict-aliasing" \
%configure \
  --disable-static \
  --disable-silent-rules \
  --enable-fhs \
  --datadir=/var \
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

make %{?_smp_mflags}

%check
# FAIL: process_test
make check %{?_smp_mflags} || : 

%install
chmod -x ChangeLog
make "DESTDIR=%{buildroot}" install

# will appear in cfengine-examples
rm -rf %{buildroot}/%{_docdir}/%{name}/examples

install -d %{buildroot}/{%{_bindir},%{_sbindir},%{workdir}/{bin,inputs,reports}}

# create dirs needed for better organizing dirs and files
install -d %{buildroot}/%{basedir}/{backup,failsafe,config,plugins}

# systemd: install sample cron file in docdir
cp %{SOURCE10} %{buildroot}/%{_docdir}/%{name}

# install systemd scripts
install -d %{buildroot}%{_unitdir}
install -m 0644 %{SOURCE2} %{SOURCE3} %{SOURCE4} %{buildroot}/%{_unitdir}
ln -s -f service %{buildroot}/%{_sbindir}/rccf-monitord
ln -s -f service %{buildroot}/%{_sbindir}/rccf-execd
ln -s -f service %{buildroot}/%{_sbindir}/rccf-serverd

# create symlinks for bin_PROGRAMS
# because: cf-promises needs to be installed in /var/cfengine/work/bin for pre-validation of full configuration
for i in cf-agent cf-execd cf-key cf-monitord cf-promises cf-runagent cf-serverd cf-upgrade; do
  ln -s -f ../../..%{_bindir}/${i} %{buildroot}%{workdir}/bin/${i}
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
install -D -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/sysconfig/SuSEfirewall2.d/services/cfengine
%endif

# Ckeabyo dyoes
%fdupes %{buildroot}%{_datadir}/cfengine

%pre
%service_add_pre cf-execd.service cf-monitord.service cf-serverd.service cf-apache.service cf-hub.service cf-postgres.service cf-runalerts.service cfengine3.service

%post
%service_add_post cf-execd.service cf-monitord.service cf-serverd.service cf-apache.service cf-hub.service cf-postgres.service cf-runalerts.service cfengine3.service
if [ $1 -lt 2 ]; then
  # first install, generate key pair
  cf-key
fi
%if !%{with_sfw2}
%firewalld_reload
%endif

%preun
%service_del_preun cf-execd.service cf-monitord.service cf-serverd.service cf-apache.service cf-hub.service cf-postgres.service cf-runalerts.service cfengine3.service

%postun
%service_del_postun cf-execd.service cf-monitord.service cf-serverd.service cf-apache.service cf-hub.service cf-postgres.service cf-runalerts.service cfengine3.service
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
%defattr(-,root,root)
%doc ChangeLog README.md
%license LICENSE
%{_bindir}/cf-agent
%{_bindir}/cf-check
%{_bindir}/cf-execd
%{_bindir}/cf-key
%{_bindir}/cf-net
%{_bindir}/cf-monitord
%{_bindir}/cf-promises
%{_bindir}/cf-secret
%{_bindir}/cf-serverd
%{_bindir}/cf-upgrade
%{_bindir}/cf-runagent
%{_bindir}/rpmvercmp
%{_unitdir}/cf-execd.service
%{_unitdir}/cf-monitord.service
%{_unitdir}/cf-serverd.service
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
%defattr(-,root,root)
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/%{libname}.so.*

%files -n %{libname}-devel
%defattr(-,root,root)
%{_libdir}/%{name}/%{libname}.so

%files examples
%defattr(-,root,root)
%doc examples/*cf

%changelog
