#
# spec file for package libqmi
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2012 Dominique Leuenberger, Amsterdam, The Netherlands.
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


%define _soname libqmi-glib5
Name:           libqmi
Version:        1.32.4
Release:        0
# NOTE: The file headers state LESSER GPL, which is a mistake. The upstream intended license is LIBRARY GPL 2.0+
Summary:        Library to control QMI devices
License:        LGPL-2.1-or-later AND GPL-2.0-or-later
Group:          Hardware/Modem
URL:            https://gitlab.freedesktop.org/mobile-broadband/libqmi
Source0:        %{url}/-/archive/%{version}/%{name}-%{version}.tar.bz2

BuildRequires:  help2man
BuildRequires:  pkgconfig
BuildRequires:  meson
BuildRequires:  python3-base
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.56
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gudev-1.0) >= 232
BuildRequires:  pkgconfig(mbim-glib) >= 1.18
BuildRequires:  pkgconfig(qrtr-glib)

%description
libqmi is a glib-based library for talking to WWAN modems and devices
which speak the Qualcomm MSM Interface (QMI) protocol.

%package -n %{_soname}
Summary:        Library to control QMI devices
Group:          System/Libraries
# The tools are a useful addition
Recommends:     %{name}-tools

%description -n %{_soname}
libqmi is a glib-based library for talking to WWAN modems and devices
which speak the Qualcomm MSM Interface (QMI) protocol.

%package tools
Summary:        Helper utilities to control QMI devices
Group:          Hardware/Modem

%description tools
libqmi is a glib-based library for talking to WWAN modems and devices
which speak the Qualcomm MSM Interface (QMI) protocol.

This package contains command line tools to manage such devices.

%package -n typelib-1_0-Qmi-1_0
Summary:        Introspection bindings for %{name}
Group:          System/Libraries

%description -n typelib-1_0-Qmi-1_0
libqmi is a glib-based library for talking to WWAN modems and devices
which speak the Qualcomm MSM Interface (QMI) protocol.

This package contains the introspection bindings for %{name}.

%package devel
Summary:        Development files for the QMI device control library
Group:          Development/Languages/C and C++
Requires:       %{_soname} = %{version}
Requires:       typelib-1_0-Qmi-1_0 = %{version}

%description devel
A GLib/GIO based library to control QMI devices

This package contains files required to link sources against libqmi.

%prep
%autosetup -p1

%build
# Do not rely on env for choosing python
sed -i "s|env python$|python3|g" build-aux/qmi-codegen/*
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%ldconfig_scriptlets -n %{_soname}

%files tools
%license COPYING
%doc NEWS
%{_bindir}/qmi-network
%{_bindir}/qmicli
%{_bindir}/qmi-firmware-update
# Own dirs to avoid depending on them while building
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/qmicli
%{_libexecdir}/qmi-proxy
%{_mandir}/man1/qmi-network.1%{?ext_man}
%{_mandir}/man1/qmicli.1%{?ext_man}
%{_mandir}/man1/qmi-firmware-update.1%{?ext_man}

%files -n %{_soname}
%license COPYING.LIB
%{_libdir}/libqmi-glib.so.*

%files -n typelib-1_0-Qmi-1_0
%{_libdir}/girepository-1.0/Qmi-1.0.typelib

%files devel
%doc AUTHORS README.md TODO
%{_includedir}/libqmi-glib/
%{_libdir}/libqmi-glib.so
%{_libdir}/pkgconfig/qmi-glib.pc
%{_datadir}/gir-1.0/Qmi-1.0.gir


%changelog
