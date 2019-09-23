#
# spec file for package tryton
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2015-2018 Dr. Axel Braun
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


%define majorver 4.6
Name:           tryton
Version:        %{majorver}.23
Release:        0
Summary:        The client of the Tryton application platform
License:        GPL-3.0-only
Group:          Productivity/Office/Management
Url:            http://www.tryton.org/
Source:         http://downloads.tryton.org/%{majorver}/%{name}-%{version}.tar.gz
Source1:        ftp://ftp.gnu.org/gnu/health/plugins/gnuhealth-camera-plugin-latest.tar.gz
Patch0:         tryton_crypto.patch
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  python-Babel
BuildRequires:  python-Sphinx
# List of additional build dependencies
BuildRequires:  python-devel
BuildRequires:  python-gtk
BuildRequires:  python-python-dateutil
BuildRequires:  python-setuptools
BuildRequires:  python-simplejson
BuildRequires:  update-desktop-files
Requires:       librsvg
#for the plugins:
Requires:       opencv
Requires:       python-cdecimal
Requires:       python-chardet
Requires:       python-dateutil
Requires:       python-gnupg
Requires:       python-gtk
Requires:       python-opencv
Requires:       python-pytz
Requires:       python-setuptools
Requires:       python-simplejson
Requires:       python-xml
Requires:       python2-GooCalendar
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
pwd
cd %{name}/plugins/
tar --strip-components 1 -xzvf %{SOURCE1}

%build
:

%install

python setup.py install --prefix=%{_prefix} --root=%{buildroot}

# menu-entry
desktop-file-install --dir %{buildroot}%{_datadir}/applications %{name}.desktop
%suse_update_desktop_file %{name}

%python_expand %fdupes %{buildroot}%{_datadir}
%python_expand %fdupes %{buildroot}%{_prefix}/lib

mkdir -p %{buildroot}%{_datadir}/pixmaps
cp %{buildroot}%{python_sitelib}/%{name}/data/pixmaps/%{name}/%{name}-icon.png %{buildroot}%{_datadir}/pixmaps/%{name}-icon.png

%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun

%files
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%doc README CHANGELOG
%license LICENSE COPYRIGHT
%{_datadir}/pixmaps/*
%{python_sitelib}/*

%changelog
