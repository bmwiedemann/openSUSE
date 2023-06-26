#
# spec file for package python-django-haystack
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


%{?sle15_python_module_pythons}
Name:           python-django-haystack
Version:        3.2.1
Release:        0
Summary:        Pluggable search for Django
License:        BSD-3-Clause
URL:            https://github.com/django-haystack/django-haystack
Source:         https://files.pythonhosted.org/packages/source/d/django-haystack/django-haystack-%{version}.tar.gz
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django >= 2.2
Suggests:       python-elasticsearch
Suggests:       python-pysolr >= 3.7.0
Suggests:       python-Whoosh >= 2.5.4
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Django >= 2.2}
BuildRequires:  %{python_module Whoosh >= 2.5.4}
BuildRequires:  %{python_module elasticsearch}
BuildRequires:  %{python_module geopy >= 2.0.0}
BuildRequires:  %{python_module pysolr >= 3.7.0}
BuildRequires:  %{python_module pytest-django}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-dateutil}
BuildRequires:  %{python_module requests}
BuildRequires:  python3-GDAL
# /SECTION
%python_subpackages

%description
Pluggable search for Django.

%prep
%setup -q -n django-haystack-%{version}
sed -i 's:==:>=:' setup.py

# This causes errors with pytest
sed -i '/django.setup()/d' test_haystack/__init__.py
echo 'import django; django.setup()' > conftest.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export DJANGO_SETTINGS_MODULE=test_haystack.settings
# elasticsearch and solr tests require running services
# test_ensure_wgs84 is broken with some GDAL issues
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitelib}:${PWD}
$python -m pytest -rs -k 'not (elasticsearch or solr or test_ensure_wgs84)'
}

%files %{python_files}
%doc AUTHORS README.rst
%license LICENSE
%{python_sitelib}/*haystack*/

%changelog
