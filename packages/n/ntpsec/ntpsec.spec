#
# spec file for package ntpsec
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2016 Malcolm J Lewis <malcolmlewis@opensuse.org>
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


Name:           ntpsec
Version:        1.1.9
Release:        0
Summary:        Improved implementation of Network Time Protocol
License:        BSD-2-Clause AND NTP AND BSD-3-Clause AND MIT
URL:            https://www.ntpsec.org/
Source0:        ftp://ftp.ntpsec.org/pub/releases/%{name}-%{version}.tar.gz
Source1:        ftp://ftp.ntpsec.org/pub/releases/%{name}-%{version}.tar.gz.asc
Source3:        %{name}.changes
Source4:        logrotate.ntp
Source8:        ntp.conf
BuildRequires:  asciidoc
BuildRequires:  avahi-compat-mDNSResponder-devel
BuildRequires:  bison
BuildRequires:  fdupes
# Needed for waf init in the git snapshot
BuildRequires:  git-core
BuildRequires:  libcap-devel
BuildRequires:  libxslt-tools
# Required for tests to pass
BuildRequires:  netcfg
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  pps-tools-devel
BuildRequires:  python3-curses
BuildRequires:  python3-gpsd
BuildRequires:  pkgconfig(libbsd)
BuildRequires:  pkgconfig(libevent)
BuildRequires:  pkgconfig(libseccomp)
BuildRequires:  pkgconfig(python3)
Requires:       netcfg
Requires:       ntpsec-utils
Requires(pre):  shadow
Recommends:     logrotate
# For ntpleapfetch
Recommends:     wget
Conflicts:      ntp-daemon
Provides:       ntp-daemon

%description
A more secure implementation of NTP, derived from NTP Classic, Dave
Mills’s original.

%package -n python3-ntp
Summary:        Python ntpsec bindings

%description -n python3-ntp
The ntpsec python bindings used by various ntp utilities.

%package utils
Summary:        Utilities and commands for ntp
Requires:       %{name} = %{version}
# For ntpmon
Requires:       python3-curses
# For ntploggps
Requires:       python3-gpsd
Requires:       python3-ntp
# For ntpviz
Recommends:     python3-psutil
# Same binaries
Conflicts:      ntp

%description utils
The ntpsec utilities relying on the python module of ntp

%package doc
Summary:        Documentation for %{name}

%description doc
Documentation files generated from asciidoc for %{name}.

