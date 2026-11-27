#
# spec file for package halloween-openSUSE
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "firefox"
# Firefox reads the theme only from its arch-specific %%{_libdir} folder,
# so it builds apart and the rest stays noarch
%define psuffix -firefox-theme
%endif
%define base_name halloween-openSUSE
Name:           %{base_name}%{?psuffix}
Version:        2026.10.6
Release:        0
URL:            https://github.com/plusky/halloween-openSUSE
Source0:        %{url}/releases/download/v%{version}/%{base_name}-%{version}.tar.gz
# The build downloads these pinned files (tools/upstream.toml); they are
# provided here and placed where tools/common.py's fetch() reuses them.
Source1:        https://download.kde.org/stable/plasma/6.8.0/libplasma-6.8.0.tar.xz
Source2:        https://github.com/lassekongo83/adw-gtk3/releases/download/v6.5/adw-gtk3v6.5.tar.xz
Source3:        https://archive.xfce.org/src/xfce/xfwm4/4.20/xfwm4-4.20.0.tar.bz2
Source4:        https://invent.kde.org/sysadmin/ci-utilities/-/raw/68adf5e6e8c83db9327f7b1d2980e67fc12d548c/resources/jsonschemas/kpluginmetadata.schema.json
Source10:       https://gitlab.freedesktop.org/plymouth/plymouth/-/raw/26.134.222/themes/spinner/bullet.png#/plymouth-bullet.png
Source11:       https://gitlab.freedesktop.org/plymouth/plymouth/-/raw/26.134.222/themes/spinner/capslock.png#/plymouth-capslock.png
Source12:       https://gitlab.freedesktop.org/plymouth/plymouth/-/raw/26.134.222/themes/spinner/entry.png#/plymouth-entry.png
Source13:       https://gitlab.freedesktop.org/plymouth/plymouth/-/raw/26.134.222/themes/spinner/keyboard.png#/plymouth-keyboard.png
Source14:       https://gitlab.freedesktop.org/plymouth/plymouth/-/raw/26.134.222/themes/spinner/lock.png#/plymouth-lock.png
BuildRequires:  python3 >= 3.11
BuildRequires:  python3-Pillow >= 11.3.0
BuildRequires:  python3-jsonschema >= 4.24.0
BuildRequires:  python3-license-expression >= 30.0
BuildRequires:  python3-scour >= 0.38.2
%if "%{flavor}" == "firefox"
Summary:        Halloween theme for Firefox
License:        CC-BY-SA-4.0
Requires:       MozillaFirefox%{?_isa}
Supplements:    (%{base_name} and MozillaFirefox%{?_isa})
%else
Summary:        Autumn Halloween desktop theme
License:        CC-BY-SA-4.0 AND CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.0-or-later AND LGPL-2.1-only
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
# kf6-filesystem and plymouth own the Plasma and Plymouth directories, as for
# Factory's Plasma and Plymouth themes; the icon theme links into Breeze Dark
# and the SDDM theme into breeze-openSUSE, whose targets brp-25-symlink checks.
BuildRequires:  kf6-breeze-icons
BuildRequires:  kf6-filesystem
BuildRequires:  plasma6-sddm-theme-openSUSE
BuildRequires:  plymouth
# tools/check.py's licence lint, run once in this flavor
BuildRequires:  reuse >= 6.2.0
Requires:       %{name}-wallpapers = %{version}-%{release}
BuildArch:      noarch
%endif
%if "%{flavor}" == "firefox"
%description
The Halloween Firefox theme, installed into Firefox's application
extension directory.

%package -n %{base_name}-firefox-defaults
Summary:        Make the Halloween theme Firefox's default
License:        CC0-1.0
Requires:       %{name} = %{version}-%{release}
Supplements:    (%{base_name} and %{name})

