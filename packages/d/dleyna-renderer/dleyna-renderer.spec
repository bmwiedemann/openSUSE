#
# spec file for package dleyna-renderer
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           dleyna-renderer
Version:        0.6.0
Release:        0
Summary:        Discover and manipulate Digital Media Renderers
License:        LGPL-2.1
Group:          System/Libraries
Url:            http://01.org/dleyna
Source:         https://01.org/sites/default/files/downloads/dleyna/%{name}-%{version}.tar_2.gz

BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(dleyna-core-1.0) >= 0.6.0
BuildRequires:  pkgconfig(gio-2.0) >= 2.28
BuildRequires:  pkgconfig(glib-2.0) >= 2.28
BuildRequires:  pkgconfig(gssdp-1.0) >= 0.13.2
BuildRequires:  pkgconfig(gupnp-1.0) >= 0.20.5
BuildRequires:  pkgconfig(gupnp-av-1.0) >= 0.11.5
BuildRequires:  pkgconfig(gupnp-dlna-2.0) >= 0.9.4
BuildRequires:  pkgconfig(libsoup-2.4) >= 2.28.2
Provides:       dbus(dleyna-renderer-service) = %{version}
Requires:       dleyna-connector(dbus)

%description
dleyna-renderer is a library for implementing services that allow clients to discover and manipulate
Digital Media Renderers. An implementation of such a service for linux is also included

%package devel
Summary:        Discover and manipulate Digital Media Renderers -- Development files
Group:          Development/Languages/C and C++
Requires:       %{name} = %{version}

%description devel
dleyna-renderer is a library for implementing services that allow clients to discover and manipulate
Digital Media Renderers. An implementation of such a service for linux is also included

%prep
%setup -q

%build
autoreconf -fi
%configure \
	--disable-static \
	%{nil}
make %{?_smp_mflags}

%install
%make_install
find %{buildroot}%{_libdir} -type f -name '*.la' -delete -print

%files
%license COPYING
%doc ChangeLog README
%dir %{_datadir}/dbus-1
%dir %{_datadir}/dbus-1/services
%{_datadir}/dbus-1/services/com.intel.dleyna-renderer.service
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/libdleyna-renderer-1.0.so.*
%{_libexecdir}/dleyna-renderer-service
%config %{_sysconfdir}/dleyna-renderer-service.conf

%files devel
%{_includedir}/dleyna-1.0/
%{_libdir}/%{name}/libdleyna-renderer-1.0.so
%{_libdir}/pkgconfig/dleyna-renderer-service-1.0.pc

%changelog
