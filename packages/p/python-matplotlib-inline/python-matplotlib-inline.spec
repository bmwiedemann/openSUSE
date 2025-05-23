#
# spec file for package python-matplotlib-inline
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
# no ipython anymore
%define skip_python39 1
%else
%define psuffix %{nil}
%bcond_with test
%endif
%{?sle15_python_module_pythons}
Name:           python-matplotlib-inline%{psuffix}
Version:        0.1.7
Release:        0
Summary:        Inline Matplotlib backend for Jupyter
License:        BSD-3-Clause
URL:            https://github.com/ipython/matplotlib-inline
Source:         https://files.pythonhosted.org/packages/source/m/matplotlib-inline/matplotlib_inline-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module traitlets}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-traitlets
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module ipython}
BuildRequires:  %{python_module matplotlib}
%endif
%python_subpackages

%description
Matplotlib Inline Back-end for IPython and Jupyter

%prep
%setup -q -n matplotlib_inline-%{version}

%build
%pyproject_wheel

%install
%if ! %{with test}
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
# this is upstream's only CI check either
%python_exec -B -c 'from matplotlib_inline.backend_inline import show'
%endif

%if ! %{with test}
%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/matplotlib_inline
%{python_sitelib}/matplotlib_inline-%{version}*-info
%endif

%changelog