%description -n %{base_name}-firefox-defaults
A Firefox vendor preference that makes the Halloween theme the theme
of every Firefox profile created from then on. Existing profiles keep
their theme, and a theme picked in the add-ons manager still wins.
%else
%description
A cosy autumn Halloween theme for openSUSE Tumbleweed with KDE Plasma,
GNOME, Xfce and Sway. This metapackage installs the wallpapers and,
through the subpackages' Supplements, the pieces for the desktops and
programs present on the system: the Plasma theme, icon themes, SDDM
login theme, Plymouth boot splash, GTK 3, GNOME Shell, Xfce and Sway
themes, the Firefox theme, and the SDDM, Plasma Login Manager, GNOME
and Firefox defaults that make it the default there.
Users' own choices still win over those defaults.

%package wallpapers
Summary:        Halloween wallpapers for Plasma, GNOME and Xfce
License:        CC-BY-SA-4.0 AND CC0-1.0

%description wallpapers
Light and dark autumn Halloween wallpapers, for Plasma's wallpaper
picker and GNOME's background settings.

%package icon-theme
Summary:        Halloween icon theme based on Breeze
License:        CC-BY-SA-4.0
# Its kde/ folder links to Breeze Dark's icons
Requires:       kf6-breeze-icons
Supplements:    (%{name} and plasma6-workspace)

%description icon-theme
The openSUSE-halloween freedesktop icon theme, which falls back to
Breeze for the icons it does not draw.

%package adwaita-icon-theme
Summary:        Halloween icon theme based on Adwaita
License:        CC-BY-SA-4.0
# Links its icon folders to the openSUSE-halloween theme
Requires:       %{name}-icon-theme = %{version}-%{release}
Requires:       pkgconfig(adwaita-icon-theme)
Recommends:     (adwaita-xfce-icon-theme if xfwm4)
Supplements:    (%{name} and (gnome-shell or xfwm4 or sway))

%description adwaita-icon-theme
The openSUSE-halloween-adwaita freedesktop icon theme for GNOME,
Xfce and Sway: the openSUSE-halloween icons, falling back to Adwaita
for the icons they do not draw.

%package plasma
Summary:        Halloween colour scheme, Plasma style and global theme
License:        CC-BY-SA-4.0 AND GPL-2.0-or-later AND LGPL-2.0-or-later
Requires:       %{name}-icon-theme = %{version}-%{release}
Requires:       %{name}-wallpapers = %{version}-%{release}
Requires:       plasma6-workspace
Supplements:    (%{name} and plasma6-workspace)

%description plasma
The Halloween colour scheme, Plasma style and global theme (with its
splash screen) for KDE Plasma 6, and the login background for Plasma
Login Manager.

%package sddm-theme
Summary:        Halloween login theme for SDDM
License:        CC-BY-SA-4.0 AND CC0-1.0
# The theme links its QML to openSUSE's breeze-openSUSE theme.
Requires:       plasma6-sddm-theme-openSUSE
Supplements:    (%{name} and plasma6-sddm-theme-openSUSE)

%description sddm-theme
The breeze-openSUSE-halloween SDDM login theme: openSUSE's Breeze login
screen with a Halloween background.

%package plymouth-theme
Summary:        Halloween boot splash for Plymouth
License:        CC-BY-SA-4.0 AND GPL-2.0-or-later
Requires:       plymouth
Requires:       plymouth-plugin-two-step
Supplements:    (%{name} and plymouth)

%description plymouth-theme
The openSUSE-halloween Plymouth boot splash. Selecting it and rebuilding
the initrd is left to the administrator.

%package gtk3-theme
Summary:        Halloween GTK 3, GNOME Shell and Xfce themes
License:        CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.1-only
Suggests:       gnome-shell-extension-user-theme
Supplements:    (%{name} and (gnome-shell or xfwm4 or sway))

%description gtk3-theme
The openSUSE-halloween GTK 3 theme with a GNOME Shell stylesheet (used
through the User Themes extension), and xfwm4 and xfce4-notifyd themes
for Xfce.

%package sway-theme
Summary:        Halloween theme for Sway, Waybar and SwayNotificationCenter
License:        CC0-1.0
Supplements:    (%{name} and sway)

