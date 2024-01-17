#
# spec file for package python-googlemaps
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


%define skip_python2 1
Name:           python-googlemaps
Version:        4.7.3
Release:        0
Summary:        Python client library for Google Maps API Web Services
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/googlemaps/google-maps-services-python
Source:         https://github.com/googlemaps/google-maps-services-python/archive/v%{version}.tar.gz#/googlemaps-%{version}.tar.gz
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests >= 2.20.0}
BuildRequires:  %{python_module responses >= 0.3}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-requests >= 2.20.0
BuildArch:      noarch
%python_subpackages

%description
Geocoding, reverse geocoding, driving directions, and local search in
Python via Google.

%prep
%setup -q -n google-maps-services-python-%{version}
# do not require coverage
sed -i 's/--cov.*$//' setup.cfg

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# the tests catch ApiError, which means they have to connect to the actual GoogleMaps (and they get no internet for it)
%pytest -k "not (test_elevation_along_path_single or test_transit_without_time)"

%files %{python_files}
%license LICENSE
%doc README.md CHANGELOG.md
%{python_sitelib}/googlemaps*

%changelog
