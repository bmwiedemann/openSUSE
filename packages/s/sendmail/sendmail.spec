#
# spec file for package sendmail
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


#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif

#
# sysvinit -- build for SysVinit and not for systemd
#
%if %{undefined systemd_requires}
%global		with_sysvinit 1
%endif
%bcond_with     sysvinit
%define libmilter_somajor 1
%define libmilter_sominor 0
%define libmilter_sopatch 1
%define libmilter_soversion %{libmilter_somajor}.%{libmilter_sominor}.%{libmilter_sopatch}
%define libmilter_soname    libmilter.so.%{libmilter_somajor}.%{libmilter_sominor}

Name:           sendmail
BuildRequires:  cyrus-sasl-devel
BuildRequires:  db-devel
BuildRequires:  groff
BuildRequires:  libopenssl-devel
BuildRequires:  m4
BuildRequires:  mailx
BuildRequires:  netcfg
BuildRequires:  openldap2-devel
BuildRequires:  procmail
BuildRequires:  tcpd-devel
BuildRequires:  vacation
%if 0%{?suse_version} > 1140
BuildRequires:  libnsl-devel
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libsystemd)
%endif
URL:            http://www.sendmail.org/
%define         SUBDIRS libsmutil libsmdb sendmail mail.local mailstats makemap praliases rmail smrsh libmilter libsm editmap
Provides:       sendcf
Provides:       sendmail-tls
Provides:       smailcfg
Provides:       smtp_daemon
Requires:       /bin/fuser
Requires:       coreutils
Requires:       filesystem
Requires:       findutils
Requires:       m4
Requires:       make
Requires:       netcfg
Requires:       procmail
%if %{without sysvinit}
Requires(pre):  sysvinit(network)
%else
Requires(pre):  %insserv_prereq
Requires(post): %insserv_prereq
Requires(postun): %insserv_prereq
%endif
%if 0%{?suse_version} >= 1330
Requires(pre):  group(daemon)
Requires(pre):  user(daemon)
Requires(pre):  group(mail)
Requires(pre):  user(mail)
%endif
Requires(post): %fillup_prereq
Requires(post): coreutils
Requires(post): permissions
Requires(post): sed
Requires(posttrans): coreutils
Requires(posttrans): findutils
Requires(posttrans): m4
Requires(verify): permissions
%{?systemd_requires}
Conflicts:      smail postfix postfix-tls
Obsoletes:      sendmail-tls
Version:        8.15.2
Release:        0
Summary:        BSD Sendmail
License:        Sendmail
Group:          Productivity/Networking/Email/Servers
Source0:        ftp://ftp.sendmail.org/pub/sendmail/sendmail.%{version}.tar.gz
Source1:        sendmail-suse.tar.bz2
Source2:        sendmail-rpmlintrc
Source3:        sendmail-client.path
Source4:        sendmail.service
Source5:        sendmail-client.service
Source6:        sendmail.systemd
Source7:        sendmail-client.systemd
# PATCH-FIX-OPENSUSE: Add our m4 extensions and maintenance scripts
Patch0:         sendmail-8.15.2.dif
# PATCH-FIX-OPENSUSE: if select(2) is interrupted the timeout become undefined
Patch1:         sendmail-8.14.7-select.dif
# PATCH-FIX-UPSTREAM: SMTP session reuse bugfix (boo#1162204)
Patch2:         8.15.2.mci.p0
# PATCH-FIX-UPSTREAM: Detect shared libraries
Patch4:         sendmail-8.14.8-m4header.patch
# PATCH-FIX-DEBIAN: systemd socket activation support for libmilter
Patch5:         sendmail-fd-passing-libmilter.patch
Patch6:         sendmail-8.15.2-openssl-1.1.0-fix.patch
Patch7:         sendmail-8.15.2-openssl-1.1.0-ecdhe-fix.patch
# PATCH-FIX-OPENSUSE: make build result reproducible
Patch8:         sendmail-8.15.2-reproducible.patch
# PATCH-FIX-OPENSUSE: The former deprecated macro RES_USE_INET6 is gone with glibc 2.30
Patch9:         sendmail-8.15.2-glibc-2.30.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%global         _sysconfdir	%{_sysconfdir}
%global         _mailcnfdir	%{_sysconfdir}/mail
%global         _localstatedir  %{_localstatedir}
%if 0%{?suse_version} < 1120
%global _libexecdir %{_exec_prefix}/lib
%endif

