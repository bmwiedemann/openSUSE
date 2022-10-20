#
# spec file for package python-opencensus-context
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


%define repo_version 0.11.0
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-opencensus-context
Version:        0.1.3
Release:        0
Summary:        Python in-process context propogation
License:        Apache-2.0
URL:            https://github.com/census-instrumentation/opencensus-python
Source:         https://github.com/census-instrumentation/opencensus-python/archive/v%{repo_version}.tar.gz#/opencensus-%{repo_version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module contextvars if (%python-base >= 3.6 and %python-base < 3.7)}
%if 0%{python_version_nodots} == 36
Requires:       python-contextvars
%endif
BuildArch:      noarch
%python_subpackages

%description
The OpenCensus Runtime Context provides in-process context propagation.
By default, thread local storage is used for Python 2.7, 3.4 and 3.5;
contextvars is used for Python >= 3.6, which provides asyncio support.

%prep
%setup -q -n opencensus-python-%{repo_version}/context/opencensus-context
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
}

%check
%pyunittest -v

%files %{python_files}
%doc CHANGELOG.md README.rst
%license ../../LICENSE
%dir %{python_sitelib}/opencensus
%dir %{python_sitelib}/opencensus/common/
%{python_sitelib}/opencensus/common/runtime_context
%{python_sitelib}/opencensus_context-%{version}*-info

%changelog
