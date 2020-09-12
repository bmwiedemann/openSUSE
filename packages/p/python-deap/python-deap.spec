#
# spec file for package python-deap
#
# Copyright (c) 2020 SUSE LLC
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
Name:           python-deap
Version:        1.3.1
Release:        0
Summary:        Distributed Evolutionary Algorithms in Python
License:        LGPL-3.0-only
URL:            https://github.com/DEAP/deap
Source:         https://files.pythonhosted.org/packages/source/d/deap/deap-%{version}.tar.gz
# https://github.com/DEAP/deap/pull/507
Patch0:         python-deap-remove-nose.patch
# https://github.com/DEAP/deap/pull/507
Patch1:         python-deap-python3.patch
BuildRequires:  %{python_module numpy-devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
DEAP is intended to be an easy to use distributed evolutionary algorithm
library in the Python language. Its two main components are modular and
can be used separately. The first module is a Distributed Task Manager
(DTM), which is intended to run on cluster of computers. The second
part is the Evolutionary Algorithms in Python (EAP) framework.

%prep
%setup -q -n deap-%{version}
%patch0 -p1
%patch1 -p1

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
# failures only for 2.7; will have to be soved trough
# https://github.com/DEAP/deap/pull/507
# as well
%pytest_arch -k 'not (test_nsga3 or test_bin2float)'

%files %{python_files}
%doc README.md
%license LICENSE.txt
%{python_sitearch}/*

%changelog