%prep
%setup -q
# Fix python shebangs
sed -i -e 's:#!%{_bindir}/env python:#!%{_bindir}/python3:' \
    ntpclients/*
# there is no actual reason for 3.18 gpsd version
sed -i -e 's:, condition="ver >= num(3, 18)"::' \
    pylib/wscript

%build
# We use the date from the changes file
epoch=`date --date "@\`stat --format %%Y %{SOURCE3}\`" +"%%s"`

%global _lto_cflags %{nil}
export CFLAGS="%{optflags}"
export CCFLAGS="%{optflags}"
python3 ./waf configure \
    --build-epoch="$epoch" \
    --enable-debug \
    --enable-doc --htmldir=%{_docdir}/ntpsec/html \
    --prefix=%{_prefix} \
    --mandir="%{_mandir}" \
    --python=%{_bindir}/python3 \
    --pythonarchdir=%{python3_sitearch} \
    --pythondir=%{python3_sitearch} \
    --sbindir=%{_sbindir} \
    --bindir=%{_bindir} \
    --enable-seccomp \
    --enable-debug-gdb \
    --enable-early-droproot \
    --enable-leap-smear \
    --enable-mssntp \
    --refclock=all
python3 ./waf build --verbose %{?_smp_mflags}

%install
python3 ./waf install --destdir=%{buildroot}

# Use correct path in unit file

ln -s service %{buildroot}%{_sbindir}/rcntpd
ln -s service %{buildroot}%{_sbindir}/rcntplogtemp
ln -s service %{buildroot}%{_sbindir}/rcntpviz-daily
ln -s service %{buildroot}%{_sbindir}/rcntpviz-weekly
ln -s service %{buildroot}%{_sbindir}/rcntp-wait

install -pm 0644 -D %{SOURCE4} %{buildroot}%{_sysconfdir}/logrotate.d/ntp
install -pm 0644 -D %{SOURCE8} %{buildroot}%{_sysconfdir}/ntp.conf

%fdupes -s %{buildroot}

%check
python3 ./waf check --verbose %{?_smp_mflags}

%pre
getent group ntp >/dev/null || groupadd -r ntp
getent passwd ntp >/dev/null || useradd -u 74 -r -g ntp -d %{_localstatedir}/lib/ntp -s /sbin/nologin -c "NTP daemon" ntp
%service_add_pre ntp.service ntpd.service
exit 0

%pre utils
%service_add_pre ntp-wait.service ntplogtemp.service ntpviz-daily.service ntpviz-weekly.service

%post
%service_add_post ntpd.service

%post utils
%service_add_post ntp-wait.service ntplogtemp.service ntpviz-daily.service ntpviz-weekly.service

%preun
%service_del_preun ntpd.service

%preun utils
%service_del_preun ntp-wait.service ntplogtemp.service ntpviz-daily.service ntpviz-weekly.service

%postun
%service_del_postun ntpd.service

%postun utils
%service_del_postun ntp-wait.service ntplogtemp.service ntpviz-daily.service ntpviz-weekly.service

%files -n python3-ntp
%{python3_sitearch}/ntp*

%files utils
%{_bindir}/ntploggps
%{_bindir}/ntpdig
%{_bindir}/ntpkeygen
%{_bindir}/ntpmon
%{_bindir}/ntpq
%{_bindir}/ntpsweep
%{_bindir}/ntptrace
%{_bindir}/ntpviz
%{_bindir}/ntpwait
%{_bindir}/ntplogtemp
%{_bindir}/ntpsnmpd
%{_mandir}/man1/ntploggps.1%{?ext_man}
%{_mandir}/man1/ntpdig.1%{?ext_man}
%{_mandir}/man8/ntpkeygen.8%{?ext_man}
%{_mandir}/man1/ntpmon.1%{?ext_man}
%{_mandir}/man1/ntpq.1%{?ext_man}
%{_mandir}/man1/ntpsweep.1%{?ext_man}
%{_mandir}/man1/ntptrace.1%{?ext_man}
%{_mandir}/man1/ntpviz.1%{?ext_man}
%{_mandir}/man8/ntpwait.8%{?ext_man}
%{_mandir}/man1/ntplogtemp.1%{?ext_man}
%{_mandir}/man8/ntpsnmpd.8%{?ext_man}
%{_sbindir}/rcntp-wait
%{_sbindir}/rcntplogtemp
%{_sbindir}/rcntpviz-daily
%{_sbindir}/rcntpviz-weekly
%{_unitdir}/ntp-wait.service
%{_unitdir}/ntplogtemp.*
%{_unitdir}/ntpviz-*

%files doc
%dir %{_docdir}/%{name}/html
%doc %{_docdir}/%{name}/html/*

%files
%license LICENSE.adoc
%doc NEWS.adoc README.adoc
%config(noreplace) %{_sysconfdir}/ntp.conf
%{_sbindir}/rcntpd
%{_bindir}/ntpfrob
%{_bindir}/ntpleapfetch
%{_bindir}/ntptime
%{_sbindir}/ntpd
%{_mandir}/man5/ntp.conf.5%{?ext_man}
%{_mandir}/man5/ntp.keys.5%{?ext_man}
%{_mandir}/man8/ntpd.8%{?ext_man}
%{_mandir}/man8/ntpfrob.8%{?ext_man}
%{_mandir}/man8/ntpleapfetch.8%{?ext_man}
%{_mandir}/man8/ntptime.8%{?ext_man}
%config %{_sysconfdir}/logrotate.d/ntp
%{_unitdir}/ntpd.service

%changelog
