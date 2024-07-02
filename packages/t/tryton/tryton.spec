#
# spec file for package tryton
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2015-2024 Dr. Axel Braun <DocB@opensuse.org>
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

%define majorver 6.0

%if 0%{?suse_version} >= 1550
%define pythons python3
%define mypython python3
%define mysitelib %python3_sitelib
%else
%{?sle15_python_module_pythons}
%define mypython %pythons
%define mysitelib %{expand:%%%{mypython}_sitelib}
%endif


Name:           tryton
Version:        %{majorver}.40
Release:        0
Summary:        The client of the Tryton application platform
License:        GPL-3.0-or-later
Group:          Productivity/Office/Management
URL:            http://www.tryton.org/
Source:         http://downloads.tryton.org/%{majorver}/%{name}-%{version}.tar.gz
## Source1:        http://downloads.tryton.org/%{majorver}/%{name}-%{version}.tar.gz.asc
## Source2:        https://keybase.io/cedrickrier/pgp_keys.asc?fingerprint=7C5A4360F6DF81ABA91FD54D6FF50AFE03489130#/%{name}.keyring

Patch0:         000-pygtkcompat.diff
Patch1:         001-disable-version-check.diff

BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python-rpm-generators
BuildRequires:  %{mypython}-Babel
BuildRequires:  %{mypython}-Sphinx
BuildRequires:  %{mypython}-devel
BuildRequires:  %{mypython}-gobject
BuildRequires:  %{mypython}-python-dateutil
BuildRequires:  %{mypython}-setuptools
BuildRequires:  %{mypython}-simplejson
BuildRequires:  update-desktop-files
BuildRequires:  %{mypython}-pip
BuildRequires:  %{mypython}-wheel

Requires:       %{mypython}-GooCalendar >= 0.7
Requires:       %{mypython}-cairo
Requires:       %{mypython}-chardet
Requires:       %{mypython}-dateutil
Requires:       %{mypython}-gnupg
Requires:       %{mypython}-gobject
Requires:       %{mypython}-gobject-Gdk
Requires:       %{mypython}-gobject-cairo >= 1.15.10
Requires:       %{mypython}-pytz
Requires:       %{mypython}-setuptools
Requires:       %{mypython}-simplejson
Requires:       %{mypython}-xml
BuildArch:      noarch

%description
The client of the Tryton application platform.
A three-tiers  high-level general purpose application platform
written in Python and use Postgresql as database engine.
It is the core base of an Open Source ERP.
It provides modularity, scalability and security.

%prep
%autosetup -p1

#shebag ersetzen
find . -iname "bin/tryton" -exec sed -i "s/env python/%{mypython}/" '{}' \;

%build
%pyproject_wheel

%install
%pyproject_install

# menu-entry
desktop-file-install --dir %{buildroot}%{_datadir}/applications %{name}.desktop
%suse_update_desktop_file %{name}

%python_expand %fdupes %{buildroot}%{mysitelib}

mkdir -p %{buildroot}%{_datadir}/pixmaps
cp %{buildroot}%{mysitelib}/%{name}/data/pixmaps/%{name}/%{name}-icon.png %{buildroot}%{_datadir}/pixmaps/%{name}-icon.png

%files
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%doc COPYRIGHT README.rst CHANGELOG
%license LICENSE
%{_datadir}/pixmaps/*
%{mysitelib}/tryton*

%changelog
