#
# spec file for package irqbalance
#
# Copyright (c) 2022 SUSE LLC
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
Name:           irqbalance
Version:        1.9.2
Release:        0
Summary:        Daemon to balance IRQs on SMP machines
License:        GPL-2.0-or-later
Group:          System/Daemons
URL:            https://github.com/Irqbalance/irqbalance
Source:         https://github.com/Irqbalance/irqbalance/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source3:        sysconfig.irqbalance
Patch1:         Set-fd-limit.patch
# PATCH-FIX-UPSTREAM: https://github.com/Irqbalance/irqbalance/pull/250
Patch2:         irqbalance-systemd-netlink.patch
BuildRequires:  libcap-ng-devel
BuildRequires:  libtool
BuildRequires:  ncurses-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(glib-2.0)
%ifarch x86_64 %{?x86_64}
BuildRequires:  pkgconfig(libnl-3.0)
%endif
Requires(pre):  %fillup_prereq
Recommends:     %{name}-ui
ExcludeArch:    s390 s390x
%{?systemd_ordering}
%ifnarch %{arm}
BuildRequires:  libnuma-devel
%endif

%description
irqbalance dynamically switches the CPUs for IRQs to prevent cpu0 from
being used for all IRQs.

%package ui
Summary:        UI for IRQ balance Daemon
Group:          System/Daemons
Requires:       %{name} = %{version}

%description ui
Text UI for the IRQ balance daemon.

%prep
%setup -q
%autopatch -p1

%build
NOCONFIGURE=1 ./autogen.sh
%configure \
%ifarch x86_64 %{?x86_64}
    --enable-thermal
%endif

%make_build LDFLAGS="-Wl,-z,relro,-z,now" CFLAGS="%{optflags} -fPIE -pie $(ncurses6-config --cflags)" LDFLAGS="$(ncurses6-config --libs)"
cp %{SOURCE3} .

%install
%make_install

mkdir -p %{buildroot}%{_fillupdir}/
install -m 0644 sysconfig.irqbalance %{buildroot}%{_fillupdir}/
sed -ie "s|EnvironmentFile=.*|EnvironmentFile=%{_sysconfdir}/sysconfig/irqbalance|g" misc/irqbalance.service
# Remove syslog.target in systemd service file; not provided by systemd anymore
sed -ie "s|After=syslog.target||g" misc/irqbalance.service
install -D -m 0644 misc/irqbalance.service %{buildroot}%{_unitdir}/irqbalance.service
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rcirqbalance

%check
%make_build check

%pre
%service_add_pre irqbalance.service

%post
%fillup_only %{name}
%service_add_post irqbalance.service

%preun
%service_del_preun irqbalance.service

%postun
%service_del_postun irqbalance.service

%files
%license COPYING
%doc AUTHORS README.md
%{_sbindir}/irqbalance
%{_sbindir}/rcirqbalance
%{_unitdir}/irqbalance.service
%{_mandir}/man1/irqbalance.1%{?ext_man}
%{_fillupdir}/sysconfig.irqbalance

%files ui
%{_sbindir}/irqbalance-ui
%{_mandir}/man1/irqbalance-ui.1%{?ext_man}

%changelog
