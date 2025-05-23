#
# spec file for package python-Gloo
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
Name:           python-Gloo
Version:        0.1.2
Release:        0
Summary:        Project management for data analysis projects
License:        BSD-3-Clause
URL:            https://pypi.python.org/pypi/Gloo/
Source:         https://files.pythonhosted.org/packages/source/G/Gloo/Gloo-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pandas
BuildArch:      noarch

%python_subpackages

%description
Gloo ties together a lot of the data analysis actions that happen
regularly. It automatically loads data into the IPython environment,
runs scripts, makes utitlity functions available and more.

%prep
%setup -q -n Gloo-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# The tests in test directory are broken and so they are not checked

%files %{python_files}
%doc CHANGES.txt README.rst
%license LICENSE.txt
%{python_sitelib}/[Gg]loo
%{python_sitelib}/[Gg]loo-%{version}.dist-info

%changelog
