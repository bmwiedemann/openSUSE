#
# spec file for package cinnamon
#
# Copyright (c) 2025 SUSE LLC
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


%define _version 6.4.6
Name:           cinnamon
Version:        6.4.6
Release:        0
Summary:        GNU/Linux Desktop featuring a traditional layout
License:        GPL-2.0-or-later AND LGPL-2.1-only
Group:          System/GUI/Other
URL:            https://github.com/linuxmint/cinnamon
Source:         https://github.com/linuxmint/cinnamon/archive/%{version}/%{name}-%{version}.tar.gz
# Some documentation for people writing branding packages, shipped in the branding-upstream package.
Source1:        README.Gsettings-overrides
# PATCH-FIX-OPENSUSE cinnamon-wheel-and-sbin-path sor.alexei@meowr.ru -- Make full sbin paths and use wheel as a sudo group.
Patch1:         %{name}-wheel-and-sbin-path.patch
# PATCH-FIX-OPENSUSE cinnamon-settings-native.patch andythe_great@pm.me shenlebantongying@gmail.com -- Remove foreign configuration tools and add openSUSE's native.
Patch2:         %{name}-settings-native.patch
# PATCH-FIX-OPENSUSE cinnamon-settings-xscreensaver-path.patch boo#960165 sor.alexei@meowr.ru -- Fix xscreensaver configs path.
Patch3:         %{name}-settings-xscreensaver-path.patch
# PATCH-FEATURE-OPENSUSE cinnamon-favourite-applications.patch sor.alexei@meowr.ru -- Remove mintinstall from favourites and add YaST.
Patch4:         %{name}-favourite-applications.patch
# PATCH-FEATURE-OPENSUSE cinnamon-fallback-icewm.patch sor.alexei@meowr.ru -- Use IceWM as fallback.
Patch7:         %{name}-fallback-icewm.patch
# For gnome-background-properties.
# PATCH-FIX-OPENSUSE support_yast_settings.patch shenlebantongying@gmail.com gh#linuxmint/cinnamon#9590 -- Fix cinnamon-settings cannot invoke YaST commands.
Patch8:         support_yast_settings.patch

BuildRequires:  cmake
BuildRequires:  desktop-data-openSUSE-extra
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gtk-doc
# For distributor.svg.
BuildRequires:  hicolor-icon-theme-branding-openSUSE
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  python3-devel
BuildRequires:  python3-libsass
BuildRequires:  python3-xml
BuildRequires:  pkgconfig(cinnamon-desktop) >= 6.2.0
BuildRequires:  pkgconfig(cjs-1.0) >= 6.0.0
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(gcr-base-3)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(libcinnamon-menu-3.0)
BuildRequires:  pkgconfig(libmuffin-0) >= 6.2.0
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(libstartup-notification-1.0)
BuildRequires:  pkgconfig(polkit-agent-1)
BuildRequires:  pkgconfig(xapp)
Requires:       %{name}-gschemas = %{version}
Requires:       adwaita-icon-theme
Requires:       cinnamon-control-center-common >= 6.2.0
Requires:       cinnamon-screensaver >= 6.0.3
Requires:       cinnamon-session >= 6.2.1
Requires:       cinnamon-settings-daemon >= 6.2.0
Requires:       cjs >= 6.0.0
Requires:       cups-pk-helper
Requires:       dbus-1
Requires:       gettext-runtime
Requires:       glib2-tools
# gkbd-capplet / gkbd-keyboard-display.
Requires:       gnomekbd-tools
Requires:       iso-country-flags-png
Requires:       libcinnamon-desktop-data >= 6.2.0
Requires:       muffin >= 6.2.0
Requires:       nemo
Requires:       pkgconfig
Requires:       polkit-gnome
Requires:       python3-Pillow
Requires:       python3-cairo
Requires:       python3-distro
Requires:       python3-gobject
Requires:       python3-gobject-Gdk
Requires:       python3-gobject-cairo
Requires:       python3-pexpect
Requires:       python3-pyinotify
Requires:       python3-python-pam
# cinnamon-settings calendar module
Requires:       python3-pytz
# cinnamon-settings theme module
Requires:       python3-tinycss2
Requires:       v4l-tools
Requires:       wget
Requires:       xdg-user-dirs
Requires:       xdg-user-dirs-gtk
Requires(post): update-alternatives
Requires(postun): update-alternatives
Recommends:     %{name}-lang
Recommends:     blueberry
Recommends:     cinnamon-themes
Recommends:     gnome-terminal
Recommends:     gnome-themes-standard
Recommends:     icewm
# cinnamon-2d was last used in openSUSE 13.2.
Provides:       %{name}-2d = %{version}
Obsoletes:      %{name}-2d < %{version}
# cinnamon-menu-editor was last used in openSUSE 13.2.
Provides:       %{name}-menu-editor = %{version}
Obsoletes:      %{name}-menu-editor < %{version}
# cinnamon-settings was last used in openSUSE 13.2.
Provides:       %{name}-settings = %{version}
Obsoletes:      %{name}-settings < %{version}
# typelib-1_0-Cinnamon-0_1 was last used in openSUSE Leap 42.1.
Provides:       typelib-1_0-Cinnamon-0_1 = %{version}
Obsoletes:      typelib-1_0-Cinnamon-0_1 < %{version}
%if 0%{?suse_version} >= 1500
BuildRequires:  pkgconfig(libnm)
Requires:       NetworkManager-applet
Requires:       python3-dbus-python
%else
BuildRequires:  pkgconfig(libnm-glib)
Requires:       NetworkManager-gnome
Requires:       dbus-1-python3
%endif

