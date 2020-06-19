#
# spec file for package python-google-cloud-storage
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-google-cloud-storage
Version:        1.29.0
Release:        0
Summary:        Google Cloud Storage API python client library
License:        Apache-2.0
URL:            https://github.com/GoogleCloudPlatform/google-cloud-python
Source:         https://files.pythonhosted.org/packages/source/g/google-cloud-storage/google-cloud-storage-%{version}.tar.gz
BuildRequires:  %{python_module google-auth >= 1.11.0}
BuildRequires:  %{python_module google-cloud-core >= 1.2.0}
BuildRequires:  %{python_module google-resumable-media >= 0.5.0}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-google-auth >= 1.11.0
Requires:       python-google-cloud-core >= 1.2.0
Requires:       python-google-resumable-media >= 0.5.0
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
# skipped tests need the credentials set up
%pytest tests/unit -k 'not (test_conformance_post_policy or test_get_signed_policy_v4 or test_create)'

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/*

%changelog
