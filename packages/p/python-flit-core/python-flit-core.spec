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
Name:           python-flit-core%{psuffix}
Version:        3.6.0
Release:        0
Summary:        Distribution-building parts of Flit
License:        BSD-3-Clause
URL:            https://github.com/pypa/flit
Source0:        https://files.pythonhosted.org/packages/source/f/flit-core/flit_core-%{version}.tar.gz
Source1:        https://github.com/pypa/flit/raw/%{version}/flit_core/build_dists.py
BuildRequires:  %{python_module base >= 3.6}
%if %{with test}
BuildRequires:  %{python_module flit-core = %{version}}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module testpath}
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
cp %{SOURCE1} .

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
%{python_expand # debundle after the bootstrap. See vendor/README
sed -i 's/from .vendor import tomli/import tomli/'  %{buildroot}%{$python_sitelib}/flit_core/config.py
rm -r %{buildroot}%{$python_sitelib}/flit_core/vendor
}
%{?python_compileall}
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
# make sure we do not test the sources but the debundled package
rm flit_core/*.py pyproject.toml
%pytest -rfEs
%endif

%if !%{with test}
%files %{python_files}
%{python_sitelib}/flit_core
%{python_sitelib}/flit_core-%{version}*-info
%endif

%changelog
