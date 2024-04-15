#
# spec file for package python-rstcheck-core
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


Name:           python-rstcheck-core
Version:        1.2.1
Release:        0
Summary:        Checks syntax of reStructuredText and code blocks nested within it
License:        MIT
URL:            https://github.com/rstcheck/rstcheck-core
Source:         https://files.pythonhosted.org/packages/source/r/rstcheck-core/rstcheck-core-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools_scm >= 6.2}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module docutils >= 0.7}
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module Sphinx >= 4}
BuildRequires:  %{python_module pydantic >= 2}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  gcc-c++
# /SECTION
BuildRequires:  fdupes
Requires:       python-docutils >= 0.7
Requires:       python-pydantic >= 2
Suggests:       python-sphinx >= 4.0
Suggests:       python-pyyaml >= 6.0.0
BuildArch:      noarch
%python_subpackages

%description
Checks syntax of reStructuredText and code blocks nested within it

%prep
%autosetup -p1 -n rstcheck-core-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc AUTHORS.rst CHANGELOG.md README.rst
%license LICENSE
%{python_sitelib}/rstcheck_core
%{python_sitelib}/rstcheck_core-%{version}.dist-info

%changelog
