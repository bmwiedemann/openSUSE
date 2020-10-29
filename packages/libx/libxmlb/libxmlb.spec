#
# spec file for package libxmlb
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2019 Bjørn Lie, Bryne, Norway.
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


%define sover 2

Name:           libxmlb
Version:        0.2.1
Release:        0
Summary:        Library for querying compressed XML metadata
License:        LGPL-2.1-or-later
Group:          Development/Libraries/Other
URL:            https://github.com/hughsie/libxmlb
Source0:        %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.xz

BuildRequires:  meson >= 0.47.0
# Enable when/if libstemmer becomes available in openSUSE (+ in meson call)
#BuildRequires:  libstemmer-devel
BuildRequires:  %{python_module setuptools}
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gio-2.0) >= 2.45.8
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk-doc)
# Needed for the self tests
BuildRequires:  pkgconfig(shared-mime-info)

%description
XML is slow to parse and strings inside the document cannot be
memory mapped as they do not have a trailing NUL char. The libxmlb
library takes XML source, and converts it to a structured binary
representation with a deduplicated string table -- where the
strings have the NULs included.

This allows an application to mmap the binary XML file, do an XPath
query and return some strings without actually parsing the entire
document. This is all done using (almost) zero allocations and no
actual copying of the binary data.

%package -n %{name}%{sover}
Summary:        Library for querying compressed XML metadata
Group:          System/Libraries

%description -n %{name}%{sover}
This package provides the shared library for %{name}.

%package -n typelib-1_0-Xmlb-1_0
Summary:        Introspection bindings for %{name}
Group:          System/Libraries

%description -n typelib-1_0-Xmlb-1_0
This package provides the GObject Introspection bindings for
%{name}.

%package -n xmlb-tool
Summary:        Optional tool for %{name}
Group:          Development/Libraries/Other

%description -n xmlb-tool
This package provides the optional xb-tool for %{name}.

%package devel
Summary:        Development package for %{name}
Group:          Development/Libraries/Other
Requires:       %{name}%{sover} = %{version}
Requires:       typelib-1_0-Xmlb-1_0 = %{version}
Requires:       xmlb-tool = %{version}

%description devel
Files for development with %{name}.

%prep
%autosetup -p1

%build
%meson \
	-Dgtkdoc=true \
	-Dintrospection=true \
	-Dtests=true \
#	-Dstemmer=true \
	%{nil}
%meson_build

%check
%meson_test

%install
%meson_install

%post -n %{name}%{sover} -p /sbin/ldconfig
%postun -n %{name}%{sover} -p /sbin/ldconfig

%files -n %{name}%{sover}
%license LICENSE
%{_libdir}/%{name}.so.%{sover}*

%files -n typelib-1_0-Xmlb-1_0
%{_libdir}/girepository-1.0/*.typelib

%files -n xmlb-tool
%doc README.md NEWS
%{_libexecdir}/xb-tool

%files devel
%doc %{_datadir}/gtk-doc/html/%{name}
%{_datadir}/gir-1.0/*.gir
%{_includedir}/%{name}-%{sover}/
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/xmlb.pc
%{_libexecdir}/installed-tests/
%{_datadir}/installed-tests/

%changelog
