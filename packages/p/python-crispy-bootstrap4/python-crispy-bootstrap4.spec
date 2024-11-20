#
# spec file for package python-crispy-bootstrap4
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
Name:           python-crispy-bootstrap4
Version:        2024.10
Release:        0
Summary:        Bootstrap4 template pack for django-crispy-forms
License:        MIT
URL:            https://github.com/django-crispy-forms/crispy-bootstrap4
Source:         https://github.com/django-crispy-forms/crispy-bootstrap4/archive/refs/tags/%{version}.tar.gz#/crispy-bootstrap4-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module Django >= 4.2}
BuildRequires:  %{python_module django-crispy-forms >= 2.3}
BuildRequires:  %{python_module pytest-django}
BuildRequires:  %{python_module pytest}
# /SECTION
BuildRequires:  fdupes
Requires:       python-Django >= 4.2
Requires:       python-django-crispy-forms >= 2.3
BuildArch:      noarch
%python_subpackages

%description
Bootstrap4 template pack for django-crispy-forms

%prep
%autosetup -p1 -n crispy-bootstrap4-%{version}

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
%doc README.md
%license LICENSE
%{python_sitelib}/crispy_bootstrap4
%{python_sitelib}/crispy_bootstrap4-%{version}.dist-info

%changelog