%description
Cinnamon is a modern Linux desktop which provides advanced innovative
features and a traditional user experience. It's easy to use,
powerful and flexible.

%package gschemas
Summary:        GNU/Linux Desktop featuring a traditional layout -- GSchemas
Group:          System/Libraries
Requires:       %{name}-gschemas-branding = %{version}
%if 0%{?suse_version} < 1500
%glib2_gsettings_schema_requires
%endif

%description gschemas
This package provides GSettings schemas for
Cinnamon Desktop Environment.

%package gschemas-branding-upstream
Summary:        Upstream definitions of default settings and applications
Group:          System/Libraries
Requires:       %{name}-gschemas = %{version}
Supplements:    (cinnamon-gschemas and branding-upstream)
Conflicts:      %{name}-gschemas-branding
Provides:       %{name}-gschemas-branding = %{version}
# cinnamon-branding-upstream was last used in openSUSE Leap 42.2.
Provides:       %{name}-branding-upstream = %{version}
Obsoletes:      %{name}-branding-upstream < %{version}
BuildArch:      noarch
#BRAND: A /usr/share/glib-2.0/schemas/$NAME.gschema.override file can
#BRAND: be used to override the default value for GSettings keys. See
#BRAND: README.Gsettings-overrides for more details. The branding
#BRAND: package should then have proper Requires for features changed
#BRAND: with such an override file.

%description gschemas-branding-upstream
This package provides upstream defaults for settings stored with
GSettings and applications used by the MIME system.

%prep
%autosetup -p1

cp -a %{SOURCE1} .

