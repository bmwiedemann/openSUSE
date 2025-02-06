#
# spec file for package cinnamon-screensaver
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


%define         appid org.cinnamon.ScreenSaver
Name:           cinnamon-screensaver
Version:        6.4.0
Release:        0
Summary:        Cinnamon screensaver and locker
License:        GPL-2.0-or-later
URL:            https://github.com/linuxmint/cinnamon-screensaver
Source:         %{url}/archive/%{version}/%{name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE cinnamon-screensaver-suse-pam.patch -- Use SUSE-specific PAM configuration.
Patch0:         %{name}-suse-pam.patch
BuildRequires:  fdupes
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  python3 >= 3.4
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(gdk-x11-3.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libxdo)
%if 0%{?suse_version} >= 1600
BuildRequires:  pkgconfig(pam)
%else
BuildRequires:  pam-devel
%endif
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
Requires:       iso-country-flags-png
Requires:       python3-cairo
Requires:       python3-gobject
Requires:       python3-gobject-Gdk
Requires:       python3-gobject-cairo
Requires:       python3-setproctitle
Requires:       python3-xapp
Recommends:     xscreensaver-data
Suggests:       xscreensaver-data-extra

%description
cinnamon-screensaver is a screensaver and locker that aims to have
simple, sane and secure defaults, and be well integrated with the
Cinnamon Desktop.

%package -n typelib-1_0-CScreensaver-1_0
Summary:        Typelib for %{name}

%description -n typelib-1_0-CScreensaver-1_0
%{summary}.

This package ships the typelib for %{name}.

%package devel
Summary:        Development files for %{name}
Requires:       typelib-1_0-CScreensaver-1_0

%description devel
%{summary}.

Development files for %{name}.

%prep
%autosetup -p1

%build
%meson \
  -Dsetres=false \
  -Dlocking=true \
  -Dxinerama=true \
  -Duse-debian-pam=false \
  -Ddeprecated-warnings=true
%meson_build

%install
%meson_install

%fdupes %{buildroot}

mkdir -p %{buildroot}%{_pam_vendordir}
mv %{buildroot}%{_sysconfdir}/pam.d/%{name} %{buildroot}%{_pam_vendordir}/%{name}
mkdir -p %{buildroot}%{_libdir}/girepository-1.0
mv %{buildroot}%{_libexecdir}/%{name}/girepository-1.0/CScreensaver-1.0.typelib \
   %{buildroot}%{_libdir}/girepository-1.0/
rm -rf %{buildroot}%{_libexecdir}/%{name}/girepository-1.0

# Fix missing shabang
chmod a+x %{buildroot}%{_datadir}/%{name}/*.py
chmod a+x %{buildroot}%{_datadir}/%{name}/*/*.py

# remove the executable bit for these files (above we add it, out of convenience)
chmod a-x %{buildroot}%{_datadir}/%{name}/{__init__.py,config.py,dbusdepot/__init__.py,util/__init__.py,widgets/__init__.py}

%pre
# Prepare for migration to /usr/lib; save any old .rpmsave
for i in pam.d/cinnamon-screensaver ; do
     test -f %{_sysconfdir}/${i}.rpmsave && mv -v %{_sysconfdir}/${i}.rpmsave %{_sysconfdir}/${i}.rpmsave.old ||:
done

%posttrans
# Migration to /usr/lib, restore just created .rpmsave
for i in pam.d/cinnamon-screensaver ; do
     test -f %{_sysconfdir}/${i}.rpmsave && mv -v %{_sysconfdir}/${i}.rpmsave %{_sysconfdir}/${i} ||:
done

%files
%license COPYING COPYING.LIB
%doc AUTHORS README.md HACKING
%dir %{_libexecdir}/%{name}
%{_bindir}/{%{name}{,-command},cinnamon-unlock-desktop}
%{_datadir}/applications/%{appid}.desktop
%{_libexecdir}/%{name}/{%{name}-pam-helper,cs-backup-locker,libcscreensaver.so}
%{_datadir}/%{name}
%{_datadir}/dbus-1/services/%{appid}.service
%{_datadir}/icons/hicolor/scalable/{actions,apps,status}/*.svg
%{_pam_vendordir}/%{name}

%files -n typelib-1_0-CScreensaver-1_0
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/CScreensaver-1.0.typelib

%files devel
%{_datadir}/gir-1.0/CScreensaver-1.0.gir

%changelog
