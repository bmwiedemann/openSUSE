#
# spec file for package irqbalance
#
# Copyright (c) 2025 SUSE LLC
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

%bcond_with meson
Name:           irqbalance
Version:        1.9.5.0.git+cf76396
Release:        0
Summary:        Daemon to balance IRQs on SMP machines
License:        GPL-2.0-only
Group:          System/Daemons
URL:            https://github.com/Irqbalance/irqbalance
#Source:         https://github.com/Irqbalance/irqbalance/archive/refs/tags/v%%{version}.tar.gz#/%%{name}-%%{version}.tar.gz
Source:         %{name}-%{version}.tar.gz
Patch1:         irqbalance_banmod.diff
BuildRequires:  libcap-ng-devel
BuildRequires:  libtool
BuildRequires:  ncurses-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(systemd)
Recommends:     %{name}-ui
ExcludeArch:    s390 s390x
%{?systemd_ordering}
%if %{with meson}
BuildRequires:  meson
%endif
%ifarch x86_64 %{?x86_64}
BuildRequires:  pkgconfig(libnl-3.0)
%endif
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
%if %{with meson}
%meson -Dpkgconfdir=%{_distconfdir}/default -Dusrconfdir=%{_sysconfdir}/default
%meson_build
%else

NOCONFIGURE=1 ./autogen.sh
%configure \
    --with-systemd \
    --with-pkgconfdir=%{_distconfdir}/default \
    --with-usrconfdir=%{_sysconfdir}/default \
%ifarch x86_64 %{?x86_64}
    --enable-thermal
%endif

%make_build LDFLAGS="-Wl,-z,relro,-z,now" CFLAGS="%{optflags} -fPIE -pie $(ncurses6-config --cflags)" LDFLAGS="$(ncurses6-config --libs)"
%endif

%install
%if %{with meson}
%meson_install
%else
%make_install
%endif

%if 0%{?suse_version} < 1600
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rcirqbalance
%endif

%if %{without meson}
%check
%make_build check
%endif

%pre
%service_add_pre irqbalance.service

%post
%service_add_post irqbalance.service

%preun
%service_del_preun irqbalance.service

%postun
%service_del_postun irqbalance.service

%files
%license COPYING
%doc AUTHORS README.md
%{_sbindir}/irqbalance
%if 0%{?suse_version} < 1600
%{_sbindir}/rcirqbalance
%endif
%{_unitdir}/irqbalance.service
%{_mandir}/man1/irqbalance.1%{?ext_man}
%{_distconfdir}/default/irqbalance.env

%files ui
%{_sbindir}/irqbalance-ui
%{_mandir}/man1/irqbalance-ui.1%{?ext_man}

%changelog
