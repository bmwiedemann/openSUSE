#
# spec file for package gnome-settings-daemon
#
# Copyright (c) 2021 SUSE LLC
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

Name:           gnome-settings-daemon
Version:        40.0.1
Release:        0
Summary:        Settings daemon for the GNOME desktop
License:        GPL-2.0-or-later AND LGPL-2.1-only
Group:          System/GUI/GNOME
URL:            https://gitlab.gnome.org/GNOME/gnome-settings-daemon
Source0:        https://download.gnome.org/sources/gnome-settings-daemon/40/%{name}-%{version}.tar.xz

# PATCH-FIX-OPENSUSE gnome-settings-daemon-initial-keyboard.patch bsc#979051 boo#1009515 federico@suse.com -- Deal with the default keyboard being set from xkb instead of GNOME
Patch1:         gnome-settings-daemon-initial-keyboard.patch
# PATCH-FIX-OPENSUSE gnome-settings-daemon-switch-Japanese-default-input-to-mozc.patch bnc#1029083 boo#1056289 qzhao@suse.com -- Switch new user's default input engine from "anthy" to "mozc" in gnome-desktop with Japanese language and ibus input frame-work condition.
Patch2:         gnome-settings-daemon-switch-Japanese-default-input-to-mozc.patch
# PATCH-FIX-UPSTREAM gnome-settings-daemon-bgo793253.patch bgo#793253 dimstar@opensuse.org -- Fix no-return-in-nonvoid-function
Patch3:         gnome-settings-daemon-bgo793253.patch
# PATCH-FEATURE-OPENSUSE gnome-settings-daemon-notify-idle-resumed.patch bnc#439018 bnc#708182 bgo#575467 hpj@suse.com -- notify user about auto suspend when returning from sleep
Patch4:         gnome-settings-daemon-notify-idle-resumed.patch
# PATCH-FIX-OPENSUSE gnome-settings-daemon-bnc873545-hide-warnings.patch bnc#873545 fezhang@suse.com -- hide the warnings when g-s-d cannot find colord running, which is expected on SLES
Patch5:         gnome-settings-daemon-bnc873545-hide-warnings.patch
# PATCH-FIX-OPENSUSE gnome-settings-daemon-more-power-button-actions.patch bsc#996342 fezhang@suse.com -- Bring back the "shutdown" and "interactive" power button actions.
Patch7:         gnome-settings-daemon-more-power-button-actions.patch

## SLE-only patches start at 1000

BuildRequires:  cups-devel
BuildRequires:  fdupes
BuildRequires:  gnome-patch-translation
BuildRequires:  gtk-doc
BuildRequires:  meson >= 0.47.0
BuildRequires:  pkgconfig
# For directory ownership; it's fine to BuildRequire it since it's also a Requires
BuildRequires:  polkit
BuildRequires:  translation-update-upstream
BuildRequires:  xsltproc
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(colord) >= 1.3.5
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(gcr-3) >= 3.7.5
BuildRequires:  pkgconfig(geoclue-2.0) >= 2.1.2
BuildRequires:  pkgconfig(geocode-glib-1.0) >= 3.10.0
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.56
BuildRequires:  pkgconfig(gnome-desktop-3.0) >= 3.11.1
BuildRequires:  pkgconfig(gsettings-desktop-schemas) >= 3.35.91
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.15.3
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(gweather-3.0) >= 3.9.5
BuildRequires:  pkgconfig(kbproto)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libcanberra-gtk3)
BuildRequires:  pkgconfig(libgeoclue-2.0) >= 2.3.1
BuildRequires:  pkgconfig(libnm) >= 1.0
BuildRequires:  pkgconfig(libnotify) >= 0.7.3
BuildRequires:  pkgconfig(libpulse) >= 2.0
BuildRequires:  pkgconfig(libpulse-mainloop-glib) >= 2.0
BuildRequires:  pkgconfig(librsvg-2.0) >= 2.36.2
BuildRequires:  pkgconfig(mm-glib) >= 1.0
BuildRequires:  pkgconfig(nss)
BuildRequires:  pkgconfig(pango) >= 1.20.0
BuildRequires:  pkgconfig(polkit-gobject-1) >= 0.114
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(udev)
BuildRequires:  pkgconfig(upower-glib) >= 0.99.8
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xkbfile)
# Needed for tests
BuildRequires:  python3-gobject-devel
BuildRequires:  python3-python-dbusmock
#
Requires:       gsettings-desktop-schemas
# g-s-d uses the pkexec binary
Requires:       polkit
# For housekeeping plugin, that uses the nautilus dbus service
Recommends:     nautilus
%if %{with wacom}
BuildRequires:  pkgconfig(libwacom) >= 0.7
%endif
%if %{with wayland}
BuildRequires:  pkgconfig(wayland-client)
%endif
Recommends:     iio-sensor-proxy
# g-s-d only support configurtion of libinput based pointer drivers now.
Recommends:     xf86-input-libinput

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
translation-update-upstream po %{name}
gnome-patch-translation-prepare po %{name}
%patch1 -p1
%patch2 -p1
%patch3 -p1
# Enable the patches for both Leap 15 and SLE 15, please find the clarification at bsc#1158476.
%if 0%{?sle_version} >= 150000
%patch4 -p1
%patch5 -p1
%patch7 -p1
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

