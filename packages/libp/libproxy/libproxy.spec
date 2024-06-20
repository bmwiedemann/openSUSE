#
# spec file for package libproxy
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


%define flavor @BUILD_FLAVOR@%nil
%if "%{flavor}" == ""
ExclusiveArch:  do-not-build
%else
%if "%{flavor}" == "client"
  %define name_suffix %{flavor}
  %define dash -
  %define mini -mini
%else
  %define name_suffix %{flavor}
  %define dash -
%endif
%endif

%define _name   libproxy
Name:           libproxy%{?dash}%{?name_suffix}
Version:        0.5.7
Release:        0
Summary:        Automatic proxy configuration management for applications
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            http://libproxy.github.io/libproxy/
Source:         %{_name}-%{version}.tar.zst
Source99:       baselibs.conf
BuildRequires:  meson
BuildRequires:  sysuser-tools
BuildRequires:  vala
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
%if "%{flavor}" == "backend"
BuildRequires:  pkgconfig(duktape)
BuildRequires:  pkgconfig(gi-docgen)
BuildRequires:  pkgconfig(gsettings-desktop-schemas)
BuildRequires:  pkgconfig(libcurl)
#!BuildIgnore:  libproxy1
# We require a config module, at worst the env reader
Requires:       PxPlugin(config)
# the env reader is part of this package
Provides:       PxPlugin(config)
# If pac/wpad is used, we need to interpret it
Recommends:     PxPlugin(pacrunner)
# config plugins envvar and sysconfig are shipped with the daemon
Provides:       PxPlugin(config)
%endif

%description
libproxy is a library that provides automatic proxy configuration
management.

%package -n libproxy-tools
Summary:        An example application using libproxy
Group:          System/Libraries
Requires:       libproxy1 = %{version}

%description -n libproxy-tools
An example application that will use libproxy to give the results that can
be expected from other applications. It can be used to debug what would
happen in various cases.

%package -n libproxy-devel
Summary:        Development files for libproxy, a library to do PAC/WPAD
Group:          Development/Libraries/C and C++
Requires:       libproxy1 = %{version}

%description -n libproxy-devel
libproxy is a library that provides automatic proxy configuration
management.

This subpackage contains header files for developing applications
that want to make use of libproxy.

%package -n libproxy-devel-doc
Summary:        Libproxy developers documentation
BuildArch:      noarch

%description -n libproxy-devel-doc
The developers documentation to libproxy (consumer library)

%package -n libproxy1
Summary:        Automatic proxy configuration management for applications
Group:          System/Libraries
# Starting with version 0.5.0, libproxy, the client library, has no plugins
# all plugins are moved to the backend
Obsoletes:      libproxy1-config-gnome3 < 0.5
Obsoletes:      libproxy1-config-kde < 0.5
Obsoletes:      libproxy1-networkmanager < 0.5
Obsoletes:      libproxy1-pacrunner-duktape < 0.5
Obsoletes:      libproxy1-pacrunner-webkit < 0.5

%description -n libproxy1
libproxy is a library that provides automatic proxy configuration
management.

Proxy autoconfiguration (PAC) requires JavaScript (which most
applications do not have), and determing the PAC script location
requires a WPAD protocol implementation, which complicates proxy
support. libproxy exists to abstract this issue and provides
an answer how to reach a certain network resource.

%package -n libpxbackend-1_0%{?mini}
Summary:        Backend library for libproxy, handles plugin loading
Group:          System/Libraries
%if "%{flavor}" == "client"
Conflicts:      libpxbackend-1_0
Requires:       this-is-only-for-build-envs
%endif

%description -n libpxbackend-1_0%{?mini}
libproxy is a library that provides automatic proxy configuration
management.

Proxy autoconfiguration (PAC) requires JavaScript (which most
applications do not have), and determing the PAC script location
requires a WPAD protocol implementation, which complicates proxy
support. libproxy exists to abstract this issue and provides
an answer how to reach a certain network resource.

%package -n typelib-1_0-Libproxy-1_0
Summary:        Gobject introspected access to libproxy

%description -n typelib-1_0-Libproxy-1_0
Libproxy is using gobject-introspection and is thus usable
from a wide range of programming languages.

%prep
%autosetup -p1 -n %{_name}-%{version}

%build
%meson \
%if "%{flavor}" == "client"
  -Dcurl=false \
  -Dconfig-gnome=false \
  -Dpacrunner-duktape=false \
  -Ddocs=false \
  -Dtests=false \
%endif
%nil
%meson_build

%install
%meson_install

%if "%{flavor}" == "backend"
# this stuff is already shipped as part of the client library (built without cURL to break cycles)
rm      %{buildroot}%{_bindir}/proxy
rm      %{buildroot}%{_mandir}/man8/proxy*
rm      %{buildroot}%{_libdir}/libproxy.so*
rm      %{buildroot}%{_libdir}/girepository-1.0/Libproxy*.typelib
rm -rf  %{buildroot}%{_includedir}/libproxy
rm -rf  %{buildroot}%{_datadir}/gir-1.0
rm -rf  %{buildroot}%{_datadir}/vala
rm      %{buildroot}%{_libdir}/pkgconfig/libproxy-1.0.pc
%endif

%if "%{flavor}" == "backend"
%check
%meson_test ||:
%endif

%ldconfig_scriptlets -n libpxbackend-1_0%{?mini}

%if "%{flavor}" == "client"
%ldconfig_scriptlets -n libproxy1
%endif

%if "%{flavor}" == "client"
%files -n libproxy1
%{_libdir}/libproxy.so.*

%files -n libpxbackend-1_0%{?mini}
%dir %{_libdir}/libproxy
%{_libdir}/libproxy/libpxbackend-1.0.so

%files -n libproxy-tools
%{_bindir}/proxy
%{_mandir}/man8/proxy.8%{?ext_man}

%files -n typelib-1_0-Libproxy-1_0
%{_libdir}/girepository-1.0/Libproxy-1.0.typelib

%files -n libproxy-devel
%{_datadir}/gir-1.0/Libproxy-1.0.gir
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/libproxy-1.0.*
%{_includedir}/libproxy/
%{_libdir}/libproxy.so
%{_libdir}/pkgconfig/libproxy-1.0.pc
%endif

%if "%{flavor}" == "backend"
%files -n libpxbackend-1_0
%dir %{_libdir}/libproxy
%{_libdir}/libproxy/libpxbackend-1.0.so

%files -n libproxy-devel-doc
%{_datadir}/doc/libproxy-1.0
%endif

%changelog
