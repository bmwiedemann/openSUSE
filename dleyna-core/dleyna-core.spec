#
# spec file for package dleyna-core
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


%define _sover 5

Name:           dleyna-core
Version:        0.6.0
Release:        0
Summary:        Utility functions used by higher level dLeyna libraries
License:        LGPL-2.1-only
Group:          Productivity/Multimedia/Other
Url:            http://01.org/dleyna
Source:         https://01.org/sites/default/files/downloads/dleyna/%{name}-%{version}.tar_3.gz
# PATCH-FIX-UPSTREAM dleyna-core-port-to-gupnp1_2.patch -- Port to gupnp-1.2
Patch0:         dleyna-core-port-to-gupnp1_2.patch

BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gio-2.0) >= 2.28
BuildRequires:  pkgconfig(glib-2.0) >= 2.28
BuildRequires:  pkgconfig(gmodule-2.0) >= 2.28
BuildRequires:  pkgconfig(gupnp-1.2) >= 1.2.0

%description
dleyna-core is a library of utility functions that are used by the higher level dLeyna libraries that
communicate with DLNA devices, e.g., dleyna-server.

In brief, it provides APIs for logging, error, settings and task management and an IPC abstraction API.

%package -n libdleyna-core-1_0-%{_sover}
Summary:        Utility functions used by higher level dLeyna libraries
Group:          System/Libraries

%description -n libdleyna-core-1_0-%{_sover}
dleyna-core is a library of utility functions that are used by the higher level dLeyna libraries that
communicate with DLNA devices, e.g., dleyna-server.

In brief, it provides APIs for logging, error, settings and task management and an IPC abstraction API.

%package devel
Summary:        Development files for the dLeyna libraries
Group:          Development/Languages/C and C++
Requires:       libdleyna-core-1_0-%{_sover} = %{version}

%description devel
dleyna-core is a library of utility functions that are used by the higher level dLeyna libraries that
communicate with DLNA devices, e.g., dleyna-server.

In brief, it provides APIs for logging, error, settings and task management and an IPC abstraction API.

%prep
%autosetup -p1

%build
autoreconf -fi
%configure \
	--disable-static \
	%{nil}
make %{?_smp_mflags}

%install
%make_install
find %{buildroot}%{_libdir} -type f -name '*.la' -delete -print

%post -n libdleyna-core-1_0-%{_sover} -p /sbin/ldconfig
%postun -n libdleyna-core-1_0-%{_sover} -p /sbin/ldconfig

%files -n libdleyna-core-1_0-%{_sover}
%license COPYING
%{_libdir}/libdleyna-core-1.0.so.*

%files devel
%doc ChangeLog README
%{_includedir}/dleyna-1.0/
%{_libdir}/libdleyna-core-1.0.so
%{_libdir}/pkgconfig/dleyna-core-1.0.pc

%changelog
