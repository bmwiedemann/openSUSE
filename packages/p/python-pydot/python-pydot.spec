#
# spec file for package python-pydot
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
Name:           python-pydot
Version:        3.0.4
Release:        0
Summary:        Module to create (dot) graphs from Python
License:        MIT
URL:            https://github.com/erocarrera/pydot
Source:         https://files.pythonhosted.org/packages/source/p/pydot/pydot-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module chardet}
BuildRequires:  %{python_module parameterized}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pyparsing >= 3.0.9}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  ghostscript-fonts-std
BuildRequires:  graphviz
BuildRequires:  graphviz-gd
BuildRequires:  python-rpm-macros
Requires:       graphviz
Requires:       graphviz-gd
Requires:       python-pyparsing >= 3.0.9
# we need at least some fonts
Requires:       dejavu-fonts
BuildArch:      noarch
%python_subpackages

%description
pydot allows to create both directed and non-directed graphs from
Python. All attributes implemented in the Dot language up to Graphviz
2.16 are supported.

%prep
%autosetup -p1 -n pydot-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSES/MIT.txt LICENSES/Python-2.0.txt
%doc README.md
%{python_sitelib}/pydot
%{python_sitelib}/pydot-%{version}.dist-info

%changelog
