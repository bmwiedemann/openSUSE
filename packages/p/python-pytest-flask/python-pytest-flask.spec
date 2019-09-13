#
# spec file for package python-pytest-flask
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-pytest-flask
Version:        0.15.0
Release:        0
License:        MIT
Summary:        A set of py.test fixtures to test Flask applications
Url:            https://github.com/pytest-dev/pytest-flask
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/p/pytest-flask/pytest-flask-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  fdupes
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module Flask}
BuildRequires:  %{python_module pytest >= 3.6}
BuildRequires:  %{python_module Werkzeug >= 0.7}
Requires:       python-Flask
Requires:       python-pytest >= 3.6
Requires:       python-Werkzeug >= 0.7
BuildArch:      noarch

%python_subpackages

%description
An extension of pytest test runner which provides a set of useful tools
to simplify testing and development of the Flask extensions and applications.

%prep
%setup -q -n pytest-flask-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}/pytest_flask

%check
%pytest --ignore tests/test_live_server.py

%files %{python_files}
%defattr(-,root,root,-)
%license LICENSE
%doc README.rst
%{python_sitelib}/*

%changelog

