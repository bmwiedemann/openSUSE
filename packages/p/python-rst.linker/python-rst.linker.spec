#
# spec file for package python-rst.linker
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


%define _name   rst.linker
%{?sle15_python_module_pythons}
Name:           python-rst.linker
Version:        2.4.0
Release:        0
Summary:        Changelog link and timestamp adding Sphinx plugin
License:        MIT
URL:            https://github.com/jaraco/rst.linker
Source:         https://files.pythonhosted.org/packages/source/r/%{_name}/%{_name}-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module importlib-metadata if %python-version < 3.8}
BuildRequires:  %{python_module path}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-dateutil}
BuildRequires:  %{python_module setuptools >= 56}
BuildRequires:  %{python_module setuptools_scm >= 3.4.1}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-Sphinx
%if 0%{python_version_nodots} < 38
Requires:       python-importlib-metadata
%endif
Requires:       python-python-dateutil
BuildArch:      noarch
%python_subpackages

%description
rst.linker is a Sphinx plugin to add links and timestamps to the
changelog.

%prep
%setup -q -n %{_name}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc CHANGES.rst README.rst
# This needs a fix if there will be any more rst.* namespace packages (none on PyPI so far)
%{python_sitelib}/rst
%{python_sitelib}/rst.linker-%{version}*-info

%changelog