%description
The "Unix System Administration Handbook" calls sendmail "The most
complex and complete mail delivery system in common use..." .

Ready-made configuration files are included for systems connected by
TCP/IP (with or without a name server) and for systems using UUCP.

'procmail' is used as a local mail agent.

"sendmail" is a trademark of Sendmail, Inc.

%package devel
Summary:        BSD Sendmail Development Kit
Group:          Development/Libraries/Other
Requires:       libmilter%{libmilter_somajor}_%{libmilter_sominor}

%description devel
This package includes libraries and header files for building tools to
access sendmail features.

"sendmail" is a trademark of Sendmail, Inc.

%package -n libmilter%{libmilter_somajor}_%{libmilter_sominor}
Summary:        BSD Sendmail Content Management API (milter)
# To be exact: a MTA with libmilter support *is* required
Group:          System/Libraries
Requires:       smtp_daemon

%description -n libmilter%{libmilter_somajor}_%{libmilter_sominor}
Sendmail's Content Management API (milter) provides third-party programs to
access mail messages as they are being processed by the Mail Transfer Agent
(MTA), allowing them to examine and modify message content and
meta-information. Filtering policies implemented by Milter-conformant filters
may then be centrally configured and composed in an end-user's MTA
configuration file.

"sendmail" is a trademark of Sendmail, Inc.

%package -n libmilter-doc
Summary:        BSD Sendmail Content Management API (milter)
Group:          Documentation/HTML
Requires:       libmilter%{libmilter_somajor}_%{libmilter_sominor}
%if 0%{?suse_version} > 1140
BuildArch:      noarch
%endif

%description -n libmilter-doc
Sendmail's Content Management API (milter) provides third-party programs to
access mail messages as they are being processed by the Mail Transfer Agent
(MTA), allowing them to examine and modify message content and
meta-information. Filtering policies implemented by Milter-conformant filters
may then be centrally configured and composed in an end-user's MTA
configuration file.

"sendmail" is a trademark of Sendmail, Inc.

%package -n sendmail-starttls
Summary:        BSD Sendmail Starttls helper scripts
Group:          Productivity/Networking/Security
Requires:       cyrus-sasl-saslauthd
Requires:       openssl
%if 0%{?suse_version} > 1140
BuildArch:      noarch
%endif

%description -n sendmail-starttls
This package includes the directory layout as well as some useful
helper scripts for better SSL/TLS support.

"sendmail" is a trademark of Sendmail, Inc.

%package -n rmail
Version:        %{version}
Release:        0
Summary:        Rmail of the BSD Sendmail
Group:          Productivity/Networking/Email/Servers

%description -n rmail
Rmail interprets incoming mail received via uucp and passing the
processed mail on to the MTA (e.g. sendmail).

%prep
%setup -n sendmail-%{version}
%patch1 -p0 -b .select
%patch2 -p0 -b .reuse
%patch4 -p0 -b .m4head
%patch5 -p1 -b .fdmilt
if pkg-config --atleast-version=1.1.0 openssl; then
%patch6 -p1 -b .openssl11
%patch7 -p1 -b .ecdhe
fi
%patch0 -p0 -b .p0
%patch8 -p1 -b .reproducible
%patch9 -p0 -b .use_inet6
    tar --strip-components=1 -xf %{S:1} 
    set -f
    cat <<-EOF > file-list
	%%defattr(-,root,root)
%if %{with sysvinit}
	%%ghost %%dir %%attr(1750,root,root)   %{_localstatedir}/run/sendmail
%endif
	%%dir    %%attr(0750,root,root)        %{_localstatedir}/lib/sendmail
	%%attr(0600,root,root)                 %{_localstatedir}/lib/sendmail/statistics
	%%attr(0600,root,root)                 %{_mailcnfdir}/statistics
	%%dir    %%attr(0700,root,root)        %{_localstatedir}/spool/mqueue
	%%dir    %%attr(0700,root,root)        %{_localstatedir}/spool/mqueue/.hoststat
	# Part of filesystem RPM
	# %%dir    %%attr(0770,root,mail)      %{_localstatedir}/spool/clientmqueue
	%%attr(0660,root,mail)                 %{_localstatedir}/spool/clientmqueue/sm-client.st
	%%config %%attr(0644,root,root)        %{_sysconfdir}/permissions.d/sendmail
	%%config %%attr(0644,root,root)        %{_sysconfdir}/permissions.d/sendmail.paranoid
	EOF
    cat <<-EOF > milterversion.c
	#include "libmilter/mfapi.h"
	#include <stdio.h>
	int main()
	{
	     return printf("%d.%d.%d\n",
			   SM_LM_VRS_MAJOR(SMFI_VERSION),
			   SM_LM_VRS_MINOR(SMFI_VERSION),
			   SM_LM_VRS_PLVL(SMFI_VERSION)) > 0 ? 0 : 1;
	}
	EOF
    set +f

