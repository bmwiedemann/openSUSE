#
# spec file for package restorecond
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


%define libselinux_ver   3.1
Name:           restorecond
Version:        3.1
Release:        0
Summary:        Daemon to restore SELinux contexts
License:        GPL-2.0-or-later
Group:          Productivity/Security
URL:            https://github.com/SELinuxProject/selinux.git
Source0:        https://github.com/SELinuxProject/selinux/releases/download/20200710/restorecond-%{version}.tar.gz
BuildRequires:  dbus-1-glib-devel
BuildRequires:  libselinux-devel >= %{libselinux_ver}
Requires:       libselinux1 >= %{libselinux_ver}
Requires:       selinux-tools >= %{libselinux_ver}

%description
Daemon that watches for file creation and then sets the default SELinux file context

%prep
%setup -q

%build
export CFLAGS="%optflags"
%make_build LSPP_PRIV=y all

%install
make DESTDIR=%{buildroot} SHLIBDIR=/%{_lib} SYSTEMDSYSTEMUNITDIR=%{_unitdir} SYSTEMDUSERUNITDIR=%{_userunitdir} install
rm %{buildroot}%{_sysconfdir}/rc.d/init.d/restorecond
ln -s /sbin/service %{buildroot}%{_sbindir}/rcrestorecond

%pre
%service_add_pre restorecond.service

%post
%service_add_post restorecond.service

%preun
%service_del_preun restorecond.service

%postun
%service_del_postun restorecond.service

%files
%config %{_sysconfdir}/selinux/restorecond.conf
%config(noreplace) %{_sysconfdir}/selinux/restorecond_user.conf
%{_sysconfdir}/xdg/autostart/restorecond.desktop
%{_unitdir}/restorecond.service
%{_userunitdir}/restorecond_user.service

%{_sbindir}/restorecond
%{_sbindir}/rcrestorecond
%{_datadir}/dbus-1/services/org.selinux.Restorecond.service
%{_mandir}/man8/restorecond.8%{?ext_man}
%{_mandir}/ru/man8/restorecond.8%{?ext_man}

%changelog
