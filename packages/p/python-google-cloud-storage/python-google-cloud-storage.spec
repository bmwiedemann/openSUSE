#
# spec file for package python-google-cloud-storage
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


%define skip_python2 1

%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-google-cloud-storage
Version:        2.2.1
Release:        0
Summary:        Google Cloud Storage API python client library
License:        Apache-2.0
URL:            https://github.com/googleapis/python-storage
Source:         https://files.pythonhosted.org/packages/source/g/google-cloud-storage/google-cloud-storage-%{version}.tar.gz
# PATCH-FIX-UPSTREAM no-relative-imports.patch bsc#[0-9]+ mcepl@suse.com
# fix relative imports
Patch2:         no-relative-imports.patch
BuildRequires:  %{python_module google-api-core >= 1.31.5}
BuildRequires:  %{python_module google-auth >= 1.25.0}
BuildRequires:  %{python_module google-cloud-core >= 1.6.0}
BuildRequires:  %{python_module google-resumable-media >= 2.3.2}
BuildRequires:  %{python_module mock >= 3.0.0}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests >= 2.18.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-google-api-core >= 1.31.5
Requires:       python-google-auth >= 1.25.0
Requires:       python-google-cloud-core >= 1.6.0
Requires:       python-google-resumable-media >= 2.3.2
Requires:       python-googleapis-common-protos
Requires:       python-requests >= 2.18.0
BuildArch:      noarch
%python_subpackages

%description
Google Cloud Storage allows you to store data on Google
infrastructure with very high reliability, performance and
availability, and can be used to distribute large data objects
to users via direct download. This package provides client to it.

%prep
%autosetup -p1 -n google-cloud-storage-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export PYTEST_ADDOPTS="--import-mode=importlib"
%pytest tests/unit -k 'not network'

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/*

%changelog