%build
%global _lto_cflags %{?_lto_cflags} -ffat-lto-objects
    #
    ID=$(id -u)
    RPM_OPT_FLAGS="%{optflags} -fno-strict-aliasing -D_GNU_SOURCE"
    ARCH_LIB=%{_lib}
    export ARCH_LIB
    gcc $RPM_OPT_FLAGS -I./include -o milterversion milterversion.c
    MILTERVERSION=$(./milterversion)
    test %libmilter_soversion = $MILTERVERSION || exit 1
    sed -ri -e 's/@sm_libmilter_somajor@/%{libmilter_somajor}/' \
	    -e 's/@sm_libmilter_soname@/%{libmilter_soname}/' \
	    -e 's/@sm_libmilter_soversion@/%{libmilter_soversion}/' \
	devtools/Site/site.config.m4
    make clean
    # ingnore vacation (we have our own)
    make %{?_smp_mflags} SUBDIRS="%{SUBDIRS}"

%install
    ID=$(id -u)
    ARCH_LIB=%{_lib}
    export ARCH_LIB
    doc=%{buildroot}%{_defaultdocdir}/sendmail
    if test "$ID" -ne 0 ; then
	mkdir bin
	PATH=${PWD}/bin:$PATH
	(cat > bin/install)<<-EOF
	#!/bin/bash
	argv=""
	while test \$# -gt 0; do
	    case "\$1" in
	    -o) shift 2;;
	    -g) shift 2;;
	    *)  argv="\${argv:+"\$argv "}\$1"
		shift
	    esac
	done
	set -- \$(echo \${argv})
	exec -a install %{_bindir}/install \${1+"\$@"}
	EOF
	chmod 755 bin/install
	type -p install
    fi
    mkdir -p ${doc}
    mkdir -p ${doc}/libmilter
    mkdir -p %{buildroot}/sbin/conf.d
    mkdir -p %{buildroot}%{_bindir}
    mkdir -p %{buildroot}%{_sbindir}
    mkdir -p %{buildroot}%{_mailcnfdir}/certs
    mkdir -p %{buildroot}%{_mailcnfdir}/certs/certs
    mkdir -p %{buildroot}%{_mailcnfdir}/certs/crl
    mkdir -p %{buildroot}%{_mailcnfdir}/certs/private
    mkdir -p %{buildroot}%{_mailcnfdir}/certs/newcerts
    mkdir -p %{buildroot}%{_mailcnfdir}/certs/scripts
    mkdir -p %{buildroot}%{_mailcnfdir}/auth
%if %{with sysvinit}
    mkdir -p %{buildroot}%{_sysconfdir}/init.d
%endif
    mkdir -p %{buildroot}%{_sysconfdir}/pam.d
    mkdir -p %{buildroot}%{_libdir}
    mkdir -p %{buildroot}%{_libexecdir}/sendmail.d/bin
    mkdir -p %{buildroot}%{_datadir}/sendmail
    mkdir -p %{buildroot}%{_includedir}/sm
    mkdir -p %{buildroot}%{_includedir}/sm/os
    chmod 0750 %{buildroot}%{_mailcnfdir}/certs
    chmod 0750 %{buildroot}%{_mailcnfdir}/auth
    mkdir -p %{buildroot}%{_sysconfdir}/permissions.d
    mkdir -p %{buildroot}%{_mandir}/man1
    mkdir -p %{buildroot}%{_mandir}/man5
    mkdir -p %{buildroot}%{_mandir}/man8
    mkdir -p %{buildroot}%{_fillupdir}
%if %{without sysvinit}
    mkdir -p %{buildroot}%{_unitdir}
    mkdir -p %{buildroot}%{_mailcnfdir}/system
