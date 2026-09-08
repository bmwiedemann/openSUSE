#
# spec file for package python-geopy
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/


%{?sle15_python_module_pythons}
Name:           python-geopy
Version:        2.5.0
Release:        0
Summary:        Python Geocoding Toolbox
License:        MIT
URL:            https://github.com/geopy/geopy
Source:         https://github.com/geopy/geopy/archive/%{version}.tar.gz#/geopy-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-geographiclib < 3
Requires:       python-geographiclib >= 1.52
Recommends:     python-pytz
Recommends:     python-xml
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module docutils}
BuildRequires:  %{python_module geographiclib < 3}
BuildRequires:  %{python_module geographiclib >= 1.52}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module pytest >= 3.10}
BuildRequires:  %{python_module pytest-asyncio >= 0.17}
BuildRequires:  %{python_module pytz}
BuildRequires:  %{python_module xml}
# /SECTION
%python_subpackages

%description
Geopy can determine the coordinates of addresses, cities, countries,
and landmarks using third-party geocoders and other data sources such
as wikis.

Geopy currently includes support for six geocoders: Google Maps, Yahoo! Maps, Windows
Local Live (Virtual Earth), geocoder.us, GeoNames, MediaWiki pages (with the GIS
extension), and Semantic MediaWiki pages.

%prep
%autosetup -n geopy-%{version}

%build
export LANG=en_US.UTF-8
%pyproject_wheel

%install
export LANG=en_US.UTF-8
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
# upstream's downstream-facing opt-out: skips every test hitting a live geocoder
%pytest --skip-tests-requiring-internet

%files %{python_files}
%doc AUTHORS README.rst docs/changelog_09x.rst docs/changelog_1xx.rst docs/changelog_2xx.rst
%license LICENSE
%{python_sitelib}/geopy
%{python_sitelib}/geopy-%{version}.dist-info

%changelog
