#
# spec file for package python-google-cloud-translate
#
# Copyright (c) 2023 SUSE LLC
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
%define skip_python2 1
Name:           python-google-cloud-translate
Version:        3.11.0
Release:        0
Summary:        Google Cloud Translation API client library
License:        Apache-2.0
URL:            https://github.com/googleapis/python-translate
Source:         https://files.pythonhosted.org/packages/source/g/google-cloud-translate/google-cloud-translate-%{version}.tar.gz
BuildRequires:  %{python_module google-api-core >= 1.34.0}
BuildRequires:  %{python_module google-cloud-core >= 1.3.0}
BuildRequires:  %{python_module proto-plus >= 1.22.2}
BuildRequires:  %{python_module protobuf >= 3.19.5}
BuildRequires:  %{python_module setuptools}
# START TESTING SECTION
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest}
# END TESTING SECTION
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-google-api-core >= 1.34.0
Requires:       python-google-cloud-core >= 1.3.0
Requires:       python-proto-plus >= 1.22.2
Requires:       python-protobuf >= 3.19.5
BuildArch:      noarch
%python_subpackages

%description
With `Google Cloud Translation`_, you can dynamically translate text between
thousands of language pairs. The Google Cloud Translation API lets websites
and programs integrate with Google Cloud Translation programmatically.

%prep
%autosetup -p1 -n google-cloud-translate-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest tests/unit -k 'not test_extra_headers'

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
