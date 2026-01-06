#
# spec file for package python-pytest-mpl
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
Name:           python-pytest-mpl
Version:        0.18.0
Release:        0
Summary:        Pytest plugin for testing Matplotlib figures
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            https://github.com/matplotlib/pytest-mpl
Source:         https://files.pythonhosted.org/packages/source/p/pytest_mpl/pytest_mpl-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.9}
BuildRequires:  %{python_module pip}
# Upstream says >= 80 but that is a bit ambitious and not needed here
BuildRequires:  %{python_module setuptools}
# Upstream says >= 8 but that is not enough for the [simple] hook used
BuildRequires:  %{python_module setuptools_scm >= 9}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Jinja2 >= 2.10.2
Requires:       python-Pillow >= 8.1.1
Requires:       python-matplotlib >= 3.3.3
Requires:       python-packaging >= 22
Requires:       python-pytest >= 5.4.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Jinja2 >= 2.10.2}
BuildRequires:  %{python_module Pillow >= 8.1.1}
BuildRequires:  %{python_module matplotlib >= 3.3.3}
BuildRequires:  %{python_module packaging >= 22}
BuildRequires:  %{python_module pytest >= 5.4}
# /SECTION
%python_subpackages

%description
This is a pytest plugin to help with testing figures output from Matplotlib.

%prep
%setup -q -n pytest_mpl-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# not the right path setup in obs build environment
donttest="(test_generate_summary and test_config)"
%pytest -k "not ($donttest)"

%files %{python_files}
%doc CHANGES.md README.rst
%license LICENSE
%{python_sitelib}/pytest_mpl
%{python_sitelib}/pytest_mpl-%{version}.dist-info

%changelog
