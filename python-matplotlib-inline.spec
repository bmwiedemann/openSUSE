#
# spec file
#
# Copyright (c) 2022 SUSE LLC
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
%{?!python_module:%define python_module() python3-%{**}}
%define skip_python2 1
Name:           python-matplotlib-inline%{psuffix}
Version:        0.1.6
Release:        0
Summary:        Inline Matplotlib backend for Jupyter
License:        BSD-3-Clause
URL:            https://github.com/ipython/matplotlib-inline
Source:         https://files.pythonhosted.org/packages/source/m/matplotlib-inline/matplotlib-inline-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module traitlets}
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
%setup -q -n matplotlib-inline-%{version}

%build
%python_build

%install
%if ! %{with test}
%python_install
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
