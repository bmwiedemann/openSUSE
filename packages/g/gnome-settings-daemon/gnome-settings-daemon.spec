#
# spec file for package gnome-settings-daemon
#
# Copyright (c) 2025 SUSE LLC and contributors
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


# Allow to disable wayland components
%bcond_without wayland
# Smart-Card support was not available from version 3.7.3 to 3.9.5; allow to easily disable it
%bcond_without smartcard
# Wacom input support is not available on all platforms
%ifarch s390 s390x
%bcond_with wacom
%else
%bcond_without wacom
%endif

%define base_ver 49

Name:           gnome-settings-daemon
Version:        49.1
Release:        0
Summary:        Settings daemon for the GNOME desktop
License:        GPL-2.0-or-later AND LGPL-2.1-only
Group:          System/GUI/GNOME
URL:            https://gitlab.gnome.org/GNOME/gnome-settings-daemon
Source0:        %{name}-%{version}.tar.zst

# PATCH-FIX-OPENSUSE gnome-settings-daemon-initial-keyboard.patch bsc#979051 boo#1009515 federico@suse.com -- Deal with the default keyboard being set from xkb instead of GNOME
Patch0:         gnome-settings-daemon-initial-keyboard.patch
# PATCH-FIX-OPENSUSE gnome-settings-daemon-switch-Japanese-default-input-to-mozc.patch bnc#1029083 boo#1056289 qzhao@suse.com -- Switch new user's default input engine from "anthy" to "mozc" in gnome-desktop with Japanese language and ibus input frame-work condition.
Patch1:         gnome-settings-daemon-switch-Japanese-default-input-to-mozc.patch
# PATCH-FIX-UPSTREAM 0001-usb-protection-Treat-hubs-and-HID-devices-like-any-o.patch glgo#GNOME/gnome-settings-daemon#780, bsc#1226423, CVE-2024-38394 sckang@suse.com -- usb-protection: Treat hubs and HID devices like any other USB gadget
Patch4:         0001-usb-protection-Treat-hubs-and-HID-devices-like-any-o.patch
# PATCH-FEATURE-OPENSUSE -- Sorry GNOME, but pestering users like this is not welcome. We will add a Support GNOME into our welcome app thogh
Patch5:         g-s-d-skip-donation.patch

## SLE/LEAP-only patches start at 1000
# PATCH-FEATURE-OPENSUSE gnome-settings-daemon-notify-idle-resumed.patch bnc#439018 bnc#708182 bgo#575467 hpj@suse.com -- notify user about auto suspend when returning from sleep
Patch1000:      gnome-settings-daemon-notify-idle-resumed.patch
# PATCH-FIX-OPENSUSE gnome-settings-daemon-more-power-button-actions.patch bsc#996342 fezhang@suse.com -- Bring back the "shutdown" and "interactive" power button actions.
Patch1001:      gnome-settings-daemon-more-power-button-actions.patch

