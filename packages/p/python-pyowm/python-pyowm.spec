#
# spec file for package python-pyowm
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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

%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-pyowm
Version:        2.10.0
Release:        0
Summary:        A Python wrapper around the OpenWeatherMap web API
License:        MIT
Group:          Development/Languages/Python
URL:            http://github.com/csparpa/pyowm
Source:         https://files.pythonhosted.org/packages/source/p/pyowm/pyowm-%{version}.tar.gz
Source99:       https://raw.githubusercontent.com/csparpa/pyowm/master/LICENSE
BuildRequires:  %{python_module requests >= 2.18.2}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-geojson >= 2.3.0
Requires:       python-requests >= 2.18.2
BuildArch:      noarch
%python_subpackages

%description
PyOWM is a client Python wrapper library for the OpenWeatherMap web API.
It allows quick and easy consumption of OWM weather data from Python
applications via a simple object model and in a human-friendly fashion.

%prep
%setup -q -n pyowm-%{version}
cp %{SOURCE99} .

# Remove shebang line:
sed -i '1d' pyowm/__init__.py

# pyowm/weatherapi25/cityids/__init__.py not null
cp -a pyowm/weatherapi25/__init__.py pyowm/weatherapi25/cityids/

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*

%changelog
