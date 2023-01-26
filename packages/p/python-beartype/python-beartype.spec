#
# spec file for package python-beartype
#
# Copyright (c) 2023 SUSE LLC
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


Name:           python-beartype
Version:        0.12.0
Release:        0
Summary:        Unbearably fast runtime type checking in pure Python
License:        MIT
URL:            https://github.com/beartype/beartype
Source:         https://files.pythonhosted.org/packages/source/b/beartype/beartype-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module mypy >= 0.800}
BuildRequires:  %{python_module Sphinx}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pytest >= 4.0.0}
BuildRequires:  %{python_module typing_extensions}
# /SECTION
BuildRequires:  fdupes
Suggests:       python-typing_extensions >= 3.10.0.0
Suggests:       python-coverage >= 5.5
Suggests:       python-sphinx
Suggests:       python-pytest >= 4.0.0
Suggests:       python-tox >= 3.20.1
Suggests:       python-sphinx >= 4.1.0
Suggests:       python-mypy >= 0.800
Suggests:       python-typing_extensions
Suggests:       python-numpy
Suggests:       python-sphinx == 4.1.0
Suggests:       python-sphinx-rtd-theme == 0.5.1
Suggests:       python-sphinx
Suggests:       python-pytest >= 4.0.0
Suggests:       python-coverage >= 5.5
Suggests:       python-mypy >= 0.800
Suggests:       python-typing_extensions
Suggests:       python-numpy
BuildArch:      noarch
%python_subpackages

%description
Unbearably fast runtime type checking in pure Python.

%prep
%autosetup -p1 -n beartype-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Disable test_beartype_in_sphinx, broken with sphinx 6.1.3 gh#beartype/beartype#209
%pytest -k 'not (test_doc_readme or test_sphinx or test_pep561_mypy or test_beartype_in_sphinx)'

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/beartype
%{python_sitelib}/beartype-%{version}*-info

%changelog
