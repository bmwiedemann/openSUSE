#
# spec file for package python-crispy-bootstrap3
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


Name:           python-crispy-bootstrap3
Version:        2024.1
Release:        0
Summary:        Bootstrap3 template pack for django-crispy-forms
License:        MIT
URL:            https://github.com/django-crispy-forms/crispy-bootstrap3
Source:         https://files.pythonhosted.org/packages/source/c/crispy-bootstrap3/crispy-bootstrap3-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 61.0}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module Django >= 3.2}
BuildRequires:  %{python_module django-crispy-forms >= 1.14.0}
BuildRequires:  %{python_module pytest-django}
BuildRequires:  %{python_module pytest}
# /SECTION
BuildRequires:  fdupes
Requires:       python-Django >= 3.2
Requires:       python-django-crispy-forms >= 1.14.0
BuildArch:      noarch
%python_subpackages

%description
Bootstrap3 template pack for django-crispy-forms

%prep
%autosetup -p1 -n crispy-bootstrap3-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export DJANGO_SETTINGS_MODULE=tests.test_settings
export PYTHONPATH=$PWD
%pytest

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE
%{python_sitelib}/crispy_bootstrap3
%{python_sitelib}/crispy_bootstrap3-%{version}.dist-info

%changelog
