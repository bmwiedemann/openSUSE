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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-geopy
Version:        1.18.1
Release:        0
License:        MIT
Summary:        Python Geocoding Toolbox
Url:            https://github.com/geopy/geopy
Group:          Development/Languages/Python
Source:         https://github.com/geopy/geopy/archive/%{version}.tar.gz#/geopy-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
# SECTION test requirements
BuildRequires:  %{python_module geographiclib >= 1.49}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pytest >= 3.10}
BuildRequires:  %{python_module pytz}
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module xml}
BuildRequires:  (python2-contextlib2 if python)
BuildRequires:  (python2-statistics if python)
# /SECTION
BuildRequires:  fdupes
Requires:       python-geographiclib >= 1.49
Requires:       python-six
Recommends:     python-pytz
Recommends:     python-xml
%ifpython2
Requires:       python-statistics
%endif
BuildArch:      noarch

%python_subpackages

%description
Geopy can determine the coordinates of addresses, cities, countries,
and landmarks using third-party geocoders and other data sources such
as wikis.
 
Geopy currently includes support for six geocoders: Google Maps, Yahoo! Maps, Windows
Local Live (Virtual Earth), geocoder.us, GeoNames, MediaWiki pages (with the GIS
extension), and Semantic MediaWiki pages.

%prep
%setup -q -n geopy-%{version}

# Proxy to live service will not work, resulting in unexpected exceptions
# that do not match test cases
rm test/test_proxy.py

# Online services are not available
rm \
  test/geocoders/arcgis.py \
  test/geocoders/banfrance.py \
  test/geocoders/databc.py \
  test/geocoders/geocodefarm.py \
  test/geocoders/geonames.py \
  test/geocoders/googlev3.py \
  test/geocoders/nominatim.py \
  test/geocoders/openmapquest.py \
  test/geocoders/photon.py \
  test/geocoders/pickpoint.py \
  test/geocoders/yandex.py

%build
export LANG=en_US.UTF-8
%python_build

%install
export LANG=en_US.UTF-8
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
%python_exec setup.py test

%files %{python_files}
%doc AUTHORS README.rst docs/changelog_09x.rst docs/changelog_1xx.rst
%license LICENSE
%{python_sitelib}/*

%changelog