%endif
    make \
	DESTDIR=%{buildroot} \
	SUBDIRS="%{SUBDIRS}" \
	EBINDIR=%{_libexecdir}/sendmail.d/bin \
	HFDIR=%{_libexecdir}/sendmail.d \
	MANROOTMAN=%{_mandir}/man \
	MANROOT=%{_mandir}/cat \
	install
    # needed to be able to comple a milter which uses libsm, i.e. amavis-milter
    cd include/sm
    ln -s os/sm_os_linux.h sm_os.h
    cd ../../
    cd include/sm/os
    ln -s sm_os_linux.h sm_os.h
    cd ../../../
    cp -pr include/sm  %{buildroot}%{_includedir}/
    test "$ID" -ne 0 || \
    chown root:root    %{buildroot}%{_mailcnfdir}/submit.cf
    chmod 0644	       %{buildroot}%{_mailcnfdir}/submit.cf
    test "$ID" -ne 0 || \
    chown root:mail    %{buildroot}%{_sbindir}/sendmail
    ln -sf %{_sbindir}/sendmail %{buildroot}%{_prefix}/lib/sendmail
    mv %{buildroot}%{_sbindir}/praliases \
			      %{buildroot}%{_bindir}/praliases
    mkdir -p           %{buildroot}%{_localstatedir}/spool/mqueue/.hoststat
    test "$ID" -ne 0 || \
    chown -R root:root %{buildroot}%{_localstatedir}/spool/mqueue
    chmod 0700         %{buildroot}%{_localstatedir}/spool/mqueue
    chmod 0700         %{buildroot}%{_localstatedir}/spool/mqueue/.hoststat
%if %{with sysvinit}
    mkdir -p           %{buildroot}%{_localstatedir}/run/sendmail
    chmod 1750         %{buildroot}%{_localstatedir}/run/sendmail
