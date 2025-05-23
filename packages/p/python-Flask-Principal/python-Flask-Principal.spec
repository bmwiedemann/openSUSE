#
# spec file for package python-Flask-Principal
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


%{?sle15_python_module_pythons}
Name:           python-Flask-Principal
Version:        0.4.0
Release:        0
License:        MIT
Summary:        Identity management for flask
URL:            http://packages.python.org/Flask-Principal/
# Pypi sources don't include tests
#Source:         https://files.pythonhosted.org/packages/source/F/Flask-Principal/Flask-Principal-%%{version}.tar.gz
Source:         https://github.com/mattupstate/flask-principal/archive/%{version}.tar.gz
Source99:       https://raw.githubusercontent.com/mattupstate/flask-principal/master/LICENSE
BuildRequires:  %{python_module importlib-metadata}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# Test requirements
BuildRequires:  %{python_module blinker}
BuildRequires:  %{python_module Flask}
# End of test requirements
Requires:       python-blinker
Requires:       python-Flask
BuildArch:      noarch

%python_subpackages

%description
Flask-Principal provides a very loose framework to tie in providers of
two types of services, often located in different parts of a web application:
Authentication providers and User information providers.

%prep
%setup -q -n flask-principal-%{version}
cp %{SOURCE99} .

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest discover -v

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/flask_principal.py
%pycache_only %{python_sitelib}/__pycache__/flask_principal.*.pyc
%{python_sitelib}/[Ff]lask[_-][Pp]rincipal-%{version}.dist-info

%changelog
