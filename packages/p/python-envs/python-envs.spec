#
# spec file for package python-envs
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


%{?sle15_python_module_pythons}
Name:           python-envs
Version:        1.4
Release:        0
Summary:        Easy access of environment variables from Python
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/capless/envs
Source:         https://files.pythonhosted.org/packages/source/e/envs/envs-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module base >= 3.6}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core >= 1.0.0}
BuildRequires:  %{python_module click >= 8.0.3}
BuildRequires:  %{python_module Jinja2 >= 3.0.3}
BuildRequires:  %{python_module terminaltables >= 3.1.10}
BuildRequires:  %{python_module poetry-core >= 1.0.0}
Requires:  python-click >= 8.0.3
Requires:  python-Jinja2 >= 3.0.3
Requires:  python-terminaltables >= 3.1.10
BuildArch:      noarch
%python_subpackages

%description
Easy access of environment variables from Python with support for typing 
(ex. booleans, strings, lists, tuples, integers, floats, and dicts).
Now with CLI settings file converter. 

%prep
%autosetup -p1 -n envs-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
# Fix python-bytecode-inconsistent-mtime
pushd %{buildroot}%{python_sitelib}
find . -name '*.pyc' -exec rm -f '{}' ';'
python%python_bin_suffix -m compileall *.py ';'
popd
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_clone -a %{buildroot}%{_bindir}/envs

%check
%pyunittest -v

%post
%python_install_alternative envs

%postun
%python_uninstall_alternative envs

%files %{python_files}
%license LICENSE
%{python_sitelib}/envs
%{python_sitelib}/envs-%{version}.dist-info
%python_alternative %{_bindir}/envs

%changelog
