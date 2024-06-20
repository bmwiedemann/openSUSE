#
# spec file for package uhttpmock
#
# Copyright (c) 2024 SUSE LLC
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
Version:        0.11.0
Release:        0
Summary:        HTTP web service mocking library
License:        LGPL-2.1-or-later
Group:          Development/Tools/Other
URL:            https://gitlab.freedesktop.org/pwithnall/uhttpmock
Source0:        %{name}-%{version}.tar.zst

BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gio-2.0) >= 2.38.0
BuildRequires:  pkgconfig(glib-2.0) >= 2.38.0
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(libsoup-3.0) >= 3.1.2
BuildRequires:  pkgconfig(vapigen)

%description
uhttpmock is a project for mocking web service APIs which use HTTP or HTTPS.
It provides a library, libuhttpmock, which implements recording and
playback of HTTP request/response traces.

%package -n libuhttpmock-1_0-1
Summary:        HTTP web service mocking library
Group:          System/Libraries

%description -n libuhttpmock-1_0-1
uhttpmock is a project for mocking web service APIs which use HTTP or HTTPS.
It provides a library, libuhttpmock, which implements recording and
playback of HTTP request/response traces.

%package -n typelib-1_0-Uhm-1_0
Summary:        HTTP web service mocking library
Group:          System/Libraries

%description -n typelib-1_0-Uhm-1_0
uhttpmock is a project for mocking web service APIs which use HTTP or HTTPS.
It provides a library, libuhttpmock, which implements recording and
playback of HTTP request/response traces.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries/Other
Requires:       libuhttpmock-1_0-1 = %{version}
Requires:       typelib-1_0-Uhm-1_0 = %{version}

%description devel
This package contains libraries, header files and documentation for
developing applications that use %{name}.

%prep
%autosetup -p1

%build
%meson \
	-Dgtk_doc=true \
	-Dintrospection=true \
	-Dvapi=enabled \
	%{nil}
%meson_build

%install
%meson_install

%ldconfig_scriptlets -n libuhttpmock-1_0-1

%files -n libuhttpmock-1_0-1
%license COPYING
%doc README NEWS AUTHORS
%{_libdir}/libuhttpmock-1.0.so.*

%files -n typelib-1_0-Uhm-1_0
%{_libdir}/girepository-1.0/Uhm-1.0.typelib

%files devel
%doc %{_datadir}/gtk-doc/html/libuhttpmock-1.0/
%{_libdir}/*.so
%{_includedir}/libuhttpmock-1.0/
%{_libdir}/pkgconfig/libuhttpmock-1.0.pc
%{_datadir}/gir-1.0/Uhm-1.0.gir
%{_datadir}/vala/vapi/

%changelog
