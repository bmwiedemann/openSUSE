#
# spec file for package tryton
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2015-2022 Dr. Axel Braun <DocB@opensuse.org>
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
Name:           tryton
Version:        %{majorver}.22
Release:        0
Summary:        The client of the Tryton application platform
License:        GPL-3.0-or-later
Group:          Productivity/Office/Management
URL:            http://www.tryton.org/
Source:         http://downloads.tryton.org/%{majorver}/%{name}-%{version}.tar.gz
Source1:        https://keybase.io/cedrickrier/pgp_keys.asc?fingerprint=7C5A4360F6DF81ABA91FD54D6FF50AFE03489130#/%{name}.keyring

Patch0:         000-pygtkcompat.diff
Patch1:         001-disable-version-check.diff
BuildRequires:  fdupes
BuildRequires:  python3-Babel
BuildRequires:  python3-Sphinx
BuildRequires:  python3-devel
BuildRequires:  python3-gobject
BuildRequires:  python3-python-dateutil
BuildRequires:  python3-setuptools
BuildRequires:  python3-simplejson
BuildRequires:  update-desktop-files

Requires:       python3-GooCalendar >= 0.7
Requires:       python3-cairo
Requires:       python3-chardet
Requires:       python3-dateutil
Requires:       python3-gnupg
Requires:       python3-gobject
Requires:       python3-gobject-Gdk
Requires:       python3-gobject-cairo >= 1.15.10
Requires:       python3-pytz
Requires:       python3-setuptools
Requires:       python3-simplejson
Requires:       python3-xml
BuildArch:      noarch

%description
The client of the Tryton application platform.
A three-tiers  high-level general purpose application platform
written in Python and use Postgresql as database engine.
It is the core base of an Open Source ERP.
It provides modularity, scalability and security.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%python3_build

%install
%python3_install

# menu-entry
desktop-file-install --dir %{buildroot}%{_datadir}/applications %{name}.desktop
%suse_update_desktop_file %{name}

%python_expand %fdupes %{buildroot}%{python3_sitelib}

mkdir -p %{buildroot}%{_datadir}/pixmaps
cp %{buildroot}%{python3_sitelib}/%{name}/data/pixmaps/%{name}/%{name}-icon.png %{buildroot}%{_datadir}/pixmaps/%{name}-icon.png

%files
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%doc COPYRIGHT README.rst CHANGELOG
%license LICENSE
%{_datadir}/pixmaps/*
%{python3_sitelib}/*

%changelog
