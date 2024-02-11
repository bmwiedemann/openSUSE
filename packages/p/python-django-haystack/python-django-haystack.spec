#
# spec file for package python-django-haystack
#
# Copyright (c) 2024 SUSE LLC
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
# pkg_resources is broken since the flufl.lock update in Factory
# https://github.com/django-haystack/django-haystack/pull/1935
Patch:          gh-pr-1935_importlib.patch
# PATCH-FIX-UPSTREAM https://github.com/django-haystack/django-haystack/commit/3a566a50e4963bed4fb8853eca60bc894b0b7fc5 Fix unittest assert calls for Python 3.12
Patch:          unittest312.patch
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django >= 2.2
Requires:       python-packaging
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
%autosetup -n django-haystack-%{version} -p1
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