%description sway-theme
Window colours, borders and gaps for Sway, a Waybar stylesheet and a
SwayNotificationCenter theme. Selecting them in the programs'
configuration is left to the user.

%package sddm-defaults
Summary:        Make the Halloween login theme SDDM's default
License:        CC0-1.0
Requires:       %{name}-sddm-theme = %{version}-%{release}
Supplements:    (%{name} and %{name}-sddm-theme)

%description sddm-defaults
An SDDM vendor configuration drop-in that makes the
Halloween login theme the default. A login theme the administrator
picks in System Settings still wins.

%package plasmalogin-defaults
Summary:        Make the Halloween background Plasma Login Manager's default
License:        CC0-1.0
Requires:       %{name}-plasma = %{version}-%{release}
Supplements:    (%{name} and plasma6-login-manager)

%description plasmalogin-defaults
A Plasma Login Manager vendor configuration drop-in that makes the
Halloween background the login screen's wallpaper. A background the
administrator picks in System Settings still wins.

%package gnome-defaults
Summary:        Make the Halloween theme GNOME's default
License:        CC0-1.0
Requires:       %{name}-gtk3-theme = %{version}-%{release}
Requires:       %{name}-wallpapers = %{version}-%{release}
Supplements:    (%{name} and gnome-shell)

%description gnome-defaults
A GSettings override that makes the Halloween colours, wallpaper and
Shell theme GNOME's defaults, for the login screen too, and colours
IBus's keyboard indicator to match. Users' own choices still win.
%endif

%prep
%autosetup -p1 -n %{base_name}-%{version}
# Rebuild everything from the sources, not the archive's prebuilt output
rm -rf build
mkdir -p build/cache/libplasma-breeze build/cache/archives build/cache/kde build/cache/plymouth
tar -xf %{SOURCE1} -C build/cache/libplasma-breeze --strip-components=4 libplasma-6.8.0/src/desktoptheme/breeze
cp -p %{SOURCE2} %{SOURCE3} build/cache/archives/
cp -p %{SOURCE4} build/cache/kde/kpluginmetadata.schema.json
for f in %{SOURCE10} %{SOURCE11} %{SOURCE12} %{SOURCE13} %{SOURCE14}; do
  cp -p "$f" build/cache/plymouth/"$(basename "$f" | sed 's/^plymouth-//')"
done

%build
python3 tools/build.py

%install
%if "%{flavor}" == "firefox"
install -Dpm0644 build/firefox/openSUSE-halloween.xpi \
  %{buildroot}%{_libdir}/firefox/browser/extensions/openSUSE-halloween@pluskal.org.xpi
install -Dpm0644 build/defaults/firefox/openSUSE-halloween.js \
  %{buildroot}%{_libdir}/firefox/browser/defaults/preferences/openSUSE-halloween.js
%else
python3 tools/install.py --quiet --destdir %{buildroot} --prefix %{_prefix} \
  --libdir %{_libdir} --sysconfdir %{_sysconfdir}
python3 tools/install.py --quiet --defaults --destdir %{buildroot} --prefix %{_prefix} \
  --libdir %{_libdir} --sysconfdir %{_sysconfdir}
%icon_theme_cache_create_ghost openSUSE-halloween
%icon_theme_cache_create_ghost openSUSE-halloween-adwaita
# The Firefox theme is the firefox flavor's
rm -r %{buildroot}%{_libdir}/firefox
%fdupes %{buildroot}%{_datadir}
%endif

%check
# The real art masters were used, not drawn placeholders
test ! -s build/placeholders.txt
python3 tools/check.py --release
# Reproducible: a second build gives the same manifest
cp build/MANIFEST.sha256 MANIFEST.first
python3 tools/build.py
cmp MANIFEST.first build/MANIFEST.sha256

