#
# spec file for package watchdog
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


Summary:        Software and/or Hardware watchdog daemon
License:        GPL-2.0-only
Group:          System/Daemons
Name:           watchdog
Version:        5.16
Release:        0
URL:            https://sourceforge.net/projects/watchdog/
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        https://sourceforge.net/projects/watchdog/files/%{name}/%{version}/%{name}-%{version}.tar.gz
Source4:        watchdog.service
Source5:        watchdog-ping.service

Patch0:         watchdog-sysconfdir.diff

BuildRequires:  libtirpc-devel

Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

%description
The watchdog program can be used as a powerful software watchdog daemon
or may be alternately used with a hardware watchdog device such as the
IPMI hardware watchdog driver interface to a resident Baseboard
Management Controller (BMC).  watchdog periodically writes to /dev/watchdog;
the interval between writes to /dev/watchdog is configurable through settings
in the watchdog sysconfig file.  This configuration file is also used to
set the watchdog to be used as a hardware watchdog instead of its default
software watchdog operation.  In either case, if the device is open but not
written to within the configured time period, the watchdog timer expiration
will trigger a machine reboot. When operating as a software watchdog, the
ability to reboot will depend on the state of the machine and interrupts.
When operating as a hardware watchdog, the machine will experience a hard
reset (or whatever action was configured to be taken upon watchdog timer
expiration) initiated by the BMC.

%prep
%autosetup -p1
mv README README.orig
iconv -f ISO-8859-1 -t UTF-8 < README.orig > README

%build
%configure \
	CFLAGS="$CFLAGS -I/usr/include/tirpc" \
	LIBS="$LIBS -ltirpc"

%__make %{?_smp_mflags}

%install
install -d -m0755 %{buildroot}%{_sysconfdir}
make DESTDIR=%{buildroot} install
install -Dp -m0644 %{SOURCE4} %{buildroot}%{_unitdir}/watchdog.service
install -Dp -m0644 %{SOURCE5} %{buildroot}%{_unitdir}/watchdog-ping.service
ln -s /usr/sbin/service %{buildroot}%{_sbindir}/rcwatchdog
ln -s /usr/sbin/service %{buildroot}%{_sbindir}/rcwatchdog-ping

%pre
%service_add_pre %{name}.service watchdog-ping.service

%post
%service_add_post %{name}.service watchdog-ping.service

%preun
%service_del_preun %{name}.service watchdog-ping.service

%postun
%service_del_postun %{name}.service watchdog-ping.service

%files
%defattr(-, root, root, -)
%doc AUTHORS ChangeLog COPYING examples/ IAFA-PACKAGE NEWS README TODO README.watchdog.ipmi
%config(noreplace) %{_sysconfdir}/watchdog.conf
%{_unitdir}/watchdog.service
%{_unitdir}/watchdog-ping.service
%{_sbindir}/rcwatchdog-ping
%{_sbindir}/rcwatchdog
%{_sbindir}/watchdog
%{_sbindir}/wd_keepalive
%{_sbindir}/wd_identify
%{_mandir}/man5/watchdog.conf.5*
%{_mandir}/man8/watchdog.8*
%{_mandir}/man8/wd_keepalive.8*
%{_mandir}/man8/wd_identify.8*

%changelog
