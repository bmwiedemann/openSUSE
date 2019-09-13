#
# spec file for package python-dpcontracts
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
%define skip_python2 1
Name:           python-dpcontracts
Version:        0.6.0
Release:        0
Summary:        An implementation of contracts for Python
License:        LGPL-3.0-or-later
Group:          Development/Languages/Python
URL:            https://github.com/deadpixi/contracts
Source:         https://files.pythonhosted.org/packages/source/d/dpcontracts/dpcontracts-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/deadpixi/contracts/master/LICENSE
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
This module provides a collection of decorators for
writing software using contracts.

Contracts are a debugging and verification tool.  They are declarative
statements about what states a program must be in to be considered
"correct" at runtime.  They are similar to assertions, and are verified
automatically at various well-defined points in the program.  Contracts can
be specified on functions and on classes.

%prep
%setup -q -n dpcontracts-%{version}
cp %{SOURCE1} .

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
