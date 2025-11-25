#
# spec file for package gnome-control-center
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


# Allow to enable/disable ibus, as GNOME is rather strict on new versions.
%bcond_without  ibus
# Wacom input support
%ifarch s390 s390x
%bcond_with     wacom
%else
%bcond_without  wacom
%endif

Name:           gnome-control-center
Version:        49.2
Release:        0
Summary:        The GNOME Control Center
License:        GPL-2.0-or-later
Group:          System/GUI/GNOME
URL:            https://apps.gnome.org/app/org.gnome.Settings
Source0:        %{name}-%{version}.tar.zst
Source1:        libgxdp-0.gitmodule.tar.zst
Source99:       %{name}-rpmlintrc

### patches for Leap >= 15 plus SLE >= 15, but not TW
# PATCH-FEATURE-SLE gnome-control-center-system-never-use-gnome-software.patch bsc#999336 fezhang@suse.com -- info: Never search for gnome-software as an option when checking for updates on SLE and Leap 42.2, because we use gpk-update-viewer.
Patch1001:      gnome-control-center-system-never-use-gnome-software.patch
# PATCH-FEATURE-SLE gnome-control-center-more-power-button-actions.patch bsc#993381 fezhang@suse.com -- power: Bring back the "shutdown" and "interactive" power button actions.
Patch1002:      gnome-control-center-more-power-button-actions.patch
# PATCH-FEATURE-SLE gnome-control-center-bring-back-firewall-zone.patch fate#316719 sckang@suse.com -- network: Bring back the firewall zone combo box to select proper firewall zone for each connection.
Patch1003:      gnome-control-center-bring-back-firewall-zone.patch

BuildRequires:  /usr/bin/Xvfb
BuildRequires:  blueprint-compiler
BuildRequires:  cups-devel >= 1.4
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  intltool
BuildRequires:  krb5-devel
BuildRequires:  meson >= 0.58.0
BuildRequires:  pkgconfig
BuildRequires:  python3-dbusmock
BuildRequires:  xsltproc
BuildRequires:  pkgconfig(accountsservice) >= 0.6.39
BuildRequires:  pkgconfig(cairo-gobject)
BuildRequires:  pkgconfig(colord) >= 0.1.34
BuildRequires:  pkgconfig(colord-gtk4)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(gcr-4) >= 4.1.0
BuildRequires:  pkgconfig(gdk-pixbuf-2.0) >= 2.23.0
BuildRequires:  pkgconfig(gdk-wayland-3.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glib-2.0) >= 2.76.6
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gnome-bluetooth-3.0)
BuildRequires:  pkgconfig(gnome-desktop-4)
BuildRequires:  pkgconfig(gnome-settings-daemon) >= 41
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(goa-1.0) >= 3.51.0
BuildRequires:  pkgconfig(goa-backend-1.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gsettings-desktop-schemas) >= 47.0
BuildRequires:  pkgconfig(gsound)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk4) >= 4.15.2
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(libadwaita-1) >= 1.6.beta
BuildRequires:  pkgconfig(libgtop-2.0)
BuildRequires:  pkgconfig(libnm) >= 1.24.0
BuildRequires:  pkgconfig(libnma-gtk4)
BuildRequires:  pkgconfig(libpulse) >= 2.0
BuildRequires:  pkgconfig(libpulse-mainloop-glib)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(malcontent-0) => 0.7.0
BuildRequires:  pkgconfig(mm-glib) >= 0.7
BuildRequires:  pkgconfig(polkit-gobject-1) >= 0.103
BuildRequires:  pkgconfig(pwquality) >= 1.2.2
BuildRequires:  pkgconfig(smbclient)
BuildRequires:  pkgconfig(tecla)
BuildRequires:  pkgconfig(udisks2) >= 2.8.2
BuildRequires:  pkgconfig(upower-glib) >= 0.99.8
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xft)
BuildRequires:  pkgconfig(xi) >= 1.2
## CONDITIONAL BUILD REQUIREMENTS
%if %{with wacom}
BuildRequires:  pkgconfig(libwacom) >= 1.4
%endif
%if %{with ibus}
BuildRequires:  pkgconfig(ibus-1.0) >= 1.5.2
%endif
##
Requires:       gnome-settings-daemon >= 41
# needed for universal access panel
Requires:       gnome-themes-accessibility
Requires:       gnome-version
Requires:       iso-codes
# Needed for showing keyboard layout
Requires:       tecla-keyboard-layout-viewer
# For the thunderbolt panel
Recommends:     bolt
Recommends:     %{name}-user-faces
# cups-pk-helper should only be recommended, rather than a hard Requires, see boo#904047
Recommends:     cups-pk-helper
Recommends:     dbus(com.intel.dleyna-server)
# the printers panel can use the dbus service
Recommends:     system-config-printer-dbus-service
# For the power panel
# power-profile-daemon uses a dbus interface, which is provided by tuned-ppd and power-profiles-daemom
# Either one will do
Recommends:     ppd-server
# For parental control (malcontent) support for users
Recommends:     malcontent-control
# If the user expresses no choice, we pick the original power-profiles-daemon for now
Suggests:       power-profiles-daemon
# To ensure that the distribution icon is always displayed in the About section, even for minimal installations
Recommends:     distribution-logos-openSUSE-icons
%if !0%{?is_opensuse}
Recommends:     distribution-logos-branding-SLE
%endif

