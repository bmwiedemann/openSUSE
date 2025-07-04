#
# spec file for package python-orderedmultidict
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
Name:           python-orderedmultidict
Version:        1.0.1
Release:        0
Summary:        Ordered Multivalue Dictionary
License:        Unlicense
Group:          Development/Languages/Python
URL:            https://github.com/gruns/orderedmultidict
Source:         https://files.pythonhosted.org/packages/source/o/orderedmultidict/orderedmultidict-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-six >= 1.8.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module six >= 1.8.0}
# /SECTION
%python_subpackages

%description
Ordered Multivalue Dictionary - omdict.

%prep
%setup -q -n orderedmultidict-%{version}
sed -i 's/^.*flake8.*/tests_require = []/' setup.py
chmod a-x README.md LICENSE.md
rm -r *.egg-info

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest discover -v tests/

%files %{python_files}
%doc README.md
%license LICENSE.md
%{python_sitelib}/orderedmultidict
%{python_sitelib}/orderedmultidict-%{version}*-info

%changelog
