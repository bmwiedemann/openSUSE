#
# spec file for package cinnamon-screensaver
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


Name:           cinnamon-screensaver
Version:        5.6.2
Release:        0
Summary:        Cinnamon screensaver and locker
License:        GPL-2.0-or-later
Group:          System/GUI/Other
URL:            https://github.com/linuxmint/cinnamon-screensaver
Source:         https://github.com/linuxmint/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE cinnamon-screensaver-suse-pam.patch -- Use SUSE-specific PAM configuration.
Patch0:         %{name}-suse-pam.patch
BuildRequires:  fdupes
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  meson
BuildRequires:  pam-devel
BuildRequires:  pkgconfig
BuildRequires:  python3 >= 3.4
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(gdk-x11-3.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libxdo)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
Requires:       iso-country-flags-png
Requires:       python3-cairo
Requires:       python3-gobject
Requires:       python3-gobject-Gdk
Requires:       python3-gobject-cairo
Requires:       python3-setproctitle
Requires:       python3-xapp
Recommends:     %{name}-lang
Recommends:     xscreensaver-data
Suggests:       xscreensaver-data-extra

%description
cinnamon-screensaver is a screensaver and locker that aims to have
simple, sane and secure defaults, and be well integrated with the
Cinnamon Desktop.

%prep
%setup -q
%patch0 -p1

%build
%meson
%meson_build

%install
# Manually install desktop file
mkdir -p %{buildroot}%{_datadir}/applications/
cp -r data/org.cinnamon.ScreenSaver.desktop %{buildroot}%{_datadir}/applications/org.cinnamon.ScreenSaver.desktop

%meson_install

# Remove development files as they're not really there to be used.
rm -rf %{buildroot}%{_libdir}/libcscreensaver.so \
  %{buildroot}%{_includedir}/%{name}/                  \
  %{buildroot}%{_libdir}/pkgconfig/cscreensaver.pc     \
  %{buildroot}%{_datadir}/gir-1.0/CScreensaver-1.0.gir

find %{buildroot} -type f -name "*.la" -delete -print
%fdupes %{buildroot}%{_datadir}/
%suse_update_desktop_file org.cinnamon.ScreenSaver

# Fix missing shabang
chmod a-x %{buildroot}%{_datadir}/%{name}/__init__.py
chmod a-x %{buildroot}%{_datadir}/%{name}/*/__init__.py

%post
/sbin/ldconfig
%if 0%{?suse_version} < 1500
%desktop_database_post
%icon_theme_cache_post
%endif

%postun
/sbin/ldconfig
%if 0%{?suse_version} < 1500
%desktop_database_postun
%icon_theme_cache_postun
%endif

%files
%license COPYING*
%doc AUTHORS README.md debian/changelog
%config %{_sysconfdir}/pam.d/cinnamon-screensaver
%{_bindir}/%{name}
%{_bindir}/%{name}-command
%{_libexecdir}/cs-backup-locker
%{_bindir}/cinnamon-unlock-desktop
%{_libexecdir}/%{name}-pam-helper
%{_datadir}/%{name}/
%{_libdir}/libcscreensaver.so*
%{_libdir}/girepository-1.0/CScreensaver-1.0.typelib
%{_datadir}/dbus-1/services/org.cinnamon.ScreenSaver.service
%{_datadir}/applications/org.cinnamon.ScreenSaver.desktop
%{_datadir}/icons/hicolor/*/*/screensaver-*.*
%{_datadir}/icons/hicolor/scalable/apps/csr-backup-locker-icon.svg

%changelog
