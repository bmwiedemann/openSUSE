#
# spec file
#
# Copyright (c) 2023 SUSE LLC
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif

%define         skip_python2 1
Name:           python-nbval%{psuffix}
Version:        0.10.0
Release:        0
Summary:        A pytest plugin to validate Jupyter notebooks
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/computationalmodelling/nbval
Source:         https://files.pythonhosted.org/packages/source/n/nbval/nbval-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.6}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-coverage
Requires:       python-ipykernel
Requires:       python-jupyter-client
Requires:       python-nbformat
Requires:       python-pytest >= 2.8
Provides:       python-jupyter_nbval = %{version}
Obsoletes:      python-jupyter_nbval < %{version}
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module matplotlib}
BuildRequires:  %{python_module nbdime}
BuildRequires:  %{python_module nbval = %{version}}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module sympy}
%endif
%if "%{python_flavor}" == "python3" || "%{?python_provides}"  == "python3"
Provides:       jupyter-nbval = %{version}
%endif
%python_subpackages

%description
The plugin adds functionality to py.test to recognise and collect
Jupyter notebooks. The intended purpose of the tests is to determine
whether execution of the stored inputs match the stored outputs of
the .ipynb file. Whilst also ensuring that the notebooks are running
without errors.

The tests were designed to ensure that Jupyter notebooks (especially
those for reference and documentation), are executing consistently.

Each cell is taken as a test, a cell that doesn't reproduce the
expected output will fail.

%prep
%autosetup -p1 -n nbval-%{version}
sed -i 's/\r$//' README.md

%if ! %{with test}
%build
export LANG=en_US.UTF-8
%pyproject_wheel

%install
export LANG=en_US.UTF-8
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
# see dodo.py for call signature
%{pytest tests/ --nbval \
                --nbval-current-env \
                --nbval-sanitize-with tests/sanitize_defaults.cfg \
                --ignore tests/ipynb-test-samples
}
%endif

%if ! %{with test}
%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/nbval
%{python_sitelib}/nbval-%{version}.dist-info
%endif

%changelog
