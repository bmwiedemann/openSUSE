#
# spec file for package ppc64-diag
#
# Copyright (c) 2021 SUSE LLC
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


Name:           ppc64-diag
Version:        2.7.6
Release:        0
Summary:        Linux for Power Platform Diagnostics
License:        GPL-2.0-or-later
Group:          System/Monitoring
URL:            http://sourceforge.net/projects/linux-diag/files/ppc64-diag
Source0:        http://downloads.sourceforge.net/project/linux-diag/ppc64-diag/v%{version}/%{name}-%{version}.tar.gz
#PATCH-FIX-OPENSUSE - ppc64-diag.varunused.patch - fix unused variables
Patch1:         ppc64-diag.varunused.patch
#PATCH-FIX-UPSTREAM - ppc64-diag-Drop-obsolete-logging-options-from-systemd-service-f.patch - fix systemd warning
Patch2:         ppc64-diag-Drop-obsolete-logging-options-from-systemd-service-f.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  cron
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  librtas-devel >= 1.4.0
BuildRequires:  libservicelog-devel
BuildRequires:  libtool
BuildRequires:  perl
BuildRequires:  pkgconfig
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libvpd-2)
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(sqlite3)
Requires:       cron
# Light Path Diagnostics depends on below lsvpd version.
Requires:       lsvpd >= 1.7.1
Requires:       powerpc-utils >= 1.3.2
Requires:       servicelog
Requires(post): aaa_base
# autoselect the package on systems which have the /vdevice/IBM,sp node
# All pSeries POWER5 and later have this property
Supplements:    modalias(vio:TIBM*spS*)
ExclusiveArch:  ppc ppc64 ppc64le

%description
This package contains various diagnostic tools for PowerLinux.
These tools captures the diagnostic events from Power Systems
platform firmware, SES enclosures and device drivers, and
write events to servicelog database. It also provides automated
responses to urgent events such as environmental conditions and
predictive failures, if appropriate modifies the FRUs fault
indicator(s) and provides event notification to system
administrators or connected service frameworks.

%prep
%setup -q
%autopatch -p1

%build
sed -i 's@%{_prefix}/libexec/ppc64-diag@%{_libexecdir}@g' scripts/opal_errd.service
sed -i 's@%{_prefix}/libexec/ppc64-diag@%{_libexecdir}@g' scripts/rtas_errd.service
autoreconf -fvi
%configure
make %{?_smp_mflags}

%install
%make_install
chmod 644 %{buildroot}%{_sysconfdir}/ppc64-diag/servevent_parse.pl
mkdir %{buildroot}%{_sysconfdir}/ppc64-diag/ses_pages
ln -sf %{_sbindir}/usysattn %{buildroot}%{_sbindir}/usysfault
install -D -m0644 scripts/rtas_errd.service %{buildroot}%{_unitdir}/rtas_errd.service
install -D -m0644 scripts/opal_errd.service %{buildroot}%{_unitdir}/opal_errd.service
ln -s service %{buildroot}%{_sbindir}/rcrtas_errd
ln -s service %{buildroot}%{_sbindir}/rcopal_errd
rm %{buildroot}%{_prefix}/libexec/%{name}/opal_errd
rm %{buildroot}%{_prefix}/libexec/%{name}/rtas_errd
rm %{buildroot}%{_datadir}/doc/%{name}/COPYING
rm %{buildroot}%{_datadir}/doc/%{name}/README

%files
%license COPYING
%doc README
%{_sbindir}/*
%dir %{_sysconfdir}/ppc64-diag
%config %{_sysconfdir}/ppc64-diag/*
%config %{_sysconfdir}/rc.powerfail
%{_mandir}/man8/explain_syslog.8%{?ext_man}
%{_mandir}/man8/syslog_to_svclog.8%{?ext_man}
%{_mandir}/man8/diag_encl.8%{?ext_man}
%{_mandir}/man8/encl_led.8%{?ext_man}
%{_mandir}/man8/lp_diag.8%{?ext_man}
%{_mandir}/man8/usysattn.8%{?ext_man}
%{_mandir}/man8/usysfault.8%{?ext_man}
%{_mandir}/man8/usysident.8%{?ext_man}
%{_mandir}/man8/opal-dump-parse.8%{?ext_man}
%{_mandir}/man8/opal-elog-parse.8%{?ext_man}
%{_mandir}/man8/opal_errd.8%{?ext_man}
%attr(755,root,root) %{_sysconfdir}/cron.daily/run_diag_encl
%{_unitdir}/rtas_errd.service
%{_unitdir}/opal_errd.service

%post
%{_sysconfdir}/ppc64-diag/ppc64_diag_setup --register >/dev/null 2>&1
%{_sysconfdir}/ppc64-diag/lp_diag_setup --register >/dev/null 2>&1
%service_add_post rtas_errd.service
%service_add_post opal_errd.service

%preun
# Pre-uninstall script -------------------------------------------------
if [ "$1" = "0" ]; then # last uninstall
  %service_del_preun rtas_errd.service
  %service_del_preun opal_errd.service
  %{_sysconfdir}/ppc64-diag/ppc64_diag_setup --unregister >/dev/null
  %{_sysconfdir}/ppc64-diag/lp_diag_setup --unregister >/dev/null
fi

%triggerin -- librtas
# trigger on librtas upgrades ------------------------------------------
if [ "$2" = "2" ]; then
    systemctl restart rtas_errd.service >/dev/null
fi

%pre
%service_add_pre rtas_errd.service
%service_add_pre opal_errd.service

%postun
%service_del_postun rtas_errd.service
%service_del_postun opal_errd.service

%changelog
