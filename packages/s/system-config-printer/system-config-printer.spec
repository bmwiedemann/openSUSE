#
# spec file for package system-config-printer
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


%define _icontheme adwaita
%define _iconlocation Adwaita
Name:           system-config-printer
Version:        1.5.18
Release:        0
Summary:        A printer administration tool
License:        GPL-2.0-or-later
Group:          Hardware/Printing
URL:            https://github.com/OpenPrinting/system-config-printer/
Source0:        https://github.com/OpenPrinting/system-config-printer/releases/download/v%{version}/system-config-printer-%{version}.tar.gz
Source1:        https://github.com/OpenPrinting/system-config-printer/releases/download/v%{version}/system-config-printer-%{version}.tar.gz.asc
Source99:       %{name}-rpmlintrc
# PATCH-FIX-OPENSUSE system-config-printer-icon-brp-friendly.patch vuntz@novell.com -- brp checks don't like the printer icon name, so we have to use something else
Patch13:        system-config-printer-icon-brp-friendly.patch
# PATCH-FIX-OPENSUSE system-config-printer-no-openprinting.patch bnc#733542 vuntz@opensuse.org -- Disable feature that downloads ppd from openprinting.org
Patch19:        system-config-printer-no-openprinting.patch
# PATCH-FEATURE-OPENSUSE system-config-printer-no-simple-gui.patch boo#1090189 dimstar@opensuse.org -- Remove unused _simple_gui class in openprinting.py. Pulls in GTK
Patch100:       system-config-printer-no-simple-gui.patch
# For directory ownership
BuildRequires:  %{_icontheme}-icon-theme
BuildRequires:  cups-devel
BuildRequires:  dbus-1
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  glib2-devel
# Needed for typelib() requires
BuildRequires:  gobject-introspection
# For directory ownership
BuildRequires:  hicolor-icon-theme
BuildRequires:  intltool
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3-lxml
BuildRequires:  update-desktop-files
BuildRequires:  xmlto
BuildRequires:  pkgconfig(libudev) >= 172
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(udev)
Requires:       %{name}-common = %{version}
Requires:       python3-cups
Requires:       python3-pycurl
# The applet is not strictly necessary, but it really makes sense
Recommends:     %{name}-applet
Obsoletes:      gnome-cups-manager <= 0.33

%description
system-config-printer is a graphical user interface that allows the
user to configure a CUPS print server.

%package common
Summary:        Common files for GNOME's printer administration tool
Group:          Hardware/Printing
Requires:       dbus-1-python3
Requires:       python3-cairo
Requires:       python3-cups >= 1.9.60
Requires:       python3-cupshelpers
Requires:       python3-gobject
Requires:       python3-gobject-Gdk
Requires:       python3-smbc
Recommends:     cups-pk-helper
# As soon as this package is installed, it makes sense to have the
# autoconfiguration too
Recommends:     udev-configure-printer
BuildArch:      noarch

%description common
system-config-printer is a graphical user interface that allows the
user to configure a CUPS print server.

This package provides files common to various binaries.

%package applet
Summary:        Notification icon for printing via system-config-printer
Group:          Hardware/Printing
Requires:       %{name} = %{version}
# Uses the dbus service to interact with print jobs
Requires:       %{name}-dbus-service = %{version}
Provides:       dbus(com.redhat.NewPrinterNotification)
BuildArch:      noarch

%description applet
system-config-printer is a graphical user interface that allows the
user to configure a CUPS print server.

This package provides a notification icon to configure new printers and
monitor print jobs.

%package dbus-service
Summary:        D-Bus service to configure printing via system-config-printer
Group:          Hardware/Printing
Requires:       %{name}-common = %{version}
BuildArch:      noarch

%description dbus-service
system-config-printer is a graphical user interface that allows the
user to configure a CUPS print server.

This packages provides a D-Bus service to configure printers and manage
print jobs.

