#
# spec file for package python-pytest-regressions
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


%{?sle15_python_module_pythons}
Name:           python-pytest-regressions
Version:        2.4.2
Release:        0
License:        MIT
Summary:        Python fixtures to write regression tests
URL:            https://github.com/ESSS/pytest-regressions
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/p/pytest-regressions/pytest-regressions-%{version}.tar.gz
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module pytest >= 6.2.0}
BuildRequires:  %{python_module Pillow}
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pytest-datadir >= 1.2.0}
# These could be added as build dep for testing but are commented to
# reduce the number of requirements.
# BuildRequires:  %%{python_module pandas}
# BuildRequires:  %%{python_module matplotlib}
# /SECTION
BuildRequires:  fdupes
Requires:       python-PyYAML
Requires:       python-pytest >= 6.2.0
Requires:       python-pytest-datadir >= 1.2.0
Suggests:       python-matplotlib
Suggests:       python-numpy
Suggests:       python-pandas
Suggests:       python-Pillow
BuildArch:      noarch

%python_subpackages

%description
Python fixtures to write regression tests.

%prep
%autosetup -p1 -n pytest-regressions-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# ignore tests that depends on matplotlib
donttest="test_image_regression"
# Requires python-pandas
donttest+=" or test_foo"
# Ignore tests that depends on python-pandas
%pytest --ignore tests/test_num_regression.py --ignore tests/test_dataframe_regression.py -k "not ($donttest)"

%files %{python_files}
%doc CHANGELOG.rst README.rst
%license LICENSE
%{python_sitelib}/pytest_regressions*

%changelog
