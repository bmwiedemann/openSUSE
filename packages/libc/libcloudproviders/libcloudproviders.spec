#
# spec file for package libcloudproviders
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define _typelibdir %(pkg-config --variable=typelibdir gobject-introspection-1.0)
%define _girdir %(pkg-config --variable=girdir gobject-introspection-1.0)
Name:           libcloudproviders
Version:        0.4.0
Release:        0
Summary:        Library/Client to integrate cloud storage providers
License:        LGPL-3.0-or-later
Group:          System/GUI/GNOME
URL:            https://gitlab.gnome.org/World/libcloudproviders
Source0:        %{name}-%{version}.tar.zst

BuildRequires:  meson >= 1.9.0
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gio-2.0) >= 2.51.2
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.51.2
BuildRequires:  pkgconfig(glib-2.0) >= 2.51.2
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(vapigen)

%description
Cross desktop library for desktop integration of cloud storage
providers and sync tools.

%package -n libcloudproviders0
Summary:        Library to integrate cloud storage providers
Group:          System/Libraries

%description -n libcloudproviders0
Cross desktop library for desktop integration of cloud storage
providers and sync tools.

%package -n     typelib-1_0-CloudProviders-0_3_0
Summary:        CloudProviders Introspection bindings
Group:          Development/Libraries/GNOME

%description -n typelib-1_0-CloudProviders-0_3_0
Cross desktop library for desktop integration of cloud storage
providers and sync tools.

This package provides the GObject Introspection bindings for cloudproviders.

%package devel
Summary:        Development files for %{name}
Group:          Development/Languages/C and C++
Requires:       libcloudproviders0 = %{version}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1

%build
%meson \
    %{nil}
%meson_build

%install
%meson_install

%check
%meson_test

%ldconfig_scriptlets -n libcloudproviders0

%files -n libcloudproviders0
%license LICENSE
%doc CHANGELOG README.md
%{_libdir}/libcloudproviders.so.*

%files -n typelib-1_0-CloudProviders-0_3_0
%{_typelibdir}/*.typelib

%files devel
%{_includedir}/cloudproviders/
%{_libdir}/libcloudproviders.so
%{_libdir}/pkgconfig/cloudproviders.pc
%{_libdir}/*.so
%{_girdir}/*.gir
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/*.deps
%{_datadir}/vala/vapi/*.vapi

%changelog
