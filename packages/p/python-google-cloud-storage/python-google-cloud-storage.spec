#
# spec file for package python-google-cloud-storage
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-google-cloud-storage
Version:        1.15.1
Release:        0
Summary:        Google Cloud Storage API client library
License:        Apache-2.0
Group:          Development/Languages/Python
Url:            https://github.com/GoogleCloudPlatform/google-cloud-python
Source:         https://files.pythonhosted.org/packages/source/g/google-cloud-storage/google-cloud-storage-%{version}.tar.gz
BuildRequires:  %{python_module google-api-core >= 1.6.1}
BuildRequires:  %{python_module google-cloud-core >= 0.29.0}
BuildRequires:  %{python_module google-cloud-kms >= 1.0.0}
BuildRequires:  %{python_module google-resumable-media >= 0.3.1}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-google-api-core >= 1.6.1
Requires:       python-google-cloud-core >= 0.29.0
Recommends:     python-google-cloud-kms >= 1.0.0
Requires:       python-google-resumable-media >= 0.3.1
BuildArch:      noarch

%python_subpackages

%description
Python Client for Google Cloud Storage

%prep
%setup -q -n google-cloud-storage-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Disable system tests which do not work without additional tokens
rm tests/system.py
#%%python_exec setup.py test
%pytest -k "not test_extra_headers"

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/*

%changelog
