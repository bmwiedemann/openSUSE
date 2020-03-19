#
# spec file for package python-pytest-flask
#
# Copyright (c) 2020 SUSE LLC
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
Name:           python-pytest-flask
Version:        1.0.0
Release:        0
Summary:        A set of py.test fixtures to test Flask applications
License:        MIT
URL:            https://github.com/pytest-dev/pytest-flask
Source:         https://files.pythonhosted.org/packages/source/p/pytest-flask/pytest-flask-%{version}.tar.gz
BuildRequires:  %{python_module Flask}
BuildRequires:  %{python_module Werkzeug >= 0.7}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pytest >= 5.2}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Flask
Requires:       python-Werkzeug >= 0.7
Requires:       python-pytest >= 5.2
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
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest --ignore tests/test_live_server.py

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/*

%changelog
