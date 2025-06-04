#
# spec file for package python-pydotplus
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


%bcond_without tests
Name:           python-pydotplus
Version:        2.0.2
Release:        0
Summary:        Python interface to Graphviz's Dot language
License:        MIT
Group:          Development/Languages/Python
URL:            https://pydotplus.readthedocs.org/
Source:         https://files.pythonhosted.org/packages/source/p/pydotplus/pydotplus-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pyparsing >= 2.0.1}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       graphviz
Requires:       python-pyparsing >= 2.0.1
BuildArch:      noarch
%if %{with tests}
BuildRequires:  graphviz
%endif
%python_subpackages

%description
PyDotPlus is an improved version of the old pydot project that provides a
Python Interface to Graphviz's Dot language.

%prep
%setup -q -n pydotplus-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%if %{with tests}
%check
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitelib}
$python test/pydot_unittest.py
}
%endif

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/pydotplus
%{python_sitelib}/pydotplus-%{version}*-info

%changelog
