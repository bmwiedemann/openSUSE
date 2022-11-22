#
# spec file for package gssdp
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


%define soname 1_6-0
%define sover 1.6
%bcond_with sniffer
Name:           gssdp
Version:        1.6.2
Release:        0
Summary:        Library for resource discovery and announcement over SSDP
License:        LGPL-2.0-or-later
Group:          Development/Libraries/C and C++
URL:            http://www.gupnp.org/
Source0:        https://download.gnome.org/sources/gssdp/1.6/%{name}-%{version}.tar.xz
Source1:        baselibs.conf

BuildRequires:  meson >= 0.54.0
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gi-docgen)
BuildRequires:  pkgconfig(glib-2.0) >= 2.54
BuildRequires:  pkgconfig(gobject-introspection-1.0)
%if %{with sniffer}
BuildRequires:  pkgconfig(gtk4)
%endif
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(vapigen)

%description
gssdp offers a GObject-based API for handling resource discovery and
announcement over SSDP.

%package utils
Summary:        Utilities for resource discovery and announcement over SSDP
Group:          Productivity/Networking/Other

%description utils
gssdp offers a GObject-based API for handling resource discovery and
announcement over SSDP.

This package contains a device sniffer.

%package -n libgssdp-%{soname}
Summary:        Library for resource discovery and announcement over SSDP
Group:          Development/Libraries/C and C++

%description -n libgssdp-%{soname}
gssdp offers a GObject-based API for handling resource discovery and
announcement over SSDP.

%package -n typelib-1_0-GSSDP-1_0
Summary:        Lib for resource discovery and announcement over SSDP - Introspection bindings
Group:          System/Libraries

%description -n typelib-1_0-GSSDP-1_0
gssdp offers a GObject-based API for handling resource discovery and
announcement over SSDP.

This package provides the GObject Introspection bindings for gssdp.

%package doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%description doc
Documentation for %{name}.

%package -n libgssdp-devel
Summary:        Library for resource discovery and announcement over SSDP - Development Files
Group:          Development/Libraries/C and C++
Requires:       libgssdp-%{soname} = %{version}
Requires:       typelib-1_0-GSSDP-1_0 = %{version}

%description -n libgssdp-devel
gssdp offers a GObject-based API for handling resource discovery and
announcement over SSDP.

%prep
%autosetup -p1

%build
%meson \
	-Dgtk_doc=true \
	-Dmanpages=false \
%if %{without sniffer}
	-Dsniffer=false \
%endif
	-Dintrospection=true \
	-Dvapi=true \
	-Dexamples=false \
	%{nil}
%meson_build

%install
%meson_install
# Make default docdir ref openSUSE standard
mkdir -p %{buildroot}%{_docdir}/%{name}-%{sover}
# Move docs from upstream docdir to openSUSE docdir standard
mv %{buildroot}%{_datadir}/doc/%{name}-%{sover} %{buildroot}%{_docdir}

%check
#%%meson_test

%ldconfig_scriptlets -n libgssdp-%{soname}

%if %{with sniffer}
%files utils
%{_bindir}/*
%endif

%files -n libgssdp-%{soname}
%license COPYING
%doc AUTHORS NEWS
%{_libdir}/*.so.*

%files -n typelib-1_0-GSSDP-1_0
%{_libdir}/girepository-1.0/GSSDP-%{sover}.typelib

%files doc
%doc %{_docdir}/%{name}-%{sover}/

%files -n libgssdp-devel
%{_includedir}/%{name}-%{sover}/
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gir-1.0/GSSDP-%{sover}.gir
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/gssdp-%{sover}.deps
%{_datadir}/vala/vapi/gssdp-%{sover}.vapi

%changelog
