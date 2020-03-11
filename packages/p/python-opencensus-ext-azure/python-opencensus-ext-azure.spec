#
# spec file for package python-opencensus-ext-azure
#
# Copyright (c) 2020 SUSE LLC
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


%define repo_version 0.7.7
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-opencensus-ext-azure
Version:        1.0.2
Release:        0
Summary:        OpenCensus Azure Monitor Exporters
License:        Apache-2.0
URL:            https://github.com/census-instrumentation/opencensus-python
Source:         https://github.com/census-instrumentation/opencensus-python/archive/v%{repo_version}.tar.gz#/opencensus-%{repo_version}.tar.gz
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module opencensus}
BuildRequires:  %{python_module psutil}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
OpenCensus Azure Monitor Exporters

%prep
%setup -q -n opencensus-python-%{repo_version}/contrib/opencensus-ext-azure
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
%{python_sitelib}/*

%changelog
