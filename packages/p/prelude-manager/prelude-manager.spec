#
# spec file for package prelude-manager
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


Name:           prelude-manager
Version:        5.2.0
Release:        0
Summary:        Bus communication for all Prelude modules
# Prelude is GPL-2.0+
# libmissing is LGPL-2.1+
# libmissing/test is GPL-3.0+
License:        GPL-2.0-or-later AND LGPL-2.1-only AND GPL-3.0-or-later
Group:          Productivity/Networking/Security
URL:            https://www.prelude-siem.org
Source0:        https://www.prelude-siem.org/pkg/src/%{version}/%{name}-%{version}.tar.gz
Source1:        prelude-manager.service
Source2:        prelude-manager-tmpfiles.conf
Source3:        https://www.prelude-siem.org/pkg/src/%{version}/%{name}-%{version}.tar.gz.sig
Source4:        https://www.prelude-siem.org/attachments/download/233/RPM-GPG-KEY-Prelude-IDS#/%{name}.keyring
# Fix run dir for Systemd
Patch0:         prelude-manager-run-dir.patch
# Fix dirs permissions
Patch1:         prelude-manager-fix_dir_perms.patch
BuildRequires:  libprelude-devel >= 5.2.0
BuildRequires:  libpreludedb-devel >= 5.2.0
BuildRequires:  net-snmp-devel >= 5.4
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gnutls) >= 1.0.17
BuildRequires:  pkgconfig(libmaxminddb)
BuildRequires:  pkgconfig(libxml-2.0) >= 2.0.0
BuildRequires:  pkgconfig(systemd)
%{?systemd_ordering}

%description
Prelude Manager is a high availability server that
accepts secured connections from distributed sensors
and saves received events to a media specified by the user
(database, log file, mail etc.). The server schedules and
establishes the priorities of treatment according to the
critical character and the source of the alerts.

%package devel
Summary:        Libraries, include files for Prelude Manager
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}-%{release}
Requires:       libpreludedb-devel

%description devel
Header files and libraries for prelude-manager development.

%package db-plugin
Summary:        Database report plugin for Prelude Manager
Group:          Productivity/Networking/Security
Requires:       %{name} = %{version}-%{release}

%description db-plugin
This plugin allows prelude-manager to write to database.

%package xml-plugin
Summary:        XML report plugin for Prelude Manager
Group:          Productivity/Networking/Security
Requires:       %{name} = %{version}-%{release}

%description xml-plugin
This plugin adds XML logging capabilities to prelude-manager.

%package smtp-plugin
Summary:        SMTP alert plugin for Prelude Manager
Group:          Productivity/Networking/Security
Requires:       %{name} = %{version}-%{release}

%description smtp-plugin
This plugin adds alerting by email capabilities to prelude-manager

%package snmp-plugin
Summary:        SNMP traps plugin for Prelude Manager
Group:          Productivity/Networking/Security
Requires:       %{name} = %{version}-%{release}

%description snmp-plugin
This plugin adds SNMP traps capabilities to prelude-manager

%prep
%setup -q
%patch0
%patch1

%build
%configure \
	--disable-static \
	--enable-shared \
	--enable-libmaxminddb \
	--enable-snmp
%make_build

%install
mkdir -p %{buildroot}%{_defaultdocdir}/%{name}-%{version}
%make_install

find %{buildroot} -type f -name "*.la" -delete -print

mkdir -p %{buildroot}%{_localstatedir}/spool/%{name}/scheduler
mkdir -p %{buildroot}%{_localstatedir}/spool/%{name}/failover
mkdir -p %{buildroot}%{_localstatedir}/lib/%{name}
mkdir -p %{buildroot}%{_sysconfdir}/prelude/profile/%{name}

rm -f %{buildroot}/%{_defaultdocdir}/../%{name}/smtp/template.example
rm -f %{buildroot}/%{_defaultdocdir}/../%{name}/snmp/PRELUDE-SIEM-MIB.mib
mkdir -p %{buildroot}/%{_sbindir}

# Empty dir but kept by debuginfo
rm -rf src/.libs

# Service
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}
install -D -m 444 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service

# Tmpfiles
install -d -m 0755 %{buildroot}/%{_tmpfilesdir}
install -m 0644 %{SOURCE2} %{buildroot}/%{_tmpfilesdir}/%{name}.conf
rm -rf %{buildroot}/%{_localstatedir}/run/%{name}

%pre
%service_add_pre %{name}.service

%post
/sbin/ldconfig
%{_bindir}/systemd-tmpfiles --create %{_tmpfilesdir}/%{name}.conf
%service_add_post %{name}.service

%preun
%service_del_preun %{name}.service

%postun
/sbin/ldconfig
%service_del_postun %{name}.service

%files
%license COPYING
%{_unitdir}/%{name}.service
%{_sbindir}/rc%{name}
%{_bindir}/%{name}
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/decodes
%dir %{_libdir}/%{name}/filters
%dir %{_libdir}/%{name}/reports
%{_libdir}/%{name}/filters/idmef-criteria.so
%{_libdir}/%{name}/filters/thresholding.so
%{_libdir}/%{name}/decodes/normalize.so
%{_libdir}/%{name}/reports/debug.so
%{_libdir}/%{name}/reports/relaying.so
%{_libdir}/%{name}/reports/script.so
%{_libdir}/%{name}/reports/textmod.so
%attr(0750,-,-) %dir %{_localstatedir}/spool/%{name}
%attr(0750,-,-) %dir %{_localstatedir}/spool/%{name}/scheduler
%attr(0750,-,-) %dir %{_localstatedir}/spool/%{name}/failover
%dir %{_tmpfilesdir}
%{_tmpfilesdir}/%{name}.conf
%attr(0750,-,-) %dir %{_datadir}/%{name}/
%attr(0750,-,-) %dir %{_sysconfdir}/%{name}/
%config(noreplace) %attr(0640,-,-) %{_sysconfdir}/%{name}/%{name}.conf
%dir %ghost /run/%{name}
%attr(0644,-,-) %{_mandir}/man1/%{name}.1%{ext_man}

%files db-plugin
%license COPYING
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/reports
%{_libdir}/%{name}/reports/db.so

%files xml-plugin
%license COPYING
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/reports
%{_libdir}/%{name}/reports/xmlmod.so
%attr(0750,root,root) %dir %{_datadir}/%{name}/xmlmod/
%{_datadir}/%{name}/xmlmod/*

%files smtp-plugin
%license COPYING
%doc %attr(0644,root,root) plugins/reports/smtp/template.example
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/reports
%{_libdir}/%{name}/reports/smtp.so

%files snmp-plugin
%license COPYING
%doc %attr(0644,root,root) plugins/reports/snmp/PRELUDE-SIEM-MIB.mib
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/reports
%{_libdir}/%{name}/reports/snmp.so

%files devel
%license COPYING
%{_includedir}/%{name}/

%changelog
