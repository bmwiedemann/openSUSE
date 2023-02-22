#
# spec file for package secrets
#
# Copyright (c) 2023 SUSE LLC
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


Name:           secrets
Version:        7.2
Release:        0
Summary:        A password manager for GNOME
License:        GPL-3.0-or-later
URL:            https://gitlab.gnome.org/World/secrets
Source0:        %{name}-%{version}.tar.xz

BuildRequires:  appstream-glib
BuildRequires:  desktop-file-utils
BuildRequires:  meson >= 0.51.0
BuildRequires:  pkgconfig
BuildRequires:  python3-base >= 3.7.0
BuildRequires:  python3-gobject
BuildRequires:  python3-gobject-Gdk
BuildRequires:  python3-pykeepass >= 4.0.3
BuildRequires:  python3-pyotp >= 2.4.0
BuildRequires:  python3-pytest
BuildRequires:  python3-validators
BuildRequires:  python3-zxcvbn
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.66.0
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk4) >= 4.5.0
BuildRequires:  pkgconfig(libadwaita-1)

Requires:       python3-argon2-cffi
Requires:       python3-gobject-Gdk
Requires:       python3-lxml
Requires:       python3-pycryptodome
Requires:       python3-pykeepass
Requires:       python3-pyotp
Requires:       python3-validators
Requires:       python3-zxcvbn

Obsoletes:      gnome-passwordsafe < 6.1
Provides:       gnome-passwordsafe = %{version}

BuildArch:      noarch

%description
Secrets is a password manager which makes use of the Keepass v.4
format.
It integrates with the GNOME desktop and provides an interface for
the management of password databases.

%lang_package

%prep
%autosetup -p1
# Fix shebang to be py3, not env set
sed -i -e '1{s,^#!/usr/bin/env python3,#!%{_bindir}/python3,}' gsecrets/utils.py
# Drop shebang all the way
sed -i -e '1{s,^#!@PYTHON@,,}' gsecrets/const.py.in

%build
%meson \
	-D tests=true \
	%{nil}
%meson_build

%install
%meson_install
%find_lang %{name} %{?no_lang_C}

%check
# Disable meson_test for now, fails without BuildRequires itself to complete
# Run the 3 first tests manually
#%%meson_test
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
glib-compile-schemas --strict --dry-run %{buildroot}%{_datadir}/glib-2.0/schemas/
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.xml

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{python3_sitelib}/g%{name}/
%{_datadir}/applications/org.gnome.World.Secrets.desktop
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/resources.gresource
%{_datadir}/glib-2.0/schemas/org.gnome.World.Secrets.gschema.xml
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.World.Secrets-symbolic.svg
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.World.Secrets.svg
%{_datadir}/metainfo/org.gnome.World.Secrets.metainfo.xml
%{_datadir}/mime/packages/org.gnome.World.Secrets.xml

%files lang -f %{name}.lang

%changelog
