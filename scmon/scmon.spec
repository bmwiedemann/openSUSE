#
# spec file for package scmon
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           scmon
Summary:        Makes waiting for smart card events easy
License:        GPL-2.0-only
Group:          System/Daemons
Version:        0.4
Release:        0
Url:            http://code.google.com/p/loolixbodes/wiki/scmon
Source0:        http://scmon.googlecode.com/files/%{name}-%{version}.tar.gz
Patch0:         scmon.diff
Patch1:         scmon-init.patch
Patch3:         scmon-glib231.patch
# PATCH-FIX-OPENSUSE scmon-dbus-policy.patch sbrabec@suse.cz -- Fix dbus policy warning.
Patch4:         scmon-dbus-policy.patch
# PATCH-FIX-OPENSUSE scmon-includes.patch sbrabec@suse.cz -- Fix implicit declarations.
Patch5:         scmon-includes.patch
# PATCH-FIX-OPENSUSE smon-add-systemd-support.patch jmoellers@suse.de -- Add systemd support
Patch6:         smon-add-systemd-support.patch

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  pkgconfig
%if 0%{?suse_version} <= 1010
BuildRequires:  dbus-1-devel
BuildRequires:  mozilla-nspr-devel
BuildRequires:  mozilla-nss-devel
%endif
%if 0%{?suse_version} >= 1020
BuildRequires:  dbus-1-devel
BuildRequires:  dbus-1-glib-devel
BuildRequires:  mozilla-nspr-devel
BuildRequires:  mozilla-nss-devel
BuildRequires:  systemd-rpm-macros
%endif

%if 0%{?suse_version} >= 1500
%bcond_without systemd
%else
%bcond_with systemd
%endif

%if %{with systemd}
%{?systemd_requires}
%else
Requires(pre):	%insserv_prereq
%endif

%if 0%{?fedora_version} == 6
BuildRequires:  dbus-devel
BuildRequires:  dbus-glib-devel
BuildRequires:  fedora-release
BuildRequires:  nspr-devel
BuildRequires:  nss-devel
%endif

%description
SCMon monitors smart cards, configured in a system-wide nss database,
and broadcasts their insertion/removal over D-Bus. It also supports a
few simple queries.

It is intended to make it easy for applications such as screensavers
and login managers to support smart card events.



Authors:
--------
    jacob berkman  <jberkman@novell.com>

%prep
%setup -q
%patch0
%patch1
%patch3 -p1
%patch4
%patch5 -p1
%patch6 -p1

%build
%configure
make

%install
%makeinstall
%if %{with systemd}
install -m 644 -D init/scmon.service %{buildroot}%{_unitdir}/scmon.service
ln -s /usr/sbin/service %{buildroot}%{_sbindir}/rcscmon
%else
mkdir -p %{?buildroot:%{buildroot}}%{_sysconfdir}/init.d
cp init/scmon.sle %{?buildroot:%{buildroot}}%{_sysconfdir}/init.d/scmon
ln -s %{_sysconfdir}/init.d/scmon %{?buildroot:%{buildroot}}%{_sbindir}/rcscmon
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with systemd}
%pre
%service_add_pre scmon.service
%endif

%post
%if %{with systemd}
%service_add_post scmon.service
%else
%{fillup_and_insserv scmon}
%endif

%preun
%if %{with systemd}
%service_del_preun scmon.service
%else
%{stop_on_removal}
%endif

%postun
%{restart_on_update scmon}
%if %{with systemd}
%service_del_postun scmon.service
%else
%{insserv_cleanup}
%endif

%files
%defattr(-,root,root,-)
%doc
%config %{_sysconfdir}/dbus-1/system.d/com.novell.Pkcs11Monitor.conf
%if %{with systemd}
%{_unitdir}/scmon.service
%else
%{_sysconfdir}/init.d/scmon
%endif
%{_datadir}/dbus-1/services/com.novell.Pkcs11Monitor.service
%{_sbindir}/scmon
%{_sbindir}/rcscmon
%{_bindir}/scmon-client

%changelog
