#
# spec file for package secrets
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


%global         flavor @BUILD_FLAVOR@%nil
%if "%{flavor}" == "test"
%define         psuffix -test
%else
%define         psuffix %nil
%endif
Name:           secrets%{psuffix}
Version:        9.5
Release:        0
Summary:        A password manager for GNOME
License:        GPL-3.0-or-later
URL:            https://gitlab.gnome.org/World/secrets
Source0:        secrets-%{version}.tar.zst
Patch0:         fix-test.patch
BuildRequires:  appstream-glib
BuildRequires:  desktop-file-utils
BuildRequires:  meson >= 0.51.0
BuildRequires:  pkgconfig
BuildRequires:  python3-PyKCS11
BuildRequires:  python3-base >= 3.7.0
BuildRequires:  python3-gobject
BuildRequires:  python3-gobject-Gdk
BuildRequires:  python3-pykeepass >= 4.0.7.post1
BuildRequires:  python3-pyotp >= 2.4.0
BuildRequires:  python3-pytest
BuildRequires:  python3-python-yubico
BuildRequires:  python3-validators
BuildRequires:  python3-zxcvbn
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.66.0
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk4) >= 4.5.0
BuildRequires:  pkgconfig(libadwaita-1)

Requires:       opensc
Requires:       python3-PyKCS11
Requires:       python3-argon2-cffi
Requires:       python3-gobject-Gdk
Requires:       python3-lxml
Requires:       python3-pycryptodome
Requires:       python3-pykeepass
Requires:       python3-pyotp
Requires:       python3-python-yubico
Requires:       python3-pyusb
Requires:       python3-validators
Requires:       python3-zxcvbn

Obsoletes:      gnome-passwordsafe < 6.1
Provides:       gnome-passwordsafe = %{version}

%if "%{flavor}" == "test"
BuildRequires:  secrets = %{version}
%endif

BuildArch:      noarch

%description
Secrets is a password manager which makes use of the Keepass v.4
format.
It integrates with the GNOME desktop and provides an interface for
the management of password databases.

%lang_package

%prep
%autosetup -p1 -n secrets-%{version}
# Fix shebang to be py3, not env set
sed -i -e '1{s,^#!/usr/bin/env python3,#!%{_bindir}/python3,}' gsecrets/utils.py
# Drop shebang all the way
sed -i -e '1{s,^#!@PYTHON@,,}' gsecrets/const.py.in

%build
%meson
%meson_build

%if "%{flavor}" != "test"
%install
%meson_install
# Explicitly create the pycache/.pyc files, not relying on the
# generation done by meson. Should make the package reproducible.
%py3_compile %{buildroot}%{python3_sitelib}/gsecrets
%find_lang secrets %{?no_lang_C}
%suse_update_desktop_file org.gnome.World.Secrets
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.xml
glib-compile-schemas --strict --dry-run %{buildroot}%{_datadir}/glib-2.0/schemas/
%endif

%if "%{flavor}" == "test"
%check
pytest
%endif

%if "%{flavor}" != "test"
%files
%license LICENSE
%doc README.md
%{_bindir}/secrets
%{python3_sitelib}/gsecrets/
%{_datadir}/applications/org.gnome.World.Secrets.desktop
%dir %{_datadir}/secrets
%{_datadir}/%{name}/resources.gresource
%{_datadir}/glib-2.0/schemas/org.gnome.World.Secrets.gschema.xml
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.World.Secrets-symbolic.svg
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.World.Secrets.svg
%{_datadir}/metainfo/org.gnome.World.Secrets.metainfo.xml
%{_datadir}/mime/packages/org.gnome.World.Secrets.xml

%files lang -f secrets.lang
%endif

%changelog