BuildRequires:  cups-devel
BuildRequires:  fdupes
BuildRequires:  gtk-doc
BuildRequires:  meson >= 0.49.0
BuildRequires:  pkgconfig
# For directory ownership; it's fine to BuildRequire it since it's also a Requires
BuildRequires:  polkit
BuildRequires:  xsltproc
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(colord) >= 1.3.5
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(gcr-4) >= 3.7.5
BuildRequires:  pkgconfig(geoclue-2.0) >= 2.1.2
BuildRequires:  pkgconfig(geocode-glib-2.0) >= 3.10.0
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.70
BuildRequires:  pkgconfig(gnome-desktop-4) >= 3.11.1
BuildRequires:  pkgconfig(gsettings-desktop-schemas) >= 46.beta
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(gweather4)
BuildRequires:  pkgconfig(kbproto)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  pkgconfig(libgeoclue-2.0) >= 2.3.1
BuildRequires:  pkgconfig(libnm) >= 1.0
BuildRequires:  pkgconfig(libnotify) >= 0.7.3
BuildRequires:  pkgconfig(libpulse) >= 2.0
BuildRequires:  pkgconfig(libpulse-mainloop-glib) >= 2.0
BuildRequires:  pkgconfig(librsvg-2.0) >= 2.36.2
BuildRequires:  pkgconfig(mm-glib) >= 1.0
BuildRequires:  pkgconfig(polkit-gobject-1) >= 0.114
BuildRequires:  pkgconfig(systemd) >= 243
BuildRequires:  pkgconfig(udev)
BuildRequires:  pkgconfig(upower-glib) >= 0.99.12
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xfixes) >= 6.0
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xkbfile)
# Needed for tests
BuildRequires:  python3-gobject-devel
BuildRequires:  python3-python-dbusmock
#
Requires:       gsettings-desktop-schemas
# g-s-d uses the pkexec binary
Requires:       /usr/bin/pkexec
# For housekeeping plugin, that uses the nautilus dbus service
Recommends:     nautilus
%if %{with smartcard}
BuildRequires:  pkgconfig(gck-2)
%endif
%if %{with wacom}
BuildRequires:  pkgconfig(libwacom) >= 0.7
%endif
%if %{with wayland}
BuildRequires:  pkgconfig(wayland-client)
%endif
Recommends:     iio-sensor-proxy
# g-s-d only support configurtion of libinput based pointer drivers now.
Recommends:     (xf86-input-libinput if xorg-x11-server)

%description
gnome-settings-daemon provides a daemon run by all GNOME sessions to
provide live access to configuration settings and the changes done to
them as well as basic services like a clipboard manager, controlling
the startup of the screensaver, etc.

This module was previously part of GNOME Control Center, but has been
split for a more general use.

%package devel
Summary:        Development package for the GNOME settings daemon
Group:          Development/Languages/C and C++
Requires:       %{name} = %{version}

%description devel
gnome-settings-daemon provides a daemon run by all GNOME sessions to
provide live access to configuration settings and the changes done to
them as well as basic services like a clipboard manager, controlling
the startup of the screensaver, etc.

This package includes header files used for client applications to
contact the settings daemon via its DBus interface.

%lang_package

%prep
%autosetup -N

%if 0%{?is_opensuse}
%autopatch -p1 -M 999
%else
%autopatch -p1
%endif

%build
%meson \
	-Dalsa=true \
	%{!?with_wayland: -D wayland=false} \
	%{!?with_smartcard: -D smartcard=false} \
	%{nil}
%meson_build

%install
%meson_install

%find_lang %{name} %{?no_lang_C}
%fdupes %{buildroot}/%{_prefix}

%check
%meson_test

%files
%license COPYING COPYING.LIB
%doc NEWS
%{_datadir}/gnome-settings-daemon/
%{_libexecdir}/gsd-printer
%dir %{_libdir}/gnome-settings-daemon-%{base_ver}/
%{_libdir}/gnome-settings-daemon-%{base_ver}/libgsd.so
# Explicitly list all the plugins so we know we don't lose any

