#
# spec file for package chrony
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


%define _systemdutildir %(pkg-config --variable systemdutildir systemd)
%global clknetsim_ver 79ffe44
#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir %{_localstatedir}/adm/fillup-templates
%endif
Name:           chrony
Version:        3.5.1
Release:        0
Summary:        System Clock Synchronization Client and Server
License:        GPL-2.0-only
Group:          Productivity/Networking/Other
URL:            https://chrony.tuxfamily.org/
Source:         https://download.tuxfamily.org/chrony/chrony-%{version}.tar.gz
Source2:        chronyd.sysconfig
Source3:        chrony.dhclient
Source4:        chrony.helper
Source5:        chrony-dnssrv@.service
Source6:        chrony-dnssrv@.timer
Source7:        https://download.tuxfamily.org/chrony/chrony-%{version}-tar-gz-asc.txt#/chrony-%{version}.tar.gz.sig
Source8:        chrony.keyring
# Simulator for test suite
Source10:       https://github.com/mlichvar/clknetsim/archive/%{clknetsim_ver}/clknetsim-%{clknetsim_ver}.tar.gz
Source11:       chrony-tmpfiles
Source12:       pool.conf.suse
Source13:       pool.conf.opensuse
# PATCH-MISSING-TAG -- See http://wiki.opensuse.org/openSUSE:Packaging_Patches_guidelines
Patch0:         chrony-config.patch
# Add NTP servers from DHCP when starting service
Patch1:         chrony-service-helper.patch
Patch2:         chrony-logrotate.patch
Patch3:         chrony-service-ordering.patch
Patch4:         chrony-test-fix-util-unit-test-for-NTP-era-split.patch
Patch5:         chrony-test-update-processing-of-packet-log.patch
BuildRequires:  NetworkManager-devel
BuildRequires:  bison
BuildRequires:  gcc-c++
BuildRequires:  libcap-devel
BuildRequires:  libedit-devel
BuildRequires:  mozilla-nss-devel
BuildRequires:  pkgconfig
BuildRequires:  pps-tools-devel
# The timezone package is needed for the "make check" tests. It can be
# removed if the call to make check is ever deleted.
BuildRequires:  timezone
BuildRequires:  pkgconfig(systemd)
BuildRequires:  rubygem(asciidoctor)
Recommends:     logrotate
Requires(post): %fillup_prereq
Requires(pre):  %{_sbindir}/groupadd
Requires(pre):  %{_sbindir}/useradd
Requires:       %name-pool
Recommends:     %name-pool-nonempty
Provides:       ntp-daemon
%ifarch s390 s390x ppc64le
BuildRequires:  libseccomp-devel >= 2.2.0
%else
BuildRequires:  libseccomp-devel
%endif

%description
Chrony is an implementation of the Network Time Protocol (NTP). It can
synchronize the system clock with NTP servers, reference clocks (e.g. a
GPS receiver), and manual input using wristwatch and keyboard. It can
also operate as an NTPv4 (RFC 5905) server and peer to provide a time
service to other computers in the network.

Chrony consists of two programs: chronyd and chronyc.

Chronyd is a daemon which runs in the background on the system. It
obtains measurements of the system clock’s offset relative to time
servers on other systems via the network and adjusts the system time
accordingly. For isolated systems, the user can periodically enter the
correct time by hand (using chronyc). In either case, chronyd
determines the rate at which the computer gains or loses time, and
compensates for this. Chronyd can act as either a client or a server.

Chronyc provides a user interface to chronyd for monitoring its
performance and configuring various settings. It can do so while
running on the same computer as the chronyd instance it is controlling
or a different computer.

%package pool-suse
Summary:        Chrony preconfiguration for SUSE
Group:          Productivity/Networking/Other
Provides:       %name-pool = %version
Provides:       %name-pool-nonempty
Conflicts:      otherproviders(%name-pool)
Requires:       %name = %version
BuildArch:      noarch
RemovePathPostfixes: .suse

