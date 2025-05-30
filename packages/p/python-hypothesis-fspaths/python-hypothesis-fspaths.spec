#
# spec file for package python-hypothesis-fspaths
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


Name:           python-hypothesis-fspaths
Version:        0.1
Release:        0
Summary:        Hypothesis extension for generating filesystem paths
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/lazka/hypothesis-fspaths
Source:         https://files.pythonhosted.org/packages/source/h/hypothesis-fspaths/hypothesis-fspaths-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-hypothesis
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module hypothesis}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
Hypothesis extension for generating filesystem paths

%prep
%setup -q -n hypothesis-fspaths-%{version}
# https://github.com/lazka/hypothesis-fspaths/issues/3
sed -i '/pytest-runner/d' setup.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/hypothesis[-_]fspaths.py
%{python_sitelib}/hypothesis[-_]fspaths-%{version}*-info
%pycache_only %{python_sitelib}/__pycache__/hypothesis[-_]fspaths*

%changelog
