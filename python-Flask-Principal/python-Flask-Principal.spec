#
# spec file for package python-Flask-Principal
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-Flask-Principal
Version:        0.4.0
Release:        0
License:        MIT
Summary:        Identity management for flask
Url:            http://packages.python.org/Flask-Principal/
Group:          Development/Languages/Python
# Pypi sources don't include tests
#Source:         https://files.pythonhosted.org/packages/source/F/Flask-Principal/Flask-Principal-%%{version}.tar.gz
Source:         https://github.com/mattupstate/flask-principal/archive/%{version}.tar.gz
Source99:       https://raw.githubusercontent.com/mattupstate/flask-principal/master/LICENSE
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
# Test requirements
BuildRequires:  %{python_module blinker}
BuildRequires:  %{python_module Flask}
BuildRequires:  %{python_module nose}
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
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