for file in files%{_datadir}/%{name}/%{name}-settings/bin/*.py files%{_datadir}/%{name}/%{name}-looking-glass/*.py \
   files%{_datadir}/%{name}/%{name}-settings/modules/cs_{applets,desklets}.py; do
   chmod a+x $file
done
chmod a-x files%{_datadir}/%{name}/%{name}-settings/bin/__init__.py

sed -i -e 's!imports.gi.NMClient!imports_gi_NMClient!g' js/ui/extension.js

%build
%meson --libexecdir=%{_libdir}/%{name}
%meson_build

%install
%meson_install

# Non-executable in /usr/bin/ is unacceptable.
chmod a+x %{buildroot}%{_bindir}/%{name}-file-dialog

# We should own this directory.
mkdir -p %{buildroot}%{_libdir}/%{name}/extensions/

# Provide all GNOME compatible backgrounds (including openSUSE branding) to Cinnamon.
ln -s gnome-background-properties \
  %{buildroot}%{_datadir}/cinnamon-background-properties

dirname $(find %{buildroot}%{_datadir} -type f -name '*.py') | sort -u | while read dir; do
    # Compile Python bytecode.
    %py3_compile .
done

mkdir -p %{buildroot}%{_sysconfdir}/alternatives/
touch %{buildroot}%{_sysconfdir}/alternatives/default-xsession.desktop
ln -s %{_sysconfdir}/alternatives/default-xsession.desktop \
  %{buildroot}%{_datadir}/xsessions/default.desktop

find %{buildroot} -type f -name "*.a" -delete -print
find %{buildroot} -type f -name "*.la" -delete -print
# Delete useless gir files
%{__rm} -rf %{buildroot}%{_datadir}/gir-1.0/
%fdupes %{buildroot}%{_datadir}/

%post
/sbin/ldconfig
%{_sbindir}/update-alternatives --install %{_datadir}/xsessions/default.desktop \
  default-xsession.desktop %{_datadir}/xsessions/%{name}.desktop 20
%if 0%{?suse_version} < 1500
%desktop_database_post
%icon_theme_cache_post
%endif

%postun
/sbin/ldconfig
if [ ! -f %{_datadir}/xsessions/%{name}.desktop ]; then
    %{_sbindir}/update-alternatives --remove default-xsession.desktop \
      %{_datadir}/xsessions/%{name}.desktop
fi
%if 0%{?suse_version} < 1500
%desktop_database_postun
%icon_theme_cache_postun
%endif

%if 0%{?suse_version} < 1500
%post gschemas
%glib2_gsettings_schema_post

%postun gschemas
%glib2_gsettings_schema_postun
%endif

%files
%license COPYING
%doc AUTHORS README.rst debian/changelog
%{_bindir}/%{name}
%{_bindir}/%{name}2d
%{_bindir}/%{name}-*
%{_bindir}/xlet-about-dialog
%{_bindir}/xlet-settings
%config(noreplace) %{_sysconfdir}/xdg/menus/*
%ghost %{_sysconfdir}/alternatives/default-xsession.desktop
%ghost %{_sysconfdir}/alternatives/default.desktop
%{_datadir}/cinnamon-session
%dir %{_datadir}/wayland-sessions
%{_datadir}/wayland-sessions/cinnamon-wayland.desktop
%dir %{_datadir}/xdg-desktop-portal/
%{_datadir}/xdg-desktop-portal/x-cinnamon-portals.conf
%{_datadir}/applications/*
%{_datadir}/dbus-1/services/org.Cinnamon.*.service
%{_datadir}/dbus-1/services/org.cinnamon.*.service
%{_datadir}/desktop-directories/*
%exclude %{_datadir}/%{name}/theme/menu*.svg
%{_datadir}/icons/hicolor/*/*/*.svg
%{_datadir}/icons/hicolor/*/*/*.png
%{_datadir}/polkit-1/actions/org.%{name}.settings-users.policy
%{_datadir}/xsessions/*
%{_datadir}/%{name}/
%{_datadir}/%{name}-background-properties
%{_libdir}/%{name}/
%{_mandir}/man1/cinnamon*%{?ext_man}
%{_prefix}/lib/python%{python_version}/site-packages/%{name}/

%files gschemas
%{_datadir}/glib-2.0/schemas/org.cinnamon.gschema.xml
%{_datadir}/glib-2.0/schemas/org.cinnamon.gestures.gschema.xml

%files gschemas-branding-upstream
%doc README.Gsettings-overrides
%{_datadir}/%{name}/theme/menu*.svg

%changelog
