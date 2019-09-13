#
# spec file for package python-django-storages
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
Name:           python-django-storages
Version:        1.7.1
Release:        0
Summary:        Support for many storage backends in Django
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/jschneier/django-storages
Source:         https://files.pythonhosted.org/packages/source/d/django-storages/django-storages-%{version}.tar.gz
Patch0:         e9bb4bcb8a1b7720468add08bc8343ffbaa0165c.patch
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django >= 1.11
Suggests:       python-apache-libcloud
Suggests:       python-azure >= 3.0.0
Suggests:       python-azure-storage-blob >= 1.3.1
Suggests:       python-boto >= 2.32.0
Suggests:       python-boto3 >= 1.4.4
Suggests:       python-dropbox >= 7.2.1
Suggests:       python-google-cloud-storage >= 0.22.0
Suggests:       python-paramiko
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Django >= 1.11}
BuildRequires:  %{python_module azure-storage-blob}
BuildRequires:  %{python_module boto3}
BuildRequires:  %{python_module boto}
BuildRequires:  %{python_module dropbox}
BuildRequires:  %{python_module google-cloud-storage}
BuildRequires:  %{python_module paramiko}
BuildRequires:  python2-mock
# /SECTION
%python_subpackages

%description
Support for many storage backends in Django

%prep
%setup -q -n django-storages-%{version}
%patch0 -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export PYTHONPATH=.
export DJANGO_SETTINGS_MODULE=tests.settings
# Integration tests, which is only azure, fail systematically
rm -r tests/integration
# Skip two tests in test_s3boto3.py
%python_exec -m nose -e 'test_deprecated_(acl|bucket)'

%files %{python_files}
%doc AUTHORS CHANGELOG.rst README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
