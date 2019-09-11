#
# spec file for package python-pydot3
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2017 Dr. Axel Braun
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}

%define modname pydot3
Name:           python-%{modname}
Version:        1.0.9
Release:        0
Summary:        Create (dot) graphs from python
License:        MIT
Group:          Development/Libraries/Python
Url:            https://pypi.python.org/pypi/pydot3
Source:         https://files.pythonhosted.org/packages/source/p/%{modname}/%{modname}-%{version}.tar.gz
Source1:        example-demo.py
Source2:        example-rank.py
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
Requires:       graphviz
Requires:       python-pyparsing
BuildArch:      noarch
%python_subpackages

%description
pydot allows to easily create both directed and non directed graphs from Python.
Currently all attributes implemented in the Dot language are supported (up to Graphviz 2.16).

%prep
%setup -q -n %{modname}-%{version}

mkdir examples && cp %{SOURCE1} %{SOURCE2} examples

%build
%python_build

%install
%python_install
rm -rf %{buildroot}%{_prefix}/{LICENSE,README,README.md} # Wrongly installed by setup script

%files %{python_files}
%defattr(-,root,root,-)
%doc LICENSE examples README.md
%{python_sitelib}/*

%changelog
