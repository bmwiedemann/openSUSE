#
# spec file for package menulibre
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


Name:           menulibre
Version:        2.4.0
Release:        0
Summary:        Desktop menu editor
License:        GPL-3.0-only
Group:          System/GUI/Other
URL:            https://bluesabre.org/projects/menulibre/
Source0:        https://github.com/bluesabre/menulibre/releases/download/%{name}-%{version}/%{name}-%{version}.tar.gz
BuildRequires:  appstream-glib
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  gnome-menus
BuildRequires:  gobject-introspection
BuildRequires:  hicolor-icon-theme
BuildRequires:  intltool
BuildRequires:  pkgconfig(libgnome-menu-3.0)
BuildRequires:  python-rpm-macros
BuildRequires:  python3-distutils-extra
BuildRequires:  python3-gobject-devel
BuildRequires:  python3-pip
BuildRequires:  python3-psutil
BuildRequires:  typelib(Gtk) = 3.0
BuildRequires:  xdg-utils
Requires:       gnome-menus
Requires:       hicolor-icon-theme
Requires:       python3-gobject
Requires:       python3-psutil
Requires:       xdg-utils
BuildArch:      noarch

%description
A desktop menu editor. Budgie, Cinnamon, GNOME, KDE (Plasma), LXDE, LXQt, MATE,
Pantheon, Unity, and Xfce are supported.

%lang_package

%prep
%autosetup

%build
%if 0%{?suse_version} > 1500
%python3_pyproject_wheel
%endif

%install
%if 0%{?suse_version} > 1500
%python3_pyproject_install
%else
%{__python3} setup.py install --root=%{buildroot}
%endif
%fdupes %{buildroot}
%find_lang %{name}

# fix upstream
rm %{buildroot}%{python_sitelib}/uninstall.py
rm -r %{buildroot}%{_datadir}/doc/%{name}
rm -r %{buildroot}%{_datadir}/icons/hicolor/*x*/
rm -r %{buildroot}%{python_sitelib}/__pycache__
sed -i 's|#!/usr/bin/python3||g' %{buildroot}%{python_sitelib}/%{name}/*.py
sed -i 's|#!/usr/bin/python3||g' %{buildroot}%{python_sitelib}/%{name}_lib/*.py

%check
appstream-util validate --nonet %{buildroot}%{_datadir}/metainfo/%{name}.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%license COPYING
%doc AUTHORS NEWS README.md
%{_bindir}/%{name}
%{_bindir}/%{name}-menu-validate
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/metainfo/%{name}.appdata.xml
%{_datadir}/pixmaps/%{name}.png
%{_mandir}/man?/%{name}-menu-validate.?%{?ext_man}
%{_mandir}/man?/%{name}.?%{?ext_man}
%{python_sitelib}/%{name}
%if 0%{?suse_version} > 1500
%{python_sitelib}/%{name}-%{version}.dist-info
%else
%{python_sitelib}/%{name}-%{version}-py%{python_version}.egg-info
%endif
%{python_sitelib}/%{name}_lib

%files lang -f %{name}.lang

%changelog
