#
# spec file for package python-sybil
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
Name:           python-sybil
Version:        3.0.0
Release:        0
Summary:        Automated testing of examples in documentation
License:        MIT
URL:            https://github.com/cjw296/sybil
Source:         https://files.pythonhosted.org/packages/source/s/sybil/sybil-%{version}.tar.gz
Patch0:         python-sybil-fix-ordering.diff
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest >= 6.2}
BuildRequires:  %{python_module setuptools-git}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
%if 0%{?sle_version} && 0%{?sle_version} <= 150400
BuildRequires:  %{python_module dataclasses}
%endif
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Recommends:     python-pytest
BuildArch:      noarch
%python_subpackages

%description
python-sybil provides a way to test examples in one's documentation by parsing
them from the documentation source and evaluating the parsed examples as part
of the normal test run. Integration is provided for the main Python test runners.

%prep
%setup -q -n sybil-%{version}
sed -i '/pytest-cov/ d'  setup.py
%autopatch -p1

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst docs/changes.rst
%license docs/license.rst
%{python_sitelib}/sybil
%{python_sitelib}/sybil-%{version}*-info

%changelog
