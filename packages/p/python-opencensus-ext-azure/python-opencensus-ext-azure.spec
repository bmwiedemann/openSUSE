#
# spec file for package python-opencensus-ext-azure
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


%define repo_version 0.11.4-1.1.14

%{?sle15_python_module_pythons}
Name:           python-opencensus-ext-azure
Version:        1.1.14
Release:        0
Summary:        OpenCensus Azure Monitor Exporters
License:        Apache-2.0
URL:            https://github.com/census-instrumentation/opencensus-python
Source:         https://github.com/census-instrumentation/opencensus-python/archive/v%{repo_version}.tar.gz#/opencensus-%{repo_version}.tar.gz
# PATCH-FIX-UPSTREAM opencensus-pr1002-remove-mock.patch -- gh#census-instrumentation/opencensus-python#1002
Patch0:         opencensus-pr1002-remove-mock.patch
# PATCH-FIX-UPSTREAM python313.patch -- gh#census-instrumentation/opencensus-python#1248
Patch1:         python313.patch
BuildRequires:  %{python_module azure-core >= 1.12.0}
BuildRequires:  %{python_module azure-identity >= 1.5.0}
BuildRequires:  %{python_module opencensus >= 0.11.0}
BuildRequires:  %{python_module psutil >= 5.6.3}
BuildRequires:  %{python_module requests >= 2.19.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
Requires:       python-azure-core >= 1.12.0
Requires:       python-azure-identity >= 1.5.0
Requires:       python-opencensus >= 0.11.0
Requires:       python-psutil >= 5.6.3
Requires:       python-requests >= 2.19.0
%python_subpackages

%description
OpenCensus Azure Monitor Exporters

%prep
%setup -q -n opencensus-python-%{repo_version}/contrib/opencensus-ext-azure
pushd ../..
%autopatch -p1
popd
# for discovery to work
touch tests/__init__.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%{python_expand # delete common files
rm -rf %{buildroot}%{$python_sitelib}/opencensus/__init__.*
rm -rf %{buildroot}%{$python_sitelib}/opencensus/__pycache__
rm -rf %{buildroot}%{$python_sitelib}/opencensus/common/__init__.*
rm -rf %{buildroot}%{$python_sitelib}/opencensus/common/__pycache__
rm -rf %{buildroot}%{$python_sitelib}/opencensus/ext/__init__.*
rm -rf %{buildroot}%{$python_sitelib}/opencensus/ext/__pycache__
}

%check
%python_exec -m unittest discover -v

%files %{python_files}
%doc CHANGELOG.md README.rst
%license ../../LICENSE
%dir %{python_sitelib}/opencensus
%dir %{python_sitelib}/opencensus/ext
%{python_sitelib}/opencensus/ext/azure
%{python_sitelib}/opencensus_ext_azure-%{version}*-info

%changelog
