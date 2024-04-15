#
# spec file for package python-google-cloud-translate
#
# Copyright (c) 2024 SUSE LLC
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


%{?sle15_python_module_pythons}
Name:           python-google-cloud-translate
Version:        3.15.3
Release:        0
Summary:        Google Cloud Translation API client library
License:        Apache-2.0
URL:            https://github.com/googleapis/google-cloud-python
Source:         https://files.pythonhosted.org/packages/source/g/google-cloud-translate/google-cloud-translate-%{version}.tar.gz
BuildRequires:  %{python_module google-api-core >= 1.34.1}
BuildRequires:  %{python_module google-auth}
BuildRequires:  %{python_module google-cloud-core >= 1.4.4}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module proto-plus >= 1.22.3}
BuildRequires:  %{python_module protobuf >= 3.19.5}
BuildRequires:  %{python_module wheel}
# START TESTING SECTION
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest}
# END TESTING SECTION
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-google-api-core >= 1.34.1
Requires:       python-google-auth
Requires:       python-google-cloud-core >= 1.4.4
Requires:       python-proto-plus >= 1.22.3
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
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest tests/unit -k 'not test_extra_headers'

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/google/cloud/translate*
%{python_sitelib}/google_cloud_translate-%{version}.dist-info

%changelog
