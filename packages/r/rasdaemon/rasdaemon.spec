#
# spec file for package rasdaemon
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           rasdaemon
Version:        0.6.2
Release:        0
Summary:        Utility to receive RAS error tracings
License:        GPL-2.0-only
Group:          Hardware/Other
URL:            http://git.infradead.org/users/mchehab/rasdaemon.git
Source:         %{name}-%{version}.tar.xz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gettext-devel
BuildRequires:  libtool
BuildRequires:  sqlite3-devel
BuildRequires:  systemd-rpm-macros
Requires:       perl-DBD-SQLite
%{?systemd_requires}
%ifnarch s390x ppc64le
Requires:       dmidecode
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
%setup -q

%build
autoreconf -fvi
%configure \
  --enable-mce \
  --enable-aer \
  --enable-sqlite3 \
  --enable-extlog \
  --enable-abrt-report \
  --enable-arm \
  --enable-non-standard \
  --enable-hisi-ns-decode
make %{?_smp_mflags} V=1

%install
%make_install
install -D -p -m 0644 misc/rasdaemon.service %{buildroot}%{_unitdir}/rasdaemon.service
ln -s %{_sbindir}/service %{buildroot}/%{_sbindir}/rcrasdaemon
install -D -p -m 0644 misc/ras-mc-ctl.service %{buildroot}%{_unitdir}/ras-mc-ctl.service
ln -s %{_sbindir}/service %{buildroot}/%{_sbindir}/rcras-mc-ctl
install -D -p -m 0644 labels/dell %{buildroot}%{_sysconfdir}/ras/dimm_labels.d/dell
rm %{buildroot}%{_includedir}/*.h
mkdir -p %{buildroot}%{_localstatedir}/lib/rasdaemon

%pre
%service_add_pre rasdaemon.service ras-mc-ctl.service

%post
%service_add_post rasdaemon.service ras-mc-ctl.service

%preun
%service_del_preun rasdaemon.service ras-mc-ctl.service

%postun
%service_del_postun rasdaemon.service ras-mc-ctl.service

%files
%license COPYING
%doc AUTHORS ChangeLog README TODO
%{_sbindir}/rasdaemon
%{_sbindir}/ras-mc-ctl
%{_sbindir}/rcrasdaemon
%{_sbindir}/rcras-mc-ctl
%{_mandir}/*/*
%{_unitdir}/*.service
%dir %{_sysconfdir}/ras
%dir %{_localstatedir}/lib/rasdaemon
%ghost %{_localstatedir}/lib/rasdaemon/ras-mc_event.db
%config %{_sysconfdir}/ras/dimm_labels.d

%changelog
