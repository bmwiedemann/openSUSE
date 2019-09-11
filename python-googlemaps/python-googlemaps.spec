#
# spec file for package python-googlemaps
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-googlemaps
Version:        3.0.2
Release:        0
Summary:        Python client library for Google Maps API Web Services
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/googlemaps/google-maps-services-python
Source:         https://files.pythonhosted.org/packages/source/g/googlemaps/googlemaps-%{version}.tar.gz
BuildRequires:  %{python_module nose}
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
%setup -q -n googlemaps-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} nosetests-%{$python_bin_suffix} -v

%files %{python_files}
%license LICENSE
%{python_sitelib}/*

%changelog