%if "%{flavor}" == "firefox"
%files
%license LICENSES/CC-BY-SA-4.0.txt
%dir %{_libdir}/firefox
%dir %{_libdir}/firefox/browser
%dir %{_libdir}/firefox/browser/extensions
%{_libdir}/firefox/browser/extensions/openSUSE-halloween@pluskal.org.xpi

%files -n %{base_name}-firefox-defaults
%license LICENSES/CC0-1.0.txt
%dir %{_libdir}/firefox
%dir %{_libdir}/firefox/browser
%dir %{_libdir}/firefox/browser/defaults
%dir %{_libdir}/firefox/browser/defaults/preferences
%{_libdir}/firefox/browser/defaults/preferences/openSUSE-halloween.js
%else
%files

%files wallpapers
%license LICENSES/CC-BY-SA-4.0.txt LICENSES/CC0-1.0.txt
%doc README.md
%dir %{_datadir}/wallpapers
%{_datadir}/wallpapers/openSUSEhalloween
%dir %{_datadir}/backgrounds
%{_datadir}/backgrounds/openSUSEhalloween
%dir %{_datadir}/gnome-background-properties
%{_datadir}/gnome-background-properties/openSUSEhalloween.xml

%files icon-theme
%license LICENSES/CC-BY-SA-4.0.txt
%{_datadir}/icons/openSUSE-halloween
%ghost %{_datadir}/icons/openSUSE-halloween/icon-theme.cache

%files adwaita-icon-theme
%license LICENSES/CC-BY-SA-4.0.txt
%{_datadir}/icons/openSUSE-halloween-adwaita
%ghost %{_datadir}/icons/openSUSE-halloween-adwaita/icon-theme.cache

%files plasma
%license LICENSES/CC-BY-SA-4.0.txt LICENSES/GPL-2.0-or-later.txt LICENSES/LGPL-2.0-or-later.txt
%{_datadir}/color-schemes/openSUSEHalloween.colors
%{_datadir}/plasma/desktoptheme/openSUSE-halloween
%{_datadir}/plasma/look-and-feel/org.openSUSE.halloween.desktop
%dir %{_datadir}/openSUSE-halloween
%{_datadir}/openSUSE-halloween/plasmalogin

%files sddm-theme
%license LICENSES/CC-BY-SA-4.0.txt LICENSES/CC0-1.0.txt
%{_datadir}/sddm/themes/breeze-openSUSE-halloween

%files plymouth-theme
%license LICENSES/CC-BY-SA-4.0.txt LICENSES/GPL-2.0-or-later.txt
%{_datadir}/plymouth/themes/openSUSE-halloween

%files gtk3-theme
%license LICENSES/CC0-1.0.txt LICENSES/GPL-2.0-or-later.txt LICENSES/LGPL-2.1-only.txt
%{_datadir}/themes/openSUSE-halloween
%{_datadir}/themes/openSUSE-halloween-hdpi
%{_datadir}/themes/openSUSE-halloween-xhdpi

%files sway-theme
%license LICENSES/CC0-1.0.txt
%dir %{_datadir}/openSUSE-halloween
%{_datadir}/openSUSE-halloween/sway
%{_datadir}/openSUSE-halloween/swaync
%{_datadir}/openSUSE-halloween/waybar

%files sddm-defaults
%license LICENSES/CC0-1.0.txt
%dir %{_prefix}/lib/sddm
%dir %{_prefix}/lib/sddm/sddm.conf.d
%{_prefix}/lib/sddm/sddm.conf.d/30-breeze-openSUSE-halloween.conf

%files plasmalogin-defaults
%license LICENSES/CC0-1.0.txt
%dir %{_prefix}/lib/plasmalogin
%dir %{_prefix}/lib/plasmalogin/plasmalogin.conf.d
%{_prefix}/lib/plasmalogin/plasmalogin.conf.d/30-openSUSE-halloween.conf

%files gnome-defaults
%license LICENSES/CC0-1.0.txt
%{_datadir}/glib-2.0/schemas/30_openSUSE-halloween.gschema.override
%endif

%changelog
