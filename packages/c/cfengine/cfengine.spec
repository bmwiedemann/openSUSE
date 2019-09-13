#
# spec file for package cfengine
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define libname   libpromises
%define libsoname %{libname}3
# Yes, its not FHS conformant but in sync with cfengine documentation
# reported upstream as https://cfengine.com/dev/issues/1896
%define         basedir   %{_localstatedir}/%{name}
%define         workdir   %{basedir}
%if 0%{?suse_version} >= 1210
%define have_systemd 1
%else
%define have_systemd 0
%endif
%if 0%{?suse_version} <= 150100
%define with_sfw2 1
%else
%define with_sfw2 0
%endif
# pass --with-bla to enable the build
%bcond_with mysql
%bcond_with postgresql
%bcond_with libvirt
Name:           cfengine
Version:        3.12.1
Release:        0
# This is the place where workdir should be
#define         basedir   /var/lib/%%{name}
#define         workdir   %%{basedir}/work
Summary:        Configuration management framework
License:        GPL-3.0-only
Group:          Productivity/Networking/System
Url:            http://www.cfengine.org/
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
# docs
Source101:      http://www.cfengine.org/manuals/cf3-Reference.pdf
Source102:      http://www.cfengine.org/manuals/cf3-conceptguide.pdf
Source103:      http://www.cfengine.org/manuals/cf3-glossary.pdf
Source104:      http://www.cfengine.org/manuals/cf3-quickstart.pdf
Source105:      http://www.cfengine.org/manuals/cf3-solutions.pdf
Source106:      http://www.cfengine.org/manuals/cf3-tutorial.pdf
Source107:      http://www.verticalsysadmin.com/cfengine/primer.pdf

# PATCH-FIX-SUSE
# set cfengine's notion of bindir to /usr/bin instead of /var/cfengine/bin
# kkaempf@suse.de
Patch1:         0001-Set-sys.bindir-to-usr-sbin-expect-cf-components-ther.patch
# PATCH-FIX-UPSTREAM add 'suse' class for consistency with other vendor classes
# PATCH-FEATURE-UPSTREAM better /etc/SuSE-release parsing, upstream #5423
# kkaempf@suse.de
Patch2:         0002-Simplify-and-fix-parsing-of-etc-SuSE-release-fixes-i.patch
# PATCH-FIX-SUSE reduce "string truncated" (in strncpy) warnings
Patch3:         0003-Reduce-string-truncation-warnings.patch
# PATCH-FIX-SUSE BNC#1016848, adam.majer
Patch10:        0004-make-home-dir-for-tests.patch
# SLE 11 or RHEL5 autoconf does not support AM_SUBST_NOTMAKE, kkaempf@suse.de
Patch99:        remove-am_subst_notmake.patch

BuildRequires:  bison
BuildRequires:  db-devel
BuildRequires:  fakeroot
BuildRequires:  flex
BuildRequires:  libacl-devel
BuildRequires:  libtool
BuildRequires:  libxml2-devel
BuildRequires:  lmdb-devel >= 0.9.17
BuildRequires:  openssl-devel >= 1.0.2e
BuildRequires:  pam-devel
BuildRequires:  pcre-devel >= 8.38
BuildRequires:  python
# for flock
BuildRequires:  util-linux
# for llzma
BuildRequires:  xz-devel
Requires:       %{libsoname} = %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if %{with mysql}
BuildRequires:  mysql-devel
%endif
%if %{with libvirt}
BuildRequires:  libvirt-devel
%endif
%if %{with postgresql}
BuildRequires:  postgresql-devel
%endif
%if %{have_systemd}
BuildRequires:  systemd
%{?systemd_requires}
%else
# Without systemd we require cron
Requires:       cron
%if 0%{?suse_version}
Requires(post): %insserv_prereq %fillup_prereq
%endif
%endif
# FHS was a hit with sle11 so it dies out otherwise
%if 0%{?suse_version} <= 1110
BuildRequires:  -post-build-checks
%endif
%if 0%{?suse_version} > 1020
BuildRequires:  fdupes
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

%package doc
Summary:        Documentation for CFEngine, a config management framework
Group:          Documentation/Other

%description doc
Documentation for cfengine.

%package examples
Summary:        CFEngine example promises
Group:          Documentation/Other

%description examples
Lots of example promises for CFEngine.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
%if 0%{?suse_version} <= 1110
%patch99 -p1
%endif
%patch10 -p1

