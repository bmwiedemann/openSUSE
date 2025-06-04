#
# spec file for package python-tkreadonly
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


Name:           python-tkreadonly
Version:        0.6.1
Release:        0
Summary:        A set of Tkinter widgets to display readonly text and code
License:        BSD-3-Clause
URL:            http://github.org/pybee/tkreadonly
Source:         https://files.pythonhosted.org/packages/source/t/tkreadonly/tkreadonly-%{version}.tar.gz
BuildRequires:  %{python_module idle}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module tk}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Pygments >= 1.5
Requires:       python-idle
Requires:       python-tk
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Pygments >= 1.5}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
A set of Tkinter widgets to display readonly text and code.

%prep
%setup -q -n tkreadonly-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest tests.py

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/tkreadonly.py
%pycache_only %{python_sitelib}/__pycache__/tkreadonly.*.pyc
%{python_sitelib}/tkreadonly-%{version}.dist-info

%changelog