%if %{without wacom}
rm %{buildroot}%{_sysconfdir}/xdg/autostart/org.gnome.SettingsDaemon.Wacom.desktop
%endif

%find_lang %{name} %{?no_lang_C}
%fdupes %{buildroot}/%{_prefix}

%check
%meson_test

%files
%license COPYING COPYING.LIB
%doc NEWS
%{_datadir}/gnome-settings-daemon/
%{_libexecdir}/gsd-backlight-helper
%{_libexecdir}/gsd-printer
%dir %{_libdir}/gnome-settings-daemon-40/
%{_libdir}/gnome-settings-daemon-40/libgsd.so
# Explicitly list all the plugins so we know we don't lose any

%{_libexecdir}/gsd-a11y-settings
%{_sysconfdir}/xdg/autostart/org.gnome.SettingsDaemon.A11ySettings.desktop
%{_userunitdir}/org.gnome.SettingsDaemon.A11ySettings.service
%{_userunitdir}/org.gnome.SettingsDaemon.A11ySettings.target
%{_libexecdir}/gsd-color
%{_sysconfdir}/xdg/autostart/org.gnome.SettingsDaemon.Color.desktop
%{_userunitdir}/org.gnome.SettingsDaemon.Color.service
%{_userunitdir}/org.gnome.SettingsDaemon.Color.target
%{_libexecdir}/gsd-datetime
%{_sysconfdir}/xdg/autostart/org.gnome.SettingsDaemon.Datetime.desktop
%{_userunitdir}/org.gnome.SettingsDaemon.Datetime.service
%{_userunitdir}/org.gnome.SettingsDaemon.Datetime.target
%{_libexecdir}/gsd-housekeeping
%{_sysconfdir}/xdg/autostart/org.gnome.SettingsDaemon.Housekeeping.desktop
%{_userunitdir}/org.gnome.SettingsDaemon.Housekeeping.service
%{_userunitdir}/org.gnome.SettingsDaemon.Housekeeping.target
%{_libexecdir}/gsd-keyboard
%{_sysconfdir}/xdg/autostart/org.gnome.SettingsDaemon.Keyboard.desktop
%{_userunitdir}/org.gnome.SettingsDaemon.Keyboard.service
%{_userunitdir}/org.gnome.SettingsDaemon.Keyboard.target
%{_libexecdir}/gsd-media-keys
%{_sysconfdir}/xdg/autostart/org.gnome.SettingsDaemon.MediaKeys.desktop
%{_userunitdir}/org.gnome.SettingsDaemon.MediaKeys.service
%{_userunitdir}/org.gnome.SettingsDaemon.MediaKeys.target
%{_libexecdir}/gsd-power
%{_sysconfdir}/xdg/autostart/org.gnome.SettingsDaemon.Power.desktop
%{_userunitdir}/org.gnome.SettingsDaemon.Power.service
%{_userunitdir}/org.gnome.SettingsDaemon.Power.target
%{_libexecdir}/gsd-print-notifications
%{_sysconfdir}/xdg/autostart/org.gnome.SettingsDaemon.PrintNotifications.desktop
%{_userunitdir}/org.gnome.SettingsDaemon.PrintNotifications.service
%{_userunitdir}/org.gnome.SettingsDaemon.PrintNotifications.target
%{_libexecdir}/gsd-rfkill
%{_sysconfdir}/xdg/autostart/org.gnome.SettingsDaemon.Rfkill.desktop
%{_userunitdir}/org.gnome.SettingsDaemon.Rfkill.service
%{_userunitdir}/org.gnome.SettingsDaemon.Rfkill.target
%{_libexecdir}/gsd-screensaver-proxy
%{_sysconfdir}/xdg/autostart/org.gnome.SettingsDaemon.ScreensaverProxy.desktop
%{_userunitdir}/org.gnome.SettingsDaemon.ScreensaverProxy.service
%{_userunitdir}/org.gnome.SettingsDaemon.ScreensaverProxy.target
%{_libexecdir}/gsd-sharing
%{_sysconfdir}/xdg/autostart/org.gnome.SettingsDaemon.Sharing.desktop
%{_userunitdir}/org.gnome.SettingsDaemon.Sharing.service
%{_userunitdir}/org.gnome.SettingsDaemon.Sharing.target
%if %{with smartcard}
%{_libexecdir}/gsd-smartcard
%{_sysconfdir}/xdg/autostart/org.gnome.SettingsDaemon.Smartcard.desktop
%{_userunitdir}/org.gnome.SettingsDaemon.Smartcard.service
%{_userunitdir}/org.gnome.SettingsDaemon.Smartcard.target
%endif
%{_libexecdir}/gsd-sound
%{_sysconfdir}/xdg/autostart/org.gnome.SettingsDaemon.Sound.desktop
%{_userunitdir}/org.gnome.SettingsDaemon.Sound.service
%{_userunitdir}/org.gnome.SettingsDaemon.Sound.target
%{_libexecdir}/gsd-wwan
%{_sysconfdir}/xdg/autostart/org.gnome.SettingsDaemon.Wwan.desktop
%{_userunitdir}/org.gnome.SettingsDaemon.Wwan.service
%{_userunitdir}/org.gnome.SettingsDaemon.Wwan.target
%{_libexecdir}/gsd-xsettings
%{_sysconfdir}/xdg/autostart/org.gnome.SettingsDaemon.XSettings.desktop
%{_userunitdir}/org.gnome.SettingsDaemon.XSettings.service
%{_userunitdir}/org.gnome.SettingsDaemon.XSettings.target
%{_datadir}/glib-2.0/schemas/org.gnome.settings-daemon.enums.xml
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
%{_datadir}/polkit-1/actions/org.gnome.settings-daemon.plugins.power.policy
# Own the directory since we can't depend on gconf providing them
%dir %{_datadir}/GConf
%dir %{_datadir}/GConf/gsettings
%{_datadir}/GConf/gsettings/gnome-settings-daemon.convert
%if %{with wacom}
%{_datadir}/polkit-1/actions/org.gnome.settings-daemon.plugins.wacom.policy
%{_libexecdir}/gsd-wacom-oled-helper
%{_libexecdir}/gsd-wacom
%{_sysconfdir}/xdg/autostart/org.gnome.SettingsDaemon.Wacom.desktop
%{_userunitdir}/org.gnome.SettingsDaemon.Wacom.service
%{_userunitdir}/org.gnome.SettingsDaemon.Wacom.target
%endif
%if %{with wayland}
%dir %{_sysconfdir}/xdg/Xwayland-session.d
%{_sysconfdir}/xdg/Xwayland-session.d/00-xrdb
%endif
%{_udevrulesdir}/61-gnome-settings-daemon-rfkill.rules
%dir %{_userunitdir}/gnome-session-x11-services.target.wants/
%{_userunitdir}/gnome-session-x11-services.target.wants/org.gnome.SettingsDaemon.XSettings.service
%dir %{_userunitdir}/gnome-session-x11-services-ready.target.wants/
%{_userunitdir}/gnome-session-x11-services-ready.target.wants/org.gnome.SettingsDaemon.XSettings.service
%{_sysconfdir}/xdg/autostart/org.gnome.SettingsDaemon.UsbProtection.desktop
%{_userunitdir}/org.gnome.SettingsDaemon.UsbProtection.service
%{_userunitdir}/org.gnome.SettingsDaemon.UsbProtection.target
%{_libexecdir}/gsd-usb-protection

%files devel
%doc AUTHORS ChangeLog
%{_includedir}/gnome-settings-daemon-40/
%{_libdir}/pkgconfig/gnome-settings-daemon.pc

%files lang -f %{name}.lang

%changelog
