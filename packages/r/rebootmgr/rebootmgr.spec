#
# spec file for package rebootmgr
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


Name:           rebootmgr
Version:        3.0+git20250129.eed876f
Release:        0
Summary:        Automatic controlled reboot during a maintenance window
License:        GPL-2.0-only AND LGPL-2.1-or-later
Group:          System/Base
URL:            https://github.com/SUSE/rebootmgr
Source:         %{name}-%{version}.tar.xz
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  timezone
BuildRequires:  pkgconfig(libeconf) >= 0.7.6
BuildRequires:  pkgconfig(libsystemd) >= 257

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

%check
%meson_test

%pre
%service_add_pre rebootmgr.service
if [ -f /etc/rebootmgr.conf ] && [ ! -f /etc/rebootmgr/rebootmgr.conf.d/20-old-rebootmgr.conf ]; then
    mkdir -p /etc/rebootmgr/rebootmgr.conf.d ||:
    mv /etc/rebootmgr.conf /etc/rebootmgr/rebootmgr.conf.d/20-old-rebootmgr.conf
fi

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
%{_libexecdir}/rebootmgrd
%{_datadir}/bash-completion/completions/rebootmgrctl
%{_mandir}/man1/rebootmgrctl.1%{?ext_man}
%{_mandir}/man5/rebootmgr.conf.5%{?ext_man}
%{_mandir}/man8/rebootmgrd.8%{?ext_man}
%{_mandir}/man8/rebootmgr.service.8%{?ext_man}

%changelog
