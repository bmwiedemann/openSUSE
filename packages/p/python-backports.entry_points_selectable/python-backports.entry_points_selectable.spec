#
# spec file for package python-backports.entry_points_selectable
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


%bcond_without python2
%{?sle15_python_module_pythons}
Name:           python-backports.entry_points_selectable
Version:        1.2.0
Release:        0
Summary:        Compatibility shim providing selectable entry points for older implementations
License:        MIT
URL:            https://github.com/jaraco/backports.entry_points_selectable
Source:         https://files.pythonhosted.org/packages/source/b/backports.entry_points_selectable/backports.entry_points_selectable-%{version}.tar.gz
BuildRequires:  %{python_module importlib-metadata if %python-base < 3.7}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest >= 4.6}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module toml}
BuildRequires:  %{python_module wheel}
%if %{with python2}
BuildRequires:  python-backports
%endif
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%ifpython2
Requires:       python-backports
%endif
BuildArch:      noarch
%python_subpackages

%description
Compatibility shim providing selectable entry points for older implementations

%prep
%autosetup -p1 -n backports.entry_points_selectable-%{version}

%build
%pyproject_wheel

%install
%pyproject_install

# PEP-420 allows implicit packages without an additional __init__.py for python >= 3.3,
# gh#jaraco/backports.entry_points_selectable#5
%{python_expand # remove explicit __init__.py files (unless we need it for the python2 tests)
if [ "${python_flavor}" != "python2" ]; then
  rm -v %{buildroot}%{$python_sitelib}/backports/__init__.py* \
        %{buildroot}%{$python_sitelib}/backports/__pycache__/__init__.*
  %fdupes %{buildroot}%{$python_sitelib}
fi
}

%check
%pytest --pyargs backports

%files %{python_files}
%doc CHANGES.rst README.rst
%license LICENSE
%dir %{python_sitelib}/backports
%ifpython2
# provided by python2-backports
%exclude %{python_sitelib}/backports/__init__.py*
%endif
%{python_sitelib}/backports/entry_points_selectable.py*
%pycache_only %dir %{python_sitelib}/backports/__pycache__
%pycache_only %{python_sitelib}/backports/__pycache__/*
%{python_sitelib}/backports.entry_points_selectable-%{version}*-info

%changelog
