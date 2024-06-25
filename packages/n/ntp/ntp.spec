#
# spec file for package ntp
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


#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif

%define ntpfaqversion 3.4
Name:           ntp
Version:        4.2.8p17
Release:        0
Summary:        Network Time Protocol daemon (version 4)
License:        BSD-3-Clause AND MIT AND BSD-4-Clause AND GPL-2.0-only
Group:          Productivity/Networking/Other
URL:            http://www.ntp.org/
# main source
Source0:        http://www.eecis.udel.edu/~ntp/ntp_spool/ntp4/ntp-4.2/ntp-%{version}.tar.gz
# configuration
Source1:        conf.logrotate.ntp
Source2:        conf.ntp.conf
Source3:        conf.ntpd.service
Source4:        conf.sysconfig.ntp
Source5:        conf.sysconfig.syslog-ntp
Source6:        conf.ntp.reg
Source8:        conf.start-ntpd
Source9:        conf.ntp-wait.service
# documentation
Source10:       NTP-FAQ-%{ntpfaqversion}.tar.bz2
Source12:       README.SUSE
Source13:       ntptime.8.gz
Source16:       ntp.NetworkManager
Patch1:         ntp-segfault_on_invalid_device.patch
Patch10:        ntp-strcat.patch
Patch11:        ntp-4.2.6p2-seed_file.patch
Patch15:        bnc#506908.diff
Patch16:        MOD_NANO.diff
Patch18:        bnc#574885.diff
Patch23:        ntp-openssl-version.patch
Patch27:        ntp-netlink.patch
Patch29:        ntp-pathfind.patch
Patch30:        ntp-move-kod-file.patch
Patch33:        ntp-sntp-libevent.patch
Patch34:        testdcf-gude.diff
Patch35:        ntp-clarify-interface.patch
Patch36:        Get-rid-of-EVP_MD_CTX_FLAG_NON_FIPS_ALLOW.patch

BuildRequires:  avahi-compat-mDNSResponder-devel
BuildRequires:  fdupes
BuildRequires:  libcap-devel
BuildRequires:  libevent-devel
BuildRequires:  openssl-devel
%if 0%{?suse_version} > 1320 || 0%{?sle_version} >= 120200
BuildRequires:  pps-tools-devel
%endif
BuildRequires:  readline-devel
BuildRequires:  systemd-rpm-macros
%systemd_ordering
Requires:       /bin/logger
Requires:       timezone
Requires(pre):  %fillup_prereq
Requires(pre):  user(ntp)
Requires(post): /usr/bin/base64
Requires(post): /usr/bin/gawk
Suggests:       logrotate
Provides:       ntp-daemon
Provides:       xntp = %{version}
Provides:       xntp3 = %{version}
Obsoletes:      xntp < %{version}
Obsoletes:      xntp3 < %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Conflicts:      openntpd

%description
The Network Time Protocol (NTP) is used to synchronize the time of a
computer client or server to another server or reference time source,
such as a radio, satellite receiver, or modem.

Ntpd is an operating system daemon that sets and maintains the system
time-of-day synchronized with Internet standard time servers.

%package doc
Summary:        Additional Package Documentation for ntp
Group:          Documentation/Other
Provides:       ntpdoc = %{version}
Provides:       xntp-doc = %{version}
Provides:       xntpdoc = %{version}
Obsoletes:      ntpdoc < %{version}
Obsoletes:      xntp-doc < %{version}
Obsoletes:      xntpdoc < %{version}

%description doc
The complete set of documentation for building and configuring an NTP
server or client. The documentation is in the form of HTML files
suitable for browsing and contains links to additional documentation at
various web sites.

What about NTP? Understanding and using the Network Time Protocol (A
first try on a non-technical Mini-HOWTO and FAQ on NTP). Edited by
Ulrich Windl and David Dalton.

%package dcf77-tools
Summary:        DCF77 related tools
Group:          Hardware/Other

