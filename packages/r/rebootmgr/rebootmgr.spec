#
# spec file for package rebootmgr
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


Name:           rebootmgr
Version:        2.6+git20241108.fc0c103
Release:        0
Summary:        Automatic controlled reboot during a maintenance window
License:        GPL-2.0-only AND LGPL-2.1-or-later
Group:          System/Base
URL:            https://github.com/SUSE/rebootmgr
Source:         %{name}-%{version}.tar.xz
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(libeconf)

%description
RebootManager is a dbus service to execute a controlled reboot after updates in a defined maintenance window.

If you updated a system with e.g. transactional updates or a kernel update was applied, you can tell rebootmgrd with rebootmgrctl, that the machine should be reboot at the next possible time. This can either be immediately or during a defined maintenance window.

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install
ln -sf ../bin/rebootmgrctl %{buildroot}%{_sbindir}/rebootmgrctl

#%check
#meson_test

%pre
%service_add_pre rebootmgr.service

%post
%service_add_post rebootmgr.service

%preun
%service_del_preun rebootmgr.service

%postun
%service_del_postun rebootmgr.service

%files
%license COPYING COPYING.LIB
%doc NEWS
%dir %{_datadir}/rebootmgr
%{_datadir}/rebootmgr/rebootmgr.conf
%{_unitdir}/rebootmgr.service
%{_bindir}/rebootmgrctl
%{_sbindir}/rebootmgrctl
%{_sbindir}/rebootmgrd
%{_datadir}/dbus-1/interfaces/org.opensuse.RebootMgr.xml
%{_datadir}/dbus-1/system.d/org.opensuse.RebootMgr.conf
%{_mandir}/man1/rebootmgrctl.1%{?ext_man}
%{_mandir}/man5/rebootmgr.conf.5%{?ext_man}
%{_mandir}/man8/rebootmgrd.8%{?ext_man}
%{_mandir}/man8/org.opensuse.RebootMgr.conf.8%{?ext_man}
%{_mandir}/man8/rebootmgr.service.8%{?ext_man}

%changelog
