#
# spec file for package python-pydotplus
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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
%bcond_without tests
Name:           python-pydotplus
Version:        2.0.2
Release:        0
Summary:        Python interface to Graphviz's Dot language
License:        MIT
Group:          Development/Languages/Python
URL:            http://pydotplus.readthedocs.org/
Source:         https://files.pythonhosted.org/packages/source/p/pydotplus/pydotplus-%{version}.tar.gz
BuildRequires:  %{python_module pyparsing >= 2.0.1}
BuildRequires:  %{python_module setuptools}
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
%python_build

%install
%python_install
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
%{python_sitelib}/*

%changelog
