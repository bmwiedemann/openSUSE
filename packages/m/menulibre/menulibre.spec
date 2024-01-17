#
# spec file for package menulibre
#
# Copyright (c) 2021 SUSE LLC
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

Name:           menulibre
Version:        2.2.3
Release:        0
Summary:        Desktop menu editor
License:        GPL-3.0-only
Group:          System/GUI/Other
URL:            https://bluesabre.org/projects/menulibre/
Source:         https://github.com/bluesabre/menulibre/releases/download/%{name}-%{version}/%{name}-%{version}.tar.gz
BuildRequires:  appstream-glib
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  gnome-menus
BuildRequires:  gobject-introspection
BuildRequires:  hicolor-icon-theme
BuildRequires:  intltool
BuildRequires:  python3
BuildRequires:  python3-base
BuildRequires:  python3-distutils-extra
BuildRequires:  python3-gobject
BuildRequires:  python3-psutil
BuildRequires:  update-desktop-files
BuildRequires:  xdg-utils
BuildRequires:  typelib(Gtk) = 3.0
Requires:       gnome-menus
Requires:       hicolor-icon-theme
Requires:       python3
Requires:       python3-gobject
Requires:       python3-psutil
Requires:       xdg-utils
Recommends:     %{name}-lang
BuildArch:      noarch

%description
A desktop menu editor. Budgie, Cinnamon, GNOME, KDE (Plasma), LXDE, LXQt, MATE,
Pantheon, Unity, and Xfce are supported.

%lang_package

%prep
%autosetup

%build

%install
%{__python3} setup.py install --root=%{buildroot}

# Remove hashbang line from non-executable library files
for lib in %{buildroot}%{python3_sitelib}/menulibre{,_lib}/*.py; do
    sed '1{\@^#!/usr/bin/python3@d}' $lib > $lib.new &&
    touch -r $lib $lib.new &&
    mv $lib.new $lib
done

# Fix name issue in menulibre.desktop with Budgie and Pantheon
desktop-file-edit %{buildroot}%{_datadir}/applications/%{name}.desktop --remove-only-show-in="Pantheon" \
  --remove-only-show-in="Budgie"
desktop-file-edit %{buildroot}%{_datadir}/applications/%{name}.desktop --add-only-show-in="X-Pantheon" \
  --add-only-show-in="X-Budgie"

# Fix python-bytecode-inconsistent-mtime.
pushd %{buildroot}%{python3_sitelib}/%{name}_lib
%py3_compile .
popd

# Fix duplicate doc folder
rm -rf %{buildroot}%{_datadir}/doc

# Fix duplicate icon
%fdupes %{buildroot}%{_datadir}/icons/hicolor/

desktop-file-validate %{buildroot}/%{_datadir}/applications/menulibre.desktop

rm -f %{buildroot}%{_datadir}/menulibre/metainfo/menulibre.appdata.xml.in
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.xml

%find_lang %{name}

%files -f %{name}.lang

%files
%license COPYING
%doc AUTHORS NEWS README.md
%{_bindir}/%{name}*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.svg
%{_datadir}/metainfo/%{name}.appdata.xml
%{_datadir}/pixmaps/%{name}.png
%{_mandir}/man?/%{name}*.?%{ext_man}
%{python3_sitelib}/%{name}-%{version}-py%{py3_ver}.egg-info
%{python3_sitelib}/%{name}/
%{python3_sitelib}/%{name}_lib/
%dir %{_datadir}/%{name}/
%dir %{_datadir}/%{name}/ui/
%{_datadir}/%{name}/ui/*.ui

%changelog
