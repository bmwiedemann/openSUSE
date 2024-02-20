#
# spec file for package python-pyee
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


Name:           python-pyee
Version:        11.1.0
Release:        0
Summary:        A port of node.js's EventEmitter to python
License:        MIT
URL:            https://github.com/jfhbrook/pyee
Source:         https://files.pythonhosted.org/packages/source/p/pyee/pyee-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module vcversioner}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-typing_extensions
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Twisted}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest-trio}
# /SECTION
%python_subpackages

%description
pyee supplies an ``EventEmitter`` object similar to the ``EventEmitter``
from Node.js.

%prep
%setup -q -n pyee-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/pyee
%{python_sitelib}/pyee-%{version}.dist-info

%changelog