%endif
    mkdir -p           %{buildroot}%{_localstatedir}/lib/sendmail
    chmod 0750         %{buildroot}%{_localstatedir}/lib/sendmail
    touch              %{buildroot}%{_localstatedir}/lib/sendmail/statistics
    test "$ID" -ne 0 || \
    chown -R root:root %{buildroot}%{_localstatedir}/lib/sendmail/statistics
    chmod 0600	       %{buildroot}%{_localstatedir}/lib/sendmail/statistics
    ln -sf %{_localstatedir}/lib/sendmail/statistics %{buildroot}%{_mailcnfdir}/statistics
    mkdir -p	       %{buildroot}%{_localstatedir}/spool/clientmqueue
    test "$ID" -ne 0 || \
    chown -R root:mail %{buildroot}%{_localstatedir}/spool/clientmqueue
    chmod 0770         %{buildroot}%{_localstatedir}/spool/clientmqueue
    touch              %{buildroot}%{_localstatedir}/spool/clientmqueue/sm-client.st
    test "$ID" -ne 0 || \
    chown -R root:mail %{buildroot}%{_localstatedir}/spool/clientmqueue/sm-client.st
    chmod 0660         %{buildroot}%{_localstatedir}/spool/clientmqueue/sm-client.st
    chmod 0755         %{buildroot}%{_libexecdir}/sendmail.d
    chmod 0755         %{buildroot}%{_libexecdir}/sendmail.d/bin
    chmod 0644         %{buildroot}%{_libdir}/*.a
    ln -sf %{_bindir}/vacation %{buildroot}%{_libexecdir}/sendmail.d/bin/
    ln -sf %{_bindir}/mail     %{buildroot}%{_libexecdir}/sendmail.d/bin/
    ln -sf %{_bindir}/procmail %{buildroot}%{_libexecdir}/sendmail.d/bin/
    install -m 0644 K* README RELE* doc/op/op.ps sendmail/SECURITY \
                       sendmail/TRACEFLAGS suse/README.SUSE \
                       contrib/{e*,re-*,sm*,passwd*}.pl \
		       contrib/etrn.0 ${doc}
    cat > ${doc}/FAQ.sendmail.html <<-'EOF'
	<html>
	<head>
	<title>Sendmail Frequently Asked Questions</title>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
	</head>
	<body>
	The latest Sendmail Frequently Asked Questions (FAQ) can be found at
	<br>
	<a href="http://www.sendmail.de/sm/open_source/support/support_faq"><b>http://www.sendmail.de/sm/open_source/support/support_faq</b></a>
	</body>
	</html>
	EOF
    GROFF_NO_SGR=1 groff -pe -me -mtty-char -Tlatin1 doc/op/op.me > ${doc}/op.txt
    install -m 0644 smrsh/README ${doc}/README.smrsh
    install -m 0644 libmilter/README ${doc}/README.libmilter
    bzip2 -9f ${doc}/*.ps
    bzip2 -9f ${doc}/*.txt
    bzip2 -9f ${doc}/RELEASE_NOTES
    tar cfC - cf . | tar xfC - %{buildroot}%{_datadir}/sendmail/
    test "$ID" -ne 0 || \
    chown root:root -R	%{buildroot}%{_datadir}/sendmail/
    chmod 0755		%{buildroot}%{_datadir}/sendmail/sh/makeinfo.sh
    rm -f  %{buildroot}%{_datadir}/sendmail/cf/Build
    rm -f  %{buildroot}%{_datadir}/sendmail/cf/README
    rm -f  %{buildroot}%{_datadir}/sendmail/cf/Makefile
    rm -f  %{buildroot}%{_datadir}/sendmail/cf/*.cf
    rm -fr %{buildroot}%{_datadir}/sendmail/*/*~ ${doc}/*~
    find %{buildroot}         "(" -name '*.ldap' -o -name '*.mime' -o \
				  -name '*.mrbl' -o -name '*.util' -o \
				  -name '*.p0'   -o -name '*.auth2' -o \
				  -name '*.dif'  -o -name '*.orig' -o \
				  -name '*.reproducible' ")" -print -delete
    cd suse/
    # etc/aliases and %{_sysconfdir}/aliases.d are in other packages
    #install -m 0644 aliases %{buildroot}%{_sysconfdir}/
    #install -d -m 0750 %{buildroot}%{_sysconfdir}/aliases.d
    install -m 0644 README Makefile mailertable genericstable userdb domaintable \
		    virtusertable access linux.mc linux.submit.mc \
		    linux.nullclient.mc service-nodns.switch \
		    service.switch relay-domains trusted-users \
		    local-host-names %{buildroot}%{_mailcnfdir}/
    install -m 0600 auth-info %{buildroot}%{_mailcnfdir}/auth/
    install -m 0755 sendmail.nissl %{buildroot}%{_sbindir}/
    install -m 0644 permissions %{buildroot}%{_sysconfdir}/permissions.d/sendmail
    install -m 0644 permissions.paranoid %{buildroot}%{_sysconfdir}/permissions.d/sendmail.paranoid
%if %{with sysvinit}
    install -m 0755 rc   %{buildroot}%{_sysconfdir}/init.d/sendmail
%else
    sed -ri '\@/etc/init.d/sendmail@d' %{buildroot}%{_sysconfdir}/permissions.d/sendmail
    sed -ri '\@/etc/init.d/sendmail@d' %{buildroot}%{_sysconfdir}/permissions.d/sendmail.paranoid
%endif
    install -m 0644 smtp %{buildroot}%{_sysconfdir}/pam.d/smtp
    install update.sendmail %{buildroot}%{_libexecdir}/sendmail.d/update
%if 0%{?suse_version} <= 1140
    sed -ri 's/,,//g' %{buildroot}%{_libexecdir}/sendmail.d/update
%endif
    cat > %{buildroot}%{_sbindir}/config.sendmail <<-'EOF'
	#!/bin/bash
	VERBOSE=true exec %{_libexecdir}/sendmail.d/update
	EOF
    chmod 755 %{buildroot}%{_sbindir}/config.sendmail
    install -m 0644 sysconfig.sendmail      %{buildroot}%{_fillupdir}/
    install -m 0644 sysconfig.mail-sendmail %{buildroot}%{_fillupdir}/
    > ${doc}/README.sendmail-local-only
    for m in messages/sendmail-local-only.[a-z][a-z]; do
	l=${m##*.}
	n=${m##*/}
	n=${n%.*}
	cat $m >> ${doc}/README.sendmail-local-only
	echo   >> ${doc}/README.sendmail-local-only
    done
    cd ../
    if test -n "%{buildroot}" ; then
	cat %{buildroot}%{_mailcnfdir}/linux.mc		| \
	sed "s@include(\`@include(\`%{buildroot}@"	| \
	m4 | \
	sed "s@%{buildroot}@@g"	> %{buildroot}%{_sysconfdir}/sendmail.cf
	cat %{buildroot}%{_mailcnfdir}/linux.submit.mc	| \
	sed "s@include(\`@include(\`%{buildroot}@"	| \
	m4 | \
	sed "s@%{buildroot}@@g"	> %{buildroot}%{_mailcnfdir}/submit.cf
	chmod 0644 %{buildroot}%{_sysconfdir}/sendmail.cf
	chmod 0644 %{buildroot}%{_mailcnfdir}/submit.cf
    else
	m4 < %{_mailcnfdir}/linux.mc		> %{_sysconfdir}/sendmail.cf
	m4 < %{_mailcnfdir}/linux.submit.mc	> %{_mailcnfdir}/submit.cf
	chmod 0644 %{_sysconfdir}/sendmail.cf
	chmod 0644 %{_mailcnfdir}/submit.cf
    fi
