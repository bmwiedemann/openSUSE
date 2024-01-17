#
# spec file for package python-opencensus-ext-threading
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


%define repo_version 0.7.12
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%bcond_without python2
Name:           python-opencensus-ext-threading
Version:        0.1.2
Release:        0
Summary:        OpenCensus threading Integration
License:        Apache-2.0
URL:            https://github.com/census-instrumentation/opencensus-python
Source:         https://github.com/census-instrumentation/opencensus-python/archive/v%{repo_version}.tar.gz#/opencensus-%{repo_version}.tar.gz
# PATCH-FIX-UPSTREAM remove-mock.patch gh#census-instrumentation/opencensus-python#1002
Patch0:         remove-mock.patch
BuildRequires:  %{python_module opencensus}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
%if %{with python2}
BuildRequires:  python-futures
BuildRequires:  python-mock
%endif
BuildRequires:  python-rpm-macros
Requires:       python-opencensus
BuildArch:      noarch
%ifpython2
Requires:       python-futures
%endif
%python_subpackages

%description
OpenCensus threading Integration

%prep
%setup -q -n opencensus-python-%{repo_version}/contrib/opencensus-ext-threading
pushd ../..
%patch0 -p1
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
%pyunittest discover -v

%files %{python_files}
%doc CHANGELOG.md README.rst
%license ../../LICENSE
%{python_sitelib}/*

%changelog
