#
# spec file for package iwd
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


Name:           iwd
Version:        0.21
Release:        0
Summary:        Wireless daemon for Linux
License:        LGPL-2.1-or-later
Group:          Productivity/Networking/Other
URL:            https://git.kernel.org/pub/scm/network/wireless/iwd.git
Source:         https://kernel.org/pub/linux/network/wireless/%{name}-%{version}.tar.xz
Source2:        https://kernel.org/pub/linux/network/wireless/%{name}-%{version}.tar.sign
# https://kernel.org/doc/wot/holtmann.html
Source3:        %{name}.keyring
BuildRequires:  pkgconfig
BuildRequires:  readline-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(ell) >= 0.23
BuildRequires:  pkgconfig(systemd)
%{?systemd_ordering}

%description
The iNet Wireless Daemon (iwd) project provides a wireless
connectivity solution. It attempts to optimise resource utilisation
of storage, runtime memory and link-time costs. It utilises the
features provided by the Linux kernel.

%prep
%setup -q

%build
%configure \
  --libexecdir=%{_libexecdir}/%{name} \
  --enable-external-ell
make %{?_smp_mflags} V=1

%install
%make_install

mkdir -p %{buildroot}%{_sbindir}/
ln -s service %{buildroot}%{_sbindir}/rc%{name}

%pre
%service_add_pre %{name}.service

%post
%service_add_post %{name}.service

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%files
%license COPYING
%doc AUTHORS ChangeLog README
%{_bindir}/iwctl
%{_bindir}/iwmon
%{_sbindir}/rc%{name}
%{_libexecdir}/%{name}/
%dir %{_libexecdir}/modules-load.d/
%{_libexecdir}/modules-load.d/pkcs8.conf
%{_unitdir}/%{name}.service
%if 0%{?suse_version} >= 1500
%dir %{_datadir}/dbus-1/system.d/
%{_datadir}/dbus-1/system.d/%{name}*.conf
%else
%{_sysconfdir}/dbus-1/system.d/%{name}*.conf
%endif
%{_datadir}/dbus-1/system-services/*%{name}.service

%changelog
