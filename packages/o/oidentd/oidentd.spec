#
# spec file for package oidentd
#
# Copyright (c) 2023 SUSE LLC
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
  %define _fillupdir %{_localstatedir}/adm/fillup-templates
%endif
%bcond_without systemd
Name:           oidentd
Version:        3.1.0
Release:        0
Summary:        Configurable IDENT Server That Supports NAT/IP Masquerading
License:        GPL-2.0-or-later
Group:          Productivity/Networking/System
URL:            https://oidentd.janikrabe.com/
Source:         https://files.janikrabe.com/pub/oidentd/releases/%{version}/oidentd-%{version}.tar.xz
Source1:        sysconfig.oidentd
Source2:        rc.oidentd
Source3:        oidentd@.service
Source4:        oidentd.socket
Source5:        https://files.janikrabe.com/pub/oidentd/releases/%{version}/oidentd-%{version}.tar.xz.asc
# https://janikrabe.com/key.asc
Source6:        %{name}.keyring
Patch0:         oidentd-3.0.0-configure_zstd.patch
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  flex
%if %{with systemd}
BuildRequires:  systemd-rpm-macros
%{?systemd_requires}
%else
Requires(post): %fillup_prereq
Requires(post): %insserv_prereq
%endif

%description
Oidentd is an ident (rfc1413 compliant) daemon that runs on Linux,
Darwin, FreeBSD, OpenBSD, NetBSD, and Solaris.	oidentd can handle IP
masqueraded/NAT connections on Linux, Darwin, FreeBSD (ipf only),
OpenBSD, and  NetBSD.  Oidentd has a flexible mechanism for specifying
ident responses.  Users can be granted permission to specify their own
ident responses.  Responses can be specified according to host and port
pairs.

%prep
%setup -q
%if 0%{?suse_version} < 1505
%patch0 -p1
%endif

# Avoid "Unknown key name 'XXX' in section 'Service', ignoring." warnings from systemd on older releases
%if 0%{?sle_version}
%if 0%{?sle_version} < 150300
  sed -r -i '/^(Protect(Hostname|KernelLogs|Clock))=/d' %{_sourcedir}/oidentd@.service
%if 0%{?sle_version} < 150200
  sed -r -i '/^(Protect(Home|Hostname|KernelLogs|Clock)|PrivateMounts)=/d' %{_sourcedir}/oidentd@.service
%endif
%endif
%endif
# / sle_version

%build
CFLAGS="%{optflags} -fgnu89-inline"
autoreconf --install --force
%configure
%make_build all

%install
%make_install
mkdir -p %{buildroot}/%{_sysconfdir}  \
         %{buildroot}%{_fillupdir} \
%if %{with systemd}
         %{buildroot}%{_unitdir}
%else
         %{buildroot}%{_sysconfdir}/init.d
%endif
touch %{buildroot}/%{_sysconfdir}/oidentd.conf
touch %{buildroot}/%{_sysconfdir}/oidentd_masq.conf
cp -p %{SOURCE1} %{buildroot}%{_fillupdir}
%if %{with systemd}
install -p -m 0644 %{SOURCE3} %{buildroot}/%{_unitdir}/oidentd@.service
install -p -m 0644 %{SOURCE4} %{buildroot}/%{_unitdir}/oidentd.socket
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}
%else
install -p -m 0755 %{SOURCE2} %{buildroot}%{_sysconfdir}/init.d/oidentd
ln -fs %{_sysconfdir}/init.d/oidentd %{buildroot}%{_sbindir}/rcoidentd
%endif

%if %{with systemd}
%pre
%service_add_pre oidentd@.service oidentd.socket
%endif

%post
%if %{with systemd}
%service_add_post oidentd@.service oidentd.socket
%fillup_only
%else
%fillup_and_insserv
%endif

%if %{with systemd}
%preun
%service_del_preun oidentd@.service oidentd.socket
%endif

%postun
%if %{with systemd}
%service_del_postun oidentd@.service oidentd.socket
%else
%restart_on_update
%insserv_cleanup
%endif

%files
%config(noreplace) %ghost %{_sysconfdir}/oidentd.conf
%config(noreplace) %ghost %{_sysconfdir}/oidentd_masq.conf
%if %{with systemd}
%{_unitdir}/oidentd@.service
%{_unitdir}/oidentd.socket
%else
%config %{_sysconfdir}/init.d/oidentd
%endif
%{_fillupdir}/sysconfig.oidentd
%{_sbindir}/oidentd
%{_sbindir}/rcoidentd
%{_mandir}/man5/oidentd.conf.5%{?ext_man}
%{_mandir}/man5/oidentd_masq.conf.5%{?ext_man}
%{_mandir}/man8/oidentd.8%{?ext_man}
%license COPYING*
%doc AUTHORS ChangeLog* NEWS README

%changelog
