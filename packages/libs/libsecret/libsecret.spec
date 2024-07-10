#
# spec file for package libsecret
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


%define have_lang 1
Name:           libsecret
Version:        0.21.4
Release:        0
Summary:        Library for accessing the Secret Service API
License:        LGPL-2.1-or-later
URL:            https://wiki.gnome.org/Projects/Libsecret
Source0:        %{name}-%{version}.tar.zst
Source99:       baselibs.conf

## SLE-only patches start at 1000
# PATCH-FIX-SLE libsecret-bsc932232-use-libgcrypt-allocators.patch bsc#932232 hpj@suse.com -- use libgcrypt allocators for FIPS mode
Patch1000:      libsecret-bsc932232-use-libgcrypt-allocators.patch

BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  fdupes
BuildRequires:  gobject-introspection-devel >= 1.29
BuildRequires:  libgcrypt-devel >= 1.2.2
BuildRequires:  meson >= 0.50
BuildRequires:  pkgconfig
BuildRequires:  vala >= 0.17.2.12
BuildRequires:  xsltproc
BuildRequires:  pkgconfig(gi-docgen)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.44.0

%description
libsecret is a library for storing and retrieving passwords and other
secrets. It communicates with the "Secret Service" using DBus.

%package -n libsecret-1-0
Summary:        Library for accessing the Secret Service API
%if %{have_lang}
# To make the lang package happy
Provides:       %{name} = %{version}
%endif

%description -n libsecret-1-0
libsecret is a library for storing and retrieving passwords and other
secrets. It communicates with the "Secret Service" using DBus.

%package -n typelib-1_0-Secret-1
Summary:        Introspection bindings for the Secret Service API library

%description -n typelib-1_0-Secret-1
libsecret is a library for storing and retrieving passwords and other
secrets. It communicates with the "Secret Service" using DBus.

This package provides the GObject Introspection bindings for libsecret.

%package -n secret-tool
Summary:        Store and retrieve passwords
Obsoletes:      libsecret-tools < %{version}
Provides:       libsecret-tools = %{version}

%description -n secret-tool
Secret-tool is a command line tool that can be used to store and
retrieve passwords.

%package devel
Summary:        Development files for the Secret Service API library
Requires:       libsecret-1-0 = %{version}
Requires:       typelib-1_0-Secret-1 = %{version}

%description devel
libsecret is a library for storing and retrieving passwords and other
secrets. It communicates with the "Secret Service" using DBus.

%if %{have_lang}
%lang_package
%endif

%prep
%autosetup -N

%if 0%{?sle_version}
%patch -P 1000 -p1
%endif

%build
%meson \
	%{nil}
%meson_build

%install
%meson_install
find %{buildroot} -type f -name "*.la" -delete -print
%if %{have_lang}
%find_lang %{name} %{?no_lang_C}
%endif
%fdupes %{buildroot}/%{_prefix}

%post -n libsecret-1-0 -p /sbin/ldconfig
%postun -n libsecret-1-0 -p /sbin/ldconfig

%files -n libsecret-1-0
%license COPYING
%doc NEWS README.md
%{_libdir}/libsecret-1.so.*

%files -n typelib-1_0-Secret-1
%{_libdir}/girepository-1.0/Secret-1.typelib

%files -n secret-tool
%{_bindir}/secret-tool
%{_mandir}/man1/secret-tool.1%{?ext_man}

%files devel
%{_libdir}/libsecret-1.so
%{_libdir}/pkgconfig/libsecret-1.pc
%{_libdir}/pkgconfig/libsecret-unstable.pc
%{_includedir}/libsecret-1/
%{_datadir}/gir-1.0/Secret-1.gir
%doc %{_datadir}/doc/libsecret-1/
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/libsecret-1.deps
%{_datadir}/vala/vapi/libsecret-1.vapi

%if %{have_lang}
%files lang -f %{name}.lang
%endif

%changelog
