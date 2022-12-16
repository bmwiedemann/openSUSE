#
# spec file for package libzeitgeist
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2011 Federico Mena Quintero
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


Name:           libzeitgeist
Version:        0.3.18
Release:        0
Summary:        Client library for interacting with the Zeitgeist daemon
License:        LGPL-2.1-or-later
Group:          Productivity/Other
URL:            https://launchpad.net/libzeitgeist
Source0:        %{name}-%{version}.tar.gz
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(glib-2.0)

%description
Libzeitgeist is a client library for interacting with the Zeitgeist
daemon.

%package -n libzeitgeist-1_0-1
Summary:        Client library for interacting with the Zeitgeist daemon
Group:          System/Libraries
Recommends:     zeitgeist

%description -n libzeitgeist-1_0-1
Libzeitgeist is a client library for interacting with the Zeitgeist
daemon.

%package devel
Summary:        Client library for interacting with the Zeitgeist daemon -- Development Files
Group:          Development/Libraries/GNOME
Requires:       libzeitgeist-1_0-1 = %{version}

%description devel
Libzeitgeist is a client library for interacting with the Zeitgeist
daemon.

%prep
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
# We ship those as %%doc, except INSTALL but we don't care about it
rm %{buildroot}%{_datadir}/doc/libzeitgeist/{AUTHORS,COPYING,INSTALL,MAINTAINERS,README}

%post -n libzeitgeist-1_0-1 -p /sbin/ldconfig
%postun -n libzeitgeist-1_0-1 -p /sbin/ldconfig

%files -n libzeitgeist-1_0-1
%license COPYING
%doc AUTHORS ChangeLog MAINTAINERS NEWS README
%{_libdir}/lib*.so.*

%files devel
%{_includedir}/zeitgeist-1.0/
%{_libdir}/pkgconfig/zeitgeist-1.0.pc
%{_libdir}/lib*.so
%doc %{_datadir}/gtk-doc/html/zeitgeist-1.0/
# Own these directories to not depend on vala
%dir %{_datadir}/vala
%{_datadir}/vala/vapi/

%changelog