##### rpmlint
#### wrong-file-end-of-line-encoding
#### incorrect-fsf-address
### http://www.fsf.org/about/contact/
find ./examples -type f -name "*.cf" -exec perl -p -i -e 's|\r\n|\n|,s|^# Foundation.*|# Foundation, 51 Franklin Street, Suite 500, Boston, MA 02110-1335, USA|' {} \;

### install extra docs
install -d docs
cp -a $RPM_SOURCE_DIR/*pdf docs/

%build
echo %{version} > CFVERSION
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

%if %{have_systemd}
# systemd: install sample cron file in docdir
cp %{SOURCE10} %{buildroot}/%{_docdir}/%{name}
%else
# no systemd -> use cron
# install cron file
install -D -m0644 %{SOURCE10} %{buildroot}/%{_sysconfdir}/cron.d/%{name}
%endif

%if %{have_systemd}
# install systemd scripts
install -d %{buildroot}%{_unitdir}
install -m 0644 %{SOURCE2} %{SOURCE3} %{SOURCE4} %{buildroot}/%{_unitdir}
ln -s -f service %{buildroot}/%{_sbindir}/rccf-monitord
ln -s -f service %{buildroot}/%{_sbindir}/rccf-execd
ln -s -f service %{buildroot}/%{_sbindir}/rccf-serverd
%else
# install init scripts
install -d %{buildroot}%{_initddir}
install -m 0755 %{SOURCE5} %{SOURCE6} %{SOURCE7} %{buildroot}%{_initddir}/
ln -s -f ../..%{_initddir}/cf-monitord %{buildroot}/%{_sbindir}/rccf-monitord
ln -s -f ../..%{_initddir}/cf-execd %{buildroot}/%{_sbindir}/rccf-execd
ln -s -f ../..%{_initddir}/cf-serverd %{buildroot}/%{_sbindir}/rccf-serverd
# sed @workdir@ in initscripts/cron.d
sed -i\
 -e "s,@workdir@,%{workdir},g"\
 -e "s,@basedir@,%{basedir},g" \
 %{buildroot}%{_initddir}/cf-* %{buildroot}%{_sysconfdir}/cron.d/%{name}
%endif

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
%if 0%{?suse_version} > 1020
%fdupes %{buildroot}%{_datadir}/cfengine
%endif

%pre
%if %{have_systemd}
%service_add_pre cf-execd.service cf-monitord.service cf-serverd.service
%endif

%post
%if %{have_systemd}
%service_add_post cf-execd.service cf-monitord.service cf-serverd.service
%else
for i in execd monitord serverd; do
  %fillup_and_insserv cf-${i}
done
%endif
if [ $1 -lt 2 ]; then
  # first install, generate key pair
  cf-key
fi

%preun
%if %{have_systemd}
%service_del_preun cf-execd.service cf-monitord.service cf-serverd.service
%else
for i in execd monitord serverd; do
  %stop_on_removal cf-${i}
done
%endif

%postun
%if %{have_systemd}
%service_del_postun cf-execd.service cf-monitord.service cf-serverd.service
%else
%insserv_cleanup
for i in execd monitord serverd; do
  %restart_on_update cf-${i}
done
%endif
if [ $1 -eq 0 ]; then
  # clean up inputs cache dir on removal
  rm -rf %{basedir}/inputs/*
fi

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
%{_bindir}/cf-serverd
%{_bindir}/cf-upgrade
%{_bindir}/cf-runagent
%{_bindir}/rpmvercmp
%if %{have_systemd}
%{_unitdir}/cf-execd.service
%{_unitdir}/cf-monitord.service
%{_unitdir}/cf-serverd.service
%else
%config %attr(0755,root,root) %{_initddir}/*
%endif
%{_sbindir}/rccf-execd
%{_sbindir}/rccf-monitord
%{_sbindir}/rccf-serverd
%if %{with_sfw2}
%config %{_sysconfdir}/sysconfig/SuSEfirewall2.d/services/cfengine
%endif
%{_mandir}/man8/*
%dir %{basedir}
%dir %{workdir}
%{workdir}/*
%if %{have_systemd}
%{_docdir}/%{name}/cfengine.cron
%else
%config(noreplace) %{_sysconfdir}/cron.d/%{name}
%endif

%files -n %{libsoname}
%defattr(-,root,root)
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/%{libname}.so.*

%files -n %{libname}-devel
%defattr(-,root,root)
%{_libdir}/%{name}/%{libname}.so

%files doc
%defattr(-,root,root)
%doc docs/*.pdf

%files examples
%defattr(-,root,root)
%doc examples/*cf

%changelog
