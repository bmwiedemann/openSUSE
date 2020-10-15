#
# spec file for package libqmi
#
# Copyright (c) 2020 SUSE LLC
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
Version:        1.26.6
Release:        0
# NOTE: The file headers state LESSER GPL, which is a mistake. The upstream intended license is LIBRARY GPL 2.0+
Summary:        Library to control QMI devices
License:        LGPL-2.1-or-later AND GPL-2.0-or-later
Group:          Hardware/Modem
URL:            https://www.freedesktop.org/wiki/Software/libqmi/
Source0:        https://www.freedesktop.org/software/libqmi/%{name}-%{version}.tar.xz
Source99:       libqmi-rpmlintrc

BuildRequires:  pkgconfig
BuildRequires:  python3-base
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.36
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gudev-1.0) >= 147
BuildRequires:  pkgconfig(mbim-glib) >= 1.14

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

%package devel
Summary:        Development files for the QMI device control library
Group:          Development/Languages/C and C++
Requires:       %{_soname} = %{version}

%description devel
A GLib/GIO based library to control QMI devices

This package contains files required to link sources against libqmi.

%prep
%autosetup -p1

%build
# Do not rely on env for choosing python
sed -i "s|env python|python3|g" build-aux/qmi-codegen/*
%configure \
  --disable-static
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%check
make %{?_smp_mflags} check

%post -n %{_soname} -p /sbin/ldconfig
%postun -n %{_soname} -p /sbin/ldconfig

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

%files devel
%doc AUTHORS README TODO
#Own these directories to not depend on gtk-doc
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html
%doc %{_datadir}/gtk-doc/html/libqmi-glib/
%{_includedir}/libqmi-glib/
%{_libdir}/libqmi-glib.so
%{_libdir}/pkgconfig/qmi-glib.pc

%changelog