%{_libexecdir}/gsd-a11y-settings
%{_userunitdir}/org.gnome.SettingsDaemon.A11ySettings.service
%{_userunitdir}/org.gnome.SettingsDaemon.A11ySettings.target
%{_libexecdir}/gsd-color
%{_userunitdir}/org.gnome.SettingsDaemon.Color.service
%{_userunitdir}/org.gnome.SettingsDaemon.Color.target
%{_libexecdir}/gsd-datetime
%{_userunitdir}/org.gnome.SettingsDaemon.Datetime.service
%{_userunitdir}/org.gnome.SettingsDaemon.Datetime.target
%{_libexecdir}/gsd-housekeeping
%{_userunitdir}/org.gnome.SettingsDaemon.Housekeeping.service
%{_userunitdir}/org.gnome.SettingsDaemon.Housekeeping.target
%{_libexecdir}/gsd-keyboard
%{_userunitdir}/org.gnome.SettingsDaemon.Keyboard.service
%{_userunitdir}/org.gnome.SettingsDaemon.Keyboard.target
%{_libexecdir}/gsd-media-keys
%{_userunitdir}/org.gnome.SettingsDaemon.MediaKeys.service
%{_userunitdir}/org.gnome.SettingsDaemon.MediaKeys.target
%{_libexecdir}/gsd-power
%{_userunitdir}/org.gnome.SettingsDaemon.Power.service
%{_userunitdir}/org.gnome.SettingsDaemon.Power.target
%{_libexecdir}/gsd-print-notifications
%{_userunitdir}/org.gnome.SettingsDaemon.PrintNotifications.service
%{_userunitdir}/org.gnome.SettingsDaemon.PrintNotifications.target
%{_libexecdir}/gsd-rfkill
%{_userunitdir}/org.gnome.SettingsDaemon.Rfkill.service
%{_userunitdir}/org.gnome.SettingsDaemon.Rfkill.target
%{_libexecdir}/gsd-screensaver-proxy
%{_userunitdir}/org.gnome.SettingsDaemon.ScreensaverProxy.service
%{_userunitdir}/org.gnome.SettingsDaemon.ScreensaverProxy.target
%{_libexecdir}/gsd-sharing
%{_userunitdir}/org.gnome.SettingsDaemon.Sharing.service
%{_userunitdir}/org.gnome.SettingsDaemon.Sharing.target
%if %{with smartcard}
%{_libexecdir}/gsd-smartcard
%{_userunitdir}/org.gnome.SettingsDaemon.Smartcard.service
%{_userunitdir}/org.gnome.SettingsDaemon.Smartcard.target
%endif
%{_libexecdir}/gsd-sound
%{_userunitdir}/org.gnome.SettingsDaemon.Sound.service
%{_userunitdir}/org.gnome.SettingsDaemon.Sound.target
%{_libexecdir}/gsd-wwan
%{_userunitdir}/org.gnome.SettingsDaemon.Wwan.service
%{_userunitdir}/org.gnome.SettingsDaemon.Wwan.target
%{_libexecdir}/gsd-xsettings
%{_userunitdir}/org.gnome.SettingsDaemon.XSettings.service
%{_userunitdir}/org.gnome.SettingsDaemon.XSettings.target
%{_datadir}/glib-2.0/schemas/org.gnome.settings-daemon.enums.xml
%{_datadir}/glib-2.0/schemas/org.gnome.settings-daemon.global-shortcuts.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.settings-daemon.peripherals.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.settings-daemon.peripherals.wacom.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.settings-daemon.plugins.color.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.settings-daemon.plugins.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.settings-daemon.plugins.housekeeping.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.settings-daemon.plugins.media-keys.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.settings-daemon.plugins.power.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.settings-daemon.plugins.sharing.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.settings-daemon.plugins.wwan.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.settings-daemon.plugins.xsettings.gschema.xml
# Own the directory since we can't depend on gconf providing them
%dir %{_datadir}/GConf
%dir %{_datadir}/GConf/gsettings
%{_datadir}/GConf/gsettings/gnome-settings-daemon.convert
%if %{with wayland}
%dir %{_sysconfdir}/xdg/Xwayland-session.d
%{_sysconfdir}/xdg/Xwayland-session.d/00-xrdb
%endif
%{_udevrulesdir}/61-gnome-settings-daemon-rfkill.rules
%dir %{_userunitdir}/gnome-session-x11-services.target.wants/
%{_userunitdir}/gnome-session-x11-services.target.wants/org.gnome.SettingsDaemon.XSettings.service
%dir %{_userunitdir}/gnome-session-x11-services-ready.target.wants/
%{_userunitdir}/gnome-session-x11-services-ready.target.wants/org.gnome.SettingsDaemon.XSettings.service
%{_userunitdir}/org.gnome.SettingsDaemon.UsbProtection.service
%{_userunitdir}/org.gnome.SettingsDaemon.UsbProtection.target
%{_libexecdir}/gsd-usb-protection

%files devel
%doc AUTHORS ChangeLog
%{_includedir}/gnome-settings-daemon-%{base_ver}/
%{_libdir}/pkgconfig/gnome-settings-daemon.pc

%files lang -f %{name}.lang

%changelog
