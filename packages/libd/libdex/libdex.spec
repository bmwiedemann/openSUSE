#
# spec file for package libdex
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


%define soname libdex-1-1
%bcond_with profiling

Name:           libdex
Version:        0.6.1
Release:        0
Summary:        Library supporting "Deferred Execution" for GNOME and GTK
License:        LGPL-2.1-or-later
URL:            https://gitlab.gnome.org/chergert/libdex
Source0:        %{name}-%{version}.tar.zst

BuildRequires:  c_compiler
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(atomic_ops)
BuildRequires:  pkgconfig(gi-docgen)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(liburing)
%if %{with profiling}
BuildRequires:  pkgconfig(sysprof-capture-4)
%endif
BuildRequires:  pkgconfig(vapigen)

%description
Dex is a library supporting "Deferred Execution" with the explicit
goal of integrating with GNOME and GTK-based applications.
It provides primatives for supporting futures in a variety of ways
with both read-only and writable views. Additionally, integration
with existing asynchronous-based APIs is provided through the use
of wrapper promises.
"Fibers" are implemented which allows for writing synchronous
looking code which calls asynchronous APIs from GIO underneath.

%package -n %soname
Summary:        Shared library for %name

%description -n %soname
Dex is a library supporting "Deferred Execution" with the explicit
goal of integrating with GNOME and GTK-based applications.
It provides primatives for supporting futures in a variety of ways
with both read-only and writable views. Additionally, integration
with existing asynchronous-based APIs is provided through the use
of wrapper promises.
"Fibers" are implemented which allows for writing synchronous
looking code which calls asynchronous APIs from GIO underneath.

This package contains the shared library for %name.

%package -n typelib-1_0-Dex-1_0
Summary:        Introspection bindings for %name

%description -n typelib-1_0-Dex-1_0
This package contains the introspection bindings for %name.

%package  devel
Summary:        Development files for libdex
Requires:       %soname = %{version}
Requires:       typelib-1_0-Dex-1_0 = %{version}

%description devel
This package contains the libraries and header files that are
needed for writing applications with libdex.

%package   devel-docs
Summary:        Developer documentation for libdex
BuildArch:      noarch

%description devel-docs
This package contains developer documentation for writing
applications with libdex.

%prep
%autosetup -p1

%build
%meson \
	-D docs=true \
	-D examples=false \
	-D sysprof=%{?with_profiling:true}%{!?with_profiling:false} \
	%{nil}
%meson_build

%install
%meson_install

%check
%meson_test

%ldconfig_scriptlets -n %soname

%files -n %soname
%license COPYING
%{_libdir}/libdex-1.so.1{,.*}

%files -n typelib-1_0-Dex-1_0
%{_libdir}/girepository-1.0/Dex-1.typelib

%files devel
%{_datadir}/gir-1.0/
%{_datadir}/vala/
%{_includedir}/libdex-1/
%{_libdir}/libdex-1.so
%{_libdir}/pkgconfig/libdex-1.pc

%files devel-docs
%doc NEWS README.md
%doc %{_datadir}/doc/libdex-1/

%changelog
