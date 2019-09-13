#
# spec file for package libgovirt
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


Name:           libgovirt
Version:        0.3.6
Release:        0
Summary:        GObject based oVirt bindings
License:        LGPL-2.1-or-later
Group:          Development/Libraries/GNOME
Url:            http://cgit.freedesktop.org/~teuf/govirt
Source:         http://download.gnome.org/sources/libgovirt/0.3/%{name}-%{version}.tar.xz
BuildRequires:  gobject-introspection-devel >= 1.30.0
BuildRequires:  intltool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gio-2.0) >= 2.26.0
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gthread-2.0) >= 2.26.0
BuildRequires:  pkgconfig(rest-0.7) >= 0.7.92

%description
GoVirt is a GObject wrapper for the oVirt REST API [1]. It will
only provide very basic functionality as the goal is to
autogenerate a full wrapper as it is already done for the python
bindings.

%package -n libgovirt2
Summary:        GObject based oVirt bindings
Group:          System/Libraries
Recommends:     %{name}-lang
# To make the lang package installable
Provides:       %{name} = %{version}

%description -n libgovirt2
GoVirt is a GObject wrapper for the oVirt REST API [1]. It will
only provide very basic functionality as the goal is to
autogenerate a full wrapper as it is already done for the python
bindings.

%package -n typelib-1_0-GoVirt-1_0
Summary:        Introspection bindings for the GObject-based oVirt bindings
Group:          System/Libraries

%description -n typelib-1_0-GoVirt-1_0
GoVirt is a GObject wrapper for the oVirt REST API [1]. It will
only provide very basic functionality as the goal is to
autogenerate a full wrapper as it is already done for the python
bindings.

%package devel
Summary:        Development files for the GObject-based oVirt bindings
Group:          Development/Languages/C and C++
Requires:       libgovirt2 = %{version}
Requires:       typelib-1_0-GoVirt-1_0 = %{version}

%description devel
GoVirt is a GObject wrapper for the oVirt REST API [1]. It will
only provide very basic functionality as the goal is to
autogenerate a full wrapper as it is already done for the python
bindings.

%lang_package

%prep
%setup -q

%build
%configure \
    --disable-static
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
%find_lang %{name} %{?no_lang_C}

%post -n libgovirt2 -p /sbin/ldconfig
%postun -n libgovirt2 -p /sbin/ldconfig

%files -n libgovirt2
%license COPYING
%doc README
%{_libdir}/libgovirt.so.*

%files -n typelib-1_0-GoVirt-1_0
%{_libdir}/girepository-1.0/GoVirt-1.0.typelib

%files devel
%{_datadir}/gir-1.0/GoVirt-1.0.gir
%{_includedir}/govirt-1.0/
%{_libdir}/libgovirt.so
%{_libdir}/pkgconfig/govirt-1.0.pc

%files lang -f %{name}.lang

%changelog
