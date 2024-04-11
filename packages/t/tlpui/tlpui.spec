#
# spec file for package tlpui
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


%define pythons python3
Name:           tlpui
Version:        1.6.5
Release:        0
Summary:        A GTK user interface for TLP
License:        GPL-2.0-or-later AND CC-BY-SA-4.0
URL:            https://github.com/d4nj1/TLPUI
Source0:        %{url}/archive/refs/tags/%{name}-%{version}.tar.gz
Source2:        %{name}.rpmlintrc
BuildRequires:  update-desktop-files
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  polkit
BuildRequires:  python3
BuildRequires:  python3-pip
BuildRequires:  python3-poetry
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel
Requires:       python3-gobject
Requires:       python3-gobject-Gdk
Requires:       python3-PyYAML
Requires:       tlp
BuildArch:      noarch

%description
TLPUI is a GTK user interface for TLP written in Python. The Python scripts in
this project generate a GTK-UI to change TLP configuration files easily. It has
the aim to protect users from setting bad configuration and to deliver a basic
overview of all the valid configuration values.

%prep
%autosetup -n TLPUI-%{name}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install

sed -i "1{/^#!\/usr\/bin\/env python3/d}" %{buildroot}%{python3_sitelib}/%{name}/__main__.py
chmod -x %{buildroot}%{python3_sitelib}/%{name}/__main__.py

# Link app icon to hicolor icon dir
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/scalable/apps
ln -s %{python3_sitelib}/%{name}/icons/themeable/hicolor/scalable/apps/tlpui.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/

# Install desktop file
%suse_update_desktop_file -i tlpui

%fdupes %{buildroot}%{python3_sitelib}/%{name}/

%check

%files
%license COPYING.md LICENSE.md
%doc README.md
%{_bindir}/*
%{_datadir}/icons/hicolor/scalable/apps/*.svg
%{_datadir}/applications/*.desktop
%{python3_sitelib}/%{name}/
%{python3_sitelib}/tlp_ui-%{version}*.*-info/

%changelog
