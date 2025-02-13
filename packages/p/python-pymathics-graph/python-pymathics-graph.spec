#
# spec file for package python-pymathics-graph
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


%define skip_python313 1
%define modname pymathics_graph
Name:           python-pymathics-graph
Version:        8.0.1
Release:        0
Summary:        Mathics Graph functions using NetworkX and Matplotlib
License:        GPL-3.0-only
URL:            https://github.com/Mathics3/pymathics-graph
Source0:        https://files.pythonhosted.org/packages/source/p/pymathics-graph/%{modname}-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
# SECTION test requirements
BuildRequires:  %{python_module Mathics3 >= 8.0.0}
BuildRequires:  %{python_module matplotlib}
BuildRequires:  %{python_module networkx >= 3.0.0}
BuildRequires:  %{python_module pydot}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module scipy >= 1.10.0}
BuildRequires:  %{python_module testsuite}
# /SECTION
BuildRequires:  fdupes
Requires:       python-Mathics3 >= 8.0.0
Requires:       python-matplotlib
Requires:       python-networkx >= 3.0.0
Requires:       python-pydot
Requires:       python-scipy >= 1.10.0
BuildArch:      noarch
%python_subpackages

%description
PyMathics-Graph is a Mathics3 Graph Module using NetworkX and Matplotlib.

%prep
%autosetup -p1 -n %{modname}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export MATHICS_CHARACTER_ENCODING="ASCII"
%pytest test

%files %{python_files}
%license LICENSE
%{python_sitelib}/pymathics/
%{python_sitelib}/%{modname}-%{version}*.*-info/

%changelog
