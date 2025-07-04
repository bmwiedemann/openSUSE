#
# spec file for package python-whichcraft
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
Name:           python-whichcraft
Version:        0.6.1
Release:        0
Summary:        Cross-python shutil.which functionality
License:        BSD-3-Clause
URL:            https://github.com/pydanny/whichcraft
Source:         https://files.pythonhosted.org/packages/source/w/whichcraft/whichcraft-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
This is a shim for the "shutil.which" function designed to work
across multiple versions of Python and inside of windows, and
originally done for Cookiecutter. The code for Python 2.x is based on
Python 3 code that was extracted from source.

%prep
%setup -q -n whichcraft-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc AUTHORS.rst HISTORY.rst README.rst
%{python_sitelib}/whichcraft.py
%pycache_only %{python_sitelib}/__pycache__/whichcraft.*.pyc
%{python_sitelib}/whichcraft-%{version}.dist-info

%changelog
