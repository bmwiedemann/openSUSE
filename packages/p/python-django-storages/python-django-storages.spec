#
# spec file for package python-django-storages
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
Name:           python-django-storages
Version:        1.14.4
Release:        0
Summary:        Support for many storage backends in Django
License:        BSD-3-Clause
URL:            https://github.com/jschneier/django-storages
Source:         https://files.pythonhosted.org/packages/source/d/django-storages/django-storages-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django >= 3.2
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Django >= 3.2}
BuildRequires:  %{python_module azure-storage-blob >= 12}
BuildRequires:  %{python_module boto3 >= 1.4.4}
BuildRequires:  %{python_module dropbox >= 7.2.1}
BuildRequires:  %{python_module google-cloud-storage >= 1.27}
BuildRequires:  %{python_module paramiko >= 1.15}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
django-storages is a project to provide a variety of storage backends in a single library.

%prep
%setup -q -n django-storages-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export PYTHONPATH=.
export DJANGO_SETTINGS_MODULE=tests.settings
# Integration tests, which is only azure, fail systematically
rm tests/test_azure.py tests/test_s3.py
# Skip failing test in test_s3boto3.py
%pytest -k 'not test_deprecated_default_acl and not test_with_string_file_detect_encoding'

%files %{python_files}
%doc CHANGELOG.rst README.rst
%license LICENSE
%{python_sitelib}/storages
%{python_sitelib}/django_storages-%{version}.dist-info

%changelog
