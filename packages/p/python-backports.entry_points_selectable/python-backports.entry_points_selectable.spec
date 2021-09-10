#
# spec file for package python-backports.entry_points_selectable
#
# Copyright (c) 2021 SUSE LLC
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
# See pep#0420 ... implicit namespace packages are available only in Python 3.3
%define skip_python2 1
Name:           python-backports.entry_points_selectable
Version:        1.1.0
Release:        0
Summary:        Compatibility shim providing selectable entry points for older implementations
License:        MIT
URL:            https://github.com/jaraco/backports.entry_points_selectable
Source:         https://files.pythonhosted.org/packages/source/b/backports.entry_points_selectable/backports.entry_points_selectable-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  %{python_module importlib_metadata}
BuildRequires:  %{python_module pytest >= 4.6}
BuildRequires:  %{python_module pytest-flake8}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest-black >= 0.3.7}
BuildRequires:  %{python_module pytest-mypy}
# BuildRequires:  %%{python_module pytest-checkdocs >= 2.4}
# BuildRequires:  %%{python_module pytest-enabler >= 1.0.1}
# # For docs
# BuildRequires:  %%{python_module Sphinx}
# BuildRequires:  %%{python_module jaraco.packaging >= 8.2}
# BuildRequires:  %%{python_module rst.linker >= 1.9}
BuildArch:      noarch
%python_subpackages

%description
Compatibility shim providing selectable entry points for older implementations

%prep
%autosetup -p1 -n backports.entry_points_selectable-%{version}

%build
%python_build

%install
%python_install

# PEP-420 allows implicit packages without an additional __init__.py
%{python_expand # remove explicit __init__.py files
rm -v %{buildroot}%{$python_sitelib}/backports/__init__.py \
      %{buildroot}%{$python_sitelib}/backports/__pycache__/__init__.*
%fdupes %{buildroot}%{$python_sitelib}
}

%check
%pytest

%files %{python_files}
%doc CHANGES.rst README.rst
%license LICENSE
%dir %{python_sitelib}/backports
%{python_sitelib}/backports.entry_points_selectable*
%{python_sitelib}/backports/entry_points_selectable.py
%dir %{python_sitelib}/backports/__pycache__
%pycache_only %{python_sitelib}/backports/__pycache__/*

%changelog
