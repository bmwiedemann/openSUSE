#
# spec file for package mate-control-center
#
# Copyright (c) 2024 SUSE LLC
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


%define   soname          libmate-window-settings
%define   sover           1
%define   soname_slab     libmate-slab
%define   sover_slab      0
%define   _version        1.28

Name:           mate-control-center
Version:        1.28.0
Release:        0
Summary:        MATE Desktop control center
License:        GPL-2.0-or-later
Group:          System/GUI/Other
URL:            https://mate-desktop.org/
Source:         https://pub.mate-desktop.org/releases/%{_version}/%{name}-%{version}.tar.xz
BuildRequires:  fdupes
BuildRequires:  mate-common
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  systemd-rpm-macros
BuildRequires:  update-desktop-files
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(accountsservice)
BuildRequires:  pkgconfig(atk)
%ifnarch ppc64le s390x
BuildRequires:  pkgconfig(ayatana-appindicator3-0.1)
%endif
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(dconf) >= 0.11.0
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libcanberra-gtk3)
BuildRequires:  pkgconfig(libgtop-2.0)
BuildRequires:  pkgconfig(libmarco-private) >= %{_version}
BuildRequires:  pkgconfig(libmate-menu) >= %{_version}
BuildRequires:  pkgconfig(libmatekbd)
BuildRequires:  pkgconfig(libmatekbdui)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(libxklavier)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(mate-desktop-2.0) >= %{_version}
BuildRequires:  pkgconfig(mate-settings-daemon) >= %{_version}
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(udisks2)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xscrnsaver)
Requires:       %{name}-branding >= %{_version}
Requires:       gsettings-backend-dconf
Requires:       gsettings-desktop-schemas
Recommends:     %{name}-lang
%glib2_gsettings_schema_requires
%if 0%{?is_opensuse}
BuildRequires:  pkgconfig(appindicator3-0.1)
%endif

%description
The control center is MATE's main interface for configuration of various
aspects of your desktop.

%package branding-upstream
Summary:        The MATE Control Center -- Upstream Definition of Shell Content
Requires:       %{name} = %{version}
Supplements:    (%{name} and branding-upstream)
Conflicts:      %{name}-branding
Provides:       %{name}-branding = %{version}
BuildArch:      noarch
#BRAND: This package contains the definitions of the content appearing
#BRAND: in the shell (/etc/xdg/menus/matecc.menu).

%description branding-upstream
The control center is MATE's main interface for configuration of
various aspects of your desktop.

This package provides the upstream definition of what appears in the
control center.

%package devel
Summary:        Header files for MATE Control Center
Group:          Development/Libraries/X11

%description devel
The control center is MATE's main interface for configuration of various
aspects of your desktop.

This package provides MATE control center development files.

%lang_package

%prep
%autosetup -p1

%build
%configure \
  --disable-static        \
  --disable-update-mimedb
%make_build

%install
%make_install

rm -f %{buildroot}%{_datadir}/applications/mimeinfo.cache
find %{buildroot} -type f -name "*.la" -delete -print
%find_lang %{name} %{?no_lang_C}

%suse_update_desktop_file mate-settings-mouse
%suse_update_desktop_file mate-network-properties
%suse_update_desktop_file mate-appearance-properties
%suse_update_desktop_file mate-keybinding
%suse_update_desktop_file -r mate-font-viewer GTK Utility Settings DesktopSettings
%suse_update_desktop_file mate-theme-installer
%suse_update_desktop_file mate-default-applications-properties

%fdupes -s %{buildroot}%{_datadir}

%files
%license COPYING
%doc NEWS README
%{_sbindir}/mate-display-properties-install-systemwide
%{_bindir}/mate-*
%{_datadir}/applications/*.desktop
%{_datadir}/mate-control-center/*
%dir %{_datadir}/mate-time-admin
%{_datadir}/mate-time-admin/*
%{_datadir}/mime/packages/mate-theme-package.xml
%{_datadir}/polkit-1/actions/org.mate.randr.policy
%{_datadir}/glib-2.0/schemas/*.xml
%{_datadir}/help/C/%{name}/
%{_datadir}/icons/hicolor/*/*/*.png
%{_datadir}/icons/hicolor/scalable/apps/*.svg
%{_datadir}/thumbnailers/
# From upstream branding.
%exclude %{_sysconfdir}/xdg/menus/matecc.menu
%dir %{_datadir}/desktop-directories
%{_datadir}/desktop-directories/matecc.directory
%{_mandir}/man?/mate-*.?%{?ext_man}

%files branding-upstream
%dir %{_sysconfdir}/xdg/menus
%config %{_sysconfdir}/xdg/menus/matecc.menu

%files devel
%{_libdir}/pkgconfig/mate-default-applications.pc
%{_libdir}/pkgconfig/mate-keybindings.pc

%files lang -f %{name}.lang

%changelog
