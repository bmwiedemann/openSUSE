#
# spec file for package low-memory-monitor
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


Name:           low-memory-monitor
Version:        2.1
Release:        0
Summary:        Early boot daemon to monitor memory pressure and react to low memory
License:        GPL-3.0-only
URL:            https://gitlab.freedesktop.org/hadess/low-memory-monitor
Source:         %{url}/-/archive/%{version}/%{name}-%{version}.tar.bz2
Patch0:	harden_low-memory-monitor.service.patch
BuildRequires:  gtk-doc
BuildRequires:  meson >= 0.45.0
BuildRequires:  pkgconfig
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(systemd)
%{?systemd_requires}

%description
The Low Memory Monitor is an early boot daemon that will monitor memory
pressure information coming from the kernel, and, when memory pressure means
that memory isn't as readily available and would cause interactivity problems,
would:
* send D-Bus signals to user-space applications when memory is running low,
* if configured to do so and memory availability worsens, activate the kernel's
  OOM killer.

%package doc
Summary:        Documentation for %{name}

%description doc
This package provides documentation for %{name}.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%pre
%service_add_pre %{name}.service

%preun
%service_del_preun %{name}.service

%post
%service_add_post %{name}.service

%postun
%service_del_postun %{name}.service

%files
%license COPYING
%doc NEWS README.md
# Dir ownership only needed for Leap <= 15.2
%dir %{_datadir}/dbus-1
%dir %{_datadir}/dbus-1/system.d
%{_datadir}/dbus-1/system.d/org.freedesktop.LowMemoryMonitor.conf
%{_libexecdir}/%{name}
%{_unitdir}/%{name}.service

%files doc
%doc %{_datadir}/gtk-doc/html/%{name}

%changelog