%description
The control center is GNOME's main interface for configuration of
various aspects of your desktop.

%package user-faces
Summary:        Login manager user avatars
Group:          System/GUI/GNOME
BuildArch:      noarch

%description user-faces
This package provides user avatars to be used by display managers

%package devel
Summary:        Header files for the GNOME Control Center
Group:          Development/Libraries/GNOME
Requires:       %{name} = %{version}
BuildArch:      noarch

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
BuildArch:      noarch

%description color
This package provides the color management configuration panel for
GNOME control center.

%package goa
Summary:        Configuration panel for online accounts
Group:          System/GUI/GNOME
Requires:       %{name} = %{version}
# The online accounts panel interacts with binaries and icons from gnome-online-accounts
Requires:       gnome-online-accounts
Supplements:    (%{name} and gnome-online-accounts)
BuildArch:      noarch

%description goa
This package provides the online accounts onfiguration panel for
GNOME control center.

%package users
Summary:        Configuration panel for User accounts
Group:          System/GUI/GNOME
Requires:       %{name} = %{version}
Supplements:    %{name}
BuildArch:      noarch

%description users
This package provides the online accounts onfiguration panel for
GNOME control center.

%lang_package

%prep
%autosetup -N
pushd subprojects
tar xf %{SOURCE1}
mv libgxdp-0.gitmodule libgxdp
popd
%autopatch -p1 -M 999

# patches for Leap >= 15 plus SLE >= 15, but not TW
%if !0%{?is_opensuse} || 0%{?suse_version} <= 1600
%autopatch -p1 -m 1000
%endif

%build
%meson \
	-Ddocumentation=true \
	%{!?with_ibus: -Dibus=false} \
	-Dmalcontent=true \
	-Dtests=false \
	-Dsnap=false \
	-Dlocation-services=enabled \
	%{nil}
%meson_build

%install
%meson_install
%find_lang %{name}-2.0 %{?no_lang_C}
%find_lang %{name}-2.0-timezones %{name}-2.0.lang
%fdupes %{buildroot}%{_prefix}

# We do not package gnome-control-center.rules (bnc#804966)
rm %{buildroot}%{_datadir}/polkit-1/rules.d/gnome-control-center.rules

%check
%meson_test

