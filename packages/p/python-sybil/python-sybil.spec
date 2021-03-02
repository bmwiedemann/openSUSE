#
# spec file for package python-sybil
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
Name:           python-sybil
Version:        2.0.1
Release:        0
Summary:        Automated testing of examples in documentation
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/cjw296/sybil
Source:         https://files.pythonhosted.org/packages/source/s/sybil/sybil-%{version}.tar.gz
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools-git}
BuildRequires:  %{python_module setuptools}
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

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst docs/changes.rst
%license docs/license.rst
%{python_sitelib}/sybil
%{python_sitelib}/sybil-%{version}*-info

%changelog
