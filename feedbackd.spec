#
# spec file for package feedbackd
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


%define soname libfeedback-0_0-0

Name:           feedbackd
Version:        0.0.1
Release:        0
Summary:        Feedback library for GNOME
License:        GPL-3.0-only AND LGPL-2.1-only
URL:            https://source.puri.sm/Librem5/feedbackd
Source0:        %{name}-%{version}.tar.xz

BuildRequires:  c_compiler
BuildRequires:  dbus-1
BuildRequires:  meson
BuildRequires:  vala
BuildRequires:  pkgconfig(gio-2.0) >= 2.50.0
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.50.0
BuildRequires:  pkgconfig(glib-2.0) >= 2.50.0
BuildRequires:  pkgconfig(gobject-2.0) >= 2.50.0
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gsound)
BuildRequires:  pkgconfig(gudev-1.0) >= 232
BuildRequires:  pkgconfig(json-glib-1.0)

%description
feedbackd provides a DBus daemon (feedbackd) to act on events to provide
haptic, visual and audio feedback. It offers a library (libfeedback) and
GObject introspection bindings to ease using it from applications.

%package -n typelib-1_0-Lfb-0_0
Summary:        Introspection bindings for %{name}

%description -n typelib-1_0-Lfb-0_0
feedbackd provides a DBus daemon (feedbackd) to act on events to provide
haptic, visual and audio feedback. It offers a library (libfeedback) and
GObject introspection bindings to ease using it from applications.

This package contains the introspection bindings for %{name}.

%package -n %{soname}
Summary:        Shared library for %{name}

%description -n %{soname}
feedbackd provides a DBus daemon (feedbackd) to act on events to provide
haptic, visual and audio feedback. It offers a library (libfeedback) and
GObject introspection bindings to ease using it from applications.

This package contains the shared library for %{name}.

%package devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}
Requires:       %{soname} = %{version}
Requires:       typelib-1_0-Lfb-0_0 = %{version}

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
%{__install} -Dm0644 -T debian/feedbackd.udev %{buildroot}%{_udevrulesdir}/90-feedbackd.rules

%pre
getent group feedbackd >/dev/null || groupadd -r feedbackd
exit 0

%check
%meson_test

%ldconfig_scriptlets -n %{soname}

%files
%{_bindir}/fbcli
%{_libexecdir}/feedbackd
%{_libexecdir}/fbd-ledctrl
%{_datadir}/dbus-1/interfaces/org.sigxcpu.Feedback.xml
%{_datadir}/dbus-1/services/org.sigxcpu.Feedback.service
%{_datadir}/feedbackd
%{_datadir}/glib-2.0/schemas/org.sigxcpu.feedbackd.gschema.xml
%{_udevrulesdir}/*

%files -n typelib-1_0-Lfb-0_0
%{_libdir}/girepository-1.0/Lfb-0.0.typelib

%files -n %{soname}
%{_libdir}/libfeedback-0.0.so.0

%files devel
%{_libdir}/libfeedback-0.0.so
%{_includedir}/libfeedback-0.0/
%{_datadir}/vala/
%{_datadir}/gir-1.0/Lfb-0.0.gir
%{_libdir}/pkgconfig/libfeedback-0.0.pc

%changelog
