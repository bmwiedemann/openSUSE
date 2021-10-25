#
# spec file
#
# Copyright (c) 2021 SUSE LLC
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
Name:           python-flit-core%{psuffix}
Version:        3.4.0
Release:        0
Summary:        Distribution-building parts of Flit
License:        BSD-3-Clause
URL:            https://github.com/takluyver/flit
Source:         https://files.pythonhosted.org/packages/source/f/flit-core/flit_core-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.6}
%if %{with test}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module testpath}
BuildRequires:  %{python_module tomli}
%endif
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Requires:       python-tomli
BuildArch:      noarch
%python_subpackages

%description
Flit is a simple way to put Python packages and modules on PyPI.

%prep
%setup -q -n flit_core-%{version}

%build
# https://flit.readthedocs.io/en/latest/bootstrap.html
python3 build_dists.py

%if !%{with test}
%install
%{python_expand # do manually what pip would do
mkdir -p %{buildroot}%{$python_sitelib}
unzip dist/flit_core-%{version}-py3-none-any.whl -d %{buildroot}%{$python_sitelib}
rm -r  %{buildroot}%{$python_sitelib}/flit_core/tests
}
%python_compileall
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
%pytest
%endif

%if !%{with test}
%files %{python_files}
%{python_sitelib}/flit_core
%{python_sitelib}/flit_core-%{version}*-info
%endif

%changelog
