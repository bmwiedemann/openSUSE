#
# spec file for package python-deap
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
Name:           python-deap
Version:        1.4.2
Release:        0
Summary:        Distributed Evolutionary Algorithms in Python
License:        LGPL-3.0-only
URL:            https://github.com/DEAP/deap
Source:         https://files.pythonhosted.org/packages/source/d/deap/deap-%{version}.tar.gz
BuildRequires:  %{python_module numpy-devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module pytest}
# /SECTION
Requires:       python-numpy
%python_subpackages

%description
DEAP is intended to be an easy to use distributed evolutionary algorithm
library in the Python language. Its two main components are modular and
can be used separately. The first module is a Distributed Task Manager
(DTM), which is intended to run on cluster of computers. The second
part is the Evolutionary Algorithms in Python (EAP) framework.

%prep
%setup -q -n deap-%{version}

%build
export CFLAGS="%{optflags}"
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%pytest_arch

%files %{python_files}
%doc README.md
%license LICENSE.txt
%{python_sitearch}/deap
%{python_sitearch}/deap-%{version}.dist-info

%changelog
