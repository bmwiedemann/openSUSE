#
# spec file for package gtk-vnc
#
# Copyright (c) 2025 SUSE LLC
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


%define _sover -2_0-0
%define _sonamever 2.0
%define _sonamepkg 2_0

Name:           gtk-vnc
Version:        1.5.0
Release:        0
Summary:        A GTK widget for VNC clients
License:        LGPL-2.1-only AND LGPL-2.1-or-later
Group:          Development/Libraries/X11
URL:            https://wiki.gnome.org/Projects/gtk-vnc
Source0:        https://download.gnome.org/sources/gtk-vnc/1.5/%{name}-%{version}.tar.xz

BuildRequires:  cyrus-sasl-devel
BuildRequires:  gobject-introspection-devel >= 0.9.4
BuildRequires:  intltool
BuildRequires:  libgcrypt-devel >= 1.5.0
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  vala
BuildRequires:  pkgconfig(gio-2.0) >= 2.42.0
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.42.0
BuildRequires:  pkgconfig(gnutls) >= 3.1.18
BuildRequires:  pkgconfig(gobject-2.0) >= 2.42.0
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libpulse-simple)

%description
gtk-vnc is a VNC viewer widget for GTK+. It is built using coroutines
allowing it to be completely asynchronous while remaining single
threaded.

%package -n libgvnc-1_0-0
Summary:        GObject-based library to interact with the RFB protocol
License:        LGPL-2.1-only AND LGPL-2.1-or-later
Group:          Development/Libraries/X11

%description  -n libgvnc-1_0-0
gtk-vnc is a VNC viewer widget for GTK+. It is built using coroutines
allowing it to be completely asynchronous while remaining single
threaded.

This package contains the GObject-based library to interact with the
RFB protocol.

%package -n typelib-1_0-GVnc-1_0
Summary:        Introspection bindings for gtk-vnc
License:        LGPL-2.1-only AND LGPL-2.1-or-later
Group:          System/Libraries

%description -n typelib-1_0-GVnc-1_0
gtk-vnc is a VNC viewer widget for GTK+. It is built using coroutines
allowing it to be completely asynchronous while remaining single
threaded.

This package provides the GObject Introspection bindings for the libgvnc
library.

%package -n libgvncpulse-1_0-0
Summary:        Pulse audio bridge for VNC client connections
License:        LGPL-2.1-only AND LGPL-2.1-or-later
Group:          Development/Libraries/X11

%description  -n libgvncpulse-1_0-0
gtk-vnc is a VNC viewer widget for GTK+. It is built using coroutines
allowing it to be completely asynchronous while remaining single
threaded.

This package contains the Pulse audio bridge for VNC client connections.

%package -n typelib-1_0-GVncPulse-1_0
Summary:        Pulse audio bridge for VNC client connections -- Introspection bindings
License:        LGPL-2.1-only AND LGPL-2.1-or-later
Group:          System/Libraries

%description -n typelib-1_0-GVncPulse-1_0
gtk-vnc is a VNC viewer widget for GTK+. It is built using coroutines
allowing it to be completely asynchronous while remaining single
threaded.

This package provides the GObject Introspection bindings for the
libgvncpulse library.

%package -n libgtk-vnc%{_sover}
Summary:        A GTK widget for VNC clients
License:        LGPL-2.1-only AND LGPL-2.1-or-later
Group:          Development/Libraries/X11
# Needed to make lang package installable (and because we used to
# have a gtk-vnc package earlier).
Provides:       %{name} = %{version}
Obsoletes:      %{name} < %{version}

%description  -n libgtk-vnc%{_sover}
gtk-vnc is a VNC viewer widget for GTK+. It is built using coroutines
allowing it to be completely asynchronous while remaining single
threaded.

%package -n typelib-1_0-GtkVnc-%{_sonamepkg}
Summary:        A GTK widget for VNC clients -- Introspection bindings
License:        LGPL-2.1-only AND LGPL-2.1-or-later
Group:          System/Libraries

%description -n typelib-1_0-GtkVnc-%{_sonamepkg}
gtk-vnc is a VNC viewer widget for GTK+. It is built using coroutines
allowing it to be completely asynchronous while remaining single
threaded.

