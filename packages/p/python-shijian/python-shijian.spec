#
# spec file for package python-shijian
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
Name:           python-shijian
Version:        2023.10.19.215
Release:        0
Summary:        Python utility functions relating to time and filenames
License:        GPL-3.0-only
URL:            https://github.com/wdbm/shijian
Source0:        https://files.pythonhosted.org/packages/source/s/shijian/shijian-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/wdbm/shijian/refs/heads/master/shijian/__init__.py
Source100:      python-shijian-rpmlintrc
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-matplotlib
Requires:       python-numpy
Requires:       python-pandas
Requires:       python-python-dateutil
Requires:       python-scikit-learn
Requires:       python-scipy
Requires:       python-seaborn
Requires:       python-technicolor
Recommends:     python-ipywidgets
Recommends:     python-pyprel
BuildArch:      noarch
%python_subpackages

%description
A Python module with a number of utility functions for formatting
timestamps, counting time, and deriving non-overlapping filenames or
sequences.

%prep
%setup -q -n shijian-%{version}
cp %{SOURCE1} shijian.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# no upstream tests

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/shijian.py
%pycache_only %{python_sitelib}/__pycache__/shijian*
%{python_sitelib}/shijian-%{version}*-info

%changelog