%description dcf77-tools
DCF77 related programs.

There are currently two tools:
  * testdcf, a simple DCF77 raw impulse test program.
  * dcfd, a simple DCF77 raw impulse receiver with NTP loopfilter
    mechanics for synchronisation.

%prep
%setup -q
# unpack ntp-faq
tar -x -C html -j -f %{SOURCE10}
%patch -P 1
# copy README.SUSE
cp %{SOURCE12} .
%patch -P 10 -p1
%patch -P 11 -p1
%patch -P 15
%patch -P 16
%patch -P 18
%patch -P 23
%patch -P 27
%patch -P 29
%patch -P 30
%patch -P 33
%patch -P 34 -p1
%patch -P 35
%patch -P 36 -p1

# fix DOS line breaks
sed -i 's/\r//g' html/scripts/{footer.txt,style.css}

%build
export RPM_OPT_FLAGS="$RPM_OPT_FLAGS -W -DOPENSSL_LOAD_CONF -Wall -Wstrict-prototypes -Wpointer-arith -Wno-unused-parameter -fno-strict-aliasing -fstack-protector"
%ifarch alpha s390x
export RPM_OPT_FLAGS="$RPM_OPT_FLAGS -O0"
%endif
%ifarch ia64
RPM_OPT_FLAGS="$RPM_OPT_FLAGS -ffast-math"
%endif
export CFLAGS="$RPM_OPT_FLAGS -fPIE"
export LDFLAGS="-pie"
%configure \
	--with-binsubdir=bin \
	--bindir=%{_sbindir} \
	--htmldir=%{_docdir}/ntp-doc \
	--disable-debugging \
	--enable-parse-clocks \
	--enable-all-clocks \
	--enable-linuxcaps \
	--enable-ipv6 \
	--with-sntp \
	--enable-ntp-signd \
	--disable-listen-read-drop \
	--with-lineeditlibs=readline \
	--with-crypto=openssl \
	--with-openssl-libdir=%{_libdir} \
	--with-openssl-incdir=%{_includedir} \
	--disable-thread-support \
	--without-threads \
	--enable-leap-smear \
	--enable-ntp-signd

%make_build

%install
%make_install
# Change permissions
chmod 644 html/pic/neoclock4x.gif
%fdupes -s html
#
# default configuration
#
install -d %{buildroot}%{_localstatedir}/lib/ntp/{drift,etc,var/{lib,run/ntp},dev}
install -d %{buildroot}%{_localstatedir}/run
ln -s ../.. %{buildroot}%{_localstatedir}/lib/ntp%{_localstatedir}/lib/ntp
install -m 644 -D %{SOURCE1} %{buildroot}%{_sysconfdir}/logrotate.d/ntp
install -m 600 -D %{SOURCE2} %{buildroot}%{_sysconfdir}/ntp.conf
install -m 600 -D %{SOURCE2} %{buildroot}%{_localstatedir}/lib/ntp%{_sysconfdir}/ntp.conf.iburst
#
# boot scripts
#
install -m 0644 -D %{SOURCE3} %{buildroot}/%{_unitdir}/ntpd.service
install -m 0644 -D %{SOURCE9} %{buildroot}/%{_unitdir}/ntp-wait.service
install -d %{buildroot}%{_prefix}/sbin
install -m 755 -D %{SOURCE8} %{buildroot}%{_sbindir}/start-ntpd
#
# fillup sysconfig.ntp
#
install -m 644 -D %{SOURCE4} %{buildroot}%{_fillupdir}/sysconfig.ntp
install -m 644 -D %{SOURCE5} %{buildroot}%{_fillupdir}/sysconfig.syslog-ntp
#
# install SLP reg file
#
install -m 644 -D %{SOURCE6} %{buildroot}%{_sysconfdir}/slp.reg.d/ntp.reg
#
# Install NetworkManager hook
#
install -m 755 -D %{SOURCE16} %{buildroot}%{_sysconfdir}/NetworkManager/dispatcher.d/ntp
#
# man pages
#
install -m 644 %{S:13} %{buildroot}/%{_mandir}/man8
#
# Logfile
#
install -d %{buildroot}%{_localstatedir}/log/
touch %{buildroot}%{_localstatedir}/log/ntp
#
# statsdir
#
install -d %{buildroot}%{_localstatedir}/log/ntpstats
#
# service xml
#
install -m 755 scripts/ntp-wait/ntp-wait %{buildroot}%{_sbindir}/
install -d %{buildroot}/var/lib/ntp
install -m 644 /dev/null %{buildroot}/var/lib/ntp/kod

