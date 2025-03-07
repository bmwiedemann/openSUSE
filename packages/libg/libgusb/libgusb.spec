#
# spec file for package libgusb
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


Name:           libgusb
Version:        0.4.9
Release:        0
Summary:        GObject-based library for libusb1
License:        LGPL-2.1-or-later
Group:          Development/Libraries/GNOME
URL:            https://github.com/hughsie/libgusb
Source0:        %{url}/releases/download/%{version}/%{name}-%{version}.tar.xz
Source99:       baselibs.conf
# PATCH-FIX-UPSTREAM no-pkg-resources.patch gh#hughsie/libgusb#61 mcepl@suse.com -- Don't rely on the obsolete version of pkg_resources
Patch0:         no-pkg-resources.patch
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  vala
BuildRequires:  (python3-packaging if python3-base)
BuildRequires:  (python311-packaging if python311-base)
BuildRequires:  pkgconfig(gi-docgen)
BuildRequires:  pkgconfig(glib-2.0) >= 2.44.0
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= 1.29
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libusb-1.0) >= 1.0.19

%description
GUsb is a GObject wrapper for libusb1 that makes it easy to do
asynchronous control, bulk and interrupt transfers with proper
cancellation and integration into a mainloop.

%package -n libgusb2
Summary:        GObject-based library for libusb1
Group:          System/Libraries

%description -n libgusb2
GUsb is a GObject wrapper for libusb1 that makes it easy to do
asynchronous control, bulk and interrupt transfers with proper
cancellation and integration into a mainloop.

%package -n typelib-1_0-GUsb-1_0
Summary:        Introspection bindings for libgusb, a GObject-based wrapper for libusb1
Group:          System/Libraries

%description -n typelib-1_0-GUsb-1_0
GUsb is a GObject wrapper for libusb1 that makes it easy to do
asynchronous control, bulk and interrupt transfers with proper
cancellation and integration into a mainloop.

%package devel
Summary:        Development files for libgusb, a GObject-based wrapper for libusb1
Group:          Development/Libraries/C and C++
Requires:       libgusb2 = %{version}
Requires:       typelib-1_0-GUsb-1_0 = %{version}

%description devel
GUsb is a GObject wrapper for libusb1 that makes it easy to do
asynchronous control, bulk and interrupt transfers with proper
cancellation and integration into a mainloop.

%prep
%autosetup -p1

%build
%meson \
	-D tests=false \
	%{nil}
%meson_build

%install
%meson_install

%ldconfig_scriptlets -n libgusb2

%files -n libgusb2
%license COPYING
%doc AUTHORS NEWS
%{_libdir}/libgusb.so.?
%{_libdir}/libgusb.so.?.0.*

%files -n typelib-1_0-GUsb-1_0
%{_libdir}/girepository-1.0/GUsb-1.0.typelib

%files devel
%doc %{_datadir}/doc/libgusb
%{_bindir}/gusbcmd
%{_datadir}/gir-1.0/GUsb-1.0.gir
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/gusb.deps
%{_datadir}/vala/vapi/gusb.vapi
%{_includedir}/gusb-1/
%{_libdir}/libgusb.so
%{_libdir}/pkgconfig/gusb.pc

%changelog
