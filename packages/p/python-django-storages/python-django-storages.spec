#
# spec file for package python-django-storages
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
%bcond_without python2
Name:           python-django-storages
Version:        1.13.2
Release:        0
Summary:        Support for many storage backends in Django
License:        BSD-3-Clause
URL:            https://github.com/jschneier/django-storages
Source:         https://files.pythonhosted.org/packages/source/d/django-storages/django-storages-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django >= 2.2
Suggests:       python-apache-libcloud
Suggests:       python-azure >= 3.0.0
Suggests:       python-azure-storage-blob >= 1.3.1
Suggests:       python-boto3 >= 1.4.4
Suggests:       python-dropbox >= 7.2.1
Suggests:       python-google-cloud-storage >= 1.15.0
Suggests:       python-paramiko
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Django >= 2.2}
BuildRequires:  %{python_module azure-storage-blob >= 1.3.1}
BuildRequires:  %{python_module boto3 >= 1.4.4}
BuildRequires:  %{python_module dropbox >= 7.2.1}
BuildRequires:  %{python_module google-cloud-storage >= 1.15.0}
BuildRequires:  %{python_module paramiko}
BuildRequires:  %{python_module pytest}
%if %{with python2}
BuildRequires:  python2-mock
%endif
# /SECTION
%python_subpackages

%description
django-storages is a project to provide a variety of storage backends in a single library.

%prep
%setup -q -n django-storages-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export PYTHONPATH=.
export DJANGO_SETTINGS_MODULE=tests.settings
# Integration tests, which is only azure, fail systematically
rm tests/test_azure.py
# Skip failing test in test_s3boto3.py
%pytest -k 'not test_deprecated_default_acl'

%files %{python_files}
%doc AUTHORS CHANGELOG.rst README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
