#
# spec file for package lightdm-gtk-greeter-settings
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           lightdm-gtk-greeter-settings
Version:        1.2.2
Release:        0
Summary:        Settings editor for the LightDM GTK+ Greeter
License:        GPL-3.0-or-later
Group:          System/GUI/Other
URL:            https://launchpad.net/lightdm-gtk-greeter-settings
Source:         https://launchpad.net/lightdm-gtk-greeter-settings/1.2/%{version}/+download/lightdm-gtk-greeter-settings-%{version}.tar.gz
BuildRequires:  gobject-introspection
BuildRequires:  hicolor-icon-theme
BuildRequires:  intltool
BuildRequires:  python3
BuildRequires:  python3-distutils-extra
BuildRequires:  python3-gobject-Gdk
BuildRequires:  update-desktop-files
Requires:       lightdm-gtk-greeter >= 2.0
Requires:       python3
Requires:       python3-gobject-Gdk
Recommends:     %{name}-lang
BuildArch:      noarch

%description
A dialog for allowing users to modify the settings of lightdm-gtk-greeter.

%lang_package

%prep
%autosetup
rm -f PKG-INFO

%build
%py3_build

%install
# %%py3_install does not work properly here.
%{__python3} setup.py install --root=%{buildroot} --optimize='1'

# Fix doc directory.
mkdir -p %{buildroot}%{_docdir}/
mv %{buildroot}%{_datadir}/doc/%{name} %{buildroot}%{_docdir}/%{name}

# Remove shebang from files
for lib in %{buildroot}%{python3_sitelib}/lightdm_gtk_greeter_settings/*.py; do
 sed '1{\@^#!/usr/bin/env python@d}' $lib > $lib.new &&
 touch -r $lib $lib.new &&
 mv $lib.new $lib
done

%find_lang %{name}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files
%doc NEWS README
%license COPYING
%{_bindir}/%{name}*
%{python3_sitelib}/lightdm_gtk_greeter_settings-*
%{python3_sitelib}/lightdm_gtk_greeter_settings/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/%{name}/
%{_datadir}/polkit-1/
%{_docdir}/%{name}/

%files lang -f %{name}.lang

%changelog