This package provides the GObject Introspection bindings for the
libgtk-vnc library.

%package tools
Summary:        VNC Tools based on gtk-vnc
License:        LGPL-2.1-or-later
Group:          Development/Libraries/X11

%description tools
This package contains tools based on gtk-vnc:

 - gvnccapture: a tool to capture a screenshot of the VNC desktop

 - gvncviewer: a simple VNC client

%package devel
Summary:        A GTK widget for VNC clients -- Development Files
License:        LGPL-2.1-or-later
Group:          Development/Libraries/X11
Requires:       libgtk-vnc%{_sover} = %{version}
Requires:       libgvnc-1_0-0 = %{version}
Requires:       libgvncpulse-1_0-0 = %{version}
Requires:       typelib-1_0-GVnc-1_0 = %{version}
Requires:       typelib-1_0-GVncPulse-1_0 = %{version}
Requires:       typelib-1_0-GtkVnc-%{_sonamepkg} = %{version}

%description devel
gtk-vnc is a VNC viewer widget for GTK+. It is built using coroutines
allowing it to be completely asynchronous while remaining single
threaded.

%lang_package

%prep
%autosetup
# install gvncviewer
sed -i '/install:/s/false/true/' examples/meson.build

%build
%meson \
	-D gi-docs=disabled \
	%{nil}
%meson_build

%install
%meson_install
%find_lang %{name}

%check
%meson_test

%post    -n libgvnc-1_0-0 -p /sbin/ldconfig
%postun  -n libgvnc-1_0-0 -p /sbin/ldconfig

%post    -n libgvncpulse-1_0-0 -p /sbin/ldconfig
%postun  -n libgvncpulse-1_0-0 -p /sbin/ldconfig

%post    -n libgtk-vnc%{_sover} -p /sbin/ldconfig
%postun  -n libgtk-vnc%{_sover} -p /sbin/ldconfig

%files -n libgvnc-1_0-0
%license COPYING.LIB
%{_libdir}/libgvnc-1.0.so.0*

%files -n typelib-1_0-GVnc-1_0
%{_libdir}/girepository-1.0/GVnc-1.0.typelib

%files -n libgvncpulse-1_0-0
%license COPYING.LIB
%{_libdir}/libgvncpulse-1.0.so.0*

%files -n typelib-1_0-GVncPulse-1_0
%{_libdir}/girepository-1.0/GVncPulse-1.0.typelib

%files -n libgtk-vnc%{_sover}
%license COPYING.LIB
%doc NEWS README
%{_libdir}/libgtk-vnc-%{_sonamever}.so.0*

%files -n typelib-1_0-GtkVnc-%{_sonamepkg}
%{_libdir}/girepository-1.0/GtkVnc-%{_sonamever}.typelib

%files tools
%{_bindir}/gvnccapture
%{_bindir}/gvncviewer
%{_mandir}/man1/gvnccapture.1%{?ext_man}

%files devel
%doc AUTHORS ChangeLog
%{_includedir}/gvnc-1.0/
%{_includedir}/gvncpulse-1.0/
%{_libdir}/libgvnc-1.0.so
%{_libdir}/libgvncpulse-1.0.so
%{_libdir}/pkgconfig/gvnc-1.0.pc
%{_libdir}/pkgconfig/gvncpulse-1.0.pc
%{_datadir}/gir-1.0/GVnc-1.0.gir
%{_datadir}/gir-1.0/GVncPulse-1.0.gir
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/gtk-vnc-%{_sonamever}.deps
%{_datadir}/vala/vapi/gtk-vnc-%{_sonamever}.vapi
%{_datadir}/vala/vapi/gvnc-1.0.deps
%{_datadir}/vala/vapi/gvnc-1.0.vapi
%{_datadir}/vala/vapi/gvncpulse-1.0.deps
%{_datadir}/vala/vapi/gvncpulse-1.0.vapi
%{_includedir}/gtk-vnc-%{_sonamever}/
%{_libdir}/libgtk-vnc-%{_sonamever}.so
%{_libdir}/pkgconfig/gtk-vnc-%{_sonamever}.pc
%{_datadir}/gir-1.0/GtkVnc-%{_sonamever}.gir

%files lang -f %{name}.lang

%changelog
