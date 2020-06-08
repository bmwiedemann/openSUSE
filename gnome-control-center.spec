#
# spec file for package gnome-control-center
#
# Copyright (c) 2020 SUSE LLC
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


# Allow to enable/disable ibus, as GNOME is rather strict on new versions.
%bcond_without  ibus
# Wacom input support
%ifarch s390 s390x
%bcond_with     wacom
%else
%bcond_without  wacom
%endif

Name:           gnome-control-center
Version:        3.36.3
Release:        0
Summary:        The GNOME Control Center
License:        GPL-2.0-or-later
Group:          System/GUI/GNOME
URL:            https://www.gnome.org
Source0:        https://download.gnome.org/sources/gnome-control-center/3.36/%{name}-%{version}.tar.xz

### patches for Leap >= 15 plus SLE >= 15, but not TW
# PATCH-FEATURE-SLE gnome-control-center-info-never-use-gnome-software.patch bsc#999336 fezhang@suse.com -- info: Never search for gnome-software as an option when checking for updates on SLE and Leap 42.2, because we use gpk-update-viewer.
Patch1001:      gnome-control-center-info-never-use-gnome-software.patch
# PATCH-FEATURE-SLE gnome-control-center-more-power-button-actions.patch bsc#993381 fezhang@suse.com -- power: Bring back the "shutdown" and "interactive" power button actions.
Patch1002:      gnome-control-center-more-power-button-actions.patch
# PATCH-FEATURE-SLE gnome-control-center-bring-back-firewall-zone.patch fate#316719 sckang@suse.com -- network: Bring back the firewall zone combo box to select proper firewall zone for each connection.
Patch1003:      gnome-control-center-bring-back-firewall-zone.patch

BuildRequires:  /usr/bin/Xvfb
BuildRequires:  cups-devel >= 1.4
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  intltool
BuildRequires:  krb5-devel
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  python3-dbusmock
BuildRequires:  python3-pytest-xvfb
BuildRequires:  translation-update-upstream
BuildRequires:  xsltproc
BuildRequires:  pkgconfig(accountsservice) >= 0.6.39
BuildRequires:  pkgconfig(cairo-gobject)
BuildRequires:  pkgconfig(cheese) >= 3.28.0
BuildRequires:  pkgconfig(cheese-gtk) >= 3.5.91
BuildRequires:  pkgconfig(colord) >= 0.1.34
BuildRequires:  pkgconfig(colord-gtk) >= 0.1.24
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0) >= 2.23.0
BuildRequires:  pkgconfig(gdk-wayland-3.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glib-2.0) >= 2.53.0
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gnome-bluetooth-1.0) >= 3.18.2
BuildRequires:  pkgconfig(gnome-desktop-3.0) >= 3.27.90
BuildRequires:  pkgconfig(gnome-settings-daemon) >= 3.25.90
BuildRequires:  pkgconfig(goa-1.0) >= 3.25.3
BuildRequires:  pkgconfig(goa-backend-1.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(grilo-0.3) >= 0.3.0
BuildRequires:  pkgconfig(gsettings-desktop-schemas) >= 3.31.0
BuildRequires:  pkgconfig(gsound)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22.20
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(libgtop-2.0)
BuildRequires:  pkgconfig(libhandy-0.0) >= 0.0.9
BuildRequires:  pkgconfig(libnm) >= 1.10.0
BuildRequires:  pkgconfig(libnma) >= 1.8.0
BuildRequires:  pkgconfig(libpulse) >= 2.0
BuildRequires:  pkgconfig(libpulse-mainloop-glib)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(mm-glib) >= 0.7
BuildRequires:  pkgconfig(polkit-gobject-1) >= 0.103
BuildRequires:  pkgconfig(pwquality) >= 1.2.2
BuildRequires:  pkgconfig(smbclient)
BuildRequires:  pkgconfig(udisks2)
BuildRequires:  pkgconfig(upower-glib) >= 0.99.6
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xft)
BuildRequires:  pkgconfig(xi) >= 1.2
Requires:       gnome-settings-daemon
# needed for universal access panel
Requires:       gnome-themes-accessibility
Requires:       gnome-version
Requires:       iso-codes
# Needed for showing keyboard layout, boo#898096
# Require the package providing /usr/bin/gkbd-keyboard-display
Requires:       gnomekbd-tools
# For the thunderbolt panel
Recommends:     bolt
Recommends:     %{name}-user-faces
# cups-pk-helper should only be recommended, rather than a hard Requires, see boo#904047
Recommends:     cups-pk-helper
Recommends:     dbus(com.intel.dleyna-server)
# the printers panel can use the dbus service
Recommends:     system-config-printer-dbus-service
Provides:       acme
Provides:       fontilus
Provides:       themus
Obsoletes:      acme
Obsoletes:      fontilus
Obsoletes:      themus
Provides:       control-center2 = 2.22.1
Obsoletes:      control-center2 < 2.22.1
# gnome-control-center-branding was obsoleted with g-c-c 3.8.0 (after openSUSE 12.3)
Obsoletes:      gnome-control-center-branding <= 12.3
Obsoletes:      gnome-control-center-branding-openSUSE <= 12.3
Obsoletes:      gnome-control-center-branding-upstream <= 12.3
%if %{with wacom}
BuildRequires:  pkgconfig(clutter-1.0) >= 1.11.3
BuildRequires:  pkgconfig(libwacom) >= 0.7
%endif
%if %{with ibus}
BuildRequires:  pkgconfig(ibus-1.0) >= 1.5.2
%endif