%description pool-suse
This package configures chrony to use the SUSE NTP server pool by
default.

%package pool-openSUSE
Summary:        Chrony preconfiguration for openSUSE
Group:          Productivity/Networking/Other
Provides:       %name-pool = %version
Provides:       %name-pool-nonempty
Conflicts:      otherproviders(%name-pool)
Requires:       %name = %version
BuildArch:      noarch
RemovePathPostfixes: .opensuse

%description pool-openSUSE
This package configures chrony to use the openSUSE NTP server pool by
default.

%package pool-empty
Summary:        Empty pool preconfiguration for chrony
Group:          Productivity/Networking/Other
Provides:       %name-pool = %version
Conflicts:      otherproviders(%name-pool)
Requires:       %name = %version
BuildArch:      noarch
RemovePathPostfixes: .empty

%description pool-empty
This package provides an empty /etc/chrony.d/pool.conf file for
situations when having servers preconfigured in chrony is undesirable,
e.g. because the servers will be set via DHCP.

%prep
%setup -q -a 10
%patch0 -p1
sed -e 's-@LIBEXECDIR@-%{_libexecdir}-g' -i %{PATCH1}
%patch1 -p1
%patch2 -p1
%patch3
%patch4 -p1
%patch5 -p1

# Remove pool statements from the default /etc/chrony.conf. They will
# be provided by branding packages in /etc/chrony.d/pool.conf .

sed -e 's|^\pool|! pool|' \
        < examples/chrony.conf.example2 > chrony.conf

cat << EOF >> chrony.conf

