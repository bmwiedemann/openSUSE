#
# spec file for package python-pypet
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define         skip_python2 1
# Tests take forever
%bcond_with     test
Name:           python-pypet
Version:        0.4.3
Release:        0
Summary:        Parameter exploration and storage of results for numerical simulations
License:        BSD-3-Clause
Group:          Development/Languages/Python
Url:            https://github.com/SmokinCaterpillar/pypet
Source:         https://files.pythonhosted.org/packages/source/p/pypet/pypet-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%if %{with test}
BuildRequires:  %{python_module numpy >= 1.6.1}
BuildRequires:  %{python_module pandas >= 0.15.0}
BuildRequires:  %{python_module scipy >= 0.9.0}
BuildRequires:  %{python_module scoop >= 0.7.1}
BuildRequires:  %{python_module tables >= 3.1.1}
%endif
Requires:       python-numpy >= 1.6.1
Requires:       python-pandas >= 0.15.0
Requires:       python-scipy >= 0.9.0
Requires:       python-tables >= 3.1.1
Recommends:     python-GitPython >= 0.2.1
Recommends:     python-Sumatra >= 0.7.1
Recommends:     python-dill >= 0.2.1
Recommends:     python-psutil >= 2.0.0
Recommends:     python-scoop >= 0.7.1
BuildArch:      noarch

%python_subpackages

%description
pypet is the Python parameter exploration toolkit. pypet manages
exploration of the parameter space of any numerical simulation in
Python, thereby storing data into HDF5 files. Moreover, pypet offers
a data container which gives access to all parameters and results
from a single source.

%prep
%setup -q -n pypet-%{version}

%build
export LANG=en_US.UTF-8
%python_build

%install
export LANG=en_US.UTF-8
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%if %{with test}
%check
export LANG=en_US.UTF-8
%python_exec setup.py test
%endif

%files %{python_files}
%defattr(-,root,root,-)
%doc README.md
%license LICENSE
%{python_sitelib}/*

%changelog
