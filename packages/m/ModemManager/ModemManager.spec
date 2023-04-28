#
# spec file for package ModemManager
#
# Copyright (c) 2023 SUSE LLC
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


%define glib_version 2.56.0

%define _udevdir %(pkg-config --variable udevdir udev)
Name:           ModemManager
Version:        1.20.6
Release:        0
Summary:        DBus interface for modem handling
License:        GPL-2.0-or-later AND GPL-3.0-or-later
Group:          Productivity/Networking/System
URL:            http://cgit.freedesktop.org/ModemManager/ModemManager
Source0:        https://gitlab.com/linux-mobile-broadband/ModemManager/-/archive/%{version}/%{name}-%{version}.tar.bz2

BuildRequires:  dbus-1-glib-devel
BuildRequires:  gobject-introspection-devel >= 0.9.6
BuildRequires:  hicolor-icon-theme
BuildRequires:  libgudev-1_0-devel
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  ppp-devel
BuildRequires:  python3-dbus-python
BuildRequires:  python3-gobject-Gdk
BuildRequires:  vala-devel >= 0.18
BuildRequires:  xsltproc
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  pkgconfig(gio-2.0) >= %{glib_version}
BuildRequires:  pkgconfig(glib-2.0) >= %{glib_version}
BuildRequires:  pkgconfig(gmodule-2.0) >= %{glib_version}
BuildRequires:  pkgconfig(gobject-2.0) >= %{glib_version}
BuildRequires:  pkgconfig(gudev-1.0) >= 147
BuildRequires:  pkgconfig(libsystemd) >= 209
BuildRequires:  pkgconfig(mbim-glib) >= 1.28.0
BuildRequires:  pkgconfig(polkit-gobject-1) >= 0.97
BuildRequires:  pkgconfig(qmi-glib) >= 1.32.0
BuildRequires:  pkgconfig(qrtr-glib)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(udev)
Requires:       hicolor-icon-theme
Recommends:     libmbim
Recommends:     usb_modeswitch
Provides:       org.freedesktop.ModemManager
%{?systemd_ordering}

%description
DBus interface for modem handling. Provides a standard abstracted API
(over DBus) to communicate with all sorts of modems (landline, GSM,
CDMA).

%package -n libmm-glib0
Summary:        Glib bindings for the modem handling DBus interface
Group:          System/Libraries

%description -n libmm-glib0
DBus interface for modem handling. Provides a standard abstracted API
(over DBus) to communicate with all sorts of modems (landline, GSM,
CDMA).

%package -n typelib-1_0-ModemManager-1_0
Summary:        Introspection bindings for the modem handling DBus interface
Group:          System/Libraries

%description -n typelib-1_0-ModemManager-1_0
DBus interface for modem handling. Provides a standard abstracted API
(over DBus) to communicate with all sorts of modems (landline, GSM,
CDMA).

%package devel
Summary:        Development files for the modem handling DBus interface
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       libmm-glib0 = %{version}
Requires:       typelib-1_0-ModemManager-1_0 = %{version}

%description devel
DBus interface for modem handling. Provides a standard abstracted API
(over DBus) to communicate with all sorts of modems (landline, GSM,
CDMA).

%package bash-completion
Summary:        Bash completion for mmcli
Group:          Productivity/Networking/System
Requires:       bash-completion
Supplements:    (%{name} and bash-completion)
BuildArch:      noarch

%description bash-completion
This package contain the bash completion command for nmcli tools.

%lang_package

%prep
%autosetup -p1

%build
pppddir=`ls -1d %{_libdir}/pppd/2*`
test -n "$pppddir" || exit 1
%meson \
	-Dudevdir='%{_udevdir}' \
	-Ddbus_policy_dir='%{_datadir}/dbus-1/system.d' \
	-Dsystemdsystemunitdir='%{_unitdir}' \
	-Dvapi=true \
	-Dpolkit=permissive \
	%{nil}
%meson_build

%install
%meson_install
# create suse-specific rcFOO link
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rcModemManager
%find_lang ModemManager %{name}.lang

%check
%meson_test

%pre
%service_add_pre ModemManager.service

%post
%{?udev_rules_update:%udev_rules_update}
%service_add_post ModemManager.service

%preun
%service_del_preun ModemManager.service

%postun
%service_del_postun ModemManager.service

%ldconfig_scriptlets -n libmm-glib0

%files
%license COPYING
%doc AUTHORS README
%{_bindir}/mmcli
%{_sbindir}/ModemManager
%{_sbindir}/rcModemManager
%{_datadir}/dbus-1/system.d/org.freedesktop.ModemManager1.conf
%{_libdir}/ModemManager/
%{_datadir}/dbus-1/interfaces/*.xml
%{_datadir}/dbus-1/system-services/org.freedesktop.ModemManager1.service
%{_datadir}/icons/hicolor/*/*/ModemManager.png
%{_datadir}/polkit-1/actions/org.freedesktop.ModemManager1.policy
%{_datadir}/ModemManager
%{_udevdir}/rules.d/*-mm-*.rules
%{_unitdir}/ModemManager.service
%{_mandir}/man1/mmcli.1%{?ext_man}
%{_mandir}/man8/ModemManager.8%{?ext_man}

%files lang -f %{name}.lang

%files -n libmm-glib0
%{_libdir}/libmm-glib.so.*

%files -n typelib-1_0-ModemManager-1_0
%{_libdir}/girepository-1.0/ModemManager-1.0.typelib

%files devel
%{_datadir}/gir-1.0/ModemManager-1.0.gir
%{_datadir}/vala/vapi/
%{_includedir}/ModemManager/
%{_includedir}/libmm-glib/
%{_libdir}/libmm-glib.so
%{_libdir}/pkgconfig/ModemManager.pc
%{_libdir}/pkgconfig/mm-glib.pc

%files bash-completion
%{_datadir}/bash-completion/

%changelog
