#
# spec file for package python-pegen
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


Name:           python-pegen
Version:        0.3.0
Release:        0
Summary:        CPython's PEG parser generator
License:        MIT
URL:            https://github.com/we-like-parsers/pegen
Source:         https://files.pythonhosted.org/packages/source/p/pegen/pegen-%{version}.tar.gz
# PATCH-FIX-UPSTREAM gh#we-like-parsers/pegen#104
Patch0:         support-python-313.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module testsuite}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Suggests:       python-sphinx
Suggests:       python-sphinx-copybutton
Suggests:       python-furo
Suggests:       python-black
Suggests:       python-flake8
Suggests:       python-mypy
Suggests:       python-psutil
Suggests:       python-pytest
Suggests:       python-pytest-cov
Suggests:       python-flask
Suggests:       python-flask-wtf
BuildArch:      noarch
%python_subpackages

%description
CPython's PEG parser generator

%prep
%autosetup -p1 -n pegen-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Broken with Python 3.12
%pytest -k 'not test_invalid_call_arguments'

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/pegen
%{python_sitelib}/pegen-%{version}.dist-info

%changelog