%if %{with sysvinit}
    ln -sf %{_sysconfdir}/init.d/sendmail %{buildroot}%{_sbindir}/rcsendmail
%else
    ln -sf %{_sbindir}/service %{buildroot}%{_sbindir}/rcsendmail
    ln -sf %{_sbindir}/service %{buildroot}%{_sbindir}/rcsendmail-client
%endif
    ln -sf ../aliases  %{buildroot}%{_mailcnfdir}/aliases
    pushd %{buildroot}%{_mailcnfdir}/
	OPATH=$PATH
	PATH="${OPATH}:%{buildroot}%{_sbindir}:%{buildroot}%{_bindir}"
	make DESTDIR=%{buildroot} short
	PATH=$OPATH
    popd
%if %{without sysvinit}
    #
    # systemd unit conf files
    install -m 0644 %{S:3} %{buildroot}%{_unitdir}/
    install -m 0644 %{S:4} %{buildroot}%{_unitdir}/
    install -m 0644 %{S:5} %{buildroot}%{_unitdir}/
    install -m 0644 %{S:6} %{buildroot}%{_mailcnfdir}/system/sm.pre
    install -m 0644 %{S:7} %{buildroot}%{_mailcnfdir}/system/sm-client.pre
    chmod 0755 %{buildroot}%{_mailcnfdir}/system/sm.pre
    chmod 0755 %{buildroot}%{_mailcnfdir}/system/sm-client.pre
%endif
    #
    # Documentation for libmilter
    #
    install -m 0644 libmilter/docs/* ${doc}/libmilter/

    #
    # Remove some files we don't wish to package
    #
    rm -f %{buildroot}%{_sysconfdir}/aliases %{buildroot}%{_mailcnfdir}/*.db
    rm -f %{buildroot}%{_mailcnfdir}/*/*.db

%clean
rm -rf %{buildroot}

%if %{defined verify_permissions}
%verifyscript
%if %{with sysvinit}
%verify_permissions -e %{_localstatedir}/run/sendmail/
%endif
%verify_permissions -e %{_localstatedir}/spool/mqueue/
%verify_permissions -e %{_sysconfdir}/sendmail.cf
%if %{with sysvinit}
%verify_permissions -e %{_sysconfdir}/init.d/sendmail
%endif
%verify_permissions -e %{_mailcnfdir}/auth/
%verify_permissions -e %{_mailcnfdir}/certs/
%verify_permissions -e %{_libexecdir}/sendmail.d/bin/
%verify_permissions -e %{_libexecdir}/sendmail.d/bin/mail.local
%verify_permissions -e %{_libexecdir}/sendmail.d/bin/smrsh
%verify_permissions -e %{_sbindir}/sendmail
%endif

%post
# Trigger rebuild of old db's
for db in /etc/aliases.db /etc/aliases.d/*.db /etc/mail/*.db /etc/mail/*/*.db ; do
  test -e "$db"       || continue
  test -e "${db%.db}" || continue
  touch "${db%.db}"
done
# Update from newer SUSE releases or new installation
if test -f /etc/sysconfig/mail ; then
  . /etc/sysconfig/mail
fi
# Edit older configuration files
if test -s /etc/sysconfig/sendmail ; then
  sed -ri '\@^##[[:space:]]+Type:@,\@^#[[:space:]]+@ {
    \@^##[[:space:]]+Command:@b skip
    \@# enable this to change also the recipient address\.@i\
## Command:     /usr/lib/sendmail.d/update
    \@^#[[:space:]]*$@i\
## Command:     /usr/lib/sendmail.d/update
    :skip
    N
  }' /etc/sysconfig/sendmail
fi
%{fillup_only -an mail}
%if %{with sysvinit}
%{fillup_and_insserv -nY sendmail sendmail}
%else
%{fillup_only -an sendmail}
%service_add_post sendmail.service sendmail-client.service sendmail-client.path
PATH=bin:usr/bin:$PATH
if type -p systemctl > /dev/null 2>&1 ; then
  systemctl enable sendmail.service >/dev/null 2>&1 || :
  systemctl enable sendmail-client.service >/dev/null 2>&1 || :
  systemctl enable sendmail-client.path >/dev/null 2>&1 || :
