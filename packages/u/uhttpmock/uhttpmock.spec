#
# spec file for package uhttpmock
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2013 Dominique Leuenberger, Amsterdam, The Netherlands.
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


Name:           uhttpmock
Version:        0.5.1
Release:        0
Summary:        HTTP web service mocking library
License:        LGPL-2.1-or-later
Group:          Development/Tools/Other
Url:            https://gitlab.com/uhttpmock/uhttpmock
Source0:        https://tecnocode.co.uk/downloads/uhttpmock/%{name}-%{version}.tar.xz
BuildRequires:  gobject-introspection-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gio-2.0) >= 2.36.0
BuildRequires:  pkgconfig(glib-2.0) >= 2.31.0
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(libsoup-2.4) >= 2.47.3
BuildRequires:  pkgconfig(vapigen)

%description
uhttpmock is a project for mocking web service APIs which use HTTP or HTTPS.
It provides a library, libuhttpmock, which implements recording and
playback of HTTP request/response traces.

%package -n libuhttpmock-0_0-0
Summary:        HTTP web service mocking library
Group:          System/Libraries

%description -n libuhttpmock-0_0-0
uhttpmock is a project for mocking web service APIs which use HTTP or HTTPS.
It provides a library, libuhttpmock, which implements recording and
playback of HTTP request/response traces.

%package -n typelib-1_0-Uhm-0_0
Summary:        HTTP web service mocking library
Group:          System/Libraries

%description -n typelib-1_0-Uhm-0_0
uhttpmock is a project for mocking web service APIs which use HTTP or HTTPS.
It provides a library, libuhttpmock, which implements recording and
playback of HTTP request/response traces.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries/Other
Requires:       libuhttpmock-0_0-0 = %{version}
Requires:       typelib-1_0-Uhm-0_0 = %{version}

%description devel
This package contains libraries, header files and documentation for
developing applications that use %{name}.

%prep
%setup -q

%build
%configure \
    --disable-static
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n libuhttpmock-0_0-0 -p /sbin/ldconfig
%postun -n libuhttpmock-0_0-0 -p /sbin/ldconfig

%files -n libuhttpmock-0_0-0
%license COPYING
%doc README NEWS AUTHORS
%{_libdir}/libuhttpmock-0.0.so.*

%files -n typelib-1_0-Uhm-0_0
%{_libdir}/girepository-1.0/Uhm-0.0.typelib

%files devel
%doc %{_datadir}/gtk-doc/html/libuhttpmock-0.0/
%{_libdir}/*.so
%{_includedir}/libuhttpmock-0.0/
%{_libdir}/pkgconfig/libuhttpmock-0.0.pc
%{_datadir}/gir-1.0/Uhm-0.0.gir
%{_datadir}/vala/vapi/

%changelog
