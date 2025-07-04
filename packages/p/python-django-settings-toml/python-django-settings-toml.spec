#
# spec file for package python-django-settings-toml
#
# Copyright (c) 2025 SUSE LLC
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
%{?sle15_python_module_pythons}
Name:           python-django-settings-toml
Version:        0.0.4
Release:        0
Summary:        Django settings using TOML configuration files
License:        Apache-2.0
URL:            https://github.com/maxking/django-settings-toml
Source:         https://files.pythonhosted.org/packages/source/d/django-settings-toml/django-settings-toml-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-toml
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module toml}
# /SECTION
%python_subpackages

%description
Django settings using TOML configuration files.

%prep
%setup -q -n django-settings-toml-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/django_settings_toml.py
%pycache_only %{python_sitelib}/__pycache__/django_settings_toml*.pyc
%{python_sitelib}/django_settings_toml-%{version}.dist-info

%changelog