fi
%endif
%if %{defined set_permissions}
%if %{with sysvinit}
%set_permissions %{_localstatedir}/run/sendmail/
%endif
%set_permissions %{_localstatedir}/spool/mqueue/
%set_permissions %{_sysconfdir}/sendmail.cf
%if %{with sysvinit}
%set_permissions %{_sysconfdir}/init.d/sendmail
%endif
%set_permissions %{_mailcnfdir}/auth/
%set_permissions %{_mailcnfdir}/certs/
%set_permissions %{_libexecdir}/sendmail.d/bin/
%set_permissions %{_libexecdir}/sendmail.d/bin/mail.local
%set_permissions %{_libexecdir}/sendmail.d/bin/smrsh
%set_permissions %{_sbindir}/sendmail
%endif

%if ! %{with sysvinit}
%pre
%service_add_pre sendmail.service sendmail-client.service sendmail-client.path
%endif

%preun
%if %{with sysvinit}
%{stop_on_removal sendmail}
%else
%service_del_preun sendmail.service sendmail-client.service sendmail-client.path
%endif

%postun
if test $1 = 0; then
%if %{with sysvinit}
    %{restart_on_update sendmail}
%endif
    rm -rf %{_localstatedir}/lib/sendmail
    exit 0
fi
%if ! %{with sysvinit}
%service_del_postun sendmail.service sendmail-client.service sendmail-client.path
%else
%{insserv_cleanup}
%endif

%posttrans
if test -x %{_libexecdir}/sendmail.d/update ; then
    VERBOSE=false %{_libexecdir}/sendmail.d/update
fi

%post -n libmilter%{libmilter_somajor}_%{libmilter_sominor} -p /sbin/ldconfig
%postun -n libmilter%{libmilter_somajor}_%{libmilter_sominor} -p /sbin/ldconfig