%description
The control center is GNOME's main interface for configuration of
various aspects of your desktop.

%package user-faces
Summary:        Login manager user avatars
Group:          System/GUI/GNOME

%description user-faces
This package provides user avatars to be used by display managers

%package devel
Summary:        Header files for the GNOME Control Center
Group:          Development/Libraries/GNOME
Requires:       %{name} = %{version}
Provides:       control-center2-devel = 2.22.1
Obsoletes:      control-center2-devel < 2.22.1

%description devel
The control center is GNOME's main interface for configuration of
various aspects of your desktop.

%package color
Summary:        Configuration panel for color management
Group:          System/GUI/GNOME
Requires:       %{name} = %{version}
# The color panel requires colord to be present for the glib schema
Requires:       colord
# The color panel interacts with binaries from gnome-color-manager
Requires:       gnome-color-manager
Supplements:    %{name}

%description color
This package provides the color management configuration panel for
GNOME control center.

%package goa
Summary:        Configuration panel for online accounts
Group:          System/GUI/GNOME
Requires:       %{name} = %{version}
# The online accounts panel interacts with binaries and icons from gnome-online-accounts
Requires:       gnome-online-accounts
Supplements:    packageand(%{name}:gnome-online-accounts)

%description goa
This package provides the online accounts onfiguration panel for
GNOME control center.

%lang_package

%prep
%setup -q
translation-update-upstream po gnome-control-center-2.0

# patches for Leap >= 15 plus SLE >= 15, but not TW
%if 0%{?sle_version} >= 150000
%patch1001 -p1
%patch1002 -p1
%patch1003 -p1
%endif

%build
%meson \
	-Dcheese=true \
	-Ddocumentation=true \
	%{!?with_ibus: -Dibus=false} \
	%{nil}
%meson_build

%check
%meson_test

%install
%meson_install
%find_lang %{name}-2.0 %{?no_lang_C}
%find_lang %{name}-2.0-timezones %{name}-2.0.lang
%fdupes %{buildroot}/%{_prefix}

# We do not package gnome-control-center.rules (bnc#804966)
rm %{buildroot}%{_datadir}/polkit-1/rules.d/gnome-control-center.rules

%files
%license COPYING
%doc NEWS README.md
%{_bindir}/*
%{_datadir}/metainfo/gnome-control-center.appdata.xml
%exclude %{_datadir}/applications/gnome-color-panel.desktop
%exclude %{_datadir}/applications/gnome-online-accounts-panel.desktop
%{_datadir}/applications/*.desktop
%{_datadir}/bash-completion/completions/gnome-control-center
%{_datadir}/dbus-1/services/org.gnome.ControlCenter.service
%{_datadir}/dbus-1/services/org.gnome.ControlCenter.SearchProvider.service
%{_datadir}/glib-2.0/schemas/org.gnome.ControlCenter.gschema.xml
%{_datadir}/gnome-control-center/
%dir %{_datadir}/gnome-shell/
%dir %{_datadir}/gnome-shell/search-providers/
%{_datadir}/gnome-shell/search-providers/gnome-control-center-search-provider.ini
%{_datadir}/icons/hicolor/*/*/*.png
%{_datadir}/icons/hicolor/*/*/*.svg
%{_datadir}/locale/en/
%{_datadir}/polkit-1/actions/org.gnome.controlcenter.datetime.policy
%{_datadir}/polkit-1/actions/org.gnome.controlcenter.remote-login-helper.policy
%{_datadir}/polkit-1/actions/org.gnome.controlcenter.user-accounts.policy
# We do not package gnome-control-center.rules
#{_datadir}/polkit-1/rules.d/gnome-control-center.rules
%dir %{_datadir}/sounds/gnome
%dir %{_datadir}/sounds/gnome/default
%dir %{_datadir}/sounds/gnome/default/alerts
%{_datadir}/sounds/gnome/default/alerts/*.ogg
%{_libexecdir}/cc-remote-login-helper
%{_libexecdir}/gnome-control-center-print-renderer
%{_libexecdir}/gnome-control-center-search-provider
%{_mandir}/man1/gnome-control-center.1%{?ext_man}

%files user-faces
%{_datadir}/pixmaps/faces/

%files color
%{_datadir}/applications/gnome-color-panel.desktop

%files goa
%{_datadir}/applications/gnome-online-accounts-panel.desktop

%files devel
%doc gnome-control-center.doap
%{_datadir}/pkgconfig/gnome-keybindings.pc
%{_datadir}/gettext/its/gnome-keybindings.its
%{_datadir}/gettext/its/gnome-keybindings.loc
%{_datadir}/gettext/its/sounds.its
%{_datadir}/gettext/its/sounds.loc

%files lang -f %{name}-2.0.lang
# english locale should be in the main package
%exclude %{_datadir}/locale/en

%changelog
