#
# spec file for package dleyna-server
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2014 Dominique Leuenberger, Amsterdam, The Netherlands
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


Name:           dleyna-server
Version:        0.7.2
Release:        0
Summary:        A DLNA media server
License:        LGPL-2.1-only
Group:          Productivity/Multimedia/Other
URL:            https://github.com/phako/dleyna-server
Source:         %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(dleyna-core-1.0) >= 0.6.0
BuildRequires:  pkgconfig(gio-2.0) >= 2.36
BuildRequires:  pkgconfig(glib-2.0) >= 2.36
BuildRequires:  pkgconfig(gssdp-1.2) >= 0.13.2
BuildRequires:  pkgconfig(gupnp-1.2) >= 0.20.3
BuildRequires:  pkgconfig(gupnp-av-1.0) >= 0.12.9
BuildRequires:  pkgconfig(gupnp-dlna-2.0) >= 0.9.4
BuildRequires:  pkgconfig(libsoup-2.4) >= 2.28.2
BuildRequires:  pkgconfig(libxml-2.0)
# As dleyna-server publishes itself on DBus, it needs access to the DBus connector
Requires:       dleyna-connector-dbus
Provides:       dbus(com.intel.dleyna-server) = %{version}

%description
dLeyna-server can be used in conjunction with a multimedia framework, such as GStreamer,
to implement a Digital Media Player. It can also be used to implement the
DLNA Download System Use Case.

%package devel
Summary:        Development files for the dleyna DLNA media server
Group:          Development/Languages/C and C++
Requires:       %{name} = %{version}

%description devel
dLeyna-server can be used in conjunction with a multimedia framework, such as GStreamer,
to implement a Digital Media Player. It can also be used to implement the
DLNA Download System Use Case.

%prep
%autosetup -p1

%build
%meson \
	%{nil}
%meson_build

%install
%meson_install

%files
%license COPYING
%dir %{_datadir}/dbus-1
%dir %{_datadir}/dbus-1/services
%{_datadir}/dbus-1/services/com.intel.dleyna-server.service
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/libdleyna-server-1.0.so.*
%{_libexecdir}/dleyna-server-service
%config %{_sysconfdir}/dleyna-server-service.conf

%files devel
%doc ChangeLog README.md
%{_includedir}/dleyna-1.0/
%{_libdir}/%{name}/libdleyna-server-1.0.so
%{_libdir}/pkgconfig/dleyna-server-service-1.0.pc

%changelog
