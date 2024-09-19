#
# spec file for package python-google-ai-generativelanguage
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
Name:           python-google-ai-generativelanguage
Version:        0.6.6
Release:        0
Summary:        Google Ai Generativelanguage API client library
License:        Apache-2.0
URL:            https://github.com/googleapis/google-cloud-python/tree/main/packages/google-ai-generativelanguage
Source:         https://files.pythonhosted.org/packages/source/g/google-ai-generativelanguage/google-ai-generativelanguage-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
# SECTION test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module google-api-core >= 1.34.1}
BuildRequires:  %{python_module google-auth >= 2.14.1}
BuildRequires:  %{python_module proto-plus >= 1.22.3}
BuildRequires:  %{python_module protobuf >= 3.19.5}
# /SECTION
BuildRequires:  fdupes
Requires:       python-google-api-core >= 1.34.1
Requires:       python-google-auth >= 2.14.1
Requires:       python-proto-plus >= 1.22.3
Requires:       python-protobuf >= 3.19.5
BuildArch:      noarch
%python_subpackages

%description
Google Ai Generativelanguage API client library.

%prep
%autosetup -p1 -n google-ai-generativelanguage-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest -v

%files %{python_files}
%{python_sitelib}/google
%{python_sitelib}/google_ai_generativelanguage-%{version}.dist-info

%changelog
