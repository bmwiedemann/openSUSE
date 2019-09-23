#
# spec file for package python-pydot
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-pydot
Version:        1.4.1
Release:        0
Summary:        Module to create (dot) graphs from Python
License:        MIT
Group:          Development/Libraries/Python
URL:            https://github.com/erocarrera/pydot
Source:         https://files.pythonhosted.org/packages/source/p/pydot/pydot-%{version}.tar.gz
# https://github.com/pydot/pydot/issues/204
Patch0:         pydot-skip-test.patch
BuildRequires:  %{python_module chardet}
BuildRequires:  %{python_module pyparsing >= 2.1.4}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  ghostscript-fonts-std
BuildRequires:  graphviz
BuildRequires:  graphviz-gd
BuildRequires:  python-rpm-macros
Requires:       graphviz
Requires:       python-pyparsing >= 2.1.4
Recommends:     graphviz-gd
BuildArch:      noarch
%python_subpackages

%description
pydot allows to create both directed and non-directed graphs from
Python. All attributes implemented in the Dot language up to Graphviz
2.16 are supported.

%prep
%setup -q -n pydot-%{version}
%patch0 -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python test/pydot_unittest.py --no-check

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/dot_parser.py*
%{python_sitelib}/pydot.py*
%pycache_only %{python_sitelib}/__pycache__/dot_parser.*.py*
%pycache_only %{python_sitelib}/__pycache__/pydot.*.py*
%{python_sitelib}/pydot-%{version}-py*.egg-info

%changelog
