#
# spec file for package rasdaemon
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


Name:           rasdaemon
Version:        0.8.3.0.git+db0870e
Release:        0
Summary:        Utility to receive RAS error tracings
License:        GPL-2.0-only
Group:          Hardware/Other
URL:            http://git.infradead.org/users/mchehab/rasdaemon.git
Source:         %{name}-%{version}.tar.xz
Patch1:         Fix-buffer-overflow-in-add_event_handler-read.patch
Patch2:         rasdaemon-skip-doesn-t-exist-event.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gettext-devel
BuildRequires:  libtool
BuildRequires:  libtraceevent-devel
BuildRequires:  sqlite3-devel
Requires:       perl-DBD-SQLite
Requires(pre):  %fillup_prereq
%{?systemd_ordering}
%ifarch %ix86 x86_64
Requires:       dmidecode
%else
Recommends:     dmidecode
%endif

%description
rasdaemon is a RAS (Reliability, Availability and Serviceability) logging tool.
It currently records memory errors, using the EDAC tracing events.
EDAC is drivers in the Linux kernel that handle detection of ECC errors
from memory controllers for most chipsets on i386 and x86_64 architectures.
EDAC drivers for other architectures like arm also exists.
This userspace component consists of an init script which makes sure
EDAC drivers and DIMM labels are loaded at system startup, as well as
an utility for reporting current error counts from the EDAC sysfs files.

%prep
%autosetup

%build
# Fixes:
# Makefile.am: error: required file './README' not found
# on old autoconf versions
ln -s README.md README
autoreconf -fvi
%configure --enable-all \
	   --with-sysconfdefdir=%{_sysconfdir}/sysconfig
CFLAGS="%{optflags}" make %{?_smp_mflags} V=1

%install
%make_install
make install DESTDIR=%{buildroot}
install -D -p -m 0644 misc/rasdaemon.service %{buildroot}%{_unitdir}/rasdaemon.service
install -D -p -m 0644 misc/ras-mc-ctl.service %{buildroot}%{_unitdir}/ras-mc-ctl.service
ln -s %{_sbindir}/service %{buildroot}/%{_sbindir}/rcrasdaemon
ln -s %{_sbindir}/service %{buildroot}/%{_sbindir}/rcras-mc-ctl
rm INSTALL %{buildroot}%{_includedir}/*.h
mkdir -p %{buildroot}%{_localstatedir}/lib/rasdaemon
mkdir -p %{buildroot}%{_fillupdir}
mv %{buildroot}%{_sysconfdir}/sysconfig/rasdaemon %{buildroot}/%{_fillupdir}/sysconfig.rasdaemon

%pre
%service_add_pre rasdaemon.service ras-mc-ctl.service

%post
%fillup_only
%service_add_post rasdaemon.service ras-mc-ctl.service

%preun
%service_del_preun rasdaemon.service ras-mc-ctl.service

%postun
%service_del_postun rasdaemon.service ras-mc-ctl.service

%files
%license COPYING
%doc AUTHORS ChangeLog README.md TODO
%{_sbindir}/rasdaemon
%{_sbindir}/ras-mc-ctl
%{_sbindir}/rcrasdaemon
%{_sbindir}/rcras-mc-ctl
%{_mandir}/*/*
%{_unitdir}/*.service
%dir %{_sysconfdir}/ras
%dir %{_sysconfdir}/ras/dimm_labels.d
%dir %{_sysconfdir}/ras/triggers
%{_sysconfdir}/ras/triggers/mc_event_trigger
%{_sysconfdir}/ras/triggers/mem_fail_trigger
%dir %{_localstatedir}/lib/rasdaemon
%ghost %{_localstatedir}/lib/rasdaemon/ras-mc_event.db
%attr (644,root,root) %{_fillupdir}/sysconfig.rasdaemon

%changelog
