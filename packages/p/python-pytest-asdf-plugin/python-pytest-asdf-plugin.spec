#
# spec file for package python-pytest-asdf-plugin
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


Name:           python-pytest-asdf-plugin
Version:        0.1.2
Release:        0
Summary:        Pytest plugin for testing ASDF schemas
License:        BSD-3-Clause
URL:            https://github.com/asdf-format/pytest-asdf-plugin
Source:         https://files.pythonhosted.org/packages/source/p/pytest_asdf_plugin/pytest_asdf_plugin-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.9}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 60}
BuildRequires:  %{python_module setuptools_scm >= 8}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-asdf
Requires:       python-pytest >= 7
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module asdf}
BuildRequires:  %{python_module pytest >= 7}
# /SECTION
%python_subpackages

%description
Pytest plugin for testing ASDF schemas

%prep
%autosetup -p1 -n pytest_asdf_plugin-%{version}
sed -i "/'--color=yes',$/d" pyproject.toml

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%{python_sitelib}/pytest_asdf_plugin
%{python_sitelib}/pytest_asdf_plugin-%{version}.dist-info

%changelog