%files
%license COPYING
%doc NEWS README.md
%{_bindir}/%{name}
%{_datadir}/metainfo/org.gnome.Settings.metainfo.xml
%exclude %{_datadir}/applications/gnome-color-panel.desktop
%exclude %{_datadir}/applications/gnome-online-accounts-panel.desktop
%exclude %{_datadir}/applications/gnome-users-panel.desktop
%{_datadir}/applications/gnome-about-panel.desktop
%{_datadir}/applications/gnome-applications-panel.desktop
%{_datadir}/applications/gnome-background-panel.desktop
%ifnarch s390x
%{_datadir}/applications/gnome-bluetooth-panel.desktop
%endif
%{_datadir}/applications/gnome-datetime-panel.desktop
%{_datadir}/applications/gnome-display-panel.desktop
%{_datadir}/applications/gnome-keyboard-panel.desktop
%{_datadir}/applications/gnome-mouse-panel.desktop
%{_datadir}/applications/gnome-multitasking-panel.desktop
%{_datadir}/applications/gnome-network-panel.desktop
%{_datadir}/applications/gnome-notifications-panel.desktop
%{_datadir}/applications/gnome-power-panel.desktop
%{_datadir}/applications/gnome-printers-panel.desktop
%{_datadir}/applications/gnome-privacy-panel.desktop
%{_datadir}/applications/gnome-region-panel.desktop
%{_datadir}/applications/gnome-search-panel.desktop
%{_datadir}/applications/gnome-sharing-panel.desktop
%{_datadir}/applications/gnome-sound-panel.desktop
%{_datadir}/applications/gnome-system-panel.desktop
%{_datadir}/applications/gnome-universal-access-panel.desktop
%ifnarch s390x
%{_datadir}/applications/gnome-wacom-panel.desktop
%endif
%{_datadir}/applications/gnome-wellbeing-panel.desktop
%{_datadir}/applications/gnome-wifi-panel.desktop
%{_datadir}/applications/gnome-wwan-panel.desktop
%{_datadir}/applications/org.gnome.Settings.desktop
%{_datadir}/bash-completion/completions/gnome-control-center
%{_libexecdir}/gnome-control-center-global-shortcuts-provider
%{_datadir}/dbus-1/interfaces/org.gnome.GlobalShortcutsRebind.xml
%{_datadir}/dbus-1/services/org.gnome.Settings.GlobalShortcutsProvider.service
%{_datadir}/dbus-1/services/org.gnome.Settings.service
%{_datadir}/dbus-1/services/org.gnome.Settings.SearchProvider.service
%{_datadir}/glib-2.0/schemas/org.gnome.Settings.gschema.xml
%{_datadir}/gnome-control-center/
%dir %{_datadir}/gnome-shell/
%dir %{_datadir}/gnome-shell/search-providers/
%{_datadir}/gnome-shell/search-providers/org.gnome.Settings.search-provider.ini
%{_datadir}/icons/hicolor/*/*/*.svg
%{_datadir}/icons/gnome-logo-text-dark.svg
%{_datadir}/icons/gnome-logo-text.svg
%{_datadir}/locale/en/
%{_datadir}/polkit-1/actions/org.gnome.controlcenter.remote-login-helper.policy
%{_datadir}/polkit-1/actions/org.gnome.controlcenter.remote-session-helper.policy
%{_datadir}/polkit-1/actions/org.gnome.controlcenter.system.policy
%{_datadir}/polkit-1/actions/org.gnome.controlcenter.user-accounts.policy
# We do not package gnome-control-center.rules
#{_datadir}/polkit-1/rules.d/gnome-control-center.rules
%dir %{_datadir}/sounds/gnome
%dir %{_datadir}/sounds/gnome/default
%dir %{_datadir}/sounds/gnome/default/alerts
%{_datadir}/sounds/gnome/default/alerts/*.ogg
%{_libexecdir}/gnome-control-center-print-renderer
%{_libexecdir}/gnome-control-center-search-provider
%{_mandir}/man1/gnome-control-center.1%{?ext_man}

%files user-faces
%{_datadir}/pixmaps/faces/

%files color
%{_datadir}/applications/gnome-color-panel.desktop

%files goa
%{_datadir}/applications/gnome-online-accounts-panel.desktop

%files users
%{_datadir}/applications/gnome-users-panel.desktop

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
