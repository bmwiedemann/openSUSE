#
# spec file for package xfdesktop
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


%bcond_with git
Name:           xfdesktop
Version:        4.20.1
Release:        0
Summary:        Desktop Manager for the Xfce Desktop Environment
License:        GPL-2.0-or-later
Group:          System/GUI/XFCE
URL:            https://docs.xfce.org/xfce/xfdesktop/start
Source0:        https://archive.xfce.org/src/xfce/xfdesktop/4.20/%{name}-%{version}.tar.bz2
# PATCH-FEATURE-OPENSUSE xfdesktop-backgrounds-path.patch bnc#800970 gber@opensuse.org -- Deliver background images under DATADIR/wallpapers which is already used by openSUSE and fix the default path for background images in the settings dialog
Patch0:         xfdesktop-backgrounds-path.patch
# PATCH-FIX-OPENSUSE 0002-relax-libyaml-version.patch -- Allow build for Leap with its ancient but sufficient libyaml packages.
Patch2:         0002-relax-libyaml-version.patch
%if 0%{?suse_version} && 0%{?suse_version} < 1550
# Default gcc7 is too old for new C20 features
BuildRequires:  gcc13
%endif
BuildRequires:  fdupes
BuildRequires:  gettext >= 0.19.8
BuildRequires:  update-desktop-files
BuildRequires:  xfce4-dev-tools
BuildRequires:  pkgconfig(cairo) >= 1.16
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(exo-2) >= 0.11.0
BuildRequires:  pkgconfig(garcon-1) >= 0.6.0
BuildRequires:  pkgconfig(gdk-wayland-3.0) >= 3.24.10
BuildRequires:  pkgconfig(gdk-x11-3.0) >= 3.24.10
BuildRequires:  pkgconfig(gio-2.0) >= 2.72.0
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.72.0
BuildRequires:  pkgconfig(glib-2.0) >= 2.72.0
BuildRequires:  pkgconfig(gmodule-2.0) >= 2.72.0
BuildRequires:  pkgconfig(gobject-2.0) >= 2.72.0
BuildRequires:  pkgconfig(gthread-2.0) >= 2.72.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.24.0
BuildRequires:  pkgconfig(gtk-layer-shell-0) >= 0.7.0
BuildRequires:  pkgconfig(libnotify) >= 0.4.0
BuildRequires:  pkgconfig(libwnck-3.0) >= 3.14
BuildRequires:  pkgconfig(libxfce4kbd-private-3) >= 4.18.0
BuildRequires:  pkgconfig(libxfce4ui-2) >= 4.18.0
BuildRequires:  pkgconfig(libxfce4util-1.0) >= 4.13.0
BuildRequires:  pkgconfig(libxfce4windowing-0) >= 4.19.8
BuildRequires:  pkgconfig(libxfce4windowing-x11-0) >= 4.19.8
BuildRequires:  pkgconfig(libxfce4windowingui-0) >= 4.19.8
BuildRequires:  pkgconfig(libxfconf-0) >= 4.19.3
BuildRequires:  pkgconfig(thunarx-3) >= 4.17.10
BuildRequires:  pkgconfig(x11) >= 1.6.7
BuildRequires:  pkgconfig(yaml-0.1) >= 0.1.7
Provides:       xfce4-desktop = %{version}
Obsoletes:      xfce4-desktop < %{version}
Requires:       %{name}-branding = %{version}
# menu data
Requires:       libgarcon-data
# uses exo-desktop-item-edit
Requires:       exo-tools
Recommends:     %{name}-lang = %{version}

%description
Xfdesktop is a desktop manager for the Xfce Desktop Environment which can set
the background image, provides a right-click menu to launch applications and
can optionally show files (including application launchers) or iconified
windows, includes gradient support for background color, saturation support for
background images, as well as real multiscreen and xinerama support.

%package branding-upstream
Summary:        Upstream Branding of xfce4-settings
# BRAND: default.jpg: Control the default backdrop image.
Group:          System/GUI/XFCE
Conflicts:      otherproviders(%{name}-branding)
Provides:       %{name}-branding = %{version}
Provides:       xfce4-desktop-branding-upstream = %{version}
Obsoletes:      xfce4-desktop-branding-upstream < %{version}
Supplements:    packageand(%{name}:branding-upstream)
BuildArch:      noarch

%description branding-upstream
This package provides the upstream look and feel for the Xfce Desktop Manager.

%lang_package

%prep
%autosetup -p1

%build
%if 0%{?suse_version} && 0%{?suse_version} < 1550
export CC=gcc-13
%endif
%if %{with git}
NOCONFIGURE=1 ./autogen.sh
%configure \
    --enable-maintainer-mode
    --with-default-backdrop-filename=%{_datadir}/wallpapers/xfce/default.wallpaper
%else
xdt-autogen
%configure \
    --with-default-backdrop-filename=%{_datadir}/wallpapers/xfce/default.wallpaper
%endif
%make_build

%install
%make_install

# default upstream backdrop image
ln -s %{_datadir}/wallpapers/xfce/xfce-blue.jpg \
    %{buildroot}%{_datadir}/wallpapers/xfce/default.wallpaper

%suse_update_desktop_file xfce-backdrop-settings

rm -rf %{buildroot}%{_datadir}/locale/{ast,kk,tl_PH,ur_PK}

%find_lang %{name} %{?no_lang_C}

%fdupes %{buildroot}%{_datadir}

%files
%doc README.md AUTHORS NEWS
%license COPYING
%{_bindir}/xfdesktop
%{_bindir}/xfdesktop-settings
%{_datadir}/applications/xfce-backdrop-settings.desktop
%{_datadir}/pixmaps/*.png
%{_datadir}/icons/hicolor/*/*/*.png
%{_datadir}/icons/hicolor/*/*/*.svg
%{_mandir}/man1/xfdesktop.1.gz
%{_datadir}/pixmaps/xfdesktop
%dir %{_datadir}/wallpapers
%dir %{_datadir}/wallpapers/xfce
%{_datadir}/wallpapers/xfce/*.jpg
%{_datadir}/wallpapers/xfce/*.svg

%files lang -f %{name}.lang

%files branding-upstream
%{_datadir}/wallpapers/xfce/default.wallpaper

%changelog
