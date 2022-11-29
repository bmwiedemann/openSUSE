#
# spec file for package dLeyna
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



Name:           dLeyna
Version:        0.8.2
Release:        0
Summary:        Services and D-Bus APIs to access UPnP and DLNA media devices in a network
License:        LGPL-2.1-or-later
URL:            https://gitlab.gnome.org/World/dLeyna
Source0:        %{name}-%{version}.tar.xz

BuildRequires:  meson >= 0.54.0
BuildRequires:  pkgconfig
BuildRequires:  docutils
BuildRequires:  pkgconfig(glib-2.0) >= 2.28
BuildRequires:  pkgconfig(gio-2.0) >= 2.28
BuildRequires:  pkgconfig(gssdp-1.6) >= 1.6.0
BuildRequires:  pkgconfig(gupnp-1.6) >= 1.6.0
BuildRequires:  pkgconfig(gupnp-av-1.0) >= 0.12.9
BuildRequires:  pkgconfig(gupnp-dlna-2.0) >= 0.9.4
BuildRequires:  pkgconfig(libsoup-3.0) >= 3.0
BuildRequires:  pkgconfig(libxml-2.0)

Obsoletes:      dleyna-renderer < 0.7.3
Provides:       dleyna-renderer = %{version}
Obsoletes:      dleyna-server < 0.7.3
Provides:       dleyna-server = %{version}
Obsoletes:      dleyna-core < 0.7.3
Provides:       dleyna-core = %{version}
Obsoletes:      dleyna-connector-dbus < 0.4.2
Provides:       dleyna-connector-dbus = %{version}
Obsoletes:      libdleyna-core-1_0-6 < 0.7.1
Provides:       libdleyna-core-1_0-6 = %{version}
# Re-add dbus() provides from dleyna server
Provides:       dbus(com.intel.dleyna-server)
Provides:       dbus(com.intel.dleyna-renderer)

%description
dLeyna is a set of services and D-Bus APIs that aim to simplify
access to UPnP and DLNA media devices in a network.

%package devel
Summary:        Development files for the dLeyna libraries
Requires:       %{name} = %{version}
Provides:       dleyna-core-devel = %{version}
Obsoletes:      dleyna-core-devel < 0.7.3
Provides:       dleyna-renderer-devel = %{version}
Obsoletes:      dleyna-renderer-devel < 0.7.3
Provides:       dleyna-server-devel = %{version}
Obsoletes:      dleyna-server-devel < 0.7.3

%description devel
dleyna is a library of utility functions that are used by the
higher level dLeyna libraries that communicate with DLNA devices,
e.g., dleyna-server.

In brief, it provides APIs for logging, error, settings and task
management and an IPC abstraction API.

%prep
%autosetup -p1

%build
%meson \
	-D docs=false \
	%{nil}
%meson_build

%install
%meson_install

%ldconfig_scriptlets

%files
%license COPYING
%doc NEWS README.md
%config %{_sysconfdir}/dleyna-renderer-service.conf
%config %{_sysconfdir}/dleyna-server-service.conf
%dir %{_libdir}/dleyna-1.0
%dir %{_libdir}/dleyna-1.0/connectors
%{_libdir}/dleyna-1.0/connectors/libdleyna-connector-dbus.so
%dir %{_libdir}/dleyna-server
%{_libdir}/dleyna-server/libdleyna-server-1.0.so.*
%dir %{_libdir}/dleyna
%{_libdir}/dleyna/libdleyna-renderer-1.0.so.*
%{_libexecdir}/dleyna-renderer-service
%{_libexecdir}/dleyna-server-service
%dir %{_datadir}/dbus-1
%dir %{_datadir}/dbus-1/services
%{_datadir}/dbus-1/services/com.intel.dleyna-renderer.service
%{_datadir}/dbus-1/services/com.intel.dleyna-server.service
%{_mandir}/man1/dleyna-renderer-service.1%{?ext_man}
%{_mandir}/man1/dleyna-server-service.1%{?ext_man}
%{_mandir}/man5/dleyna-renderer-service.conf.5%{?ext_man}
%{_mandir}/man5/dleyna-server-service.conf.5%{?ext_man}
%{_libdir}/libdleyna-core-1.0.so.*
%dir %{python_sitelib}/dLeyna
%{python_sitelib}/dLeyna/download_sync_controller.py
%{python_sitelib}/dLeyna/mediaconsole.py
%{python_sitelib}/dLeyna/rendererconsole.py
%{python_sitelib}/dLeyna/upload_sync_controller.py

%files devel
%{_includedir}/dleyna-1.0/
%{_libdir}/dleyna-server/libdleyna-server-1.0.so
%{_libdir}/dleyna/libdleyna-renderer-1.0.so
%{_libdir}/libdleyna-core-1.0.so
%{_libdir}/pkgconfig/dleyna-core-1.0.pc
%{_libdir}/pkgconfig/dleyna-renderer-service-1.0.pc
%{_libdir}/pkgconfig/dleyna-server-service-1.0.pc

%changelog
