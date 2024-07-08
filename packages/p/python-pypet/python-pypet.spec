#
# spec file for package python-pypet
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


%bcond_without  test
Name:           python-pypet
Version:        0.6.1
Release:        0
Summary:        Parameter exploration and storage of results for numerical simulations
License:        BSD-3-Clause
URL:            https://github.com/SmokinCaterpillar/pypet
Source:         https://files.pythonhosted.org/packages/source/p/pypet/pypet-%{version}.tar.gz
# PATCH-FIX-OPENSUSE Do not call decode() on objects that do not have that
# method
Patch0:         do-not-decode-int.patch
# PATCH-FIX-UPSTREAM ConfigParser_readfp-312.patch gh#SmokinCaterpillar/pypet!69 mcepl@suse.com
# Long deprecated method .readfp() was finally removed in 3.12.
Patch1:         ConfigParser_readfp-312.patch
# PATCH-FIX-UPSTREAM https://github.com/SmokinCaterpillar/pypet/pull/70 Replace deprecated/removed unittest.TestCase method aliases
Patch2:         unittest.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%if %{with test}
BuildRequires:  %{python_module dill}
# Due to tables
BuildRequires:  %{python_module numpy >= 1.6.1 with %python-numpy < 2}
BuildRequires:  %{python_module pandas >= 0.15.0}
BuildRequires:  %{python_module scipy >= 0.9.0}
BuildRequires:  %{python_module tables >= 3.1.1}
%endif
Requires:       python-pandas >= 0.150
Requires:       python-scipy >= 0.9.0
Requires:       python-tables >= 3.1.1
Requires:       (python-numpy >= 1.6.1 with python-numpy < 2)
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
%autosetup -p1 -n pypet-%{version}

%build
export LANG=en_US.UTF-8
%pyproject_wheel

%install
export LANG=en_US.UTF-8
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%if %{with test}
%check
export LANG=en_US.UTF-8
pushd pypet/tests
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitelib}
$python -B all_single_core_tests.py
}
%endif

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/pypet
%{python_sitelib}/pypet-%{version}.dist-info

%changelog