%package -n python3-cupshelpers
Summary:        High-level Python Bindings for CUPS
Group:          Hardware/Printing
Requires:       python3-cups >= 1.9.60
Requires:       python3-pycurl
Requires:       python3-requests
BuildArch:      noarch

%description -n python3-cupshelpers
This package provides high-level python bindings for CUPS, and can be
used on top of python3-cups.

%package -n udev-configure-printer
Summary:        Utility to autoconfigure printers when plugged
Group:          Hardware/Printing
Requires:       dbus-1-python3
Requires:       python3-cups >= 1.9.60
Requires:       python3-cupshelpers
# do not make this recommended! it would pull in KDE or GNOME
# applets, even if udev-configure-printer is used on servers
Suggests:       dbus(com.redhat.NewPrinterNotification)
Obsoletes:      cups-autoconfig <= 0.1.0
%systemd_requires

%description -n udev-configure-printer
This package contains an utility that will ensure printers get
automatically configured when plugged on the computer.

%lang_package -n system-config-printer-common

%prep
%setup -q
%patch13 -p1
%patch19 -p1
%patch100 -p1

%build
%configure \
        --with-udev-rules \
        --with-systemdsystemunitdir=%{_unitdir}

%install
%make_install dbusdir=%{_datadir}/dbus-1/system.d/
for size in 16x16 22x22 24x24 32x32 48x48 512x512; do
	if test -f %{_datadir}/icons/%{_iconlocation}/$size/devices/printer.png; then
		mkdir -p %{buildroot}/%{_datadir}/icons/hicolor/$size/apps
		cp -a %{_datadir}/icons/%{_iconlocation}/$size/devices/printer.png %{buildroot}/%{_datadir}/icons/hicolor/$size/apps/%{name}.png
	fi
done
%suse_update_desktop_file print-applet
%suse_update_desktop_file -r system-config-printer GTK System HardwareSettings
%fdupes %{buildroot}/%{py_sitedir}
%find_lang %{name} %{?no_lang_C}

%files
%license COPYING
%doc ChangeLog README
%{_bindir}/%{name}
%{_bindir}/install-printerdriver
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/system-config-printer.appdata.xml
%{_datadir}/applications/system-config-printer.desktop
%{_mandir}/man1/system-config-printer.1%{?ext_man}

%files common
%{_datadir}/%{name}/
%{_datadir}/icons/hicolor/*/apps/system-config-printer.png

%files applet
%{_bindir}/%{name}-applet
%{_mandir}/man1/system-config-printer-applet.1%{?ext_man}
# The dbus service is provided by applet.py
%{_datadir}/dbus-1/system.d/com.redhat.NewPrinterNotification.conf
%{_sysconfdir}/xdg/autostart/print-applet.desktop

%files dbus-service
%{_bindir}/scp-dbus-service
%{_datadir}/dbus-1/interfaces/org.fedoraproject.Config.Printing.xml
%{_datadir}/dbus-1/services/org.fedoraproject.Config.Printing.service

%files -n python3-cupshelpers
%dir %{_sysconfdir}/cupshelpers
%config(noreplace) %{_sysconfdir}/cupshelpers/preferreddrivers.xml
%exclude %{python3_sitelib}/cupshelpers/__pycache__/*.pyc
%{python3_sitelib}/cupshelpers
%{python3_sitelib}/cupshelpers*.egg-info
# The dbus service is provided by cupshelpers/installdriver.py
%{_datadir}/dbus-1/system.d/com.redhat.PrinterDriversInstaller.conf

%files -n udev-configure-printer
%{_unitdir}/configure-printer@.service
%dir %{_prefix}/lib/udev
%dir %{_prefix}/lib/udev/rules.d
%{_prefix}/lib/udev/rules.d/*.rules
%{_prefix}/lib/udev/udev-add-printer
%{_prefix}/lib/udev/udev-configure-printer

%files common-lang -f %{name}.lang

%changelog