# Also include any directives found in configuration files in /etc/chrony.d
include %{_sysconfdir}/chrony.d/*.conf
EOF

touch -r examples/chrony.conf.example2 chrony.conf

# regenerate the file from getdate.y
rm -f getdate.c

mv clknetsim-%{clknetsim_ver}* test/simulation/clknetsim

%build
# not autoconf:
export CFLAGS="%{optflags} -Wall -fpic -DPIC $(pkg-config --cflags libseccomp)"
export LDFLAGS="-pie -Wl,-z,relro,-z,now"
%configure                                  \
  --docdir="%{_docdir}/%{name}"             \
  %if %{with syscallfilter}
  --enable-scfilter                         \
  %endif
  --with-user=chrony                        \
  --with-hwclockfile=%{_sysconfdir}/adjtime \
  --with-sendmail=%{_sbindir}/sendmail      \
  --enable-ntp-signd
make %{?_smp_mflags} all docs

%install
%make_install
install -Dpm 0644 chrony.conf \
  %{buildroot}%{_sysconfdir}/chrony.conf
mkdir %{buildroot}%{_sysconfdir}/chrony.d
install -Dpm 0640 examples/chrony.keys.example \
  %{buildroot}%{_sysconfdir}/chrony.keys
install -Dpm 0755 examples/chrony.nm-dispatcher \
  %{buildroot}%{_sysconfdir}/NetworkManager/dispatcher.d/20-chrony
install -Dpm 0755 %{SOURCE3} \
  %{buildroot}%{_sysconfdir}/dhcp/dhclient.d/chrony.sh
install -Dpm 0644 examples/chrony.logrotate \
  %{buildroot}%{_sysconfdir}/logrotate.d/chrony
install -Dpm 0644 examples/chronyd.service \
  %{buildroot}%{_unitdir}/chronyd.service
install -Dpm 0644 examples/chrony-wait.service \
  %{buildroot}%{_unitdir}/chrony-wait.service
sed -e 's-@LIBEXECDIR@-%{_libexecdir}-g' -i %{SOURCE5}
install -Dpm 0644 %{SOURCE5} \
  %{buildroot}%{_unitdir}/chrony-dnssrv@.service
install -Dpm 0644 %{SOURCE6} \
  %{buildroot}%{_unitdir}/chrony-dnssrv@.timer
install -Dpm 0644 %{SOURCE11} \
  %{buildroot}%{_tmpfilesdir}/%{name}.conf

install -d %{buildroot}%{_sbindir}
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rcchronyd
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rcchrony-wait

install -d %{buildroot}%{_systemdutildir}/ntp-units.d
echo 'chronyd.service' > \
        %{buildroot}%{_systemdutildir}/ntp-units.d/50-chronyd.list

install -Dpm 0644 %{SOURCE2} \
  %{buildroot}%{_fillupdir}/sysconfig.chronyd
install -Dpm 755 %{SOURCE4} \
  %{buildroot}%{_libexecdir}/%name/helper

install -d %{buildroot}%{_localstatedir}/log/chrony
touch %{buildroot}%{_localstatedir}/lib/chrony/{drift,rtc}

# Install the NTP pool files
install -Dpm 644 %{SOURCE12} %{SOURCE13} %{buildroot}/etc/chrony.d
touch %{buildroot}/etc/chrony.d/pool.conf.empty

%ifnarch %ix86
%check
# Set random seed to get deterministic results
export CLKNETSIM_RANDOM_SEED=24501
export CFLAGS="%{optflags}"
make %{?_smp_mflags} -C test/simulation/clknetsim
make %{?_smp_mflags} check
%endif

%pre
getent group %{name} >/dev/null || groupadd -r %{name}
getent passwd %{name} >/dev/null || useradd -r -g %{name} -d "%{_localstatedir}/lib/chrony" -s /bin/false -c "Chrony Daemon" %{name}
%service_add_pre chronyd.service chrony-wait.service

%preun
%service_del_preun chronyd.service chrony-wait.service

%post
%fillup_only -n chronyd
%tmpfiles_create %{name}.conf
%service_add_post chronyd.service chrony-wait.service

%postun
%service_del_postun chronyd.service chrony-wait.service

%files
%license COPYING
%doc FAQ NEWS README
%doc examples
%config(noreplace) %attr(0640,root,%{name}) %{_sysconfdir}/chrony.conf
%config(noreplace) %attr(0640,root,%{name}) %verify(not md5 size mtime) %{_sysconfdir}/chrony.keys
%config(noreplace) %{_sysconfdir}/logrotate.d/chrony
%{_sysconfdir}/NetworkManager/dispatcher.d/20-chrony
%dir %{_sysconfdir}/chrony.d/
%dir %{_sysconfdir}/dhcp/
%dir %{_sysconfdir}/dhcp/dhclient.d/
%{_sysconfdir}/dhcp/dhclient.d/chrony.sh
%{_bindir}/chronyc
%{_sbindir}/chronyd
%{_libexecdir}/%name
%{_mandir}/man1/chronyc.1%{?ext_man}
%{_mandir}/man5/chrony.conf.5%{?ext_man}
%{_mandir}/man8/chronyd.8%{?ext_man}
%{_systemdutildir}/ntp-units.d/*.list
%{_unitdir}/chrony*.service
%{_unitdir}/chrony*.timer
%{_sbindir}/rcchrony*
%{_tmpfilesdir}/%{name}.conf
%{_fillupdir}/sysconfig.chronyd
%dir %attr(750,chrony,chrony) %{_localstatedir}/lib/chrony
%ghost %attr(640,chrony,chrony) %{_localstatedir}/lib/chrony/drift
%ghost %attr(640,chrony,chrony) %{_localstatedir}/lib/chrony/rtc
%dir %attr(750,chrony,chrony) %{_localstatedir}/log/chrony
%ghost %attr(0750, %{name}, %{name}) %{_rundir}/%{name}

%files pool-empty
%config (noreplace) /etc/chrony.d/pool.conf.empty

%files pool-suse
%config (noreplace) /etc/chrony.d/pool.conf.suse

%files pool-openSUSE
%config (noreplace) /etc/chrony.d/pool.conf.opensuse

%changelog