#
# DCF77 tools
#
install -d %{buildroot}%{_bindir}/
install -m 755 parseutil/testdcf %{buildroot}%{_bindir}/
install -m 755 parseutil/dcfd %{buildroot}%{_bindir}/

%pre
test -L %{_localstatedir}/run/ntp  || rm -rf %{_localstatedir}/run/ntp && :
%service_add_pre ntp.service ntpd.service
%service_add_pre ntp-wait.service
if [ $1 -ne 1 -a ! -e "%{_localstatedir}/lib/systemd/migrated/ntpd" -a -e %{_localstatedir}/lib/systemd/sysv-convert/database ]; then
  sed -i -e 's,ntp\t,ntpd\t,g' %{_localstatedir}/lib/systemd/sysv-convert/database
fi

%preun
%service_del_preun ntpd.service
%service_del_preun ntp-wait.service

# no update? Then remove these files that aren't owned by the package
if [ $1 -eq 0 ]; then
     test -e %{_localstatedir}/lib/ntp/drift/ntp.drift  && rm -f %{_localstatedir}/lib/ntp/drift/ntp.drift
     rm -f %{_localstatedir}/lib/ntp%{_sysconfdir}/* 2>/dev/null
     test -e %{_localstatedir}/log/ntp  && rm -f %{_localstatedir}/log/ntp
fi

%post -p /bin/bash

getntpconf() {
  # Get the value of a single-value ntp.conf directive, first match wins.
  awk 'NF >= 2 && $1 == option { print $2; exit } ' "option=$1" $NTPCONF
}

keyexists() {
  # Check whether a key with the given ID exists in the ntp keys file.
  awk '$1 == keyno {found = 1} END {exit !found}' "keyno=$1" $KEYSFILE
}

add_trustedkey() {
  # Merge the given key ID into the trustedkey directive.
  # Add the directive if it does not yet exist.
  FILE=$(mktemp -p /etc)
  gawk '
    NF >= 2 && $1 == "trustedkey" {
      n = split($0, a)
      for (i = 1; i <= n; i++) {
        if (a[i] == newkey) newkey = "";
        if (a[i] ~ /^#/ && newkey) {
          $(++j) = newkey; newkey = ""
        }
        $(++j) = a[i];
      }
      if (newkey) { $(++j) = newkey; newkey = "" }
    }
    { print }
    ENDFILE {
      if (newkey) { print "trustedkey", newkey }
    }
  ' "newkey=$1" $NTPCONF > $FILE
  if ! cmp --quiet $FILE $NTPCONF; then
     cat $FILE > $NTPCONF
  fi
  rm $FILE
}

NTPCONF=/etc/ntp.conf
KEYSFILE=$(getntpconf keys)
if test -z "$KEYSFILE"; then
  KEYSFILE=/etc/ntp.keys
  echo "keys $KEYSFILE" >> $NTPCONF
fi

if [ ! -f $KEYSFILE ]; then
  FILE=$(mktemp -p /etc)
  chmod 0640 $FILE
  chown root:ntp $FILE
  mv -Z $FILE $KEYSFILE
fi

CONTROLKEY=$(getntpconf controlkey)
REQUESTKEY=$(getntpconf requestkey)

if test -z "$CONTROLKEY"; then
  if test -n "$REQUESTKEY"; then
    CONTROLKEY=$REQUESTKEY
  else
    for (( CONTROLKEY = 1; CONTROLKEY < 65535; CONTROLKEY++ )); do
      keyexists $CONTROLKEY || break
    done
  fi
  echo "controlkey $CONTROLKEY" >> $NTPCONF
fi

if test -z "$REQUESTKEY"; then
  REQUESTKEY=$CONTROLKEY;
  echo "requestkey $REQUESTKEY" >> $NTPCONF
fi

for KEYNO in $REQUESTKEY $CONTROLKEY; do
  if ! keyexists $KEYNO; then
    KEY=$(head -c 15 /dev/urandom | base64)
    echo "$KEYNO SHA1 $KEY" >> $KEYSFILE
  fi
done

add_trustedkey $REQUESTKEY
add_trustedkey $CONTROLKEY

# update from previous permissions
if [ -f %{_sysconfdir}/ntp.conf ]; then
  chown root:ntp %{_sysconfdir}/ntp.conf
fi
if [ -f %{_sysconfdir}/ntp.keys ]; then
  chown root:ntp %{_sysconfdir}/ntp.keys
fi
if [ -f %{_localstatedir}/lib/ntp%{_sysconfdir}/ntp.conf.iburst ]; then
  chown --from=ntp:root root:ntp %{_localstatedir}/lib/ntp%{_sysconfdir}/ntp.conf.iburst
fi
%{fillup_only -n ntp }
%{fillup_only -n syslog }
if [ ! -f %{_localstatedir}/log/ntp ]; then
	touch %{_localstatedir}/log/ntp
	chmod 644 %{_localstatedir}/log/ntp
fi
%service_add_post ntpd.service
%service_add_post ntp-wait.service
if [ -e "%{_localstatedir}/lib/systemd/migrated/ntp" ]; then
  mv "%{_localstatedir}/lib/systemd/migrated/ntp" "%{_localstatedir}/lib/systemd/migrated/ntpd"
fi

%postun
%service_del_postun ntpd.service
%service_del_postun ntp-wait.service

%files
%license COPYRIGHT
%doc ChangeLog NEWS README* TODO WHERE-TO-START conf
%attr(0640,root,ntp) %config(noreplace) %{_sysconfdir}/ntp.conf
%dir %{_sysconfdir}/slp.reg.d
%{_unitdir}/ntpd.service
%{_unitdir}/ntp-wait.service
%config(noreplace) %{_sysconfdir}/slp.reg.d/ntp.reg
%config %{_sysconfdir}/logrotate.d/ntp
# own /etc/NetworkManager so we don't have to BuildDepend on NM
%dir %{_sysconfdir}/NetworkManager
%dir %{_sysconfdir}/NetworkManager/dispatcher.d
%config %{_sysconfdir}/NetworkManager/dispatcher.d/ntp
%{_sbindir}/*
%{_datadir}/ntp
%if 0%{?suse_version} <= 1310
/usr/lib/initscripts
%endif
%{_localstatedir}/lib/ntp/*
%attr(0640,root,ntp) %config(noreplace) %{_localstatedir}/lib/ntp%{_sysconfdir}/ntp.conf.iburst
%attr(0755,ntp,ntp) %dir %{_localstatedir}/lib/ntp/drift
%{_mandir}/man1/*
%{_mandir}/man5/*
%{_mandir}/man8/*
%{_fillupdir}/*
%attr(0775,ntp,root) %{_localstatedir}/lib/ntp%{_localstatedir}/run/ntp
%ghost %config(noreplace) %{_localstatedir}/log/ntp
%attr(0755,ntp,ntp) %dir %{_localstatedir}/log/ntpstats

%files doc
%doc %{_docdir}/ntp-doc

%files dcf77-tools
%{_bindir}/dcfd
%{_bindir}/testdcf

%changelog