%files -f file-list
%defattr(-,root,root)
%dir %{_mailcnfdir}
# %{_sysconfdir}/aliases.d is part of aaa_dir
# %dir %attr(0750,root,mail) %{_sysconfdir}/aliases.d
%dir %attr(0750,root,root) %{_mailcnfdir}/auth
%dir %attr(0750,root,root) %{_mailcnfdir}/certs
%if %{without sysvinit}
%dir %attr(0750,root,root) %{_mailcnfdir}/system
%endif
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/sendmail.cf
# %{_sysconfdir}/aliases is part of netcfg
# %config(noreplace) %{_sysconfdir}/aliases
%doc               %{_mailcnfdir}/README
%config(noreplace) %{_mailcnfdir}/Makefile
# this is a link
%config(noreplace) %{_mailcnfdir}/aliases
%config(noreplace) %verify(not md5 size mtime) %attr(0600,root,root) %{_mailcnfdir}/auth/auth-info
%config(noreplace) %verify(not md5 size mtime) %{_mailcnfdir}/linux.mc
%config(noreplace) %verify(not md5 size mtime) %{_mailcnfdir}/linux.submit.mc
%config(noreplace) %verify(not md5 size mtime) %{_mailcnfdir}/linux.nullclient.mc
%config(noreplace) %verify(not md5 size mtime) %{_mailcnfdir}/mailertable
%config(noreplace) %verify(not md5 size mtime) %{_mailcnfdir}/genericstable
%config(noreplace) %verify(not md5 size mtime) %{_mailcnfdir}/domaintable
%config(noreplace) %verify(not md5 size mtime) %{_mailcnfdir}/virtusertable
%config(noreplace) %verify(not md5 size mtime) %{_mailcnfdir}/access
%config(noreplace) %verify(not md5 size mtime) %{_mailcnfdir}/userdb
%config(noreplace) %verify(not md5 size mtime) %{_mailcnfdir}/relay-domains
%config(noreplace) %{_mailcnfdir}/service.switch
%config(noreplace) %{_mailcnfdir}/service-nodns.switch
%config(noreplace) %verify(not md5 size mtime) %{_mailcnfdir}/trusted-users
%config(noreplace) %verify(not md5 size mtime) %{_mailcnfdir}/local-host-names
%config(noreplace) %verify(not md5 size mtime) %{_mailcnfdir}/submit.cf
%doc %{_defaultdocdir}/sendmail
%exclude %{_defaultdocdir}/sendmail/README.libmilter
%exclude %dir %{_defaultdocdir}/sendmail/libmilter
%exclude %{_defaultdocdir}/sendmail/libmilter/*
%{_datadir}/sendmail
%{_fillupdir}/sysconfig.sendmail
%{_fillupdir}/sysconfig.mail-sendmail
%config %attr(0644,root,root) %{_sysconfdir}/pam.d/smtp
%if %{with sysvinit}
%config %attr(0744,root,root) %{_sysconfdir}/init.d/sendmail
%endif
%attr(0755,root,root) %{_libexecdir}/sendmail.d/update
%attr(0755,root,root) %{_sbindir}/config.sendmail
%if %{without sysvinit}
%config %attr(0644,root,root) %{_unitdir}/sendmail-client.path
%config %attr(0644,root,root) %{_unitdir}/sendmail.service
%config %attr(0644,root,root) %{_unitdir}/sendmail-client.service
%config %attr(0755,root,root) %{_mailcnfdir}/system/sm.pre
%config %attr(0755,root,root) %{_mailcnfdir}/system/sm-client.pre
%endif
%{_bindir}/hoststat
%{_bindir}/mailq
%{_bindir}/newaliases
%{_bindir}/praliases
%{_bindir}/purgestat
#%{_bindir}/rmail
%{_prefix}/lib/sendmail
%dir %attr(0755,root,root) %{_libexecdir}/sendmail.d/
%dir %attr(0755,root,root) %{_libexecdir}/sendmail.d/bin/
%{_libexecdir}/sendmail.d/bin/mail
%attr(0511,root,root) %{_libexecdir}/sendmail.d/bin/mail.local
%{_libexecdir}/sendmail.d/bin/procmail
%attr(0511,root,root) %{_libexecdir}/sendmail.d/bin/smrsh
%{_libexecdir}/sendmail.d/bin/vacation
%{_libexecdir}/sendmail.d/helpfile
%doc %{_mandir}/man1/mailq.1.gz
%doc %{_mandir}/man1/newaliases.1.gz
%doc %{_mandir}/man5/aliases.5.gz
%doc %{_mandir}/man8/editmap.8.gz
%doc %{_mandir}/man8/makemap.8.gz
#%doc %{_mandir}/man8/rmail.8.gz
%doc %{_mandir}/man8/sendmail.8.gz
%doc %{_mandir}/man8/smrsh.8.gz
%doc %{_mandir}/man8/mail.local.8.gz
%doc %{_mandir}/man8/mailstats.8.gz
%doc %{_mandir}/man8/praliases.8.gz
%{_sbindir}/editmap
%{_sbindir}/mailstats
%{_sbindir}/makemap
# Should we do 6555??
%attr(2555,root,mail) %{_sbindir}/sendmail
%{_sbindir}/sendmail.nissl
%{_sbindir}/rcsendmail*

%files devel
%defattr(-,root,root)
%dir %{_includedir}/libmilter
%{_includedir}/libmilter/*.h
%dir %{_includedir}/sm
%{_includedir}/sm/*.h
%dir %{_includedir}/sm/os
%{_includedir}/sm/os/*.h
%{_libdir}/libmilter.a
%{_libdir}/libmilter.so
%{_libdir}/libsmutil.a
%{_libdir}/libsm.a

%files -n libmilter%{libmilter_somajor}_%{libmilter_sominor}
%defattr(-,root,root)
%{_libdir}/libmilter.so.*
%doc %{_defaultdocdir}/sendmail/README.libmilter

%files -n libmilter-doc
%defattr(-,root,root)
%dir %doc %{_defaultdocdir}/sendmail/libmilter/
%doc %{_defaultdocdir}/sendmail/libmilter/*

%files -n sendmail-starttls
%defattr(-,root,root)
%dir %attr(0700,root,root) %{_mailcnfdir}/certs/certs/
%dir %attr(0700,root,root) %{_mailcnfdir}/certs/crl/
%dir %attr(0700,root,root) %{_mailcnfdir}/certs/private/
%dir %attr(0700,root,root) %{_mailcnfdir}/certs/newcerts/
%dir %attr(0700,root,root) %{_mailcnfdir}/certs/scripts/

%files -n rmail
%defattr(-,root,root)
%{_bindir}/rmail
%doc %{_mandir}/man8/rmail.8.gz

%changelog
