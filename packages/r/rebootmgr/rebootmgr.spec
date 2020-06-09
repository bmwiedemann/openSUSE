#
# spec file for package rebootmgr
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


%if ! %{defined _distconfdir}
  %define _distconfdir %{_sysconfdir}
  %define with_config 1
%else
  %define with_config 0
%endif

Name:           rebootmgr
Version:        1.2
Release:        0
Summary:        Automatic controlled reboot during a maintenance window
License:        GPL-2.0-only AND LGPL-2.1-or-later
Group:          System/Base
URL:            https://github.com/SUSE/rebootmgr
Source:         %{name}-%{version}.tar.xz
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(libeconf)

%description
RebootManager is a dbus service to execute a controlled reboot after updates in a defined maintenance window.

If you updated a system with e.g. transactional updates or a kernel update was applied, you can tell rebootmgrd with rebootmgrctl, that the machine should be reboot at the next possible time. This can either be immeaditly or during a defined maintenance window.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
%make_install
ln -sf service %{buildroot}%{_sbindir}/rcrebootmgr
if [ ! -d %{buildroot}%{_distconfdir} ]; then
    mkdir -p %{buildroot}%{_distconfdir}
    mv %{buildroot}%{_sysconfdir}/rebootmgr.conf %{buildroot}%{_distconfdir}
fi
%fdupes %{buildroot}%{_mandir}

%pre
%service_add_pre rebootmgr.service
test -f /etc/rebootmgr.conf.rpmsave && mv -v /etc/rebootmgr.conf.rpmsave /etc/rebootmgr.conf.rpmsave.old ||:

%post
%service_add_post rebootmgr.service

%preun
%service_del_preun rebootmgr.service

%postun
%service_del_postun rebootmgr.service

%posttrans
test -f /etc/rebootmgr.conf.rpmsave && mv -v /etc/rebootmgr.conf.rpmsave /etc/rebootmgr.conf ||:

%files
%license COPYING COPYING.LIB
%doc NEWS
%dir %{_sysconfdir}/dbus-1/system.d
%if %{with_config}
%config %{_sysconfdir}/rebootmgr.conf
%else
%{_distconfdir}/rebootmgr.conf
%endif
%config %{_sysconfdir}/dbus-1/system.d/org.opensuse.RebootMgr.conf
%{_prefix}/lib/systemd/system/rebootmgr.service
%{_sbindir}/rebootmgrctl
%{_sbindir}/rebootmgrd
%{_sbindir}/rcrebootmgr
%{_datadir}/dbus-1/interfaces/org.opensuse.RebootMgr.xml
%{_mandir}/man1/rebootmgrctl.1%{?ext_man}
%{_mandir}/man5/rebootmgr.conf.5%{?ext_man}
%{_mandir}/man8/rebootmgrd.8%{?ext_man}
%{_mandir}/man8/org.opensuse.RebootMgr.conf.8%{?ext_man}
%{_mandir}/man8/rebootmgr.service.8%{?ext_man}

%changelog
